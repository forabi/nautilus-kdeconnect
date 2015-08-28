nautilus-kdeconnect
====================
Nautilus extension for sending files to devices connected via KDE Connect.

KDE Connect is a service that connects your Android device with your Linux PC via Wi-Fi, enabling many features like shared clipboard, notification syncing, file sharing and media playback control. This extension provides file sharing support in Nautilus via context menu (right-click menu).

![Screenshot](./screenshot.png)

Features
---------
* Send any number of files at once. _(Directories are not supported currently)_.
* Send files to any connected device.

Installation
-------------
In addition to [KDE Connect](https://community.kde.org/KDEConnect), this extension requires [nautilus-python](https://wiki.gnome.org/Projects/NautilusPython) and libnotify. Following are the instructions for Arch Linux:

1. On your PC, install `kdeconnect-git`, `python2-nautilus` and `libnotify`.
2. Install the KDE Connect companion app for Android, available on [Google Play](https://play.google.com/store/apps/details?id=org.kde.kdeconnect_tp) and [F-Droid](https://f-droid.org/repository/browse/?fdid=org.kde.kdeconnect_tp).
3. Launch KDE Connect on your PC and on your Android device. Pair the two devices and enable the sharing plugin.
4. Clone this repository and install the extension: `git clone https://github.com/forabi/nautilus-kdeconnect && cd nautilus-kdeconnect && make`.
