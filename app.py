#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask import render_template
from libs.est_tendencia_central import TendenciaCentralNoAgrupada
from libs.frecuencia import Frecuencia

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World! This is powered by Python backend."


@app.route("/tendencia-central")
def tendencia_central():
    return render_template('tendencia.html')


@app.route("/tendencia-central/agrupada")
def agrupada():
    return render_template('agrupada.html')


@app.route("/tendencia-central/no-agrupada")
def no_agrupada():
    return render_template('nagrupada.html')


"""Post routes"""


@app.route("/tendencia-central/calcular_tendencia_agrupada", methods=['POST'])
def calcular_tendencia_agrupada():
    return jsonify(status=200)


@app.route("/tendencia-central/calcular_tendencia_no_agrupada", methods=['POST'])
def calcular_tendencia_no_agrupada():
    data = list(map(int, request.form['data'].split(',')))
    data.sort()
    frecuencia = Frecuencia(data)
    frecuencia.crear_tabla()
    fna = TendenciaCentralNoAgrupada(data)
    return jsonify(status=200,
                   tabla=frecuencia.tabla,
                   tc={'media': fna.media(),
                       'mediana': fna.mediana(),
                       'armonica': fna.media_geometrica(),
                       'geometrica': fna.media_armonica(),
                       'moda': fna.moda()})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000)
