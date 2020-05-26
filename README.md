My poor try to create a script that helps refactoring the patch directories for Armbian (kernel) patches.

Well if refactoring them by hand take forever I can use the same amount of time to create a script that does the job for me....which will probably take forever as well. So everything is good.

### Dependencies:
- `Python 3.8.2` or higher (did not test any other version)
- via apt: `patchutils`


### How to use:
0. Backup your patch folder.
1. Put the `refactor.py` in the folder **above** your patch folder (not inside!).
2. Run it.
3. Follow the instructions.
4. Did you backup your patch folder?



Sample output:
```
general-add-configfs-overlay.patch.part001.patch -> /drivers/of/Kconfig
general-add-configfs-overlay.patch.part002.patch -> /drivers/of/Makefile
general-add-configfs-overlay.patch.part003.patch -> /drivers/of/configfs.c
general-add-configfs-overlay.patch.part004.patch -> /drivers/of/fdt_address.c
0001-pinctrl-sunxi-Disable-strict-mode-for-A64-pinctrl-dr.patch -> /drivers/pinctrl/sunxi/pinctrl-sun50i-a64.c
general-add-H6-GPIO-disable_strict_mode.patch -> /drivers/pinctrl/sunxi/pinctrl-sun50i-h6.c
general_spi_bug_low_on_sck.patch -> /drivers/spi/spi-sun4i.c    (date 1581070363000)
spi6-sck-high-too-early.patch -> /drivers/spi/spi-sun6i.c
general-fix-cs_gpio-spi-support.patch -> /drivers/spi/spi.c
general-spidev-remove-warnings.patch -> /drivers/spi/spidev.c
0080-rtl8723bs-disable-error-message-about-failure-to-all.patch -> /drivers/staging/rtl8723bs/hal/sdio_ops.c
wifi-8723bs-AP-bugfix.patch -> /drivers/staging/rtl8723bs/os_dep/ioctl_cfg80211.c
wifi-fix-staging-rtl8723cs-for-5.6.y.patch -> /drivers/staging/rtl8723cs/os_dep/linux/rtw_proc.c
rename_gadget_serial_console_manufacturer.patch -> /drivers/usb/gadget/composite.c
0005-drm-gem-cma-Export-with-handle-allocator.patch.part002.patch -> /include/drm/drm_gem_cma_helper.h
0011-iio-adc-sun4i-gpadc-iio-rename-A33-specified-registe.patch.part002.patch -> /include/linux/mfd/sun4i-gpadc.h




I can filter this list and show only files that are
target of multiple patches so you could merge them.
Should I do that? (y/n) y

/arch/arm/boot/dts/Makefile is affected by:
board-h2plus-nanopi-duo-add-device.patch.part001.patch
board-h2plus-sunvell-r69-add-device.patch.part001.patch
general-sunxi-overlays.patch.part001.patch
xxx-add-nanopi-r1-and-duo2.patch.part001.patch
xxx-add-zeropi.patch.part001.patch

/arch/arm/boot/dts/sun7i-a20-cubietruck.dts is affected by:
ARM-dts-sun7i-Disable-OOB-IRQ-for-brcm-wifi-on-Cubietruck-and-Banana-Pro.patch.part002.patch
board-cubieboard-cubietruck-green-LED-mmc0.patch.part002.patch
board-cubietruck-enable-uart2.patch

/arch/arm/boot/dts/sun8i-h2-plus-bananapi-m2-zero.dts is affected by:
xxx-add-bananapim2-zero-eth.patch
xxx-add-bananapim2-zero-heartbeat-led.patch
xxx-add-bananapim2-zero-z1-HDMI-out.patch
xxx-add-bananapim2-zero-z2-HDMI-audio-out.patch
xxx-add-bananapim2-zero-z3-bluetooth-wifi-rfkill.patch

/arch/arm/boot/dts/sun8i-h3-nanopi.dtsi is affected by:
add-nanopi-npi-stuff.patch
board-nanopi-adjust-defaults.patch
```