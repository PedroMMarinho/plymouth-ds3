#!/usr/bin/env bash

# Where to install your theme
PLYMOUTH_THEME_BASEDIR=${PLYMOUTH_THEME_BASEDIR:=/usr/share/plymouth/themes/ds3}
FONTCONFIG_PATH=${FONTCONFIG_PATH:=/etc/fonts/conf.d/}

# Copy font config and font (if you use custom fonts)
install -d -m 0755 /usr/share/fonts/OTF/
install -m 0644 ./font/FOT-Matisse-Pro.otf /usr/share/fonts/OTF/
cp -v ./font/config/* "${FONTCONFIG_PATH}"

# Install Plymouth theme files
install -d -m 0755 "${PLYMOUTH_THEME_BASEDIR}"
install -m 0644 ./plymouth/ds3.plymouth "${PLYMOUTH_THEME_BASEDIR}"
install -m 0644 ./plymouth/ds3.script "${PLYMOUTH_THEME_BASEDIR}"
install -m 0644 ./plymouth/main_box.png "${PLYMOUTH_THEME_BASEDIR}"
install -m 0644 ./plymouth/darksouls3_logo.png "${PLYMOUTH_THEME_BASEDIR}"


echo "Plymouth theme installed to ${PLYMOUTH_THEME_BASEDIR}"
echo "Don't forget to update your initramfs or equivalent:"
echo "sudo update-initramfs -u  # Debian/Ubuntu"
echo "sudo mkinitcpio -P        # Arch"
