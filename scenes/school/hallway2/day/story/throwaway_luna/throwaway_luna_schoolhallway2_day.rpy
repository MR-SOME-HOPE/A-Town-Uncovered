## Throwaway Luna School Hallway 2 Day Conversation ##
label lbl_schoolhallway2_day_luna:
    if insexworld == 0:
        scene bg schoolhallway2_day
    elif insexworld == 1:
        scene bg schoolhallway2_daysexworld
    show btn_schoolhallway2_day_luna_idle2
    $ renpy.pause(0.001)

    ## Main Story
    ## Sexworld Luna
    if main_story <= 40 and insexworld == 1:
        jump lbl_schoolhallway2_day_luna_sexworld
    ## Investigation Luna
    elif main_story == 84:
        jump lbl_investigations_luna

    ## NO EVENT
    else:
        menu:
            "Have some fun at my place" if main_story >= 30:
                jump lbl_luna_doggy_bedroom
            "Talk":
                jump lbl_schoolhallway2_day_luna_convo
            "Nevermind":
                jump lbl_schoolhallway2_day_setup

label lbl_schoolhallway2_day_luna_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if date == 7 or date == 19 or date == 21:
        jump lbl_schoolhallway2_day_luna_1
    elif date == 10 or date == 20 or date == 23:
        jump lbl_schoolhallway2_day_luna_2
    elif date == 9 or date == 18 or date == 22:
        jump lbl_schoolhallway2_day_luna_3
    elif date == 8 or date == 17 or date == 24:
        jump lbl_schoolhallway2_day_luna_4
    elif date == 5 or date == 15 or date == 26:
        jump lbl_schoolhallway2_day_luna_5
    elif date == 4 or date == 16 or date == 30:
        jump lbl_town_day_luna_11
    elif date == 3 or date == 18 or date == 25:
        jump lbl_town_day_luna_12
    elif date == 2 or date == 17 or date == 27:
        jump lbl_town_day_luna_13
    elif date == 1 or date == 11 or date == 29:
        jump lbl_town_day_luna_14
    elif date == 6 or date == 12 or date == 28 or date == 0:
        jump lbl_town_day_luna_15

## Morning Exclusive
label lbl_schoolhallway2_day_luna_1: ##
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolhallway2_day_luna_idle2
    show lun neutral at right
    with dissolve
    pov "Morning, Luna."
    show pov neutral at left
    show lun confused_talk at right
    lun "Morning, [povname]. Did you have a good sleep?"
    show pov neutral_talk at left
    show lun confused at right
    pov "Yeah, it was aight. You?"
    show pov confused at left
    show lun bored_talk at right
    lun "I talked to my great grandmother last night, she was wonderful."
    show lun neutral_talk at right
    lun "Oh the stories she could tell."
    show pov confused_talk at left
    show lun confused at right
    pov "In your dreams?"
    show pov embarrassed at left
    show lun embarrassed_talk at right
    lun "Uhhh- sure. Yeah, let's go with that."

    jump lbl_schoolhallway2_day

label lbl_schoolhallway2_day_luna_2: ##
    show pov neutral at left
    with dissolve
    hide btn_schoolhallway2_day_luna_idle2
    show lun neutral_talk at right
    with dissolve
    lun "Morning, [povname]. Your energy seems really weird today."
    show pov confused_talk at left
    show lun embarrassed at right
    pov "My energy? Well some weird things have been happening to me recently I guess."
    show pov confused at left
    show lun embarrassed_talk at right
    lun "Like really weird... Have you crossed any- witches- recently?"
    show pov bored_talk at left
    show lun bored at right
    pov "Not that I know of."
    show pov bored at left
    show lun bored_talk at right
    lun "Well, keep that in mind, I feel some spiritual being doesn't like you."
    show pov smirk_talk at left
    show lun bored at right
    pov "Haters gonna hate, Luna. There's only so much I can control in my life."

    jump lbl_schoolhallway2_day

