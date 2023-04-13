from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/test_db7'
db = SQLAlchemy(app)

class towns(db.Model):
    town = db.Column(db.String(50), primary_key=True)
    visit_date = db.Column(db.Date, uniqie=True)

    def __repr__(self):
        return f"<visits {self.town}>"

@app.route('/', methods=['GET'])
def hello():
    return render_template('main.html', messages=towns.query.all())

@app.route('/add_message', methods=['POST'])
def add_message():
    town = request.form['town']
    visit_date = request.form['visit_date']
    db.session.add(towns(town, visit_date))
    db.session.commit()

    return redirect(url_for('hello'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

