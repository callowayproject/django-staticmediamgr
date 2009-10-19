from django.conf import settings

DEFAULT_COPY_PATHS = (
    {'from':settings.MEDIA_ROOT, 'to':'/mnt/media/'},
)

#: The configuration of which path(s) should be copied where. It consists of a 
#: ``tuple`` of ``dict``\ s. Each ``dict`` requires a ``from`` key and a 
#: ``to`` key. 
#: 
#: **Default:** configured to copy the ``MEDIA_ROOT`` to ``/mnt/media/``
COPY_PATHS = getattr (settings, 'STATIC_MEDIA_COPY_PATHS', 'DEFAULT_COPY_PATHS')

#: When copying a directory, should the directory at the new location be emptied
#: first (``True``) or left as-is (``False``). Left as-is is crucial if versioning
#: 
#: **Default:** True
PURGE_OLD_FILES = getattr(settings, 'STATIC_MEDIA_PURGE_OLD_FILES', True)

#: Should CSS files be compressed?
#: 
#: **Default:** ``False``
COMPRESS_CSS = getattr(settings, 'STATIC_MEDIA_COMPRESS_CSS', False)

#: Should javscript files be compressed?
#: 
#: **Default:** ``False``
COMPRESS_JS = getattr(settings, 'STATIC_MEDIA_COMPRESS_JS', False)