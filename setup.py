#! /usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup


setup(name="python-tucam",
      version='0.0.2',
      description='TUCAM API',
      url='https://github.com/RAA80/python-tucam',
      author='Alexey Ryadno',
      author_email='aryadno@mail.ru',
      license='MIT',
      packages=['tucam', 'tucam.libs'],
      package_data={"tucam": ["libs/win32/*.dll",
                              "libs/win64/*.dll",
                              "libs/linux/*.*"]},
      platforms=['Windows', 'Linux'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Operating System :: POSIX',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                  ]
     )
