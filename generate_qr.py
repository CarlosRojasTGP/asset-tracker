import qrcode
import json
import os
from datetime import datetime #import date time - not needed but important to keep format consistent across databases (specifically with init_db.py from documents >asset tracker)

# Load devices from devices.json
#with open("devices.json") as f:
   # devices = json.load(f)
class Device:
    def __init__(self, id, name, owner, serial, model, status, last_user, last_updated):
        self.id = id
        self.name = name
        self.owner = owner
        self.serial = serial
        self.model = model
        self.status = status
        self.last_user = last_user
        self.last_updated = last_updated

devices = [
    # example:
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
                name="10X24 Washroom Male-Female 1",
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
                name="8X10 Ft Guardhouse for OV1 -NFS 1",
                owner="TGP Logistics",
                serial="CWWU0235633",
                model="10' SC",
                status="Checked Out (Available)",
                last_user="No users in this session. See Microsoft List",
                last_updated=datetime.strptime("2026-03-03 13:12:12", "%Y-%m-%d %H:%M:%S")
            ),


            Device(
                id="GARD-002R",
                name="8X10 Ft Guardhouse for OV1 -NFS 2",
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
                owner="TGP Logistics",
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



# Folder to save QR codes
output_folder = "static\qrcodes"
os.makedirs(output_folder, exist_ok=True)

base_url = "https://asset-tracker-q5i0.onrender.com/device/"  # Updated to your Render app URL

# Generate QR for each device
for device in devices:
    url = base_url + device.id
    img = qrcode.make(url)
    filename = os.path.join(output_folder, f"{device.name}.png")
    img.save(filename)
    print(f"Saved QR code for {device.id} at {filename}")