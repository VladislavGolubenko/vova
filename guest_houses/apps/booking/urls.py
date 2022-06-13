from django.urls import path
from .views import index, realty, detail_realty, add_realty, create_user, user_login, user_logout, user_bookings

urlpatterns = [
    path('', index, name="home"),
    path('realty/', realty, name='realty'),
    path('realty/<int:id_realty>', detail_realty, name='detail'),
    path('registration/', create_user, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('my_bookings/', user_bookings, name='my_bookings'),
    path('realty/add_realty/', add_realty, name='add_realty'),
]
