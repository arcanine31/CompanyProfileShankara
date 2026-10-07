from django.shortcuts import render

# Create your views here.


def testing(request):
    return render(request, "base.html")


def page(request, page):
    return render(request, f"pages/{page}.html")