## The Purple Trail
label lbl_the_purple_trail_revisit:
    ## Time skip
    scene black
    with fade
    $ renpy.pause()
    "A few minutes later…"

    pov "Aye?!"
    pov "Get off me!"

    if winc == 0:
        sis "[missus] said I can have you."
    else:
        sis "Mom said I can have you."

    mum "I said no such thing."

    sis "Just close your eyes and let me feast."
    if winc == 0:
        sis "You want in on this, [missus]?"
    else:
        sis "You want in on this, mom?"

    mum "*Sigh*"
    mum "Fine."
    mum "Stay still, [povname]."
    if winc == 0:
        mum "[sister] has that scary look in her eye."
    else:
        mum "Your sister has that scary look in her eye."

    pov "Pfft, you’ve got to be kidding me."

    mum "I didn’t pack dessert so you’re our next best thing."

    ## Mom and Sister gives you a BJ in the grass.
    scene thepurpletrail_bj1
    with fade
    $ renpy.pause()
    show thepurpletrail_bj2
    $ renpy.pause()
    show bg thepurpletrail_3_6
    with vpunch
    $ renpy.pause()
    
    pov "Fuck-"
    pov "Hope you guys got your dessert fill."

    sis "Oooh surprise icing."

    mum "Yummy, just enough to hit the spot."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

image thepurpletrail_bj1:
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_1.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_5.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.3
    repeat

image thepurpletrail_bj2:
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_1.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_5.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.2
    repeat
