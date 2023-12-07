from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')   
        return render(request,'first_app/home.html',{"name":name,"email":email})
    else:
        return render(request,'first_app/home.html')
    

def forms(request):
    return render(request,'first_app/form.html')

# def profile(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         email = request.POST.get('email')   
#         return render(request,'first_app/profile.html',{"name":name,"email":email})
#     else:
#         return render(request,'first_app/profile.html')
def profile(request):
    form = ProfileForm(request.POST)
    
    if form.is_valid():
        print(form.cleaned_data)
       
        return render(request,'first_app/profile.html',{'data':form.cleaned_data})
    else:
        return render(request,'first_app/profile.html')

def django_form(request):
    
    form = ProfileForm(request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        return render(request,'first_app/django_form.html',{"form":form,'data':form.cleaned_data})