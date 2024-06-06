# flask_dir/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class UserForm(FlaskForm):
    username = StringField(
        'Full Name',
        validators=[DataRequired(), Length(min=2, max=80)],
        render_kw={"placeholder": "Enter your full name"}
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"}
    )
    company = StringField(
        'Company',
        validators=[Length(max=120)],
        render_kw={"placeholder": "Company name (optional)"}
    )
    phone = StringField(
        'Phone Number',
        validators=[Length(max=20)],
        render_kw={"placeholder": "Phone Number"}
    )
    message = TextAreaField(
        'Message',
        validators=[Length(max=500)],
        render_kw={"placeholder": "Enter your message (optional)"}
    )
    submit = SubmitField('Submit')
