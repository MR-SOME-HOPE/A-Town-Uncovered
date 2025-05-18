## Throwaway Miss Allaway Classroom Day Conversation ##
label lbl_classroom_day_missallaway:
## Main Story
    if insexworld == 1 and main_story <= 35:
        scene bg classroom_daysexworld
        show btn_classroom_day_missallaway_idle2
        if gtime == 0:
            show btn_classroom_daysexworld_effie_idle2
        $ renpy.pause(0.001)

        jump lbl_classroom_day_missallaway_sexworld_1

    elif insexworld == 0:
        scene bg classroom_day
        show btn_classroom_day_missallaway_idle2
        if gtime == 0:
            show btn_classroom_day_effie_idle2
        elif gtime == 1:# and luna_path > 0
            show btn_classroom_day_luna_idle2
        $ renpy.pause(0.001)


## Side Story
    if missallaway_path == 3:
        jump lbl_classroom_day_missallaway_16
    elif missallaway_path == 4:
        jump lbl_classroom_day_missallaway_20
    elif missallaway_path == 5:
        jump lbl_classroom_day_missallaway_17
    elif missallaway_path == 8:
        if gtime == 1:
            menu:
                "Talk":
                    jump lbl_classroom_day_missallaway_convo
                "Give Gift" if selecteditem != None and principallashley_path >= 10:
                    jump lbl_missallaway_giftgiving
                "After class tutoring":
                    jump lbl_tutoring_afterschool
                "Nevermind":
                    jump lbl_classroom_day
        else:
            jump lbl_classroom_day_missallaway_convo
    elif missallaway_path == 11:
        jump lbl_classroom_day_missallaway_18
    elif missallaway_path == 16:
        jump lbl_classroom_day_missallaway_19
    elif missallaway_path >= 25:
        if allawaybedroomsex_sneakherin == 1 and gtime == 1:
            $ allawaybedroomsex_sneakherin = 2
        elif allawaybedroomsex_sneakherin == 2:
            jump lbl_classroom_day_missallaway_come_visit_fail
        elif allawaybedroomsex_sneakherin == 3:
            jump lbl_classroom_day_missallaway_come_visit_donttalktome
        menu:
            "Talk":
                jump lbl_classroom_day_missallaway_convo
            "Give Gift" if selecteditem != None and principallashley_path >= 10:
                jump lbl_missallaway_giftgiving
            "After class fun":
                jump lbl_allaway_after_school_sex
            "Ask to movie date" if moviedate == 0:
                jump lbl_classroom_day_missallaway_moviedate
            "Ask her to come visit your house"if gtime==0 and allawaybedroomsex_sneakherin == 0:
                jump lbl_classroom_day_missallaway_come_visit
            "Nevermind":
                jump lbl_classroom_day
    else:
        menu:
            "Talk":
                jump lbl_classroom_day_missallaway_convo
            "Give Gift" if selecteditem != None and principallashley_path >= 10:
                jump lbl_missallaway_giftgiving
            "Nevermind":
                jump lbl_classroom_day

