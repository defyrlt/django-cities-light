from __future__ import unicode_literals

from django import forms

from .models import Country, Region, City, SalesRegion

__all__ = ['CountryForm', 'RegionForm', 'CityForm', 'SalesRegionForm']


class CountryForm(forms.ModelForm):
    """
    Country model form.
    """
    class Meta:
        model = Country
        exclude = ('name_ascii', 'slug', 'geoname_id')


class RegionForm(forms.ModelForm):
    """
    Region model form.
    """
    class Meta:
        model = Region
        exclude = ('name_ascii', 'slug', 'geoname_id', 'display_name',
                   'geoname_code')


class SalesRegionForm(forms.ModelForm):
    """
    SalesRegion model form.
    """
    class Meta:
        model = SalesRegion
        exclude = ('name_ascii', 'slug', 'geoname_id', 'display_name',
                   'geoname_code')


class CityForm(forms.ModelForm):
    """
    City model form.
    """
    class Meta:
        model = City
        exclude = ('name_ascii', 'search_names', 'slug', 'geoname_id',
                   'display_name', 'feature_code')
