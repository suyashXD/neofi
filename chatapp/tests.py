import asyncio
import websockets

async def send_message():
    uri1 = "ws://localhost:8000/ws/chat/gajodhar/"  # Replace <username> with the desired recipient's username
    uri2 = "ws://localhost:8000/ws/chat/mudizee/"  # Replace <username> with the desired recipient's username
    async with websockets.connect(uri1) as websocket:
        message = input("Enter a message to send: ")
        await websocket.send(message)
        print(f"Sent: {message}")
        response = await websocket.recv()
        print(f"Received: {response}")

    async with websockets.connect(uri2) as websocket:
        message = input("Enter a message to send: ")
        await websocket.send(message)
        print(f"Sent: {message}")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(send_message())