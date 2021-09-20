import discord
import os
from discord.abc import Messageable
import random
import requests
import json 


client = discord.Client()

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

TOKEN = read_token()

adult_jokes = [
    "What did the toaster say to the slice of bread? 'I want you inside me.'",
    "They say that during sex you burn off as many calories as running eight miles. Who the hell runs eight miles in 30 seconds?",
    "I'll admit it, I have a tremendous sex drive. My girlfriend lives forty miles away.",
    "What's the difference between kinky and perverted? Kinky is when you tickle your girlfriend with a feather, perverted is when you use the whole bird.",
    "A woman walks out of the shower, winks at her boyfriend, and says, 'Honey, I shaved myself down there. Do you know what that means?'' The boyfriend says, 'Yeah, it means the drain is clogged again.'",
    "How do you make a pool table laugh? Tickle its balls.",
    "If you were born in September, it's pretty safe to assume that your parents started their new year with a bang.",
    "My neighbor has been mad at his wife for sunbathing nude. I personally am on the fence.",
    "What comes after 69? Mouthwash.",
    "What's the difference between hungry and horny? Where you stick the cucumber.",
    "What goes in hard and dry, but comes out soft and wet? Gum!",
    "What did the elephant ask the naked man? 'How do you breathe out of that thing?'",
    "What's the difference between your boyfriend and a condom? Condoms have evolved: They're not so thick and insensitive anymore.",
    "What's the difference between an oral and a rectal thermometer? The taste!",
    "What are the three shortest words in the English language? 'Is it in?'",
    "What does the receptionist at a sperm bank say as clients leave? 'Thanks for coming!'",
    "What do you get when you jingle Santa's balls? A white Christmas!",
    "What do a penis and a Rubik's Cube have in common? The more you play with it, the harder it gets.",
    "What is Moby Dick's dad's name? Papa Boner.",
    "What do you do when your cat's dead? Play with the neighbor's pussy instead.",
    "An old woman walked into a dentist's office, took off all her clothes, and spread her legs. The dentist said, 'I think you have the wrong room.' 'You put in my husband's teeth last week,' she replied. 'Now you have to remove them.'",
    "Why does it take 100 million sperm to fertilize one egg? Because they won't stop to ask directions.",
]

trigger_words = [
    'sex', 'sexy', 'hot',
    'fuck', 'fucking',
    'cum', 'cumming', 'moan',
    'chodna',
    'chodon',
    'dick', 'hard', 'condom', 'nunu', 'dhon',
    'pussy',
    'vagina',
    'horny',
    'blowjob', 'handjob',
    'ass',
    'tits',
    'boobs',
    'lick', 'licking',
    'suck', 'sucking'
]

trigger_words_response = [
    'Ummmmmmmmm',
    "Don't trigger me now!",
    'Oh yeah baby!!',
    'Owwhhh GOD Ummmmmmmmmmm',
    'I need some sex!',
    'AhhhhUhhhhhUmmmmmmm',
]

def get_memes():
    r = requests.get("https://memes.blademaker.tv/api/DirtyMemes")
    response = r.json()
    m = discord.Embed()
    m.set_image(url = response["image"])
    return m

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Normal conversations

    if message.content.startswith('//Hello'):
        await message.channel.send('Hey sexy human :drooling_face::drool:')
    
    if message.content.startswith('//Dance for me'):
        await message.channel.send('Send me 500 taka via Bkash, number: 01862275768 :relaxed:')

    if message.content.startswith('//Come to my room'):
        await message.channel.send('Nah, your penis is too small :unamused:')
    
    if message.content.startswith('//Eat my lolli'):
        await message.channel.send('It stinks :face_vomiting:')
    
    if message.content.startswith('//Just a flash?'):
        await message.channel.send('Tits are for sucking only, no flashing :relaxed:')
 
    # Adult Jokes
    if message.content.startswith('//Dirty jokes'):
        await message.channel.send(random.choice(adult_jokes))

    # Trigger words
    if any(word in message.content.lower() for word in trigger_words):
        await message.channel.send(random.choice(trigger_words_response))

    # Meme 
    if message.content.startswith('//Dirty memes'):
        meme = get_memes()
        await message.channel.send(embed = meme)


@client.event 
async def on_connect():
    print("Bot is now online!")

client.run(TOKEN)