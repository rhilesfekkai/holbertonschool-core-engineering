#!/usr/bin/env python3
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def handle_client(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            disconnected = set()

            for client in connected_clients.copy():
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    disconnected.add(client)

            connected_clients.difference_update(disconnected)

    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(
        handle_client,
        "0.0.0.0",
        8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
