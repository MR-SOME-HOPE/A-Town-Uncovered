label lbl_classroom_day_effie:
## Throwaway Effie Classroom Day Conversation ##
    if insexworld == 0:
        scene bg classroom_day
    elif insexworld == 1:
        scene bg classroom_daysexworld

    if IsAllawayInClass():
        show btn_classroom_day_missallaway_idle2
## Main Story Conversation
    if 32 <= main_story <= 33:
        show btn_classroom_daysexworld_effie_idle2
        $ renpy.pause(0.001)
        jump lbl_classroom_day_effie_sexworld


## Side Story Conversation
    ## No Event
    else:
        show btn_classroom_day_effie_idle2
        $ renpy.pause(0.001)
        if main_story == 75.5:
            menu:
                "Talk":
                    jump lbl_classroom_day_effie_convo
                "Hang at the Mall":
                    $ hangatthemall_location = 1
                    jump lbl_hang_at_the_mall_now
                "Nevermind":
                    jump lbl_classroom_day
        else:
            menu:
                "Talk":
                    jump lbl_classroom_day_effie_convo
                "Give Gift" if selecteditem != None:
                    jump lbl_effie_giftgiving
                "Nothing":
                    jump lbl_classroom_day

label lbl_classroom_day_effie_convo:
## 1 - 4 is classroom exclusive
## 5 - 8 is cafe exclusive
## 9 - 12 is park exclusive
## 13 - 15 is interchangable
    if date == 1 or date == 20:
        jump lbl_classroom_day_effie_1
    elif date == 2 or date == 17 or date == 21:
        jump lbl_classroom_day_effie_2
    elif date == 5 or date == 18 or date == 23:
        jump lbl_classroom_day_effie_3
    elif date == 6 or date == 19 or date == 24:
        jump lbl_classroom_day_effie_4
    elif date == 9 or date == 14 or date == 25:
        jump lbl_classroom_day_effie_1
    elif date == 10 or date == 15 or date == 26:
        jump lbl_classroom_day_effie_2
    elif date == 16 or date == 30:
        jump lbl_classroom_day_effie_3
    elif date == 7 or date == 11 or date == 27:
        jump lbl_classroom_day_effie_4
    elif date == 3 or date == 12 or date == 28:
        jump lbl_town_day_effie_13
    elif date == 4 or date == 13 or date == 29:
        jump lbl_town_day_effie_14
    elif date == 8 or date == 22 or date == 31:
        jump lbl_town_day_effie_15

## Classroom Exclusive
label lbl_classroom_day_effie_1:
    show pov confused at left
    with dissolve
    hide btn_classroom_day_effie_idle2
    show eff neutral_talk at right
    with dissolve
    eff "Hey, [povname]. Just waiting for class to start."
    show pov smirk_talk at left
    show eff neutral at right
    pov "You're an eager one, aren't you?"
    show pov confused at left
    show eff smirk_talk at right
    eff "May as well try to get excited about it."
    eff "As they say, time flies when you have fun."
    show pov embarrassed at left
    eff "What's the point of moaning and groaning about it when it'll feel like hours?"
    show pov embarrassed_talk at left
    show eff bored at right
    pov "That logic sounds really unhealthy."

    jump lbl_classroom_day

label lbl_classroom_day_effie_2:
    show pov shocked at left
    with dissolve
    hide btn_classroom_day_effie_idle2
    show eff neutral_talk at right
    with dissolve
    eff "Morning, [povname]. Have you studied for the quuiz?"
    show pov shocked_talk at left
    show eff confused at right
    pov "Q-q-q-q-q-q-q-q-q-"
    pov "Quiz?!"
    show pov shocked at left
    show eff confused_talk at right
    eff "Don't hyperventilate like that, it's creepy and you might pass out."
    show pov shocked_talk at left
    show eff bored at right
    pov "What quiz?"
    show pov shocked at left
    show eff bored_talk at right
    eff "I feel like the hyperventilating panic is appropriate now."

    jump lbl_classroom_day

label lbl_classroom_day_effie_3:
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_effie_idle2
    show eff confused at right
    with dissolve
    pov "Hey, where's Jacob?"
    show pov confused at left
    show eff confused_talk at right
    eff "Wasn't he out in the hallway before you entered the classroom?"
    show pov confused_talk at left
    show eff confused at right
    pov "Oh? Was he? I must have missed him."
    show pov confused at left
    show eff embarrassed_talk at right
    eff "He gets that a lot."
    show pov confused_talk at left
    show eff smirk at right
    pov "What? Ignored?"
    show pov smirk at left
    show eff smirk_talk at right
    eff "Right on the nail."

    jump lbl_classroom_day

