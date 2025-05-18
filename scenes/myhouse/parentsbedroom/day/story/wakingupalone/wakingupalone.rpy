label lbl_waking_up_alone:
    #-The Mc wakes up on Missus bed all alone, if he didn’t had a threesome the night before or just had foreplay with one of the girls, he will be fully clothed, but if he did achieved a threeway, he will wake up naked-
    scene bg parentsbedroom_day
    with fade
    $ renpy.pause(1.0)
    window show dissolve
    pov "Mnnn…" with dissolve
    window hide dissolve
    $ renpy.pause(0.5)

    if parentsbedroommovie_threesome == 0:
        show pov confused at left
    elif parentsbedroommovie_threesome == 3:
        show povn confused at left
    with dissolve
    $ renpy.pause(1.0)

    pov "Mmm.."
    if parentsbedroommovie_threesome == 0:
        show pov confused_talk at left
    elif parentsbedroommovie_threesome == 3:
        show povn confused_talk at left
    with dissolve
    pov "W-What?"

    #-The Mc sits up in bed-
    if parentsbedroommovie_threesome == 0:
        show pov embarrassed_talk at left
    elif parentsbedroommovie_threesome == 3:
        show povn embarrassed_talk at left
    pov "Where did they…"

    if parentsbedroommovie_threesome == 0:
        show pov shocked at left
    elif parentsbedroommovie_threesome == 3:
        show povn shocked at left
    mum "[povname]!"
    if parentsbedroommovie_threesome == 0:
        show pov confused_talk at left
    elif parentsbedroommovie_threesome == 3:
        show povn confused_talk at left
    pov "Y-Yeah?!"

    mum "Come on down, sweetie!"
    if parentsbedroommovie_threesome == 0:
        show pov confused at left
    elif parentsbedroommovie_threesome == 3:
        show povn confused at left
    pov "{i}They must be in the kitchen.{/i}"
    mum "Breakfast is ready!"


    #-If a threeway scene was reached-
    if parentsbedroommovie_threesome == 3:
        show povn confused at left
        sis "And keep the clothes off!"
        show povn confused_talk at left
        pov "What?"
        show povn shocked at left
        sis "You heard the woman: get that naked butt in here, you well endowed dunce!"
        show povn confused at left
        mum "Don’t you dare!"
        #$ renpy.pause(2.0)
        #show mum confused at Position(xpos=1200) with dissolve
        #$ renpy.pause(0.5)
        #show mum confused_talk at Position(xpos=1200)
        mum "No naughty stuff before or while we are eating!"
        show povn shocked at left
        sis "Aww, come on, [missus]!"
        show povn embarrassed at left
        sis "Why not have a “dinner and show”?"
        #show sis smirk at right
        mum "Because it’s breakfast and none of us have taken a shower. Now zip it!"
        show povn bored at left
        mum "And you come down with clothes, now, [povname]!"


    #-If the threeway scene was Not reached at all-
    elif parentsbedroommovie_threesome == 0:
        show pov embarrassed at left
        mum "Quickly darling, it’s going to get cold!"
        show pov embarrassed_talk at left
        pov "Y-Yeah, coming!"
        show pov embarrassed at left
        sis "Get down already, she won’t let me start eating until we are all together, and I’m starving down here!"

    if parentsbedroommovie_threesome == 0:
        show pov embarrassed_talk at left
    elif parentsbedroommovie_threesome == 3:
        show povn embarrassed_talk at left
    pov "R-Right!"
    if parentsbedroommovie_threesome == 0:
        show pov neutral_talk at left
    elif parentsbedroommovie_threesome == 3:
        show povn neutral_talk at left
    pov "Sorry, I’ll be right there!"

    $ main_story = 81

    if parentsbedroommovie_threesome in (0,3):
        jump lbl_parentsbedroom_day_setup
    else:
        jump lbl_mybedroom_day_setup
