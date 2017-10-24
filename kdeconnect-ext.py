import importlib
from subprocess import check_output, call
from gi.repository import GObject
from kdeconnect import send_files, get_available_devices
import zipfile

TARGET = "%%TARGET%%".title()
Nautilus = importlib.import_module("gi.repository.{}".format(TARGET))


class KDEConnectExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def zipdir(self, path, ziph):
        # ziph is zipfile handle
        import os
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    def menu_activate_cb(self, menu, files, device_id, device_name, folder_list):
        import zipfile
        import os
        for folder_name in folder_list:
            zip_name = folder_name + '.zip'
            zipf = zipfile.ZipFile(zip_name[7:], 'w', zipfile.ZIP_DEFLATED)
            self.zipdir(folder_name + '/', zipf)
            zipf.close()
            zipfile = Nautilus.FileInfo.create_for_uri(zip_name)
            files.append(zipfile)

        send_files(files, device_id, device_name)
        # for folder_name in folder_list:
        #     os.remove(folder_name[7:] + '.zip')

    def get_file_items(self, window, files):
        try:
            devices = get_available_devices()
        except Exception as e:
            raise Exception("Failed to get available devices")

        files_new = []
        folder_list = []
        for i in range(len(files)):
            if (files[i].is_directory() == False):
                files_new.append(files[i])
            else:
                folder_list.append(files[i].get_uri())

        files = files_new
        print files
        print folder_list

        if (len(files_new) + len(folder_list) < 1):
            return []

        items = []
        for device in devices:
            item = Nautilus.MenuItem(
                name="KDEConnectExtension::Send_File",
                label="Send to %s" % device["name"]
            )
            item.connect('activate', self.menu_activate_cb,
                         files, device["id"], device["name"], folder_list)
            items.append(item)

        return items
