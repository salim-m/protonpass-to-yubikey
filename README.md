## ProtonPass TOTPs to YubiKey

This script reads totp uris from a proton pass json export and adds them to all connected yubikeys

Important: Make sure to have Yubikey Manager installed

### How to use

1.  Click on ProtonPass settings then click "export", make sure that you've picked unencrypted "json" format
2.  Unzip the export, you'll find a json file called "data.json", copy-paste it inside the root of the repo (alongside the script.py)
3.  Run `ykman script script.py`
4.  Done !
