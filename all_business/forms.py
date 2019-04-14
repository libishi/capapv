# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from .models import Institution, Product, FCompany, ThirdParty, Qppv, QppvDeputy, PvSystem, ActiveIng
from ajax_select.fields import AutoCompleteSelectMultipleField

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        exclude = ()

class PvSystemForm(forms.ModelForm):
    class Meta:
        model = PvSystem
        exclude = ()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()

class FCompanyForm(forms.ModelForm):
    class Meta:
        model = FCompany
        exclude = ()

class ThirdPartyForm(forms.ModelForm):
    class Meta:
        model = ThirdParty
        exclude = ()

class QppvForm(forms.ModelForm):
    class Meta:
        model = Qppv
        exclude = ()


class QppvDeputyForm(forms.ModelForm):
    class Meta:
        model = QppvDeputy
        exclude = ()


class ActiveIngForm(forms.ModelForm):
    class Meta:
        model = ActiveIng
        exclude = ()