label lbl_schoolhallway2_day_luna_3: ##
    show pov bored_talk at left
    with dissolve
    hide btn_schoolhallway2_day_luna_idle2
    show lun confused at right
    with dissolve
    pov "I wish I was home right now, I wanna lay in bed and rest all day."
    show pov shocked at left
    show lun smirk_talk at right
    lun "You can rest when you're dead!"
    show pov embarrassed_talk at left
    show lun smirk at right
    pov "Y'know usually that wouldn't bother me but coming from you, it sounds sus."
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "Why? Because I have love everything dead?"
    show pov embarrassed_talk at left
    show lun smirk at right
    pov "..."
    show pov bored at left
    show lun bored_talk  at right
    lun "Sue me, while you're still alive, [povname]. While we're all still alive."
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "It's only a matter of time."

    jump lbl_schoolhallway2_day

label lbl_schoolhallway2_day_luna_4: ##
    show pov neutral at left
    with dissolve
    hide btn_schoolhallway2_day_luna_idle2
    show lun neutral_talk at right
    with dissolve
    lun "Hey, can I copy your homework for today's class?"
    show pov embarrassed_talk at left
    show lun bored at right
    pov "Sorry, I haven't done it myself."
    show pov shocked  at left
    show lun angry_talk at right
    lun "Damn, I swear I did it legitimately last night but I accidentally broke my blood vial and made a mess all over it."
    show pov shocked_talk at left
    show lun embarrassed at right
    pov "I- there's so much to unpack right there."
    show pov embarrassed at left
    show lun neutral_talk at right
    lun "No, not really. It's just blood plus paper."
    lun "Spoiler alert, it doesn't wash out."
    show pov smirk_talk at left
    show lun neutral at right
    pov "Damn, well, I guess that goes that theory. Sorry, girl."

    jump lbl_schoolhallway2_day

label lbl_schoolhallway2_day_luna_5: ##
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolhallway2_day_luna_idle2
    show lun sad at right
    with dissolve
    pov "Good morning, Luna."
    show pov confused at left
    show lun bored_talk at right
    lun "{i}*Sigh*{/i} Morning."
    show pov embarrassed_talk at left
    show lun confused at right
    pov "Why the long face?"
    show pov confused at left
    show lun bored_talk at right
    lun "One of my ghosts got mad at me and tripped me this morning."
    lun "I don't know what I did to make them angry but I can sense that they'll continue to harass me later tonight."
    show pov confused_talk at left
    show lun smirk at right
    pov "I'm- sorry to hear... Maybe apologize?"
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "They want a proper full apology and I have no idea what I did wrong so that's impossible."
    lun "I guess I'll have to settle for another sacrifice."

    jump lbl_schoolhallway2_day

## Interchangeable
label lbl_town_day_luna_11: ##
    show pov neutral_talk at left
    with dissolve
    if gtime == 1:
        hide btn_classroom_day_luna_idle2
    elif gtime == 0:
        hide btn_schoolhallway2_day_luna_idle2
    show lun neutral at right
    with dissolve
    pov "Hey, Luna. What's up?"
    show pov smirk at left
    show lun neutral_talk at right
    lun "Well, I ordered a taxidermied rabbit and it's supposedly arriving today! I'm so excited."
    show pov confused_talk at left
    show lun smirk at right
    pov "It sounds- exciting."
    pov "Whatcha gonna name it?"
    show pov embarrassed at left
    show lun neutral_talk at right
    lun "It's name is Luna, and no I didn't name it."
    show pov embarrassed_talk at left
    show lun neutral at right
    pov "Wow! Same-name buddies."
    show pov smirk at left
    show lun smirk at right
    lun "I know right, it's like we were meant to be."

    jump lbl_town_day_luna_end

