from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('modules.core.urls')),
    path('api/questionnaire/', include('modules.questionnaire.urls')),
    path('nested_admin/', include('nested_admin.urls')),
]
