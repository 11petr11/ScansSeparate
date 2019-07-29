import asyncio, evdev
import asyncio
import time
from evdev import UInput, ecodes as e

UINPUT_NAME = "VKey"

ui = UInput(None,UINPUT_NAME)

lastN = 0
activeID = ""

def scanFilter(id,ev):
  n = time.time()
  global lastN
  global activeID
  d = n - lastN
  b = d > 0.4

  #print(b, d, n, e.KEY[ev.code])

  if b:
    activeID = id
  if activeID == id:
    #print(id," : ",evdev.categorize(ev), "diff: ", b)
    ui.write_event(ev)
  else:
    print("BLOCK",b, d, n, e.KEY[ev.code])
  lastN = n

@asyncio.coroutine
def print_events(device,path):
  with device.grab_context():
    while True:
      try:
        events = yield from device.async_read()
        for event in events:
            #print(device.path, evdev.categorize(event), sep=': ')
            scanFilter(device.path,event)
      except OSError:
        global listDevices
        listDevices.remove(path)
        break

listDevices = []
async def CheckDevices(interval):
    global listDevices
    while True:
        print("CheckDevice",[evdev.InputDevice(dev).name for dev in listDevices])
        for dev in evdev.list_devices():
          if not (dev in listDevices):
            devices = evdev.InputDevice(dev)
            if not (devices.name in [UINPUT_NAME,"gpio_keys"]):
              listDevices.append(dev)
              asyncio.ensure_future(print_events(devices,dev))
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
