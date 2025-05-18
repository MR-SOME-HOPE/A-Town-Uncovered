## Overslept in Basement ##
label lbl_overselpt_in_basement:

    scene bg mybasement_lightson
    with vpunch
    sis "SHIIT!"
    show pov shocked at left
    with dissolve
    show sis shocked_talk at right
    with dissolve
    sis "Shit! Shit! Shit!"
    show pov shocked_talk at left
    show sis shocked at right
    pov "WHAAT?!"
    pov "What's going on?"
    show pov shocked at left
    show sis shocked_talk at right
    sis "I overslept! I'm late for work!"
    show pov shocked at left
    show sis angry_talk at right
    sis "Jesus, man. Why didn't you wake me up?"
    show pov shocked_talk at left
    show sis sad at right
    pov "I don't know what the hell your schedule is."
    show pov embarrassed at left
    show sis sad_talk at right
    sis "Fuck, I'm outtie."
    show sis embarrassed_talk at right
    sis "Peace."
    $ sister_path = 12
    $ gtime = 0
    call lbl_next_date
    $ skill_int_times = 0
    $ skill_sta_times = 0
    $ skill_luc_times = 0
    $ hitomibeach_day = 0
    $ randomencounter = 0
    call lbl_skill_items
    play music "audio/music/a_family_home.ogg"
    $ townmap_enabled = 0
    if day == 2:
        $ day = 3
        $ renpy.notify("Thursday Morning")
    elif day == 6:
        $ day = 0
        $ renpy.notify("Monday Morning")

    jump lbl_mybasement_day_setup
