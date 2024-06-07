from django.urls import path
from common.views import CreateCustomerView, LoginView, CustomerListView, UploadDocumentView, ExtractDataView, DocumentListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
"""customer_ocr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('create/', CreateCustomerView.as_view()),
    path('upload/', UploadDocumentView.as_view()),
    path('document/', DocumentListView.as_view()),
    path('extract/', ExtractDataView.as_view()),
    path("", CustomerListView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]
