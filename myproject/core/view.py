# myproject/core/view.py
from flask import render_template, url_for, redirect, request, Blueprint, flash
from flask_login import login_user, current_user, logout_user, login_required
from myproject import db
from myproject.models import Users, JKSarees
from myproject.jksarees.forms import JKSareesForm, DeleteJKSareesForm
from datetime import datetime

from myproject.jksarees.picture_handler import add_profile_pic
from base64 import b64encode 
import base64
import io
from PIL import Image


core = Blueprint('core', __name__)


def decode_image(x):
    print(f" type of x {type(x)}")
    print(type(b64encode(x).decode("utf-8")))
    return b64encode(x).decode("utf-8")


@core.route('/')
def home():
    sarees = JKSarees.query.order_by(JKSarees.img_name.desc()).all()
    count_of_sarees = len(sarees)
    return render_template('homepage.html', sarees=sarees, count_of_sarees=count_of_sarees, decode_image=decode_image)

@core.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


