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

#: Which external javascript compression command to use. The command string
#: can use ``%(outfile)s`` and ``%(infile)s`` placeholders. If the command
#: is ``None`` then the internal ``jsmin`` library is used when :ref:`COMPRESS_JS`
#: is ``True``.
#: 
#: **Default:** ``None`` (Use the internal compression)
JS_COMPRESSION_CMD = getattr(settings, 'STATIC_MEDIA_JS_COMPRESSION_CMD', None)

#: Where should the contents of the media directory inside each entry in 
#: INSTALLED_APPS be installed? If the value is ``None`` then application
#: media will not be copied
#:
#: **Default:** ``settings.MEDIA_ROOT``
APP_MEDIA_PATH = getattr(settings, 'STATIC_MEDIA_APP_MEDIA_PATH', settings.MEDIA_ROOT)

#: List of apps to exclude when copying media to ``APP_MEDIA_PATH``\ . Needs to
#: match the name as listed in ``INSTALLED_APPS``\ .
#: 
#: **Default:** ``()``
EXCLUDE_APPS = getattr(settings, 'STATIC_MEDIA_EXCLUDE_APPS', tuple())

#: A dictionary mapping of extension to compression command. Each command string
#: can use ``%(outfile)s`` and ``%(infile)s`` placeholders.
#:
#: Example::
#: 
#:     STATIC_MEDIA_COMPRESS_IMG_CMDS = {
#:         'png': '/usr/local/bin/optipng -quiet -out %(outfile)s %(infile)s',
#:     }
#:
#: **Default:** ``{}``
COMPRESS_IMG_CMDS = getattr(settings, 'STATIC_MEDIA_COMPRESS_IMG_CMDS', {})

#: A dictionary mapping a (new) file to a combination/concatenation of several
#: other files. The concatenation is done in the order of the list. It will 
#: compress the file according to the :data:`COMPRESS_CSS` and :ref:`COMPRESS_JS` 
#: settings.
#: 
#: Example::
#: 
#:     STATIC_MEDIA_FILE_COMBINATIONS = {
#:         MEDIA_ROOT+'/css/combo.css': [
#:             MEDIA_ROOT+'/css/base.css', 
#:             MEDIA_ROOT+'/css/forms.css', 
#:             MEDIA_ROOT+'/css/coolui.css'],
#:     }
#: **Default:** ``{}``
FILE_COMBINATIONS = getattr(settings, 'STATIC_MEDIA_FILE_COMBINATIONS', {})

#: In order to segregate user uploaded content from the site content, you can
#: use the ``STATIC_URL`` and the static url ``staticmediamgr.context_processor.static_url``
#: to keep things separate.
#: 
#: **Default:** STATIC_URL = MEDIA_URL
STATIC_URL = getattr(settings, 'STATIC_URL', settings.MEDIA_URL)