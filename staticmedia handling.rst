=============================
Static Media Management Goals
=============================

* Copies files from one path to another. e.g. Copy all files from ``media/*`` to ``/mnt/media/``
* Handles application media

  - Looks for media directories for each installed app.
  - Allows for "overrides" similar to templates
  - Copies files from app/media/ directory to media/ directory, but doesn't replace any files already there.
  - Has a "collect" function that just does the above. The function that copies all media somewhere else ("deploy"?), will call this function first.

* Partial functionality found in:

  - http://pypi.python.org/pypi/django-staticmedia/0.2
  - http://github.com/bradleywright/django-static-management

* Optionally minify javascript and css
* Optionally combine javascript files or css files into one file

  - Create the groups in the admin
  - Files used are read from the filesystem

    + Optional upload of files, if not using version control

* Optionally version content

  - Need a way to track versions, or that there is a new version.
  - Possibly:

    1. Checkbox next to files to allow for versioning.
    2. Versioning puts a filename & sha1 hash in the database

       a. Will have to have a detection if file is deleted/not found
       b. Marry up the listing with the file system

    3. Also has a counter for a version number in the row
    4. A template tag is used for the file url in templates: ::

			{% static_media_file forms.css 2 %} 

       Where ``forms.css`` is the file name and ``2`` is the optional version number. Leaving off the version number puts in the current version