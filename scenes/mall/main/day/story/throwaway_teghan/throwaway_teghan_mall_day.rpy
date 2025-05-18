## Throwaway Teghan Mall Day Conversation ##
label lbl_mall_day_teghan:

    ## Main Story
    if main_story <= 35 and insexworld == 1:
        jump lbl_mall_day_teghan_sexworld
    ## NO EVENT
    else:
        jump lbl_mall_day_teghan_convo

label lbl_mall_day_teghan_convo:
## 1 - 5 is morning exclusive (School Bathroom)
## 6 - 10 is afternoon and weekend exclusive (Mall)
## 11 - 15 is interchangeable
    if date == 10 or date == 17 or date == 26 or date == 0:
        jump lbl_mall_day_teghan_6
    elif date == 9 or date == 16 or date == 21:
        jump lbl_mall_day_teghan_7
    elif date == 8 or date == 11 or date == 22:
        jump lbl_mall_day_teghan_8
    elif date == 5 or date == 12 or date == 23:
        jump lbl_mall_day_teghan_9
    elif date == 4 or date == 13 or date == 24:
        jump lbl_mall_day_teghan_10
    elif date == 3 or date == 14 or date == 25:
        jump lbl_town_day_teghan_11
    elif date == 2 or date == 15 or date == 27:
        jump lbl_town_day_teghan_12
    elif date == 1 or date == 18 or date == 28:
        jump lbl_town_day_teghan_13
    elif date == 7 or date == 19 or date == 29:
        jump lbl_town_day_teghan_14
    elif date == 6 or date == 20 or date == 30:
        jump lbl_town_day_teghan_15

## Afternoon Exclusive
label lbl_mall_day_teghan_6:
    show pov neutral at left
    with dissolve
    hide btn_mall_day_teghan_idle2
    show teg neutral_talk at right
    with dissolve
    teg "Afternoon, my main dude."
    show teg smirk_talk at right
    teg "You here to shop or something?"
    show pov neutral_talk at left
    show teg smirk at right
    pov "Maybe, I might take a shift at Ice Cream'py."
    show pov embarrassed at left
    show teg neutral_talk at right
    teg "Oh yeah! I've seen you there a couple of times, cute uniform."
    show teg smirk_talk at right
    teg "It's very... manly."
    show pov confused_talk at left
    show teg smirk at right
    pov "Pink is manly, only a real man can rock it."
    show pov smirk at left
    show teg smirk_talk at right
    teg "And rock it, you do."

    jump lbl_mall_day

label lbl_mall_day_teghan_7:
    show pov neutral at left
    with dissolve
    hide btn_mall_day_teghan_idle2
    show teg neutral_talk at right
    with dissolve
    teg "Sup."
    show pov neutral_talk at left
    show teg neutral at right
    pov "Sup, Teghan."
    show pov confused_talk at left
    show teg confused at right
    pov "Did you see the luggage store is having a clearance sale."
    show pov confused at left
    show teg confused_talk at right
    teg "Yeah, I think they're going out of business."
    teg "How do luggage stores stay in business, luggage is so..."
    teg "Like you buy it and keep it for years."
    show pov confused_talk at left
    show teg confused at right
    pov "Yeah, I have no idea."

    jump lbl_mall_day

label lbl_mall_day_teghan_8:
    show pov neutral at left
    with dissolve
    hide btn_mall_day_teghan_idle2
    show teg neutral_talk at right
    with dissolve
    teg "Nice seeing you here, [povname]."
    show pov neutral_talk at left
    show teg neutral at right
    pov "Call me a mallrat but this really is my home away from home."
    show pov neutral at left
    show teg bored_talk at right
    teg "I feel you so hard."
    show pov smirk at left
    show teg neutral_talk at right
    teg "If there was ever a zombie apocalypse, the mall would be the best place to be."
    show pov confused_talk at left
    show teg confused at right
    pov "Have you ever played 'Dead Uprising'?"
    show pov neutral at left
    show teg smirk_talk at right
    teg "No, it sounds fun."
    show pov smirk_talk at left
    show teg neutral at right
    pov "The funnest."

    jump lbl_mall_day

label lbl_mall_day_teghan_9:
    show pov neutral_talk at left
    with dissolve
    hide btn_mall_day_teghan_idle2
    show teg confused at right
    with dissolve
    pov "Good Arvo."
    show pov neutral at left
    show teg confused_talk at right
    teg "Arvo? Like Arvocado?"
    show pov neutral_talk at left
    show teg shocked at right
    pov "It's Australian for 'afternoon'."
    show pov neutral at left
    show teg shocked_talk at right
    teg "Didn't know you spoke Australian."
    show pov smirk_talk at left
    show teg neutral at right
    pov "Yeah, I dabble in the lost language."
    show pov neutral at left
    show teg sad_talk at right
    teg "Can't believe they all went extinct."
    show pov sad_talk at left
    show teg smirk at right
    pov "Truly a sad day in history."

    jump lbl_mall_day

label lbl_mall_day_teghan_10:
    show pov sad_talk at left
    with dissolve
    hide btn_mall_day_teghan_idle2
    show teg confused at right
    with dissolve
    pov "Fuck, why is it so hot today?"
    show pov bored at left
    show teg smirk_talk at right
    teg "Shall I leave the mall?"
    show pov bored_talk at left
    show teg smirk at right
    pov "Har har har, never heard that one before."
    show pov confused at left
    show teg confused_talk at right
    teg "What's up your butt, [povname]? Swampass."
    show pov confused_talk at left
    show teg shocked at right
    pov "Don't even get me started."
    show pov sad at left
    show teg embarrassed_talk at right
    teg "Eugh- Sorry I asked."

    jump lbl_mall_day
