from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

from home.forms.forms import AddStudentForm
from home.models import StudentInformation


def addStudent(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if len(request.POST['phone_no']) == 10:
            if form.is_valid():
                form.save()
                messages.success(request, 'Congrats! Your details entered successfully.')
                return redirect('add-student')
            else:
                id = request.POST['register_no']
                if StudentInformation.objects.filter(register_no=id).exists:
                    messages.error(request, "Oops! This Register Number already exists")
                    return redirect('add-student')
        else:
            messages.error(request, "Oops! Please check your entered phone number")
            return redirect('add-student')
    return render(request, 'index.html')
