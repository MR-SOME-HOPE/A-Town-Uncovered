## Throwaway Phil School Bathroom Male Day Conversation ##
label lbl_schoolbathroommale_day_phil:
    show btn schoolbathroom_day_phil_idle
    $ renpy.pause(0.001)

    ## Main Story
    if main_story <= 40 and insexworld == 1:
        jump lbl_schoolbathroommale_day_phil_sexworld
    ## NO EVENT
    else:
        jump lbl_schoolbathroommale_day_phil_convo

label lbl_schoolbathroommale_day_phil_convo:
## 1 - 3 is afternoon exclusive (School Bathroom)
## 4 - 6 is night exclusive (School Gym)
## 7 - 10 is interchangeable
    if date == 1 or date == 19 or date == 30 or date == 23 or date == 28:
        jump lbl_schoolbathroommale_day_phil_1
    elif date == 2 or date == 20 or date == 21 or date == 31 or date == 14:
        jump lbl_schoolbathroommale_day_phil_2
    elif date == 3 or date == 18 or date == 22 or date == 16 or date == 6:
        jump lbl_schoolbathroommale_day_phil_3
    elif date == 9 or date == 17 or date == 25 or date == 7:
        jump lbl_town_both_phil_7
    elif date == 10 or date == 11 or date == 26 or date == 29:
        jump lbl_town_both_phil_8
    elif date == 4 or date == 12 or date == 27 or date == 15:
        jump lbl_town_both_phil_9
    elif date == 5 or date == 13 or date == 24 or date == 8:
        jump lbl_town_both_phil_10

## Afternoon Exclusive
label lbl_schoolbathroommale_day_phil_1: ##
    show pov confused_talk at left
    with dissolve
    show phi bored at right
    hide btn schoolbathroom_day_phil_idle
    with dissolve
    pov "Dude, what are you doing in here?"
    show pov bored at left
    show phi bored_talk at right
    phi "Aye, man. Piss off. Lemme chill in peace, ya?"

    jump lbl_schoolbathroommale_day

label lbl_schoolbathroommale_day_phil_2: ##
    show pov confused_talk at left
    with dissolve
    show phi bored at right
    hide btn schoolbathroom_day_phil_idle
    with dissolve
    pov "Dude, what are you doing in here?"
    show pov bored at left
    show phi bored_talk at right
    phi "Aye, man. Piss off. Lemme chill in peace, ya?"

    jump lbl_schoolbathroommale_day

label lbl_schoolbathroommale_day_phil_3: ##
    show pov confused_talk at left
    with dissolve
    show phi bored at right
    hide btn schoolbathroom_day_phil_idle
    with dissolve
    pov "Dude, what are you doing in here?"
    show pov bored at left
    show phi bored_talk at right
    phi "Aye, man. Piss off. Lemme chill in peace, ya?"

    jump lbl_schoolbathroommale_day

## Interchangeable
label lbl_town_both_phil_7: ##
    show pov confused_talk at left
    with dissolve
    show phi bored at right
    if gtime == 1:
        hide btn schoolbathroom_day_phil_idle
    with dissolve
    pov "Dude, what are you doing in here?"
    show pov bored at left
    show phi bored_talk at right
    phi "Aye, man. Piss off. Lemme chill in peace, ya?"

    jump lbl_town_both_phil_end

label lbl_town_both_phil_8: ##
    show pov confused_talk at left
    with dissolve
    show phi bored at right
    if gtime == 1:
        hide btn schoolbathroom_day_phil_idle
    with dissolve
    pov "Dude, what are you doing in here?"
    show pov bored at left
    show phi bored_talk at right
    phi "Aye, man. Piss off. Lemme chill in peace, ya?"

    jump lbl_town_both_phil_end

label lbl_town_both_phil_9: ##
    show pov confused_talk at left
    with dissolve
    show phi bored at right
    if gtime == 1:
        hide btn schoolbathroom_day_phil_idle
    with dissolve
    pov "Dude, what are you doing in here?"
    show pov bored at left
    show phi bored_talk at right
    phi "Aye, man. Piss off. Lemme chill in peace, ya?"

    jump lbl_town_both_phil_end

label lbl_town_both_phil_10: ##
    show pov confused_talk at left
    with dissolve
    show phi bored at right
    if gtime == 1:
        hide btn schoolbathroom_day_phil_idle
    with dissolve
    pov "Dude, what are you doing in here?"
    show pov bored at left
    show phi bored_talk at right
    phi "Aye, man. Piss off. Lemme chill in peace, ya?"

    jump lbl_town_both_phil_end

label lbl_town_both_phil_end:
    if gtime == 1:
        jump lbl_schoolbathroommale_day
    else:
        jump lbl_schoolgym_night
