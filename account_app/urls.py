from django.urls import path, include
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
