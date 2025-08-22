# DS3 plymouth theme

The Full Darksouls Experience:

|  [Dark Souls Grub](https://github.com/PedroMMarinho/grubsouls-theme)  | *> DS3 Plymouth <*
| --- | ---  |

The actual DS3 loading screen styled Plymouth theme, revealing to be the continuation of [GrubSouls](https://github.com/PedroMMarinho/grubsouls-theme).

For the real booting experience of darksouls you should use this!!! Or don't it's really up to you XD.

**Screenshots preview:**

![Gale Soul](preview/gale_soul.png)

![Midir Soul](preview/midir_soul.png)

![Bone](preview/bone.png)

# Installation

- Clone or download the theme repository:

```bash
git clone git@github.com:PedroMMarinho/plymouth-ds3.git
```

## Using the script

If you are using an OS which follows the `POSIX filesystem` structure (`/etc`, `/usr` and friends), you won't have any issues.

Do the following:
```bash
sudo ./install.sh
# Update and set the theme to the installed one
# A message should appear after running the script
```

And thats it you are good to go!

## Manually

- If the script doesn't work you might need to see where the `plymouth themes` are **stored**, and copy the repo's `plymouth folder` to that path. 
- Do not forget to have the `font` installed.
- This installation uses `mkinitcpio` as the `default initramfs updater`. If you use dracut you'll need to do things differently.


# Configuration

## Update Item After Every Boot

The `update_config` script, updates the `ds3.script` altering the item being shown and its description, using as reference the `items.json` and the folder `sprites`.

For this to work you have to do the following:

- Simple Python 3 (or other variation) installation
- If you want you can add a custom entry to `items.json` :) 
   - Here's an example:
       ```
        {
        "name": "Black Separation Crystal",
        "description": "A charm of farewell granted to banished Undead. The crystal sends phantoms back to their homes, or you back to yours.\n\nBeware of fickle use of this item if you intend to nurture relations.",
        "image": "sprites/black_separation_crystal.png"
        },
       ```
    - Double `\n` puts an empty line before the next sentence.
    - One `\n` makes the next sentence start in the next line.
    - **Don't forget** to add into `./ds3/sprites` the png you are refering to. (The image should be 160x160 pixels)
- You can run `python update_config` with no arguments and it will choose a random item. If you run `python update_config <ITEM_NAME>` it will choose that one instead.
- For the changes to be applied you need to **regenerate** the `initramfs` .

To have this running `automatically` you'll to do the following:

> For systemd

- Copy `./ds3-plymouth-update` to `/etc/systemd/system`.

- Enable the service: `systemctl enable ds3-plymouth-update`

- If for some reason it does not update after boot you can run` systemctl status grubsouls-update.service` and check for errors.

## Delaying Plymouth Theme

- If the `splash` is **too fast**, you can delay it using a `service`:
```
[Unit]
Description=Waits for Plymouth animation to finish
Before=plymouth-quit.service display-manager.service

[Service]
Type=oneshot
ExecStart=/usr/bin/sleep 5

[Install]
WantedBy=plymouth-start.service
```
In this case the plymouth takes up `5 seconds`.

# Common Issues

- If using the `service for theme update`, when rebooting you might need to **wait** a short period of time because of the initramfs being regenerated. This only happens if you **boot** and **reboot** your pc almost instantly.
- If can't see the `splash` you should check the `/etc/default/grub` file. It should have these parameters: 
    - `GRUB_CMDLINE_LINUX_DEFAULT="quiet loglevel=3 udev.log-priority=3 splash ...` (**Order matters!!**)
    - And then run:
        ```
        sudo grub-mkconfig -o /boot/grub/grub.cfg
        ```

# Future DEV

Support for different window sizes. For now `1920x1080` is the target resolution. Upper Resolutions should have no problem but lower than that it won't look good.

# Documentation

https://wiki.gentoo.org/wiki/Plymouth/Theme_creation

https://wiki.gentoo.org/wiki/User:DerpDays/Plymouth/Theming
