## Throwaway Edward Schoolyard Day Conversation ##
label lbl_schoolyard_day_edward:
    default edward_vr_path = 1#TEMP 0
    ## Main Story
    ## Sexworld Talk
    if main_story <= 40 and insexworld == 1:
        jump lbl_schoolyard_day_edward_sexworld
    ## Investigation Edward
    elif main_story == 84:
        jump lbl_investigations_edward
    ## Edward's Advice
    elif main_story in (87,88,89):
        jump lbl_edwards_advice

    ## NO EVENT
    else:
        show btn schoolyard_day_edward_idle
        $ renpy.pause(0.001)

        if 1 <= edward_vr_path <= 5:
            if edward_vr_path == 2:
                if not inventory.has_item(Items.vrheadset):
                    pov "{i}I still need to fork out the money for the VR Headset from the mall.{/i}"
                elif inventory.has_item(Items.vrheadset):
                    jump lbl_vr_buds
            elif edward_vr_path == 3:
                edw "Hey man, I'm still working on the device. Check back later on."
            elif edward_vr_path == 4:
                edw "Almost done modding the device. Check back soon."
            elif edward_vr_path == 5:
                jump lbl_memories_of_a_virtual_reality

            else:
                menu:
                    "Virtual Reality" if edward_vr_path == 1:
                        jump lbl_snap_back_to_virtual_reality
                    "Talk":
                        pass

        #if inventory.has_item(Items.vrheadset):
        #    jump lbl_schoolyard_day_edward_headsetmod
        #else:
        jump lbl_schoolyard_day_edward_convo

label lbl_schoolyard_day_edward_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is night exclusive
## 11 - 15 is interchangeable

    if date == 3 or date == 14 or date == 23:
        jump lbl_schoolyard_day_edward_1
    elif date == 2 or date == 11 or date == 28:
        jump lbl_schoolyard_day_edward_2
    elif date == 1 or date == 15 or date == 22:
        jump lbl_schoolyard_day_edward_3
    elif date == 6 or date == 12 or date == 26:
        jump lbl_schoolyard_day_edward_4
    elif date == 5 or date == 16 or date == 21:
        jump lbl_schoolyard_day_edward_5
    elif date == 4 or date == 13 or date == 29:
        jump lbl_town_both_edward_11
    elif date == 10 or date == 20 or date == 27:
        jump lbl_town_both_edward_12
    elif date == 8 or date == 19 or date == 24:
        jump lbl_town_both_edward_13
    elif date == 7 or date == 18 or date == 30:
        jump lbl_town_both_edward_14
    elif date == 9 or date == 17 or date == 25 or date == 31:
        jump lbl_town_both_edward_15

## Morning Exclusive #######################################
label lbl_schoolyard_day_edward_1:
    show pov smirk_talk at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused at right
    with dissolve
    pov "Hey, Edward, how's it hanging?"
    show pov neutral at left
    show edw neutral_talk at right
    edw "Oh, morning, [povname]."
    show pov confused at left
    show edw confused_talk at right
    edw "Just waiting for my chance to get my readings device from the teacher."
    show edw angry_talk at right
    edw "They took it yesterday thinking it was a drone and I'm trying to get it back to set it up again."
    show pov confused_talk at left
    show edw shocked at right
    pov "Why did they think it was a drone?"
    show pov confused at left
    show edw bored_talk at right
    edw "I have to build them like one."
    show edw angry_talk at right
    edw "Nowadays, if an adult finds you with any sort of equipment that doesn't have wheels, a propeller or a speaker-"
    show pov shocked at left
    show edw bored_talk at right
    edw "You end up with a bomb squad in the area and your photo on a government watchlist."
    show pov embarrassed_talk at left
    show edw angry at right
    pov "Rough. Sorry to hear that."

    jump lbl_schoolyard_day

