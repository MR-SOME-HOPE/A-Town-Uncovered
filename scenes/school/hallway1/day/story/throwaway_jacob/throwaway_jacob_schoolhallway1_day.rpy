## Throwaway Jacob School Hallway 1 Day Conversation ##
label lbl_schoolhallway1_day_jacob:
    show btn schoolhallway1_day_jacob_idle
    $ renpy.pause(0.001)

    ## Main Story ##################
    ## Sexworld
    if main_story <= 35 and insexworld == 1:
        jump lbl_schoolhallway1_day_jacob_sexworld
    ## Hang at the Mall Now
    elif main_story == 75.5:
        menu:
            "Talk":
                jump lbl_schoolhallway1_day_jacob_convo
            "Hang at the Mall":
                jump lbl_hang_at_the_mall_now

    ## Hitomi Story ##################
    ## Awkwardness Between Bros
    elif hitomi_path == 8:
        jump lbl_awkwardness_between_bros
    ## Awkwardness Between Bros
    elif hitomi_path == 26:
        jump lbl_bros_before_hoes_part1

    ## Effie Story ##################
    elif effie_path == 3:
        jump lbl_brodacious_advice

    ## NO EVENT
    else:
        jump lbl_schoolhallway1_day_jacob_convo

label lbl_schoolhallway1_day_jacob_convo:
## 1 - 5 is morning exclusive (School Hallway 1)
## 6 - 10 is afternoon exclusive (Comic Book Store)
## 11 - 15 is interchangeable
    if date == 1 or date == 11 or date == 23:
        jump lbl_schoolhallway1_day_jacob_1
    elif date == 4 or date == 13 or date == 21:
        jump lbl_schoolhallway1_day_jacob_2
    elif date == 7 or date == 16 or date == 22:
        jump lbl_schoolhallway1_day_jacob_3
    elif date == 9 or date == 12 or date == 26:
        jump lbl_schoolhallway1_day_jacob_4
    elif date == 2 or date == 20 or date == 28:
        jump lbl_schoolhallway1_day_jacob_5
    elif date == 3 or date == 17 or date == 29:
        jump lbl_town_day_jacob_11
    elif date == 6 or date == 18 or date == 24:
        jump lbl_town_day_jacob_12
    elif date == 8 or date == 16 or date == 27:
        jump lbl_town_day_jacob_13
    elif date == 5 or date == 14 or date == 30:
        jump lbl_town_day_jacob_14
    elif date == 10 or date == 19 or date == 25 or date == 0:
        jump lbl_town_day_jacob_15

## Morning Exclusive
label lbl_schoolhallway1_day_jacob_1:
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    show jac neutral at right
    with dissolve
    pov "Hey, dude."
    show pov neutral at left
    show jac neutral_talk at right
    jac "Yo yo yo! You heading to class?"
    show pov confused_talk at left
    show jac confused at right
    pov "I'm heading somewhere."
    show pov embarrassed at left
    show jac confused_talk at right
    jac "You're always acting mysterious."
    show pov bored at left
    show jac smirk_talk at right
    jac "I like that. I should be more mysterious."

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_jacob_2:
    show pov neutral at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    show jac neutral_talk at right
    with dissolve
    jac "Sup, [povname]. How you been?"
    show pov neutral_talk at left
    show jac neutral at right
    pov "Can't complain I guess."
    show pov shocked at left
    show jac smirk_talk at right
    jac "Are you ready for the test today?"
    show pov shocked_talk at left
    show jac smirk at right
    pov "...What test?"
    show pov bored at left
    show jac neutral_talk at right
    jac "I'm just kidding, man. Hahaha, should've seen the look on your face."

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_jacob_3:
    show pov confused at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    show jac bored_talk at right
    with dissolve
    jac "Man, is school over yet?"
    show pov confused_talk at left
    show jac sad at right
    pov "It's still the morning."
    show pov bored at left
    show jac sad_talk at right
    jac "I just wanna go and check out the new issue of Hentai Weakly already."
    show pov bored_talk at left
    show jac sad at right
    pov "You.. can't wait a few more hours?"
    show pov shocked at left
    show jac bored_talk at right
    jac "I have a boner right now, ma dude. Don't stand too close."

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_jacob_4:
    show pov confused at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    show jac neutral_talk at right
    with dissolve
    jac "Did you hear what happened outside today?"
    show pov confused_talk at left
    show jac smirk at right
    pov "No? What happened?"
    show pov shocked at left
    show jac smirk_talk at right
    jac "Some dude got roundhouse kicked in the face for 'accidentally' falling over and grabbing a tit."
    show pov confused_talk at left
    show jac neutral at right
    pov "Was that the Weebo Knievo?"
    show pov neutral at left
    show jac neutral_talk at right
    jac "Yup. He didn't get enough time to do the 'gomen nazi' thing before her foot was in his face. Hahaha!"

    jump lbl_schoolhallway1_day

