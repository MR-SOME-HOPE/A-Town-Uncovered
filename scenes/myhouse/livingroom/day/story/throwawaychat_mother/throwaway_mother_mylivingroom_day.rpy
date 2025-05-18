## Throwaway Mother Living Room Day Conversation

label lbl_mylivingroom_day_mother:

## Main Story Conversation
    if 28 <= main_story <= 34:
        jump lbl_mykitchen_day_mother_sexworld_1

## Mother Side Story:
    if mum_path == 4:
        jump lbl_mykitchen_day_mother_fixedpc_1
    elif mum_path == 6:
        if mompastsunset_attend == 2:
            jump lbl_mylivingroom_day_mother_mompastsunset_2_1
        elif mompastsunset_attend == 0 or 4:
            jump lbl_mylivingroom_day_mother_mompastsunset_1_1
    elif mum_path >= 18:
        show btn_mylivingroom_day_mother_idle2
        if sister_path == 24 and not (day == 2 and gtime == 1):
            show btn_mylivingroom_day_sister_idle2
        menu:
            "Talk":
                jump lbl_mylivingroom_day_mother_convo
            "Give Gift" if selecteditem != None:
                jump lbl_mum_giftgiving
            "Ask her if she wants to hang out in the livingroom tonight":
                jump lbl_mom_past_sunset_again_pre
            "Ask her out to the cinema" if moviedate == 0:
                jump lbl_ask_mom_to_cinema
            "Ask her out to a fancy dinner date" if mum_path == 25:
                jump lbl_dinner_with_me_mom
            "You. Me. Dinner. Tonight." if mum_path == 26:
                if inventory.has_item(Items.suit):
                    jump lbl_dinner_date_with_mom_pre
                else:
                    pov "{i}I still need a suit.{/i}"
                    call screen scr_mykitchen_day
            "Can I get a BJ with you and [sister]?" if mumsis_path >= 13:
                jump lbl_momxsisterxmc_doublebj
            "Can we have some fun with you and [sister]?" if mumsis_path >= 13:
                jump lbl_momxsisterxmc_69doggy
            "Talk about the Internship"if main_story in (87,88,89):
                jump lbl_moms_help
            "Nevermind":
                jump lbl_mylivingroom_day
    else:
        jump lbl_mylivingroom_day_mother_convo

label lbl_mylivingroom_day_mother_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if date == 3 or date == 18 or date == 25:
        jump lbl_mylivingroom_day_mother_6
    elif date == 5 or date == 16 or date == 24:
        jump lbl_mylivingroom_day_mother_7
    elif date == 7 or date == 19 or date == 27:
        jump lbl_mylivingroom_day_mother_8
    elif date == 9 or date == 13 or date == 29:
        jump lbl_mylivingroom_day_mother_9
    elif date == 1 or date == 20 or date == 30:
        jump lbl_mylivingroom_day_mother_10
    elif date == 4 or date == 14 or date == 22:
        jump lbl_myhouse_day_mother_11
    elif date == 2 or date == 17 or date == 21:
        jump lbl_myhouse_day_mother_12
    elif date == 10 or date == 19 or date == 23:
        if sister_path == 24 and not (day == 2 and gtime == 1):
            jump lbl_myhouse_day_mother_12
        else:
            jump lbl_myhouse_day_mother_13
    elif date == 8 or date == 12 or date == 22:
        jump lbl_myhouse_day_mother_14
    elif date == 6 or date == 11 or date == 26 or date == 0:
        if main_story >= 22:
            jump lbl_myhouse_day_mother_15
        else:
            jump lbl_myhouse_day_mother_13

## Afternoon Exclusive
label lbl_mylivingroom_day_mother_6:
    if winc == 1:
        show pov neutral at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral_talk at right
        with dissolve
        mum "What are you going to use the last remaining daylight for?"
        show pov bored_talk at left
        show mum neutral at right
        pov "I have absolutely no idea."
        show pov bored at left
        show mum neutral_talk at right
        mum "Well, you have the whole town to explore. Get your butt out there and do something."
        show pov neutral_talk at left
        show mum neutral at right
        pov "Alright alright. I'll see what I can find to do."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Love you, [povname]. Be safe!"
        show pov neutral_talk at left
        show mum neutral at right
        pov "Love you too, Mom."

        jump lbl_mylivingroom_day
    else:
        show pov neutral at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral_talk at right
        with dissolve
        mum "What are you going to use the last remaining daylight for?"
        show pov bored_talk at left
        show mum neutral at right
        pov "I have absolutely no idea."
        show pov bored at left
        show mum neutral_talk at right
        mum "Well, you have the whole town to explore. Get your butt out there and do something."
        show pov neutral_talk at left
        show mum neutral at right
        pov "Alright alright. I'll see what I can find to do."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Love you, [povname]. Be safe!"
        show pov neutral_talk at left
        show mum neutral at right
        pov "Love you too, [missus]."

        jump lbl_mylivingroom_day