label lbl_classroom_day_missallaway_convo:
## 1 - 4 is morning exclusive
## 5 - 8 is afternoon exclusive
## 9 - 11 is the weekend morning exclusive (cafe)
## 12 - 15 is interchangeable
    if gtime == 0:
        if date == 10 or date == 20 or date == 27 or date == 4:
            jump lbl_classroom_day_missallaway_1
        elif date == 9 or date == 11 or date == 28 or date == 14:
            jump lbl_classroom_day_missallaway_2
        elif date == 8 or date == 12 or date == 29 or date == 21:
            jump lbl_classroom_day_missallaway_3
        elif date == 5 or date == 13 or date == 30:
            jump lbl_classroom_day_missallaway_4
        elif date == 3 or date == 16 or date == 22 or date == 7:
            jump lbl_town_day_missallaway_12
        elif date == 1 or date == 17 or date == 24 or date == 19:
            jump lbl_town_day_missallaway_13
        elif date == 2 or date == 15 or date == 23 or date == 26:
            jump lbl_town_day_missallaway_14
        elif date == 6 or date == 18 or date == 25 or date == 0:
            jump lbl_town_day_missallaway_15
    elif gtime == 1:
        if date == 7 or date == 11 or date == 30 or date == 9:
            jump lbl_classroom_day_missallaway_5
        elif date == 6 or date == 15 or date == 27 or date == 16:
            jump lbl_classroom_day_missallaway_6
        elif date == 8 or date == 14 or date == 24 or date == 29:
            jump lbl_classroom_day_missallaway_7
        elif date == 5 or date == 12 or date == 21:
            jump lbl_classroom_day_missallaway_8
        elif date == 4 or date == 20 or date == 26 or date == 1:
            jump lbl_town_day_missallaway_12
        elif date == 10 or date == 17 or date == 23 or date == 13:
            jump lbl_town_day_missallaway_13
        elif date == 3 or date == 19 or date == 28 or date == 22:
            jump lbl_town_day_missallaway_14
        elif date == 2 or date == 18 or date == 25 or date == 0:
            jump lbl_town_day_missallaway_15

## Morning Exclusive
label lbl_classroom_day_missallaway_1:
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral_talk at right
    with dissolve
    mis "Good morning, [povname]."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Morning to you too, Miss."
    show pov bored at left
    show mis neutral_talk at right
    mis "Class is about to start, you should get to your seat."
    show pov bored_talk at left
    show mis bored at right
    pov "Yay.. can't wait."
    show pov embarrassed at left
    show mis bored_talk at right
    mis "Don't give me that sass, [povname]."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_2:
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral_talk at right
    with dissolve
    mis "How's your morning, [povname]?"
    show pov neutral_talk at left
    show mis embarrassed at right
    pov "It's good so far. How's yours going?"
    show pov neutral at left
    show mis sad_talk at right
    mis "The coffee machine in the teacher's room is broken.."
    show pov embarrassed at left
    mis "I'm... going to survive..."
    mis "Right?"
    show pov embarrassed_talk at left
    show mis embarrassed at right
    pov "I believe you will, don't worry about it."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_3:
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral at right
    with dissolve
    pov "Morning, Miss Allaway."
    show pov neutral at left
    show mis neutral_talk at right
    mis "Morning."
    show pov embarrassed at left
    show mis bored_talk at right
    mis "Uh, [povname]. Can you do me a favour and stop drawing in your books?"
    show pov bored_talk at left
    show mis bored at right
    pov "But I get bored in cla-"
    show pov embarrassed_talk at left
    pov "I meant.. I listen better when I'm multitasking..."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_4:
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis embarrassed at right
    with dissolve
    pov "Hey, beautiful day, isn't it, Miss Allaway?"
    show pov confused at left
    show mis embarrassed_talk at right
    mis "You can say that."
    show pov smirk_talk at left
    show mis bored at right
    pov "Why, not a morning person?"
    show pov neutral at left
    show mis bored_talk at right
    mis "Oh y'know. I just rather be at home right now."
    show pov neutral_talk at left
    show mis neutral at right
    pov "You and me both."

    jump lbl_classroom_day

