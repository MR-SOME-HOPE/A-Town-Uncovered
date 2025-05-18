## See Some ID ##
label lbl_see_some_id:
    show pov neutral_talk at left
    with dissolve
    show ste neutral at right
    call lbl_nightclub_counter_check
    with dissolve

    pov "Hey, buddy!"
    if steve_path == 0:
        show pov smirk at left
        show ste neutral_talk at right
        idk "Hey, how is it going?"
        show pov embarrassed at left
        show ste smirk_talk at right
        idk "You look kind of young, can I see some ID?"
        show pov smirk_talk at left
        show ste neutral at right
        pov "I just have young-looking... genetics."
        show pov embarrassed at left
        show ste smirk_talk at right
        idk "I believe you, t'ough I still need to make sure you're over 21."
        show ste smirk at right
        pov "..."
        show ste confused at right
        idk "..."
        show pov embarrassed_talk at left
        show ste bored at right
        pov "Y'know what? I'm not all that thirsty."
        show pov embarrassed at left
        show ste smirk_talk at right
        idk "I have my eye on you."
        $ steve_path = 1
    elif sister_path >= 20:#underagedrinking
        jump lbl_nightclub_night_steve
    elif principallashley_path == 10:
        jump lbl_drinking_advice
    else:
        show pov bored at left
        show ste smirk_talk at right
        ste "Do not t'ink you're so clever. I remember your face."
        show ste confused_talk at right
        ste "No proop', no service."
        show pov bored_talk at left
        show ste smirk at right
        pov "Fine.."

    jump lbl_nightclub_night_setup
