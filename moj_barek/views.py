from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from moj_barek.models import Butelka


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world")


def logout(request):
    return HttpResponse("Logout Page")

def login(request):
    return HttpResponse("Login Page")



@csrf_exempt
def butelki(request):
    form = """
    <form method='POST' action=''>
        Name: <input name="name"> <br />
        Volume: <input name="volume"> <br />
        Date: <input name="bought"> <br />
        <input type="submit" value="Zapisz">
    </form>
    """

    if request.method == "POST":
        name = request.POST.get("name")
        volume = request.POST.get("volume")
        bougth = request.POST.get("bought")

        Butelka.objects.create(name=name, volume=volume, bougth=bougth)

        form = "Udało sie zapisać do bazy danych" + form
        return HttpResponse(form)
    else:
        # wyświetl formularz
        return HttpResponse(form)