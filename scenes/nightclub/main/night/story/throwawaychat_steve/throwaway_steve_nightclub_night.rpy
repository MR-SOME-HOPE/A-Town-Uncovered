## Throwaway Steve Nightclub Night Conversation ##
label lbl_nightclub_night_steve:

## Side Story Conversation
    #if steve_path <= 1:
    #    jump lbl_see_some_id
    #else:
    if principallashley_path == 10:
        jump lbl_drinking_advice
    jump lbl_nightclub_night_steve_convo

label lbl_nightclub_night_steve_convo:
## 1 - 5 is Evening exclusive
## 6 - 10 is Late Night exclusive
## 11 - 15 is interchangeable
    if gtime == 2:
        if date == 2 or date == 20 or date == 21 or date == 31:
            jump lbl_nightclub_night_steve_1
        elif date == 4 or date == 18 or date == 27:
            jump lbl_nightclub_night_steve_2
        elif date == 6 or date == 15 or date == 22:
            jump lbl_nightclub_night_steve_3
        elif date == 8 or date == 13 or date == 25:
            jump lbl_nightclub_night_steve_4
        elif date == 10 or date == 14 or date == 30:
            jump lbl_nightclub_night_steve_5
        elif date == 9 or date == 12 or date == 29:
            jump lbl_nightclub_night_steve_11
        elif date == 7 or date == 11 or date == 24:
            jump lbl_nightclub_night_steve_12
        elif date == 5 or date == 16 or date == 23:
            jump lbl_nightclub_night_steve_13
        elif date == 3 or date == 17 or date == 28:
            jump lbl_nightclub_night_steve_14
        elif date == 1 or date == 19 or date == 26:
            jump lbl_nightclub_night_steve_15
    elif gtime == 3:
        if date == 1 or date == 16 or date == 27 or date == 31:
            jump lbl_nightclub_night_steve_6
        elif date == 10 or date == 19 or date == 28:
            jump lbl_nightclub_night_steve_7
        elif date == 9 or date == 18 or date == 26:
            jump lbl_nightclub_night_steve_8
        elif date == 2 or date == 17 or date == 24:
            jump lbl_nightclub_night_steve_9
        elif date == 5 or date == 11 or date == 25:
            jump lbl_nightclub_night_steve_10
        elif date == 4 or date == 14 or date == 23:
            jump lbl_nightclub_night_steve_11
        elif date == 3 or date == 13 or date == 30:
            jump lbl_nightclub_night_steve_12
        elif date == 6 or date == 12 or date == 21:
            jump lbl_nightclub_night_steve_13
        elif date == 8 or date == 20 or date == 22:
            jump lbl_nightclub_night_steve_14
        elif date == 7 or date == 15 or date == 29:
            jump lbl_nightclub_night_steve_15

## Unhash the '$ steve_path = 2' in 'underageddrinking' when these are ready

## Evening Exclusive
label lbl_nightclub_night_steve_1:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_2:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_3:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_4:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_5:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

## Late Night Exclusive
label lbl_nightclub_night_steve_6:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_7:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_8:

    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_9:

    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_10:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

## Interchangable
label lbl_nightclub_night_steve_11:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_12:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_13:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_14:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night

label lbl_nightclub_night_steve_15:
    show pov neutral at left
    with dissolve
    show ste neutral_talk at right
    call lbl_nightclub_counter_check
    with dissolve
    ste "No no no! No service!"

    jump lbl_nightclub_night
