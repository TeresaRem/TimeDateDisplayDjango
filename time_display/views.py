from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%B %d, %Y %H:%M %p", localtime())
    }
    return render(request, "index.html", context)
