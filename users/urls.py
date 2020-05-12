from django.urls import path, include
from users.views import(
    UserViewSet,
    TokenAuthenticationView,
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = "users"

urlpatterns = [
    path('login',obtain_auth_token, name='login'),
    path('authentication', TokenAuthenticationView.as_view(), name='authentication'),
    path('rest-auth/registration', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
