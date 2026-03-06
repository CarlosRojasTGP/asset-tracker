import csv

TEMPLATE = """
            Device(
                id="{id}",
                name="{name}",
                owner="{owner}",
                serial="{serial}",
                model="{model}",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
"""


with open("devices.csv", newline='', encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for item in reader:
        print(TEMPLATE.format(
            id =item["id"],
            name=item["name"],
            owner=item["owner"],
            serial=item["serial"],
            model=item["model"]
        ))