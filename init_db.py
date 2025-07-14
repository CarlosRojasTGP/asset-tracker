from models import db, Device
from app import app
from datetime import datetime

### Note: the ID is the equipment number ###
### Note: GPS-003 GPS Rover and GPS-003 CS20 Field Controller share ID and SERIAL ###

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")

    if not Device.query.first():
        sample_devices = [
            Device(
                id="31538416",
                name="P40-01 Outdoor LiDAR Scan & TS",
                owner="Some Owner Name",
                serial="1852705",
                model="ScanStation P40",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:54:48", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31036861",
                name="AP-001 Auto Pole",
                owner="Some Owner Name",
                serial="574104",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 14:07:36", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31036808",
                name="AP-002 Auto Pole",
                owner="Some Owner Name",
                serial="574051",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31100393",
                name="AP-003 Auto Pole",
                owner="Some Owner Name",
                serial="574446",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31305203",
                name="GPS-001 GPS Rover",
                owner="Some Owner Name",
                serial="4906024",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31313793",
                name="GPS-001 CS20 Field Controller",
                owner="Some Owner Name",
                serial="2467956",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31305206",
                name="GPS-002 GPS Rover",
                owner="Some Owner Name",
                serial="4906027",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31075304",
                name="GPS-002 CS20 Field Controller",
                owner="Some Owner Name",
                serial="2467852",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31321958ROVER",
                name="GPS-003 GPS Rover",
                owner="Some Owner Name",
                serial="2467993",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31321958FIELDCONTROLLER",
                name="GPS-003 CS20 Field Controller",
                owner="Some Owner Name",
                serial="2467993",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31307411",
                name="GPS-004 GPS Rover",
                owner="Some Owner Name",
                serial="4906046",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478314",
                name="GPS-004 CS20 Field Controller",
                owner="Some Owner Name",
                serial="4581248",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31305216",
                name="GPS-005 GPS Rover",
                owner="Some Owner Name",
                serial="4906037",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478318",
                name="GPS-005 CS20 Field Controller",
                owner="Some Owner Name",
                serial="4581252",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31237232",
                name="TS16-001 Total Station",
                owner="Some Owner Name",
                serial="3018484",
                model="TS16 I 1'' R500",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31075281",
                name="TS16-001 CS20 Field Controller",
                owner="Some Owner Name",
                serial="2467829",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31264416",
                name="TS60-001 Total Station",
                owner="Some Owner Name",
                serial="897434",
                model="TS60 I 0.5'' R1000",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31075305",
                name="TS60-001 CS20 Field Controller",
                owner="Some Owner Name",
                serial="2467853",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31522152",
                name="TS60-002 Total Station",
                owner="Some Owner Name",
                serial="898960",
                model="TS60 I 0.5'' R1000",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478315",
                name="TS60-002 CS20 Field Controller",
                owner="Some Owner Name",
                serial="4581249",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31062662",
                name="LEV-001 Digital Level",
                owner="Some Owner Name",
                serial="711184",
                model="LS15 0.2mm AF",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478131",
                name="LEV-002 Digital Level",
                owner="Some Owner Name",
                serial="712255",
                model="LS15 0.2mm AF",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="Cthrue",
                name="SCN-001 Concrete Scanner",
                owner="Some Owner Name",
                serial="010-24-000429",
                model="Cthrue",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="MAGGIE",
                name="Magnetic Locator",
                owner="Some Owner Name",
                serial="452156",
                model="MAGGIE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31471889",
                name="RTC360-01 Indoor LiDAR Scanner",
                owner="Some Owner Name",
                serial="2989411",
                model="RT360 3D Laser Scanner",
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
