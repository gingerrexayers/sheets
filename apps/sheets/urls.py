from django.conf.urls import url

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^create$', views.create, name='create')
]
