from models import db, Device
from app import app
from datetime import datetime

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")

    if not Device.query.first():
        sample_devices = [
            Device(
                id="31538416",
                name="P40-01 Outdoor LiDAR Scan & TS",
                serial="1852705",
                model="ScanStation P40",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:54:48", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31036861",
                name="AP-001 Auto Pole",
                serial="574104",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 14:07:36", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31036808",
                name="AP-002 Auto Pole",
                serial="574051",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            )
        ]
        db.session.add_all(sample_devices)
        db.session.commit()
        print("Database initialized with sample devices.")
    else:
        print("Database already initialized.")
