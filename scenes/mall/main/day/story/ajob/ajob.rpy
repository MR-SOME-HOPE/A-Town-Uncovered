## A Job ##
label lbl_a_job:
    scene bg mall_day_icecreampy
    with fade
    show pov neutral at left
    with dissolve
    show ala neutral_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    idk "Welcome to Ice Cream'py. What can I get for you today?"
    show pov neutral_talk at left
    show ala neutral at right
    pov "Hey, actually, I was wondering if you guys are hiring at the moment."
    show pov neutral at left
    show ala bored_talk at right
    idk "Actually, funny enough... No really, it's hilarious. You're going to die of laughter."
    show pov embarrassed at left
    show ala bored at right
    idk "..."
    show pov neutral at left
    show ala bored_talk at right
    idk "My manager told me to hire the first person that asks for a job today."
    show pov neutral_talk at left
    show ala bored at right
    pov "Really?"
    show pov neutral at left
    show ala bored_talk at right
    idk "Yeah, no kidding.."
    show pov embarrassed at left
    show ala smirk_talk at right
    idk "Or am I?"
    show pov embarrassed at left
    show ala bored_talk at right
    idk "I'm not."
    show pov confused_talk at left
    show ala bored at right
    pov "No resume or interview or anything?"
    show pov bored at left
    show ala confused_talk at right
    idk "Do you know how to scoop an icecream?"
    show pov bored_talk at left
    show ala confused at right
    pov "I mean, I guess."
    show pov bored at left
    show ala bored_talk at right
    idk "Then you've got yourself a PHD in minimum wage."
    show pov confused_talk at left
    show ala bored at right
    pov "Yay for me?"
    show pov bored at left
    show ala bored_talk at right
    idk "This is how it'll work. I'm basically here every day. You can just come in anytime and take the shift while I work in the backroom."
    show pov bored_talk at left
    show ala bored at right
    pov "What are you doing in the backroom if I may ask."
    show pov bored at left
    show ala bored_talk at right
    idk "No you may not."
    show pov neutral_talk at left
    show ala bored at right
    pov "Fair enough. I'm [povname] by the way."
    show pov neutral at left
    show ala bored_talk at right
    ala "I'm Alanna. You can start tomorrow at the earliest, maybe not. We'll let you know."
    show pov neutral_talk at left
    show ala bored at right
    pov "Alright, thank you so much, Alanna. And thank your boss for me too!"
    show pov bored at left
    show ala bored_talk at right
    ala "Whatever."
    $ nextday_ajob = 1
    $ renpy.notify("New Contact: Alanna")
    if main_story == 20 and nextday_ajob == 1:
        $ renpy.pause(3,hard=True)
        if winc == 0:
            $ renpy.notify("New Objective: Get Back Home and Talk to [missus] in the Afternoon")
        else:
            $ renpy.notify("New Objective: Get Back Home and Talk to Mom in the Afternoon")
    else:
        pass

    jump lbl_mall_day_setup

label lbl_a_job_2:

    scene bg mall_day_icecreampy
    with fade
    show pov neutral at left
    with dissolve
    show ala bored_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "Hi, unless you're here for an icecream, you can start tomorrow, most likely. We're still working things out."
    show pov neutral_talk at left
    show ala bored at right
    pov "Alright, just making sure."

    jump lbl_mall_day_setup