label lbl_mylivingroom_day_mother_7:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum bored at right
        with dissolve
        pov "I'm hungry, what's for lunch?"
        show pov neutral at left
        show mum bored_talk at right
        mum "Are you going to constantly ask me what there is to eat?"
        show pov smirk_talk at left
        show mum bored at right
        pov "It's one of the things you signed when you gave birth to us."
        show pov smirk at left
        show mum bored_talk at right
        mum "If I knew that was in the contract, I would've kept you in."
        show pov smirk_talk at left
        show mum bored at right
        pov "Hah, funny. Serious thou-"
        show pov bored at left
        show mum bored_talk at right
        mum "Go cook some 2-minute noodles."

        jump lbl_mylivingroom_day
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum bored at right
        with dissolve
        pov "I'm hungry, what's for lunch?"
        show pov neutral at left
        show mum bored_talk at right
        mum "Are you going to constantly ask me what there is to eat?"
        show pov smirk_talk at left
        show mum bored at right
        pov "It's one of the things you signed when you signed the contract."
        show pov smirk at left
        show mum bored_talk at right
        mum "If I knew that was in the contract, I would've kept you in."
        show pov smirk_talk at left
        show mum bored at right
        pov "Hah, funny. Serious thou-"
        show pov bored at left
        show mum bored_talk at right
        mum "Go cook some 2-minute noodles."

        jump lbl_mylivingroom_day

label lbl_mylivingroom_day_mother_8:
    if winc == 1:
        show pov smirk_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "What's on TV."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Just my k-dramas."
        show pov neutral_talk at left
        show mum neutral at right
        pov "What's happening in it?"
        show pov bored at left
        show mum confused_talk at right
        mum "Shh, I can't talk and read subs at the same time."
        show pov bored_talk at left
        show mum neutral at right
        pov "...Cool, I'm just going to go get a tattoo, Mom."
        show pov bored at left
        show mum neutral_talk at right
        mum "Mhmm.. sure, yeah. That's nice, honey."

        jump lbl_mylivingroom_day
    else:
        show pov smirk_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "What's on TV."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Just my k-dramas."
        show pov neutral_talk at left
        show mum neutral at right
        pov "What's happening in it?"
        show pov bored at left
        show mum confused_talk at right
        mum "Shh, I can't talk and read subs at the same time."
        show pov bored_talk at left
        show mum neutral at right
        pov "...Cool, I'm just going to go get a tattoo, [missus]."
        show pov bored at left
        show mum neutral_talk at right
        mum "Mhmm.. sure, yeah. That's nice, honey."

        jump lbl_mylivingroom_day

label lbl_mylivingroom_day_mother_9:
    if winc == 1:
        show pov neutral at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral_talk at right
        with dissolve
        mum "Hey, honey. Want to sit with Mommy?"
        show pov smirk_talk at left
        show mum bored at right
        pov "Just wanted to stop by and see how you're doing."
        show pov neutral at left
        show mum bored_talk at right
        mum "Oh, well. I'm doing splendidly. Thanks for asking."
        show pov smirk_talk at left
        show mum bored at right
        pov "Cool, I'll be off."
        show pov neutral at left
        show mum bored_talk at right
        mum "Sure thing, don't stay up too late."
    else:
        show pov neutral at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral_talk at right
        with dissolve
        mum "Hey, honey. Want to sit with, [missus]?"
        show pov smirk_talk at left
        show mum bored at right
        pov "Just wanted to stop by and see how you're doing."
        show pov neutral at left
        show mum bored_talk at right
        mum "Oh, well. I'm doing splendidly. Thanks for asking."
        show pov smirk_talk at left
        show mum bored at right
        pov "Cool, I'll be off."
        show pov neutral at left
        show mum bored_talk at right
        mum "Sure thing, don't stay up too late."

    jump lbl_mylivingroom_day

label lbl_mylivingroom_day_mother_10:
    if winc == 1:
        show pov confused_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "Mom!"
        show pov confused at left
        show mum confused at right
        mum "Hmm?"
        show pov confused_talk at left
        show mum confused at right
        pov "Why do you have the TV up so loud?"
        show pov angry at left
        show mum confused_talk at right
        mum "What? Sorry, sweetie, I can't hear you."
        show pov bored_talk at left
        show mum neutral at right
        pov "Why is the T- nevermind!"
        show pov bored at left
        show mum neutral_talk at right
        mum "Alright, honey. Just don't get into trouble, okay?"

        jump lbl_mylivingroom_day
    else:
        show pov confused_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "[missus]!"
        show pov confused at left
        show mum confused at right
        mum "Hmm?"
        show pov confused_talk at left
        show mum confused at right
        pov "Why do you have the TV up so loud?"
        show pov angry at left
        show mum confused_talk at right
        mum "What? Sorry, sweetie, I can't hear you."
        show pov bored_talk at left
        show mum neutral at right
        pov "Why is the T- nevermind!"
        show pov bored at left
        show mum neutral_talk at right
        mum "Alright, honey. Just don't get into trouble, okay?"

        jump lbl_mylivingroom_day
