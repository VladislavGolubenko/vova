from datetime import datetime, date, time
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Booking, Realty
from .forms import FormAddHotel, FormCreateUser, FormLoginUser, FormBooking
from .filters import RealtyFilter


def create_user(request):
    if request.method == 'POST':
        form = FormCreateUser(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user = User(**form.cleaned_data)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return render(request, 'booking/index.html')
    else:
        form = FormCreateUser

    context = {
        'form': form,
    }
    return render(request, 'booking/registration.html', context)


def user_login(request):
    if request.method == 'POST':
        form = FormLoginUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('realty')
            else:
                return HttpResponseRedirect("/account/invalid/")
    else:
        form = FormLoginUser

    context = {
        'form': form,
    }
    return render(request, 'booking/login.html', context)


def user_logout(request):
    auth.logout(request)
    return redirect('home')


def index(request):
    booking = Booking.objects.all()
    user = request.user
    context = {
        'booking': booking,
        'user': user,
    }
    return render(request, template_name='booking/index.html', context=context)


def realty(request):
    realty = Realty.objects.prefetch_related('pictures').all()
    filter = RealtyFilter(request.GET, queryset=realty)

    paginator = Paginator(filter.qs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'realty': realty,
        'filter': filter,
        'page_obj': page_obj
    }

    return render(request, template_name='booking/realtys.html', context=context)


def detail_realty(request, id_realty):
    realty = Realty.objects.prefetch_related('pictures').get(pk=id_realty)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FormBooking(request.POST)
            if form.is_valid():
                date_start = form.cleaned_data['date_start']
                date_end = form.cleaned_data['date_end']
                id_user = request.user.id
                user = User.objects.get(pk=id_user)
                realty = Realty.objects.get(pk=id_realty)
                date_creation = date.today()
                amount = realty.price
                booking = Booking(date_start=date_start, date_end=date_end, id_user=user,
                                  date_creation=date_creation, amount=amount, id_realty=realty)
                booking.save()
        else:
            form = FormBooking
        return render(
            request,
            'booking/realty_detail.html',
            {
                'form': form,
                'realty': realty
            }
        )

    return render(
        request,
        'booking/realty_detail.html',
        {'realty': realty, }
    )


def user_bookings(request):
    user_id = request.user.pk
    user = User.objects.get(pk=user_id)
    bookings = Booking.objects.filter(id_user=user_id)
    context = {
        'bookings': bookings,
        'user': user
    }
    return render(request, 'booking/bookings.html', context=context)


def add_realty(request):
    if request.method == 'POST':
        form = FormAddHotel(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            realty = Realty.objects.create(**form.cleaned_data)
            return redirect(realty)
    else:
        form = FormAddHotel()
    return render(request, 'booking/add_hotel.html', {'form': form})
