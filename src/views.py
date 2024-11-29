from flask import Flask, request, render_template
from models import db, User, WorkEntry
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestion_horas.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_entry', methods=['POST'])
def add_entry():
    user_id = request.form['user_id']
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    hours_worked = float(request.form['hours_worked'])
    entry = WorkEntry(user_id=user_id, date=date, hours_worked=hours_worked)
    db.session.add(entry)
    db.session.commit()
    return 'Entry added!'

@app.route('/total_hours/<int:user_id>')
def total_hours(user_id):
    user = User.query.get(user_id)
    total_hours = sum(entry.hours_worked for entry in user.work_entries)
    total_earnings = total_hours * user.hourly_rate
    return f'Total hours: {total_hours}, Total earnings: {total_earnings}'