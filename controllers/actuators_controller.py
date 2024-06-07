from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.actuators import Actuators

actuators_ = Blueprint("actuators_",__name__, template_folder="views")

@actuators_.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuators_.route('/actuators')
def actuators():
    actuators = Actuators.get_actuators()
    return render_template("actuators.html", actuators=actuators)

@actuators_.route('/add_actuator', methods=['POST'])
def add_actuator():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Actuators.save_actuators(name, brand, model, topic, unit, is_active)

    
    return render_template("actuators.html")


@actuators_.route('/edit_actuator/<int:id>', methods=['GET'])
def edit_actuator(id):
    actuator = Actuators.get_single_actuator(id)
    return render_template("update_actuator.html", actuators=[actuator])


@actuators_.route('/update_actuator', methods=['POST'])
def update_actuator():
    id = request.form.get("id")
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Actuators.update_actuator(id, name, brand, model, topic, unit, is_active)
    
    return redirect(url_for('actuators_.actuators'))

@actuators_.route('/del_actuator', methods=['GET'])
def del_actuator():
    id = request.args.get('id', None)
    Actuators.delete_actuator(id)
    
    return redirect(url_for('actuators_.actuators'))
