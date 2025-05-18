## Throwaway Sister Bedroom Night Conversation ##
label lbl_sisterbedroom_night_sister:

## Side Story
    if mum_path == 21:
        jump lbl_sisterbedroom_night_sister_mompark
    else:
        show btn sisterbedroom_night_sister_idle
        menu:
            "Talk":
                hide btn sisterbedroom_night_sister_idle
                jump lbl_sisterbedroom_night_sister_convo
            "Give Gift" if selecteditem != None:
                jump lbl_sister_giftgiving
            "Ask to movie date" if moviedate == 0 and sister_path >= 20:
                jump lbl_sisterbedroom_daynight_sister_moviedate
            "Wanna play?":
                menu:
                    "Right here, right now" if sister_path >= 40:
                        hide btn sisterbedroom_night_sister_idle
                        jump lbl_sister_bedroom_daynight_sister_play
                    "With Mom down in the fort" if winc == 1 and mumsis_path >= 13:
                        jump lbl_momxsisxmc_boxfort_presister
                    "With [missus] down in the fort" if winc == 0 and mumsis_path >= 13:
                        jump lbl_momxsisxmc_boxfort_presister
                    "Nevermind":
                        jump lbl_sisterbedroom_night_sister
            "Nevermind":
                jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_convo:
## 1 - 10 is evening exclusive
    if date == 1 or date == 14 or date == 22:
        jump lbl_sisterbedroom_night_sister_1
    elif date == 3 or date == 19 or date == 30:
        jump lbl_sisterbedroom_night_sister_2
    elif date == 2 or date == 11 or date == 25:
        jump lbl_sisterbedroom_night_sister_3
    elif date == 5 or date == 12 or date == 27:
        jump lbl_sisterbedroom_night_sister_4
    elif date == 4 or date == 13 or date == 23:
        jump lbl_sisterbedroom_night_sister_5
    elif date == 7 or date == 15 or date == 29:
        jump lbl_sisterbedroom_night_sister_6
    elif date == 6 or date == 18 or date == 21:
        jump lbl_sisterbedroom_night_sister_7
    elif date == 10 or date == 20 or date == 24:
        jump lbl_sisterbedroom_night_sister_8
    elif date == 8 or date == 16 or date == 26:
        jump lbl_sisterbedroom_night_sister_9
    elif date == 9 or date == 17 or date == 28 or date == 31:
        jump lbl_sisterbedroom_night_sister_10

label lbl_sisterbedroom_night_sister_sleep:
    pov "{i}She's sleeping, I shouldn't disturb her.{/i}"
    call screen scr_sisterbedroom_night

