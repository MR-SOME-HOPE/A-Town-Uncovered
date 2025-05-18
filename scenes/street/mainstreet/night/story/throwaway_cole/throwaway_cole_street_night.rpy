## Throwaway Cole School Street Night Conversation ##
label lbl_street_night_cole:
    ## Background
    if insexworld == 0:
        scene bg street_night
    elif insexworld == 1:
        pass
        # scene bg street_nightsexworld
    show btn_street_night_cole_idle2
    $ renpy.pause(0.001)

    ## NO EVENT
    jump lbl_street_night_cole_convo

label lbl_street_night_cole_convo:
## 1 - 5 is morning exclusive (School Cafeteria)
## 6 - 10 is night exclusive (Street Night)
## 11 - 15 is interchangeable
    if date == 4 or date == 11 or date == 29:
        jump lbl_street_night_cole_6
    elif date == 1 or date == 14 or date == 27:
        jump lbl_street_night_cole_7
    elif date == 2 or date == 12 or date == 22:
        jump lbl_street_night_cole_8
    elif date == 3 or date == 13 or date == 24:
        jump lbl_street_night_cole_9
    elif date == 8 or date == 15 or date == 25:
        jump lbl_street_night_cole_10
    elif date == 5 or date == 18 or date == 23:
        jump lbl_town_day_cole_11
    elif date == 6 or date == 16 or date == 21:
        jump lbl_town_day_cole_12
    elif date == 7 or date == 17 or date == 30:
        jump lbl_town_day_cole_13
    elif date == 9 or date == 20 or date == 26:
        jump lbl_town_day_cole_14
    elif date == 10 or date == 19 or date == 28 or date == 0:
        jump lbl_town_day_cole_15

## Night Exclusive
label lbl_street_night_cole_6: ##
    show pov smirk_talk at left
    with dissolve
    hide btn_street_night_cole_idle2
    show col neutral at right
    with dissolve
    pov "Evening, Cole. What brings you here."
    show pov smirk at left
    show col neutral_talk at right
    col "Just here for a good time, [povname]."
    col "Guessing, you're here for the same reason."
    show pov smirk_talk at left
    show col smirk at right
    pov "Yup, I like having a good time."
    show pov neutral at left
    show col smirk_talk at right
    col "Good for you, my man."
    col "Welp- I'll just continue to have fun here."
    show pov smirk_talk at left
    show col neutral at right
    pov "Cool- yeah. Good talk."

    jump lbl_street_night

label lbl_street_night_cole_7: ##
    show pov neutral at left
    with dissolve
    hide btn_street_night_cole_idle2
    show col neutral_talk at right
    with dissolve
    col "Evening, big dude."
    show pov neutral_talk at left
    show col smirk at right
    pov "What's up, dude."
    show pov confused at left
    show col smirk_talk at right
    col "Have you seen a girl with massive tits, ash-brown hair, wearing an ocean blue dress?"
    show pov confused_talk at left
    show col smirk at right
    pov "Around this area, possibly, but can't say for certain."
    show pov shocked at left
    show col neutral_talk at right
    col "I have a date."
    show pov neutral_talk at left
    show col smirk at right
    pov "Oh cool! I hope she shows."
    show pov smirk at left
    show col embarrassed_talk at right
    col "I've been telling myself that for the past hour."

    jump lbl_street_night

label lbl_street_night_cole_8: ##
    show pov confused_talk at left
    with dissolve
    hide btn_street_night_cole_idle2
    show col bored at right
    with dissolve
    pov "It's cold tonight, don't you think?"
    show pov confused at left
    show col bored_talk at right
    col "Sorry, dude. Not time for small talk."
    col "I gotta meet up with a certain someone."
    show pov confused_talk at left
    show col smirk at right
    pov "A date?"
    show pov smirk at left
    show col bored_talk at right
    col "With success that is. Assuming they'll show up with the money."
    col "This will be my big break."
    show pov smirk_talk at left
    show col smirk at right
    pov "What you got for sale?"
    show pov smirk at left
    show col smirk_talk at right
    col "A chicken nugget that looks like Daniel DeVitol."

    jump lbl_street_night

label lbl_street_night_cole_9: ##
    show pov confused at left
    with dissolve
    hide btn_street_night_cole_idle2
    show col shocked_talk at right
    with dissolve
    col "Dude, keep an eye out. I heard there's secret police here tonight."
    show pov confused_talk at left
    show col bored at right
    pov "As long as I'm not doing anything wrong."
    show pov confused at left
    show col smirk_talk at right
    col "Right right right right right."
    show pov smirk_talk at left
    show col shocked at right
    pov "And as long as you're not doing anything wrong."
    show pov smirk at left
    show col shocked_talk at right
    col "[povname]. Look at me."
    show col smirk_talk at right
    col "I'm already fucked."
    show pov smirk_talk at left
    show col smirk at right
    pov "Touche."

    jump lbl_street_night

label lbl_street_night_cole_10: ##
    show pov confused_talk at left
    with dissolve
    hide btn_street_night_cole_idle2
    show col shocked at right
    with dissolve
    pov "What's that smell?"
    show pov confused at left
    show col angry_talk at right
    col "Probably vomit. You get used to it."
    show pov angry_talk at left
    show col angry at right
    pov "I can never get used to it."
    show pov confused at left
    show col bored_talk at right
    col "That's what I told myself, and one day-"
    show col smirk_talk at right
    col "I'm ascended into a whole new dimension."
    show pov shocked_talk at left
    show col smirk at right
    pov "What the fuck, man?"
    show pov angry_talk at left
    pov "I'm outta here, this place {i}really{/i} stinks. Like way more than normal."

    jump lbl_street_night
