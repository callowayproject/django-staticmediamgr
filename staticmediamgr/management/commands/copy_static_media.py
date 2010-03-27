import os, shutil, re, glob
from optparse import OptionParser, make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from staticmediamgr import settings as sm_settings
from staticmediamgr import utils

class Command(BaseCommand):
    """
    Copy all the static media to a new place as configured in ``settings.py``
    """
    help = 'Copy static media to a new place(s) as configured in settings.py'
    
    option_list = BaseCommand.option_list + (
        make_option("-c", "--compresscss", action="store_true", dest="compress", default=False, help='Compress css files, overriding "STATIC_MEDIA_COMPRESS_CSS".'),
        make_option("-j", "--compressjs", action="store_true", dest="compress", default=False, help='Compress javascript files, overriding "STATIC_MEDIA_COMPRESS_JS".'),
        #make_option("-v", "--version", action="store_true", dest="version", default=False, help="Appends a SHA1 hash to the end of each file based on the file's contents"),
        make_option("-p", "--purge", action="store_true", dest="purge", default=sm_settings.PURGE_OLD_FILES, help='Override the "STATIC_MEDIA_PURGE_OLD_FILES" setting on handling the files in destination directories.'),
    )
    
    def handle(self, *args, **kwargs):
        self.options = kwargs
        for key, val in sm_settings.FILE_COMBINATIONS.items():
            combine_files(key, val)
        if self.options['purge'] or sm_settings.PURGE_OLD_FILES:
            for configitem in sm_settings.COPY_PATHS:
                try:
                    shutil.rmtree(configitem['to'])
                    os.makedirs(configitem['to'])
                except OSError:
                    pass # Probably trying to remove the same destination twice
        for configitem in sm_settings.COPY_PATHS:
            for item in glob.iglob(configitem['from']):
                utils.copy(item, configitem['to'], purge=False)
        utils.copy_app_media()
