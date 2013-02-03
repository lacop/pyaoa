__all__ = ['find_device', 'find_accessory', 'toggle_accessory_mode', 'write', 'read']

import usb.core

class find_filtered:
	def __init__(self, known_devices):
		self.known_devices = known_devices
	
	def __call__(self, device):
		for pair in self.known_devices:
			if pair[0] == device.idVendor and pair[1] == device.idProduct:
				return True
		
		return False
	

def find_device(known_devices):
	return usb.core.find(custom_match=find_filtered(known_devices))

def find_accessory():
	return usb.core.find(custom_match=find_filtered([(0x18d1, 0x2d00), (0x18d1, 0x2d01)]))

def toggle_accessory_mode(device, manufacturer, model, description, version, uri, sn):
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_IN, 51, 0, 0, 256)
	# TODO check returned version
	
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT, 52, 0, 0, manufacturer)
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT, 52, 0, 1, model)
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT, 52, 0, 2, description)
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT, 52, 0, 3, version)
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT, 52, 0, 4, uri)
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT, 52, 0, 5, sn)
	
	device.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT, 53, 0, 0, None)

def write(device, data, timeout = None):
	if timeout is None:
		return device.write(0x04, data, 0)
	else:
		return device.write(0x04, data, 0, timeout)
	
def read(device, length, timeout = None):
	if timeout is None:
		return device.read(0x82, length, 0)
	else:
		return device.read(0x82, length, 0, timeout)
