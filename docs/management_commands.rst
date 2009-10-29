.. _management_commands:

===================
Management Commands
===================

``copy_static_media``
=====================

* Combines any files configured in :ref:`STATIC_MEDIA_FILE_COMBINATIONS`\ .

* Copies all media files configured in :ref:`STATIC_MEDIA_COPY_PATHS`\ . Compression is applied according to :ref:`STATIC_MEDIA_COMPRESS_CSS` and :ref:`STATIC_MEDIA_COMPRESS_JS` unless overridden by command-line options.

* Copies all application media unless :ref:`STATIC_MEDIA_APP_MEDIA_PATH` is ``None``.


Options
-------

.. cmdoption:: -c, --compresscss

   Override the :ref:`STATIC_MEDIA_COMPRESS_CSS` setting and compress the css files while copying.


.. cmdoption:: -j, --compressjs

   Override the :ref:`STATIC_MEDIA_COMPRESS_JS` setting and compress the javascript files while copying.


.. cmdoption:: -p, --purge

   Override the :ref:`STATIC_MEDIA_PURGE_OLD_FILES` setting and purge all existing files in the destination before copying.

