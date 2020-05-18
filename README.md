My poor try to create a script that helps refactoring the patch directories for Armbian kernel patches.

Well if refactoring them by hand take forever I can use the same amount of time to create a script that does the job for me....which will probably take forever as well. So everything is good.


Sample output:
```
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Patch file                                                                                   | target file                                                                                                    |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| 0129-dt-bindings-Add-ANX6345-DP-eDP-transmitter-binding.patch                                | +++ b/Documentation/devicetree/bindings/display/bridge/anx6345.txt                                             |
| 0104-dt-bindings-gpio-gpio-axp209-add-AXP803-GPIO-binding.patch                              | +++ b/Documentation/devicetree/bindings/gpio/gpio-axp209.txt                                                   |
| 0105-dt-bindings-iio-adc-add-AXP803-ADC-bindings.patch                                       | +++ b/Documentation/devicetree/bindings/iio/adc/axp20x_adc.txt                                                 |
| 0141-dt-bindings-net-bluetooth-Add-rtl8723bs-bluetooth.patch                                 | +++ b/Documentation/devicetree/bindings/net/rtl8723bs-bluetooth.txt                                            |
| 0103-dt-bindings-power-supply-axp20x-add-AXP803-power-bin.patch.part001.patch                | +++ b/Documentation/devicetree/bindings/power/supply/axp20x_ac_power.txt                                       |
| 0103-dt-bindings-power-supply-axp20x-add-AXP803-power-bin.patch.part002.patch                | +++ b/Documentation/devicetree/bindings/power/supply/axp20x_battery.txt                                        |
| board-pine-h6-pine-h6-0021-dt-bindings-usb-add-binding-for-the-DWC3-controller-.patch        | +++ b/Documentation/devicetree/bindings/usb/allwinner,dwc3.txt                                                 |
| general-fix-builddeb-packaging.patch                                                         | +++ b/Makefile                                                                                                 |
| general-add-overlay-compilation-support.patch.part001.patch                                  | +++ b/arch/arm/boot/.gitignore                                                                                 |
| board-h2plus-nanopi-duo-add-device.patch.part001.patch                                       | +++ b/arch/arm/boot/dts/Makefile                                                                               |
| board-h2plus-sunvell-r69-add-device.patch.part001.patch                                      | +++ b/arch/arm/boot/dts/Makefile                                                                               |
| general-sunxi-overlays.patch.part001.patch                                                   | +++ b/arch/arm/boot/dts/Makefile                                                                               |
| xxx-add-nanopi-r1-and-duo2.patch.part001.patch                                               | +++ b/arch/arm/boot/dts/Makefile                                                                               |
| xxx-add-zeropi.patch.part001.patch                                                           | +++ b/arch/arm/boot/dts/Makefile                                                                               |
| 0038-ARM-dts-add-gpu-node-to-exynos4.patch                                                   | +++ b/arch/arm/boot/dts/exynos4.dtsi                                                                           |
| general-sunxi-overlays.patch.part002.patch                                                   | +++ b/arch/arm/boot/dts/overlay/Makefile                                                                       |
| general-sunxi-overlays.patch.part003.patch                                                   | +++ b/arch/arm/boot/dts/overlay/README.sun4i-a10-overlays                                                      |
| general-sunxi-overlays.patch.part004.patch                                                   | +++ b/arch/arm/boot/dts/overlay/README.sun5i-a13-overlays                                                      |
| general-sunxi-overlays.patch.part005.patch                                                   | +++ b/arch/arm/boot/dts/overlay/README.sun7i-a20-overlays                                                      |
| general-sunxi-overlays.patch.part006.patch                                                   | +++ b/arch/arm/boot/dts/overlay/README.sun8i-h3-overlays                                                       |
| general-sunxi-overlays.patch.part007.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-analog-codec.dts                                                     |
| general-sunxi-overlays.patch.part008.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-can.dts                                                              |
| general-sunxi-overlays.patch.part009.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-fixup.scr-cmd                                                        |
| general-sunxi-overlays.patch.part010.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-i2c1.dts                                                             |
| general-sunxi-overlays.patch.part011.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-i2c2.dts                                                             |
| general-sunxi-overlays.patch.part012.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-nand.dts                                                             |
| general-sunxi-overlays.patch.part013.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-pps-gpio.dts                                                         |
| general-sunxi-overlays.patch.part014.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-pwm.dts                                                              |
| general-sunxi-overlays.patch.part015.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-spdif-out.dts                                                        |
| general-sunxi-overlays.patch.part016.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-spi-jedec-nor.dts                                                    |
| general-sunxi-overlays.patch.part017.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-spi-spidev.dts                                                       |
| general-sunxi-overlays.patch.part018.patch                                                   | +++ b/arch/arm/boot/dts/overlay/sun4i-a10-spi0.dts
```