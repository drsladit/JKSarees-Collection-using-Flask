#myproject/jksarees/view.py

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

jksarees = Blueprint("jksarees", __name__)


def decode_image(x):
    #print(f" type of x {type(x)}")
    #print(type(b64encode(x).decode("utf-8")))
    return b64encode(x).decode("utf-8")


def byte_image(y):
    img = img.open(io.BytesIO(y))
    return img.show()

@jksarees.route('/add', methods=['GET', 'POST'])
@login_required
def add_saree():

    form = JKSareesForm()
    sarees = JKSarees.query.order_by(JKSarees.img_name.desc()).all()
    if form.validate_on_submit():
        provider=form.provider.data
        category=form.category.data
        subCategory=form.subCategory.data
        #print(f"abc {type(form.image.data)}")
        image=(form.image.data).read()
        #print(type(form.image.data))
        #print(type(image))
        #image = add_profile_pic(form.image.data)

        img_name = datetime.now().strftime("%Y%m%d_%H_%M_%S")
        saree = JKSarees(current_user.id, provider,category,subCategory, img_name, image)
        db.session.add(saree)
        db.session.commit()
        flash('Saree got added')
        print('image added successfully')
        
        return render_template('addsaree.html', form=form, sarees=sarees, decode_image=decode_image, byte_image=byte_image)
        #return redirect(url_for('jksarees.add_saree'))
    return render_template('addsaree.html', form=form, sarees=sarees, decode_image=decode_image, byte_image=byte_image)




@jksarees.route('/view', methods=['GET', 'POST'])
def view_saree():

    #sarees = JKSarees.query.limit(2).all()
    sarees = JKSarees.query.order_by(JKSarees.img_name.desc()).all()
    for saree in sarees:
        print(type(saree.image))
    return render_template('viewsarees.html', sarees=sarees, decode_image=decode_image, byte_image=byte_image)


@jksarees.route('/delete', methods=['GET', 'POST'])
@login_required
def delete_saree():

    form = DeleteJKSareesForm()

    sarees = JKSarees.query.order_by(JKSarees.img_name.desc()).all()

    if form.validate_on_submit():
        
    
        saree = JKSarees.query.filter_by(img_name=form.img_name.data).first()
        db.session.delete(saree)
        db.session.commit()
        return render_template('deletesaree.html', form=form, sarees=sarees, decode_image=decode_image)
    return render_template('deletesaree.html', form=form, sarees=sarees, decode_image=decode_image)