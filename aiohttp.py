import asyncio
import aiohttp
import argparse
import random

parser = argparse.ArgumentParser(description="Asynchronous Web Server Load Test Tool with Proxies")
parser.add_argument('url', type=str, help='Target URL')
parser.add_argument('-n', '--num_requests', type=int, default=1000, help='Number of requests to send (default 1000)')
parser.add_argument('-p', '--proxy_file', type=str, default='proxyscrape_premium_http_proxies.txt', help='File containing proxies (default proxyscrape_premium_http_proxies.txt)')
args = parser.parse_args()


def load_proxies(proxy_file):
    with open(proxy_file, 'r') as f:
        proxies = f.readlines()
    return [proxy.strip() for proxy in proxies]

def get_random_proxy(proxies):
    return random.choice(proxies)

async def send_request(session, url, proxy):
    proxy_url = f"http://{proxy}"  
    try:
        async with session.get(url, proxy=proxy_url) as response:
            print(f"Received {response.status} from {url} using proxy {proxy}")
            await response.read() 
    except Exception as e:
        print(f"Request failed with proxy {proxy}: {e}")

async def main():
    proxies = load_proxies(args.proxy_file)
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(args.num_requests):
            proxy = get_random_proxy(proxies)  
            task = asyncio.create_task(send_request(session, args.url, proxy))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
