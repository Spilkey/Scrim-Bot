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
    array_string = m.group(0)
    print(array_string)
    player_names = ast.literal_eval(array_string)

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
    sql_insert_players="""
    INSERT INTO players 
    (scrim_id, player_name)
    VALUES (?, ?);
    """
    player_insert = []
    for player in player_names:
        player_insert.append((scrim_id, player))

    print(player_insert)
    print(sql_insert_players)
    
    curr.executemany(sql_insert_players, player_insert)
    conn.commit()
    del db

    players = '\n'.join(player_names)

    embed=Embed(title="Players Added", description=f"Players: \n {players}", color=0xe10e0e)
    embed=set_author(embed)

    await message.channel.send(embed=embed)
    await scrims_details.main(message)