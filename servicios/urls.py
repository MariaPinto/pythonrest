from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views as authviews

from API.views import Personas, PersonasDetail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    path('personas/', Personas.as_view()),
    path('personas/<int:pk>/', PersonasDetail.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

