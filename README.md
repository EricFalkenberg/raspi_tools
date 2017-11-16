# Raspberry Pi Tools
Aides in setup and deployment to Raspberry Pi hosts

## Installation
```
pip install git+https://github.com/EricFalkenberg/raspi_tools.git
```

## Usage

#### Flashing Raspbian onto an SD Card
##### flash_sd
```
Usage: flash_sd [OPTIONS] RASPBIAN_IMAGE

  Flash a rasbian image onto your SD card.

Options:
  --help  Show this message and exit.
```
Provide the script with a raspbian image and follow the instructions to setup your SD card to run Raspbian with headless setup.
```
flash_sd path/to/raspbian/image.img
```
#### Discovering Raspberry Pi Hosts on your Local Area Network (LAN)
##### discover_rpi
###### External Dependencies: nmap
```
Usage: discover_rpi [OPTIONS] [SUBNET]

  Discover Raspberry Pi hosts on local network and deploy to them. Must be
  run as root user.

Options:
  --help  Show this message and exit.
```
This script will return a space separated list of ip addresses corresponding to Raspberry Pi Hosts on your LAN. If no subnet is provided, the script will default to `192.168.0.0/24`. Must be run as root.
```
sudo discover_rpi <my_awesome_subnet>
```
