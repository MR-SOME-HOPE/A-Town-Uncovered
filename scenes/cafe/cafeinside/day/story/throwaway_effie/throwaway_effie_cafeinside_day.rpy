## Throwaway Effie Cafe Inside Day Conversation ##
label lbl_cafeinside_day_effie:
## Main Story Conversation
    if main_story == 10:
        jump lbl_cafeinside_day_effie_free_drink
    elif main_story == 11:
        jump lbl_cafeinside_day_effie_meet_effie_house
    elif main_story == 33:
        jump lbl_cafeinside_day_effie_sexworld
    elif main_story == 84:
        pov "{i}I don't need to talk to her again, right now.{/i}"
        jump lbl_cafeinside_day

## Side Story Conversation
## No Event
    else:
        menu:
            "A job" if 16 <= main_story <= 21 and nextday_ajob == 0 and cafe_ajob == 0:
                jump lbl_cafeinside_day_effie_job
            "Sweet talk":
                jump lbl_cafeinside_day_effie_sweettalk
            "Have some fun later" if not main_story == 20:
                jump lbl_cafeinside_day_effie_funlater
            "Talk":
                jump lbl_cafeinside_day_effie_convo
            "Give Gift" if selecteditem != None:
                jump lbl_effie_giftgiving
            "Office Coffee Orders" if on_coffee_run_blocking and not bought_coffee_run_drinks:
                jump lbl_get_coffee_from_cafe
            "Ask Effie about Modeling"if hitomi_path == 14:
                jump lbl_modelling_requests_part2
            "Nevermind.":
                jump lbl_cafeinside_day

label lbl_cafeinside_day_effie_convo:
## 1 - 4 is classroom exclusive
## 5 - 8 is cafe exclusive
## 9 - 12 is park exclusive
## 13 - 15 is interchangable
    if date == 5 or date == 16 or date == 29:
        jump lbl_cafeinside_day_effie_5
    elif date == 10 or date == 11 or date == 30:
        jump lbl_cafeinside_day_effie_6
    elif date == 6 or date == 21:
        jump lbl_cafeinside_day_effie_7
    elif date == 8 or date == 17 or date == 22:
        jump lbl_cafeinside_day_effie_8
    elif date == 9 or date == 20:
        jump lbl_cafeinside_day_effie_5
    elif date == 7 or date == 18 or date == 24:
        jump lbl_cafeinside_day_effie_6
    elif date == 1 or date == 19 or date == 25:
        jump lbl_cafeinside_day_effie_7
    elif date == 2 or date == 14 or date == 26:
        jump lbl_cafeinside_day_effie_8
    elif date == 4 or date == 12 or date == 27:
        jump lbl_town_day_effie_13
    elif date == 3 or date == 15 or date == 28:
        jump lbl_town_day_effie_14
    elif date == 13 or date == 23 or date == 0:
        jump lbl_town_day_effie_15

## Cafe Exclusive
label lbl_cafeinside_day_effie_5:
    show pov neutral_talk at left
    with dissolve
    show effw neutral at right
    call lbl_cafeinside_counter_check
    with dissolve

    pov "Hey, Effie. How's work going so far?"
    show pov neutral at left
    show effw neutral_talk
    eff "Oh, y'know. The usual regulars and some unregular faces."
    show pov neutral at left
    show effw neutral_talk
    eff "Can I get you anything?"
    show pov embarrassed_talk at left
    show effw confused
    pov "Mmm, not right now. Sorry."
    show effw smirk
    pov "I really just came to see a friendly face."
    show pov neutral at left
    show effw smirk_talk
    eff "Naww, how sweet. I guess I'll get back to work, can't really talk all day."

    jump lbl_cafeinside_day

label lbl_cafeinside_day_effie_6:
    show pov neutral_talk at left
    with dissolve
    show effw confused at right
    call lbl_cafeinside_counter_check
    with dissolve

    pov "Hola, Effe."
    show pov smirk at left
    show effw bored_talk at right
    eff "Ha. I see what you did there."
    show pov smirk_talk at left
    show effw bored at right
    pov "Do you have any tacos here?"
    show pov smirk at left
    show effw bored_talk at right
    eff "{i}*Sigh*{/i} For the millionth time. We don't sell tacos."
    show pov smirk_talk at left
    show effw bored at right
    pov "I'm just hoping that by consistently asking, it would eventually happen."
    show pov smirk at left
    show effw bored_talk at right
    eff "In your wet dreams, [povname]."

    jump lbl_cafeinside_day

label lbl_cafeinside_day_effie_7:
    show pov neutral at left
    with dissolve
    show effw neutral_talk at right
    call lbl_cafeinside_counter_check
    with dissolve

    eff "Good afternoon, sir. What can I- oh- it's just you."
    show pov confused_talk at left
    show effw smirk at right
    pov "Um- excuse me. I'm just as much as a 'sir' as the next dude."
    show pov bored at left
    show effw smirk_talk at right
    eff "Yeah, dude. Totally."
    show effw neutral_talk at right
    eff "Anyway, what can I get you today?"
    show pov smirk_talk at left
    show effw neutral at right
    pov "How about-"
    show pov shocked at left
    show effw bored_talk at right
    eff "And no, I'm not just going to give you my assignment to copy."
    show pov sad_talk at left
    show effw bored at right
    pov "... Tartare sauce..."

    jump lbl_cafeinside_day

label lbl_cafeinside_day_effie_8:
    show pov neutral at left
    with dissolve
    show effw neutral_talk at right
    call lbl_cafeinside_counter_check
    with dissolve

    eff "Hey, [povname]."
    show pov confused at left
    show effw smirk_talk at right
    eff "Making your rounds today?"
    show pov confused_talk at left
    show effw smirk at right
    pov "What do you mean?"
    show pov embarrassed at left
    show effw neutral_talk at right
    eff "Y'know, just running around town waiting for things to happen."
    show pov smirk_talk at left
    show effw bored at right
    pov "You can't find adventure if you don't go searching for it."
    show pov bored at left
    show effw smirk_talk at right
    eff "Thank you, Mr. Fortune Cookie. Would you like a coffee with that wisdom? That'd be $5."

    jump lbl_cafeinside_day
