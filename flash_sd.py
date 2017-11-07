#!/usr/bin/python
import click
import subprocess
import sys
import os
import time

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
RETRY_COUNT  = 3

def check_success(return_code):
    if return_code != EXIT_SUCCESS:
        sys.exit(EXIT_FAILURE)

def retry_call(sbs_data):
    for i in range(RETRY_COUNT):
        if i == RETRY_COUNT-1:
            ret = subprocess.call(sbs_data)
        else: 
            ret = subprocess.call(sbs_data, stderr=open(os.devnull, 'wb'))
        if ret == EXIT_SUCCESS:
            return ret
        time.sleep(1)
    sys.exit(EXIT_FAILURE)

@click.command()
@click.argument('raspbian_image', type=click.Path(exists=True, resolve_path=True))
def cli(raspbian_image):
    """
    Flash a rasbian image onto your SD card.
    """
    os.devnull
    subprocess.call(['diskutil', 'list'])
    disk = click.prompt('Which of these disks is your SD card?', type=str)
    if click.confirm('Are you sure you want to flash {0}? '.format(disk) + \
                     'Any data on this drive will be overwritten.'):

        click.echo('Unmounting {0}s1'.format(disk))
        # Unmount first partition of specified disk
        ret = subprocess.call(['diskutil', 'unmount', '{0}s1'.format(disk)])
        check_success(ret)
        # Flash SD with image specified by raspbian_image
        click.echo('Writing from:\n\t{0}\nto:\n\t{1}'.format(raspbian_image, disk))
        click.echo('(This takes a while to run. Go grab a coffee or something.)')
        ret = subprocess.call(['sudo', 'dd', 
                               'if={0}'.format(raspbian_image), 
                               'of={0}'.format(disk),
                               'bs=1m'])
        check_success(ret)
        # Create ssh file on SD to enable headless setup
        click.echo('Finishing install and enabling headless setup.')
        retry_call(['touch', '/Volumes/boot/ssh'])
    else:
        sys.exit(EXIT_FAILURE)

    sys.exit(EXIT_SUCCESS) 
        
if __name__ == '__main__':
    cli()

