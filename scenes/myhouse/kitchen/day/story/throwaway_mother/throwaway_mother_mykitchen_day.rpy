## Throwaway Mother Kitchen Day Conversation
label lbl_mykitchen_day_chalkboard:

label lbl_mykitchen_day_mother:

## Main Story Converstaion
    if main_story == 3:
        jump lbl_mykitchen_day_mother_wake_up_sister
    elif 28 <= main_story <= 34:
        show btn mykitchen_day_mother_idle
        if mykitchen_day_chalkboard == 1:
            show img mykitchen_day_chalkboard_1
        elif mykitchen_day_chalkboard == 2:
            show img mykitchen_day_chalkboard_2
        elif mykitchen_day_chalkboard == 3:
            show img mykitchen_day_chalkboard_3
        elif mykitchen_day_chalkboard == 4:
            show img mykitchen_day_chalkboard_4
        elif mykitchen_day_chalkboard == 5:
            show img mykitchen_day_chalkboard_5
        elif mykitchen_day_chalkboard == 6:
            show img mykitchen_day_chalkboard_6
        elif mykitchen_day_chalkboard == 7:
            show img mykitchen_day_chalkboard_7
        elif mykitchen_day_chalkboard == 8:
            show img mykitchen_day_chalkboard_8
        elif mykitchen_day_chalkboard == 9:
            show img mykitchen_day_chalkboard_9
        elif mykitchen_day_chalkboard == 10:
            show img mykitchen_day_chalkboard_10
        $ renpy.pause(0.001)
        jump lbl_mykitchen_day_mother_sexworld_0
    elif main_story == 69:
        jump lbl_mom_is_worried

    ## Side Story Conversations
    if mum_path == 4:
        jump lbl_mykitchen_day_mother_fixedpc_0
    elif mum_path == 6:
        if mompastsunset_attend == 2:
            jump lbl_mykitchen_day_mother_mompastsunset_2_0
        elif mompastsunset_attend == 0 or 4:
            jump lbl_mykitchen_day_mother_mompastsunset_1_0
    elif 29 <= sister_path <= 29.5:
        jump lbl_mykitchen_day_mother_sistergone
    else:
        show btn mykitchen_day_mother_idle
        if mykitchen_day_chalkboard == 1:
            show img mykitchen_day_chalkboard_1
        elif mykitchen_day_chalkboard == 2:
            show img mykitchen_day_chalkboard_2
        elif mykitchen_day_chalkboard == 3:
            show img mykitchen_day_chalkboard_3
        elif mykitchen_day_chalkboard == 4:
            show img mykitchen_day_chalkboard_4
        elif mykitchen_day_chalkboard == 5:
            show img mykitchen_day_chalkboard_5
        elif mykitchen_day_chalkboard == 6:
            show img mykitchen_day_chalkboard_6
        elif mykitchen_day_chalkboard == 7:
            show img mykitchen_day_chalkboard_7
        elif mykitchen_day_chalkboard == 8:
            show img mykitchen_day_chalkboard_8
        elif mykitchen_day_chalkboard == 9:
            show img mykitchen_day_chalkboard_9
        elif mykitchen_day_chalkboard == 10:
            show img mykitchen_day_chalkboard_10
        menu:
            "Talk":
                hide btn mykitchen_day_mother_idle
                jump lbl_mykitchen_day_mother_convo
            "Give Gift" if selecteditem != None:
                jump lbl_mum_giftgiving
            "Ask her out to a fancy dinner date" if mum_path == 25.1:
                hide btn mykitchen_day_mother_idle
                jump lbl_dinner_with_me_mom
            "You. Me. Dinner. Tonight." if mum_path == 26:
                if inventory.has_item(Items.suit):
                    hide btn mykitchen_day_mother_idle
                    jump lbl_dinner_date_with_mom_pre
                else:
                    pov "{i}I still need a suit.{/i}"
                    if gtime == 0:
                        call screen scr_mykitchen_day
                    else:
                        call screen scr_mylivingroom_day
            "Ask her for a quickie right now" if mum_path >= 27:
                hide btn mykitchen_day_mother_idle
                jump lbl_mom_kitchen_seat_fun
            "Wanna quick morning fuck? [sister] can join us." if mumsis_path >= 13:
                jump lbl_momxsisterxmc_bedroomfun
            "Nevermind":
                jump lbl_mykitchen_day

