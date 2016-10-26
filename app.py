#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from flask import Flask
from flask import render_template

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
	pass

@app.route("/tendencia-central/calcular_tendencia_no_agrupada", methods=['POST'])
def calcular_tendencia_no_agrupada():
	pass

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000)
