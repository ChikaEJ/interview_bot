import asyncio

from app.bot.main import bot_main

async def main():
    await bot_main()

if __name__ == '__main__':
    asyncio.run(main())