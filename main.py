import asyncio
import json
import sys
import aiohttp
import validators
import logging
from const import HTTP_METHODS as http_methods


async def check_method(session, url, method):
    try:
        async with session.request(method, url, timeout=10) as response:
            return (method, response.status)
    except Exception as e:
        logging.error(f"Ошибка: {e}")
    return (method, None)


async def check_url_method(session, url):
    result = {}
    tasks = [check_method(session, url, method) for method in http_methods]
    results = await asyncio.gather(*tasks)
    for method, status in results:
        if status != 405 and status != None:
            result[method] = status

    return (url, result)


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        results = {}
        for url in urls:
            if validators.url(url):
                tasks.append(check_url_method(session, url))
            else:
                print(f'Строка "{url}" не является ссылкой.')
        url_results = await asyncio.gather(*tasks)
        for url, methods in url_results:
            if methods:
                results[url] = methods
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    urls = sys.argv[1:]
    asyncio.run(main(urls))
