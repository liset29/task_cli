import pytest
import aiohttp
from main import check_method, check_url_method, main
from const import HTTP_METHODS as http_methods
from aioresponses import aioresponses


@pytest.mark.asyncio
async def test_check_method():
    url = "http://example.com"
    method = "GET"

    with aioresponses() as m:
        m.get(url, status=200)

        async with aiohttp.ClientSession() as session:
            result = await check_method(session, url, method)
            assert result == (method, 200)


@pytest.mark.asyncio
async def test_check_url_method():
    url = "http://example.com"

    with aioresponses() as m:
        for method in http_methods:
            m.add(method.lower(), url, status=200)

        async with aiohttp.ClientSession() as session:
            result_url, methods = await check_url_method(session, url)
            assert result_url == url
            assert all(methods[m] == 200 for m in methods)


@pytest.mark.asyncio
async def test_main_valid_url(mocker):
    urls = ["http://example.com"]

    with aioresponses() as m:
        for method in http_methods:
            m.add(method.lower(), urls[0], status=200)

        mock_print = mocker.patch('builtins.print')
        await main(urls)
        mock_print.assert_called()


@pytest.mark.asyncio
async def test_main_invalid_url(mocker):
    urls = ["invalid_url"]

    mock_print = mocker.patch('builtins.print')
    await main(urls)
    mock_print.assert_any_call('Строка "invalid_url" не является ссылкой.')
