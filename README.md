# Sid Meier's Civilization VI Downgrader

Script to downgrade Sid Meier's Civilization VI to version 1.0.12.28 (15 December 2022).
This is sometimes necessary to play with mac players.

> **Note:** This script was only tested on Linux and wil VERY PROBABLY not work on Windows or MacOS

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

When prompted, enter your Steam username and password and an authentication code sent to you by email if needed.

Then, you need to wait for the installation to finish. This might take some time, depending on your network.

Finally, you should be able to launch Civilization VI through Steam. Note however that it may crash the first time you try. In that case, try launching the game a second time.

### How to update the game after running this script
To prevent Steam from automatically updating Civilization VI to the latest version, this script edits some configuration files. To revert the game to its original configuration, the easiest way is to uninstall and reinstall the game.

Otherwise, you can edit the configuration file yourself, by following [this guide](https://steamcommunity.com/sharedfiles/filedetails/?id=885555151). This file can be found in `~/.steam/debian-installation/steamapps/appmanifest_289070.acf`

### Notes
This script is not affiliated with Steam or Sid Meier's Civilization VI in any way. USe it at your own risk. 

### References
- This code is basically an implementation of [this article](https://steamcommunity.com/sharedfiles/filedetails/?id=2353930763) by Wooden Spirit.
- Therefore, it uses [SteamRE DepotDownloader](https://github.com/SteamRE/DepotDownloader) to download the game from Steam. 
- In addition, to prevent Steam from automatically update the game, this script uses [leovp's acf parser](https://github.com/SteamRE/DepotDownloader) to edit Steam configuration files.