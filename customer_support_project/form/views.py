from django.shortcuts import render, redirect
from .models import FormSubmission

# Create your views here.
def form(request):
    return render(request, 'form/form.html')

def submission(request):
    return render(request, 'form/submission.html')

def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Saving to DB
        submission = FormSubmission.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            message=message
        )
        submission.save()

        return redirect('submission') 
    else:
        return render(request, 'form/form.html')
