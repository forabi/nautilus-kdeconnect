from gi.repository import Nautilus, GObject
from kdeconnect import send_files, get_available_devices

class KDEConnectExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def menu_activate_cb(self, menu, files, device_id, device_name):
        send_files(files, device_id, device_name)

    def get_file_items(self, window, files):
        try:
            devices = get_available_devices()
        except Exception as e:
            raise Exception("Failed to get available devices")

        files_new = []
        for i in range(len(files)):
            if (files[i].is_directory() == False):
                files_new.append(files[i])
        files = files_new

        if (len(files_new) < 1):
            return []

        items=[]
        for device in devices:
            item = Nautilus.MenuItem(
                name="KDEConnectExtension::Send_File",
                label="Send to %s" % device["name"]
            )
            item.connect('activate', self.menu_activate_cb, files, device["id"], device["name"])
            items.append(item)

        return items
