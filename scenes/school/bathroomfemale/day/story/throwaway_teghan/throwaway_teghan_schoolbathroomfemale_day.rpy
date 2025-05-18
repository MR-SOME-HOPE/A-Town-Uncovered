## Throwaway Teghan School Bathroom Female Day Conversation ##
label lbl_schoolbathroomfemale_day_teghan:

    ## Main Story
    if main_story <= 35 and insexworld == 1:
        jump lbl_schoolbathroomfemale_day_teghan_sexworld
    ## NO EVENT
    else:
        jump lbl_schoolbathroomfemale_day_teghan_convo

label lbl_schoolbathroomfemale_day_teghan_convo:
## 1 - 5 is morning exclusive (School Bathroom)
## 6 - 10 is afternoon and weekend exclusive (Mall)
## 11 - 15 is interchangeable
    if date == 8 or date == 14 or date == 21 or date == 0:
        jump lbl_schoolbathroomfemale_day_teghan_1
    elif date == 9 or date == 15 or date == 23:
        jump lbl_schoolbathroomfemale_day_teghan_2
    elif date == 10 or date == 17 or date == 25:
        jump lbl_schoolbathroomfemale_day_teghan_3
    elif date == 7 or date == 16 or date == 26:
        jump lbl_schoolbathroomfemale_day_teghan_4
    elif date == 6 or date == 18 or date == 27:
        jump lbl_schoolbathroomfemale_day_teghan_5
    elif date == 5 or date == 19 or date == 28:
        jump lbl_town_day_teghan_11
    elif date == 4 or date == 20 or date == 29:
        jump lbl_town_day_teghan_12
    elif date == 3 or date == 11 or date == 30:
        jump lbl_town_day_teghan_13
    elif date == 2 or date == 12 or date == 24:
        jump lbl_town_day_teghan_14
    elif date == 1 or date == 13 or date == 22:
        jump lbl_town_day_teghan_15

## Morning Exclusive
label lbl_schoolbathroomfemale_day_teghan_1:
    show pov neutral at left
    with dissolve
    hide btn_schoolbathroom_day_teghan_idle2
    show teg neutral_talk at right
    with dissolve
    teg "Ayeee! [povname]!"
    teg "Whaaaaadup!"
    show pov smirk_talk at left
    show teg neutral at right
    pov "Hey, Teghan. You're sure in a good mood."
    show pov smirk at left
    show teg smirk_talk at right
    teg "Maaan, what's not to feel good about?! You know what I'm sayin'?"
    teg "It's just like, everyday is a hype fest."
    show pov neutral_talk at left
    show teg smirk at right
    pov "I feel you, girl."

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_teghan_2:
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolbathroom_day_teghan_idle2
    show teg neutral at right
    with dissolve
    pov "Teghan, wassup!"
    show pov neutral at left
    show teg smirk_talk at right
    teg "Aye, [povname], ma bro-myster!"
    show pov confused at left
    show teg embarrassed_talk at right
    teg "W-what are you doing here?"
    show pov confused_talk at left
    show teg embarrassed at right
    pov "What are you talking about? It's school hours."
    show pov shocked at left
    show teg embarrassed_talk at right
    teg "I'm talking about here. In the girl's bathroom?"
    show pov embarrassed_talk at left
    show teg smirk at right
    pov "Oh! Uh- I just... wanted to see how you're doing."
    show pov embarrassed at left
    show teg embarrassed_talk at right
    teg "Dude, you're so fuckin' rad but we'll talk later, aight?"

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_teghan_3:
    show pov neutral at left
    with dissolve
    hide btn_schoolbathroom_day_teghan_idle2
    show teg neutral_talk at right
    with dissolve
    teg "G'morning, [povname]."
    teg "What brings you to this humble yet innapropriate locale."
    show pov neutral_talk at left
    show teg confused at right
    pov "Oh, y'know. Doing my runs."
    show pov neutral at left
    show teg embarrassed_talk at right
    teg "Respect. Respect."
    show pov shocked at left
    show teg confused_talk at right
    teg "Well, listen: The girls and I are talking about something-something."
    show pov neutral at left
    show teg embarrassed_talk at right
    teg "So if you wouldn't mind skidaddling your tight tushie outta here?"
    show pov neutral_talk at left
    show teg neutral at right
    pov "No worries. Catch you later, T."

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_teghan_4:
    show pov shocked_talk at left
    with dissolve
    hide btn_schoolbathroom_day_teghan_idle2
    show teg confused at right
    with dissolve
    pov "Did you see what was going on outside?"
    show pov shocked at left
    show teg confused_talk at right
    teg "You talking about the round house kick?"
    show pov confused_talk at left
    show teg smirk at right
    pov "Yeah, that seems to be happening often, huh?"
    show pov neutral at left
    show teg neutral_talk at right
    teg "It's his signature move."
    show pov embarrassed at left
    teg "It's the only kick he knows."
    show pov neutral_talk at left
    show teg smirk at right
    pov "It's the only kick you really need at the end of the day."
    show pov neutral at left
    show teg smirk_talk at right
    teg "I'd like to see a tornado kick actually, that'll be the day to rejoice."

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_teghan_5:
    show pov confused at left
    with dissolve
    hide btn_schoolbathroom_day_teghan_idle2
    show teg neutral_talk at right
    with dissolve
    teg "Good afternoon, [povname]."
    show pov confused_talk at left
    show teg confused at right
    pov "Afternoon? It's morning."
    show pov confused at left
    show teg confused_talk at right
    teg "Are you sure about that?"
    show pov confused_talk at left
    show teg confused at right
    pov "Pretty sure."
    show pov confused at left
    show teg confused_talk at right
    teg "Really?"
    show pov bored at left
    show teg smirk_talk at right
    teg "....You're bluffing."
    teg "I can see that smile on your face."

    jump lbl_schoolbathroomfemale_day

