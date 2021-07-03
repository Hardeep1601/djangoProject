
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # path('register/', views.registerPage, name="register"),
	# path('login/', views.loginPage, name="login"),
	# path('logout/', views.logoutUser, name="logout"),
    #
    path('', views.login_request, name="home"),
    # path("", views.homepage, name="homepage"),

    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('claim', views.claims, name='claim'),
    path('editform/<str:vechile_num>', views.EDitClaimForm, name='editForm')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
