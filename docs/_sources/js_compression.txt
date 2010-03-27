.. _js_compression:

==============
JS Compression
==============

There are two ways to compress javascript, the first is using a python port of Douglas Crockford's `jsmin <http://www.crockford.com/javascript/jsmin.html>`_ . The second is using a user specified command.

Internal ``jsmin``
==================

Simply set the :ref:`STATIC_MEDIA_COMPRESS_JS` setting to ``True``.

External Command
================

First you must set the :ref:`STATIC_MEDIA_COMPRESS_JS` setting to ``True``.

Then you need to set the :ref:`STATIC_MEDIA_JS_COMPRESSION_CMD` setting to the appropriate command string. The command string should include ``%(infile)s`` and ``%(outfile)s`` placeholders for the in and out file paths.

For example, to use the new `Google Closure Compiler <http://code.google.com/closure/compiler/>`_ your command string might look like::

	java -jar ~/compiler-latest/compiler.jar --js %(infile)s --js_output_file %(outfile)s

