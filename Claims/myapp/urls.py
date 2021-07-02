
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.contact),
    # path('snippet', views.snippet_detail),
    path('', views.claims, name='claim'),
    path('editform/<str:vechile_num>', views.EDitClaimForm, name='editForm')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
