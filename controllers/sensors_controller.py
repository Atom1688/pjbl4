# sensors_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors import Sensor
from models.iot.devices import Device
from models.db import db

sensor_ = Blueprint("sensor_", __name__, template_folder="views")

@sensor_.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor_.route('/sensors')
def sensors():
    sensors = Sensor.get_sensors()
    return render_template("sensors.html", sensors=sensors)

@sensor_.route('/add_sensor', methods=['POST'])
def add_sensor():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, topic, unit, is_active)
    
    sensors = Sensor.get_sensors()
    return render_template("sensors.html", sensors=sensors)

@sensor_.route('/edit_sensor/<int:id>', methods=['GET'])
def edit_sensor(id):
    sensor = Sensor.get_single_sensor(id)
    return render_template("update_sensor.html", sensors=[sensor])


@sensor_.route('/update_sensor', methods=['POST'])
def update_sensor():
    id = request.form.get("id")
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    sensor = Sensor.query.filter_by(id=id).first()
    if sensor:
        sensor.unit = unit
        sensor.topic = topic
        db.session.commit()

        device = Device.query.filter_by(id=sensor.devices_id).first()
        if device:
            device.name = name
            device.brand = brand
            device.model = model
            device.is_active = is_active
            db.session.commit()

    return redirect(url_for('sensor_.sensors'))



@sensor_.route('/del_sensor', methods=['GET'])
def del_sensor():
    id = request.args.get('id', None)
    Sensor.delete_sensor(id)
    
    sensors = Sensor.get_sensors()
    return render_template("sensors.html", sensors=sensors)