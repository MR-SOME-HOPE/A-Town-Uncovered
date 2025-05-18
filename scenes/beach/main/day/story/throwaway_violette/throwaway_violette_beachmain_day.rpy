## Throwaway Violette Beach Day Conversation ##
label lbl_beachmain_day_violette:
    ## MAIN STORY
    ## Sex World
    if main_story == 33:
        jump lbl_beachmain_daysexworld_violette_1
    ## Buukakki Followers Are Everywhere
    # elif main_story == 151:
    #     jump lbl_buukakki_followers_are_everywhere_violette
    ## SIDE STORY
    ## Meet Violette
    elif violette_path == 1:
        if beach_naked == 1:
            jump lbl_meet_violette
        else:
            jump lbl_beachmain_day_violette_16
    elif beach_naked == 0:
        jump lbl_beachmain_day_violette_16
    ## Day One Lifeguard
    elif violette_path == 2:
        jump lbl_day_one_lifeguard
    ## Keeping it Consistent
    elif violette_path == 3:
        jump lbl_keeping_it_consistent
    ## A Hard Balancing Act
    elif violette_path == 5:
        jump lbl_a_hard_balancing_act
    ## A Health Scare
    elif violette_path == 6:
        jump lbl_a_health_scare
    ## Back to Lifeguard Business
    elif violette_path == 8:
        jump lbl_back_to_lifeguard_business
    ## The Last Training Session
    elif violette_path == 15:
        jump lbl_the_last_training_session
    ## NO EVENT
    else:
        show btn beachmain_day_chair_idle
        if beach_naked == 1:
            menu:
                "A job" if 16 <= main_story <= 21 and nextday_ajob == 0 and beach_ajob == 0:
                    hide btn beachmain_day_chair_idle
                    jump lbl_beachmain_day_violette_ajob
                "Talk":
                    hide btn beachmain_day_chair_idle
                    jump lbl_beachmain_day_violette_convo
                "Can I sit up on the chair?" if main_story >= 35:
                    hide btn beachmain_day_chair_idle
                    jump lbl_violette_seated_cowgirl
                "Nevermind.":
                    jump lbl_beachmain_day_setup
        else:
            hide btn beachmain_day_chair_idle
            jump lbl_beachmain_day_violette_change

label lbl_beachmain_day_violette_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 1 or date == 20 or date == 26 or date == 0:
            jump lbl_beachmain_day_violette_1
        elif date == 4 or date == 17 or date == 27:
            jump lbl_beachmain_day_violette_2
        elif date == 5 or date == 15 or date == 28:
            jump lbl_beachmain_day_violette_3
        elif date == 8 or date == 13 or date == 29:
            jump lbl_beachmain_day_violette_4
        elif date == 9 or date == 11 or date == 30:
            jump lbl_beachmain_day_violette_5
        elif date == 10 or date == 12 or date == 25:
            jump lbl_beachmain_day_violette_11
        elif date == 7 or date == 14 or date == 24:
            jump lbl_beachmain_day_violette_12
        elif date == 6 or date == 16 or date == 23:
            jump lbl_beachmain_day_violette_13
        elif date == 3 or date == 18 or date == 22:
            jump lbl_beachmain_day_violette_14
        elif date == 2 or date == 19 or date == 21:
            jump lbl_beachmain_day_violette_15
    elif gtime == 1:
        if date == 9 or date == 16 or date == 28 or date == 31:
            jump lbl_beachmain_day_violette_6
        elif date == 10 or date == 17 or date == 27:
            jump lbl_beachmain_day_violette_7
        elif date == 1 or date == 18 or date == 26:
            jump lbl_beachmain_day_violette_8
        elif date == 2 or date == 19 or date == 25:
            jump lbl_beachmain_day_violette_9
        elif date == 3 or date == 11 or date == 24:
            jump lbl_beachmain_day_violette_10
        elif date == 4 or date == 12 or date == 23:
            jump lbl_beachmain_day_violette_11
        elif date == 5 or date == 13 or date == 22:
            jump lbl_beachmain_day_violette_12
        elif date == 6 or date == 14 or date == 21:
            jump lbl_beachmain_day_violette_13
        elif date == 7 or date == 15 or date == 30:
            jump lbl_beachmain_day_violette_14
        elif date == 8 or date == 20 or date == 29:
            jump lbl_beachmain_day_violette_15

## Change Out of Clothes
label lbl_beachmain_day_violette_change:
    show pov bored at left
    with dissolve
    show vio bored_talk at right
    with dissolve
    vio "Look, you're going to need to take off your clothes."
    vio "You're creeping people out: it looks like you're hiding some genitalia disease, with your pants on."
    show pov bored_talk at left
    show vio neutral at right
    pov "Fair enough reason there."

    jump lbl_beachmain_day_setup

