from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signupfunc(request):
  if request.method == 'POST':
    username2 = request.POST['username']
    password2 = request.POST['password']
    try:
      User.objects.get(username=username2)
      return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
    except:
      user = User.objects.create_user(username2, '', password2)
      return render(request, 'signup.html', {'some': 100})
  return render(request, 'signup.html', {'some': 100})

def loginfunc(request):
    if request.method == 'POST':
      username2 = request.POST['username']
      password2 = request.POST['password']
      user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.