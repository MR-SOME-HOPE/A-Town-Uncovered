## Stop Snooping Clothed ##
label lbl_stop_snooping_clothed:

    scene bg beachmain_day
    show btn beachmain_day_chair_idle
    with hpunch
    if violette_path == 0:
        idk "Hey!"
        show pov shocked at left
        with dissolve
        show vio bored_talk at right
        hide btn beachmain_day_chair_idle
        with dissolve
        idk "No snooping around the beach with your clothes on."
        show pov embarrassed at left
        idk "You're acting weird, dude."
        idk "Get naked before you're free to roam around."
        show pov embarrassed_talk at left
        show vio neutral at right
        pov "Sorry about that."
    else:
        vio "Hey!"
        show pov shocked at left
        with dissolve
        show vio bored_talk at right
        hide btn beachmain_day_chair_idle
        with dissolve
        vio "No snooping around the beach with your clothes on."
        show pov embarrassed at left
        vio "You're acting weird, dude."
        vio "Get naked before you're free to roam around."
        show pov embarrassed_talk at left
        show vio neutral at right
        pov "Sorry about that."

    jump lbl_beachmain_day