label lbl_mykitchen_day_mother_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if date == 1 or date == 19 or date == 30:
        jump lbl_mykitchen_day_mother_1
    elif date == 2 or date == 17 or date == 25:
        jump lbl_mykitchen_day_mother_2
    elif date == 3 or date == 11 or date == 28:
        if 27 <= sister_path <= 33:
            jump lbl_mykitchen_day_mother_2
        else:
            jump lbl_mykitchen_day_mother_3
    elif date == 4 or date == 14 or date == 27:
        jump lbl_mykitchen_day_mother_4
    elif date == 5 or date == 13 or date == 26:
        jump lbl_mykitchen_day_mother_5
    elif date == 6 or date == 15 or date == 24:
        jump lbl_myhouse_day_mother_11
    elif date == 7 or date == 18 or date == 23:
        jump lbl_myhouse_day_mother_12
    elif date == 8 or date == 20 or date == 29:
        if 27 <= sister_path <= 33:
            jump lbl_myhouse_day_mother_12
        else:
            jump lbl_myhouse_day_mother_13
    elif date == 9 or date == 16 or date == 21:
        jump lbl_myhouse_day_mother_14
    elif date == 10 or date == 12 or date == 22 or date == 31:
        if main_story >= 22:
            jump lbl_myhouse_day_mother_15
        else:
            jump lbl_myhouse_day_mother_14

## Morning Exclusive
label lbl_mykitchen_day_mother_1:
    if winc == 1:
        show pov neutral at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum neutral_talk at right
        with dissolve
        mum "Good morning, [povname]."
        show pov neutral_talk at left
        show mum neutral at right
        pov "Morning, Mom."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Have a great day today, okay? I love you."
        show pov neutral_talk at left
        show mum neutral at right
        pov "I love you too, Mom."

        jump lbl_mykitchen_day
    else:
        show pov neutral at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum neutral_talk at right
        with dissolve
        mum "Good morning, [povname]."
        show pov neutral_talk at left
        show mum neutral at right
        pov "Morning, [missus]."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Have a great day today, okay? I love you."
        show pov neutral_talk at left
        show mum neutral at right
        pov "I love you too, [missus]."

        jump lbl_mykitchen_day

label lbl_mykitchen_day_mother_2:
    if winc == 1:
        show pov neutral at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum neutral_talk at right
        with dissolve
        mum "Hey, honey."
        mum "Any plans for today?"
        show pov neutral_talk at left
        show mum neutral at right
        pov "No idea what I have in store. We'll see what life throws at me."
        show pov neutral at left
        show mum smirk_talk at right
        mum "Hmm, well alright, just be careful. I love you"
        show pov neutral_talk at left
        show mum smirk at right
        pov "Thanks, Mom. I love you too."

        jump lbl_mykitchen_day
    else:
        show pov neutral at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum neutral_talk at right
        with dissolve
        mum "Hey, honey."
        mum "Any plans for today?"
        show pov neutral_talk at left
        show mum neutral at right
        pov "No idea what I have in store. We'll see what life throws at me."
        show pov neutral at left
        show mum smirk_talk at right
        mum "Hmm, well alright, just be careful. I love you"
        show pov neutral_talk at left
        show mum smirk at right
        pov "Thanks, [missus]. I love you too."

        jump lbl_mykitchen_day

