from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm


def landing (request):
    return render(request, 'landing.html')

def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    students = Student.objects.get(pk=id)
    return render(request, 'index.html', )

def add(request):
    form = StudentForm()
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            return render(request, 'add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'add.html', {
        'form': form
    })
        

def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # Redirect to the detail page of the edited student
            return redirect('view_student', id=id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {'form': form})

def delete_student(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    return render(request, 'confirm_delete_student.html', {'student': student})



