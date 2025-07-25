import os
import csv
import json
from pathlib import Path

from collections import defaultdict

# input a csv file and output a json file
csv_path = Path(__file__).resolve().parent / "mtaaapi_data.csv"
json_path = Path(__file__).resolve().parent / "mtaaapi_data.json"

# def convert_csv_to_json(csv_file, json_file):
#     data = []
#     with open(csv_file, mode="r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             data.append({
#                 "county_code": row["County_Code"].strip(),
#                 "county_name": row["County_Name"].strip(),
#                 "constituency_code": row["Constituency_Code"].strip(),
#                 "constituency_name": row["Constituency_Name"].strip(),
#                 "ward_code": row["Ward_Code"].strip(),
#                 "ward_name": row["Ward_Name"].strip(),
#             })

#     with open(json_file, mode="w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4)

#     print(f"✅ Successfully converted {csv_file} to {json_file}")

# if __name__ == "__main__":
#     convert_csv_to_json(csv_path, json_path)

data = defaultdict(lambda: {
    "county_code": "",
    "county_name": "",
    "constituencies": defaultdict(lambda: {
        "const_code": "",
        "const_name": "",
        "wards": []
    })
})

# Read the CSV and build the hierarchy
with open(csv_path, newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(row.keys())
        # break
        county_code = row['County_Code'].strip()
        county_name = row['County_Name'].strip()
        const_code = row['Constituency_Code'].strip()
        const_name = row['Constituency_Name'].strip()
        ward_code = row['Ward_Code'].strip()
        ward_name = row['Ward_Name'].strip()

        # Set county and constituency info
        county = data[county_code]
        county['county_code'] = county_code
        county['county_name'] = county_name

        constituency = county['constituencies'][const_code]
        constituency['const_code'] = const_code
        constituency['const_name'] = const_name

        # Add ward
        constituency['wards'].append({
            "ward_code": ward_code,
            "ward_name": ward_name,
        })

# Convert defaultdicts to lists for JSON output
output = []
for county in data.values():
    county['constituencies'] = list(county['constituencies'].values())
    output.append(county)

# Write to JSON file
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Done! Output written to {os.path.abspath(json_path)}")