label lbl_mykitchen_day_mother_3:
    if winc == 1:
        show pov confused at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum angry_talk at right
        with dissolve
        mum "I told you to take out the trash last night."
        show pov confused_talk at left
        show mum angry at right
        pov "No you didn't. It was [sister]'s turn last night."
        show pov bored at left
        show mum embarrassed_talk at right
        mum "Oh. Right, wrong child."
        show pov bored_talk at left
        show mum embarrassed at right
        pov "Really, Mom?"
        show pov bored at left
        show mum embarrassed_talk at right
        mum "I love you."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "Love you too, Mom."

        jump lbl_mykitchen_day
    else:
        show pov confused at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum angry_talk at right
        with dissolve
        mum "I told you to take out the trash last night."
        show pov confused_talk at left
        show mum angry at right
        pov "No you didn't. It was [sister]'s turn last night."
        show pov bored at left
        show mum embarrassed_talk at right
        mum "Oh. Right, wrong [povdadrole]."
        show pov bored_talk at left
        show mum embarrassed at right
        pov "Really, [missus]?"
        show pov bored at left
        show mum embarrassed_talk at right
        mum "I love you."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "Love you too, [missus]."

        jump lbl_mykitchen_day

label lbl_mykitchen_day_mother_4:
    show pov neutral at left
    with dissolve
    hide btn mykitchen_day_mother_idle
    show mum neutral_talk at right
    with dissolve
    mum "Hey, sweetie. How was your sleep?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was alright, I guess."
    show pov shocked at left
    show mum smirk_talk at right
    mum "I heard you sleep talking."
    show pov confused_talk at left
    show mum smirk at right
    pov "I don't sleep talk."
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "I heard you calling my name. Must've been a nightmare."
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "Yeah... probably a nightmare. How embarrassing."

    jump lbl_mykitchen_day

label lbl_mykitchen_day_mother_5:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum neutral at right
        with dissolve
        pov "Morning, Mom."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Morning, honey."
        show pov neutral_talk at left
        show mum neutral at right
        pov "What's for breakfast."
        show pov sad at left
        show mum embarrassed_talk at right
        mum "Sorry, I didn't cook anything this morning."
        show pov embarrassed at left
        mum "You can make toast, cereal, heat up leftov-"
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "It's okay, I'm not that hungry."

        jump lbl_mykitchen_day
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn mykitchen_day_mother_idle
        show mum neutral at right
        with dissolve
        pov "Morning, [missus]."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Morning, honey."
        show pov neutral_talk at left
        show mum neutral at right
        pov "What's for breakfast."
        show pov sad at left
        show mum embarrassed_talk at right
        mum "Sorry, I didn't cook anything this morning."
        show pov embarrassed at left
        mum "You can make toast, cereal, heat up leftov-"
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "It's okay, I'm not that hungry."

        jump lbl_mykitchen_day

## Interchangable in the Kitchen and Living Room

label lbl_myhouse_day_mother_11:
    show pov bored at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    hide btn mykitchen_day_mother_idle
    show mum smirk_talk at right
    with dissolve
    mum "Hey, [povname]. I've got a joke for you."
    show pov bored_talk at left
    show mum shocked at right
    pov "Is this about the horse that walks into a bar?"
    show pov bored at left
    mum "..."
    show pov bored_talk at left
    show mum embarrassed at right
    pov "You've told me that joke 100 times already."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "It's a good joke, isn't it?"
    show pov bored_talk at left
    show mum smirk at right
    pov "The best."

    jump lbl_myhouse_day_mother_end

label lbl_myhouse_day_mother_12:
    show pov neutral at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    hide btn mykitchen_day_mother_idle
    show mum neutral_talk at right
    with dissolve
    mum "I heard it's going to pour with rain tonight."
    show pov neutral_talk at left
    show mum neutral at right
    pov "It always rains at night."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "It's soothing, isn't it?"
    show mum confused_talk at right
    mum "Weird how it all dries by morning though."
    show pov neutral_talk at left
    show mum neutral at right
    pov "I guess it's just one of this town's unique traits."

    jump lbl_myhouse_day_mother_end

label lbl_myhouse_day_mother_13:
    show pov confused_talk at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    hide btn mykitchen_day_mother_idle
    show mum confused at right
    with dissolve
    pov "Have you seen [sister]?"
    show pov confused at left
    show mum embarrassed_talk at right
    mum "I haven't. Honestly, she could be out or in her room."
    mum "I've been a bit occupied to notice."
    show pov confused_talk at left
    show mum bored at right
    pov "Shouldn't you be keeping an eye on her."
    show pov embarrassed at left
    show mum bored_talk at right
    mum "I've done that for the past 18 years, honey."
    show mum smirk_talk at right
    mum "I think it's time I get a break."

    jump lbl_myhouse_day_mother_end

