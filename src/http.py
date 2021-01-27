from aiohttp import ClientSession

from config.config import TOKEN

BASE = "https://discord.com/api/v8"


class HTTP:
    def __init__(self):
        self.sess = ClientSession(headers={'Authorization': f'Bot {TOKEN}'})

    async def init(self):
        if self.sess.closed:
            self.sess = ClientSession(headers={'Authorization': f'Bot {TOKEN}'})

    async def send_message(self, channel: str, message: str, allowed_mentions: dict = {}):
        async with self.sess.post(BASE + f"/channels/{channel}/messages", json={"content":message, **allowed_mentions}) as resp:
            return await resp.json()

    async def add_role(self, guild, user, role):
        async with self.sess.put(BASE + f"/guilds/{guild}/members/{user}/roles/{role}") as resp:
            return await resp.status == 204

    async def del_role(self, guild, user, role):
        async with self.sess.delete(BASE + f"/guilds/{guild}/members/{user}/roles/{role}") as resp:
            return await resp.status == 204