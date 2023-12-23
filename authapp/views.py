
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, authenticate
from authapp.models import CustomUser

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('display_name')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        user = CustomUser.objects.create_user(username = username, full_name = full_name, email = email, password = password, user_type = user_type)
        user.save()
    return render( request, 'index.html')


def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')