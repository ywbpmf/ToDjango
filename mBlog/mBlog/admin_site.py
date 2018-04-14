from django.contrib.admin import AdminSite

class BlogAdminSite(AdminSite):
    site_header = 'Blog.administration'
    site_title = 'Blog site admin'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser


admin_site = BlogAdminSite(name='admin')
