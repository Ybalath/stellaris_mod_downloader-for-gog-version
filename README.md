# Stellaris Mod Downloader

This repository contains a tool to download and install in mods for non-Steam version of Stellaris.

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