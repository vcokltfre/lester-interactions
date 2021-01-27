from discord_interactions import InteractionResponseType, InteractionResponseFlags

def respond_default(message: str) -> dict:
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "content": message,
            "allowed_mentions":{
                "users": False
            }
        }
    }

def respond_ephemeral(message: str) -> dict:
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE,
        "data": {
            "content": message,
            "allowed_mentions":{
                "users": False
            },
            "flags": InteractionResponseFlags.EPHEMERAL
        }
    }

def respond_default_embed(embed: dict) -> dict:
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "embeds": [embed],
            "allowed_mentions":{
                "users": False
            }
        }
    }

def respond_ephemeral_embed(embed: dict) -> dict:
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE,
        "data": {
            "embeds": [embed],
            "allowed_mentions":{
                "users": False
            },
            "flags": InteractionResponseFlags.EPHEMERAL
        }
    }