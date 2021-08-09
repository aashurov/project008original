
from django.contrib import admin
from django.urls import path, include, re_path
from Users.forms import UserForm
from django_registration.backends.one_step.views import RegistrationView
from main.views import Index
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Moneys.urls')),
    path('api/', include('Services.urls')),
    path('api/', include('Users.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('rest_framework.urls')),
    path('accounts/register/', RegistrationView.as_view(form_class=UserForm, success_url='/'), name='register'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^.*$', Index.as_view(), name="index"),

]
