from django.shortcuts import render, redirect, HttpResponse
from django.template import Template , Context
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
#from django.shortcuts import render_to_response

# Create your views here.

@csrf_exempt

def login(request):
        if request.method == "POST" :
            form = AuthenticationForm(data=request.POST)
            #submit_button_value = #request.POST.get('Login')
            submit_button_value = request.POST.get('submit')
            username_value = request.POST.get('username')
            password_value = request.POST.get('password')
        
        # Check if the submit button value matches the button that should trigger the redirection
            if username_value == 'owner' and password_value == 'owner123':
            # Redirect to the 'owner_home' URL name
                return redirect('/owner_home')

            elif username_value == 'service' and password_value == 'service123':
                return redirect('/service_home')
            
            else:
            # Display a warning message for incorrect password.
                error_message = "Incorrect username or password. Please try again."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
            
        return render(request,'login.html')

def owner_home(request): 
      return render(request,'owner_home.html')

def service_home(request): 
      return render(request,'service_home.html')

def items(request): 
      return render(request,'items.html')