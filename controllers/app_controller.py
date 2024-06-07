from flask import Flask, render_template, request, flash
from flask_mqtt import Mqtt
import json
from flask_socketio import SocketIO
from models.db import db, instance
from controllers.sensors_controller import sensor_
from controllers.actuators_controller import actuators_
from controllers.reads_controller import read
from controllers.users_controller import User_

from login import login


def create_app():

    app = Flask(__name__, template_folder="./views/", root_path="./")

    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(actuators_, url_prefix='/')
    app.register_blueprint(read, url_prefix='/')
    app.register_blueprint(User_, url_prefix='/')

    app.register_blueprint(login, url_prefix='/')

    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    app.secret_key = 'gatogato'  # Necessário para usar a função flash

    # --------------- MQTT --------------- # 

    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_KEEPALIVE'] = 60
    app.config['MQTT_REFRESH_TIME'] = 1.0

    socketio = SocketIO(app)
    mqtt = Mqtt(app)

    @mqtt.on_connect()
    def handle_connect(client, userdata, flags, rc):
        mqtt.subscribe('umidadeTDE')

    @mqtt.on_message()
    def handle_mqtt_message(client, userdata, message):
        print(f'Mensagem recebida: {message.payload.decode()}')
        socketio.emit('mqtt_message', {
            'topic': message.topic,
            'payload': message.payload.decode()
        })

    @socketio.on('publish_mqtt')
    def handle_publish_mqtt_event(json):
        topic = json['topic']
        payload = json['payload']
        mqtt.publish(topic, payload)

    @app.route('/mqtt_display')
    def mqtt_display():
        return render_template('mqtt/mqtt_display.html')

    @app.route('/mqtt_publish')
    def mqtt_publish():
        return render_template('mqtt/mqtt_publish.html')
    
    return app