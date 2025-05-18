## Throwaway Jack Street Day Conversation ##
label lbl_street_day_jack:

    ## Main Story
    ## Answers Around Town Sexworld
    if main_story <= 40 and insexworld == 1:
        show btn street_day_jack_idle
        $ renpy.pause(0.001)

        jump lbl_street_day_jack_sexworld
    ## NO EVENT
    else:
        show btn street_day_jack_idle
        menu:
            "Talk":
                hide btn street_day_jack_idle
                jump lbl_street_day_jack_convo
            "Nevermind.":
                jump lbl_street_day

label lbl_street_day_jack_convo:
## 1 - 3 is afternoon exclusive
## 4 - 6 is night exclusive
## 7 - 10 is interchangeable
    if date == 3 or date == 16 or date == 24 or date == 0 or date == 10:
        jump lbl_street_day_jack_1
    elif date == 5 or date == 11 or date == 21 or date == 15 or date == 23:
        jump lbl_street_day_jack_2
    elif date == 6 or date == 17 or date == 25 or date == 4 or date == 12:
        jump lbl_street_day_jack_3
    elif date == 7 or date == 14 or date == 26 or date == 30:
        jump lbl_street_day_jack_7
    elif date == 8 or date == 13 or date == 22 or date == 29:
        jump lbl_street_day_jack_8
    elif date == 9 or date == 18 or date == 28 or date == 1:
        jump lbl_street_day_jack_9
    elif date == 2 or date == 20 or date == 27 or date == 19:
        jump lbl_street_day_jack_10

## Afternoon Exclusive
label lbl_street_day_jack_1: ##
    show pov bored at left
    with dissolve
    show jack angry_talk at right
    with dissolve
    jack "Fuck off, can't you see I'm busy."

    jump lbl_street_day

label lbl_street_day_jack_2: ##
    show pov bored at left
    with dissolve
    show jack angry_talk at right
    with dissolve
    jack "Fuck off, can't you see I'm busy."

    jump lbl_street_day

label lbl_street_day_jack_3: ##
    show pov bored at left
    with dissolve
    show jack angry_talk at right
    with dissolve
    jack "Fuck off, can't you see I'm busy."

    jump lbl_street_day

## Interchageable
label lbl_street_day_jack_7: ##
    show pov bored at left
    with dissolve
    show jack angry_talk at right
    with dissolve
    jack "Fuck off, can't you see I'm busy."

    jump lbl_town_daynight_jack_end

label lbl_street_day_jack_8: ##
    show pov bored at left
    with dissolve
    show jack angry_talk at right
    with dissolve
    jack "Fuck off, can't you see I'm busy."

    jump lbl_town_daynight_jack_end

label lbl_street_day_jack_9: ##
    show pov bored at left
    with dissolve
    show jack angry_talk at right
    with dissolve
    jack "Fuck off, can't you see I'm busy."

    jump lbl_town_daynight_jack_end

label lbl_street_day_jack_10: ##
    show pov bored at left
    with dissolve
    show jack angry_talk at right
    with dissolve
    jack "Fuck off, can't you see I'm busy."

    jump lbl_town_daynight_jack_end

label lbl_town_daynight_jack_end:
    if gtime <= 1:
        jump lbl_street_day
    else:
        jump lbl_schoolgym_night
