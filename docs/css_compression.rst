.. _css_compression:

===============
CSS Compression
===============

The CSS compression used was ported over from `YUI Compressor <http://developer.yahoo.com/yui/compressor/>`_. It is available separately at `github <http://github.com/coordt/csscompressor>`_. 


Each part of the compression is separated and could technically be turned off, although there is no configuration mechanism for that currently. Some of the regular expressions could fail if other parts are turned off as they may assume that a previous filter has already ran. For example, some of the filters *may* assume the ``normalize_whitespace`` filter has ran and not look for multiple spacing options.

``remove_comments``
===================

Removes multi-line (``/* ... */``) and single line (``// ...``) comments.


``normalize_whitespace``
========================

Convert all whitespace, including line endings, to a single space. This makes manipulation a bit easier.


``convert_boxmodelhack``
========================

Make a pseudo class for the `Box Model Hack <http://tantek.com/CSS/Examples/boxmodelhack.html>`_ that is sometimes used to make Internet Explorer work right. The hack itself could be destroyed by some of the filters, so this filter replaces it with ``___PSEUDOCLASSBMH___`` so it can be restore later.


``restore_boxmodelhack``
========================

Undo what was done with the ``convert_boxmodelhack``.


``remove_extra_spaces``
=======================

Remove the spaces before the things that should not have spaces before them. But, be careful not to turn ``p :link {...}`` into ``p:link{...}``. Swap out any pseudo-class colons with the token, and then swap back.


``add_missing_semicolon``
=========================

Add a semicolon before any ``}`` if it is missing.


``minify_zeros``
================

This filter does several things. First it strips out any measurement unit after a 0, so ``0px`` becomes ``0``. Then it converts measurements with multiple dimensions of zero to just one zero, so ``0 0 0 0`` becomes ``0``.
Finally it strips the leading zero from decimal measurements between zero and one, so ``0.6`` becomes ``.6``.


``shorten_colors``
==================

There are two parts to this filter. The first part converts colors specified using ``rgb(0, 0, 0)`` notation to hex notation (``#000000``).


Next the hex colors are reduced from six characters to three characters if each pair of characters is the same (``#aabbcc`` becomes ``#abc``).


``remove_empty_rules``
======================

Remove any empty rules, such as ``p { }``.


``replace_multiple_semicolons``
===============================

Convert multiple semicolons in a row with just one.
