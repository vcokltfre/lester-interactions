from src.responses import respond_ephemeral
from src.utils import getop

rolemap = {
    "228674040871649290": "PC",
    "228674193439457280": "Xbox",
    "228674178566455297": "Playstation",
    "288129330293374986": "Modder",
    "727278556182347866": "Server News",
    "727278657797881914": "GTA News"
}


class RoleHandler:
    def __init__(self, http):
        self.http = http

    async def call(self, data: dict) -> dict:
        name = data["data"]["name"]
        ops = data["data"]["options"]
        roleid = getop("role", ops)
        guildid = data["guild_id"]
        userid = data["member"]["user"]["id"]

        if name == "join":
            success = await self.http.add_role(guildid, userid, roleid)
            content = f"Successfully joined role {rolemap[roleid]}"
        else:
            success = await self.http.del_role(guildid, userid, roleid)
            content = f"Successfully left role {rolemap[roleid]}"

        if success:
            return respond_ephemeral(content)
        return respond_ephemeral("Uh oh! Something went wrong, please try again in a couple of seconds, and if the issue peresists report it to modmail.")