label lbl_town_day_luna_12: ##
    show pov neutral at left
    with dissolve
    if gtime == 1:
        hide btn_classroom_day_luna_idle2
    elif gtime == 0:
        hide btn_schoolhallway2_day_luna_idle2
    show lun neutral_talk at right
    with dissolve
    lun "Hi! Hi! Hi!"
    show pov neutral_talk at left
    show lun smirk at right
    pov "Sounds like you just got some good news!"
    show pov embarrassed at left
    show lun neutral_talk at right
    lun "Yeah! My friend gave me a tarot card reading last night and let's just say, I got everything going my way right now."
    show pov neutral_talk at left
    show lun shocked at right
    pov "That's good, I'm glad you got luck going for you."
    show pov shocked at left
    show lun confused_talk at right
    lun "Oh-no. Not luck, tarot reading isn't about luck or the future."
    lun "It's simply a means of self-reflection and addressing things that one {i}may{/i} experience in the past, present, and future."
    show pov embarrassed_talk at left
    show lun smirk at right
    pov "I shall need to give that a try sometime."

    jump lbl_town_day_luna_end

label lbl_town_day_luna_13: ##
    show pov confused_talk at left
    with dissolve
    if gtime == 1:
        hide btn_classroom_day_luna_idle2
    elif gtime == 0:
        hide btn_schoolhallway2_day_luna_idle2
    show lun embarrassed at right
    with dissolve
    pov "Luna, you good? You've been day dreaming for quite a while."
    show pov confused at left
    show lun confused_talk at right
    lun "How can you tell? Have you been staring at me for the entire time period?"
    show pov bored_talk at left
    show lun smirk at right
    pov "Uhm- well no. I kinda glanced over at you, every- y'know. Once in a while."
    show pov confused at left
    show lun smirk_talk at right
    lun "Worry not, [povname]. I'm just planning how I am to ruin someone's life."
    show pov shocked_talk at left
    show lun smirk at right
    pov "What did this person do?"
    show pov embarrassed at left
    show lun bored_talk at right
    lun "If I tell you, I'll have to ruin your life too, [povname]. Hear nothing, say nothing."
    show pov embarrassed_talk at left
    show lun neutral at right
    pov "Ears and lips are sealed."

    jump lbl_town_day_luna_end

label lbl_town_day_luna_14: ##
    show pov neutral at left
    with dissolve
    if gtime == 1:
        hide btn_classroom_day_luna_idle2
    elif gtime == 0:
        hide btn_schoolhallway2_day_luna_idle2
    show lun neutral_talk at right
    with dissolve
    lun "Have you seen the Bloody Mary series?"
    show pov embarrassed_talk at left
    show lun neutral at right
    pov "Not really, I've been meaning to get around to watching them. I heard the 6th and 9th movies are the best."
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "Those are pretty good but my personal favourite is the original one."
    lun "Some would say it's the least bloody but I think it's the most tasteful and risque."
    lun "After that it gets bloodier but also more bland."
    show pov smirk_talk at left
    show lun neutral at right
    pov "Hmm, I thought the amount of blood is relative to how 'exciting' it is."
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "C'mon, [povname]. What do you take me for?"

    jump lbl_town_day_luna_end

label lbl_town_day_luna_15: ##
    show pov neutral at left
    with dissolve
    if gtime == 1:
        hide btn_classroom_day_luna_idle2
    elif gtime == 0:
        hide btn_schoolhallway2_day_luna_idle2
    show lun sad_talk at right
    with dissolve
    lun "I need to buy some new candles, I'm running low."
    show pov confused_talk at left
    show lun sad at right
    pov "Ah well, good thing they aren't that expensive."
    show pov shocked at left
    show lun bored_talk at right
    lun "Yeah, doesn't really help that I have at least 20 of them lit every night."
    show pov shocked_talk at left
    show lun bored at right
    pov "Daaaamn, really? What do you not have electricity at your place?"
    show pov confused at left
    show lun bored_talk at right
    lun "I don't judge you for using a light bulb, why do you have to judge me for using 20 candles?"
    show pov embarrassed_talk at left
    show lun bored at right
    pov "You bring up a good point, sorry."
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "Not everyone is as bright as they look."

    jump lbl_town_day_luna_end

label lbl_town_day_luna_end:
    if gtime == 0:
        jump lbl_schoolhallway2_day
    else:
        jump lbl_classroom_day
