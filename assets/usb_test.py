import usb.core
import usb.util

# Find all USB devices
devices = usb.core.find(find_all=True)

# List detected devices
for device in devices:
    print(f"Device: ID Vendor  {device.idVendor:04x}: ID Product{
          device.idProduct:04x}")
