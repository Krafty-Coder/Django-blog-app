from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.views.generic import TemplateView

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap.xml$',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^$', TemplateView.as_view(template_name='link/index.html')),
    url(r'^work/', TemplateView.as_view(template_name='link/index.html')),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^7i3d4foued8o7d97x12wcsicjkiq4t.html/', TemplateView.as_view(template_name='link/7i3d4foued8o7d97x12wcsicjkiq4t.html')),
]