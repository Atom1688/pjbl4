# sensors.py
from models.db import db
from models.iot.devices import Device

class Sensor(db.Model):
    __tablename__ = 'sensors'
    id = db.Column(db.Integer, primary_key=True)
    devices_id = db.Column(db.Integer, db.ForeignKey('devices.id'))  # Adiciona a chave estrangeira referindo-se a 'devices.id'
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    @staticmethod
    def save_sensor(name, brand, model, topic, unit, is_active):
        device = Device(name=name, brand=brand, model=model, is_active=is_active)
        db.session.add(device)
        db.session.commit()

        sensor = Sensor(devices_id=device.id, unit=unit, topic=topic)
        db.session.add(sensor)
        db.session.commit()

    @staticmethod
    def get_sensors():
        sensors = Sensor.query.join(Device, Device.id == Sensor.devices_id)\
            .add_columns(Device.id, Device.name,
                Device.brand, Device.model,
                Device.is_active, Sensor.topic,
                Sensor.unit).all()
    
        return sensors

    @staticmethod
    def get_single_sensor(id):
        sensor = Sensor.query.filter(Sensor.devices_id == id).first()
        if sensor is not None:
            sensor = Sensor.query.filter(Sensor.devices_id == id)\
                    .join(Device).add_columns(Device.id, Device.name, Device.brand,
                        Device.model, Device.is_active, Sensor.topic, Sensor.unit).first()

        return [sensor]

  
    @staticmethod
    def update_sensor(id, name, brand, model, topic, unit, is_active):
        sensor = Sensor.query.filter_by(id=id).first()
        if sensor:
            sensor.unit = unit
            sensor.topic = topic
            db.session.commit()

            device = Device.query.get(sensor.devices_id)
            if device:
                device.name = name
                device.brand = brand
                device.model = model
                device.is_active = is_active
                db.session.commit()

        sensors = Sensor.get_sensors()
        return sensors

    @staticmethod
    def delete_sensor(id):
        sensor = Sensor.query.filter(Sensor.devices_id == id).first()
        if sensor:
            db.session.delete(sensor)
            db.session.commit()
        
        device = Device.query.filter(Device.id == id).first()
        if device:
            db.session.delete(device)
            db.session.commit()