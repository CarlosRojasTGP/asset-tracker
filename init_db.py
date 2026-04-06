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
                serial="1003-1409",
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
            ),
            Device(
                id="34-20-002R",
                name="20' Sea Container 2",
                owner="TGP Logistics",
                serial="1016092",
                model="20' Sea Container",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="34-20-003R",
                name="20' Sea Container 3",
                owner="TGP Logistics",
                serial="IPXU 3707255",
                model="20' Sea Container",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="24-20-002R",
                name="20' Boxx Modular Office Trailer on Wheels 2",
                owner="TGP Logistics",
                serial="OSW102020MF01709",
                model="10 x 20 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="37-12-002",
                name="0.5 Hammer Drill-Driver 3",
                owner="TGP Logistics",
                serial="M64AF241416936",
                model="2904-20",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="34-20-004R",
                name="20' Sea Container 4",
                owner="TGP Logistics",
                serial="KKTU7545598",
                model="20' Sea Container",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="24-32-002R",
                name="32' Boxx Modular Office Trailer on Wheels 2",
                owner="TGP Logistics",
                serial="OSW103221MF01876",
                model="10 x 32 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="25-25-004R",
                name="25 KVA Generator with Ground Plate 1",
                owner="TGP Logistics",
                serial="WNMG0201VM0000809",
                model="G25",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="18-10-004R",
                name="1000L Fuel Cube 1",
                owner="TGP Logistics",
                serial="G43469831",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="24-10-004R",
                name="Double Restroom Trailer",
                owner="TGP Logistics",
                serial="1003-689",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2025-07-08 13:56:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CCAN-001R",
                name="10' Sea Container 5",
                owner="TGP Logistics",
                serial=" -",
                model=" -",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CCAN-002R",
                name="10' Sea Container 6",
                owner="TGP Logistics",
                serial=" -",
                model=" -",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CCAN-006R",
                name="10' Sea Container 7",
                owner="TGP Logistics",
                serial=" -",
                model=" -",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CUBE-001R",
                name="1000L Fuel Cube 115V with 20' Fuel Feed Return Hose 3",
                owner="TGP Logistics",
                serial="24009019",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CUBE-002R",
                name="1000L Fuel Cube 115V with 20' Fuel Feed Return Hose 4",
                owner="TGP Logistics",
                serial="19003593",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CUBE-003R",
                name="1000L Fuel Cube with Fuel Transfer Pump ( Electric ) 2",
                owner="TGP Logistics",
                serial="24008011",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="WASH-007R",
                name="10X24 Washroom Male/Female 1",
                owner="TGP Logistics",
                serial="LV10240416MF00254",
                model=" -",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="BOXX-006R",
                name="10X32 Office Trailer 1",
                owner="TGP Logistics",
                serial="MU103217NRB00821",
                model="10X32",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="BOXX-007R",
                name="10X32 Office Trailer 2",
                owner="TGP Logistics",
                serial="OSW103219NI01280",
                model="10X32",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="GEN-007R",
                name="125 KVA Diesel Generator 1",
                owner="TGP Logistics",
                serial="B220040803",
                model="C100D2RE",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="BOXX-009R",
                name="12X60 Boxx Modular Office Trailer on Wheels 1",
                owner="TGP Logistics",
                serial="OSW126019N101110",
                model="12X60",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="BOXX-001R",
                name="20' Boxx Modular Office Trailer on Wheels 3",
                owner="TGP Logistics",
                serial="0SW102018N101051",
                model="10 x 20 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="BOXX-003R",
                name="20' Boxx Modular Office Trailer on Wheels 4",
                owner="TGP Logistics",
                serial="OSW102020MF01709",
                model="10 x 20 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CCAN-003R",
                name="20' Sea Container 5",
                owner="TGP Logistics",
                serial="Cooper252",
                model="20' Sea Container",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CCAN-004R",
                name="20' Sea Container 6",
                owner="TGP Logistics",
                serial="1016092",
                model="20' Sea Container",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CCAN-005R",
                name="20' Sea Container 7",
                owner="TGP Logistics",
                serial="KKTU7545598",
                model="20' Sea Container",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CCAN-007R",
                name="20' Sea Container 8",
                owner="TGP Logistics",
                serial="IPXU 3707255",
                model="20' Sea Container",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CUBE-004R",
                name="2000L Fuel Cube 1",
                owner="TGP Logistics",
                serial="G43469831",
                model="10TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="CUBE-005R",
                name="2000L Fuel Cube 2",
                owner="TGP Logistics",
                serial="25000870",
                model="20TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-001R",
                name="25 KVA Diesel Generator (480V) with Ground Plate 3",
                owner="TGP Logistics",
                serial="48-000187",
                model=" -",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-002R",
                name="25 KVA Diesel Generator (480V) with Ground Plate 4",
                owner="TGP Logistics",
                serial="7161810",
                model="DCA-25SSIU4F",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-008R",
                name="25 KVA Diesel Generator (480V) with Ground Plate 5",
                owner="TGP Logistics",
                serial="24548605",
                model="G25",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-003R",
                name="25 KVA Diesel Generator with Ground Plate 2",
                owner="TGP Logistics",
                serial="WNMG0201CM0003359 ",
                model=" -",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-005R",
                name="25 KVA Diesel Generator with Ground Plate 3",
                owner="TGP Logistics",
                serial="24501964",
                model="G25",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-004R",
                name="25 KVA Generator with Ground Plate 2",
                owner="TGP Logistics",
                serial="WNMG0201VM0000809",
                model="G25",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-009R",
                name="25KW Generator with Fuel Cube 1",
                owner="TGP Logistics",
                serial="3013508245",
                model="MDG25IF4",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LIFT-001R",
                name="26 Ft RT Scissor Lift 1",
                owner="TGP Logistics",
                serial="37012138",
                model=" -",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="BOXX-002R",
                name="32' Boxx Modular Office Trailer on Wheels 3",
                owner="TGP Logistics",
                serial="MU10320717NRB00809",
                model="10 x 32 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="BOXX-004R",
                name="32' Boxx Modular Office Trailer on Wheels 4",
                owner="TGP Logistics",
                serial="OSW103221MF01876",
                model="10 x 32 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="BOXX-005R",
                name="32' Boxx Modular Office Trailer on Wheels 5",
                owner="TGP Logistics",
                serial="OSW103220MF01721",
                model="10 x 32 Mobile Office",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="BOXX-008R",
                name="32' Boxx Modular Office Trailer on Wheels 6",
                owner="TGP Logistics",
                serial="OSW103221MF01935",
                model="10X32",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="PANEL-001R",
                name="400 Amp Disconnect",
                owner="TGP Logistics",
                serial="G1630575",
                model="DB400LP-AW-S3",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-010R",
                name="45 KW Generator ",
                owner="TGP Logistics",
                serial="3014755799",
                model="MMG45IF4",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GARD-001",
                name="4X6 Guardhouse 1",
                owner="TGP Logistics",
                serial="-",
                model="4X6 Guardhouse",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GARD-002",
                name="4X6 Guardhouse 2",
                owner="TGP Logistics",
                serial="-",
                model="4X6 Guardhouse",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GARD-003",
                name="4X6 Guardhouse 3",
                owner="TGP Logistics",
                serial="-",
                model="4X6 Guardhouse",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GARD-004",
                name="4X6 Guardhouse 4",
                owner="TGP Logistics",
                serial="-",
                model="4X6 Guardhouse",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GEN-006R",
                name="50 KVA Generator with Ground Plate 1",
                owner="TGP Logistics",
                serial="WNMG0203JM0000517",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-001R",
                name="6 KW Diesel Light Tower 1",
                owner="TGP Logistics",
                serial="37-001840",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-010R",
                name="6 KW Diesel Light Tower 10",
                owner="TGP Logistics",
                serial="37-002869",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-011R",
                name="6 KW Diesel Light Tower 11",
                owner="TGP Logistics",
                serial="47-000270",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-012R",
                name="6 KW Diesel Light Tower 12",
                owner="TGP Logistics",
                serial="37-002304",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-013R",
                name="6 KW Diesel Light Tower 13",
                owner="TGP Logistics",
                serial="47-003784",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-014R",
                name="6 KW Diesel Light Tower 14",
                owner="TGP Logistics",
                serial="37-002304",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-015R",
                name="6 KW Diesel Light Tower 15",
                owner="TGP Logistics",
                serial="47-001852",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-016R",
                name="6 KW Diesel Light Tower 16",
                owner="TGP Logistics",
                serial="47-003713",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-002R",
                name="6 KW Diesel Light Tower 2",
                owner="TGP Logistics",
                serial="WNCLTV04HPUM00649",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-003R",
                name="6 KW Diesel Light Tower 3",
                owner="TGP Logistics",
                serial="3010678466",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-004R",
                name="6 KW Diesel Light Tower 4",
                owner="TGP Logistics",
                serial="37-001742",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-005R",
                name="6 KW Diesel Light Tower 5",
                owner="TGP Logistics",
                serial="37-003563",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-006R",
                name="6 KW Diesel Light Tower 6",
                owner="TGP Logistics",
                serial="39-001909",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-007R",
                name="6 KW Diesel Light Tower 7",
                owner="TGP Logistics",
                serial="37-000753",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-008R",
                name="6 KW Diesel Light Tower 8",
                owner="TGP Logistics",
                serial="WUX914984",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="LT-009R",
                name="6 KW Diesel Light Tower 9",
                owner="TGP Logistics",
                serial="3013359656",
                model="6KW Diesel Light Tower",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GARD-001R",
                name="8X10 Ft Guardhouse for OV1 /NFS 1",
                owner="TGP Logistics",
                serial="CWWU0235633",
                model="10' SC",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GARD-002R",
                name="8X10 Ft Guardhouse for OV1 /NFS 2",
                owner="TGP Logistics",
                serial="-",
                model="10AO",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="SKID-003R",
                name="Backhoe Loader Rental 1",
                owner="TGP Logistics",
                serial="JJGN58SNPNC780434",
                model="580SN",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="SKID-003RA",
                name="Backhoe Plow Blade Attachment 1",
                owner="TGP Logistics",
                serial="X52887",
                model="SP08B",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="WASH-001R",
                name="Double Restroom Trailer 2",
                owner="TGP Logistics",
                serial="1003-1409",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="WASH-002R",
                name="Double Restroom Trailer 3",
                owner="TGP Logistics",
                serial="1003-1032",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="WASH-003R",
                name="Double Restroom Trailer 4",
                owner="TGP Logistics",
                serial="1003-045",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="WASH-004R",
                name="Double Restroom Trailer 5",
                owner="TGP Logistics",
                serial="1003-689",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="WASH-005R",
                name="Double Restroom Trailer 6",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="WASH-006R",
                name="Double Restroom Trailer 7",
                owner="TGP Logistics",
                serial="1003-129",
                model="1003",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="WASH-008R",
                name="Double Restroom Trailer 8",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="CUBE-006R",
                name="Fuel  Cube 2000L with Fuel Transfer Pump 1",
                owner="TGP Logistics",
                serial="OKPA201492",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="CUBE-010R",
                name="Fuel Cube 1000L 1",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="CUBE-008R",
                name="Fuel Cube 2000L 2",
                owner="TGP Logistics",
                serial="16001899",
                model="20TCG-GLB",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="CUBE-009R",
                name="Fuel Cube 250-300 Galloon Diesel 1",
                owner="TGP Logistics",
                serial="22011980",
                model="10TCG-UR-CA-12V",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="CUBE-007R",
                name="Fuel Cube 500 Gal  tied to 125KVA Generator 1",
                owner="TGP Logistics", #owner will always be tgp
                serial="F96546016",
                model="20TCG-UR-CA-12V",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="HYB-001R",
                name="Hybrid Comfort Station 1",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="HYB-002R",
                name="Hybrid Comfort Station 2",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="HYB-003R",
                name="Hybrid Comfort Station 3",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="HYB-004R",
                name="Hybrid Comfort Station 4",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="HYB-005R",
                name="Hybrid Comfort Station 5",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="HYB-006R",
                name="Hybrid Comfort Station 6",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="HYB-007R",
                name="Hybrid Comfort Station 7",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="SALT-001",
                name="Salt Spreader 1",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="SALT-002",
                name="Salt Spreader 2",
                owner="TGP Logistics",
                serial="-",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),

            Device(
                id="SKID-004RA",
                name="Salt Spreader attachment for Skidsteer 2",
                owner="TGP Logistics",
                serial="AC1N03897",
                model="Salt Spreader",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="SKID-001R",
                name="Tracked Skidsteer with forks and bucket 1",
                owner="TGP Logistics",
                serial="408012075",
                model="TL8R2-CR",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="SKID-002R",
                name="Tracked Skidsteer with forks and bucket 2",
                owner="TGP Logistics",
                serial="410005148",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="SKID-004R",
                name="Tracked Skidsteer with forks and bucket 3",
                owner="TGP Logistics",
                serial="B5FF11036",
                model="T650",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),
            Device(
                id="WASH-007RA",
                name="Waste Containment and Fresh Water 1",
                owner="TGP Logistics",
                serial="CN08200917DS00065",
                model="-",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            )
        ]
        db.session.add_all(sample_devices)
        db.session.commit()
        print("Database initialized with sample devices.")
    else:
        print("Database already initialized.")
