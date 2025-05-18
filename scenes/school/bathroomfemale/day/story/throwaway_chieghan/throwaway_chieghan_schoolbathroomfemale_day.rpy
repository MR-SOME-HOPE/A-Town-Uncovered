## Throwaway Chieghan School Bathroom Female Day Conversation ##
label lbl_schoolbathroomfemale_day_chieghan:

    ## Main Story
    if main_story <= 35 and insexworld == 1:
        jump lbl_schoolbathroomfemale_day_chieghan_sexworld
    ## NO EVENT
    else:
        jump lbl_schoolbathroomfemale_day_chieghan_convo

label lbl_schoolbathroomfemale_day_chieghan_convo:
## 1 - 5 is morning exclusive (School Bathroom)
## 6 - 10 is afternoon and weekend exclusive (Mall)
## 11 - 15 is interchangeable
    if date == 1 or date == 11 or date == 23 or date == 0:
        jump lbl_schoolbathroomfemale_day_chieghan_1
    elif date == 2 or date == 12 or date == 22:
        jump lbl_schoolbathroomfemale_day_chieghan_2
    elif date == 3 or date == 13 or date == 21:
        jump lbl_schoolbathroomfemale_day_chieghan_3
    elif date == 4 or date == 14 or date == 24:
        jump lbl_schoolbathroomfemale_day_chieghan_4
    elif date == 5 or date == 17 or date == 25:
        jump lbl_schoolbathroomfemale_day_chieghan_5
    elif date == 8 or date == 18 or date == 29:
        jump lbl_town_day_chieghan_11
    elif date == 9 or date == 20 or date == 30:
        jump lbl_town_day_chieghan_12
    elif date == 6 or date == 15 or date == 26:
        jump lbl_town_day_chieghan_13
    elif date == 7 or date == 16 or date == 27:
        jump lbl_town_day_chieghan_14
    elif date == 10 or date == 19 or date == 28:
        jump lbl_town_day_chieghan_15

## Morning Exclusive
label lbl_schoolbathroomfemale_day_chieghan_1:
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolbathroom_day_chieghan_idle2
    show chi neutral at right
    with dissolve
    pov "Hey, Chieghan."
    show pov neutral at left
    show chi neutral_talk at right
    chi "Annyeong, [povname]-ssi."
    show chi smirk_talk at right
    chi "It is good day, neh?"
    show pov neutral_talk at left
    show chi neutral at right
    pov "It is a good day. How are you?"
    show pov embarrassed at left
    show chi neutral_talk at right
    chi "I am good! Class will be soon startin-geu."
    show pov shocked at left
    show chi smirk_talk at right
    chi "Pali pali paaaali! Les' geeeeet it!"

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_chieghan_2:
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolbathroom_day_chieghan_idle2
    show chi neutral at right
    with dissolve
    pov "Morning, Chieghan."
    show pov neutral at left
    show chi neutral_talk at right
    chi "Good morning, [povname]."
    show pov neutral at left
    show chi neutral_talk at right
    chi "Did you watch 'Reply 1921' last night?"
    show pov confused_talk at left
    show chi neutral at right
    pov "Is that- the... K-drama?"
    show pov embarrassed at left
    show chi neutral_talk at right
    chi "Nehh~"
    show pov embarrassed_talk at left
    show chi neutral at right
    pov "Oh.. shucks... I guess I missed it."
    show pov embarrassed at left
    show chi neutral_talk at right
    chi "Oh! That's okay, it's on Webflicks."
    show chi smirk_talk at right
    chi "Lucky-ah~"

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_chieghan_3:
    show pov neutral at left
    with dissolve
    hide btn_schoolbathroom_day_chieghan_idle2
    show chi confused_talk at right
    with dissolve
    chi "Morning, [povname]."
    show pov embarrassed at left
    chi "Is it normal for guys here to hang out in this girls' bathroom?"
    show pov embarrassed_talk at left
    show chi confused at right
    pov "Um, not really."
    show pov embarrassed at left
    show chi confused_talk at right
    chi "Ah-"
    show chi confused at right
    chi "I see, I see."
    chi "..."
    show pov embarrassed_talk at left
    pov "I guess- I should go?"
    show pov embarrassed at left
    show chi neutral_talk at right
    chi "I like that idea!"

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_chieghan_4: ##
    show pov smirk_talk at left
    with dissolve
    hide btn_schoolbathroom_day_chieghan_idle2
    show chi neutral at right
    with dissolve
    pov "Hey, lovely day, ain't it? A little chilly outside but it's all good."
    show pov smirk at left
    chi "..."
    show pov embarrassed at left
    show chi shocked_talk at right
    chi "Hmm? Were you talking to me?"
    show pov embarrassed_talk at left
    show chi shocked at right
    pov "I was... talking in your general direction..."
    show pov embarrassed at left
    show chi smirk_talk at right
    chi "Haha, you are weird, [povname]-chingu."
    show pov embarrassed_talk at left
    show chi embarrassed at right
    pov "Haha... yeah. Chingu back at chuu... too."
    show pov embarrassed at left
    chi "..."

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_chieghan_5:
    show pov confused at left
    with dissolve
    hide btn_schoolbathroom_day_chieghan_idle2
    show chi neutral_talk at right
    with dissolve
    chi "[povname]! There you are!"
    show pov confused_talk at left
    show chi confused at right
    pov "Oh- where you waiting for me- here?"
    show pov confused at left
    show chi confused_talk at right
    chi "Huh- no?"
    show chi embarrassed_talk at right
    chi "It's like- a type of greeting, right?"
    chi "I'm trying to learn new ways to say 'hi'."
    show chi embarrassed at right
    chi "..."
    show pov shocked at left
    show chi neutral_talk at right
    chi "Hi!"
    show pov neutral_talk at left
    show chi neutral at right
    pov "Hi!"

    jump lbl_schoolbathroomfemale_day

