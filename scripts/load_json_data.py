import json
import os
import django
from pathlib import Path

from apps.regions.models import County, Constituency, Ward

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MtaaAPI.settings")
django.setup()

json_path = Path(__file__).resolve().parent / "mtaaapi_data.json"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for row in data:
    county_code = row["county_code"].strip()
    county_name = row["county_name"].strip()
    constituency_code = row["constituency_code"].strip()
    constituency_name = row["constituency_name"].strip()
    ward_code = row["ward_code"].strip()
    ward_name = row["ward_name"].strip()

    # County
    county, _ = County.objects.get_or_create(code=county_code, defaults={"name": county_name})

    # Constituency
    constituency, _ = Constituency.objects.get_or_create(
        code=constituency_code,
        defaults={"name": constituency_name, "county": county}
    )

    # Ward
    Ward.objects.get_or_create(
        code=ward_code,
        defaults={"name": ward_name, "constituency": constituency}
    )

print("✅ Import completed successfully!")