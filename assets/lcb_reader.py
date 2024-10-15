import usb.core
import usb.util

# Find the USB device (replace with your barcode reader's VID and PID)
VID = 0xXXXX  # Vendor ID (e.g., 0x04b8)
PID = 0xYYYY  # Product ID (e.g., 0x0202)

# Find the device
dev = usb.core.find(idVendor=VID, idProduct=PID)

if dev is None:
    raise ValueError('Device not found')

# Set the active configuration (sometimes needed)
dev.set_configuration()

# Detach kernel driver if necessary (Linux specific)
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)

# Claim the interface (usually interface 0)
usb.util.claim_interface(dev, 0)

# Read data from the endpoint
endpoint = dev[0][(0, 0)][0]

# Try reading data
try:
    data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
    print('Data:', data)
except usb.core.USBError as e:
    print(f"USB error: {e}")
