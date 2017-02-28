from setuptools import setup

setup(name="Assignment3",
      version="0.1",
      description="Program to count lit LEDs in a matrix",
      url="",
      author="William Delaney",
      author_email="william.delaney1@ucdconnect.ie",
      licence="GPL3",
      packages=['Assignment3'],
      entry_points={'console_scripts':['comp30670_Assignment3=Assignment3.main:main']})