from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('age_likes.urls')),
    path('blog/', include('blog.urls')),
    # path('dv/', include('dataviewer.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Add this line
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
