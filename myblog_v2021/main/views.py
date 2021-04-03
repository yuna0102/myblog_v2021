from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') #render는 django 함수로 request, template_namem context 