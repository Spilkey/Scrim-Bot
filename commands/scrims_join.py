import random
from discord import Message, Member, Embed
from commands import scrims_details

from models.database import DB
from models.tags_commands import set_author

async def main(message: Message):

    scrim_name = message.content.split(' ')[2]


    player: Member = (message.author)
    player_id = player.id

    # Creating 
    db = DB()
    conn = db.get_conn()
    curr = db.get_cursor()

    get_scrim_sql = """
    SELECT scrim_id
    FROM scrims
    WHERE scrim_name = ?
    """
    curr.execute(get_scrim_sql, (scrim_name, ))
    id = curr.fetchone()["scrim_id"]
    
    sql = """
    INSERT INTO players 
    VALUES(?, ?, ?)
    """

    curr.execute(sql, (player_id, id, player.display_name))
    conn.commit()
    del db

    db = DB()
    curr = db.get_cursor()

    get_players_sql = """
    SELECT *
    FROM players
    WHERE scrim_id = ?
    """

    curr.execute(get_players_sql, (id, ))
    players = curr.fetchall()

    players_list = "\n".join([row["player_name"] for row in players])
    del db
    embed=Embed(title="Joined Scrim", description=f"{player.display_name} has joined scrim {scrim_name}", color=0xe10e0e)

    await message.channel.send(embed=embed) 
    await scrims_details.main(message)