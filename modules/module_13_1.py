import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал сорвенования.')

    for ball in range(1,6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball}')

    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task3
    await task2


asyncio.run(start_tournament())