# 비동기적인 코드 예시
import asyncio

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)  # 1초 동안 대기
    print("end")

async def print_numbers2():
    for i in range(6, 11):
        print(i)
        await asyncio.sleep(1)  # 1초 동안 대기
    print("end")
        
async def main():
    task = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_numbers2())
    await task,task2
    print("All numbers printed.")

asyncio.run(main())
