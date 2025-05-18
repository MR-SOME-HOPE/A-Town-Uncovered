## Night Nap ##
label lbl_mybedroom_night_nap:
    $ gtime += 1

## Nap Night Graphic
    scene bg mybedroom_night_nap
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg mybedroom_night
    with dissolve
    if day == 0:
        $ renpy.notify("Late Monday Night")
    elif day == 1:
        $ renpy.notify("Late Tuesday Night")
    elif day == 2:
        $ renpy.notify("Late Wednesday Night")
    elif day == 3:
        $ renpy.notify("Late Thursday Night")
    elif day == 4:
        $ renpy.notify("Late Friday Night")
    elif day == 5:
        $ renpy.notify("Late Saturday Night")
    elif day == 6:
        $ renpy.notify("Late Sunday Night")

    jump lbl_mybedroom_night_setup

## Night Sleep
label lbl_mybedroom_night_sleep:
    call lbl_mybedroom_sleep_variable_changes

##############################################################################

## Sleep Night Graphic
    play sound "audio/sfx/bedsheets.mp3"
    scene bg mybedroom_night_sleep
    with dissolve
    $ renpy.pause(1,hard=True)
    if gtime == 2:
        $ renpy.pause(1,hard=True)
    show bg mybedroom_day_sleep
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg mybedroom_day
    with dissolve

label lbl_mybedroom_night_sleep_1:
    $ gtime = 0
    $ newspaper = 0
    call lbl_misc_restart
    call lbl_skill_items
    call lbl_next_date
    # ##TEMP TEST
    # if not inventory.has_item(Items.flowerlilies):
    #     $ inventory.add(Items.flowerlilies)
    # if not inventory.has_item(Items.flowerroses):
    #     $ inventory.add(Items.flowerroses)
    # if not inventory.has_item(Items.flowersunflowers):
    #     $ inventory.add(Items.flowersunflowers)

    play music "audio/music/a_family_home.ogg"
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    ##$ day += 1 % 6#
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

    #elif day == 6:
        #$ day = 0
    elif day == 0:
        $ renpy.notify("Monday Morning")



    if main_story == 28:
        $ renpy.pause(3,hard=True)
        $ renpy.notify("New Objective: Go to the Kitchen")
        $ renpy.pause(3,hard=True)
    elif main_story == 80:
        jump lbl_waking_up_alone


    jump lbl_mybedroom_day_setup
