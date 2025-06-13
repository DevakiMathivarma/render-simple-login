from flask import Flask, render_template, redirect, url_for, flash, session
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Hardcoded credentials
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password123'

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == VALID_USERNAME and form.password.data == VALID_PASSWORD:
            session['username'] = form.username.data
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password", 'error')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash("Please log in first.", 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
