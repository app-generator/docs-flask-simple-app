from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, db

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

# Public homepage route
@main.route('/')
def home():
    return render_template('home.html')

# Protected route
@main.route('/private')
@login_required
def private():
    return render_template('private.html')

# API route to list users
@main.route('/api/users')
def list_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

# Authentication routes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.private'))
            
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            return "Username already exists"
            
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
        
    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