## Afternoon and Mall Exclusive
label lbl_town_day_chieghan_11:
    show pov smirk_talk at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_chieghan_idle2
    else:
        hide btn_mall_day_chieghan_idle2
    show chi smirk at right
    with dissolve
    pov "Yooo!"
    show pov smirk at left
    show chi smirk_talk at right
    chi "Yo yo, [povname]."
    show pov neutral at left
    show chi neutral_talk at right
    chi "What is up in the hood-hood."
    show pov neutral at left
    show chi smirk_talk at right
    chi "A yee-yee~"
    show pov neutral_talk at left
    show chi shocked at right
    pov "Hehehe, that was just too cute, Chieghan."
    show pov smirk at left
    show chi sad_talk at right
    chi "Yo yo, no!"
    show pov shocked at left
    show chi neutral_talk at right
    chi "I'M PUCCKIING YAKUZA, BITTCHH!"

    jump lbl_town_day_chieghan_end

label lbl_town_day_chieghan_12:
    show pov neutral_talk at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_chieghan_idle2
    else:
        hide btn_mall_day_chieghan_idle2
    show chi neutral at right
    with dissolve
    pov "Hey, Chieghan."
    show pov smirk_talk at left
    show chi confused at right
    pov "Chicken-lickin-"
    show pov confused at left
    show chi confused_talk at right
    chi "That's like the McDolands, neh?"
    show pov neutral at left
    show chi smirk_talk at right
    chi "Finger-licking niceeeee~"
    show pov neutral_talk at left
    show chi confused at right
    pov "It's actually KCF."
    show pov confused at left
    show chi confused_talk at right
    chi "Korean Chicken Fries?"
    show pov confused_talk at left
    show chi confused at right
    pov "No, Kentucky Chicken Fries."
    show pov embarrassed at left
    show chi neutral_talk at right
    chi "Korean one better. Hwaiting."

    jump lbl_town_day_chieghan_end

label lbl_town_day_chieghan_13:
    show pov confused at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_chieghan_idle2
    else:
        hide btn_mall_day_chieghan_idle2
    show chi confused_talk at right
    with dissolve
    chi "What's the bird?"
    show pov confused_talk at left
    show chi confused at right
    pov "The bird?"
    show pov confused at left
    show chi smirk_talk at right
    chi "Yeah, I heard it on TV last night. Westerners are so weird."
    show pov neutral_talk at left
    show chi confused at right
    pov "The bird is when you put the middle finger up, it's a rude gesture."
    show pov confused at left
    show chi neutral_talk at right
    chi "A b-b-bird bird bird, the bird is the word."
    show pov bored at left
    show chi smirk_talk at right
    chi "A b-b--- bird bird-"
    show pov bored_talk at left
    show chi smirk at right
    pov "Oh- that bird."
    show pov bored at left
    show chi smirk_talk at right
    chi "Don't chu know that the word is the bird?"

    jump lbl_town_day_chieghan_end

label lbl_town_day_chieghan_14:
    show pov neutral at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_chieghan_idle2
    else:
        hide btn_mall_day_chieghan_idle2
    show chi confused_talk at right
    with dissolve
    chi "Hey, you know how to use chopsticks, right?"
    show pov neutral_talk at left
    show chi smirk at right
    pov "Yeah? Shouldn't everyone?"
    show pov neutral at left
    show chi smirk_talk at right
    chi "Teghan can't use chopsticks."
    show chi shocked_talk at right
    chi "How can that even be?!"
    chi "It's so easy!"
    show pov embarrassed_talk at left
    show chi confused at right
    pov "Different cultural up-bringing?"
    show chi shocked at right
    pov "Maybe she never liked Asian food? I don't know."
    show pov embarrassed at left
    show chi angry_talk at right
    chi "Unacceptable."

    jump lbl_town_day_chieghan_end

label lbl_town_day_chieghan_15:
    show pov neutral_talk at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_chieghan_idle2
    else:
        hide btn_mall_day_chieghan_idle2
    show chi neutral at right
    with dissolve
    pov "Have you seen 'Parasite'?"
    show pov confused at left
    show chi neutral_talk at right
    chi "I don't really watch anime."
    show pov smirk_talk at left
    show chi confused at right
    pov "No, not 'Parasyte'. 'Parasite'."
    show pov embarrassed at left
    chi "..."
    show chi confused_talk at right
    chi "Para..."
    show pov embarrassed_talk at left
    show chi confused at right
    pov "Site."
    show pov embarrassed at left
    show chi confused_talk at right
    chi "Site."
    show pov bored at left
    show chi embarrassed_talk at right
    chi "I don't- sorry. I don't really watch anime."

    jump lbl_town_day_chieghan_end

label lbl_town_day_chieghan_end:
    if gtime == 0:
        jump lbl_schoolbathroomfemale_day
    else:
        jump lbl_mall_day
