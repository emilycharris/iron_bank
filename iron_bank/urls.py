"""iron_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bank.views import IndexView, CreateUserView, ProfileView, CreateTransactionView, TransactionDetailView, CreateTransferView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', CreateUserView.as_view(), name='create_user_view'),
    url(r'^profile/$', login_required(ProfileView.as_view()), name='profile_view'),
    url(r'^new_transaction/$', login_required(CreateTransactionView.as_view()), name='create_transaction_view'),
    url(r'^transaction_detail/(?P<pk>\d+)/$', login_required(TransactionDetailView.as_view()), name='transaction_detail_view'),
    url(r'^transfer/$', login_required(CreateTransferView.as_view()), name='create_transfer_view' )
]
