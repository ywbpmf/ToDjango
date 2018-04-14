from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.urls import path

from mBlog.admin_site import admin_site

sitemaps = {

}

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'
handler403 = 'blog.views.permission.denied_view'

urlpatterns = [
    url(r'^admin/', admin_site.urls)
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
