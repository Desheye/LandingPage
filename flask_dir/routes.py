# flask_dir/routes.py

from flask import render_template, redirect, url_for, flash
from flask_dir import app, db
from flask_dir.forms import UserForm
from flask_dir.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        # Create a new User object with form data
        user = User(
            username=form.username.data,
            email=form.email.data,
            company=form.company.data,
            phone=form.phone.data,
            message=form.message.data
        )
        # Add the new user to the session and commit to the database
        db.session.add(user)
        db.session.commit()
        flash('Your details have been submitted successfully!', 'success')
        return redirect(url_for('index'))
    # Render the form template if the request method is GET or form validation fails
    return render_template('index.html', form=form)
