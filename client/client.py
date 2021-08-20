import asyncio
import websockets as ws
import datetime

from utils import get_config

uri = f"ws://{get_config()['server_host']}:{get_config()['server_port']}"


async def loop():
    while True:
        async with ws.connect(uri, ping_interval=None) as websocket:
            msg = input(" > ")
            if msg == "CLOSE_CONN":
                exit(-9)
            await websocket.send(msg)

            response = await websocket.recv()
            print(f'[{str(datetime.datetime.utcnow()).rsplit(".")[0]}] response for "{msg}":\n', response if response else "NO_RESPONSE")


asyncio.get_event_loop().run_until_complete(loop())
