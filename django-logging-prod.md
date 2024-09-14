## Intro

Logging is as important as testing your app. Proper logging can save your hours if not days of trying to debug your application. 
From my own experience, I'll document how I implement logging for my `django apps` served by `apache` webserver.
Log configs are at your `settings.py` leevl so to avoid redudancy, I'll only include necessary script here for log configs. 
My major focus is how your logs are handled in production.
Lets get started...............

### Django Logging Levels
Django uses and extends the python logging module to perofm system logging. The python logging consist of four parts `loggers, Handlers, Filters and Formatters`

Want to learn more, here [logging](https://docs.djangoproject.com/en/5.1/topics/logging/)

Python loggers has the follwoing available logger levers at our disposa.
```go  
    DEBUG: Low level system information for debugging purposes
    INFO: General system information
    WARNING: Information describing a minor problem that has occurred.
    ERROR: Information describing a major problem that has occurred.
    CRITICAL: Information describing a critical problem that has occurred.
```
I should warn that, `DEBUG` is very verbose and therefore, the log size can grow huge taking up your disk space in production environment. Therefore, to reduce `verbosity` I highly recommend you use `INFO or WARNING` levels. `RotatingFileHandler` can be used to manage log file sizes automatically.

A  sample config file
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Retain default loggers

    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {name} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'appstore_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'appstore.log'),
            'maxBytes': 5 * 1024 * 1024,  # 5 MB
            'backupCount': 5,  # Keep up to 5 backup files
            'level': 'INFO',  # Set to INFO or WARNING
            'formatter': 'verbose',
        },
        'appstore_error_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'appstore_error.log'),
            'maxBytes': 5 * 1024 * 1024,  # 5 MB
            'backupCount': 5,
            'level': 'ERROR',  # Log only errors for DB queries
            'formatter': 'verbose',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['appstore_file'],
            'level': 'INFO',  # Change to INFO or WARNING
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['appstore_error_file'],
            'level': 'ERROR',  # Log only errors for DB queries
            'propagate': False,
        },
    },
}
```

### Breaking it Down

#### Handlers:
  - `RotatingFileHandler` manages log file sizes by rotating them once they reach a specified size` maxBytes`.
  - `backupCount` determines how many rotated log files to keep.
  - Separate handlers for _general logs_ (appstore_file) and _error logs_ (appstore_error_file) help in organizing logs efficiently.
### Loggers:
  - The `django` logger captures general application logs.
  - The `django.db.backends` logger captures database-related errors.
  
###  System-Level Log Rotation with logrotate

Its always a good idea to set up system-level log rotation to provide an additional layer of log management.
#### Create a Logrotate Configuration for Django Logs
##### Steps
1. Create Log Directory 
    `sudo mkdir -p /var/log/django`
    `sudo chown www-data:www-data /var/log/django`
    `sudo chmod 755 /var/log/django`
2. Move Existing Logs
   Move your existing appstore.log and appstore_error.log to the new directory.
   `sudo mv /home/appstore_admin/appstore/appstore.log /var/log/django/`
    `sudo mv /home/appstore_admin/appstore/appstore_error.log /var/log/django/`
##### Update the LOGGING configuration in settings.py accordingly
Since we've created our log dir, its good to point the filename to this new directory on your settings config.
    `'filename': '/var/log/django/appstore.log'`,
    `'filename': '/var/log/django/appstore_error.log'`,

3. Create Logrotate Configuration File
   Create a new file /etc/logrotate.d/django with the following content
   
   `/var/log/django/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 640 www-data www-data
    sharedscripts
    postrotate
        systemctl reload apache2 > /dev/null
    endscript
}`


### Breaking it Down ...

`daily`: Rotate logs daily.
`rotate 14`: Keep 14 days of logs.
`compress`: Compress old logs to save space.
`create 640`: Create new log files with specific permissions.
`postrotate`: Reload Apache to ensure it writes to the new log file after rotation.

4. Test Logrotate Configuration
`sudo logrotate -d /etc/logrotate.d/django`

manually force a rotation to ensure it works
`sudo logrotate -f /etc/logrotate.d/django`

###  Monitor Log File Sizes and Contents
Regular monitoring helps in identifying issues early and ensures that log files remain manageable.
Use Monitoring Tools:
1. Log Monitoring: Tools like ELK Stack (Elasticsearch, Logstash, Kibana), Graylog, or Splunk can help in centralizing and analyzing logs.
2. Alerting: Set up alerts to notify you when log files reach a certain size or when specific error patterns are detected.
#### Basic Monitoring Commands
1. Check Log File Sizes
   `du -h /var/log/django/*.log`
2. Tail Logs in Real-Time
  ` tail -f /var/log/django/appstore.log`
  ` tail -f /var/log/django/appstore_error.log`
3. Search for Frequent Errors
   `grep "Error: OrganizationUserProfile matching query does not exist" /var/log/django/appstore.log | wc -l`

### Ensure Proper Permissions and Ownership
Another common pain in the but is having insufficient permission especially for th apache user. Correct permissions ensure that your application can write to the log files without exposing them to unauthorized access.
##### Set Permissions
 `sudo chown www-data:www-data /var/log/django/appstore.log /var/log/django/appstore_error.log`
    `sudo chmod 640 /var/log/django/appstore.log /var/log/django/appstore_error.log`

#### Breakind dow the perms
   1. Owner: `www-data` (assuming this is your Apache user).
   2. Group: `www-data`.
   3. Permissions: `640` allows the owner to read/write, the group to read, and others have no access.
###  Analyze and Fix Frequent Errors
Frequent errors can lead to rapid log file growth and may indicate underlying issues in your application.
#### Example Error
`Error: OrganizationUserProfile matching query does not exist.`
##### Steps to Address
1. Identify the Source
    Locate where this error is being raised in your Django code.
    Investigate the Cause:

2. Determine why the` OrganizationUserProfile` is not found. It could be due to missing data, incorrect query parameters, or logic errors.

3. Implement Fixes
    Ensure that the necessary data exists.
    Handle cases where the profile might not exist gracefully to prevent repetitive error logging.
4. Update Logging Strategy:
    If this is an expected situation, consider logging it at a lower level (e.g., `WARNING`) instead of `ERROR`.

### Restart Apache to Apply Changes
`    sudo systemctl restart apache2`

### Optional: Use Asynchronous Logging
For high-performance applications, consider using asynchronous logging to prevent logging from blocking your application’s execution.
Using the `ConcurrentRotatingFileHandler`
Steps
`pip install ConcurrentLogHandler`
Update logging code
```python
'handlers': {
    'appstore_file': {
        'class': 'ConcurrentLogHandler.ConcurrentRotatingFileHandler',
        'filename': '/var/log/django/appstore.log',
        'maxBytes': 5 * 1024 * 1024,  # 5 MB
        'backupCount': 5,
        'level': 'INFO',
        'formatter': 'verbose',
    },
    # ... other handlers
},
```

...and thats it for now happy logging 😎...





