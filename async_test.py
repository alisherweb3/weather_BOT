import asyncio
import time

def fun1(x):
  print(x**2)
  await asyncio.sleep(3)
  print('fun1 fins')
  
  
def fun2(x):
  print(x**0.5)
  await asyncio.sleep(3)
  print('fun2 fins')
  
async def main():
  task1 = asyncio.create_task(fun1(4))
  task2 = asyncio.create_task(fun2(4))
  
print(time.strftime('%X'))

asyncio.run()

print(time.sprftime('%X'))
