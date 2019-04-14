
from .models import *
from .forms import *
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect


# def institution(request):
#     all_institution = Institution.objects.all()
#     context = {'all_institution': all_institution}
#     return render(request, 'institutions/institutions.html', context)


# def inst_detail(request, institution_id):
#     institution = get_object_or_404(Institution, pk=institution_id)   
#     context = {'institution': institution}
#     return render(request, 'institutions/inst_detail.html', context)


class PVSystemList(ListView):
    template_name = 'pvsystem/pvsystem_list.html'
    model = PvSystem


class PVSystemCreate(CreateView):
    template_name = 'pvsystem/pvsystem_form.html'
    model = PvSystem
    form_class = PvSystemForm
    success_url = reverse_lazy('pvsystem-list')
    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.updated_by = self.request.user
    #     post.updated_at = timezone.now()
    #     post.save()
    #     return redirect('pvsystem-list', pk=post.topic.board.pk, topic_pk=post.topic.pk)


class PVSystemUpdate(UpdateView):
    template_name = 'pvsystem/pvsystem_form.html'
    form_class = PvSystemForm
    success_url = '/'


class PVSystemDelete(DeleteView):
    template_name = 'pvsystem/pvsystem_confirm_delete.html'
    model = PvSystem
    success_url = reverse_lazy('pvsystem-list')

###############################################################

class InstitutionList(ListView):
    template_name = 'institution/institution_list.html'
    model = Institution


class InstitutionCreate(CreateView):
    template_name = 'institution/institution_form.html'
    form_class = InstitutionForm


class InstitutionUpdate(UpdateView):
    template_name = 'institution/institution_form.html'
    form_class = InstitutionForm
    success_url = '/'


class InstitutionDelete(DeleteView):
    template_name = 'institution/institution_confirm_delete.html'
    model = Institution
    success_url = reverse_lazy('institution-list')

###################################################################

class ProductList(ListView):
    template_name = 'product/product_list.html'
    model = Product


class ProductCreate(CreateView):
    template_name = 'product/product_form.html'
    form_class = ProductForm


class ProductUpdate(UpdateView):
    template_name = 'product/product_form.html'
    form_class = ProductForm
    success_url = '/'


class ProductDelete(DeleteView):
    template_name = 'product/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('product-list')

###################################################################

class FCompanyList(ListView):
    template_name = 'fcompany/fcompany_list.html'
    model = FCompany


class FCompanyCreate(CreateView):
    template_name = 'fcompany/fcompany_form.html'
    form_class = FCompanyForm


class FCompanyUpdate(UpdateView):
    template_name = 'fcompany/fcompany_form.html'
    form_class = FCompanyForm
    success_url = '/'


class FCompanyDelete(DeleteView):
    template_name = 'fcompany/fcompany_confirm_delete.html'
    model = FCompany
    success_url = reverse_lazy('fcompany-list')

###################################################################

class ThirdPartyList(ListView):
    template_name = 'thirdparty/thirdparty_list.html'
    model = ThirdParty


class ThirdPartyCreate(CreateView):
    template_name = 'thirdparty/thirdparty_form.html'
    form_class = ThirdPartyForm


class ThirdPartyUpdate(UpdateView):
    template_name = 'thirdparty/thirdparty_form.html'
    form_class = ThirdPartyForm
    success_url = '/'


class ThirdPartyDelete(DeleteView):
    template_name = 'thirdparty/thirdparty_confirm_delete.html'
    model = ThirdParty
    success_url = reverse_lazy('thirdparty-list')

###################################################################

class QppvList(ListView):
    template_name = 'qppv/qppv_list.html'
    model = Qppv


class QppvCreate(CreateView):
    template_name = 'qppv/qppv_form.html'
    form_class = QppvForm


class QppvUpdate(UpdateView):
    template_name = 'qppv/qppv_form.html'
    form_class = QppvForm
    success_url = '/'


class QppvDelete(DeleteView):
    template_name = 'qppv/qppv_confirm_delete.html'
    model = Qppv
    success_url = reverse_lazy('qppv-list')

###################################################################

class QppvDeputyList(ListView):
    template_name = 'qppvdeputy/qppvdeputy_list.html'
    model = QppvDeputy


class QppvDeputyCreate(CreateView):
    template_name = 'qppvdeputy/qppvdeputy_form.html'
    form_class = QppvDeputyForm


class QppvDeputyUpdate(UpdateView):
    template_name = 'qppvdeputy/qppvdeputy_form.html'
    form_class = QppvDeputyForm
    success_url = '/'


class QppvDeputyDelete(DeleteView):
    template_name = 'qppvdeputy/qppvdeputy_confirm_delete.html'
    model = QppvDeputy
    success_url = reverse_lazy('qppvdeputy-list')
