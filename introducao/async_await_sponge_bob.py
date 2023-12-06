import time
import asyncio

start_time = time.time()

class SyncSpongeBot:
    def cook_bread(self):
        time.sleep(3)

    def cook_hamburger(self):
        time.sleep(10)

    def mount_sandwich(self):
        time.sleep(3)

    def make_milkshake(self):
        time.sleep(5)

    def cook(self):
        self.cook_bread()
        self.cook_hamburger()
        self.mount_sandwich()
        self.make_milkshake()


class ASyncSpongeBot:
    async def cook_bread(self):
        await asyncio.sleep(3)

    async def cook_hamburger(self):
        await asyncio.sleep(10)

    async def mount_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)

    async def make_mount_sandwich(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburger(),
        )

        event_loop = asyncio.get_event_loop()
        event_loop.create_task(self.mount_sandwich())

    async def cook(self):
        await asyncio.gather(
            self.make_mount_sandwich(),
            self.make_milkshake(),
        )

sync_sponge = SyncSpongeBot()
sync_sponge.cook()

async_sponge = ASyncSpongeBot()
asyncio.run(async_sponge.cook())

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
