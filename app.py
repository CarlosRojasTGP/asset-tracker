from flask import Flask, render_template, abort, request
from datetime import datetime
import json
import os

HISTORY_FILE = "history.json"

app = Flask(__name__)

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


#Loading the sample-test devices from the devices.json.
def get_device_data(device_id):
    try:
        with open("devices.json") as f:
            devices = json.load(f)
        return devices.get(device_id)
    except Exception:
        return None

@app.route("/device/<device_id>")
def device_page(device_id):
    device = get_device_data(device_id)
    if not device:
        abort(404)

    history = [h for h in load_history() if h["device_id"] == device_id]

    # Optionally sort by timestamp descending (latest first)
    history.sort(key=lambda x: x["timestamp"], reverse=True)

    return render_template("device.html", device=device, device_id=device_id, history=history)

# Helper to load and save the devices.json file
def load_devices():
    with open("devices.json") as f:
        return json.load(f)

def save_devices(data):
    with open("devices.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/device/<device_id>/checkout", methods=["POST"])
def checkout_device(device_id):
    devices = load_devices()
    device = devices.get(device_id)
    if not device:
        abort(404)

    device["status"] = "Checked Out (Available)"
    device["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Appending to History
    history = load_history() 
    history.append({
        "device_id": device_id,
        "action": "checkout",
        "user": device.get("last_user", "Unknown"),
        "timestamp": device["last_updated"]
    })
    save_history(history)
    save_devices(devices)
    return "", 204  # No content, just success

@app.route("/device/<device_id>/checkin", methods=["POST"])
def checkin_device(device_id):
    devices = load_devices()
    device = devices.get(device_id)
    if not device:
        abort(404)

    user = request.json.get("user")
    if not user:
        abort(400)

    device["status"] = "In Use"
    device["last_user"] = user
    device["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history = load_history()
    history.append({
        "device_id": device_id,
        "action": "checkin",
        "user": user,
        "timestamp": device["last_updated"]
    })

    save_history(history)
    save_devices(devices)
    return "", 204

from waitress import serve

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