label lbl_classroom_day_effie_4:
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_effie_idle2
    show eff bored at right
    with dissolve
    pov "You look tired this morning, Effie."
    show pov shocked at left
    show eff bored_talk at right
    eff "You look like shit this morning, [povname]."
    show pov shocked_talk at left
    show eff bored at right
    pov "I-"
    show pov embarrassed_talk at left
    pov "Alright, I probably deserved that."
    show pov embarrassed at left
    show eff bored_talk at right
    eff "At least you're aware."
    show pov embarrassed_talk at left
    show eff bored at right
    pov "Sorry, you look great-"
    show pov shocked at left
    show eff angry_talk at right
    eff "Shove your tampon up your nose and stop being a little pussy."

    jump lbl_classroom_day

## Interchangable
label lbl_town_day_effie_13:
    if not gtime == 1:
        show pov neutral_talk at left
        with dissolve
        if gtime == 0:
            hide btn_classroom_day_effie_idle2
        show eff neutral at right
        with dissolve
        pov "Hey, Effie."
        show pov smirk_talk at left
        show eff confused at right
        pov "Do you by any chance have the notes from class-"
        show pov embarrassed at left
        show eff bored_talk at right
        eff "Hey, just because we're friends, doesn't mean I'm completely fine giving you my notes all the time."
        eff "The only thing that teaches you is that skipping class is okay."
        show pov embarrassed_talk at left
        show eff bored at right
        pov "Al-right... I'll go ask Jacob."
        show pov bored at left
        show eff smirk_talk at right
        eff "Yeah, because he's one to take notes. Good luck."
    else:
        show pov neutral_talk at left
        with dissolve
        show effw neutral at right
        call lbl_cafeinside_counter_check
        with dissolve

        pov "Hey, Effie."
        show pov smirk_talk at left
        show effw confused at right
        pov "Do you by any chance have the notes from class-"
        show pov embarrassed at left
        show effw bored_talk at right
        eff "Hey, just because we're friends, doesn't mean I'm completely fine giving you my notes all the time."
        eff "The only thing that teaches you is that skipping class is okay."
        show pov embarrassed_talk at left
        show effw bored at right
        pov "Al-right... I'll go ask Jacob."
        show pov bored at left
        show effw smirk_talk at right
        eff "Yeah, because he's one to take notes. Good luck."

    jump lbl_town_day_effie_end

label lbl_town_day_effie_14:
    if not gtime == 1:
        show pov embarrassed at left
        with dissolve
        if gtime == 0:
            hide btn_classroom_day_effie_idle2
        show eff sad_talk at right
        with dissolve
        eff "Man, I'm so frikkin' tired."
        show pov embarrassed_talk at left
        show eff confused at right
        pov "You {i}are{/i} a full-time university student with a part time job that you attend every- single- day."
        pov "It doesn't seem like you have a lot of down time."
        show pov embarrassed at left
        show eff confused_talk at right
        eff "I'll have down time when I'm dead."
        show pov embarrassed_talk at left
        show eff bored at right
        pov "Tsk- at this rate, you'll be dead from exhaustion."
        show pov embarrassed at left
        show eff bored_talk at right
        eff "Winners never sleep... much."
    else:
        show pov embarrassed at left
        with dissolve
        show effw sad_talk at right
        call lbl_cafeinside_counter_check
        with dissolve

        eff "Man, I'm so frikkin' tired."
        show pov embarrassed_talk at left
        show effw confused at right
        pov "You {i}are{/i} a full-time university student with a part time job that you attend every- single- day."
        pov "It doesn't seem like you have a lot of down time."
        show pov embarrassed at left
        show effw confused_talk at right
        eff "I'll have down time when I'm dead."
        show pov embarrassed_talk at left
        show effw bored at right
        pov "Tsk- at this rate, you'll be dead from exhaustion."
        show pov embarrassed at left
        show effw bored_talk at right
        eff "Winners never sleep... much."

    jump lbl_town_day_effie_end

label lbl_town_day_effie_15:
    if not gtime == 1:
        show pov smirk at left
        with dissolve
        if gtime == 0:
            hide btn_classroom_day_effie_idle2
        show eff smirk_talk at right
        with dissolve
        eff "What's gucc, guccifam?"
        show pov confused_talk at left
        show eff smirk at right
        pov "Dead-ass finna sleep."
        show pov embarrassed at left
        show eff embarrassed_talk at right
        eff "Lit. Lit."
        show pov confused at left
        show eff confused_talk at right
        eff "Low-key same. Wanna KMS."
        show pov bored_talk at left
        show eff bored at right
        pov "Hashtag such a mood."
        show pov bored at left
        show eff bored_talk at right
        eff "Fuck, we actually big-brained AF."
    else:
        show pov smirk at left
        with dissolve
        show effw smirk_talk at right
        call lbl_cafeinside_counter_check
        with dissolve

        eff "What's gucc, guccifam?"
        show pov confused_talk at left
        show effw smirk at right
        pov "Dead-ass finna sleep."
        show pov embarrassed at left
        show effw embarrassed_talk at right
        eff "Lit. Lit."
        show pov confused at left
        show effw confused_talk at right
        eff "Low-key same. Wanna KMS."
        show pov bored_talk at left
        show effw bored at right
        pov "Hashtag such a mood."
        show pov bored at left
        show effw bored_talk at right
        eff "Fuck, we actually big-brained AF."

    jump lbl_town_day_effie_end

