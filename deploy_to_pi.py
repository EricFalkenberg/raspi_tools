import nmap
import subprocess
import click

RPI_HOST = "Raspberry Pi Foundation"

def discover_rpi(subnet):
    click.echo("Searching for Raspberry Pi hosts on LAN")
    nm = nmap.PortScanner()
    ret = nm.scan(hosts=subnet, arguments='-sS -p 22')
    rpi_list = []
    for ip, scan in ret['scan'].items():
        addrs = scan['addresses']
        if 'mac' in addrs:
            host_type = scan['vendor'][addrs['mac']]
            if host_type == RPI_HOST:
                rpi_list.append(ip)
    click.echo("Pi's found: {0}".format(len(rpi_list))) 
    return rpi_list
    
def deploy_pi(rpi_list):
    for rpi in rpi_list:
        ssh = subprocess.call(['ssh', 'pi@{0}'.format(rpi), 'uname'])

@click.command()
@click.argument('subnet', default='192.168.0.0/24')
def cli(subnet):
    """
    Discover Raspberry Pi hosts on local network and deploy
    to them. Must be run as root user.
    """
    rpi_list = discover_rpi(subnet)
    deploy_pi(rpi_list)

if __name__ == '__main__':
    cli()
