# flask_dir/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'userInfo'  # Ensure the model maps to the correct table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True)  # Adjusted to match the column type and length
    email = db.Column(db.String(100), unique=True, nullable=True)  # Adjusted to match the column type and length
    company = db.Column(db.String(100), nullable=True)  # Adjusted to match the column type and length
    phone = db.Column(db.String(20), nullable=True)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'
