define e = Character("Eileen")
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

label help_megumi:
    "... You really thought megumi would need your help?"
    "nah, he doesn't want help anyways... he'll be fine"
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
