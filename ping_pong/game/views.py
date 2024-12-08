from django.shortcuts import redirect, render
from django.contrib import messages
from . import models
import pdb

# pdb.set_trace()


# Create your views here.
def index(request):
    if request.method == "POST":
        # pdb.set_trace()

        playerName = request.POST.get("player-name", None)
        # TODO check for a valid name
        if playerName == None or len(playerName) == 0:
            # TODO send error message
            return render(request, "index.html")

        roomId = request.POST.get("room-id", None)
        if roomId:
            try:
                room = models.Room.objects.get(id=roomId)
                return redirect(f"/game/{room.id}/{playerName}/")
            except models.Room.DoesNotExist:
                messages.error(request, "Room does not exist.")
                return redirect("/")

        room = models.Room.objects.create()
        return redirect(f"/game/{room.id}/{playerName}/")

    return render(request, "index.html")


def game(request, id=None, name=None):
    print("GAME VIEW")
    try:
        room = models.Room.objects.get(id=id)
        return render(
            request,
            "game.html",
            {
                "id": room.id,
                "name": name,
            },
        )
    except models.Room.DoesNotExist:
        messages.error(request, "Room does not exist.")
        return redirect("/")
