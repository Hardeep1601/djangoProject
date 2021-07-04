
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # path('register/', views.registerPage, name="register"),
	path('delete', views.delete_request, name="delete"),
	path('logout/', views.logout_request, name="logout"),

    path('', views.login_request, name="home"),
    path('dashboard', views.homepage, name='dashboard'),

    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('claim', views.claims, name='claim'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
