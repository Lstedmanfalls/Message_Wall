from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Message, Comment

def wall(request): #GET REQUEST
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        context = {
            "this_user": User.objects.get(id=request.session["user_id"]),
            "all_the_messages": Message.objects.all().order_by("-created_at"),
            "all_the_comments": Comment.objects.all(),
    }
    return render(request, "wall.html", context)

def create_message(request): #POST REQUEST
    # errors = Message.objects.create_validator(request.POST)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect("/")
    if request.method != "POST":
        return redirect("/wall")
    elif request.method == "POST":
        create = Message.objects.create(message = request.POST["message"], user = User.objects.get(id=request.session["user_id"]))
        message_id = create.id
        messages.success(request, "Message successfully created")
    return redirect("/wall")