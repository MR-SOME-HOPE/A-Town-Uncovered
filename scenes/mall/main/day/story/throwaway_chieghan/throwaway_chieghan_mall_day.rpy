## Throwaway Chieghan Mall Day Conversation ##
label lbl_mall_day_chieghan:

    ## Main Story
    if main_story <= 35 and insexworld == 1:
        jump lbl_mall_day_chieghan_sexworld
    ## NO EVENT
    else:
        jump lbl_mall_day_chieghan_convo

label lbl_mall_day_chieghan_convo:
## 1 - 5 is morning exclusive (School Bathroom)
## 6 - 10 is afternoon and weekend exclusive (Mall)
## 11 - 15 is interchangeable
    if date == 3 or date == 19 or date == 23 or date == 0:
        jump lbl_mall_day_chieghan_6
    elif date == 2 or date == 18 or date == 21:
        jump lbl_mall_day_chieghan_7
    elif date == 1 or date == 20 or date == 22:
        jump lbl_mall_day_chieghan_8
    elif date == 4 or date == 17 or date == 24:
        jump lbl_mall_day_chieghan_9
    elif date == 5 or date == 15 or date == 25:
        jump lbl_mall_day_chieghan_10
    elif date == 6 or date == 16 or date == 30:
        jump lbl_town_day_chieghan_11
    elif date == 9 or date == 14 or date == 29:
        jump lbl_town_day_chieghan_12
    elif date == 8 or date == 12 or date == 28:
        jump lbl_town_day_chieghan_13
    elif date == 7 or date == 13 or date == 26:
        jump lbl_town_day_chieghan_14
    elif date == 10 or date == 11 or date == 27:
        jump lbl_town_day_chieghan_15

## Afternoon Exclusive
label lbl_mall_day_chieghan_6:
    show pov neutral_talk at left
    with dissolve
    hide btn_mall_day_chieghan_idle2
    show chi neutral at right
    with dissolve
    pov "Hey, Chieghan. Whatcha drinking?"
    show pov neutral at left
    show chi neutral_talk at right
    chi "Honeydew smoothie. The best flavour."
    show pov neutral_talk at left
    show chi smirk at right
    pov "Oh, nice! Hella' yum"
    show pov neutral at left
    show chi smirk_talk at right
    chi "Very yum! You want to try some. [povname]-ssi?"
    show pov neutral_talk at left
    show chi neutral at right
    pov "Sure! I'd love a sip."
    show pov embarrassed at left
    show chi embarrassed_talk at right
    chi "The- uh- place to buy... is over there."

    jump lbl_mall_day

label lbl_mall_day_chieghan_7:
    show pov neutral_talk at left
    with dissolve
    hide btn_mall_day_chieghan_idle2
    show chi neutral at right
    with dissolve
    pov "Hey-hey."
    show pov neutral at left
    show chi neutral_talk at right
    chi "Hi-hi."
    show pov neutral_talk at left
    show chi neutral at right
    pov "Pretty packed here today, huh?"
    show pov neutral at left
    show chi neutral_talk at right
    chi "There are lots of sales."
    show chi shocked_talk at right
    chi "Oooh! That reminds me, we need to go to M&H later."
    show chi smirk_talk at right
    chi "I saw some cute sweaters."
    show pov neutral_talk at left
    show chi neutral at right
    pov "Well, don't let me hold you up. See you 'round."

    jump lbl_mall_day

label lbl_mall_day_chieghan_8:
    show pov neutral at left
    with dissolve
    hide btn_mall_day_chieghan_idle2
    show chi smirk_talk at right
    with dissolve
    chi "Hey, [povname]."
    show pov shocked at left
    chi "You have something on your shirt."
    show pov confused_talk at left
    show chi smirk at right
    pov "Oh- oops- where is it?"
    show pov confused at left
    pov "..."
    show pov confused_talk at left
    pov "I don't see anything."
    show pov bored at left
    show chi smirk_talk at right
    chi "That is what is called, 'a goof'!"
    show pov bored_talk at left
    show chi smirk at right
    pov "Haha... you got me there, Chieghan. Nice one."

    jump lbl_mall_day

label lbl_mall_day_chieghan_9:
    show pov confused at left
    with dissolve
    hide btn_mall_day_chieghan_idle2
    show chi sad_talk at right
    with dissolve
    chi "Oh man, the aircon is too cold."
    chi "Aren't you freezing, [povname]."
    show pov confused_talk at left
    show chi confused at right
    pov "Nope. Maybe you're coming up with a fever"
    show pov confused at left
    show chi confused_talk at right
    chi "Fever?"
    show pov embarrassed_talk at left
    show chi confused at right
    pov "Yeah, maybe you're becoming sick."
    show pov embarrassed at left
    show chi shocked_talk at right
    chi "Oh! Sick."
    show chi neutral at right
    chi "..."
    show chi bored_talk at right
    chi "I fucking hope not."

    jump lbl_mall_day

label lbl_mall_day_chieghan_10:
    show pov neutral at left
    with dissolve
    hide btn_mall_day_chieghan_idle2
    show chi neutral_talk at right
    with dissolve
    chi "Afternoon, [povname]."
    show pov neutral_talk at left
    show chi neutral at right
    pov "Hey, Chieghan, what's new."
    show pov confused at left
    show chi shocked_talk at right
    chi "Don't go to that new KBBQ place."
    show chi bored_talk at right
    chi "The sides they give are so..."
    chi "So...."
    chi "Crappy."
    show pov neutral_talk at left
    show chi bored at right
    pov "Any recommendations then?."
    show pov bored at left
    show chi smirk_talk at right
    chi "Have you been to Korea?"

    jump lbl_mall_day
