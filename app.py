from flask import Flask, render_template, abort, request
from datetime import datetime
from models import db, Device, History

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize db with app here

# === Routes ===

@app.route("/device/<device_id>")
def device_page(device_id):
    device = Device.query.get(device_id)
    if not device:
        abort(404)

    history = History.query.filter_by(device_id=device_id).order_by(History.timestamp.desc()).all()
    return render_template("device.html", device=device, device_id=device_id, history=history)

@app.route("/device/<device_id>/checkout", methods=["POST"])
def checkout_device(device_id):
    device = Device.query.get(device_id)
    if not device:
        abort(404)

    device.status = "Checked Out (Available)"
    device.last_updated = datetime.utcnow()

    db.session.add(device)
    db.session.add(History(device_id=device_id, action="checkout", user=device.last_user or "Unknown"))
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

    device.status = "In Use"
    device.last_user = user
    device.last_updated = datetime.utcnow()

    db.session.add(device)
    db.session.add(History(device_id=device_id, action="checkin", user=user))
    db.session.commit()
    return "", 204

@app.route("/")
def home():
    devices = Device.query.all()
    return render_template("index.html", devices={d.id: d for d in devices})

# === Deployment ===
import os
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)

