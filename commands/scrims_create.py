import random
import sqlite3
from discord import Message, Member, Embed
from commands import scrims_details

from models.database import DB
from models.tags_commands import set_author

async def main(message: Message):

    # scrim lobby name
    scrim_name = message.content.split(' ')[2]

    # host
    host: Member = (message.author)
    host_id = host.id
    
    # Creating 
    db = DB()
    conn = db.get_conn()
    curr = db.get_cursor()
    
    sql = """
    INSERT INTO scrims
    (scrim_name, host_id)
    VALUES (?,?)
    """

    try:          
        curr.execute(sql, (scrim_name, host_id))
        conn.commit()

        embed=Embed(title="Scrim Created", description="Scrim has been created", color=0xe10e0e)
        embed=set_author(embed)
        embed.add_field(name="Host", value=host.display_name, inline=False)
        embed.add_field(name="Scrim Name", value=scrim_name, inline=False)
        embed.add_field(name="Join", value=f""" ```/scrims join {scrim_name}```   """, inline=False)
        embed.add_field(name="Add Players", value=f""" ```/scrims add {scrim_name} ['player1', 'player2', 'player3']```   """, inline=False)
        embed.add_field(name="Delete Scrim", value=f""" ```/scrims delete {scrim_name}```   """, inline=False)
        embed.add_field(name="Scrim Details", value=f""" ```/scrims details {scrim_name}```   """, inline=False)
        embed.add_field(name="Generate Teams", value=f""" ```/scrims generate {scrim_name}```   """, inline=False)

    except sqlite3.IntegrityError as e: 
        embed=Embed(title="Scrim Not Created", description="Scrim already exists", color=0xe10e0e)
    finally:
        del db

    await message.channel.send(embed=embed)
    await scrims_details.main(message)