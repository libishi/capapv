from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.institution),
    # path('institutions/', views.institution, name="institutions"),
    # re_path(r'^(?P<institution_id>[0-9]+)/$', views.inst_detail, name="inst_detail"),

    re_path(r'pvsystem/', views.PVSystemList.as_view(), name='pvsystem-list'),
    re_path(r'pvadd/$', views.PVSystemCreate.as_view(), name='pvsystem-add'),
    re_path(r'pvsystem/(?P<pk>[0-9]+)/$', views.PVSystemUpdate.as_view(), name='pvsystem-update'),
    re_path(r'pvsystem/(?P<pk>[0-9]+)/delete/$', views.PVSystemDelete.as_view(), name='pvsystem-delete'),

    re_path(r'institution/$', views.InstitutionList.as_view(), name='institution-list'),
    re_path(r'institution/add/$', views.InstitutionCreate.as_view(), name='institution-add'),
    re_path(r'institution/(?P<pk>[0-9]+)/$', views.InstitutionUpdate.as_view(), name='institution-update'),
    re_path(r'institution/(?P<pk>[0-9]+)/delete/$', views.InstitutionDelete.as_view(), name='institution-delete'),

    re_path(r'product', views.ProductList.as_view(), name='product-list'),
    re_path(r'product/add/$', views.ProductCreate.as_view(), name='product-add'),
    re_path(r'product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product-update'),
    re_path(r'product/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),

    re_path(r'fcompany', views.FCompanyList.as_view(), name='fcompany-list'),
    re_path(r'fcompany/add/$', views.FCompanyCreate.as_view(), name='fcompany-add'),
    re_path(r'fcompany/(?P<pk>[0-9]+)/$', views.FCompanyUpdate.as_view(), name='fcompany-update'),
    re_path(r'fcompany/(?P<pk>[0-9]+)/delete/$', views.FCompanyDelete.as_view(), name='fcompany-delete'),

    re_path(r'thirdparty', views.ThirdPartyList.as_view(), name='thirdparty-list'),
    re_path(r'thirdparty/add/$', views.ThirdPartyCreate.as_view(), name='thirdparty-add'),
    re_path(r'thirdparty/(?P<pk>[0-9]+)/$', views.ThirdPartyUpdate.as_view(), name='thirdparty-update'),
    re_path(r'thirdparty/(?P<pk>[0-9]+)/delete/$', views.ThirdPartyDelete.as_view(), name='thirdparty-delete'),

    re_path(r'qppv', views.QppvList.as_view(), name='qppv-list'),
    re_path(r'qppv/add/$', views.QppvCreate.as_view(), name='qppv-add'),
    re_path(r'qppv/(?P<pk>[0-9]+)/$', views.QppvUpdate.as_view(), name='qppv-update'),
    re_path(r'qppv/(?P<pk>[0-9]+)/delete/$', views.QppvDelete.as_view(), name='qppv-delete'),

    re_path(r'qppvdeputy', views.QppvDeputyList.as_view(), name='qppvdeputy-list'),
    re_path(r'qppvdeputy/add/$', views.QppvDeputyCreate.as_view(), name='qppvdeputy-add'),
    re_path(r'qppvdeputy/(?P<pk>[0-9]+)/$', views.QppvDeputyUpdate.as_view(), name='qppvdeputy-update'),
    re_path(r'qppvdeputy/(?P<pk>[0-9]+)/delete/$', views.QppvDeputyDelete.as_view(), name='qppvdeputy-delete'),
]