## Afternoon and Mall Exclusive
label lbl_town_day_teghan_11:
    show pov neutral at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_teghan_idle2
    else:
        hide btn_mall_day_teghan_idle2
    show teg smirk_talk at right
    with dissolve
    teg "What's new, [povname]."
    show pov neutral_talk at left
    show teg neutral at right
    pov "The usually, this and that, that and this."
    show pov neutral at left
    show teg neutral_talk at right
    teg "Sounds like you're living a pretty interesting life."
    show pov neutral_talk at left
    show teg embarrassed at right
    pov "Yeah, I'm reaching each end of the horizon."
    show pov neutral at left
    show teg embarrassed_talk at right
    teg "This, that, and everything in between."
    show teg smirk_talk at right
    teg "Out of this world."

    jump lbl_town_day_teghan_end

label lbl_town_day_teghan_12:
    show pov neutral at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_teghan_idle2
    else:
        hide btn_mall_day_teghan_idle2
    show teg shocked_talk at right
    with dissolve
    teg "Have you seen that new series on Webflicks?"
    show pov confused at left
    show teg sad_talk at right
    teg "Oh dip- what is it called again?"
    show pov embarrassed at left
    show teg confused_talk at right
    teg "Fuck- it's on the tip of my tongue."
    show teg embarrassed_talk at right
    teg "The- The- The Re- The Ba- The Shr-"
    show teg sad_talk at right
    teg "Anyway, it's fucking depressing."
    show teg smirk_talk at right
    teg "I highly not not recommend it."
    show pov embarrassed_talk at left
    show teg smirk at right
    pov "I'll see if I can find it... whatever it is."

    jump lbl_town_day_teghan_end

label lbl_town_day_teghan_13:
    show pov neutral at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_teghan_idle2
    else:
        hide btn_mall_day_teghan_idle2
    show teg shocked_talk at right
    with dissolve
    teg "Yo! Did you catch the game last night?"
    show pov confused_talk at left
    show teg embarrassed at right
    pov "I did not."
    show pov neutral at left
    show teg smirk_talk at right
    teg "Oh, damn. You missed out, it was a close one."
    show pov neutral_talk at left
    show teg neutral at right
    pov "Who were playing?"
    show pov confused at left
    show teg neutral_talk at right
    teg "Red vs Blue."
    show pov confused_talk at left
    show teg confused at right
    pov "...Like the MeTube series?"
    show pov embarrassed at left
    show teg embarrassed_talk at right
    teg "Like... the colours, they wore?"

    jump lbl_town_day_teghan_end

label lbl_town_day_teghan_14:
    show pov smirk_talk at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_teghan_idle2
    else:
        hide btn_mall_day_teghan_idle2
    show teg neutral at right
    with dissolve
    pov "Teghan, what's cracking with you?"
    show pov neutral at left
    show teg shocked_talk at right
    teg "Bro, I had some Mediterranean cuisine yesterday."
    show pov neutral at left
    show teg smirk_talk at right
    teg "Not gonna lie, fuckin' dope."
    show pov neutral_talk at left
    show teg smirk at right
    pov "It do be good."
    show pov neutral at left
    show teg sad_talk at right
    teg "I love the world."
    teg "And all of its' cuisines."
    show pov smirk at left
    show teg neutral_talk at right
    teg "They actually know how to create flavour."

    jump lbl_town_day_teghan_end

label lbl_town_day_teghan_15:
    show pov confused at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_teghan_idle2
    else:
        hide btn_mall_day_teghan_idle2
    show teg sad_talk at right
    with dissolve
    teg "Ughh, my shoulder aches like a mofo."
    show pov confused_talk at left
    show teg sad at right
    pov "What did you do this time?"
    show pov confused at left
    show teg shocked_talk at right
    teg "Nothing!"
    show pov embarrassed at left
    show teg confused_talk at right
    teg "Maybe I should see a chiropractor."
    show pov smirk_talk at left
    show teg confused at right
    pov "Get them cracks in ya'."
    show pov embarrassed at left
    show teg bored_talk at right
    teg "Crack is not cool, [povname]. Stay off the hard stuff."

    jump lbl_town_day_teghan_end

label lbl_town_day_teghan_end:
    if gtime == 0:
        jump lbl_schoolbathroomfemale_day
    else:
        jump lbl_mall_day
