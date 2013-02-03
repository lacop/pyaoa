PyAOA
=====

Very simple [Android Open Accessory 1.0](http://source.android.com/tech/accessories/aoap/aoa.html) library. Finds a device, toggles accessory mode and provides `read` and `write` functions.

This was written in a few minutes as a proof-of-concept so the code is terrible, sorry about that. Pull requests are welcome :)

Usage
-----

First you need to get an Android device handle. Find them by providing a list of (vendor ID, product ID) tuples (you can find them using `lsusb`):

```python
dev = find_device([0x04e8, 0x6860)])
```

Next attempt to switch this device to accessory mode. You need to provide various info like manufacturer and model:

```python
toggle_accessory_mode(dev, "Manufacturer", "Model", "Description", "1.0", "http://example.com", "SN-123-456-789")
```

This will cause the device to reconnect under a new USB id, you can find it again using `find_accessory()`:

```python
dev = find_accessory()
```

And that's it. Now you can read/write from the device:

```python
data = read(dev, 1024)
write(dev, data)
```

Dependencies
------------

Requires [pyUSB](http://pypi.python.org/pypi/pyusb) package.

