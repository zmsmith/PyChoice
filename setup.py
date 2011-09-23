#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='pychoice',
      version='1.0',
      description='Makes all your choices',
      author='Zach Smith',
      author_email='zachmsmith@gmail.com',
      packages=find_packages(),
      entry_points={
          'choose': [
              'fab = choice:choose',
          ]
      },
      
)