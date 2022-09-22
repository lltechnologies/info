from django.shortcuts import render, redirect
from . models import Customer

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        err=None
        name=request.POST.get('name')
        emailadd=request.POST.get('email')
        phone=request.POST.get('contact')
        sub=request.POST.get('subject')
        mess=request.POST.get('message')

        # Validation
        values={'name':name,
                'emailadd':emailadd,
                'phone':phone,
                'sub':sub,
                'mess':mess,}
        customer = Customer(name=name, email=emailadd, contact=phone, subject=sub, message=mess)

        if not name.isalpha():
            err="Invalid Name, please try again"
        if not phone.isnumeric() or len(phone)<10:
            err="Invalid Contact Number, please try again"

        data = {}
        data['err'] = err
        data['values'] = values
        if err:
            return render(request, 'contact.html')
        customer.save()

        return render(request, 'submit.html',{'err': err})
    else:
        return render(request, 'contact.html')

def submit(request):
    return redirect(request,'submit.html')
