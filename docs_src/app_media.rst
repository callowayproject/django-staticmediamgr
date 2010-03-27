.. _app_media:

=================
Application Media
=================

There are two ways to handle application media: manual and automatic. 


Manual Copying
==============

The manual method is where you add an entry for each application in :ref:`STATIC_MEDIA_COPY_PATHS`\ . ::

	STATIC_MEDIA_COPY_PATHS = (
	    {'from': settings.MEDIA_ROOT, 'to': '/mnt/mediaserver/media/'},
	    {'from': 'apps/coolapp/media/', 'to': '/mnt/mediaserver/media/'},
	)

This gives you some control over where each application's media files are stored.

.. note::

   If the application's media files are not in a directory named ``media``, then this is the only way you can copy the application's media files.


Automatic Copying
=================

The automatic copying of application media consists of searching for a directory named ``media`` in each installed application, with the exception of django contrib applications, and copying the contents to :ref:`STATIC_MEDIA_APP_MEDIA_PATH`\ .


Overriding Application Media Files
**********************************

Sometimes you might want to replace one or more of an existing application's media files with one of your own. This is easy to do. Simply put the file(s) in the ``MEDIA_ROOT`` directory with the same relative path as the application's media.

For example, if an application had a structure ::

	coolapp/
	  admin.py
	  media/
	    coolapp/
	      css/
	        base.css
	        forms.css
	      img/
	        logo.png
	  models.py
	  templates/
	  urls.py

You would override the ``base.css`` file by putting your file ::

	media/
	  css/
	  img/
	  js/
	  coolapp/
	    css/
	      base.css

During the copying process, your existing file(s) will **not** be overwritten.

By default, automatic copying is turned on. The :ref:`STATIC_MEDIA_APP_MEDIA_PATH` setting is ``MEDIA_ROOT``. Turn off automatic copying by setting :ref:`STATIC_MEDIA_APP_MEDIA_PATH` to ``None``.