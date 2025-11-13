import httpx
import asyncio

async def get_data():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.github.com")
        print(r.json())

async def main():
  await get_data()

if __name__ == "__main__":
    asyncio.run(main())

