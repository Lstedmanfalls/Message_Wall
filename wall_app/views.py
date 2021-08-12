from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Class_name, Class_name, Comment, Wall

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Class_name, Class_name

def wall(request): #GET REQUEST
    context = {
    "this_wall": Wall.objects.filter(id = request.POST["email.id"][0]), #<--- find correct key for passsing user id from login
    "all_the_comments": Comment.objects.all(),
    }
    return render(request, "wall.html", context)

def add_message(request): #GET REQUEST
    context = {
    "all_the_messages": Class_name.objects.all()
    }
    return render(request, "add_message.html", context)

def add_comment(request): #GET REQUEST
    context = {
    "all_the_comments": Comment.objects.all()
    }
    return render(request, "add_comment.html", context)

def create_comment(request): #POST REQUEST
    errors = Comment.objects.create_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/root_name/new_comment")
    elif request.method != "POST":
        return redirect("/")
    elif request.method == "POST":
        create = Class_name.objects.create(label = request.POST["label"], label = request.POST["label"])
        comment_id = create.id
        messages.success(request, "Object successfully created")
    return redirect(f"/root_name/{comment_id}")

def view_comment(request, comment_id): #GET REQUEST
    this_comment = Class_name.objects.get(id = comment_id)
    context = {
    "a_comment": this_comment
    }
    return render(request, "view_comment.html", context)

def edit_comment(request, comment_id): #GET REQUEST
    this_comment = Class_name.objects.get(id = comment_id)
    context = {
    "a_comment": this_comment
    }
    return render(request, "edit_comment.html", context)

def update_comment(request, comment_id): #POST REQUEST
    errors = class_name.objects.update_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"root_name/{comment_id}/edit")
    elif request.method != "POST":
        return redirect("/")
    elif request.method == "POST":
        a_comment = Class_name.objects.get(id = comment_id)
        a_comment.label = request.POST["label"]
        a_comment.label = request.POST["label"]
        a_comment.label = request.POST["label"]
        a_comment.save()
        messages.success(request, "Object successfully updated")
    return redirect(f"/root_name/{comment_id}")

def delete_comment(request, comment_id): #POST Request
    if request.method != "POST":
        return redirect("/")
    if request.method == "POST":
        a_comment = Class_name.objects.get(id = comment_id)
        a_comment.delete()
    return redirect("/")