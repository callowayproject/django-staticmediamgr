.. _getting_started:

===============
Getting Started
===============

Installation
============

1. **Install the package.**
   
   **From Source Checkout**\ : ::
   
   	git clone http://opensource.washingtontimes.com/git/public/django-staticmediamgr.git/
   	cd django-staticmediamgr
   	python setup.py install
   
   **From PyPI**\ : ::
   
   **Comming soon**

2. **Add to INSTALLED_APPS.** In your projects ``settings.py`` file, add ``staticmediamgr`` to ``INSTALLED_APPS``\ .

3. **Configure Settings.** In ``settings.py`` or ``local_settings.py`` configure at least :ref:`STATIC_MEDIA_COPY_PATHS` and possibly :ref:`STATIC_MEDIA_COMPRESS_CSS` and :ref:`STATIC_MEDIA_COMPRESS_JS`\ .


Local Development vs. Production
================================

For local development, assuming you are using a ``local_settings.py`` file, set your :ref:`STATIC_MEDIA_COPY_PATHS` to a path that is not versioned with version control. Then configure django to serve media from that directory.

In ``local_settings.py``\ : ::

	STATIC_MEDIA_COPY_PATHS = (
	    {'from': 'media', 'to': 'media2'},
	)

Then in ``urls.py``\ : ::

	urlpatterns += patterns('',
	    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
	        {'document_root': os.path.join(os.path.basedir(__file__), 'media2')}),
	)


Using Static Media Manager
==========================

Static Media Manager creates a management command ``copy_static_media``\ . To copy all your static media simply: ::

	./manage.py copy_static_media


