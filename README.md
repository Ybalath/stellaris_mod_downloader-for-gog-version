# Stellaris Mod Downloader

This repository contains a tool to download and install in mods for gog version of Stellaris.
This script intends to automate instalation process for mods in gog version of Stellaris. 

Script downloads mods provided in modlist.txt file and downloads them from steam workshop. Next step is to copy mod files to stellaris mod folder loceted in Documents folder and add descriptor.mod file with updated path so paradox launcher can recognise mods.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/stellaris_mod_downloader.git
    ```
2. Downaload [steamCMD](https://developer.valvesoftware.com/wiki/SteamCMD)

## Usage
1. Add mods ID from steam workshop to modlist.txt

2. Run the script:
    ```sh
    python main.py
    ```
    First run will take longer as steamCMD will need to download all files. 

## TODO
- add more customisation options for download and installation process
- make installation more verbose
- add GUI?