from flask_wtf import FlaskForm
from flask_wtf import FileAllowed, FileField, FileRequired




class UploadForm(FlaskForm):
    photo_test = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'Images Only!'])
    ])