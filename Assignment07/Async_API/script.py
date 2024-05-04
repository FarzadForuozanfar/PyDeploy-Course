from dotenv import load_dotenv
import os, time, random, asyncio, aiohttp

state_selected = []
city_selected = []

async def rhyme_finder(word: str):
    start = time.perf_counter()
    url = f"https://rhyming.ir/api/rhyme-finder?api={RHYME_SECRET_KEY}&w={word}&sb=1&mfe=2&eq=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    run = time.perf_counter() - start
    print(f"\nExecuted RhymeFinder Time: {run}")
    return data

async def get_states():
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    return random.choice(data)

async def get_city(state_id):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    return random.choice(data['cities'])

async def get_coordinates():
    start = time.perf_counter()
    state_selected = await get_states()
    city_selected = await get_city(state_id=state_selected['id'])
    run = time.perf_counter() - start
    print(f"Executed Coordinates Time: {run}")
    return {"lat": city_selected['latitude'], 'lng': city_selected['longitude']}

async def main():
    rhyme_result, coordinates_result = await asyncio.gather(rhyme_finder('سپهر'), get_coordinates())
    print("\nRhyme Result:", rhyme_result)
    print("Coordinates Result:", coordinates_result)

if __name__ == "__main__":
    start_time_main_app = time.perf_counter()
    load_dotenv()
    RHYME_SECRET_KEY = os.getenv('RHYME_SECRET_KEY')
    asyncio.run(main())
    run_time_main_app = time.perf_counter() - start_time_main_app
    print(f"\nExecuted Application Time: {run_time_main_app}")
