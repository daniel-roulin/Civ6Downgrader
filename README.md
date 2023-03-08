# Sid Meier's Civilization VI Downgrader

Script to downgrade Sid Meier's Civilization VI to version 1.0.12.28 (15 December 2022).
This is sometimes necessary to play with MacOS players.

> **Note:** This script was only tested on Linux and will VERY PROBABLY not work on Windows or MacOS.

> **Note:** You obviously need to possess Civilization VI on Steam to be able to use this script.

### Requirements
- Python 3
- A steam account possessing Civilization VI on Steam

### Usage
Clone or download this repository
```
git clone https://github.com/DanielRoulin/Civ6Downgrader.git
cd Civ6Downgrader
```

Run the script
```
python3 main.py
```

When prompted, enter your Steam username and password. You will probably also be askes an authentication code which will sent to you by email.

Then, you need to wait for the installation to finish. This might take some time, depending on your network.

Finally, you should be able to launch Civilization VI through Steam. Note however that it may crash the first time you try. In that case, try running the game a second time.

### How to update the game after running this script
To prevent Steam from automatically updating Civilization VI to the latest version, this script edits some configuration files. To revert the game to its original configuration, the easiest way is to uninstall and reinstall the game.

However, you can also edit the configuration file manually, by following [this guide](https://steamcommunity.com/sharedfiles/filedetails/?id=885555151). This file can be found here: `~/.steam/debian-installation/steamapps/appmanifest_289070.acf`

### References
- This code is basically an implementation of [this article](https://steamcommunity.com/sharedfiles/filedetails/?id=2353930763) by Wooden Spirit.
- Therefore, it uses a compiled for linux version of [SteamRE's DepotDownloader](https://github.com/SteamRE/DepotDownloader) to download the game. 
- In addition, to prevent Steam from automatically update the game, this script uses [leovp's acf parser](https://github.com/SteamRE/DepotDownloader) to edit some configuration files.

### Notes
This script is not affiliated with Steam or Sid Meier's Civilization VI in any way. Use it at your own risk. 
