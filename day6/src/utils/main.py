import sys 
import os
import aiohttp
import asyncio

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)
from src.configurations.conf import config  

async def user_service(url, id, session):
    user_service_url = f"{url}/users/{id}"
    print(user_service_url)
    async with session.get(user_service_url) as response:
        if response.status == 200:
            user_data = await response.json()
            return {
                "id": user_data["id"],
                "name": user_data["name"],
                "email": user_data["email"]
            }
        else:
            print(f"Failed to fetch user data. Status code: {response.status}")
            return None

async def post_service(url, id, session):
    post_service_url = f"{url}/posts/{id}"
    print(post_service_url)
    async with session.get(post_service_url) as response:
        if response.status == 200:
            post_data = await response.json()
            return {
                "id": post_data["id"],
                "title": post_data["title"],
                "body": post_data["body"]
            }
        else:
            print(f"Failed to fetch post data. Status code: {response.status}")
            return None

async def album_service(url, id, session):
    album_service_url = f"{url}/albums/{id}"
    print(album_service_url)
    async with session.get(album_service_url) as response:
        if response.status == 200:
            album_data = await response.json()
            return {
                "user_id": album_data["userId"],
                "id": album_data["id"],
                "title": album_data["title"]
            }
        else:
            print(f"Failed to fetch album data. Status code: {response.status}")
            return None

async def photo_service(url, id, session):
    photo_service_url = f"{url}/photos/{id}"
    print(photo_service_url)
    async with session.get(photo_service_url) as response:
        if response.status == 200:
            photo_data = await response.json()
            return {
                "album_id": photo_data["albumId"],
                "id": photo_data["id"],
                "title": photo_data["title"],
                "url": photo_data["url"],
                "thumbnail_url": photo_data["thumbnailUrl"]
            }
        else:
            print(f"Failed to fetch photo data. Status code: {response.status}")
            return None

async def dashboard_service(url):
    async with aiohttp.ClientSession() as session:
        # Run all requests in parallel
        user_data, post_data, album_data, photo_data = await asyncio.gather(
            user_service(url, 1, session),
            post_service(url, 1, session),
            album_service(url, 1, session),
            photo_service(url, 1, session)
        )
        
        dashboard_data = {
            "user": user_data,
            "post": post_data,
            "album": album_data,
            "photo": photo_data
        }
        return dashboard_data

if __name__ == "__main__":
    conf = config()
    print(f"Connecting to: {conf.url}")
    try:
        # Use standard asyncio.run
        result = asyncio.run(dashboard_service(conf.url))
        print("\nDashboard Data Results:")
        print(result)
    except aiohttp.ClientError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")