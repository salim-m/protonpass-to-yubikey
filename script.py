from ykman.device import list_all_devices
from yubikit.oath import CredentialData, OathSession
from yubikit.core.smartcard import SmartCardConnection
import json

result = {}

with open("data.json") as data:
    body = json.loads(data.read())
    vaults = body['vaults'];
    
    for key in vaults.keys():
        name = vaults[key]["name"]
        items = vaults[key]['items']
       
        result[name] = [item["data"]["content"]["totpUri"] for item in items if item["state"] == 1 and "totpUri" in item["data"]["content"] and item["data"]["content"]["totpUri"]]


device, info = list_all_devices()[0]


for device, info in list_all_devices():
    print(f"Found YubiKey with serial number: {info.serial} ... Running ... \n")

    with device.open_connection(SmartCardConnection) as connection:
        oath = OathSession(connection)
        for vault, uris in result.items():
            print(f"Adding items from vault \"{vault}\" ... ", end="")
            
            for uri in uris:
                oath.put_credential(CredentialData.parse_uri(uri))
            print("Done \n")