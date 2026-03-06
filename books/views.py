from django.shortcuts import render

def browse_books(request):
    return render(request, "books.html")
