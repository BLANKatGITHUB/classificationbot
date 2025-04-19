import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()


intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.slash_command(name="hello",description="greets the user")
async def greet(inter:disnake.ApplicationCommandInteraction,user:disnake.Member=commands.Param(description="user to greet")):
    await inter.response.send_message(f"hello {user.mention}")

@bot.slash_command(name="dog_or_cat",description="classify whether a image is cat or dog")
async def cat_or_dog(inter:disnake.ApplicationCommandInteraction,image:disnake.Attachment=commands.Param(description="image to classify")):
    await inter.response.defer()
    if not image.filename.endswith((".jpg",".jpeg",".png")):
        await inter.followup.send("Invalid attachment type")
        return 
    try:
        await inter.followup.send(f"heres your image {image.url}")
    except Exception as e:
        print(f"error occured {e}")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(os.getenv('TOKEN'))