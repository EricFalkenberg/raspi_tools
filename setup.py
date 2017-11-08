#!/usr/bin/env python

from setuptools import setup

setup(name="flash_sd",
    version="0.0.1",
    modules=["flash_sd"],
    install_requires=[
        'click'
    ],
    entry_points = {
        'console_scripts' : [
            'flash_sd = src.flash_sd:cli'
        ]
    }
)  

setup(name="discover_rpi",
    version="0.0.1",
    modules=['discover_rpi'],
    install_requires=[
        'click',
        'python-nmap'
    ],
    entry_points = {
        'console_scripts' : [
            'discover_rpi = src.discover_rpi:cli'
        ]
    }
)
