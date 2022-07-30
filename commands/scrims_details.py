import random
from discord import Message, Member, Embed

from models.database import DB
from models.tags_commands import set_author

async def main(message: Message):

    scrim_name = message.content.split(' ')[2]

    # Creating 
    db = DB()
    curr = db.get_cursor()


    # Combine these into a left join or something
    sql_get_scrim_id = """
    SELECT scrim_id
    FROM scrims 
    WHERE scrim_name = ?
    """
    curr.execute(sql_get_scrim_id, (scrim_name,))
    scrim_id = curr.fetchone()["scrim_id"]

    # Combine these into a left join or something
    sql_get_players="""
    SELECT player_name 
    FROM players 
    WHERE scrim_id = ?
    """
    curr.execute(sql_get_players, (scrim_id,))
    del db

    players = curr.fetchall()
    player_names = "\n".join([player["player_name"] for player in players])

    embed=Embed(title="Scrim Details", description=scrim_name, color=0xe10e0e)
    embed.add_field(name="Scrim Name", value=scrim_name, inline=False)
    embed.add_field(name="Players", value=player_names, inline=False)
    embed=set_author(embed)

    await message.channel.send(embed=embed) 