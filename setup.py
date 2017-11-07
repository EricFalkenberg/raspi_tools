#!/usr/bin/env python

from setuptools import setup

setup(name="tools",
    version="0.0.1",
    py_modules=['tools'],
    install_requires=[
        'click',
        'python-nmap'
    ],
    entry_points='''
        [console_scripts]
        flash_sd=src.flash_sd:cli
        deploy_to_pi=src.deploy_to_pi:cli
    ''',
)  
