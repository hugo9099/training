from django.views import static
from django.conf.urls.static import static as static_url


def staticfiles_urlpatterns(prefix, doc_root, disable_caching=False):
    """
    Helper function to return a URL pattern for serving static files.
    """
    return static_url(prefix, view=gen_static_serve(doc_root, disable_caching))


def gen_static_serve(document_root, disable_caching):
    def serve(request, path, **kwargs):
        response = static.serve(request, path, document_root=document_root, **kwargs)
        if disable_caching:
            response['Cache-Control'] = 'must-revalidate, no-cache'
        return response

    return serve