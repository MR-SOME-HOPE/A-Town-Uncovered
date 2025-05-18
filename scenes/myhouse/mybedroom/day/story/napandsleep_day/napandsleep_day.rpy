## Day Nap ##
label lbl_mybedroom_day_nap:
    $ gtime += 1
    if gtime == 1:
        ## Nap Day Graphic
        scene bg mybedroom_day_nap
        with dissolve
        $ renpy.pause(1,hard=True)
        show bg mybedroom_day
        with dissolve
        if day == 0:
            $ renpy.notify("Monday Afternoon")
        elif day == 1:
            $ renpy.notify("Tuesday Afternoon")
        elif day == 2:
            $ renpy.notify("Wednesday Afternoon")
        elif day == 3:
            $ renpy.notify("Thursday Afternoon")
        elif day == 4:
            $ renpy.notify("Friday Afternoon")
        elif day == 5:
            $ renpy.notify("Saturday Afternoon")
        elif day == 6:
            $ renpy.notify("Sunday Afternoon")

        jump lbl_mybedroom_day_setup
    elif gtime == 2:
        ## Nap to Night Graphic
        scene bg mybedroom_day_nap
        with dissolve
        show bg mybedroom_night_nap
        with dissolve
        $ renpy.pause(1,hard=True)
        show bg mybedroom_night
        with dissolve
        stop music fadeout 2.0
        if day == 0:
            $ renpy.notify("Monday Night")
        elif day == 1:
            $ renpy.notify("Tuesday Night")
        elif day == 2:
            $ renpy.notify("Wednesday Night")
        elif day == 3:
            $ renpy.notify("Thursday Night")
        elif day == 4:
            $ renpy.notify("Friday Night")
        elif day == 5:
            $ renpy.notify("Saturday Night")
        elif day == 6:
            $ renpy.notify("Sunday Night")

        jump lbl_mybedroom_night_setup

##############################################################################
## Day Sleep EVENTS
label lbl_mybedroom_day_sleep:
    call lbl_mybedroom_sleep_variable_changes

##############################################################################

## Sleep Graphic
    play sound "audio/sfx/bedsheets.mp3"
    scene bg mybedroom_day_sleep
    with dissolve
    $ renpy.pause(1,hard=True)
    if gtime == 0:
        $ renpy.pause(1,hard=True)
    show bg mybedroom_night_sleep
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg mybedroom_day_sleep
    with dissolve
    show bg mybedroom_day
    with dissolve

## Day Sleep NO EVENTS
label lbl_mybedroom_day_sleep_1:
    $ gtime = 0
    $ newspaper = 0
    call lbl_misc_restart
    call lbl_skill_items
    call lbl_next_date
    play music "audio/music/a_family_home.ogg"
    if day <= 5:
        $ day += 1
        if day == 1:
            $ renpy.notify("Tuesday Morning")
        elif day == 2:
            $ renpy.notify("Wednesday Morning")
        elif day == 3:
            $ renpy.notify("Thursday Morning")
        elif day == 4:
            $ renpy.notify("Friday Morning")
        elif day == 5:
            $ renpy.notify("Saturday Morning")
        elif day == 6:
            $ renpy.notify("Sunday Morning")

        jump lbl_mybedroom_day_setup
    elif day == 6:
        $ day = 0
        if day == 0:
            $ renpy.notify("Monday Morning")

        jump lbl_mybedroom_day_setup
