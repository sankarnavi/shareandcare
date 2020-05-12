
from django.contrib import admin
from django.urls import include, path
from Communications import views
from django.conf.urls.static import static
from shareandcare import settings
urlpatterns = [
    path('connect/<id>/', views.Contactdetails, name='Contactdetails'),
    path('Accept/<id>', views.Accept, name='Accept'),
    path('Reject/<id>', views.Reject, name='Reject'),
    path('Delete/<id>', views.Delete, name='Delete'),
]
