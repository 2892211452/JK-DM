"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from cmdb import views  # 导入对应app的视图文件
from django.views.generic.base import TemplateView
from yh import views as yhdm
urlpatterns = [
    url(r'^save/', yhdm.saveU),
    url(r'^load/', yhdm.loadU),
    url(r'^va/', yhdm.va),
    url(r'^search/', yhdm.searchDm),
    url(r'^viewDm/', yhdm.viewDm),
    url(r'^admin/', admin.site.urls),  # 后台管理页面
    url(r"^main/", views.main),  # app路由 url(regex, view, kwargs=None, name=None)
    url(r"^login/", views.login),

    url(r'^test/', views.test),
    url(r"^bili", views.bili),
    url(r'^vue/', TemplateView.as_view(template_name='index.html')),
    url(r'^upL/', views.upload),
]


