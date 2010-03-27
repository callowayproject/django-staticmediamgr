from distutils.core import setup
try:
    f = open('README.rst', 'r')
    long_description = f.read()
    f.close()
except IOError:
    long_description = ''
import staticmediamgr
version = staticmediamgr.get_version()

setup(name='django-staticmediamgr',
      version=version,
      description='A Django app to copy static media files over to a remote place, optionally minifying css and js.',
      long_description=long_description,
      author='Corey Oordt, The Washington Times',
      author_email='coordt@washingtontimes.com',
      url='http://opensource.washingtontimes.com/projects/django-staticmediamgr/',
      packages=['staticmediamgr'],
      classifiers=['Development Status :: 4 - Beta',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            ],
)
