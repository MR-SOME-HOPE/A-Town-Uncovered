## Throwaway Meghan School Bathroom Female Day Conversation ##
label lbl_mall_day_meghan:

    ## Main Story
    if main_story <= 35 and insexworld == 1:
        jump lbl_mall_day_meghan_sexworld
    ## NO EVENT
    else:
        jump lbl_mall_day_meghan_convo

label lbl_mall_day_meghan_convo:
## 1 - 5 is morning exclusive (School Bathroom)
## 6 - 10 is afternoon and weekend exclusive (Mall)
## 11 - 15 is interchangeable
    if date == 1 or date == 20 or date == 22 or date == 0:
        jump lbl_mall_day_meghan_6
    elif date == 4 or date == 18 or date == 23:
        jump lbl_mall_day_meghan_7
    elif date == 5 or date == 17 or date == 21:
        jump lbl_mall_day_meghan_8
    elif date == 8 or date == 16 or date == 24:
        jump lbl_mall_day_meghan_9
    elif date == 9 or date == 11 or date == 25:
        jump lbl_mall_day_meghan_10
    elif date == 10 or date == 12 or date == 26:
        jump lbl_town_day_meghan_11
    elif date == 7 or date == 13 or date == 27:
        jump lbl_town_day_meghan_12
    elif date == 6 or date == 14 or date == 30:
        jump lbl_town_day_meghan_13
    elif date == 3 or date == 15 or date == 29:
        jump lbl_town_day_meghan_14
    elif date == 2 or date == 19 or date == 28:
        jump lbl_town_day_meghan_15

## Afternoon Exclusive
label lbl_mall_day_meghan_6:
    show pov confused at left
    with dissolve
    hide btn_mall_day_meghan_idle2
    show meg sad_talk at right
    with dissolve
    meg "Ughh, there's no cute guys here today."
    meg "Where'd they all go?"
    show pov smirk_talk at left
    show meg confused at right
    pov "I'm here."
    show pov embarrassed at left
    show meg bored_talk at right
    meg "Don't say that, that's embarrassing."
    show pov embarrassed_talk at left
    show meg bored
    pov "I-"
    pov "Yeah, it sorta just came out."
    show pov bored at left
    show meg bored_talk at right
    meg "You're still talking to me?"

    jump lbl_mall_day

label lbl_mall_day_meghan_7:
    show pov confused at left
    with dissolve
    hide btn_mall_day_meghan_idle2
    show meg confused_talk at right
    with dissolve
    meg "They're playing this song again?"
    meg "It's so annoying."
    show pov neutral_talk at left
    show meg confused at right
    pov "It's catchy."
    show pov neutral at left
    show meg bored_talk at right
    meg "It's annoying."
    show pov smirk_talk at left
    show meg bored at right
    pov "Potato potato."
    show pov embarrassed at left
    show meg bored_talk at right
    meg "It's annoying."

    jump lbl_mall_day

label lbl_mall_day_meghan_8:
    show pov neutral_talk at left
    with dissolve
    hide btn_mall_day_meghan_idle2
    show meg confused at right
    with dissolve
    pov "Hey, Meghan."
    pov "Buy anything new today?"
    show pov confused at left
    show meg confused_talk at right
    meg "Wouldn't you like to know."
    show pov embarrassed_talk at left
    show meg confused at right
    pov "Yeah, that's why I asked-"
    show pov bored_talk at left
    pov "Actually, no. I don't really care."
    show pov bored at left
    meg "Mhmm."

    jump lbl_mall_day

label lbl_mall_day_meghan_9:
    show pov confused_talk at left
    with dissolve
    hide btn_mall_day_meghan_idle2
    show meg confused at right
    with dissolve
    pov "Don't you have anywhere else to be?"
    pov "You're always here."
    show pov confused at left
    show meg confused_talk at right
    meg "How would you know?"
    show pov shocked at left
    meg "For you to know we're always is means you have to be here to witness us here."
    show pov embarrassed_talk at left
    show meg confused at right
    pov "Well- I"
    show pov confused_talk at left
    show meg smirk at right
    pov "Fuck... you actually made a decent point."

    jump lbl_mall_day

label lbl_mall_day_meghan_10:
    show pov neutral_talk at left
    with dissolve
    hide btn_mall_day_meghan_idle2
    show meg smirk at right
    with dissolve
    pov "Any plans later tonight, Meghan?"
    show pov neutral at left
    show meg smirk_talk at right
    meg "The girls and I are gonna have a slumber party."
    show pov shocked at left
    show meg embarrassed_talk at right
    meg "Braid each other's hair, gossip about boys."
    meg "Eat junk food and watch horror movies late into the night."
    show pov neutral_talk at left
    show meg confused at right
    pov "Sounds awesome, huh- I was kinda expecting a more snarky answer."
    show pov neutral at left
    show meg embarrassed_talk at right
    meg "I love my girls, can't joke about that."

    jump lbl_mall_day
