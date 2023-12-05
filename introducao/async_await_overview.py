import asyncio

async def sum(a, b):
  return a + b

async def print_sum(a, b):
  result = await sum(a, b)
  print(f'{a} + {b} = {result}')


#Event loop
event_loop = asyncio.new_event_loop()
event_loop.run_until_complete(print_sum(5,3))
