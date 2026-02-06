from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classbased/', include('classbased.urls')),
    path('functionbased/', include('functionbased.urls')),
    path('gericbased/', include('gericbased.urls')),
    path('api/', include('api.urls')),
    path('form_exmple/', include('form_exmple.urls')),
]


urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]