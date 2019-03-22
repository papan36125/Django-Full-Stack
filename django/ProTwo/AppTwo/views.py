from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html', context = {})
# Create your views here.
def help(request):
    my_dict = {'insert_me':'Help Page'}
    return render(request,'AppTwo/help.html', context = my_dict)

def view_users(request):
    # user_list = User.objects.order_by('last_name')
    # user_data = {'user_list' : user_list}
    # return render(request,'AppTwo/users.html', context = user_data)
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'AppTwo/users.html',{'form': form})
