from django.urls import path
from invoice import account
from . import login
from . import invoice
from invoice import products, market,catalog

urlpatterns =[
    path('create-invoice/',login.home,name='home'),
    path('invoice/',invoice.invoice,name='get invoice'),
    path('revenue/',invoice.revenue,name='get revenue'),
    path('home/invoice/create/',invoice.create,name='create invoice'),
    path('account/create/',account.createUserAccount,name='create account now'),
    path('invoice/download/<int:id>/',invoice.download,name='download'),
    path('invoice/delete/<int:id>/',invoice.delete,name='delete invoice'),
    path('invoice/email/<int:id>/',invoice.sendEmail,name='send invoice'),
    path('invoice/edit/<int:id>/',invoice.editInvoice,name='edit invoice'),
    path('invoice/copy/<int:id>/',invoice.copy,name='copy invoice'),
    path('invoice/logout/',login.logOut,name='logOut'),
    path('invoice/profile/',account.profile,name='display the edit html'),
    path('account/update/',account.profileUpdate,name='update account now'),
    path('account/upload/',account.picUpload,name='upload a new picture now'),
    path('administration/', products.admin, name='admin'),
     path('products/', products.productList, name='products'),
     path('market/', market.market, name='market user fronted'),
     path('catalog/<str:name>/', catalog.catalog, name='catalog'),
]
