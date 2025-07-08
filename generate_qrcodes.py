import qrcode
import json
import os

# Load devices from devices.json
with open("devices.json") as f:
    devices = json.load(f)

# Folder to save QR codes
output_folder = "static/qrcodes"
os.makedirs(output_folder, exist_ok=True)

base_url = "http://10.10.23.79:8080/device/"  # Change this if hosted elsewhere

for device_id in devices:
    url = base_url + device_id
    img = qrcode.make(url)
    filename = os.path.join(output_folder, f"{device_id}.png")
    img.save(filename)
    print(f"Saved QR code for {device_id} at {filename}")
