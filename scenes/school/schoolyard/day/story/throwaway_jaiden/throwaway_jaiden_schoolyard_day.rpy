## Throwaway Jaiden Schoolyard Day Conversation ##
label lbl_schoolyard_day_jaiden:

    ## Main Story
    ## Sexworld Jaiden
    if main_story <= 40 and insexworld == 1:
        jump lbl_schoolgym_day_jaiden_sexworld
    ## Investigations Jaiden
    elif main_story == 84:
        jump lbl_investigations_jaiden
    ## NO EVENT
    else:
        jump lbl_schoolyard_day_jaiden_convo

label lbl_schoolyard_day_jaiden_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if date == 1 or date == 17 or date == 23:
        jump lbl_schoolyard_day_jaiden_6
    elif date == 4 or date == 18 or date == 30:
        jump lbl_schoolyard_day_jaiden_7
    elif date == 9 or date == 16 or date == 25:
        jump lbl_schoolyard_day_jaiden_8
    elif date == 2 or date == 15 or date == 26:
        jump lbl_schoolyard_day_jaiden_9
    elif date == 7 or date == 20 or date == 28:
        jump lbl_schoolyard_day_jaiden_10
    elif date == 6 or date == 14 or date == 29:
        jump lbl_town_both_jaiden_11
    elif date == 3 or date == 13 or date == 24:
        jump lbl_town_both_jaiden_12
    elif date == 8 or date == 12 or date == 27:
        jump lbl_town_both_jaiden_13
    elif date == 5 or date == 11 or date == 22:
        jump lbl_town_both_jaiden_14
    elif date == 10 or date == 19 or date == 21 or date == 31:
        jump lbl_town_both_jaiden_15

## Afternoon Exclusive
label lbl_schoolyard_day_jaiden_6: ##
    show pov bored at left
    with dissolve
    show jai angry_talk at right
    with dissolve
    jai "Hey, maggot!"
    show pov bored_talk at left
    show jai angry at right
    pov "Yes, it's me, the maggot. What's up?"
    show pov shocked at left
    show jai angry_talk at right
    jai "Were you the dumb son-of-a-bitch with a death wish who took my dumbbells?!"
    show pov shocked_talk at left
    show jai confused at right
    pov "What?! No! Look at me, I don't lift... much."
    show pov confused_talk at left
    show jai bored at right
    pov "W-wait, you bring your dumbbells to uni? How heavy were they anyway?"
    show pov shocked at left
    show jai bored_talk at right
    jai "A set of two 60lbs dumbbells. Chump change as my dad calls them."
    show pov embarrassed_talk at left
    show jai angry at right
    pov "Were you using them to work out or cave n the skulls of your enemies?!"
    show pov shocked at left
    show jai angry_talk at right
    jai "Both!"

    jump lbl_schoolyard_day

label lbl_schoolyard_day_jaiden_7:
    show pov bored at left
    with dissolve
    show jai angry_talk at right
    with dissolve
    jai "Hey, maggot!"
    show pov bored_talk at left
    show jai angry at right
    pov "Yes, it's me, the maggot. What's up?"
    show pov shocked at left
    show jai angry_talk at right
    jai "Were you the dumb son-of-a-bitch with a death wish who took my dumbbells?!"
    show pov shocked_talk at left
    show jai confused at right
    pov "What?! No! Look at me, I don't lift... much."
    show pov confused_talk at left
    show jai bored at right
    pov "W-wait, you bring your dumbbells to uni? How heavy were they anyway?"
    show pov shocked at left
    show jai bored_talk at right
    jai "A set of two 60lbs dumbbells. Chump change as my dad calls them."
    show pov embarrassed_talk at left
    show jai angry at right
    pov "Were you using them to work out or cave in the skulls of your enemies?!"
    show pov shocked at left
    show jai angry_talk at right
    jai "Both!"

    jump lbl_schoolyard_day

label lbl_schoolyard_day_jaiden_8:
    show pov confused at left
    with dissolve
    show jai neutral_talk at right
    with dissolve
    jai "Hey, maggot, I'm hitting the park later for a run, you want to come?"
    show pov confused_talk at left
    show jai neutral at right
    pov "Why are you asking me?"
    show pov shocked at left
    show jai smirk_talk at right
    jai "Seen you run there from time to time, I could use a good spotter for some of my drills."
    show pov embarrassed_talk at left
    show jai smirk at right
    pov "I kinda feel pretty honored that you think I'd make for a good work out partner."
    show pov shocked at left
    show jai smirk_talk at right
    jai "I've gotten into hand to hand combat, need a buddy to practice some headlocks and a few strikes."
    show pov shocked_talk at left
    show jai bored at right
    pov "Oh! Uh-- r-rrriiiing- oh- what? Was that the bell or possibly a phone call?! Better run or answer it depending-!"

    jump lbl_schoolyard_day

label lbl_schoolyard_day_jaiden_9: ##
    show pov bored at left
    with dissolve
    show jai angry_talk at right
    with dissolve
    jai "Hey, maggot!"
    show pov bored_talk at left
    show jai angry at right
    pov "Yes, it's me, the maggot. What's up?"
    show pov shocked at left
    show jai angry_talk at right
    jai "Were you the dumb son-of-a-bitch with a death wish who took my dumbbells?!"
    show pov shocked_talk at left
    show jai confused at right
    pov "What?! No! Look at me, I don't lift... much."
    show pov confused_talk at left
    show jai bored at right
    pov "W-wait, you bring your dumbbells to uni? How heavy were they anyway?"
    show pov shocked at left
    show jai bored_talk at right
    jai "A set of two 60lbs dumbbells. Chump change as my dad calls them."
    show pov embarrassed_talk at left
    show jai angry at right
    pov "Were you using them to work out or cave n the skulls of your enemies?!"
    show pov shocked at left
    show jai angry_talk at right
    jai "Both!"

    jump lbl_schoolyard_day

label lbl_schoolyard_day_jaiden_10: ##
    show pov bored at left
    with dissolve
    show jai angry_talk at right
    with dissolve
    jai "Hey, maggot!"
    show pov bored_talk at left
    show jai angry at right
    pov "Yes, it's me, the maggot. What's up?"
    show pov shocked at left
    show jai angry_talk at right
    jai "Were you the dumb son-of-a-bitch with a death wish who took my dumbbells?!"
    show pov shocked_talk at left
    show jai confused at right
    pov "What?! No! Look at me, I don't lift... much."
    show pov confused_talk at left
    show jai bored at right
    pov "W-wait, you bring your dumbbells to uni? How heavy were they anyway?"
    show pov shocked at left
    show jai bored_talk at right
    jai "A set of two 60lbs dumbbells. Chump change as my dad calls them."
    show pov embarrassed_talk at left
    show jai angry at right
    pov "Were you using them to work out or cave n the skulls of your enemies?!"
    show pov shocked at left
    show jai angry_talk at right
    jai "Both!"

    jump lbl_schoolyard_day
