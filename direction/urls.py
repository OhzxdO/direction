
from django.contrib import admin
from django.urls import path
import dire.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getwords/',views.getwords)
]
