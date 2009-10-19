.. _management_commands:

===================
Management Commands
===================

``copy_static_media``
=====================

Copies all media files configured in :ref:`STATIC_MEDIA_COPY_PATHS`\ .

Options
-------

.. cmdoption:: -c, --compresscss

   Override the :ref:`STATIC_MEDIA_COMPRESS_CSS` setting and compress the css files while copying.


.. cmdoption:: -j, --compressjs

   Override the :ref:`STATIC_MEDIA_COMPRESS_JS` setting and compress the javascript files while copying.


.. cmdoption:: -p, --purge

   Override the :ref:`STATIC_MEDIA_PURGE_OLD_FILES` setting and purge all existing files in the destination before copying.

