from subprocess import check_output, call
import re

def send_files(files, device_id, device_name):
    # results=[]
    # failed=0
    for file in files:
        print "filename", file.get_uri()
        return_code=call(["kdeconnect-cli", "-d", device_id, "--share", file.get_uri()])
        # if (return_code != 0):
        #     failed += 1
        # results.append(return_code)
    call(["notify-send", "Sending {num_files} file(s) to {device_name}. Check your device.".format(num_files=len(files), device_name=device_name)])
    # return results

def get_available_devices():
    # return [ {"name": "Xperia Z", "id": "stuff"} ]
    devices_a=[]
    devices = check_output(["kdeconnect-cli", "-a"]).strip().split("\n")
    devices.pop()
    for device in devices:
        device_name=re.search("(?<=-\s).+(?=:\s)", device).group(0)
        device_id=re.search("(?<=:\s)[a-z0-9]+(?=\s\()", device).group(0).strip()
        devices_a.append({ "name": device_name, "id": device_id })
    return devices_a
