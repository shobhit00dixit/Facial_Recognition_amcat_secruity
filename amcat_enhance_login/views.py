from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from amcat_enhance_login.forms import registration_form

def main(request):
    #return render(request,'index.html')
    return render(request,'home.html')

def login_func(request):
    ''' Function to take user information '''
    form=registration_form()
    if request.method=='POST':
        form=registration_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success.html')
    return render(request, 'login_app/form_upload.html', {
        'form': form
    })



