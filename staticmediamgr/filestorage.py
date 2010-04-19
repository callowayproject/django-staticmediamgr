from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

DEFAULT_ROOT = getattr(settings, 'STATIC_ROOT', settings.MEDIA_ROOT)
DEFAULT_URL = getattr(settings, 'STATIC_URL', settings.MEDIA_URL)

class StaticMediaStorage(FileSystemStorage):
    """
    A way to segregate the system files and user-uploaded files.
    
    The ``location`` parameter looks first for ``STATIC_ROOT`` and then
    falls back to ``MEDIA_ROOT``\ . The ``base_url`` parameter looks for
    ``STATIC_URL`` and then falls back to ``MEDIA_URL``\ .
    
    To use this by default, in your settings.py ::
    
    DEFAULT_FILE_STORAGE = 'staticmediamgr.storage.StaticMediaStorage'
    
    For FileFields and ImageFields, you can pass a relative location and it
    will store your uploaded files under that combined path. For example::
    
    photo = ImageField(storage=StaticMediaStorage(location='photos/%Y/%b/%d/'))
    
    The uploaded files would be stored under ``STATIC_ROOT/photos/%Y/%b/%d/``
    """
    def __init__(self, location='', base_url='', *args, **kwargs):
        real_location = os.path.join(DEFAULT_ROOT, location)
        real_base_url = DEFAULT_URL + base_url
        super(StaticFileStorage, self).__init__(real_location, real_base_url, *args, **kwargs)
