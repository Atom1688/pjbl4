from models.db import db
from models.iot.devices import Device

class Actuators(db.Model):
    __tablename__ = 'actuators'
    id = db.Column(db.Integer, primary_key=True)
    devices_id = db.Column(db.Integer, db.ForeignKey('devices.id'))  
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    @staticmethod
    def save_actuators(name, brand, model, topic, unit, is_active):
        device = Device(name=name, brand=brand, model=model, is_active=is_active)
        db.session.add(device)
        db.session.commit()

        actuators = Actuators(devices_id=device.id, unit=unit, topic=topic)
        db.session.add(actuators)
        db.session.commit()

    @staticmethod
    def get_actuators():
        actuators = Actuators.query.join(Device, Device.id == Actuators.devices_id)\
            .add_columns(Device.id, Device.name,
                Device.brand, Device.model,
                Device.is_active, Actuators.topic,
                Actuators.unit).all()
    
        return actuators

    @staticmethod
    def get_single_actuator(id):
        actuator = Actuators.query.filter(Actuators.devices_id == id).first()
        if actuator is not None:
            actuator = Actuators.query.filter(Actuators.devices_id == id)\
                    .join(Device).add_columns(Device.id, Device.name, Device.brand,
                        Device.model, Device.is_active, Actuators.topic, Actuators.unit).first()

        return [actuator]

    @staticmethod
    def update_actuator(id, name, brand, model, topic, unit, is_active):
        actuator = Actuators.query.filter_by(id=id).first()
        if actuator:
            actuator.unit = unit
            actuator.topic = topic
            db.session.commit()

            device = Device.query.get(actuator.devices_id)
            if device:
                device.name = name
                device.brand = brand
                device.model = model
                device.is_active = is_active
                db.session.commit()

        actuators = Actuators.get_actuators()
        return actuators

    @staticmethod
    def delete_actuator(id):
        actuator = Actuators.query.filter(Actuators.devices_id == id).first()
        if actuator:
            db.session.delete(actuator)
            db.session.commit()
        
        device = Device.query.filter(Device.id == id).first()
        if device:
            db.session.delete(device)
            db.session.commit()

