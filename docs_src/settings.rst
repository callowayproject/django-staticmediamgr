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


.. _static_media_js_compression_cmd:

STATIC_MEDIA_JS_COMPRESSION_CMD
===============================

Which external javascript compression command to use. The command string can use ``%(outfile)s`` and ``%(infile)s`` placeholders. If the value is ``None`` then the internal ``jsmin`` library is used when :ref:`STATIC_MEDIA_COMPRESS_JS` is ``True``. The default is ``None`` (Use the internal compression)


.. _static_media_app_media_path:

STATIC_MEDIA_APP_MEDIA_PATH
===========================

Where should the contents of the media directory inside each entry in ``INSTALLED_APPS`` be installed? If the value is ``None`` then application media will not be copied. The default is ``MEDIA_ROOT``\ .

Application media will not overwrite existing files, so it is possible for you to override one, several or all of the files in a given application's media.


.. _static_media_file_combinations:

STATIC_MEDIA_FILE_COMBINATIONS
==============================

A dictionary mapping a (new) file to a combination/concatenation of several other files. The concatenation is done in the order of the list. The resulting file will be compressed according to the :data:`COMPRESS_CSS` and :data:`COMPRESS_JS` settings.

For example, to combine three CSS files into one ``combo.css`` file::

    STATIC_MEDIA_FILE_COMBINATIONS = {
        MEDIA_ROOT+'/css/combo.css': [
            MEDIA_ROOT+'/css/base.css', 
            MEDIA_ROOT+'/css/forms.css', 
            MEDIA_ROOT+'/css/coolui.css'],
    }

.. note::
   File combinations are done before anything else, so make the destination path for combination files be in a directory configured in a ``from`` key in :ref:`STATIC_MEDIA_COPY_PATHS`.

The original files are not touched and the destination file can safely reside with them. The default setting is an empty dictionary.