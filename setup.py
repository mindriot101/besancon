from setuptools import setup
from glob import glob

setup(name='besancon',
        version='0.0.1',
        author='Simon Walker',
        author_email='s.r.walker101@googlemail.com',
        packages=['besancon', ],
        package_dir={'': 'src'},
        long_description=open('README.markdown').read(),
        )
