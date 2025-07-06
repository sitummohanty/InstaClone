"""
   Handle user-registration requests and return a JSON response.

   History:
   --------
   • **v1.1 – 2025-07-06**
     Replaced manual "User" instantiation with "UserCreateSerializer"
     to leverage built-in validation and password hashing.
     Added proper HTTP 201 on success and HTTP 400 on validation error.

   Parameters:
   -----------
   request : rest_framework.request.Request
       Must contain "username", "password", and "email" keys (plus
       any optional fields accepted by "UserCreateSerializer") in the
       POST body.

   Returns:
   --------
   rest_framework.response.Response
       A JSON object with either
       - {"data": {"success": true}} on success (HTTP 201) or
       - {"errors": {...}} on failure (HTTP 400).

   • **v1.0 – 2025-06-30**
     Initial proof-of-concept: hand-built the "User" object inside the
     view (commented outy in code) and responded with plain JSON plus HTTP 200.
       # Serialization: converting python objects --> native data types --> into json/xml
       # DE-Serialization: json/xml --> native data types --> converting python objects

   """


from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import UserSignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
# Create your views here.

def index(request):

# /myapp/index/ -- GET -- /myapp/index/.......
# message1 = f"{request.path} -- {request.method} --  {request.path_info} -- {request.META}"
# message2 = f"{request.GET['colour']}"
# return HttpResponse(message2)

  return HttpResponse("Sumi")


def signup(request):

  form = UserSignUpForm()
  context = {
    'form' : form
  }
  return render(request, 'myapp/signup.html')

def home(request):
    # any context you like; for now just render a simple template
    return render(request, 'myapp/home.html', {})

def login_view(request):
    # Instantiate your LoginForm, binding POST data if present
    form = UserSignUpForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # form.get_user() returns the authenticated user
            user = form.get_user()
            login(request, user)
            return redirect('home')

        # Pass the form under the key 'form'
    return render(request, 'myapp/login.html', {
        'form': form
 })

@api_view(['POST'])  #<-- DRF looks into this
def create_user(request):

    """
    <-- Manual way
       user = User()
       user.first_name = request.data['first_name']
       user.last_name = request.data['last_name']
       user.email = request.data['email']

       user.save()

       response_objects = {
       "first_name": user.first_name,
       "last_name": user.last_name
        }
        import json
       response_data = json.loads(response_objects)
    """

    print("On line 50 --->", request.data)

    # Can you may the user data to user object
    serializer = UserCreateSerializer(data=request.data)

    response_data = {
        "errors": None,
        "data": None
    }

    if serializer.is_valid():
        user = serializer.save()
        response_data["data"] = {
            "Success":"True"
        }
        response_status = status.HTTP_201_CREATED
    else:
        response_data["error"] = serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data, status=response_status)

