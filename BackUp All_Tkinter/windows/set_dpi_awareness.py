# Fucntion to correct high DPI values in case of Windows 10 in actual screens
def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetprocessDpiAwareness(1)
        print('Avoiding Windows 10')
    except Exception:
        print('Avoiding Windows 10 Exception')
        pass