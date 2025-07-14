from flask import Flask, render_template, abort, request, jsonify
from datetime import datetime
import pytz #for timezone
from pytz import timezone
from models import db, Device, History

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db' #sql lite which has some limitations
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     

db.init_app(app)  # Initialize db with app here

# Toronto timezone object (used consistently)
eastern = pytz.timezone("America/Toronto")

# === Routes ===
@app.route("/device/<device_id>")
def device_page(device_id):
    device = Device.query.get(device_id)
    if not device:
        abort(404)

    history = History.query.filter_by(device_id=device_id).order_by(History.timestamp.desc()).all()

    # Preparing formatted history list with fixed timezone
    history_display = []
    for record in history:


        timestamp = record.timestamp
        if timestamp.tzinfo is None:
    # Local naive timestamp is actually in Toronto time, so localize to Toronto :00000000
            timestamp = eastern.localize(timestamp)
# Now timestamp is timezone-aware in Toronto time, so format directly
        formatted_time = timestamp.strftime("%Y-%m-%d %I:%M %p")

        history_display.append({
            "timestamp": formatted_time,
            "action": record.action,
            "user": record.user
        })

    return render_template("device.html", device=device, device_id=device_id, history=history_display)

@app.route("/device/<device_id>/history.json")
def device_history_json(device_id):
    device = Device.query.get(device_id)
    if not device:
        abort(404)

    history = History.query.filter_by(device_id=device_id).order_by(History.timestamp.desc()).all()

    # Convert timestamps to readable strings
    result = [
        {
            "timestamp": h.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "action": h.action,
            "user": h.user
        } for h in history
    ]
    return {"device": device.name, "device_id": device_id, "history": result}




@app.route("/device/<device_id>/checkout", methods=["POST"])
def checkout_device(device_id):
    device = Device.query.get(device_id)
    if not device:
        abort(404)

    # timezone-aware Toronto time
    now = datetime.now(eastern)

    device.status = "Checked Out (Available)"
    device.last_updated = now

    db.session.add(device)
    db.session.add(History(device_id=device_id, action="checkout", user=device.last_user or "Unknown", timestamp=now))
    db.session.commit()
    return "", 204

@app.route("/device/<device_id>/checkin", methods=["POST"])
def checkin_device(device_id):
    device = Device.query.get(device_id)
    if not device:
        abort(404)

    user = request.json.get("user")
    if not user:
        abort(400)

    # timezone-aware Toronto time
    now = datetime.now(eastern)

    device.status = "In Use"
    device.last_user = user
    device.last_updated = now

    db.session.add(device)
    db.session.add(History(device_id=device_id, action="checkin", user=user, timestamp=now))
    db.session.commit()
    return "", 204

@app.route("/")
def home():
    devices = Device.query.all()
    return render_template("index.html", devices={d.id: d for d in devices})



@app.route("/history_all")
def get_all_history():
    history_records = History.query.order_by(History.timestamp.desc()).all()

    result = []
    for record in history_records:
        device = Device.query.get(record.device_id)
        result.append({
            "device_id": record.device_id,
            "device_name": device.name if device else "Unknown",  # ← ADD THIS
            "user": record.user,
            "action": record.action,
            "timestamp": record.timestamp.isoformat()
        })

    return jsonify(result)


# === Deploymentttt ===
import os
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)