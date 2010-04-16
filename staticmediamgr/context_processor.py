from settings import STATIC_URL

def static_url(request):
    return {'STATIC_URL': STATIC_URL}
