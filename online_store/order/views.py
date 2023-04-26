from django.shortcuts import render

# Create your views here.
def search_item(request):
    return render(request,r"search_temp\search_item.html")
