#!/usr/bin/python
import nmap
import subprocess
import click

RPI_HOST = "Raspberry Pi Foundation"

def discover_rpi(subnet):
    nm = nmap.PortScanner()
    ret = nm.scan(hosts=subnet, arguments='-sS -p 22')
    rpi_list = []
    for ip, scan in ret['scan'].items():
        addrs = scan['addresses']
        if 'mac' in addrs:
            host_type = scan['vendor'][addrs['mac']]
            if host_type == RPI_HOST:
                rpi_list.append(ip)
    return rpi_list
    
@click.command()
@click.argument('subnet', default='192.168.0.0/24')
def cli(subnet):
    """
    Discover Raspberry Pi hosts on local network and deploy
    to them. Must be run as root user.
    """
    try:
        rpi_list = discover_rpi(subnet)
        click.echo(' '.join(rpi_list))
    except nmap.PortScannerError as e:
        click.echo(e.value)

if __name__ == '__main__':
    cli()
