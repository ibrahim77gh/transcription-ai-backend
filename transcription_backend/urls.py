from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('authentication.urls')),
    path('auth/', include('transcription.urls')),
    # path('auth/', include('djoser.social.urls')),
]

# We are telling Django to make a new endpoint /media, and any request made to this endpoint should be routed to MEDIA_ROOT file system.
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
