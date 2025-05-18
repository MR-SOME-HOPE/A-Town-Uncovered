## Throwaway Jaiden Schoolyard Day Conversation ##
label lbl_schoolgym_day_jaiden:

    ## Main Story
    ## Sexworld Jaiden
    if main_story <= 40 and insexworld == 1:
        jump lbl_schoolgym_day_jaiden_sexworld
    ## Investigations Jaiden
    elif main_story == 84:
        jump lbl_investigations_jaiden
    ## NO EVENT
    else:
        jump lbl_schoolgym_day_jaiden_convo

label lbl_schoolgym_day_jaiden_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    show btn schoolgym_day_jaiden_idle
    $ renpy.pause(0.001)

    if date == 1 or date == 11 or date == 23:
        jump lbl_schoolgym_day_jaiden_1
    elif date == 2 or date == 12 or date == 21:
        jump lbl_schoolgym_day_jaiden_2
    elif date == 3 or date == 19 or date == 22:
        jump lbl_schoolgym_day_jaiden_3
    elif date == 4 or date == 18 or date == 25:
        jump lbl_schoolgym_day_jaiden_4
    elif date == 5 or date == 20 or date == 28:
        jump lbl_schoolgym_day_jaiden_5
    elif date == 9 or date == 17 or date == 29:
        jump lbl_town_both_jaiden_11
    elif date == 6 or date == 16 or date == 30:
        jump lbl_town_both_jaiden_12
    elif date == 7 or date == 15 or date == 27:
        jump lbl_town_both_jaiden_13
    elif date == 10 or date == 14 or date == 24:
        jump lbl_town_both_jaiden_14
    elif date == 8 or date == 13 or date == 26 or date == 31:
        jump lbl_town_both_jaiden_15

## Morning Exclusive
label lbl_schoolgym_day_jaiden_1:
    show pov smirk_talk at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
    show jai neutral at right
    with dissolve
    pov "Morning, Jaiden. What's cracking."
    show pov neutral at left
    show jai neutral_talk at right
    jai "Morning, [povname]. I was about to start my morning routine actually! Care to join me, maggot?"
    show pov bored_talk at left
    show jai smirk at right
    pov "Please don't call me maggot in such an endearing manner... What's your routine like?"
    show pov confused at left
    show jai neutral_talk at right
    jai "Oh, nothing too complicated."
    show pov shocked at left
    show jai neutral_talk at right
    jai "We start warming up with 100 push ups, followed by 100 sit ups and 100 squats and we cool off with a 10 mile run."
    show pov shocked_talk at left
    show jai confused at right
    pov "And you do this every morning?"
    show pov shocked at left
    show jai smirk_talk at right
    jai "Never missed a single day. Had to do it all in crutches one summer."

    jump lbl_schoolgym_day

label lbl_schoolgym_day_jaiden_2: ##
    show pov smirk_talk at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
    show jai neutral at right
    with dissolve
    pov "Morning, Jaiden. What's cracking."
    show pov neutral at left
    show jai neutral_talk at right
    jai "Morning, [povname]. I was about to start my morning routine actually! Care to join me, maggot?"
    show pov bored_talk at left
    show jai smirk at right
    pov "Please don't call me maggot in such an endearing manner... What's your routine like?"
    show pov confused at left
    show jai neutral_talk at right
    jai "Oh, nothing too complicated."
    show pov shocked at left
    show jai neutral_talk at right
    jai "We start warming up with 100 push ups, followed by 100 sit ups and 100 squats and we cool off with a 10 mile run."
    show pov shocked_talk at left
    show jai confused at right
    pov "And you do this every morning?"
    show pov shocked at left
    show jai smirk_talk at right
    jai "Never missed a single day. Had to do it all in crutches one summer."

    jump lbl_schoolgym_day

label lbl_schoolgym_day_jaiden_3: ##
    show pov smirk_talk at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
    show jai neutral at right
    with dissolve
    pov "Morning, Jaiden. What's cracking."
    show pov neutral at left
    show jai neutral_talk at right
    jai "Morning, [povname]. I was about to start my morning routine actually! Care to join me, maggot?"
    show pov bored_talk at left
    show jai smirk at right
    pov "Please don't call me maggot in such an endearing manner... What's your routine like?"
    show pov confused at left
    show jai neutral_talk at right
    jai "Oh, nothing too complicated."
    show pov shocked at left
    show jai neutral_talk at right
    jai "We start warming up with 100 push ups, followed by 100 sit ups and 100 squats and we cool off with a 10 mile run."
    show pov shocked_talk at left
    show jai confused at right
    pov "And you do this every morning?"
    show pov shocked at left
    show jai smirk_talk at right
    jai "Never missed a single day. Had to do it all in crutches one summer."

    jump lbl_schoolgym_day

label lbl_schoolgym_day_jaiden_4: ##
    show pov smirk_talk at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
    show jai neutral at right
    with dissolve
    pov "Morning, Jaiden. What's cracking."
    show pov neutral at left
    show jai neutral_talk at right
    jai "Morning, [povname]. I was about to start my morning routine actually! Care to join me, maggot?"
    show pov bored_talk at left
    show jai smirk at right
    pov "Please don't call me maggot in such an endearing manner... What's your routine like?"
    show pov confused at left
    show jai neutral_talk at right
    jai "Oh, nothing too complicated."
    show pov shocked at left
    show jai neutral_talk at right
    jai "We start warming up with 100 push ups, followed by 100 sit ups and 100 squats and we cool off with a 10 mile run."
    show pov shocked_talk at left
    show jai confused at right
    pov "And you do this every morning?"
    show pov shocked at left
    show jai smirk_talk at right
    jai "Never missed a single day. Had to do it all in crutches one summer."

    jump lbl_schoolgym_day

label lbl_schoolgym_day_jaiden_5: ##
    show pov smirk_talk at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
    show jai neutral at right
    with dissolve
    pov "Morning, Jaiden. What's cracking."
    show pov neutral at left
    show jai neutral_talk at right
    jai "Morning, [povname]. I was about to start my morning routine actually! Care to join me, maggot?"
    show pov bored_talk at left
    show jai smirk at right
    pov "Please don't call me maggot in such an endearing manner... What's your routine like?"
    show pov confused at left
    show jai neutral_talk at right
    jai "Oh, nothing too complicated."
    show pov shocked at left
    show jai neutral_talk at right
    jai "We start warming up with 100 push ups, followed by 100 sit ups and 100 squats and we cool off with a 10 mile run."
    show pov shocked_talk at left
    show jai confused at right
    pov "And you do this every morning?"
    show pov shocked at left
    show jai smirk_talk at right
    jai "Never missed a single day. Had to do it all in crutches one summer."

    jump lbl_schoolgym_day

## Interchangable
label lbl_town_both_jaiden_11: ##
    show pov bored at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
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

    jump lbl_town_both_jaiden_end

label lbl_town_both_jaiden_12: ##
    show pov bored at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
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

    jump lbl_town_both_jaiden_end

label lbl_town_both_jaiden_13: ##
    show pov bored at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
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

    jump lbl_town_both_jaiden_end

label lbl_town_both_jaiden_14: ##
    show pov bored at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
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

    jump lbl_town_both_jaiden_end

label lbl_town_both_jaiden_15: ##
    show pov bored at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
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

    jump lbl_town_both_jaiden_end

label lbl_town_both_jaiden_end:
    if gtime == 0:
        jump lbl_schoolgym_day
    else:
        jump lbl_schoolyard_day
