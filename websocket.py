import asyncio
import websockets, json
import queue, collectSignal as cs

q = queue.Queue()

async def addQ():
    while True:
        l = cs.generateCoordinates()
        q.put(l)
        print(q.qsize())
        await asyncio.sleep(0.1)

async def getQ(websocket):
    while True:
        while not q.empty():
            try:
                js = json.dumps(q.get_nowait())
                await websocket.send(js)
                print(js)
            except queue.Empty:
                print('Queue is empty')
        await asyncio.sleep(0.1)


async def hello(websocket):
    # name = await websocket.recv()
    tasks = [
        asyncio.create_task(addQ()),
        asyncio.create_task(getQ(websocket))
    ]
    print('Running tasks concurrently...')
    await asyncio.gather(*tasks)
    print('Done!')
    

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())