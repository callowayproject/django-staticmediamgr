import unittest, os
from staticmediamgr.utils import combine_files
from django.conf import settings

STATIC_MEDIA_FILE_COMBINATIONS = {
    settings.MEDIA_ROOT+'/css/combo.css': [
        settings.MEDIA_ROOT+'/css/base.css', 
        settings.MEDIA_ROOT+'/css/forms.css', 
        settings.MEDIA_ROOT+'/css/coolui.css'],
}

class TestFileCombinations(unittest.TestCase):
    def testCSSFileCombination(self):
        for key, val in STATIC_MEDIA_FILE_COMBINATIONS.items():
            combine_files(key, val)
            
            self.assertTrue(os.path.exists(key))
        