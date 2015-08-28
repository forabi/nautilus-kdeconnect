all:
	mkdir -p ~/.local/share/nautilus-python/extensions && cp *.py ~/.local/share/nautilus-python/extensions
	echo "Done. Please restart Nautilus."