## Morning Exclusive
label lbl_beachmain_day_violette_1:
    show povn neutral at left
    with dissolve
    show vio neutral_talk at right
    with dissolve
    vio "Good morning! Decided to start your day by giving that D some vitamin D?"
    show povn neutral_talk at left
    show vio neutral at right
    pov "Haha, I see what you did there!"
    show povn smirk_talk at left
    pov "Vitamin D.. on my D.."
    show povn embarrassed_talk at left
    show vio bored at right
    pov "Because it's D for-"
    show povn embarrassed at left
    show vio bored_talk at right
    vio "Yeah, no need to drag it out, [povname]."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_2:
    show povn neutral at left
    with dissolve
    show vio neutral_talk at right
    with dissolve
    vio "Morning, [povname]. Did you get a good night's rest?"
    show povn neutral_talk at left
    show vio neutral at right
    pov "I did, how about you?"
    show povn neutral at left
    show vio embarrassed_talk at right
    vio "Couldn't sleep, had an all-nighter binge watching webflicks."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "It wasn't the only thing that was flicking."
    vio "If you get my drift."
    show vio embarrassed_talk at right
    vio "{i}*Sigh*{/i} David Hosselhaff is such a fucking stud."
    show povn smirk_talk at left
    show vio embarrassed at right
    pov "Beachwatch again, huh?"

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_3:
    show povn neutral at left
    with dissolve
    show vio confused_talk at right
    with dissolve
    vio "Morning, [povname]. Careful out there in the water."
    show povn confused_talk at left
    show vio confused at right
    pov "Why's that?"
    show povn confused at left
    show vio bored_talk at right
    vio "Someone's disguising themself as a shark and poking at people's genitals."
    show povn confused_talk at left
    show vio bored at right
    pov "Again?"
    show povn embarrassed at left
    show vio confused_talk at right
    vio "I don't know why people can't just have sex out in the open and not be creepy about it."
    vio "I guess it's a niche fetish of some sorts."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_4:
    show povn neutral_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Hey, Violette. How's your morning going?"
    show povn neutral_talk at left
    show vio smirk at right
    vio "No one has drowned yet, hahaha."
    show povn shocked at left
    show vio confused_talk at right
    vio "At least not that I know of."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "People can get too freaky in the water."
    show povn smirk_talk at left
    show vio neutral at right
    pov "I can scarily understand why one would take that risk."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_5:
    show povn neutral_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Morning, Violette. How's lifeguard duty?"
    show povn neutral at left
    show vio neutral_talk at right
    vio "Same old, same old."
    show povn smirk_talk at left
    show vio smirk at right
    pov "Why? Don't you like freely gazing at people's bare bodies on duty?"
    show povn smirk at left
    show vio smirk_talk at right
    vio "I didn't say that at all, I love my job."
    vio "And I love boobs and dick as much as the next person."
    show povn neutral_talk at left
    show vio smirk at right
    pov "I'll drink to that."

    jump lbl_beachmain_day

## Afternoon Exclusive
label lbl_beachmain_day_violette_6:
    show povn neutral at left
    with dissolve
    show vio neutral_talk at right
    with dissolve
    vio "Afternoon, [povname]. Here to watch the beautiful sunset?"
    show povn sad_talk at left
    show vio neutral at right
    pov "I wish. I always happen to miss it for some reason."
    show povn sad at left
    show vio confused_talk at right
    vio "Huh, that sucks."
    show povn confused_talk at left
    show vio confused at right
    pov "Yeah, it's as if I just black out when the sun hits the horizon."
    show povn embarrassed at left
    show vio confused_talk at right
    vio "Totally weird. Youre missing out."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_7:
    show povn neutral at left
    with dissolve
    show vio neutral_talk at right
    with dissolve
    vio "Afternoon, sweet thing."
    show povn neutral_talk at left
    show vio neutral at right
    pov "Hey, Violette. Anyhing new happen today?"
    show povn embarrassed at left
    show vio confused_talk at right
    vio "Other than the ocassional accidental butt fuck injury?"
    show vio neutral_talk at right
    vio "Nope, it's been pretty tame today."
    show povn embarrassed_talk at left
    show vio confused at right
    pov "Is that a good thing or a bad thing?"
    show povn neutral at left
    show vio smirk_talk at right
    vio "Most days you want some butt-fucking action, and some days you wanna chill, y'know?"

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_8:
    show povn smirk_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Hello, Miss Lifeguard."
    show povn smirk at left
    show vio confused_talk at right
    vio "Hello, [povname]. Don't tell me you forgot my name."
    show povn smirk_talk at left
    show vio smirk at right
    pov "With a chest like that, how could I forget you, Violette."
    show povn smirk at left
    show vio smirk_talk at right
    vio "Likewise with you and your nameless friend."
    show povn confused at left
    show vio confused at right
    vio "But seriously, why don't you name it?"
    show povn bored_talk at left
    show vio confused at right
    pov "It's personal."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_9:
    show povn smirk_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Violette! How's my favourite lifeguard?"
    show povn neutral at left
    show vio embarrassed_talk at right
    vio "Afternoon, [povname]. I'm well."
    show povn neutral_talk at left
    show vio neutral at right
    pov "That's good, any plans for the weekend?"
    show povn smirk at left
    show vio smirk_talk at right
    vio "I'm thinking to have a vacation. Somewhere tropical."
    show povn confused at left
    vio "Like a beach!"
    show povn smirk_talk at left
    show vio smirk at right
    pov "Ha, funny you are. I guess everyday's a vacation if one had a job like yours."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_10:
    show povn confused_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "It's hot today, isn't it?"
    show povn smirk at left
    show vio confused_talk at right
    vio "Yeah, wish we had the freedom to just go nude."
    show povn smirk_talk at left
    show vio embarrassed at right
    pov "That would just be the best."
    show povn neutral at left
    show vio shocked_talk at right
    vio "I mean, this waist strap I'm wearing is sooo thick."
    show vio embarrassed_talk at right
    vio "I should have left the house without it."
    show povn smirk_talk at left
    show vio smirk at right
    pov "Yeah, it looks more like winter attire."

    jump lbl_beachmain_day

