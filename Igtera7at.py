from discord_webhook import DiscordWebhook, DiscordEmbed

import discord

bot = discord.Client()

# Start Command
prefix = "!"

@bot.event

async def on_ready():
    print("{0.user} Bot is Ready".format(bot))

@bot.event

async def on_message(message):

    if message.content.startswith(prefix+"Sugs"):

        # Find from where the Suggestion has send

        From_Server = message.guild.name
        # Cut the suggestion
        Suggestion = message.content[6:]

        # send a message to chat
        await message.channel.send("**سوف يتم معالجة اقتراحك في خلال 3 الى 4 ساعات** :wink: ")
        
        # find the sender
        sender = message.author

        # print the sender and Suggestion
        print(str(sender)+" Has Send The Suggestion "+str(Suggestion))

        url_is = ""
        webhook = DiscordWebhook(url=url_is, content='**New Suggestion**\n **Sender:** `'+str(sender)+'`\n **Suggestion:** `'+str(Suggestion)+'`\n **from server:** `'+str(From_Server)+'`')
        sent_webhook = webhook.execute()
    
# Run Your bot
bot.run('')
