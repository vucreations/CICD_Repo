from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from vite_integration.views import homepage


urlpatterns = [
    # must be at last to catch all non existing routes
    # re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("", homepage, name="homepage"),
    re_path(
        r"^r/.*$", login_required(TemplateView.as_view(template_name="react_base.html"))
    ),
    # without login
    # re_path(
    #     r"^.*$",
    #     TemplateView.as_view(template_name="react_base.html")
    # )
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.ENABLE_DEBUG_TOOLBAR:
#     import debug_toolbar

#     urlpatterns = [
#         path("__debug__/", include(debug_toolbar.urls)),
#     ] + urlpatterns


admin.site.site_header = "Django Todos Vite"
admin.site.site_title = "Django Todos Vite Portal"
admin.site.index_title = "Welcome to the Django Todos Portal"