## Afternoon Exclusive
label lbl_classroom_day_missallaway_5:
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral_talk at right
    with dissolve
    mis "Hey, [povname]. What can I do you for?"
    show pov neutral_talk at left
    show mis neutral at right
    pov "Nothing at the moment, I'm alright."
    show pov neutral at left
    show mis neutral_talk at right
    mis "Well, don't be a stranger. See me anytime you need help."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Thanks, Miss."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_6:
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral_talk at right
    with dissolve
    mis "Did you have lunch, [povname]?"
    show pov neutral_talk at left
    show mis confused at right
    pov "Not feeling that hungry."
    show pov neutral at left
    show mis smirk_talk at right
    mis "Really? I heard they're serving spaghetti today."
    show pov smirk_talk at left
    show mis neutral at right
    pov "Yeah... sounds delicious. University cafeteria spaghetti."
    show pov smirk at left
    show mis smirk_talk at right
    mis "Not a fan of ketchup and noodles? What a surprise."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_7:
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral_talk at right
    with dissolve
    mis "How are you holding up in class?"
    show pov embarrassed_talk at left
    show mis confused at right
    pov "I'm doing better than some people at least?"
    show pov embarrassed at left
    show mis confused_talk at right
    mis "I'm not going too fast for you, am I?"
    show pov neutral_talk at left
    show mis neutral at right
    pov "Honestly, you'd going at the perfect pace."
    show pov neutral at left
    show mis smirk_talk at right
    mis "Oh, good. I guess that means I'm going too fast for the others."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_8:
    show pov confused_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis confused at right
    with dissolve
    pov "How much of this do we need to know for the test?"
    show pov confused at left
    show mis neutral_talk at right
    mis "For this class? Only what I cover."
    show pov embarrassed at left
    mis "And I assure you, it's not that much."
    show pov embarrassed_talk at left
    show mis neutral at right
    pov "There's actually quite a lot of information to retain."
    show pov bored at left
    show mis smirk_talk at right
    mis "Well, you better start memorising your notes."

    jump lbl_classroom_day

## Interchangeable
label lbl_town_day_missallaway_12:
    if day >= 5:
        show pov neutral_talk at left
        with dissolve
        show misc neutral at right
        hide btn cafeoutside_day_missallaway_idle
        with dissolve
        pov "How's your day going so far, Miss?"
        show pov neutral at left
        show misc neutral_talk at right
        mis "Same old same old."
        show misc embarrassed_talk at right
        mis "I'm sure your life is more eventful than mine."
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "What shenanigans did you get up to this time?"
        show pov embarrassed_talk at left
        show misc confused at right
        pov "If you mean wondering around waiting for things to happen, eventful.. then sure."

        jump lbl_town_day_missallaway_end
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn_classroom_day_missallaway_idle2
        show mis neutral at right
        with dissolve
        pov "How's your day going so far, Miss?"
        show pov neutral at left
        show mis neutral_talk at right
        mis "Same old same old."
        show mis embarrassed_talk at right
        mis "I'm sure your life is more eventful than mine."
        show pov embarrassed at left
        show mis smirk_talk at right
        mis "What shenanigans did you get up to this time?"
        show pov embarrassed_talk at left
        show mis confused at right
        pov "If you mean wondering around waiting for things to happen, eventful.. then sure."

        jump lbl_town_day_missallaway_end

label lbl_town_day_missallaway_13:
    if day >= 5:
        show pov neutral at left
        with dissolve
        show misc neutral_talk at right
        hide btn cafeoutside_day_missallaway_idle
        with dissolve
        mis "How're liking the town so far?"
        show pov neutral_talk at left
        show misc neutral at right
        pov "I like it. I'm feeling very at home here nowadays."
        show pov neutral at left
        show misc neutral_talk at right
        mis "That's good to hear."
        mis "I grew up here all my life and I can't imagine myself anywhere else."
        mis "There's a perfect balance of fun and peacefulness without it feeling like a town-wide bingo night."

        jump lbl_town_day_missallaway_end
    else:
        show pov neutral at left
        with dissolve
        hide btn_classroom_day_missallaway_idle2
        show mis neutral_talk at right
        with dissolve
        mis "How're liking the town so far?"
        show pov neutral_talk at left
        show mis neutral at right
        pov "I like it. I'm feeling very at home here nowadays."
        show pov neutral at left
        show mis neutral_talk at right
        mis "That's good to hear."
        mis "I grew up here all my life and I can't imagine myself anywhere else."
        mis "There's a perfect balance of fun and peacefulness without it feeling like a town-wide bingo night."

        jump lbl_town_day_missallaway_end

