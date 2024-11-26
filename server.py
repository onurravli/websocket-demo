import asyncio
import websockets

connected_clients = set()


async def handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            response = f"Server received: {message}"
            await asyncio.gather(
                *(client.send(response) for client in connected_clients)
            )
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)


async def main():
    start_server = await websockets.serve(handler, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
