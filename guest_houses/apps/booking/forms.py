from django.contrib.auth.models import User
from django import forms
from django.contrib.admin import widgets
from .models import Realty


class FormCreateUser(forms.Form):
    first_name = forms.CharField(
        max_length=250,
        label='Имя',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    last_name = forms.CharField(
        max_length=250,
        label='Фамилия',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

    username = forms.CharField(
        max_length=250,
        label='Это имя вы будете использовать при авторизации',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password = forms.CharField(
        label='пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    password2 = forms.CharField(
        label='повторите пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class FormLoginUser(forms.Form):
    username = forms.CharField(
        max_length=250,
        label='логин',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password = forms.CharField(
        label='пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class FormBooking(forms.Form):
    date_start = forms.DateField(
        label='Дата когда вы планируете приехать',
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        )
    )
    date_end = forms.DateField(
        label='Дата отъезда',
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        )
    )


class FormFindHotel(forms.Form):
    hotels_graid = (
        ('1 звезд', '1 звезд'),
        ('2 звезд', '2 звезд'),
        ('3 звезд', '3 звезд'),
        ('4 звезд', '4 звезд'),
        ('5 звезд', '5 звезд'),
    )

    peoples_arrey = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    region_query = Realty.objects.distinct('region').values('region')
    region_array = []
    for key in region_query:
        region = key['region']
        region_array.append([region, region])

    graid = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': "selectpicker show-tick form-control",
                'data-live-search': "true",
                'id': "basic",
            }
        ),
        choices=hotels_graid,
        required=True,
    )

    region = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': "selectpicker show-tick form-control",
                'data-live-search': "true",
                'id': "basic",
            }
        ),
        choices=region_array,
        required=True,
    )

    from_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Когда',
            }
        ),
    )

    peoples = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': "selectpicker show-tick form-control",
                'data-live-search': "true",
                'id': "basic",
            }
        ),
        choices=peoples_arrey,
        required=True,
    )


class FormAddHotel(forms.Form):
    type = forms.CharField(max_length=250, label='Тип', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    rooms = forms.IntegerField(label='Кол-во комнат', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    bedrooms = forms.IntegerField(label='Кол-во спален', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    exile = forms.ImageField(label="Изображение", widget=forms.FileInput(
        attrs={'class': 'form-control'}
    ))
    rating = forms.FloatField(label="Рэйтинг", widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    price = forms.FloatField(label='Цена', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    region = forms.CharField(max_length=100, label='Регион', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    address = forms.CharField(max_length=100, label='Адрес', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
