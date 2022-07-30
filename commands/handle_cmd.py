from commands import scrims_create, scrims_kick, scrims_list, scrims_delete, scrims_join, scrims_details, scrims_generate, scrims_kick, scrims_add
from discord import Message

async def handle(self, message: Message):
    # Takes in a discord.py message
    message_content = message.content

    # # Run command files here
    # if (message_content == "tonight on bottom gear"):
    #     await btm_gear.main(self, message)
    # elif (message_content.startswith("avatar")):
    #     await avatar.main(self, message)
    # elif(message_content.startswith("magik")):
    #     await magik.main(self, message)
    # elif(message_content.startswith("tag") or message_content.startswith("tags")):
    #     await tags.main(self, message)
    # else:
    #     await message.channel.send("Errrrny nice")

    if(message_content.startswith("/scrims")):
        if("create" in message_content):
            return await scrims_create.main(message=message)
        elif("list" in message_content):
            return await scrims_list.main(message=message)
        elif("delete" in message_content):
            return await scrims_delete.main(message=message)
        elif("join" in message_content):
            return await scrims_join.main(message=message)
        elif("details" in message_content):
            return await scrims_details.main(message=message)
        elif("generate" in message_content):
            return await scrims_generate.main(message=message)
        elif("kick" in message_content):
            return await scrims_kick.main(message=message)
        elif("add" in message_content):
            return await scrims_add.main(message=message)
