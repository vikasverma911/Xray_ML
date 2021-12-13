from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length

class UploadForm(FlaskForm):
    picture_file = FileField('Upload Xray', validators=[FileAllowed(['jpg','jpeg' ,'png']) , DataRequired()])
    submit = SubmitField('Submit')
