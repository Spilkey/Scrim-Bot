import random
from discord import Message, Member, Embed
from commands import scrims_details

from models.database import DB
from models.tags_commands import set_author

import re
import ast

async def main(message: Message):

    scrim_name = message.content.split(' ')[2]

    m = re.search(r"\[[^()]+\]", message.content)
    player_name = m.group(0).replace("[", "").replace("]", "")

    # Creating 
    db = DB()
    conn = db.get_conn()
    curr = db.get_cursor()

    sql_get_scrim_id = """
    SELECT scrim_id
    FROM scrims 
    WHERE scrim_name = ?
    """
    curr.execute(sql_get_scrim_id, (scrim_name,))
    scrim_id = curr.fetchone()["scrim_id"]

    # For some f'ing reason foreign keys don't work in sqlite properly
    sql_delete_players="""
    DELETE FROM players 
    WHERE scrim_id = ? 
    AND player_name = ?
    """

    curr.execute(sql_delete_players, (scrim_id, player_name))
    conn.commit()
    del db

    embed=Embed(title="Player Removed", description=f"Player: {player_name} removed from {scrim_name} ", color=0xe10e0e)
    embed=set_author(embed)

    await message.channel.send(embed=embed)
    await scrims_details.main(message)