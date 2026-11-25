#!/usr/bin/env python3
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def handle_client(websocket):
    try:
        async for s in websocket:
            if len(s.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{s}")
    except ConnectionClosed:
        pass


async def main():
    async with websockets.serve(handle_client, "0.0.0.0", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
