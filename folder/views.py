from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

from .forms import FileForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')  # Redirect to the view_responses page
    else:  # If the request method is GET
        form = FileForm()

    return render(request, 'index.html', {'form': form})
    


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email is already in used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Name is already in used.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Account created successfully!!!")
                return redirect('register')
        else:
            messages.info(request, "Passwords do not match.")
            return redirect('register')
    else:
        #method="GET"  
        return render(request, 'register.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if user has entered correct credentials
        user = auth.authenticate(username=username, password=password)

        if user is not None:
    # A backend authenticated the credentials
            auth.login(request,user)
            messages.success(request,"User logged in successfully!")
            return redirect("index")
        else:
    # No backend authenticated the credentials
            messages.info(request,"User not found! Please enter correct credentials")
            return render(request,'login.html')
    else:
        return render(request, 'login.html')
    
def userlogout(request):
   auth.logout(request)
   return redirect ("/login")

def confirm(request):
    success_message = messages.get_messages(request)
    return render(request, 'confirm.html', {'success_message': success_message})