from django.shortcuts import render

# Create your views here.
def sost_list(request):
    return render(request,'sost/sost_list.html')