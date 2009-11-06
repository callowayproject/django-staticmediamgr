import os, shutil, settings, csscompressor, jsmin

def compress_copy(src, dst, replace_files=True, compress_css=settings.COMPRESS_CSS, compress_js=settings.COMPRESS_JS):
    """
    A wrapper around ``shutil.copy2`` to optionally compress javascript or css
    files.
    
    :param src:
        The path to the original file/directory
    :type src: 
        ``string``
    :param dst: 
        The path to the destination file/directory
    :type dst: 
        ``string``
    :param compress_css:
        Should CSS files be compressed. **Default:** False
    :type compress_css:
        ``bool``
    :param compress_js:
        Should javascript files be compressed. **Default:** False
    :type compress_js:
        ``bool``
    """
    root, ext = os.path.splitext(src)
    
    if not replace_files and os.path.exists(dst):
        return
    
    if compress_css and ext == '.css':
        mincss = csscompressor.compress_cssfile(src)
        fileptr = open(dst, 'w').write(mincss)
        if fileptr:
            fileptr.close()
    elif compress_js and ext == '.js':
        if settings.JS_COMPRESSION_CMD:
            os.system(settings.JS_COMPRESSION_CMD % {'infile': src, 'outfile': dst})
        else:
            js = open(src).read()
            minjs = jsmin.jsmin(js)
            fileptr = open(dst, 'w').write(minjs)
            if fileptr:
                fileptr.close()
    else:
        shutil.copy2(src, dst)

def copydir(src, dst, replace_files=True):
    """
    A port of the recursive shutil.copytree, except it assumes the 
    destination directory exists.
    
    :param src:
        The path to the original file/directory
    :type src: 
        ``string``
    :param dst: 
        The path to the destination file/directory
    :type dst: 
        ``string``
    """
    names = os.listdir(src)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.isdir(srcname):
                if not os.path.exists(dstname):
                    os.makedirs(dstname)
                copydir(srcname, dstname, replace_files)
            else:
                #shutil.copy2(srcname, dstname)
                compress_copy(srcname, dstname, replace_files)
        except (IOError, os.error), why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Exception, err:
            errors.append(err.args[0])
    try:
        shutil.copystat(src, dst)
    except OSError, why:
        errors.append((src, dst, str(why)))
    except:
        # can't copy file access times on Windows
        pass
        
    if errors:
        raise Exception, errors


def copy(original, destination, purge=settings.PURGE_OLD_FILES, replace_files=True):
    """
    Do the file copying with all the appropriate error checking. Don't replace 
    an existing file if ``replace_files`` is ``False``
    
    :param original:
        The path to the original file/directory
    :type original: 
        ``string``
    :param destination: 
        The path to the destination file/directory
    :type destination: 
        ``string``
    :param purge:
        Should directories be emptied before copying. **Default:** ``settings.PURGE_OLD_FILES``
    :type purge:
        ``bool``
    :param replace_files:
        Should existing files be over-written (``True``) or kept (``False``). 
        Whole directories will *not* be over-written. Each file within a directory
        will be evaluated. **Default:** ``True``
    :type replace_files:
        ``bool``
    """
    # Check if the original exists
    if not os.path.exists(original):
        print "Can't access %s or it doesn't exist." % original
        return
    
    # If original is a file, copy it over
    if os.path.isfile(original):
        if os.path.isdir(destination):
            dst_file = os.path.join(destination, os.path.basename(original))
        else:
            dst_file = destination
        if os.path.exists(dst_file) and replace_files:
            shutil.copy2(original, dst_file)
    
    # if original is a directory, check for an existing directory
    # Empty it out if configured
    if os.path.isdir(original):
        if os.path.exists(destination) and purge:
            shutil.rmtree(destination)
            os.makedirs(destination)
        elif os.path.exists(destination) and not os.path.isdir(destination):
            print "The destination (%s) for directory %s is a file instead of a directory." % (destination, original)
            return
        elif not os.path.exists(destination):
            os.makedirs(destination)
        copydir(original, destination, replace_files)


def copy_app_media(destination=settings.APP_MEDIA_PATH):
    """
    Copy each application's media files to the path specified in 
    ``STATIC_MEDIA_APP_MEDIA_PATH``. Won't do any of the django.contrib 
    applications.
    """
    from django.utils import importlib
    from django.conf import settings as global_settings
    
    if destination is None:
        return
    for app in global_settings.INSTALLED_APPS:
        if 'django.contrib' in app:
            continue
        mod = importlib.import_module(app)
        app_media_path = os.path.join(os.path.abspath(mod.__path__[0]), 'media')
        if os.path.exists(app_media_path) and os.path.isdir(app_media_path) and not os.path.exists(os.path.join(app_media_path, '__init__.py')):
            copy(app_media_path, destination, purge=False, replace_files=False)


def combine_files(destination, path_list):
    """
    Combine the files in ``path_list`` to create one file at ``destination``.
    
    :param destination: The full file path of the resulting file
    :type destination: ``string``
    :param path_list: A list of full file paths that should be combined
    :type path_list: ``list``
    """
    result_file = open(destination, 'w')
    
    try:
        try:
            for item in path_list:
                result_file.write(file(item).read())
                result_file.write('\n')
        finally:
            result_file.close()
    except IOError:
        # If there was a problem, don't leave a bad file lying around
        try:
            if os.path.exists(destination):
                os.remove(destination)
        except:
            pass
        raise