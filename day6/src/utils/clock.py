import asyncio
import time
async def create_clock():
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()))
        """
        pause the execution for 1 second before printing the time again
        allowing other tasks to run while waiting for the next time update
        """
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(create_clock())