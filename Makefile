TARGET ?= Nautilus

# To lower case function
lc = $(shell echo "$1" | tr '[:upper:]' '[:lower:]')

# File manager extension directory
directory-ext   := ${HOME}/.local/share/$(call lc,${TARGET})-python/extensions
directory-build := build

.PHONY: all
all: build

# Copy files to build directory and substitute %%TARGET%% for the given target name
.PHONY: build
build:
	mkdir -p "${directory-build}"
	cp $(wildcard *.py) "${directory-build}/"
	sed -i "s/%%TARGET%%/$(call lc,${TARGET})/g" "${directory-build}"/*

# Copy files from build directory to the target's python extension directory
.PHONY: install
install: build
	mkdir -p "${directory-ext}"
	cp "${directory-build}"/* "${directory-ext}/"
	@echo "Done. Please restart ${TARGET}."

# Remove build directory
.PHONY: clean
clean:
	rm -rf "${directory-build}"
