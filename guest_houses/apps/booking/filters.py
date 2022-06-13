import django_filters
from django import forms
from .models import Realty


class RealtyFilter(django_filters.FilterSet):

    region_query = Realty.objects.distinct('region').values('region')
    region_array = []

    for key in region_query:
        region = key['region']
        region_array.append([region, region])

    region = django_filters.MultipleChoiceFilter(
        widget=forms.CheckboxSelectMultiple(),
        choices=region_array,
    )

    types = (
        ('Номер в гостевом доме', 'Номер в гостевом доме'),
        ('Квартира', 'Квартира'),
        ('Частный дом', 'Частный дом'),
        ('Номер в гостинице', 'Номер в гостинице')
    )

    type = django_filters.MultipleChoiceFilter(
        widget=forms.CheckboxSelectMultiple(),
        choices=types,
    )

    rooms_array = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    rooms = django_filters.MultipleChoiceFilter(
        widget=forms.CheckboxSelectMultiple(),
        choices=rooms_array,
    )

    bedrooms_array = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )

    bedrooms = django_filters.MultipleChoiceFilter(
        widget=forms.CheckboxSelectMultiple(),
        choices=bedrooms_array,
    )

    price = django_filters.RangeFilter()

    class Meta:
        query = Realty.objects.prefetch_related('pictures').all()
        fields = ['']
