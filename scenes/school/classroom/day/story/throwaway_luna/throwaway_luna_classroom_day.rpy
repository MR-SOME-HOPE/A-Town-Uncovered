## Throwaway Luna Classroom Day Conversation ##
label lbl_classroom_day_luna:
    if insexworld == 0:
        scene bg classroom_day
    elif insexworld == 1:
        scene bg classroom_daysexworld

    if missallaway_path not in (3,4,13):
        show btn_classroom_day_missallaway_idle2
    show btn_classroom_day_luna_idle2
    $ renpy.pause(0.001)

    ## Main Story
    ## Sexworld Luna
    if main_story <= 40 and insexworld == 1:
        jump lbl_schoolhallway2_day_luna_sexworld
    ## Investigation Luna
    elif main_story == 84:
        jump lbl_investigations_luna
    ## Temp Tied Missionary Anal H-scene Option
    elif (day == 3 or day == 4):
        menu:
            "Talk":
                jump lbl_classroom_day_luna_convo
            "Have some fun":
                jump lbl_luna_tied_missionary_pre

## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
label lbl_classroom_day_luna_convo:
    if date == 8 or date == 19 or date == 27:
        jump lbl_classroom_day_luna_6
    elif date == 7 or date == 18 or date == 22:
        jump lbl_classroom_day_luna_7
    elif date == 9 or date == 18 or date == 24:
        jump lbl_classroom_day_luna_8
    elif date == 6 or date == 17 or date == 23:
        jump lbl_classroom_day_luna_9
    elif date == 5 or date == 15 or date == 26:
        jump lbl_classroom_day_luna_10
    elif date == 10 or date == 16 or date == 30:
        jump lbl_town_day_luna_11
    elif date == 4 or date == 20 or date == 25:
        jump lbl_town_day_luna_12
    elif date == 3 or date == 11 or date == 21:
        jump lbl_town_day_luna_13
    elif date == 2 or date == 17 or date == 28:
        jump lbl_town_day_luna_14
    elif date == 1 or date == 12 or date == 29 or date == 31:
        jump lbl_town_day_luna_15

## Afternoon Exclusive
label lbl_classroom_day_luna_6: ##
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_luna_idle2
    show lun neutral at right
    with dissolve
    pov "Good to see you in class, Luna."
    show pov confused at left
    show lun bored_talk at right
    lun "Is it, [povname]? Is it really? You like being here in class and seeing me here too, in class?"
    show pov bored_talk at left
    show lun bored at right
    pov "{i}*Sigh*{/i} No, I wish I was anywhere but here."
    show pov embarrassed at left
    show lun bored_talk at right
    lun "I wish I was at the graveyard, I have a few friends there."
    show pov embarrassed_talk at left
    show lun confused at right
    pov "Oh, I'm sorry."
    show pov embarrassed at left
    show lun bored_talk at right
    lun "Don't be sorry, it's life- or death. Anyway, they died decades ago, most of them at least."
    show pov confused_talk at left
    show lun confused at right
    pov "And they were your friends?"
    show pov embarrassed at left
    show lun bored at right
    lun "{i}Are{/i} my friends."

    jump lbl_classroom_day

label lbl_classroom_day_luna_7: ##
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_luna_idle2
    show lun neutral_talk at right
    with dissolve
    lun "Good Midday."
    show pov  at left
    show lun  at right
    pov "Hey, Luna. Did you do yesterday's homework."
    show pov  at left
    show lun  at right
    lun "Yup, why? You're not gonna ask me for answers are you?"
    lun "It's annoying how I have to do all the work and get nothing in return."
    show pov  at left
    show lun  at right
    pov "I'll give you answers to my homework next time."
    show pov  at left
    show lun  at right
    lun "Yeah, and vampires love garlic bread."
    lun "This isn't a fairy tale, [povname]. It's the real world."

    jump lbl_classroom_day

label lbl_classroom_day_luna_8: ##
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_luna_idle2
    show lun neutral at right
    with dissolve
    pov "Sup, Lunes."
    show pov  at left
    show lun  at right
    lun "Did you see the full moon last night."
    lun "It felt especially bright and beautiful."
    show pov  at left
    show lun  at right
    pov "Is that why you're glowing right now?"
    show pov  at left
    show lun  at right
    lun "Oh hush your face, [povname]."
    lun "But really~? That's so sweet of you. I'll make sure you have a safe trip home tonight."
    show pov  at left
    show lun  at right
    pov "I- why is that so ominous."

    jump lbl_classroom_day

label lbl_classroom_day_luna_9: ##
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_luna_idle2
    show lun neutral_talk at right
    with dissolve
    lun "I had a nightmare about you last night, [povname]. And I rarely have nightmares."
    show pov  at left
    show lun  at right
    pov "Did I die?"
    show pov  at left
    show lun  at right
    lun "No, but you were suffering, badly. And the scary part was that you were enjoying it."
    show pov  at left
    show lun  at right
    pov "That's kinda fucked."
    show pov  at left
    show lun  at right
    lun "No, kidding. Although it was titalating and the best dream I've had in a while."
    show pov  at left
    show lun  at right
    pov "Now was that really necessary? I didn't really wanna know my suffering was the best dream you've had in forever."
    show pov  at left
    show lun  at right
    lun "Sorry, but ughhh, thank you for such an {i}exciting{/i} dream."

    jump lbl_classroom_day

label lbl_classroom_day_luna_10: ##
    show pov neutral at left
    with dissolve
    hide btn_classroom_day_luna_idle2
    show lun neutral_talk at right
    with dissolve
    lun "Was I in your dream last night?"
    show pov shocked_talk at left
    show lun smirk at right
    pov "Not that I remember... why?"
    show pov confused at left
    show lun smirk_talk at right
    lun "I didn't have any dream last night and which is weird because I always have a dream."
    show pov smirk_talk at left
    show lun bored at right
    pov "Why would you think you were in mine?"
    show pov embarrassed at left
    show lun bored_talk at right
    lun "I'm just asking everyone really, I'm trying to figure out who I have to blame for such a boring night."
    show pov confused_talk at left
    show lun shocked at right
    pov "Have you tried Jacob? He's got a thing for Asian girls apparently."
    show pov smirk at left
    show lun angry_talk at right
    lun "That douchebag!"

    jump lbl_classroom_day
