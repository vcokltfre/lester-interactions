from src.responses import respond_ephemeral_embed, respond_default_embed

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
            func = respond_default_embed
        else:
            func = respond_ephemeral_embed

        fields = []
        for name, url in services.items():
            online = await self.http.pong(url)
            fields.append({
                "name": name,
                "value": YES if online else NO
            })

        e = {
            "title": "Lester Interactions",
            "description": f"Bot is online!\n\n[Source](https://github.com/vcokltfre/lester-interactions)\n\nComponent Statuses:",
            "fields": [
                {
                    "name": "LISC-Webserver",
                    "value": YES
                }
            ]
        }