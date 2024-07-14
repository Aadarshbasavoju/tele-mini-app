from flask import render_template
from app import app
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leaderboard')
def leaderboard():
    users = User.query.order_by(User.referrals.desc()).all()
    return render_template('leaderboard.html', users=users)

@app.route('/referral/<username>')
def referral(username):
    link = f"http://yourdomain.com/referral/{username}"
    return render_template('referral.html', link=link)
