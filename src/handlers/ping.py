from src.responses import respond_ephemeral, respond_default

CHANNELS = [
    "802591454953865236",
    "755412864142934046",
    "464807048148942868",
    "779479420481175554"
]

services = {
    "GTAO-Website": "http://gtaodiscord.com",
}

YES = "<:Yes:744714896666787900> Online!"
NO = "<:No:744714930946572371> Offline!"


class PingHandler:
    def __init__(self, http):
        self.http = http

    async def call(self, data: dict) -> dict:
        channel = data["channel_id"]

        if channel in CHANNELS:
            func = respond_default
        else:
            func = respond_ephemeral

        statuses = [f"LISC-Webserver:".ljust(16) + f"  {YES}"]
        for name, url in services.items():
            online = await self.http.pong(url)
            statuses.append(f"{name}:".ljust(16) + f"  {YES if online else NO}")

        content = f"**__Lester Interactions Ping__**\n\nBot is online.\n\nService Statuses:{'\n'.join(statuses)}"

        return func(content)