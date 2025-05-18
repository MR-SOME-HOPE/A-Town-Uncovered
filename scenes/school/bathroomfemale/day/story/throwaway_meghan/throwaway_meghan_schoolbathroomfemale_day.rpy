## Throwaway Meghan School Bathroom Female Day Conversation ##
label lbl_schoolbathroomfemale_day_meghan:

    ## Main Story
    if main_story <= 35 and insexworld == 1:
        jump lbl_schoolbathroomfemale_day_meghan_sexworld
    ## NO EVENT
    else:
        jump lbl_schoolbathroomfemale_day_meghan_convo

label lbl_schoolbathroomfemale_day_meghan_convo:
## 1 - 5 is morning exclusive (School Bathroom)
## 6 - 10 is afternoon and weekend exclusive (Mall)
## 11 - 15 is interchangeable
    if date == 3 or date == 19 or date == 25 or date == 0:
        jump lbl_schoolbathroomfemale_day_meghan_1
    elif date == 2 or date == 20 or date == 29:
        jump lbl_schoolbathroomfemale_day_meghan_2
    elif date == 1 or date == 17 or date == 28:
        jump lbl_schoolbathroomfemale_day_meghan_3
    elif date == 6 or date == 18 or date == 30:
        jump lbl_schoolbathroomfemale_day_meghan_4
    elif date == 5 or date == 15 or date == 21:
        jump lbl_schoolbathroomfemale_day_meghan_5
    elif date == 4 or date == 16 or date == 22:
        jump lbl_town_day_meghan_11
    elif date == 9 or date == 13 or date == 23:
        jump lbl_town_day_meghan_12
    elif date == 8 or date == 14 or date == 26:
        jump lbl_town_day_meghan_13
    elif date == 7 or date == 11 or date == 24:
        jump lbl_town_day_meghan_14
    elif date == 10 or date == 12 or date == 27:
        jump lbl_town_day_meghan_15

## Morning Exclusive
label lbl_schoolbathroomfemale_day_meghan_1:
    show pov shocked at left
    with dissolve
    hide btn_schoolbathroom_day_meghan_idle2
    show meg angry_talk at right
    with dissolve
    meg "What are you doing here?"
    show pov embarrassed_talk at left
    show meg angry at right
    pov "The door was unlocked."
    show pov embarrassed at left
    show meg angry_talk at right
    meg "This is the girl's bathroom, pleb."
    show pov embarrassed_talk at left
    show meg bored at right
    pov "Oh, is it? My mistake I thought it was the little boy's room."
    show pov embarrassed at left
    meg "..."
    show pov shocked at left
    show meg bored_talk at right
    meg "Well? Aren't you gonna leave?"

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_meghan_2:
    show pov shocked at left
    with dissolve
    hide btn_schoolbathroom_day_meghan_idle2
    show meg bored_talk at right
    with dissolve
    meg "Okay, seriously? You need to stop coming in here."
    show pov embarrassed at left
    meg "I would tell a teacher about this but I'm not a fucking snitch."
    show pov shocked at left
    show meg angry_talk at right
    meg "Although, which is worst? A snitch, or a pervert?"
    show meg bored_talk at right
    meg "Food for thought."
    show pov embarrassed at left
    show meg bored at right
    pov "Hmm.."
    show pov bored at left
    show meg bored_talk at right
    meg "Um, no. That wasn't an invitation for a conversation."
    show meg bored at right
    pov "..."

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_meghan_3:
    show pov bored at left
    with dissolve
    hide btn_schoolbathroom_day_meghan_idle2
    show meg confused_talk at right
    with dissolve
    meg "Hey, uh.. you..."
    show pov confused at left
    meg "Um... Lophanzo."
    show pov confused_talk at left
    show meg confused at right
    pov "Lophanzo, where did you get Lophanzo from?"
    show pov confused at left
    show meg angry_talk at right
    meg "It's the first name that popped into my mind."
    show pov smirk_talk at left
    show meg confused at right
    pov "How many Lophanzo's do you know in your life?"
    show pov bored at left
    show meg bored_talk at right
    meg "..."
    show pov bored at left
    show meg bored_talk at right
    meg "22?"
    show pov bored at left
    show meg bored_talk at right
    meg "No, 23. Forgot about 'Smooth Jazz Lophanzo'."

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_meghan_4:
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolbathroom_day_meghan_idle2
    show meg bored at right
    with dissolve
    pov "Morning, Meghan."
    pov "How's it hanging"
    show pov smirk at left
    show meg neutral_talk at right
    meg "My tits are hanging perky and balanced."
    show pov smirk_talk at left
    show meg neutral at right
    pov "I- was not expecting that response."
    show pov bored at left
    show meg neutral_talk at right
    meg "Yeah, well that's because you have a basic bitch mindset."
    show pov bored_talk at left
    show meg confused at right
    pov "What is wrong with you."
    show pov bored at left
    show meg smirk_talk at right
    meg "Not my tits, that's for damn sure."

    jump lbl_schoolbathroomfemale_day

