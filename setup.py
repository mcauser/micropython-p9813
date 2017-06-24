import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-p9813',
    py_modules=['p9813'],
    version='1.0.0',
    description='MicroPython library for the P9813 RGB LED driver.',
    long_description='This library lets you control individual or a strip of P9813 based RGB LEDs.',
    keywords='p9813 rgb led micropython',
    url='https://github.com/mcauser/micropython-p9813',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)