label lbl_myhouse_day_mother_14:
    show pov neutral_talk at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    hide btn mykitchen_day_mother_idle
    show mum neutral at right
    with dissolve
    pov "How's your day going?"
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "Oh, that's sweet of you to ask. I'm doing well."
    mum "Yourself?"
    show pov bored_talk at left
    show mum smirk at right
    pov "Eh, just trying to occupy myself."
    show pov bored at left
    show mum smirk_talk at right
    mum "You could do some chores."
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "...Actually, I've just remembered I have to... go.."

    jump lbl_myhouse_day_mother_end

label lbl_myhouse_day_mother_15:
    if winc == 1:
        show pov bored at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        hide btn mykitchen_day_mother_idle
        show mum smirk_talk at right
        with dissolve
        mum "How's work, my big baby?"
        show pov bored_talk at left
        show mum neutral at right
        pov "Please don't call me a big baby, Mom."
        show pov bored_talk at left
        show mum neutral at right
        pov "Work's fine."
        show pov bored at left
        show mum neutral_talk at right
        mum "I saw you working hard a few days ago."
        show mum smirk_talk at right
        mum "That pink looks great on you. I love a man in pink."
        show pov bored_talk at left
        show mum smirk at right
        pov "Thanks.. Mom."

        jump lbl_myhouse_day_mother_end
    else:
        show pov bored at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        hide btn mykitchen_day_mother_idle
        show mum smirk_talk at right
        with dissolve
        mum "How's work, poopy bottom?"
        show pov bored_talk at left
        show mum neutral at right
        pov "Please don't call me a poopy bottom, [missus]."
        show pov bored_talk at left
        show mum neutral at right
        pov "Work's fine."
        show pov bored at left
        show mum neutral_talk at right
        mum "I saw you working hard a few days ago."
        show mum smirk_talk at right
        mum "That pink looks great on you. I love a man in pink."
        show pov bored_talk at left
        show mum smirk at right
        pov "Thanks.. [missus]."

        jump lbl_myhouse_day_mother_end

label lbl_myhouse_day_mother_end:
    if gtime == 0:
        jump lbl_mykitchen_day
    else:
        jump lbl_mylivingroom_day

