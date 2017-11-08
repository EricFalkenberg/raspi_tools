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

setup(name="deploy_to_pi",
    version="0.0.1",
    modules=['deploy_to_pi'],
    install_requires=[
        'click',
        'python-nmap'
    ],
    entry_points = {
        'console_scripts' : [
            'deploy_to_pi = src.deploy_to_pi:cli'
        ]
    }
)
