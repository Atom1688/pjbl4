from flask import Blueprint, request, render_template, flash, redirect
from models.iot.read import Read
from models.iot.sensors import Sensor


read = Blueprint("read",__name__, template_folder="views")

@read.route("/history_read")
def history_read():
    sensors = Sensor.get_sensors()
    read = {}
    return render_template("history_read.html", sensors = sensors, read = read)

@read.route("/get_read", methods=['POST'])
def get_read():
    if request.method == 'POST':
        id = request.form['id']
        start = request.form['start']
        end = request.form['end']
        if not start or not end:
            # Se as datas não forem fornecidas, redirecione para a mesma página
            # com uma mensagem de erro
            flash('Por favor, forneça as datas de início e fim.', 'error')
            return redirect(request.referrer)
        read = Read.get_read(id, start, end)
        sensors = Sensor.get_sensors()
        return render_template("history_read.html", sensors=sensors, read=read)


