"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('register', views. register),
    path('login', views.login),
    path('landingpage', views.landingpage),
    path('upload', views.upload, name= 'upload'),
    path('books', views.book_list, name = 'book_list'),
    path('books/upload', views.upload_book, name = 'upload_book'),
    path('delete/<int:prop_id>', views.delete),
    path('addfaves/<int:prop_id>', views.addfaves),
    path('removejob/<int:prop_id>', views.removejob),
    path('showprop/<int:prop_id>', views.showprop),
    path('editfaves/<int:prop_id>', views.editfaves, name = "editpage"),
    path('updateposting/<int:prop_id>', views.updateposting),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)