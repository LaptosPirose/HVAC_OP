import usb.core
import usb.util

# Find all USB devices
devices = usb.core.find(find_all=True)

# List detected devices
for device in devices:
    print(f"\nDevice: ID Vendor  {device.idVendor:04x}: ID Product{
          device.idProduct:04x}")
    VID = device.idVendor  # Vendor ID do dispositivo
    PID = device.idProduct  # Product ID do dispositivo
    dev = usb.core.find(idVendor=VID, idProduct=PID)
    print(dev)
