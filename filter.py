import asyncio, evdev
import asyncio
import time


lastN = 0
activeID = ""

def scanFilter(id,s):
  n = time.time()
  global lastN
  global activeID
  d = n - lastN
  b = d > 0.2

  if b:
    activeID = id
  if activeID == id:
    print(id," : ",s, "diff: ", b)
    lastN = n

@asyncio.coroutine
def print_events(device,path):
    while True:
      try:
        events = yield from device.async_read()
        for event in events:
            #print(device.path, evdev.categorize(event), sep=': ')
            scanFilter(device.path,evdev.categorize(event))
      except OSError:
        global listDevices
        listDevices.remove(path)
        break

listDevices = []
async def CheckDevices(interval):
    global listDevices
    while True:
        print("CheckDevice",listDevices)
        for dev in evdev.list_devices():
          if not (dev in listDevices):
            listDevices.append(dev)
            devices = evdev.InputDevice(dev)
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




import asyncio, evdev
import asyncio
import time


lastN = 0
activeID = ""

def scanFilter(id,s):
  n = time.time()
  global lastN
  global activeID
  d = n - lastN
  b = d > 0.2

  if b:
    activeID = id
  if activeID == id:
    print(id," : ",s, "diff: ", b)
    lastN = n

@asyncio.coroutine
def print_events(device,path):
    while True:
      try:
        events = yield from device.async_read()
        for event in events:
            #print(device.path, evdev.categorize(event), sep=': ')
            scanFilter(device.path,evdev.categorize(event))
      except OSError:
        global listDevices
        listDevices.remove(path)
        break

listDevices = []
async def CheckDevices(interval):
    global listDevices
    while True:
        print("CheckDevice",listDevices)
        for dev in evdev.list_devices():
          if not (dev in listDevices):
            listDevices.append(dev)
            devices = evdev.InputDevice(dev)
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





