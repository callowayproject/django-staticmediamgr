
===============================================
Segregating Your Media from User-uploaded Media
===============================================

By default, Django keeps all static content together. Uploads from ImageFields or FileFields are all stored under the ``MEDIA_ROOT`` path. ``MEDIA_ROOT`` is also where it expects to find your static media as well. You may not want this as user-uploaded content could be a security risk. A common practice is to differentiate between the types by adding ``STATIC_ROOT`` and ``STATIC_URL`` settings.


Template Access
===============

A context processor that will give templates access to the ``STATIC_URL`` setting (defaulting to ``MEDIA_URL``\ ) is available by adding ``staticmediamgr.context_processor.static_url`` to the ``TEMPLATE_CONTEXT_PROCESSORS`` setting, like so::

	TEMPLATE_CONTEXT_PROCESSORS = (
	    "django.contrib.auth.context_processors.auth",
	    "django.core.context_processors.debug",
	    "django.core.context_processors.i18n",
	    "django.core.context_processors.media",
	    "django.contrib.messages.context_processors.messages",
	    "staticmediamgr.context_processor.static_url",
	)

File Upload Access
==================

Django will still save uploaded files under the ``MEDIA_ROOT`` unless you either change the ``DEFAULT_FILE_STORAGE`` or add the ``storage`` parameter to your ``FileField``\ s.

StaticMediaMgr contains a file storage object that defaults to the ``STATIC_ROOT`` and ``STATIC_URL`` settings defined, or else drops back to ``MEDIA_ROOT`` and ``MEDIA_URL``\ . Just add::

	from staticmediamgr.filestorage import StaticMediaStorage
	DEFAULT_FILE_STORAGE = StaticMediaStorage()

to your settings to make it the default, or else add it to your ``FileField`` like::

	photo = models.ImageField(storage=StaticMediaStorage(location='photos/%Y/%b/%d/'))

If you have already changed the ``DEFAULT_FILE_STORAGE`` setting, this is not necessary.