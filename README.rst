=====================
Django-StaticMediaMgr
=====================

**New in version 0.4:** Fixed a bug where copying multiple directories into the same directory with the purge options would only allow the last copy to work. Now multiple source directories can be copied into one destination, with each successive copy potentially overwriting the previous files.

**New in version 0.3:** Added support for external javascript compression commands, such as Google's compressor.

**New in version 0.2:** Ability to combine multiple files into a new file before copying and/or compressing them.

This app provides a way to copy and consolidate static media files to one or more configured locations. This is incredibly helpful if you have your media served from another server.

It consists of a management command, ``copy_static_media``, and several settings including:

* ``STATIC_MEDIA_COPY_PATHS``  A tuple of dictionaries specifying the from/to for copying files.

* ``STATIC_MEDIA_PURGE_OLD_FILES``  Should old files be purged from the destination directory.

* ``STATIC_MEDIA_COMPRESS_CSS``  Should CSS files be compressed during copy using the included port of `YUI Compressor <http://developer.yahoo.com/yui/compressor/>`_ 

* ``STATIC_MEDIA_COMPRESS_JS``  Should javascript files be compressed during copy using the included python port of Douglas Crockford's `jsmin <http://www.crockford.com/javascript/jsmin.html>`_

* ``STATIC_MEDIA_APP_MEDIA_PATH``  Where (and if) should the application media be copied to automatically.

* ``STATIC_MEDIA_FILE_COMBINATIONS`` Configuration of combining multiple files into one.


TODO
====

* Allow lossless image compression for pngs, gifs and jpegs using external tools like optiPNG.

* Create a template tag to minify inline CSS and javascript with caching



