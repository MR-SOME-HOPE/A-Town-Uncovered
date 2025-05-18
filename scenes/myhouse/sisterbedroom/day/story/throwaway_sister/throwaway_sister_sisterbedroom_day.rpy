## Throwaway Sister Bedroom Day Conversation ##
label lbl_sisterbedroom_day_sister:
    show btn sisterbedroom_day_sister_idle
    menu:
        "Talk":
            hide btn sisterbedroom_day_sister_idle
            jump lbl_sisterbedroom_day_sister_convo
        "Give Gift" if selecteditem != None:
            jump lbl_sister_giftgiving
        "Ask to movie date" if moviedate == 0 and sister_path >= 20:
            jump lbl_sisterbedroom_daynight_sister_moviedate
        "Wanna play?" if sister_path >= 40:
            hide btn sisterbedroom_day_sister_idle
            jump lbl_sister_bedroom_daynight_sister_play
        "Wanna visit Effie for some fun?" if sister_path >= 33 and gtime == 0 and day >= 5:
            hide btn sisterbedroom_day_sister_idle
            jump lbl_mcxsister_eating_effie_pre
        "Nevermind":
            jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 1 or date == 19 or date == 22:
            jump lbl_sisterbedroom_day_sister_1
        elif date == 2 or date == 12 or date == 30:
            jump lbl_sisterbedroom_day_sister_2
        elif date == 3 or date == 14 or date == 21:
            jump lbl_sisterbedroom_day_sister_3
        elif date == 4 or date == 17 or date == 25:
            jump lbl_sisterbedroom_day_sister_4
        elif date == 5 or date == 11 or date == 27:
            jump lbl_sisterbedroom_day_sister_5
        elif date == 6 or date == 18 or date == 26:
            jump lbl_sisterbedroom_day_sister_11
        elif date == 7 or date == 13 or date == 23:
            jump lbl_sisterbedroom_day_sister_12
        elif date == 8 or date == 15 or date == 29:
            jump lbl_sisterbedroom_day_sister_13
        elif date == 9 or date == 20 or date == 28:
            jump lbl_sisterbedroom_day_sister_14
        elif date == 10 or date == 16 or date == 24 or date == 0:
            jump lbl_sisterbedroom_day_sister_15
    elif gtime == 1:
        if date == 5 or date == 11 or date == 22:
            jump lbl_sisterbedroom_day_sister_6
        elif date == 6 or date == 15 or date == 30:
            jump lbl_sisterbedroom_day_sister_7
        elif date == 7 or date == 18 or date == 21:
            jump lbl_sisterbedroom_day_sister_8
        elif date == 8 or date == 17 or date == 25:
            jump lbl_sisterbedroom_day_sister_9
        elif date == 9 or date == 12 or date == 27:
            jump lbl_sisterbedroom_day_sister_10
        elif date == 10 or date == 13 or date == 26:
            jump lbl_sisterbedroom_day_sister_12
        elif date == 1 or date == 14 or date == 23:
            jump lbl_sisterbedroom_day_sister_14
        elif date == 2 or date == 20 or date == 29:
            jump lbl_sisterbedroom_day_sister_11
        elif date == 3 or date == 16 or date == 28:
            jump lbl_sisterbedroom_day_sister_15
        elif date == 4 or date == 19 or date == 24 or date == 0:
            jump lbl_sisterbedroom_day_sister_13