label lbl_sisterbedroom_night_sister_1:
    show pov neutral_talk at left
    with dissolve
    show sis confused at right
    with dissolve
    pov "You busy?"
    show pov neutral at left
    show sis bored_talk at right
    sis "If you want me to do something for you then yeah."
    show pov smirk_talk at left
    show sis confused at right
    pov "Yeah, you'll do it?"
    show pov confused at left
    show sis confused_talk at right
    sis "What? No."
    show pov confused_talk at left
    show sis confused at right
    pov "But you said yeah."
    show pov confused at left
    show sis confused_talk at right
    sis "Yeah, I meant no, I'm busy."
    show pov confused at left
    show sis confused at right
    pov "..."

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_2:
    show pov angry_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "Did you eat the last piece of chocolate in the fridge?"
    show pov angry at left
    show sis smirk_talk at right
    sis "What are you gonna do if I say yes?"
    show pov smirk_talk at left
    show sis confused at right
    pov "I'm going to climb into your mouth and explode out alien-style."
    show pov bored at left
    show sis confused_talk at right
    sis "You have weird kinks."
    show pov bored_talk at left
    show sis shocked at right
    pov "Yeah? Well chocolate makes you fat."
    show pov bored at left
    show sis shocked_talk at right
    sis "{i}*Gasp*{/i} You said the fucking 'F' word. Get out."

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_3:
    show pov smirk_talk at left
    with dissolve
    show sis bored at right
    with dissolve
    pov "Isn't it past your bedtime?"
    show pov smirk at left
    show sis bored_talk at right
    sis "Still older than you."
    show pov smirk_talk at left
    show sis bored at right
    pov "By the looks of how your room is decorated..."
    pov "Not old enough."
    show pov neutral at left
    show sis bored_talk at right
    sis "Do you have naked posters on your wall because you don't see enough in real life..."
    show pov bored at left
    show sis smirk_talk at right
    sis "Or are you trying to convince yourself you're not trapped in a closet?"

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_4:
    show pov confused at left
    with dissolve
    show sis bored_talk at right
    with dissolve
    sis "Did you forget which room is your room?"
    show pov smirk_talk at left
    show sis confused at right
    pov "Oh, I thought we were gonna sleep in the same bed as usual."
    show pov smirk at left
    show sis confused_talk at right
    sis "As usual 15 years ago."
    show pov smirk_talk at left
    show sis bored at right
    pov "Really? Seemed as if it was only yesterday."
    show pov neutral at left
    show sis bored_talk at right
    sis "Weirdo."

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_5:
    show pov confused at left
    with dissolve
    show sis confused_talk at right
    with dissolve
    sis "I thought I locked the door."
    show pov smirk_talk at left
    show sis bored at right
    pov "Well, obviously you didn't."
    show pov confused at left
    show sis bored_talk at right
    sis "You're lucky I wasn't-"
    show pov smirk_talk at left
    show sis embarrassed at right
    pov "...Wasn't what?"
    show pov smirk at left
    show sis angry_talk at right
    sis "I can see on your perverted face that you're thinking perverted thoughts."
    show pov embarrassed at left
    if winc == 0:
        sis "Stop it. I'm your [sisrole], you creep."
    else:
        sis "Stop it. I'm your sister, you creep."

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_6:
    show pov neutral_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "What's up?"
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "Not much, just talking to friends back home."
    show pov embarrassed_talk at left
    show sis sad at right
    pov "Home is here."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "You know what I meant. I miss them."
    show pov sad_talk at left
    show sis sad at right
    pov "Yeah, I feel the same."

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_7:
    show pov neutral_talk at left
    with dissolve
    show sis bored at right
    with dissolve
    pov "No plans for tonight?"
    show pov neutral at left
    show sis bored_talk at right
    sis "Obviously not. I'm a little tired and lazy today."
    show sis neutral_talk at right
    sis "Oooh! Check this Facepage event."
    show pov smirk_talk at left
    show sis neutral at right
    pov "...'Baruto's Dad Ninja Run for Fun'?"
    show pov neutral at left
    show sis smirk_talk at right
    sis "I'm going to mark myself as interested."
    show pov neutral_talk at left
    show sis neutral at right
    pov "Invite me into it."

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_8:
    show pov confused at left
    with dissolve
    show sis angry_talk at right
    with dissolve
    sis "Mooom!"
    show pov confused_talk at left
    show sis bored at right
    pov "What do you need her for?"
    show pov shocked at left
    show sis angry_talk at right
    sis "Get [povname] outta my roooom!"
    show pov shocked_talk at left
    show sis neutral at right
    pov "What the hell, I didn't even say anything yet!"
    show pov angry at left
    show sis smirk_talk at right
    sis "He keeps poking meee!"
    show pov angry_talk at left
    show sis smirk at right
    pov "I'm not even touching heeeer!"

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_9:
    show pov neutral_talk at left
    with dissolve
    show sis embarrassed at right
    with dissolve
    pov "How's work going for you?"
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "Work is work, it puts money in my pocket. That's all I care about."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "If you're not working full-time then, what do you-"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Narnia."
    show pov confused_talk at left
    show sis smirk at right
    pov "Narnia?"
    show pov bored at left
    show sis smirk_talk at right
    sis "Yeah, narnia business, slick."

    jump lbl_sisterbedroom_night

label lbl_sisterbedroom_night_sister_10:
    show pov confused_talk at left
    with dissolve
    show sis bored at right
    with dissolve
    if winc == 0:
        pov "Are you and [dadname] still..?"
    else:
        pov "Are you and Dad still..?"
    show pov embarrassed at left
    show sis embarrassed_talk at right
    sis "You know how him and I are."
    show sis sad_talk at right
    sis "He hasn't been the same since we moved."
    show sis confused_talk at right
    sis "If you ask me, I think the stress from his new job is really making him cranky."
    show pov embarrassed_talk at left
    show sis smirk at right
    pov "A bit dick-ish, if you will."
    show pov smirk at left
    show sis smirk_talk at right
    sis "Invert the dick, he's an asshole."

    jump lbl_sisterbedroom_night
