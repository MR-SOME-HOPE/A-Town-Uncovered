## The First Night ##
label lbl_the_first_night:

    scene bg intro_cutscene_12
    with fade
    $ renpy.pause ()
    $ main_story = 2
    $ hud_enabled = 0
    $ gtime = 0
    $ day = 0

    scene bg mybedroom_day
    with fade
    $ renpy.notify("Monday Morning")
    $ renpy.pause(3,hard=True)
    $ renpy.notify("New Objective: Get ready for University")

    jump lbl_mybedroom_day_setup
