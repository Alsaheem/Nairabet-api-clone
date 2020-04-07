from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing page and API documentation
    path('', include_docs_urls(title='Project\'s API Documentation')),

    # Authentication
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # API endpoints
    path('api/v1/', include([
        path('bets/', include('betcore.urls')),
        path('users/', include('users.urls')),
        path('payment/', include('paymentgateway.urls')),
        ])),
    
]
