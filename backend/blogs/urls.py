from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('blogs.urls')),  # 👈 This ensures proper routing
    path('api/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
