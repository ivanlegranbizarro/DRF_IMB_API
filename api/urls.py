from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="IMB API Clone",
        default_version='v1',
        description="The Clone of the IMB API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'own_api'

urlpatterns = [
    path('all_movies/', views.ListMovieView.as_view()),
    path('add_movie/', views.CreateMovieView.as_view()),
    path('movie/<str:title>/', views.RetrieveMovieView.as_view()),
    path('genre/', views.ListCreateGenreView.as_view()),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