## GIFT GIVING
label lbl_mum_giftgiving:
    ##if inventory.has_item(selecteditem):
        ##if mumAcceptedItems():
    if selecteditem.id ==  Items.flowerlilies.id:
        if day == 2 or day == 4:
            $ mum_gift_like_level += 95
        elif day == 3:
            $ mum_gift_like_level += 85
        else:
            $ mum_gift_like_level += 90
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum embarrassed_talk at right
        with dissolve
        mum "Nawww, honey. These look amazing. Thank you."
    elif selecteditem.id ==  Items.flowerroses.id:
        if day == 0 or day == 2:
            $ mum_gift_like_level += 45
        elif day == 4:
            $ mum_gift_like_level += 35
        else:
            $ mum_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum embarrassed_talk at right
        with dissolve
        mum "Awwww, baby. I love you so much. You just made my day."
    elif selecteditem.id ==  Items.flowersunflowers.id:
        if day == 1 or day == 6:
            $ mum_gift_like_level += 45
        elif day == 0:
            $ mum_gift_like_level += 35
        else:
            $ mum_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum embarrassed_talk at right
        with dissolve
        mum "Sunflowers~? Sweetie, you shouldn't have. They smell beautiful."
    elif selecteditem.id ==  Items.redwine.id:
        if day == 1 or day == 6:
            $ mum_gift_like_level += 105
        elif day == 0 or day == 3:
            $ mum_gift_like_level += 95
        else:
            $ mum_gift_like_level += 100
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum smirk_talk at right
        with dissolve
        mum "What's the special ocassion, honey? Hehehe, thanks so much for this. We were definitely running low."
    elif selecteditem.id ==  Items.whitewine.id:
        if day == 0 or day == 4:
            $ mum_gift_like_level += 105
        elif day == 2 or day == 6:
            $ mum_gift_like_level += 95
        else:
            $ mum_gift_like_level += 100
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum smirk_talk at right
        with dissolve
        mum "I was craving a nice glass of wine. You are the best, don't tell [sister]. Hehehe~"
    elif selecteditem.id ==  Items.icecream1.id:
        if day == 0 or day == 1:
            $ mum_gift_like_level += 30
        elif day == 2:
            $ mum_gift_like_level += 20
        else:
            $ mum_gift_like_level += 25
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum neutral_talk at right
        with dissolve
        mum "Is this triple fudge delight? Ooh you're spoiling me today."
    elif selecteditem.id ==  Items.icecream2.id:
        if day == 2 or day == 3:
            $ mum_gift_like_level += 30
        elif day == 4:
            $ mum_gift_like_level += 20
        else:
            $ mum_gift_like_level += 25
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum neutral_talk at right
        with dissolve
        mum "Is this rare velvet? Fancy~ Gimme-gimme!."
    elif selecteditem.id ==  Items.icecream3.id:
        if day == 5 or day == 6:
            $ mum_gift_like_level += 30
        elif day == 0:
            $ mum_gift_like_level += 20
        else:
            $ mum_gift_like_level += 25
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum neutral_talk at right
        with dissolve
        mum "Is this creme fatale? I guess today's my cheat day."
    elif selecteditem.id ==  Items.icecream4.id:
        if day == 4 or day == 5:
            $ mum_gift_like_level += 45
        elif day == 1:
            $ mum_gift_like_level += 35
        else:
            $ mum_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show mum neutral_talk at right
        with dissolve
        mum "I have no idea what flavour this is but I love it. Thank you, honeybum."
    else:
        show pov embarrassed at left
        with dissolve
        show mum embarrassed_talk at right
        with dissolve
        if day == 1 or day == 4:
            mum "Naww, honey. You don't have to give me that."
        elif day == 2 or day == 5:
            mum "Baby, we have enough random stuff in the house."
        else:
            mum "That's thoughtful, bubby. But I don't really want that."
        show mum embarrassed at right
        pov "{i}Hmmm.. maybe she'd like something else.{/i}"
        $ selecteditem = None

        if gtime == 0:
            jump lbl_mykitchen_day
        elif gtime == 1:
            jump lbl_mylivingroom_day
        else:
            jump lbl_parentsbedroom_night

    ##else:#incase selcted item is not non but item not in inventory
    ##    jump lbl_comicbookstore_day_setup

    if mum_points == 0 and mum_gift_like_level >= 20:
        if mum_path >= 1:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 1 and mum_gift_like_level >= 40:
        if mum_path >= 3:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 2 and mum_gift_like_level >= 60:
        if mum_path >= 5:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 3 and mum_gift_like_level >= 80:
        if mum_path >= 7:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 4 and mum_gift_like_level >= 100:
        if mum_path >= 9:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 5 and mum_gift_like_level >= 120:
        if mum_path >= 11:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 6 and mum_gift_like_level >= 140:
        if mum_path >= 15:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 7 and mum_gift_like_level >= 160:
        if mum_path >= 19:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 8 and mum_gift_like_level >= 180:
        if mum_path >= 22:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif mum_points == 9 and mum_gift_like_level >= 200:
        if mum_path >= 25:
            call lbl_mum_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    else:
        pov "{i}Our relationship doesn't seem to have changed just yet.{/i}"
        pov "{i}A few more gifts may help us move to the next step.{/i}"

    if gtime == 0:
        jump lbl_mykitchen_day
    elif gtime == 1:
        jump lbl_mylivingroom_day
    else:
        jump lbl_parentsbedroom_night

label lbl_mum_giftgiving_success:
    $ mum_points += 1
    $ mum_gift_like_level = 0
    if winc == 1:
        $ renpy.notify("Relationship with Mom Increased")
    else:
        $ renpy.notify("Relationship with Missus Increased")
    pov "{i}I can feel us getting closer.{/i}"
    return
