# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///


import httpx
import asyncio
import time


async def fetch_url(url, client):
    response = await client.get(url)
    return url, response.status_code


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
    ]

    start_time = time.time()

    # Using an async client as a context manager
    async with httpx.AsyncClient() as client:
        # Create a list of tasks
        tasks = [fetch_url(url, client) for url in urls]

        # Gather all tasks (execute them concurrently)
        results = await asyncio.gather(*tasks)

        # Print results
        for url, status_code in results:
            print(f"URL: {url}, Status: {status_code}")

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
