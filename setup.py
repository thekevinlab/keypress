from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='keypress',
   version='1.0.0',
   description='A scuffed and useless alternative to MechaKeys.',
   license="BSD 3-Clause",
   long_description=long_description,
   author='Synchronous',
   packages=['keypress'], 
   install_requires=['playsound', 'pynput'], 
)