label lbl_schoolbathroomfemale_day_meghan_5:
    show pov smirk_talk at left
    with dissolve
    hide btn_schoolbathroom_day_meghan_idle2
    show meg bored at right
    with dissolve
    pov "Gooood morning, Meghan."
    show pov smirk at left
    show meg bored_talk at right
    meg "You know I don't like you, [povname]."
    meg "Why do you keep talking to me."
    show pov smirk_talk at left
    show meg confused at right
    pov "Because I know eventually you'll come to like me."
    show pov smirk at left
    show meg bored_talk at right
    meg "Not even in your dreams, [povname]."
    show pov smirk_talk at left
    show meg sad at right
    pov "My dreams about you so far have said otherwise."
    show pov embarrassed at left
    show meg confused_talk at right
    meg "Ew."

    jump lbl_schoolbathroomfemale_day

## Afternoon and Mall Exclusive
label lbl_town_day_meghan_11:
    show pov confused at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_meghan_idle2
    else:
        hide btn_mall_day_meghan_idle2
    show meg bored_talk at right
    with dissolve
    meg "Hey, you."
    show pov bored_talk at left
    show meg confused at right
    pov "[povname]."
    show pov confused at left
    show meg confused_talk at right
    meg "Whatever. Stop breathing so close to me."
    show pov confused_talk at left
    show meg confused at right
    pov "I'm standing like 5 feet from you."
    show pov bored at left
    show meg bored_talk at right
    meg "What did I just say?"
    show pov bored_talk at left
    show meg confused at right
    pov "Why even start a conversation if you're gonna be so icy?"

    jump lbl_town_day_meghan_end

label lbl_town_day_meghan_12:
    show pov shocked at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_meghan_idle2
    else:
        hide btn_mall_day_meghan_idle2
    show meg confused_talk at right
    with dissolve
    meg "[povname]?"
    show pov neutral_talk at left
    show meg confused at right
    pov "You remembered!"
    show pov shocked at left
    show meg confused_talk at right
    meg "You have shit on your shirt."
    show pov embarrassed_talk at left
    show meg confused at right
    pov "Oh-"
    show pov angry_talk at left
    show meg smirk at right
    pov "Wait- No there isn't!"
    show pov angry at left
    show meg smirk_talk at right
    meg "Made you look."
    show pov bored at left
    show meg neutral_talk at right
    meg "Loser. Hahahaha! Oh Chieghan! Did you see that?"

    jump lbl_town_day_meghan_end

label lbl_town_day_meghan_13:
    show pov shocked at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_meghan_idle2
    else:
        hide btn_mall_day_meghan_idle2
    show meg neutral_talk at right
    with dissolve
    meg "Hey, you're invited to an all-exclusive private party!"
    show pov smirk at left
    show meg smirk_talk at right
    meg "There'll be hot girls, obviously."
    meg "Alcohol, obviously."
    meg "And enough MJ to make you fly."
    show pov neutral_talk at left
    show meg confused at right
    pov "Hell yeah! Count me in!"
    show pov shocked at left
    show meg confused_talk at right
    meg "Wait, oh. Sorry, you looked like someone else."
    show pov angry at left
    show meg smirk_talk at right
    meg "Uninvited."

    jump lbl_town_day_meghan_end

label lbl_town_day_meghan_14:
    show pov smirk_talk at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_meghan_idle2
    else:
        hide btn_mall_day_meghan_idle2
    show meg bored at right
    with dissolve
    pov "What's up, Meghan?"
    show meg confused at right
    pov "Make anyone cry today."
    show pov neutral at left
    show meg confused_talk at right
    meg "It's still early."
    show pov confused at left
    show meg neutral_talk at right
    meg "Maybe you'll be the first."
    show pov smirk_talk at left
    show meg smirk at right
    pov "I doubt you can make me cry."
    show pov bored at left
    show meg smirk_talk at right
    meg "Ran out of tears from the last time?"

    jump lbl_town_day_meghan_end

label lbl_town_day_meghan_15:
    show pov neutral_talk at left
    with dissolve
    if gtime == 0:
        hide btn_schoolbathroom_day_meghan_idle2
    else:
        hide btn_mall_day_meghan_idle2
    show meg confused at right
    with dissolve
    pov "Hey-"
    show pov shocked_talk at left
    show meg embarrassed at right
    pov "Oooft- that's a strong fragrance."
    show pov sad_talk at left
    pov "I knew I smelt something pungent."
    show pov confused at left
    show meg sad_talk at right
    meg "Look, I may have sprayed three times the amount of perfume I usually do..."
    show meg embarrassed_talk at right
    meg "Y'know, like you do something, and then you forget if you've already done it."
    meg "So you do it again..."
    show meg sad_talk at right
    meg "And again..."

    jump lbl_town_day_meghan_end

label lbl_town_day_meghan_end:
    if gtime == 0:
        jump lbl_schoolbathroomfemale_day
    else:
        jump lbl_mall_day
