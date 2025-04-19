import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import tensorflow as tf
import numpy as np


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
        await image.save(f"./{image.filename}")
        loaded_image = tf.keras.utils.load_img(f"./{image.filename}",target_size=(300,300))
        loaded_image = tf.keras.utils.img_to_array(loaded_image)
        model = tf.keras.models.load_model("./base_cat_dog_cnn.keras")
        predict = model.predict(np.array([loaded_image]))
        value = "cat" if predict<0.5 else "dog"
        os.remove(f"./{image.filename}")
        await inter.followup.send(f"The image {image.url} is a {value}")
    except Exception as e:
        print(f"error occured {e}")
        await inter.followup.send("error occured")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(os.getenv('TOKEN'))