## Morning Exclusive
label lbl_sisterbedroom_day_sister_1:
    show pov neutral_talk at left
    with dissolve
    show sis bored at right
    with dissolve
    pov "Morning. Don't you have work?"
    show pov neutral at left
    show sis bored_talk at right
    sis "Not right now. Why?"
    show pov neutral_talk at left
    show sis bored at right
    pov "Just asking."
    show pov neutral at left
    show sis neutral_talk at right
    sis "Shouldn't you be.. I don't know?"
    show sis bored_talk at right
    sis "Not bothering me?"
    show pov smirk_talk at left
    show sis bored at right
    pov "Touche."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_2:
    show pov neutral_talk at left
    with dissolve
    show sis bored at right
    with dissolve
    if winc == 0:
        pov "Hey, [missus]'s calling you for breakfast."
    else:
        pov "Hey, mom's calling you for breakfast."
    show pov neutral at left
    show sis bored_talk at right
    sis "Tell her I'm not hungry."
    show pov smirk_talk at left
    show sis confused at right
    pov "But she made pancakes."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "I know she didn't make pancakes."
    sis "You just want me to get up from my comfortable position."
    show pov smirk_talk at left
    show sis bored at right
    pov "If you put it that way."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_3:
    show pov sad_talk at left
    with dissolve
    show sis confused at right
    with dissolve
    pov "Can you help me with my assignment?"
    show pov embarrassed at left
    show sis confused_talk at right
    sis "I dropped out, remember?"
    show pov sad_talk at left
    show sis bored at right
    pov "Yeah, but you're older than me."
    show pov neutral at left
    show sis bored_talk at right
    sis "By 13 minutes."
    show pov smirk_talk at left
    show sis bored at right
    pov "Still 13 minutes smarter."
    show pov bored at left
    show sis bored_talk at right
    sis "No."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_4:
    show pov neutral_talk at left
    with dissolve
    show sis bored at right
    with dissolve
    pov "What's up?"
    show pov embarrassed at left
    show sis sad_talk at right
    sis "Ugh, woke up with a headache."
    show pov smirk_talk at left
    show sis bored at right
    pov "You want me to rub some ointment on your forehead like the Lion Prince?"
    show pov smirk at left
    show sis angry_talk at right
    sis "Don't go anywhere near my forehead."
    show sis sad_talk at right
    sis "You'll ruin my bangs."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_5:
    show pov smirk_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "Sleep well, munchkin?"
    show pov neutral at left
    show sis smirk_talk at right
    sis "Slept better than you did."
    show pov confused_talk at left
    show sis neutral at right
    pov "Was that suppose to hurt me?"
    show pov confused at left
    show sis neutral_talk at right
    sis "Did it work?"
    show pov confused_talk at left
    show sis embarrassed at right
    pov "No?"
    show pov smirk at left
    show sis embarrassed_talk at right
    sis "Then no..."

    jump lbl_sisterbedroom_day

## Afternoon Exclusive
label lbl_sisterbedroom_day_sister_6:
    show pov neutral_talk at left
    with dissolve
    show sis confused at right
    with dissolve
    pov "How's work?"
    show pov neutral at left
    show sis confused_talk at right
    sis "...Work's good?"
    sis "Why..? Do you need to borrow money?"
    show pov neutral_talk at left
    show sis confused at right
    pov "Can I borrow some mo-"
    show pov bored at left
    show sis bored_talk at right
    sis "No. I barely have enough for my expensive lifestyle."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_7:
    show pov neutral_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "Are you gonna shower first?"
    show pov neutral at left
    show sis neutral_talk at right
    sis "Nah, you go ahead. I'm busy."
    show pov confused_talk at left
    show sis neutral at right
    pov "It looks like you're on Tweete-"
    show pov confused at left
    show sis angry_talk at right
    sis "I'm reading the news."
    show pov bored at left
    show sis bored_talk at right
    sis "Jeez, get with the times, [povname]."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_8:
    show pov neutral at left
    with dissolve
    show sis neutral_talk at right
    with dissolve
    sis "Is dinner ready?"
    show pov confused_talk at left
    show sis sad at right
    pov "It's still to early."
    show pov embarrassed at left
    show sis sad_talk at right
    sis "Gosh, I'm starving."
    show pov bored at left
    show sis embarrassed_talk at right
    sis "Be an angel and get me something to eat."
    show pov smirk_talk at left
    show sis smirk at right
    pov "Honey, I'm not your bitch."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_9:
    show pov confused_talk at left
    with dissolve
    show sis confused at right
    with dissolve
    pov "You going out tonight?"
    show pov confused at left
    show sis confused_talk at right
    sis "Maybe, maybe not. Depends on my mood."
    show pov confused_talk at left
    show sis shocked at right
    if winc == 0:
        pov "Does [missus] know you go clubbing and drinking?"
    else:
        pov "Does Mom know you go clubbing and drinking?"
    show pov embarrassed at left
    show sis angry_talk at right
    sis "No, I prefer if you don't be an asshole and rat me out."
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "Yeah, no worries. Just curious."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_10:
    show pov confused_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "Gosh, it's hot in here."
    show pov confused at left
    show sis confused_talk at right
    sis "Your point is?"
    show pov smirk_talk at left
    show sis bored at right
    pov "Should I leave the room?"
    show pov bored at left
    show sis neutral_talk at right
    sis "Actually, yes please. And don't come back."
    show pov neutral_talk at left
    show sis neutral at right
    pov "I love you too, sis."

    jump lbl_sisterbedroom_day

