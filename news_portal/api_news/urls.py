
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *

schema_view = get_schema_view(
    openapi.Info(
        title="NEWS PORTAL API",
        default_version='v1',
        description="NEWS PORTAL API",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="boiovyevhen@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', UserApiUpdate.as_view()),
    path('user_delete/<int:pk>/', UserApiDestroy.as_view()),
    path('category/', CategoryApiView.as_view()),
    path('category/<str:slug_category>/', PostsByCategoryApiView.as_view(), name='category-posts'),
    path('post/', PostApiView.as_view()),
    path('post/<int:pk>/', PostUpdateApiView.as_view()),
    path('post_delete/<int:pk>/', PostDeleteApiView.as_view()),
    path('image/', ImageApiView.as_view()),
    path('image_delete/<int:pk>/', ImageDeleteApiView.as_view()),

]
