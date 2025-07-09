from models import db, Device
from app import app
from datetime import datetime

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")

    if not Device.query.first():
        sample_devices = [
            Device(
                id="TGP-LAPTOP-001",
                name="Laptop #1",
                serial="LAPTOP12345",
                model="Test Model Jerry",
                status="Checked Out (Available)",
                last_user="Carlos2.0",
                last_updated=datetime.strptime("2025-07-08 13:54:48", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="TGP-PRINTER-002",
                name="Office Printer",
                serial="PRINTER12345",
                model="Test model Not Jerry",
                status="Checked Out (Available)",
                last_user="Carlos Test",
                last_updated=datetime.strptime("2025-07-08 14:07:36", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="TGP-MOUSE-003",
                name="Carlos' Mouse",
                serial="Mouse12345",
                model="Logi working well",
                status="Checked Out (Available)",
                last_user="Alo",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            )
        ]
        db.session.add_all(sample_devices)
        db.session.commit()
        print("Database initialized with sample devices.")
    else:
        print("Database already initialized.")
