import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                message = input("Enter message to send: ")
                await websocket.send(message)
                print(f"Message sent to server: {message}")

                # Wait for server response
                response = await websocket.recv()
                print(f"Response from server: {response}")
        except KeyboardInterrupt:
            print("\nDisconnected from server.")


asyncio.run(client())