label lbl_schoolyard_day_edward_2:
    show pov confused at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused_talk at right
    with dissolve
    edw "Hey, [povname]. Have you got any magnets on you?"
    show pov bored_talk at left
    show edw sad at right
    pov "I must have left all my magnets in my other jeans, sorry."
    show pov confused at left
    show edw angry_talk at right
    edw "Drats: it's just that some of my devices seem to go a bit wild whenever they get your readings."
    show pov confused_talk at left
    show edw bored at right
    pov "What are they supposed to measure again?"
    show pov bored at left
    show edw bored_talk at right
    edw "A variety of things - mostly anomalies."
    show pov bored_talk at left
    show edw sad at right
    pov "I may be guessing, but maybe it's just faulty."

    jump lbl_schoolyard_day

label lbl_schoolyard_day_edward_3:
    show pov confused_talk at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw neutral at right
    with dissolve
    pov "Hey, man, what are you up to?"
    show pov bored at left
    show edw neutral_talk at right
    edw "Going around university, collecting all the readings for today."
    show pov bored_talk at left
    show edw neutral at right
    pov "How's that coming along?"
    show pov confused at left
    show edw smirk_talk at right
    edw "It's good, haven't collected the readings from the device from the girl's bathroom yet."
    show pov confused_talk at left
    show edw embarrassed at right
    pov "You get a lot of readings from that one?"
    show pov bored at left
    show edw embarrassed_talk at right
    edw "No, but I do get the beating of a lifetime if I get caught."
    show pov bored_talk at left
    show edw neutral at right
    pov "And you still use that spot?"
    show pov bored at left
    show edw smirk_talk at right
    edw "I like adding the extra excitement to the routine, you know?"

    jump lbl_schoolyard_day

label lbl_schoolyard_day_edward_4:
    show pov smirk_talk at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused at right
    with dissolve
    pov "Hey, Edward, how's it hanging?"
    show pov neutral at left
    show edw neutral_talk at right
    edw "Oh, morning, [povname]."
    show pov confused at left
    show edw confused_talk at right
    edw "Just waiting for my chance to get my readings device from the teacher."
    show edw angry_talk at right
    edw "They took it yesterday thinking it was a drone and I'm trying to get it back to set it up again."
    show pov confused_talk at left
    show edw shocked at right
    pov "Why did they think it was a drone?"
    show pov confused at left
    show edw bored_talk at right
    edw "I have to build them like one."
    show edw angry_talk at right
    edw "Nowadays, if an adult finds you with any sort of equipment that doesn't have wheels, a propeller or a speaker-"
    show pov shocked at left
    show edw bored_talk at right
    edw "You end up with a bomb squad in the area and your photo on a government watchlist."
    show pov embarrassed_talk at left
    show edw angry at right
    pov "Rough. Sorry to hear that."

    jump lbl_schoolyard_day

label lbl_schoolyard_day_edward_5:
    show pov smirk_talk at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused at right
    with dissolve
    pov "Hey, Edward, how's it hanging?"
    show pov neutral at left
    show edw neutral_talk at right
    edw "Oh, morning, [povname]."
    show pov confused at left
    show edw confused_talk at right
    edw "Just waiting for my chance to get my readings device from the teacher."
    show edw angry_talk at right
    edw "They took it yesterday thinking it was a drone and I'm trying to get it back to set it up again."
    show pov confused_talk at left
    show edw shocked at right
    pov "Why did they think it was a drone?"
    show pov confused at left
    show edw bored_talk at right
    edw "I have to build them like one."
    show edw angry_talk at right
    edw "Nowadays, if an adult finds you with any sort of equipment that doesn't have wheels, a propeller or a speaker-"
    show pov shocked at left
    show edw bored_talk at right
    edw "You end up with a bomb squad in the area and your photo on a government watchlist."
    show pov embarrassed_talk at left
    show edw angry at right
    pov "Rough. Sorry to hear that."

    jump lbl_schoolyard_day

