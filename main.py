from getpass import getpass
import os
import acf

APP_ID = 289070
STEAM_PATH = "~/.steam/debian-installation/steamapps"


def run(command, error=None, fatal=False):
    code = os.system(command)
    if code != 0:
        if not error:
            error = f"Command {command} exited with non zero code."
        print(error)
        if fatal:
            print("Exiting.")
            exit()


print("Welcome to Civ6 Downgrader!")
print("To continue, you need to connect to Steam.")
username = input("Username: ")
password = getpass("Password: ")

run(f"./DepotDownloader/DepotDownloader -app 289070 -depot 289072 -manifest 2083953515690984432 -username {username} -password {password}", "Unable to download 1st depot.", True)
run(f"./DepotDownloader/DepotDownloader -app 289070 -depot 289071 -manifest 5394165790985725247 -username {username} -password {password}", "Unable to download 2nd depot.", True)

print("Download complete, installing game...")
run(f"rsync -a -v depots/289072/10568987/ {STEAM_PATH}/common/Sid\ Meier\\'s\ Civilization\ VI/", "Unable to install 1st depot.", True)
run("rm -rf depots/289072/10568987/*", "Unable to clean up 1st depot.")
run(f"rsync -a -v depots/289071/10568987/ {STEAM_PATH}/common/Sid\ Meier\\'s\ Civilization\ VI/", "Unable to install 2nd depot.", True)
run("rm -rf depots/", "Unable to clean up depots.")

print("Installation complete, blocking automatic updates...")
manifest_path = os.path.expanduser(os.path.join(STEAM_PATH, f"appmanifest_{APP_ID}.acf"))
with open(manifest_path) as f:
    manifest = acf.load(f)
manifest["AppState"]["StateFlags"] = 4
with open(manifest_path, "w") as f:
    acf.dump(manifest, f)

print("Done!")