## Interchangable
label lbl_sisterbedroom_day_sister_11:
    show pov neutral at left
    with dissolve
    show sis confused_talk at right
    with dissolve
    sis "Is there a reason why you're in my room?"
    show pov neutral_talk at left
    show sis confused at right
    pov "I'm looking for something."
    show pov neutral at left
    show sis confused_talk at right
    sis "What are you looking for exactly?"
    show pov smirk_talk at left
    show sis angry at right
    pov "Blackmail material."
    show pov smirk at left
    show sis angry_talk at right
    sis "Get the fuck out, dude."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_12:
    show pov neutral_talk at left
    with dissolve
    show sis confused at right
    with dissolve
    pov "Did you see this video on Facepage?"
    show pov neutral at left
    show sis confused_talk at right
    sis "That's an old video."
    show pov embarrassed_talk at left
    show sis confused at right
    pov "Yeah, but.."
    show pov neutral_talk at left
    show sis bored at right
    pov "Heh. Hehe.. Hehehehaha!"
    pov "Gets me every time."
    show pov bored_talk at left
    pov "I'm glad we could share this moment together."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_13:
    show pov neutral_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "Whatcha doing?"
    show pov bored at left
    show sis smirk_talk at right
    sis "Your mom."
    show sis bored_talk at right
    sis "You know what, I keep forgetting-"
    show pov bored_talk at left
    show sis bored at right
    pov "Yeah."
    show pov bored at left
    show sis bored_talk at right
    sis "Yeah..."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_14:
    show pov confused_talk at left
    with dissolve
    show sis bored at right
    with dissolve
    pov "Why do you still have all these plushies with you?"
    pov "Isn't that a little baby-ish?"
    show pov bored at left
    show sis confused_talk at right
    sis "Says the guy with a Barbie doll on his desk."
    show pov angry_talk at left
    show sis smirk at right
    pov "It's not a Barbie. It's a Vaultgirl."
    show pov bored_talk at left
    pov "Uncultured swine."

    jump lbl_sisterbedroom_day

label lbl_sisterbedroom_day_sister_15:
    show pov neutral at left
    with dissolve
    show sis embarrassed_talk at right
    with dissolve
    sis "Oh, hi, [povname]."
    show pov neutral_talk at left
    show sis embarrassed at right
    pov "Hey, [sister]."
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Can you do me a favour and go down to the kitchen..."
    show pov bored at left
    show sis bored_talk at right
    sis "And get me a packet of 'Get the fuck outta my room'?"
    show pov smirk_talk at left
    show sis angry at right
    pov "Sorry, I think I ate the last on-"
    show pov embarrassed_talk at left
    pov "Alright, alright."

    jump lbl_sisterbedroom_day

