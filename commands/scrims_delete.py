import random
from discord import Message, Member, Embed

from models.database import DB
from models.tags_commands import set_author

async def main(message: Message):

    scrim_name = message.content.split(' ')[2]

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
    print(scrim_id)
    
    sql = """
    DELETE FROM scrims 
    WHERE scrim_id = ?
    """
    curr.execute(sql, (scrim_id,))

    # For some f'ing reason foreign keys don't work in sqlite properly
    sql_delete_players="""
    DELETE FROM players 
    WHERE scrim_id = ?
    """

    curr.execute(sql_delete_players, (scrim_id,))
    conn.commit()
    del db

    if(scrim_id):
        embed=Embed(title="Scrim Deleted", description=scrim_name, color=0xe10e0e)
        embed=set_author(embed)
    else:
        embed=Embed(title="Scrim not deleted", description=scrim_name, color=0xe10e0e)
        embed=set_author(embed)

    await message.channel.send(embed=embed) 