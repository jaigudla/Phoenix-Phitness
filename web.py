from flask import Flask, redirect, url_for, render_template
from flask import Response
import threading
import argparse
import datetime
import time
#import mediapipe as mp
import cv2
import numpy as np

app = Flask(__name__)


@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route('/info.html')
def info():
    return render_template("info.html")

@app.route('/project.html')
def project():
    return render_template("project.html")

@app.route('/ML.html')
def ML():
    return render_template("ML.html")

@app.route('/conc.html')
def conc():
    return render_template("conc.html")

if __name__ == "__main__":
    app.run()