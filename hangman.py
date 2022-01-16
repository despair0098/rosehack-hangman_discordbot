from dis import dis
from distutils import command
from email import message
import discord
import random
import asyncio
import tracemalloc   
from word import wordList

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    start = False
    user_input = ""
    k = ""
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1
        break

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):

    #async def images corresponds to the state of the hangman dependent on how many tries the player has left
    async def images(tries):
        states = dict()
        #states[0]=(
#("   _____ \n"
#"  |     | \n"
#"  |     |\n"
#"  |     | \n"
#"  |     O \n"
#"  |      \n"
#"  |      \n"
#"__|__\n")),
        states[0]="""
_________        
|       |
|       |   
|       | 
|       |           
|       |

        """ 
        states[1] = """ ```  
                        --------
                        |      |
                        |     😃
                        |      | 
                        |      
                        |      
-
                   ```""", 
        states[2] = """```  
                   --------
                   |      |
                   |     😃
                   |     \| 
                   |      
                   |     
                   -
                   ```""", 
        states[3] = """```  
                   --------
                   |      |
                   |     😃
                   |     \|/ 
                   |      
                   |     
                   -
                   ```""", 
        states[4] = """```  
                   --------
                   |      |
                   |     😃
                   |     \|/ 
                   |      |
                   |     
                   -
                   ```""", 
        states[5] = """```  
                   --------
                   |      |
                   |     😃
                   |     \|/ 
                   |      |
                   |     / 
                   -
                   ```""", 
        states[6] = """```  
                   --------
                   |      |
                   |     💀
                   |     \|/ 
                   |      |
                   |     / \ 
                   -
                   ```"""
        return states[tries]
            
    # async def input():
    #     msg = []
        
    #     command = ""
    #     if message.content[0] != '$':
    #         return
    #     def check(m):
    #         return m.isAlpha() and m.channel == channel
    #     user_message = await bot.wait_for("message", check=check) #$guess a => [$guess] [a]
    #     temp = user_message.content.split()
    #     msg.append(temp)
    #     if msg[0][1:] == "guess":
    #         return msg[1].upper()

    #def getWord() grabs a random word from our word library to set as the target word
    def getWord():
       word = random.choice(wordList)
       return word.upper()


    #async def play(word, message) activates the main game
    async def play(word, message):
        listofwords = list(word)
        word_guessing = "- " * len(word)    # _ _ _ _ _ 
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = len(listofwords)
        channel = message.channel
        def check(m):
            return str(m).isalpha() and m.channel == channel
            #return str(m.content).isalpha() and m.channel == channel
        #await message.channel.send("\n")
        
        while (not guessed) and (tries >= 0):
            #the input for the character goes here\
            #await message.channel.send(await images(tries))
            await message.channel.send("Guess a letter!")
            guessobj = await bot.wait_for('message', check=check)
            guess=guessobj.content
            if len((guess)) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    await message.channel.send(guess+" is correct!")
                elif guess not in listofwords:
                    await message.channel.send(guess+" is not in the word.")
                    tries -=1
                    guessed_letters.append(guess)
                else:
                    await message.channel.send("Awesome! "+guess+" is in the word.")
                    guessed_letters.append(guess)
                    word_list = list(wordCompleted)
                    indexx = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indexx:
                        word_list[index] = guess
                    wordCompleted = "".join(word_list)
                    if "_" not in wordCompleted:
                        guess = True
            elif len(guess) == len(word) and guess.isalpha():
                    if guess in guessed_words:
                            await message.channel.sendt("Successfully guessed the word "+guess+ ":D")
                    elif guess != word:
                            await message.channel.send("Unfortunately, "+ guess+ " is not the word.")
                            tries = 1
                            guessed_words.append(guess)
                    else:
                            guessed = True
                            wordCompleted = word
            else:
                await message.channel.send("Wrong answer")

        await message.channel.send(await images(tries))
        await message.channel.send("testing2")
                            
        if guessed: 
            await message.channel.send("You are the winner! Congrats! Unfortunately, we've run out of every single food on the menu. D: Therefore, I offer you my deepest condolences. Goodbye.")
        else: 
            await message.channel.send("Byeeee")

    async def _command(ctx):
        global times_used
        await ctx.send(f"y or n")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ["y", "n"]


    
    if message.content.lower() == "$start":
        await message.channel.send("Welcome to the Rose Café! If you wish to eat, you must answer my riddle, fiend!")
        start = True
        word = getWord()
        await play(word, message)
            #i have no clue how i generated 4 errors
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    # if message.content=="hello":
    #     # SENDS BACK A MESSAGE TO THE CHANNEL.
    # # def images(tries):
    #     await message.channel.send(
    #             """```  
    #                --------
    #                |      |
    #                |      O
    #                |     \|/ 
    #                |      |
    #                |     / \ 
    #                -
    #                ```
    #             """)    
    

    # $start
    # $guess start
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("OTMyMDE0ODY3MjIzODA1OTYz.YeM0fA.P6gWnUOkGLCEOeAfMP9JvWBKZHk")