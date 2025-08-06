#!/usr/bin/env bash
PLYMOUTH_THEME_BASEDIR=${PLYMOUTH_THEME_BASEDIR:=/usr/share/plymouth/themes/ds3}
FONTCONFIG_PATH=${FONTCONFIG_PATH:=/etc/fonts/conf.d/}

mkdir -p /usr/share/fonts/OTF/
cp -v ./font/FOT-Matisse-Pro.otf /usr/share/fonts/OTF/

mkdir -p "${FONTCONFIG_PATH}"
cp -v ./font/config/* "${FONTCONFIG_PATH}"

mkdir -p "${PLYMOUTH_THEME_BASEDIR}"

cp -vr ./plymouth/* "${PLYMOUTH_THEME_BASEDIR}/"

install -v -d -m 0755 /etc/mkinitcpio.conf.d
install -v -m 0644 ./mkinitcpio/* /etc/mkinitcpio.conf.d/99-ds3-plymouth.conf


echo "Plymouth theme installed to ${PLYMOUTH_THEME_BASEDIR}"
echo "Don't forget to update your current theme selection:"
echo "plymouth-set-default-theme -R ds3       # Arch"
echo "update-alternatives --config default.plymouth # Debian/Ubuntu"
echo "You may need to regenerate your initramfs:"
echo "mkinitcpio -P                     # Arch"
echo "update-initramfs -u        # Debian/Ubuntu"