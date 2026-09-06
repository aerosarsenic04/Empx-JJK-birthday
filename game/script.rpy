define e = Character("Mook", color="#3e883e")
define yu = Character("Yuji", color="#f3aebf")
define m = Character("Megumi", color="#0e1252")
define k = Character("Kugisaki", color="#f09124")
define go = Character("Gojo", color="#ff0000")
image mook = "mook.png"

define kugipoint = False
define megupoint = False

#SECTION - GAME START

label start:
    $ megupoint = False
    $ kugipoint = False


    show mook at left
    e "Hey, looks like it's your birthday!"
    e "or, maybe it isn't. That's okay too!"
    "so, looks like you're here to... celebrate, huh?"

"Help the students prepare for gojo's birthday party!"
menu option_1:
    "Help yuji":
        jump help_yuji
    "Help megumi" if megupoint == False:
        jump help_megumi
    "Help kugisaki" if kugipoint == False:
        jump help_kugisaki
# not me genuinely forgetting renpy syntax and having to relearn again sighs

label help_yuji:
    "he's helpless"
    "he might be a great and thoughtful guy, but he sure is indecisive."
    "mind gving him a hand? (you have no choice)"

    yu "Hey, thanks for helping me out! I can't really decide what to get gojo-sensei"
    yu "Huh? Why don't Kugisaki and Fushiguro help? They already know what to get and I want to get something unique!"
    yu "I was thinking of heading to Ginza to check stuff out!"
    yu "And maybe we can finish up at Takeshita street"
    yu "You know, Harajuku!"

    yu "oh, looks like we only have a few hours left... the party starts at 6"
    yu "let's get going!"
    yu "Oh, by the way, I only have ¥15,000 to spend..."

    "You head to Ginza via subway"
    "It is currently 2PM"

    "Yuji snoozes off on the subway, since the ride from the outskirts of Tokyo to Ginza is a long one."
    "You decide to pass the time by..."

menu option_game:
    "Play chess":
        jump play_chess #I just know this is gonna be a huge pain BUT it would be funny so...
    "Look out the window":
        jump scene_subwindow
    "Look at memes on Instagram":
        jump brainrot

label scene_subwindow:
    "You look out the subway window... and see nothing"

label brainrot:
    "You slide out your phone and pull up Instagram..."
    "It doesn't take long before the typical brainrot on your FYP floods your screen"
    "You find yourself laughig ominusly at random memes."
    "You garner a few odd stares, but nothing can come between you and your memes"

    call screen instagram_memes #TODO - Build the meme screen! make scrollable.

    "After a long while, you arrive at Tokyo station and wake Yuji up so you can transfer to the Ginza line."
    

#SECTION - Start stuff
label help_megumi:
    "... You really thought megumi would need your help?"
    "nah, he doesn't want help anyways... he'll be fine"
    m "Thanks, but I'm fine. I have sensei's credit card."
    "yuji on the other hand..."
    $ megupoint = True
    jump option_1

label help_kugisaki:
    "Did you seriously think kugisaki would need your help?"
    "she's a pro at this stuff, she's got a whole plan for her gift, while also maximizing her time shopping around for cute stuff!"
    "better worry about someone else"
    $ kugipoint = True
    jump option_1


label end:
    return