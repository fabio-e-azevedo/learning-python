# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "aiometer",
#     "httpx",
#     "rich",
# ]
# ///

import httpx
import asyncio
import aiometer
from rich import print
from functools import partial

def simple_example() -> None:
    timeout = httpx.Timeout(1.0, connect=1.0)
    
    with httpx.Client(timeout=timeout) as fetch:
        response = fetch.get('https://httpbin.org/get')
        if response.status_code == 200:
            print(response.json())


def async_example(pokename: str) -> None:
    timeout = httpx.Timeout(1.0, connect=1.0)
    
    with httpx.Client(base_url='https://pokeapi.co/api/v2', timeout=timeout) as fetch:
        print(f'Start: {pokename}')
        response1 = fetch.get(f'/pokemon/{pokename}')
        poke_id = response1.json().get('id')
        
        response2 = fetch.get(f'/pokemon-species/{poke_id}')
        evolution_chain = response2.json().get('evolution_chain').get('url')
        
        response3 = fetch.get(evolution_chain)
        evolution_name = response3.json().get('chain').get('evolves_to')[0].get('species').get('name')
        
        print(f'End: {pokename} -> {evolution_name}')
        

async def hello(msg, delay=1):
    print(f'Start Coroutine {msg}')
    await asyncio.sleep(delay)
    print(f'Middle Coroutine {msg}')
    await asyncio.sleep(delay)
    print(f'End Coroutine {msg}')


async def main():
    tasks = asyncio.gather(
        *[hello(n) for n in range(3)]
    )
    print('Todas as tasks: ', asyncio.all_tasks())
    await tasks
    print('Todas as tasks: ', asyncio.all_tasks())


async def fetch(pokename):
    async with httpx.AsyncClient(
        base_url='https://pokeapi.co/api/v2'
    ) as client:
            response1 = await client.get(f'/pokemon/{pokename}')
            poke_id = response1.json().get('id')
            
            response2 = await client.get(f'/pokemon-species/{poke_id}')
            evolution_chain = response2.json().get('evolution_chain').get('url')
            
            response3 = await client.get(evolution_chain)
            evolution_name = response3.json().get('chain').get('evolves_to')[0].get('species').get('name')
            
            print(f'End: {pokename} -> {evolution_name}')
    

async def main_fetch():
    names = ['charmander', 'bulbasaur', 'squirtle']
    # result = asyncio.gather(
    #     *[fetch(name) for name in names]
    # )
    
    result = aiometer.run_all(
        [partial(fetch, name) for name in names],
        max_at_once=2,
        max_per_second=5
    )
    
    await result


if __name__ == "__main__":
    asyncio.run(main_fetch())
