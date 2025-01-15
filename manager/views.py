from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from .forms import *


def index(request):
    courses = Course.objects.all()
    students = Student.objects.all()

    context = {
        'courses': courses,
        'students': students,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = Student.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'students': students,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    context = {
        'student': student,
        'current_year': datetime.now().year
    }

    return render(request, 'student.html', context)


@permission_required('manager.add_course', login_url='not_found')
def addCourse(request: WSGIRequest):
    if request.method == 'POST':
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Ma'lumot muvaffaqiyatli qo'shildi!")
            return redirect('index')
    else:
        form = CourseForm()

    context = {
        'forms': form,
        'current_year': datetime.now().year
    }

    return render(request, 'addCourse.html', context)


@permission_required('manager.change_course', login_url='not_found')
def updateCourse(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CourseForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi!")
            return redirect('course_detail', course_id=course_id)

    else:
        form = CourseForm(instance=course)

    context = {
        'forms': form,
        'current_year': datetime.now().year
    }

    return render(request, 'addCourse.html', context)


@permission_required('manager.delete_course', login_url='not_found')
def deleteCourse(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()

    messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi!")
    return redirect('index')


def register(request: WSGIRequest):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Tabriklaymiz! Siz muvaffaqiyatli ro'yxatdan o'tdingiz va tizimga kirish uchun tayyorsiz.")
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'forms': form,
        'current_year': datetime.now().year
    }

    return render(request, 'auth/register.html', context)


def loginView(request: WSGIRequest):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request,"Hisobingizga muvaffaqiyatli kirdingiz. Endi barcha imkoniyatlardan foydalana olasiz.")
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'forms': form
    }

    return render(request, 'auth/login.html', context)


@login_required
def logoutView(request: WSGIRequest):
    logout(request)

    messages.success(request, "Tizimdan chiqish muvaffaqiyatli amalga oshirildi.")
    return redirect('login')


@login_required
def settings(request: WSGIRequest):
    user = get_object_or_404(MyUser, username=request.user.username)
    if request.method == 'POST':
        form = SettingsForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():

            form.save()

            messages.success(request, "Ma'lumotlar muvaffaqiyatli saqlandi.")
            return redirect('settings_save')

    else:
        form = SettingsForm(instance=user)

    context = {
        'forms': form,
        'current_year': datetime.now().year
    }

    return render(request, 'settings.html', context)


@login_required
def remove_picture(request: WSGIRequest):
    user = request.user

    if user.photo:
        user.photo = None
        user.save()

        messages.success(request, "Profil rasmingiz o'chirildi.")
    else:
        messages.error(request, "Sizda profil rasm mavjud emas!")

    return redirect('settings')


@login_required
def delete_account(request):
    return render(request, 'delete_account.html')


@login_required
def delete_account_confirm(request: WSGIRequest):
    user = request.user
    user.delete()

    messages.success(request, "Hisobingiz muvaffaqiyatli o'chirildi.")
    return redirect('index')


def not_found(request):
    context = {
        'current_year': datetime.now().year
    }

    return render(request, '404.html', context)