label lbl_town_day_missallaway_14:
    if day >= 5:
        show pov neutral_talk at left
        with dissolve
        show misc neutral at right
        hide btn cafeoutside_day_missallaway_idle
        with dissolve
        pov "You been to the park recently?"
        show pov neutral at left
        show misc neutral_talk at right
        mis "I go there ocassionally to read and enjoy nature."
        show mis smirk_talk at right
        mis "Which is strange for me because I prefer being indoors."
        show pov neutral_talk at left
        show misc neutral at right
        pov "You gotta find a balanced lifestyle."
        show pov neutral at left
        show misc embarrassed_talk at right
        mis "That was the pretty much idea behind it."

        jump lbl_town_day_missallaway_end
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn_classroom_day_missallaway_idle2
        show mis neutral at right
        with dissolve
        pov "You been to the park recently?"
        show pov neutral at left
        show mis neutral_talk at right
        mis "I go there ocassionally to read and enjoy nature."
        show mis smirk_talk at right
        mis "Which is strange for me because I prefer being indoors."
        show pov neutral_talk at left
        show mis neutral at right
        pov "You gotta find a balanced lifestyle."
        show pov neutral at left
        show mis embarrassed_talk at right
        mis "That was the pretty much idea behind it."

        jump lbl_town_day_missallaway_end

label lbl_town_day_missallaway_15:
    if day >= 5:
        show pov neutral at left
        with dissolve
        show misc neutral_talk at right
        hide btn cafeoutside_day_missallaway_idle
        with dissolve
        mis "Good to see you, [povname]. Watch any new movies lately?"
        show pov smirk_talk at left
        show misc confused at right
        pov "I've watched A movie. It wasn't very good though."
        show pov neutral at left
        show misc confused_talk at right
        mis "You better not name a movie that I adore."
        show pov neutral_talk at left
        show misc shocked at right
        pov "Don't worry, I don't even know what it was called. I couldn't have cared less."
        show pov embarrassed at left
        show misc confused_talk at right
        mis "You don't know what it's called? That's something that would keep me up at night."

        jump lbl_town_day_missallaway_end
    else:
        show pov neutral at left
        with dissolve
        hide btn_classroom_day_missallaway_idle2
        show mis neutral_talk at right
        with dissolve
        mis "Good to see you, [povname]. Watch any new movies lately?"
        show pov smirk_talk at left
        show mis confused at right
        pov "I've watched A movie. It wasn't very good though."
        show pov neutral at left
        show mis confused_talk at right
        mis "You better not name a movie that I adore."
        show pov neutral_talk at left
        show mis shocked at right
        pov "Don't worry, I don't even know what it was called. I couldn't have cared less."
        show pov embarrassed at left
        show mis confused_talk at right
        mis "You don't know what it's called? That's something that would keep me up at night."

        jump lbl_town_day_missallaway_end

label lbl_town_day_missallaway_end:
    if day >= 5:
        jump lbl_cafeoutside_day
    else:
        jump lbl_classroom_day