label lbl_schoolhallway1_day_jacob_5:
    show pov bored at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    show jac smirk_talk at right
    with dissolve
    jac "Did you see what Ms. Lashley was wearing today? I wanna get my John 3:16 inside her."
    show pov confused_talk at left
    show jac smirk at right
    pov "Doesn't she wear the same thing everyday?"
    show pov confused at left
    show jac smirk_talk at right
    jac "Don't we all."
    show pov embarrassed_talk at left
    show jac confused at right
    pov "I mean.. ocassionally I..."
    show pov bored at left
    show jac bored_talk at right
    jac "Oh, just quit it, Mr-I'm-So-Special."

    jump lbl_schoolhallway1_day

## Interchangable
label lbl_town_day_jacob_11:
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    hide btn_comicbookstore_day_jacob_idle2
    show jac neutral at right
    with dissolve
    pov "Hey, Jacob. How's your day going?"
    show pov neutral at left
    show jac smirk_talk at right
    jac "I haven't died yet."
    show pov neutral_talk at left
    show jac smirk at right
    pov "That's good."
    show pov embarrassed at left
    show jac bored_talk at right
    jac "I haven't gotten my dick wet either."
    show pov embarrassed_talk at left
    show jac shocked at right
    pov "..Uh..."
    show pov embarrassed at left
    show jac shocked_talk at right
    jac "TODAY! I meant, I haven't gotten my dick wet.. today!"
    show pov confused_talk at left
    show jac embarrassed at right
    pov "You don't have to defensively exclaim it out to everyone."

    jump lbl_town_day_jacob_end

label lbl_town_day_jacob_12:
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    hide btn_comicbookstore_day_jacob_idle2
    show jac neutral at right
    with dissolve
    pov "Whatcha doing, man?"
    show pov neutral at left
    show jac smirk_talk at right
    jac "Ah y'know. Just killing time... fighting crime."
    show pov bored at left
    jac "Hair sublime, doing just fine."
    show pov confused at left
    jac "Word to your mother, brother wanna fuck her-"
    show pov confused_talk at left
    show jac shocked at right
    pov "What did you say about my mother?"
    show pov bored at left
    show jac embarrassed_talk at right
    jac "Wh-what? I di- didn''t saying anything..."

    jump lbl_town_day_jacob_end

label lbl_town_day_jacob_13:
    show pov neutral_talk at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    hide btn_comicbookstore_day_jacob_idle2
    show jac smirk at right
    with dissolve
    pov "Decided what you're going to do for your end-of-year assignment?"
    show pov confused at left
    show jac smirk_talk at right
    jac "Hahaha, you're funny, man."
    show pov confused_talk at left
    show jac confused at right
    pov "I'm guessing you haven't even thought about it."
    show pov bored at left
    show jac confused_talk at right
    jac "Thought about what?"
    show pov bored_talk at left
    show jac neutral at right
    pov "The English assignment."
    show pov bored at left
    show jac neutral_talk at right
    jac "Hahaha.. you said 'ass' again."

    jump lbl_town_day_jacob_end

label lbl_town_day_jacob_14:
    show pov confused at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    hide btn_comicbookstore_day_jacob_idle2
    show jac smirk_talk at right
    with dissolve
    jac "Well, well, well, if it isn't the man himself."
    show pov confused_talk at left
    show jac smirk at right
    pov "What are you talking about?"
    show pov confused at left
    show jac smirk_talk at right
    jac "You know what I'm talking about, Mr. Hotshot."
    jac "Tell me, how was she last night? Tight? Freaky? Maybe awittle kink-ky?"
    show pov confused_talk at left
    show jac smirk at right
    pov "Who are you talking about?"
    show pov bored at left
    show jac embarrassed_talk at right
    jac "You know... her... that girl... with.. hair?"

    jump lbl_town_day_jacob_end

label lbl_town_day_jacob_15:
    show pov confused at left
    with dissolve
    hide btn schoolhallway1_day_jacob_show
    hide btn_comicbookstore_day_jacob_idle2
    show jac confused_talk at right
    with dissolve
    jac "Alright, answer me this."
    jac "If a cute, naked chick came out of your computer screen..."
    show jac smirk_talk at right
    jac "Do you think her pussy would be squishy and lifelike or sharp and pixelated."
    show pov smirk_talk at left
    show jac smirk at right
    pov "I'm guessing it depends on the quality of the video and your internet connection, am I right?"
    show pov neutral at left
    show jac bored_talk at right
    jac "[povname]... You're definitely the wisest person I know."

    jump lbl_town_day_jacob_end

label lbl_town_day_jacob_end:
    if gtime == 0 and day <= 4:
        jump lbl_schoolhallway1_day
    else:
        jump lbl_comicbookstore_day
