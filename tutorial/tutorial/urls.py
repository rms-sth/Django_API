from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.schemas import get_schema_view # new

schema_view = get_schema_view(title='Pastebin API') # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),  # new
    path('schema/', schema_view),  # new

]

# urlpatterns = format_suffix_patterns(urlpatterns)
