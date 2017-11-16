#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="raspi_tools",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'python-nmap'
    ],
    entry_points = {
        'console_scripts' : [
            'flash_sd = src.flash_sd:cli',
            'discover_rpi = src.discover_rpi:cli'
        ]
    }
)  
