from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from app.auth import CustomAuthToken

# Creating Router


router = DefaultRouter()

# Register TodoViewSet with Router

router.register('todoapi', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='auth')),
    # path('gettoken/', obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view()),
]

