from django.urls import path
from . import views

urlpatterns = [
path('login',views.login, name='login'),
path('logout',views.logout, name='logout'),
path('dashboard',views.dashboard, name='dashboard'),
path('invoices',views.invoices, name='invoices'),
path('products',views.products, name='products'),
path('clients',views.clients, name='clients'),


path('invoices/create',views.createInvoice, name='create-invoice'),
path('invoices/create-build/<slug:slug>',views.createBuildInvoice, name='create-build-invoice'),


path('invoices/delete/<slug:slug>',views.deleteInvoice, name='delete-invoice'),


path('invoices/view-pdf/<slug:slug>',views.viewPDFInvoice, name='view-pdf-invoice'),
path('invoices/view-document/<slug:slug>',views.viewDocumentInvoice, name='view-document-invoice'),
path('invoices/email-document/<slug:slug>',views.emailDocumentInvoice, name='email-document-invoice'),


path('company/settings',views.companySettings, name='company-settings'),
]
