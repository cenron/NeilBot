import os
import pathlib
import random
import sys

import discord
import yaml
from discord.ext import commands
# Only if you want to use variables that are in the config.yaml file.
from discord.ext.commands import BucketType

if not os.path.isfile("config.yaml"):
    sys.exit("'config.yaml' not found! Please add it and try again.")
else:
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)


# Here we name the cog and create a new class for the cog.
class Neilisms(commands.Cog, name="neilisms"):
    def __init__(self, bot):
        self.bot = bot
        self.supported_image_types = ['.png', '.jpg', '.jpeg', '.gif']

    @commands.command(name="booty")
    @commands.cooldown(1, 60, BucketType.user)
    async def booty(self, context):
        """
        Provides a a random booty picture.
        """

        # Get our asset directory from the config.
        asset_root = config['asset_dir']
        booty_img_dir = os.path.join(asset_root, 'img/booty')
        # Get the channel we want to limit this command to.

        channel = self.bot.get_channel(config['booty_cmd_channel_id'])

        # Make sure the directory we are pointing to is a actually a valid directory.
        if os.path.isdir(booty_img_dir):
            # Now we need to get all the images in the booty directory.
            booty_list = os.listdir(booty_img_dir);

            # We keep generating random numbers
            while True:
                image_name = booty_list[random.randrange(len(booty_list) - 1)]
                file_ext = pathlib.Path(image_name).suffix
                if file_ext in self.supported_image_types:
                    await channel.send(file=discord.File(os.path.join(booty_img_dir, image_name)))
                    break
        else:
            embed = discord.Embed(
                title="Error!",
                description="Could not find booty pictures :(",
                color=config["error"]
            )
            await context.send(embed=embed)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Neilisms(bot))