## GIFT GIVING
label lbl_sister_giftgiving:
    ##if inventory.has_item(selecteditem):
        ##if sisterAcceptedItems():
    if selecteditem.id ==  Items.gachablue.id:
        if day == 1 or day == 2:
            $ sister_gift_like_level += 15
        elif day == 5:
            $ sister_gift_like_level += 5
        else:
            $ sister_gift_like_level += 10
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show sis neutral_talk at right
        with dissolve
        sis "Oooh! A gacha, let's see what surprise I get today! Thanks, little bro."
    elif selecteditem.id ==  Items.gachapink.id:
        if day == 0 or day == 3:
            $ sister_gift_like_level += 15
        elif day == 6:
            $ sister_gift_like_level += 5
        else:
            $ sister_gift_like_level += 10
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show sis neutral_talk at right
        with dissolve
        sis "A gacha! Another for my collection. Nyehehehe~ I mean- thanks!"
    elif selecteditem.id ==  Items.gachayellow.id:
        if day == 3 or day == 4:
            $ sister_gift_like_level += 15
        elif day == 0:
            $ sister_gift_like_level += 5
        else:
            $ sister_gift_like_level += 10
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show sis shocked_talk at right
        with dissolve
        sis "I hope it's a rare one. Appreciate it, [povname]!"
    elif selecteditem.id ==  Items.socksflamingo.id:
        if day == 5 or day == 6:
            $ sister_gift_like_level += 40
        elif day == 1:
            $ sister_gift_like_level += 35
        else:
            $ sister_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show sis neutral_talk at right
        with dissolve
        sis "Fluffy socks! These are soooo cute, I can never get enough of these."
    elif selecteditem.id ==  Items.socksclouds.id:
        if day == 0 or day == 4:
            $ sister_gift_like_level += 40
        elif day == 3:
            $ sister_gift_like_level += 35
        else:
            $ sister_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show sis neutral_talk at right
        with dissolve
        sis "More socks! Thanks, dude. You know I love my fluffy socks."
    elif selecteditem.id ==  Items.sockslightning.id:
        if day == 1 or day == 3:
            $ sister_gift_like_level += 40
        elif day == 2:
            $ sister_gift_like_level += 35
        else:
            $ sister_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show sis neutral_talk at right
        with dissolve
        sis "These are pretty cool... but are they comfy? Yes, hell-fucking yes."
    elif selecteditem.id ==  Items.rainbowlollipop.id:
        $ sister_gift_like_level += 30
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show sis neutral_talk at right
        with dissolve
        sis "Wow! For me? You shouldn't have, I need to brush my teeth extra well later."
    else:
        show pov embarrassed at left
        with dissolve
        show sis confused_talk at right
        with dissolve
        if day == 2 or day == 4:
            sis "What do you want me to do with that?."
        elif day == 5 or day == 6:
            sis "Yeah, no thanks. Give that to someone else."
        else:
            sis "Why are you giving me this?"
        show sis confused at right
        pov "{i}Hmmm.. maybe she'd like something else.{/i}"
        $ selecteditem = None

        if gtime <= 1:
            jump lbl_sisterbedroom_day
        else:
            jump lbl_sisterbedroom_night

    ##else:#incase selcted item is not non but item not in inventory
    ##    jump lbl_comicbookstore_day_setup

    if sister_points == 0 and sister_gift_like_level >= 20:
        if sister_path >= 1:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 1 and sister_gift_like_level >= 40:
        if sister_path >= 4:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 2 and sister_gift_like_level >= 60:
        if sister_path >= 8:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 3 and sister_gift_like_level >= 80:
        if sister_path >= 12:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 4 and sister_gift_like_level >= 100:
        if sister_path >= 16:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 5 and sister_gift_like_level >= 120:
        if sister_path >= 20:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 6 and sister_gift_like_level >= 140:
        if sister_path >= 24:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 7 and sister_gift_like_level >= 160:
        if sister_path >= 28:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 8 and sister_gift_like_level >= 180:
        if sister_path >= 32:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif sister_points == 9 and sister_gift_like_level >= 200:
        if sister_path >= 34:
            call lbl_sister_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    else:
        pov "{i}Our relationship doesn't seem to have changed just yet.{/i}"
        pov "{i}A few more gifts may help us move to the next step.{/i}"

    if gtime <= 1:
        jump lbl_sisterbedroom_day
    else:
        jump lbl_sisterbedroom_night

label lbl_sister_giftgiving_success:
    $ sister_points += 1
    $ sister_gift_like_level = 0
    $ renpy.notify("Relationship with [sister] Increased")
    pov "{i}I can feel us getting closer.{/i}"
    return
