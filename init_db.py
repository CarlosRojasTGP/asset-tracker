from models import db, Device
from app import app
from datetime import datetime

### Note: the ID is the equipment number ###
### Note: GPS-003 GPS Rover and GPS-003 CS20 Field Controller share ID and SERIAL ###

with app.app_context():
    db.create_all()
    print("Database tables created successfully.") #to know when it was created

    if not Device.query.first():
        sample_devices = [
            Device(
                id="31538416",
                name="P40-01 Outdoor LiDAR Scan & TS",
                owner="TGP",
                serial="1852705",
                model="ScanStation P40",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:54:48", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31036861",
                name="AP-001 Auto Pole",
                owner="TGP",
                serial="574104",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 14:07:36", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31036808",
                name="AP-002 Auto Pole",
                owner="TGP",
                serial="574051",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31100393",
                name="AP-003 Auto Pole",
                owner="TGP",
                serial="574446",
                model="AP20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31305203",
                name="GPS-001 GPS Rover",
                owner="TGP",
                serial="4906024",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31313793",
                name="GPS-001 CS20 Field Controller",
                owner="TGP",
                serial="2467956",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31305206",
                name="GPS-002 GPS Rover",
                owner="TGP",
                serial="4906027",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31075304",
                name="GPS-002 CS20 Field Controller",
                owner="TGP",
                serial="2467852",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31321958ROVER",
                name="GPS-003 GPS Rover",
                owner="TGP",
                serial="2467993",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31321958FIELDCONTROLLER",
                name="GPS-003 CS20 Field Controller",
                owner="TGP",
                serial="2467993",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31307411",
                name="GPS-004 GPS Rover",
                owner="TGP",
                serial="4906046",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478314",
                name="GPS-004 CS20 Field Controller",
                owner="TGP",
                serial="4581248",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31305216",
                name="GPS-005 GPS Rover",
                owner="TGP",
                serial="4906037",
                model="GS18 T",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478318",
                name="GPS-005 CS20 Field Controller",
                owner="TGP",
                serial="4581252",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31237232",
                name="TS16-001 Total Station",
                owner="TGP",
                serial="3018484",
                model="TS16 I 1'' R500",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31075281",
                name="TS16-001 CS20 Field Controller",
                owner="TGP",
                serial="2467829",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31264416",
                name="TS60-001 Total Station",
                owner="TGP",
                serial="897434",
                model="TS60 I 0.5'' R1000",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31075305",
                name="TS60-001 CS20 Field Controller",
                owner="TGP",
                serial="2467853",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31522152",
                name="TS60-002 Total Station",
                owner="TGP",
                serial="898960",
                model="TS60 I 0.5'' R1000",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478315",
                name="TS60-002 CS20 Field Controller",
                owner="TGP",
                serial="4581249",
                model="CS20 LTE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31062662",
                name="LEV-001 Digital Level",
                owner="TGP",
                serial="711184",
                model="LS15 0.2mm AF",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31478131",
                name="LEV-002 Digital Level",
                owner="TGP",
                serial="712255",
                model="LS15 0.2mm AF",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="Cthrue",
                name="SCN-001 Concrete Scanner",
                owner="TGP",
                serial="010-24-000429",
                model="Cthrue",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="MAGGIE",
                name="Magnetic Locator",
                owner="TGP",
                serial="452156",
                model="MAGGIE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="31471889",
                name="RTC360-01 Indoor LiDAR Scanner",
                owner="TGP",
                serial="2989411",
                model="RT360 3D Laser Scanner",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-12-001",
                name="0.5 Hammer Drill-Driver 1",
                owner="TGP Logistics",
                serial="M64AM240534185",
                model="2904-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-14-002",
                name="0.25 Impact Driver 1",
                owner="TGP Logistics",
                serial="M67AM240537319",
                model="2953-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-12-003",
                name="0.5 Hammer Drill-Driver 2",
                owner="TGP Logistics",
                serial="M64AF233801571",
                model="2904-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-14-004",
                name="0.25 Impact Driver 2",
                owner="TGP Logistics",
                serial="M67AF233803678",
                model="2953-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-10-005",
                name="1'' Rotary Hammer 1",
                owner="TGP Logistics",
                serial="L85BD243501779",
                model="2912-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-10-006",
                name="1'' Rotary Hammer 2",
                owner="TGP Logistics",
                serial="L85BD240204015",
                model="2912-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="DISTO-001",
                name="Disto P2P Distance Meter 1",
                owner="TGP Logistics",
                serial="2441860895",
                model="Disto X6",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="DISTO-002",
                name="Disto P2P Distance Meter 2",
                owner="TGP Logistics",
                serial="2440651102",
                model="Disto X6",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="DISTO-003",
                name="Disto P2P Distance Meter 3",
                owner="TGP Logistics",
                serial="2441950442",
                model="Disto X6",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-10-007",
                name="10'' Dual Bevel Sliding Compound Miter Saw",
                owner="TGP Logistics",
                serial="H17A9250905710S",
                model="2734-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="25-25-001R",
                name="25 KVA Diesel Generator with Ground Plate",
                owner="TGP Logistics",
                serial="9950699",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="18-10-001R",
                name="1000L Fuel Cube with Fuel Transfer Pump ( Electric )",
                owner="TGP Logistics",
                serial="24008011",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="34-10-001R",
                name="10' Sea Container 1",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="34-10-002R",
                name="10' Sea Container 2",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="25-25-002R",
                name="25 KVA Diesel Generator (480V) with Ground Plate 1",
                owner="TGP Logistics",
                serial="48-000187",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="18-10-002R",
                name="1000L Fuel Cube 115V with 20' Fuel Feed Return Hose 1",
                owner="TGP Logistics",
                serial="24009019",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="34-10-003R",
                name="10' Sea Container 3",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="34-10-004R",
                name="10' Sea Container 4",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="25-25-003R",
                name="25 KVA Diesel Generator (480V) with Ground Plate 2",
                owner="TGP Logistics",
                serial="7161810",
                model="DCA-25SSIU4F",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="18-10-003R",
                name="1000L Fuel Cube 115V with 20' Fuel Feed Return Hose 2",
                owner="TGP Logistics",
                serial="21010859",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="34-20-001R",
                name="20' Sea Container",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="24-20-001R",
                name="20' Boxx Modular Office Trailer on Wheels",
                owner="TGP Logistics",
                serial="0SW102018N101051",
                model="10 x 20 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="24-32-001R",
                name="32' Boxx Modular Office Trailer on Wheels",
                owner="TGP Logistics",
                serial="MU10320717NRB00809",
                model="10 x 32 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="24-10-001R",
                name="Portable Restroom 1",
                owner="TGP Logistics",
                serial="2T9GWCFL9R1208664",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="24-10-002R",
                name="Portable Restroom 2",
                owner="TGP Logistics",
                serial="1003-1032",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-10-008",
                name="5'' Grinder",
                owner="TGP Logistics",
                serial="L64BF241001404",
                model="2880-20",
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
