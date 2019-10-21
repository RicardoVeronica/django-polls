from django.shortcuts import HttpResponse


def index(request):
    """
    Show simple hello world message in browser
    """
    return HttpResponse("Hello world")
