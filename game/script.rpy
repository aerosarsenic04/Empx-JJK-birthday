define e = Character("Mook")
define kugipoint = False
define megupoint = False



label start:
    $ megupoint = False
    $ kugipoint = False
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


label help_yuji:
    "he's helpless"
    "he might be a great and thoughtful guy, but he sure is indecisive."
    "mind gving him a hand? (you have no choice)"

yu "Hey, thanks for helping me out! I can't really decide what to get gojo-sensei"
yu "Huh? Why don't Kugisaki and Fushiguro help? They already know what to get and I want to get something unique!"
yu "I was thinking of heading to Ginza to check stuff out!"
yu "And maybe we can finish up at takeshita street"
yu "You know, harajuku!"

yu "oh, looks like we only have a few hours left... the party starts at 6"
yu "let's get going!"
yu "Oh, by the way, I only have ¥15,000 to spend..."

    "You head to Ginza via subway"
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