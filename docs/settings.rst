.. _settings:

========
Settings
========

.. _static_media_copy_paths:

STATIC_MEDIA_COPY_PATHS
=======================

The configuration of which path(s) should be copied where. It consists of a tuple of dicts. Each dict requires a ``from`` key and a ``to`` key. ::

    STATIC_MEDIA_COPY_PATHS = (
        {'from': MEDIA_ROOT, 'to': '/mnt/MediaServer/media/'},
    )

If you are copying everything from your ``MEDIA_ROOT``, the above configuration would suffice. You can get more specific, as well. ::

    STATIC_MEDIA_COPY_PATHS = (
        {'from': MEDIA_ROOT+'/css/', 'to': '/mnt/MediaServer/media/css/'},
        {'from': MEDIA_ROOT+'/js/', 'to': '/mnt/MediaServer2/media/js/'},
        {'from': MEDIA_ROOT+'/img/', 'to': '/mnt/MediaServer3/media/img/'},
    )

The string in the ``from`` entry can be relative to the project path, or absolute. It can point to a file or a directory.


.. _static_media_purge_old_files:

STATIC_MEDIA_PURGE_OLD_FILES
============================

When copying a directory, should the directory at the new location be emptied first (``True``) or left as-is (``False``). The default is ``True``.


.. _static_media_compress_css:

STATIC_MEDIA_COMPRESS_CSS
=========================

Should CSS files be compressed using a port of the `YUI Compressor <http://developer.yahoo.com/yui/compressor/>`_ when copied (``True``) or left as-is (``False``). The default is ``False``.

The compression simply removes excess whitespace and comments and shortens colors and zero measurements. It does not alter any rules or combine any rule attributes. See :ref:`css_compression` for more detailed information.


.. _static_media_compress_js:

STATIC_MEDIA_COMPRESS_JS
========================

Should Javascript files be compressed using a port of Douglas Crockford's `jsmin <http://www.crockford.com/javascript/jsmin.html>`_. The default is ``False``.
