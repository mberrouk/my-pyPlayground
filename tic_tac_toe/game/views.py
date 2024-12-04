from django.shortcuts import render, redirect

from django.http import HttpResponse

# from django.views.decorators.csrf import csrf_exempt
from . import views, models

from django.contrib import messages

# Create your views here.
"""
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        roomId = request.POST.get("room-id", None)
        playerName = request.POST.get("player-name", "Unknown Player")
        if(roomId):
            try:
                room = Room.objects.get(id=roomId)
                return redirect(f"/game/{room.id}/{playerName}/")
            except Room.DoesNotExist:
                messages.error(request, "Room does not exist.")
                return redirect("/")
                
        else:
            room = Room.objects.create()
            return redirect(f"/game/{room.id}/{playerName}/")


def game(request, id=None, name=None):
    try:
        room = Room.objects.get(id=id)
        return render(request, "game.html", {"room": room, "name": name})
    except Room.DoesNotExist:
        messages.error(request, "Room does not exist. You fool!!")
        return redirect("/")
"""


# @csrf_exempt
def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        roomId = request.POST.get("room-id", None)
        playerName = request.POST.get("player-name", "Unknown")
        if roomId:
            try:
                room = models.Room.objects.get(id=roomId)
                return redirect(f"/game/{room.id}/{playerName}")
            except models.Room.DoesNotExist:
                messages.error(request, "Room does not exist.")
                return redirect("/")
        # else create a new room
        room = models.Room.objects.create()
        return redirect(f"/game/{room.id}/{playerName}")


def game(request, id=None, name=None):
    try:
        room = models.Room.objects.get(id=id)
        return render(request, "game.html", {"room": room, "name": name})
    except models.Room.DoesNotExist:
        messages.error(request, "Room does not exist.")
        return redirect("/")
