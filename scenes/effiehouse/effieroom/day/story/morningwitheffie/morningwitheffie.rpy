## Morning With Effie ##
label lbl_morning_with_effie:
    "The next morning..."

    scene bg effieroom_day
    with fade
    show pov neutral_talk at left
    with dissolve
    show eff neutral at right
    with dissolve
    pov "Morning, Effie. I guess thanks for letting me stay the night?"
    show pov neutral at left
    show eff neutral_talk at right
    eff "Oh sure, no problem."
    show pov bored_talk at left
    show eff neutral at right
    pov "I don't mean to sound ungrateful or selfish or anything but I really have to head home."
    show pov sad_talk at left
    if winc == 0:
        pov "My [mumrole] is probably going to kill me for staying over last night."
    else:
        pov "My mom is probably going to kill me for staying over last night."
    show pov neutral at left
    show eff neutral_talk at right
    eff "No worries, dude. Let me just check on Dad to see if he's still asleep."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Alright."
    show pov neutral at left
    hide eff neutral
    with dissolve
    $ renpy.pause ()
    show eff neutral_talk at right
    with dissolve
    eff "Yeah, the coast is clear. You should be able to leave now."
    if effie_points == 0:
        show eff sad_talk at right
        eff "Sorry about last night, let's forget that it happened."
        show pov neutral_talk at left
        show eff neutral at right
        pov "Don't worry, Effie. We'll keep it just between us."
    else:
        eff "Thank you again for last night, I had fun. I apologise for being so straightforward and ‘aggressive'."
        show pov neutral_talk at left
        show eff neutral at right
        pov "The pleasure is mine. Hope we can do it again someday."
        show pov neutral at left
        show eff neutral_talk at right
        eff "You just read my mind."
    show pov neutral_talk at left
    show eff neutral at right
    pov "I'll see you around later."
    show pov neutral at left
    show eff neutral_talk at right
    eff "See you, [povname]."
    
    $ main_story = 15
    $ renpy.notify("New Objective: Get Back Home")

    jump lbl_effieroom_day