## GIFT GIVING
label lbl_missallaway_giftgiving:
    ##if inventory.has_item(selecteditem):
        ##if missallawayAcceptedItems():
    if selecteditem.id ==  Items.socksflamingo.id:
        if day == 5 or day == 6:
            $ missallaway_gift_like_level += 40
        elif day == 1:
            $ missallaway_gift_like_level += 35
        else:
            $ missallaway_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if day <= 4:
            hide btn_classroom_day_missallaway_idle2
            show mis neutral_talk at right
        else:
            hide btn cafeoutside_day_missallaway_idle
            show misc neutral_talk at right
        with dissolve
        mis "These would go great with my laziness, thank you so much for these, [povname]."
    elif selecteditem.id ==  Items.socksclouds.id:
        if day == 0 or day == 4:
            $ missallaway_gift_like_level += 40
        elif day == 3:
            $ missallaway_gift_like_level += 35
        else:
            $ missallaway_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if day <= 4:
            hide btn_classroom_day_missallaway_idle2
            show mis neutral_talk at right
        else:
            hide btn cafeoutside_day_missallaway_idle
            show misc neutral_talk at right
        with dissolve
        mis "These are so cool, will the clouds make me high? Hahaha, I'm joking. Whaaaa-?!"
    elif selecteditem.id ==  Items.sockslightning.id:
        if day == 1 or day == 3:
            $ missallaway_gift_like_level += 40
        elif day == 2:
            $ missallaway_gift_like_level += 35
        else:
            $ missallaway_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if day <= 4:
            hide btn_classroom_day_missallaway_idle2
            show mis neutral_talk at right
        else:
            hide btn cafeoutside_day_missallaway_idle
            show misc neutral_talk at right
        with dissolve
        mis "Lightnight socks? And they're fluffy? I love them! Thanks so much, [povname]."
    elif selecteditem.id ==  Items.giftcardwebflix.id:
        $ missallaway_gift_like_level += 100
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if day <= 4:
            hide btn_classroom_day_missallaway_idle2
            show mis neutral_talk at right
        else:
            hide btn cafeoutside_day_missallaway_idle
            show misc neutral_talk at right
        with dissolve
        mis "A $100 Webflix giftcard?! Hell yeah! I can upgrade my plan to 4k streaming for 3 months. You shouldn't have~"
    # elif selecteditem.id ==  Items.coffeecapsulebox.id:
    #     $ missallaway_gift_like_level += 60
    #     $ inventory.drop(selecteditem)
    #     $ selecteditem = None
    #     show pov neutral at left
    #     with dissolve
    #     if day <= 4:
    #         show mis neutral_talk at right
    #     else:
    #         show misc neutral_talk at right
    #     with dissolve
    #     mis "More coffee capsule for my caffeine addiction, you are my hero."
    else:
        show pov embarrassed at left
        with dissolve
        if day <= 4:
            hide btn_classroom_day_missallaway_idle2
            show mis confused_talk at right
        else:
            hide btn cafeoutside_day_missallaway_idle
            show misc confused_talk at right
        with dissolve
        if day == 0 or day == 2:
            mis "Oh, [povname]. I can't accept that."
        elif day == 4 or day == 5:
            mis "[povname]. This doesn't look like your homework."
        else:
            mis "Uhm, [povname]. This is simply inappropriate."
        if day <= 4:
            show mis confused at right
        else:
            show misc confused at right
        pov "{i}Hmmm.. maybe she'd like something else.{/i}"
        $ selecteditem = None

        if gtime <= 1:
            jump lbl_classroom_day
        else:
            jump lbl_cafeoutside_day

    ##else:#incase selcted item is not non but item not in inventory
    ##    jump lbl_comicbookstore_day_setup

    if missallaway_points == 0 and missallaway_gift_like_level >= 20:
        if missallaway_path >= 1:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 1 and missallaway_gift_like_level >= 40:
        if missallaway_path >= 3:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 2 and missallaway_gift_like_level >= 60:
        if missallaway_path >= 5:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 3 and missallaway_gift_like_level >= 80:
        if missallaway_path >= 7:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 4 and missallaway_gift_like_level >= 100:
        if missallaway_path >= 9:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 5 and missallaway_gift_like_level >= 120:
        if missallaway_path >= 11:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 6 and missallaway_gift_like_level >= 140:
        if missallaway_path >= 13:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 7 and missallaway_gift_like_level >= 160:
        if missallaway_path >= 15:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 8 and missallaway_gift_like_level >= 180:
        if missallaway_path >= 18:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif missallaway_points == 9 and missallaway_gift_like_level >= 200:
        if missallaway_path >= 20:
            call lbl_missallaway_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    else:
        pov "{i}Our relationship doesn't seem to have changed just yet.{/i}"
        pov "{i}A few more gifts may help us move to the next step.{/i}"

    if gtime <= 1:
        jump lbl_classroom_day
    else:
        jump lbl_cafeoutside_day

label lbl_missallaway_giftgiving_success:
    $ missallaway_points += 1
    $ missallaway_gift_like_level = 0
    $ renpy.notify("Relationship with Miss Allaway Increased")
    pov "{i}I can feel us getting closer.{/i}"
    return