## Redirect End
label lbl_town_day_effie_end:
    if gtime == 0:
        jump lbl_classroom_day
    elif gtime == 1:
        jump lbl_cafeinside_day
    elif gtime >= 2:
        jump lbl_park_night

## GIFT GIVING
label lbl_effie_giftgiving:
    ##if inventory.has_item(selecteditem):
        ##if effieAcceptedItems():
    #"Developer Note: Because Effie doesn't have an official side story yet, you may currently max out her stats to access the community-suggested H-scenes that she has available."
    if selecteditem.id == Items.hairbands.id:
        $ effie_gift_like_level += 20
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if gtime == 1:
            show effw neutral_talk at right
        else:
            show eff neutral_talk at right
        with dissolve
        eff "Ayee! Thanks, dude. My hairbands keep snapping, I got my mom's thick hair."
    elif selecteditem.id ==  Items.premiumchocnutsmix.id:
        $ effie_gift_like_level += 30
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if gtime == 1:
            show effw neutral_talk at right
        else:
            show eff neutral_talk at right
        with dissolve
        eff "Dude?! This is awesome, I can go through a bag of trail mix in one single study sesh."
    elif selecteditem.id ==  Items.essentialoilcitrus.id:
        if day == 4 or day == 5:
            $ effie_gift_like_level += 45
        elif day == 6:
            $ effie_gift_like_level += 35
        else:
            $ effie_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if gtime == 1:
            show effw neutral_talk at right
        else:
            show eff neutral_talk at right
        with dissolve
        eff "Did you know scents help trigger certain memories? I use citrus for remembering math shit."
    elif selecteditem.id ==  Items.essentialoilpeppermint.id:
        if day == 1 or day == 3:
            $ effie_gift_like_level += 45
        elif day == 2:
            $ effie_gift_like_level += 35
        else:
            $ effie_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if gtime == 1:
            show effw neutral_talk at right
        else:
            show eff neutral_talk at right
        with dissolve
        eff "Did you know scents help trigger certain memories? I use peppermint for remembering literature shit."
    elif selecteditem.id ==  Items.essentialoillavender.id:
        if day == 2 or day == 6:
            $ effie_gift_like_level += 45
        elif day == 1:
            $ effie_gift_like_level += 35
        else:
            $ effie_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if gtime == 1:
            show effw neutral_talk at right
        else:
            show eff neutral_talk at right
        with dissolve
        eff "Did you know scents help trigger certain memories? I use lavender for remembering humanities shit."
    else:
        show pov embarrassed at left
        with dissolve
        if gtime == 1:
            show effw embarrassed_talk at right
        else:
            show eff embarrassed_talk at right
        with dissolve
        if day == 1 or day == 4:
            eff "No thanks. Can't think of a use for that."
        elif day == 2 or day == 5:
            eff "I suggest giving that to someone else who wants it more."
        else:
            eff "Sorry, you're too kind but I don't wanna carry that around."
        if gtime == 1:
            show effw embarrassed at right
        else:
            show eff embarrassed at right
        pov "{i}Hmmm.. maybe she'd like something else.{/i}"
        $ selecteditem = None

        if gtime == 0 and day <= 4:
            jump lbl_classroom_day
        elif gtime == 1:
            jump lbl_cafeinside_day
        elif gtime >= 2:
            jump lbl_effiehouseoutside_night
        else:
            jump lbl_effiehouseoutside_day

    ##else:#incase selcted item is not non but item not in inventory
    ##    jump lbl_comicbookstore_day_setup

    if effie_points == 0 and effie_gift_like_level >= 20:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 1 and effie_gift_like_level >= 40:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 2 and effie_gift_like_level >= 60:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 3 and effie_gift_like_level >= 80:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 4 and effie_gift_like_level >= 100:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 5 and effie_gift_like_level >= 120:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 6 and effie_gift_like_level >= 140:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 7 and effie_gift_like_level >= 160:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 8 and effie_gift_like_level >= 180:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif effie_points == 9 and effie_gift_like_level >= 200:
        $ effie_points += 1
        $ effie_gift_like_level = 0
        $ renpy.notify("Relationship with Effie Increased")
        pov "{i}I can feel us getting closer.{/i}"
    else:
        pov "{i}Our relationship doesn't seem to have changed just yet.{/i}"
        pov "{i}A few more gifts may help us move to the next step.{/i}"

    if gtime == 0 and day <= 4:
        jump lbl_classroom_day
    elif gtime == 1:
        jump lbl_cafeinside_day
    elif gtime >= 2:
        jump lbl_effiehouseoutside_night
    else:
        jump lbl_effiehouseoutside_day
