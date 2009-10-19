import os, shutil, settings, csscompressor, jsmin

def compress_copy(src, dst, compress_css=settings.COMPRESS_CSS, compress_js=settings.COMPRESS_JS):
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
    
    if compress_css and ext == '.css':
        mincss = csscompressor.compress_cssfile(src)
        fileptr = open(dst, 'w').write(mincss)
        if fileptr:
            fileptr.close()
    elif compress_js and ext == '.js':
        js = open(src).read()
        minjs = jsmin.jsmin(js)
        fileptr = open(dst, 'w').write(minjs)
        if fileptr:
            fileptr.close()
    else:
        shutil.copy2(src, dst)

def copydir(src, dst):
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
                copydir(srcname, dstname)
            else:
                #shutil.copy2(srcname, dstname)
                compress_copy(srcname, dstname)
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


def copy(original, destination, purge=settings.PURGE_OLD_FILES):
    """
    Do the file copying with all the appropriate error checking.
    
    :param original:
        The path to the original file/directory
    :type original: 
        ``string``
    :param destination: 
        The path to the destination file/directory
    :type destination: 
        ``string``
    """
    # Check if the original exists
    if not os.path.exists(original):
        print "Can't access %s or it doesn't exist." % original
        return
    
    # If original is a file, copy it over
    if os.path.isfile(original):
        shutil.copy2(original, destination)
    
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
        copydir(original, destination)
        
            