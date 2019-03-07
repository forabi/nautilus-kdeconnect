from subprocess import check_output, call
import re

def send_files(files, device_id, device_name):
    for file in files:
        return_code=call(["kdeconnect-cli", "-d", device_id, "--share", file.get_uri()])

def get_available_devices():
    devices_a=[]
    devices = check_output(["kdeconnect-cli", "-a"]).decode("utf-8").strip().split("\n")
    devices.pop()
    print(devices)
    for device in devices:
        device_name=re.search("(?<=-\s).+(?=:\s)", device).group(0)
        device_id=re.search("(?<=:\s)[a-z0-9_]+(?=\s\()", device).group(0).strip()
        devices_a.append({ "name": device_name, "id": device_id })
    print(devices_a)
    return devices_a
