import importlib
from subprocess import check_output, call
from gi.repository import GObject
from kdeconnect import send_files, get_available_devices

TARGET = "%%TARGET%%".title()
Nautilus = importlib.import_module("gi.repository.{}".format(TARGET))


class KDEConnectExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def menu_activate_cb(self, menu, files, device_id, device_name):
        send_files(files, device_id, device_name)

    def zipdir(self, path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    def get_file_items(self, window, files):
        try:
            devices = get_available_devices()
        except Exception as e:
            raise Exception("Failed to get available devices")

        files_new = []
        for i in range(len(files)):
            if (files[i].is_directory() == False):
                files_new.append(files[i])
            else:
                folder_name = files[i].get_uri()
                zip_name = folder_name + '.zip'
                zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
                self.zipdir(folder_name + '/', zipf)
                zipf.close()
                zipfile_object = Nautilus.FileInfo.create_for_uri(zip_name)
                files_new.append(zipfile_object)

        files = files_new

        if (len(files_new) < 1):
            return []

        items = []
        for device in devices:
            item = Nautilus.MenuItem(
                name="KDEConnectExtension::Send_File",
                label="Send to %s" % device["name"]
            )
            item.connect('activate', self.menu_activate_cb,
                         files, device["id"], device["name"])
            items.append(item)

        return items
