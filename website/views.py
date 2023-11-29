from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Poll, User
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    
    return render_template("home.html", user=current_user)

@views.route("/delete-poll", methods=["POST"])
def delete_poll():
    poll = json.loads(request.data)
    pollId = poll["pollId"]
    poll = Poll.query.get(pollId)
    if poll:
       if poll.user_id == current_user.id:
           db.session.delete(poll) 
           db.session.commit()
    
    return jsonify({})

@views.route("/vote", methods=["GET", "POST"])
@login_required
def vote():
    polls = Poll.query.all()
    user_names = {}  # Create a dictionary to store user names for each poll
    for poll in polls:
        user = User.query.get(poll.user_id)

        if user:
            user_names[poll.id] = user.user_name


    return render_template("vote.html", user=current_user, polls=polls, user_names=user_names)

@views.route("create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        question = request.form.get("question")
        option_1 = request.form.get("option_1")
        option_2 = request.form.get("option_2")
        option_3 = request.form.get("option_3")
        option_4 = request.form.get("option_4")

        if len(question) < 1:
            flash("Question is too short.", category="error")
        elif not(option_1):
            flash("Option 1 and Option 2 are required.", category="error")
        elif not(option_2):
            flash("Option 1 and Option 2 are required.", category="error")
        else:
            new_poll = Poll(question=question, 
                            option_1 = option_1, 
                            option_2 = option_2, 
                            option_3 = option_3, 
                            option_4 = option_4,
                            user_id=current_user.id)
            db.session.add(new_poll)
            db.session.commit()
            flash("Poll Created!", category="success")
            
    return render_template("create.html", user=current_user)
        