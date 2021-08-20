import websockets as ws
import asyncio
import datetime
import os


async def log(message):
    print(f"[{str(datetime.datetime.utcnow()).rsplit('.')[0]}]", message)


async def process(websocket: ws.WebSocketServerProtocol, path):
    try:
        print(websocket)
        content = await websocket.recv()
        await log(message=content)
        execute = os.popen(content)
        await websocket.send(execute.read())
    except OSError as e:
        await log(message=f"Client {path} disconnected!")


srv = ws.serve(process, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(srv)
asyncio.get_event_loop().run_forever()
