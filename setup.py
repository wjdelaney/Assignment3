from setuptools import setup

setup(name="Assignment3",
      version="0.1",
      description="Program to count lit LEDs in a matrix",
      url="",
      author="William Delaney",
      author_email="william.delaney1@ucdconnect.ie",
      license="GPL3",
      packages=['Assignment3'],
      entry_points={'console_scripts':['solve_led=Assignment3.main:main']})