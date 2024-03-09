from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    """Login form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    """Register form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Register')
    
class AddproductForm(FlaskForm):
    """Addprodutform"""
    product_name = StringField('Product name', validators=[DataRequired(), Length(1, 64)]) 
    product_description = StringField('Product description', validators=[DataRequired(), Length(1, 64)])
    stock_available = SelectField('Stock available', choices=[('2','2' ), ('3', '3'), ('4', '4')])
    submit = SubmitField('Addproducts')