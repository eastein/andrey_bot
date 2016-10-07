#!/usr/bin/env python

from distutils.core import setup

setup(name='andrey_bot',
      version='0.1.0',
      description='Andrey Bot - a Markov Bot',
      author='Eric Stein',
      author_email='toba@des.truct.org',
      url='https://github.com/eastein/andrey_bot/',
      packages=['andrey_bot'],
      install_requires=['mediorc', 'andrey']
     )
