import asyncio, evdev
from evdev import ecodes as e

i = 0
lastK = ""
@asyncio.coroutine
def print_events(device):
    global i
    global lastK
    while True:
      try:
        events = yield from device.async_read()
        for event in events:
            if not event.value == 0:
                if lastK == device.path:
                    i = i + 1
                else:
                   lastK = device.path
                   i = 0
                print(device.path, e.KEY[event.code], i, sep=': ')
      except :
        global listDevices
        listDevices.remove(path)
        break


listDevices = []
async def CheckDevices(interval):
    global listDevices
    while True:
        for dev in evdev.list_devices():
          if not (dev in listDevices):
            devices = evdev.InputDevice(dev)
            if not (devices.name in [""]):
              listDevices.append(dev)
              asyncio.ensure_future(print_events(devices))
        await asyncio.sleep(interval)

loop = asyncio.get_event_loop()
try:
  asyncio.ensure_future(CheckDevices(2))
#  devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
#  for device in devices:
#    asyncio.async(print_events(device))
  loop = asyncio.get_event_loop()
  loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
print("END Script")
