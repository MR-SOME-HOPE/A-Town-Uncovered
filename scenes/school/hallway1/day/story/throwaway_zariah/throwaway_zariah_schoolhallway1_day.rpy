## Throwaway Zariah School Hallway 1 Day Conversation ##
label lbl_schoolhallway1_day_zariah:

    ## Main Story
    ## Answers Around Town Sexworld
    if main_story <= 35 and insexworld == 1:
        show btn schoolhallway1_day_zariah_idle
        $ renpy.pause(0.001)
        jump lbl_schoolhallway1_day_zariah_sexworld
    ## NO EVENT
    else:
        show btn schoolhallway1_day_zariah_idle
        $ renpy.pause(0.001)
        menu:
            "Talk":
                hide btn schoolhallway1_day_zariah_idle
                jump lbl_schoolhallway1_day_zariah_convo
            "Nevermind":
                jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_zariah_convo:
## 1 - 5 is afternoon exclusive
## 6 - 10 is night exclusive
## 11 - 15 is interchangeable
    if date == 1 or date == 19 or date == 30:
        jump lbl_schoolhallway1_day_zariah_1
    elif date == 2 or date == 20 or date == 21:
        jump lbl_schoolhallway1_day_zariah_2
    elif date == 3 or date == 18 or date == 22:
        jump lbl_schoolhallway1_day_zariah_3
    elif date == 9 or date == 17 or date == 25:
        jump lbl_schoolhallway1_day_zariah_4
    elif date == 10 or date == 11 or date == 26:
        jump lbl_schoolhallway1_day_zariah_5
    elif date == 4 or date == 12 or date == 27:
        jump lbl_town_both_zariah_11
    elif date == 5 or date == 13 or date == 24:
        jump lbl_town_both_zariah_12
    elif date == 6 or date == 14 or date == 28:
        jump lbl_town_both_zariah_13
    elif date == 8 or date == 15 or date == 29:
        jump lbl_town_both_zariah_14
    elif date == 7 or date == 16 or date == 23 or date == 0:
        jump lbl_town_both_zariah_15

## Afternoon Exclusive
label lbl_schoolhallway1_day_zariah_1:
    show pov shocked at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar angry_talk at right
    with dissolve
    zar "Hey, [povname]!"
    zar "Have you seen that little shit stain, Edward?!"
    show pov embarrassed_talk at left
    show zar angry at right
    pov "Woah what happened? No, I haven't seen him."
    show pov shocked at left
    show zar angry_talk at right
    zar "I had the little fucker work on my rig and now one of my speakers doesn't work!"
    show pov sad_talk at left
    show zar angry at right
    pov "That sounds like an expensive problem."
    show pov embarrassed at left
    show zar angry_talk at right
    zar "I swear to God, I'm going to tear off his head when I find him!"

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_zariah_2:
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls, the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_zariah_3:
    show pov neutral at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar neutral_talk at right
    with dissolve
    zar "Yo, [povname]."
    show pov confused at left
    show zar embarrassed_talk at right
    zar "Do you have any of those white earbuds I can borrow?"
    show pov confused_talk at left
    show zar confused at right
    pov "Why not just use your headphones?"
    show pov neutral at left
    show zar bored_talk at right
    zar "Lashley warn me that if another teacher complains about me wearing my headphones in class she is going to ban them."
    show pov embarrassed at left
    show zar sad_talk at right
    zar "I need my doof doofs, man!"
    show pov embarrassed_talk at left
    show zar sad at right
    pov "Sorry, Z. Don't have any on me right now."

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_zariah_4: ##
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls - the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_zariah_5: ##
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls, the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_schoolhallway1_day

## Interchangeable
label lbl_town_both_zariah_11: ##
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls, the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_town_both_zariah_end

label lbl_town_both_zariah_12: ##
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls, the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_town_both_zariah_end

label lbl_town_both_zariah_13: ##
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls, the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_town_both_zariah_end

label lbl_town_both_zariah_14: ##
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls, the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_town_both_zariah_end

label lbl_town_both_zariah_15: ##
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_zariah_idle
    show zar bored at right
    with dissolve
    pov "Hey, Z. How's your afternoon?"
    show pov neutral at left
    zar "..."
    show pov embarrassed_talk at left
    pov "Z? Zariah?"
    show pov embarrassed at left
    zar "..."
    show pov confused_talk at left
    pov "Karma?"
    show pov shocked at left
    show zar angry_talk at right
    zar "Hey! Karma is for the night owls, the name's Zariah!"
    show pov smirk at left
    show zar embarrassed_talk at right
    zar "Oh... sorry, [povname]. I'm just exhausted from last night's rave. It was..."
    show pov embarrassed at left
    show zar bored_talk at right
    zar "Fuckin'... Ep..ic."

    jump lbl_town_both_zariah_end

label lbl_town_both_zariah_end:
    if gtime == 1:
        jump lbl_schoolhallway1_day
    else:
        jump lbl_nightclub_night
