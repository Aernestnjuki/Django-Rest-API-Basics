from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('', views.endpoints, name='devs'),
    path('developers/', views.developers_list, name='dev-lists'),
    path('developers/<str:username>/', views.developer_details, name='dev-info'),
    # path('developers/<str:username>/', views.DeveloperDetails.as_view(), name='dev-info'),

    # access-tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # company urls
    path('companies', views.companies_list, name='companies-list')
]