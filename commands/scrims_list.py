import random
from discord import Message, Member, Embed

from models.database import DB
from models.tags_commands import set_author

async def main(message: Message):

    # Creating 
    db = DB()
    curr = db.get_cursor()
    
    sql = """
    SELECT * 
    FROM scrims
    """

    curr.execute(sql)
    results = curr.fetchall()
    del db

    scrims = "\n".join([row["scrim_name"] for row in results])

    print(scrims)
    embed=Embed(title="Scrim List", description=scrims, color=0xe10e0e)
    embed=set_author(embed)

    await message.channel.send(embed=embed) 