## Interchangable
label lbl_beachmain_day_violette_11:
    show povn neutral at left
    with dissolve
    show vio neutral_talk at right
    with dissolve
    vio "Hey, [povname]. How's it going?"
    show povn neutral_talk at left
    show vio neutral at right
    pov "Oh, you know getting some fresh air."
    show povn neutral at left
    show vio smirk_talk at right
    vio "If you're like me, putting on one layer of clothes is like 3 layers."
    show povn smirk_talk at left
    show vio shocked at right
    pov "I actually like wearing layers."
    show povn embarrassed at left
    show vio shocked_talk at right
    vio "Do you now?"
    show povn smirk_talk at left
    show vio smirk at right
    pov "But y'know... naked is the new black."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_12:
    show povn confused at left
    with dissolve
    show vio neutral_talk at right
    with dissolve
    vio "Hey [povname]. Hope you didn't eat a lot."
    show povn smirk_talk at left
    show vio neutral at right
    pov "Why? Should I wait an hour before going into the water?"
    show povn neutral at left
    show vio smirk_talk at right
    vio "That's a total myth. I've done that plenty of times."
    show povn embarrassed at left
    show vio confused_talk at right
    vio "Although I doubt that dicks and pussies count..."
    show povn confused_talk at left
    show vio neutral at right
    pov "... Still, why the worry about my food intake?"
    show povn shocked at left
    show vio confused_talk at right
    vio "Oh! I just don't want you to throw up, there's a foul smell near the west side of the beach."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_13:
    show povn embarrassed_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "I could never get used to all the beautiful women on this beach."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "Your little friend is doing quite well holding it's ground."
    show povn smirk_talk at left
    show vio smirk at right
    pov "Oh, yeah... I uh- just don't want to cause such an uproar by unleashing it."
    show povn smirk at left
    show vio smirk_talk at right
    vio "Hahaha, cocky little bastard."
    vio "Well, I'm no stranger to... dangerous animals."
    show povn embarrassed at left
    show vio bored_talk at right
    vio "...Sharks."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_14:
    show povn neutral_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Did you catch this morning's sunrise?"
    show povn neutral at left
    show vio embarrassed_talk at right
    vio "I always do, call me cheesy but it's still the most beautiful thing to ever touch this beach."
    show povn embarrassed_talk at left
    show vio neutral at right
    pov "I want to say I wish I would wake up early enough to catch it but..."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "But... you like your bed."
    show povn smirk at left
    vio "That's okay, more sunrise for me."

    jump lbl_beachmain_day

label lbl_beachmain_day_violette_15:
    show povn neutral_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Any plans for tonight?"
    show povn neutral at left
    show vio confused_talk at right
    vio "I might go for a run in the park, maybe not."
    vio "Maybe I'll go find a poor, lonely soul on this beach to prey on."
    vio "I may even possibly just stay at home and Webflicks the shit out of the night."
    show povn smirk_talk at left
    show vio shocked at right
    pov "Just like the waves, you go with the flow."
    show povn smirk at left
    show vio smirk_talk at right
    vio "Holy hell, yes! That is an amazing saying. You should put that on a T-Shirt."

    jump lbl_beachmain_day
