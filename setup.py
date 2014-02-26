from setuptools import setup
from glob import glob

setup(name='besancon_query',
        version='0.0.1',
        author='Simon Walker',
        author_email='s.r.walker101@googlemail.com',
        packages=['besancon_query', ],
        package_dir={'': 'src'},
        scripts=glob('bin/*.py'),
        long_description=open('README.markdown').read(),
        )
