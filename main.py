from getpass import getpass
import os
import acf

APP_ID = 289070
STEAM_PATH = "~/.steam/debian-installation/steamapps"

print("Welcome to Civ6 Downgrader!")
print("To continue, you need to connect to Steam.")
username = input("Username: ")
password = getpass("Password: ")

print("Starting download...")
os.system(f"./DepotDownloader/DepotDownloader -app 289070 -depot 289072 -manifest 2083953515690984432 -username {username} -password {password}")
os.system(f"./DepotDownloader/DepotDownloader -app 289070 -depot 289071 -manifest 5394165790985725247 -username {username} -password {password}")

print("Download complete, installing game...")
os.system("rsync -a -v depots/289072/10568987/ ~/.steam/debian-installation/steamapps/common/Sid\ Meier\\'s\ Civilization\ VI/")
os.system("rm -rf depots/289072/10568987/*")
os.system("rsync -a -v depots/289071/10568987/ ~/.steam/debian-installation/steamapps/common/Sid\ Meier\\'s\ Civilization\ VI/")
os.system("rm -rf depots/")

print("Installation complete, blocking automatic updates...")
manifest_path = os.path.expanduser(os.path.join(STEAM_PATH, f"appmanifest_{APP_ID}.acf"))
with open(manifest_path) as f:
    manifest = acf.load(f)
manifest["AppState"]["StateFlags"] = 4
with open(manifest_path, "w") as f:
    acf.dump(manifest, f)

print("Done!")