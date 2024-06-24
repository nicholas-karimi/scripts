## Celery
Celery is a distributed task queue for UNIX systems.It can collect, record, schedule, and perform tasks outside of your main program. It allows you to offload work from your Python app. Once you integrate Celery into your app, you can send time-intensive tasks to Celery’s task queue.

## Message Broker
To receive tasks from your program and send results to a back end, Celery requires a message broker for communication. `Redis and RabbitMQ` are two message brokers that developers often use together with Celery.

### Services
three services to run at the same time:

1. Producer: Your Django app
2. Message Broker: The Redis server
3. Consumer: Your Celery app


## Run Celery in production
### Steps
1. Install Dependencies
   `pip install celery`
2. Choose a Message Broker. Common choices are RabbitMQ and Redis
Using redis
- Install redis on your server `sudo apt update && sudo apt install redis`
- Test redis
  `redis-server`
- Open redis cli
  `redis-cli`
- Test -> `ping` should give `pong` response.

- Instal redis on your project eivironment
  `pip install redis`

3. Configure Celery: Configure Celery in your Django project's settings.
```python
    # settings.py

    # Celery configuration
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
```

4. Define and Register Tasks
```python
    # tasks.py
    @shared_task
    def send_email_notification(domain):
        sleep(20)
        from_email = f"Konza Jitume Data  <{settings.EMAIL_HOST_USER}>"
        # email_to = email_to
        template = render_to_string("email/email_notification.html", {"domain": domain})
        subject = "Subject"
        text_content = "You have a new message"
        msg = EmailMultiAlternatives(subject, text_content, from_email, to=['example@example.com'])
        msg.attach_alternative(template, "text/html")
        msg.send()
```

5. Start Celery Workers
`celery -A your_project_name worker --loglevel=info`

6. Process Management. use a process manager like Supervisor to ensure that Celery workers are running continuously and automatically restart if they crash. Configure Supervisor to manage Celery workers.
    ### Install supervisor
    `sudo apt install supervisor`
    `pip install supervisor`
    ### Create a Celery Configuation
    On `/etc/supervisor/conf.d/`
    ```celery
    #celery.conf
    [program:celery]
    command=/path/to/your/venv/bin/celery -A your_project_name worker --loglevel=INFO
    directory=/path/to/your/django/project
    user=your_username
    numprocs=1
    stdout_logfile=/var/log/celery/worker.log
    stderr_logfile=/var/log/celery/worker.log
    autostart=true
    autorestart=true
    startsecs=10
    stopwaitsecs = 600
    stopasgroup=true
    ```
    ### Update Supervisor Configuration:
    update Supervisor's configuration and reload it:
    `sudo supervisorctl reread`
    `sudo supervisorctl update`

    ### Start Celery Worker:
    `sudo supervisorctl start celery`

    ### Verify Worker Status
    `sudo supervisorctl status`



7. Monitoring and Logging: Monitor Celery workers to ensure they're running smoothly. You can use tools like Flower for monitoring and logging to track task execution and diagnose issues.

### Posible Errors
> `ERROR: CANT_REREAD`: The directory named as part of the path /var/log/celery/worker.log does not exist. in section 'program:celery' (file: '/etc/supervisor/conf.d/clery.conf')

#### Solution
1. Create the `/var/log/celery/` Directory

    `sudo mkdir -p /var/log/celery/`

2. Set Permissions
Ensure that the directory has the appropriate permissions so that Supervisor can write to it
`sudo chown -R your_username:your_username /var/log/celery/`

3. Restart Supervisor
   `sudo supervisorctl restart all`

### Trouble installing postgres-pip?
Has this error haunted you?
>  ./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory?

Just install the required headers on your server/environment

`sudo apt-get install python3-dev libpq-dev`

### Using Flower
Extend your celery config and add the following 
```python
[program:flower]
command=/path/to/your/venv/bin/flower --port=5555  # Adjust port as needed
directory=/path/to/your/django/project
user=your_username
autostart=true
autorestart=true
startsecs=10
stdout_logfile=/var/log/flower.log
stderr_logfile=/var/log/flower.log
```
