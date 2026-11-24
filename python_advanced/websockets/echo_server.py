#!/usr/bin/env python3
"""WebSocket echo server."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Echo messages received from connected clients."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server."""
    async with websockets.serve(
        connection_handler,
        "0.0.0.0",
        8765
    ):
        print("WebSocket server listening on port 8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
