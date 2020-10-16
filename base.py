from flask import Flask,render_template,session,flash,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "mykey"

class SimpleForm(FlaskForm):
    breed = StringField('What breed are you ?',validators=[DataRequired()])
    submit = SubmitField('Click me.')

@app.route('/', methods=['GET','POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['breed']= form.breed.data
        flash(f"The selected breed is : {session['breed']}")
        return redirect(url_for('index'))

    return render_template('index.html', form=form)
              @app.route('/', methods=['GET','POST'])
def tesla():
    form = SimpleForm()
    if form.validate_on_submit():
        session['mootr']= form.breed.data
        flash(f"The selected breed is : {session['breed']}")
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=False)
