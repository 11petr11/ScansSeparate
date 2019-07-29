import asyncio
from evdev import UInput, ecodes as e



ui = UInput(None,"VKeyx")
ui2 = UInput()
A = [e.KEY_S,e.KEY_P,e.KEY_0,e.KEY_1,e.KEY_2,e.KEY_3,e.KEY_0,e.KEY_1,e.KEY_2,e.KEY_3,e.KEY_ENTER]
B = [e.KEY_T,e.KEY_S,e.KEY_A,e.KEY_B,e.KEY_C,e.KEY_D,e.KEY_E,e.KEY_F,e.KEY_G,e.KEY_H,e.KEY_ENTER]
async def VKeybord(ui,name,longPause,shortPause,keys):
    while True:
        await asyncio.sleep(longPause)

        for key in keys:
          print(name,e.KEY[key])
          # accepts only KEY_* events by default
          ui.write(e.EV_KEY, key, 1)  # KEY_A down
          ui.write(e.EV_KEY, key, 0)  # KEY_A up
          ui.syn()
          await asyncio.sleep(shortPause)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(VKeybord(ui,"first",1,0.08,A))
    asyncio.ensure_future(VKeybord(ui2,"second",2.3,0.0715,B))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
    ui.close()
    ui2.close()
