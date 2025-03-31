from django.contrib import admin
from django.urls import path, include
from blog.views import SignupView, CurrentUserView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/', CurrentUserView.as_view(), name='current_user'),
]