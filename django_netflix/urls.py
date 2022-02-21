from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

app_name = 'core'

urlspatterns = [
  path('admin/', admin.site.urls),
  path('', include('core.urls',namespace='core'))
]