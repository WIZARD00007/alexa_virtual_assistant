import random
import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
   engine.say(text)
   engine.runAndWait()
def answer():
     try:
        with sr.Microphone() as source:
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command=command.lower()





     except:
         pass
     return command
def challenges():
    questions=['Blindfolded drawing challenge.',' Pizza challenge.',' Chinese whisper challenge.','Toss and talk ball.',' Blind makeup challenge. ',
               'No thumbs challenge.','Pass the orange challenge','Jelly bean tasting challenge.', 'Try not to laugh challenge.','Seven-second challenge .','Memorize challenge.',
          ' guess who challenge .','Blindfolded food tasting challenge.','Guess the song.' ]

    rand_item=random.choice(questions)
    print(rand_item)
    talk(rand_item)

    if rand_item=='Blindfolded drawing challenge.':
        talk('You would need a sheet of paper or a book and a pencil. The participants need to wear a blindfold and attempt to draw an object of their choice. Alternatively, before beginning each round, you can select a theme, such as fashion, kitchen, dinosaurs, spaghetti, animals, or famous characters, and challenge them further by setting a time limit.')
    elif rand_item=='Pizza challenge.':
        talk('You need to get some ingredients, not necessarily pizza toppings, and place them in brown paper bags, so they’re not visible to the participants. If you have enough players, you can divide them into teams.')
    elif rand_item=='Chinese whisper challenge.':
        talk('You have to get the children to sit in a circle. Ensure there’s enough distance maintained so the children cannot hear each other’s whisper. The person who starts has to think of something silly or complicated and whisper it to the person on their right. The whispering continues until it reaches the last player. Once it comes to the last player, they say the word or phrase out loud so everyone can hear how much it has changed from the first whisper. What you hear would surprise you!')
    elif rand_item=='Toss and talk ball.':
        talk('''Take a plastic ball and write a bunch of questions all over it. Make the children sit in a circle and toss the ball around. When they catch the ball, they have to answer the question closest to their right index finger. After answering, they toss it again.
Depending on the children’s age, the questions can be changed. You can go with your favorite color, favorite movie, a sports figure you would love to meet or name your best friend.''')
    elif rand_item=='Blind makeup challenge.':
        talk('''You need to blindfold each participant and ask them to do their makeup themselves. The goal is to do a perfect makeup, but the outcome would be unexpected! You can also split the participants into teams, and the neatest result wins the challenge. Don’t forget to have a camera and plenty of makeup remover in hand. Also, adult supervision is recommended.

''')
    elif rand_item=='No thumbs challenge.':
        talk('Tape the participants’ thumbs in a way they cannot use them. Once that’s done, give them a simple task such as open a door, put clothes on, eat a bowl of spaghetti, hold a pencil, or put on nail polish. Then sit back and watch as this simple task can become a lot more challenging and hilarious.')
    elif rand_item=='Pass the orange challenge':
        talk(''' you will enjoy the activity. sit in a circle or stand in a line. The game is simple; you need to put an orange under the chin of the first person who must hold it using their chin and neck and then pass it to the next person in line, without using hands. The transfer has to be direct from neck to neck.

If the orange falls, the team has to start all over. You can play this game in teams and see which team passes the orange down the line first. The game can even help to break the ice and improve relationships.''')
    elif rand_item=='Jelly bean tasting challenge.':
        talk('If you’re crazy about jelly beans and can’t stop at just one, the challenge is for you. You would need a bunch of children and a bag of jelly beans. Each child has to close their eyes, taste one jelly bean, and guess the flavor. Record the answers to see who’s right and repeat the round.')
    elif rand_item=='Try not to laugh challenge.':
        talk('You have to watch a funny video or a series of videos without grinning, laughing, or breaking into a smile. The first player to smile, grin, or laugh loses the game. Seems easy? It’s not that easy to keep a straight face!')
    elif rand_item=='Seven-second challenge .':
        talk('''Change your hair to a ponytail
Add mascara with no mistakes.
Close your eyes and open the SMS app on your phone.
Count one to ten in a second language.
Do ten standard push-ups.
Put on lipstick without using any of your hands.
Hop on one leg for 20 meters.
Invent a challenge and do it.
Name five countries in the EU.
Name all the chess pieces. extra''')
    elif rand_item=='Memorize challenge.':
        talk('''You can play the memory challenge in multiple ways. First, you can either play with different cards, keep them face down, and match the right ones. The other way is to listen to a part of a book/newspaper or magazine and then recite the same. You can even recite some themes/words/phrases in random, including spaghetti, flowers, fashion, fingers, mirror, or balls. Lastly, display some items and give them a time limit to memorize the order. Next, remove some items, and the participants have to guess the missing items.''')
    elif rand_item==' guess who challenge .':
        talk('''You can play the challenge individually or in teams. If it’s individually, one participant goes up and makes an impression of selected characters, and the others guess. The person with the best impression wins the challenge. If it’s in teams, one team member goes up and makes an impression while the others from the same team take a guess. At the end of the game, the team with the highest number of correct guesses wins.

You can base the themes on celebrities, musicians, animals, characters, friends, and presidents. For instance, imitate Mickey Mouse or make noises like a sheep. It’s a fun game that gets children moving and makes them think outside the box!''')
    elif rand_item=='Blindfolded food tasting challenge.':
        talk('The challenge requires children to become blindfolded, taste different foods, and guess the name of the food. ')
    elif rand_item=='Guess the song.':
        talk('''You would need two people to pair up. Both of them have to squeeze into one oversized T-shirt. Use the T-shirt to jumble your arms. Once the duo is ready, they have to perform tasks such as putting on makeup, drinking, eating, or brushing their teeth. You can think of some tasks that will make this challenge uber fun and even more entertaining. It’s best to have some parental supervision during this task.''')
    answer()
try:
    answer()




except:
    pass
