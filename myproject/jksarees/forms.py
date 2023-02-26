from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class JKSareesForm(FlaskForm):

    provider    = StringField('Provider', validators=[DataRequired()])
    category    = StringField('Category', validators=[DataRequired()])
    subCategory = StringField('Sub-Category', validators=[DataRequired()])
    image       = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit      = SubmitField('Upload')



class DeleteJKSareesForm(FlaskForm):

    img_name    = StringField('Image_name', validators=[DataRequired()])
    submit      = SubmitField('Submit')