## Interchangablee #######################################
label lbl_town_both_edward_11: ##
    show pov confused at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused_talk at right
    with dissolve
    edw "Hey, [povname]. Have you got any magnets on you?"
    show pov bored_talk at left
    show edw sad at right
    pov "I must have left all my magnets in my other jeans, sorry."
    show pov confused at left
    show edw angry_talk at right
    edw "Drats, it's just that some of my devices seem to go a bit wild whenever they get your readings."
    show pov confused_talk at left
    show edw bored at right
    pov "What are they supposed to measure again?"
    show pov bored at left
    show edw bored_talk at right
    edw "A variety of things, mostly anomalies."
    show pov bored_talk at left
    show edw sad at right
    pov "I may be guessing but maybe it's just faulty."

    jump lbl_town_both_edward_end

label lbl_town_both_edward_12: ##
    show pov confused at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused_talk at right
    with dissolve
    edw "Hey, [povname]. Have you got any magnets on you?"
    show pov bored_talk at left
    show edw sad at right
    pov "I must have left all my magnets in my other jeans, sorry."
    show pov confused at left
    show edw angry_talk at right
    edw "Drats, it's just that some of my devices seem to go a bit wild whenever they get your readings."
    show pov confused_talk at left
    show edw bored at right
    pov "What are they supposed to measure again?"
    show pov bored at left
    show edw bored_talk at right
    edw "A variety of things, mostly anomalies."
    show pov bored_talk at left
    show edw sad at right
    pov "I may be guessing but maybe it's just faulty."

    jump lbl_town_both_edward_end

label lbl_town_both_edward_13: ##
    show pov confused at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused_talk at right
    with dissolve
    edw "Hey, [povname]. Have you got any magnets on you?"
    show pov bored_talk at left
    show edw sad at right
    pov "I must have left all my magnets in my other jeans, sorry."
    show pov confused at left
    show edw angry_talk at right
    edw "Drats, it's just that some of my devices seem to go a bit wild whenever they get your readings."
    show pov confused_talk at left
    show edw bored at right
    pov "What are they supposed to measure again?"
    show pov bored at left
    show edw bored_talk at right
    edw "A variety of things, mostly anomalies."
    show pov bored_talk at left
    show edw sad at right
    pov "I may be guessing but maybe it's just faulty."

    jump lbl_town_both_edward_end

label lbl_town_both_edward_14: ##
    show pov confused at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused_talk at right
    with dissolve
    edw "Hey, [povname]. Have you got any magnets on you?"
    show pov bored_talk at left
    show edw sad at right
    pov "I must have left all my magnets in my other jeans, sorry."
    show pov confused at left
    show edw angry_talk at right
    edw "Drats, it's just that some of my devices seem to go a bit wild whenever they get your readings."
    show pov confused_talk at left
    show edw bored at right
    pov "What are they supposed to measure again?"
    show pov bored at left
    show edw bored_talk at right
    edw "A variety of things, mostly anomalies."
    show pov bored_talk at left
    show edw sad at right
    pov "I may be guessing but maybe it's just faulty."

    jump lbl_town_both_edward_end

label lbl_town_both_edward_15: ##
    show pov confused at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw confused_talk at right
    with dissolve
    edw "Hey, [povname]. Have you got any magnets on you?"
    show pov bored_talk at left
    show edw sad at right
    pov "I must have left all my magnets in my other jeans, sorry."
    show pov confused at left
    show edw angry_talk at right
    edw "Drats, it's just that some of my devices seem to go a bit wild whenever they get your readings."
    show pov confused_talk at left
    show edw bored at right
    pov "What are they supposed to measure again?"
    show pov bored at left
    show edw bored_talk at right
    edw "A variety of things, mostly anomalies."
    show pov bored_talk at left
    show edw sad at right
    pov "I may be guessing but maybe it's just faulty."

    jump lbl_town_both_edward_end

label lbl_town_both_edward_end:
    if gtime == 0:
        jump lbl_schoolyard_day
    else:
        jump lbl_beachbehindrocks_night
