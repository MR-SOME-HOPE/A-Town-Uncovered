## Throwaway Director Lashley Director Office Day Conversation
label lbl_principaloffice_day_principallashley:
    default buyprincipallashleypoints = 0
    show btn principaloffice_day_principallashley_idle
    $ renpy.pause(0.001)

    ## Main Story
    ## Answers Around Town Sexworld
    if main_story <= 40 and insexworld == 1:
        jump lbl_principaloffice_day_principallashley_sexworld
    else:
        menu:
            "Spare Boxes?" if sister_path == 29 and principaloffice_spareboxes == 0:
                jump lbl_principaloffice_day_principallashley_spareboxes
            "Talk":
                jump lbl_principaloffice_day_principallashley_convo
            "Give Gift" if selecteditem != None and principallashley_path >= 10:
                jump lbl_principallashley_giftgiving
            # "Buy Relationship Points":
            #     "Developer Note: This is a temporary feature that allows you to have enough points to view Director Lashley's new h-scene."
            #     if principallashley_points <= 7:
            #         "You have [principallashley_points] and you need at least 8."
            #         menu:
            #             "Buy +1 for $100":
            #                 if inventory.money <= 99:
            #                     pov "{i}I don't have enough money at the moment.{/i}"
            #                     jump lbl_principaloffice_day_setup
            #                 else:
            #                     $ buyprincipallashleypoints += 1
            #                     $ inventory.money -= 100
            #                     $ principallashley_points += 1
            #                     $ renpy.notify("Relationship with Director Lashley Increased")
            #                     $ renpy.pause(1,hard=False)
            #                     $ renpy.notify("Current Balance: $[inventory.money]")
            #                     $ renpy.pause(1,hard=False)
            #             "Nevermind":
            #                 jump lbl_principaloffice_day_principallashley
            #     else:
            #         "You already have enough Relationship Points."
            #     jump lbl_principaloffice_day_setup
            # "Decrease Bought Points" if buyprincipallashleypoints >= 1:
            #     "Developer Note: This is a temporary feature that allows you decrease her points by 1."
            #     "Developer Note: You can only decrease the same amount of points that you've bought."
            #     menu:
            #         "Decrease by 1 point":
            #             $ buyprincipallashleypoints -= 1
            #             if principallashley_points >= 1:
            #                 $ principallashley_points -= 1
            #             else:
            #                 $ principallashley_points = 0
            #             $ renpy.notify("Relationship with Director Lashley Decreased")
            #         "Nevermind":
            #             pass
            #     jump lbl_principaloffice_day_setup
            "Ask to movie date" if moviedate == 0 and principallashley_path >= 27:
                jump lbl_principaloffice_day_lashley_moviedate
            "Fun in her Office Chair." if principallashley_points >= 8:
                jump lbl_principal_office_chair_sex
            "Fun at the Cafeteria After School." if principallashley_points >= 8:
                jump lbl_lashley_cafeteria_doggy_pre
            "Fun quickie on the Desk." if principallashley_points >= 8:
                jump lbl_lashley_bent_over_desk
            "Nevermind":
                jump lbl_principaloffice_day

    ## Side Story
        ## Nothing

    jump lbl_principaloffice_day_principallashley_convo

label lbl_principaloffice_day_principallashley_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 1 or date == 20 or date == 30 or date == 31:
            jump lbl_principaloffice_day_principallashley_1
        elif date == 10 or date == 11 or date == 29:
            jump lbl_principaloffice_day_principallashley_2
        elif date == 2 or date == 12 or date == 26:
            jump lbl_principaloffice_day_principallashley_3
        elif date == 9 or date == 13 or date == 25:
            jump lbl_principaloffice_day_principallashley_4
        elif date == 3 or date == 14 or date == 24:
            jump lbl_principaloffice_day_principallashley_5
        elif date == 8 or date == 15 or date == 22:
            jump lbl_principaloffice_day_principallashley_11
        elif date == 4 or date == 17 or date == 21:
            jump lbl_principaloffice_day_principallashley_12
        elif date == 7 or date == 16 or date == 23:
            jump lbl_principaloffice_day_principallashley_13
        elif date == 6 or date == 19 or date == 27:
            jump lbl_principaloffice_day_principallashley_14
        elif date == 5 or date == 18 or date == 28:
            jump lbl_principaloffice_day_principallashley_15
    elif gtime == 1:
        if date == 8 or date == 16 or date == 29 or date == 31:
            jump lbl_principaloffice_day_principallashley_6
        elif date == 6 or date == 17 or date == 21:
            jump lbl_principaloffice_day_principallashley_7
        elif date == 5 or date == 18 or date == 22:
            jump lbl_principaloffice_day_principallashley_8
        elif date == 10 or date == 19 or date == 23:
            jump lbl_principaloffice_day_principallashley_9
        elif date == 4 or date == 20 or date == 24:
            jump lbl_principaloffice_day_principallashley_10
        elif date == 3 or date == 15 or date == 30:
            jump lbl_principaloffice_day_principallashley_11
        elif date == 2 or date == 14 or date == 25:
            jump lbl_principaloffice_day_principallashley_12
        elif date == 9 or date == 13 or date == 26:
            jump lbl_principaloffice_day_principallashley_13
        elif date == 7 or date == 12 or date == 28:
            jump lbl_principaloffice_day_principallashley_14
        elif date == 1 or date == 11 or date == 27:
            jump lbl_principaloffice_day_principallashley_15

## Morning Exclusive
label lbl_principaloffice_day_principallashley_1:
    show pov neutral at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "Good morning, [povname]. What can I help you with on this beautiful day?"
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Nothing really, I was just stumbling around looking for something."
    show pov neutral at left
    show pri neutral_talk at right
    pri "Well, I surely hope you find what you're looking for."
    pri "I wish you a bright rest of the day, God bless."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_2:
    show pov neutral at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "Good day there, [povname]. What brings you here this fine morning?"
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Oh, sorry. I thought this was the bathroom."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Hahaha, I can understand the confusion, [povname]."
    pri "It is still quite early. Well, best you run along."
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Right, sorry again, Ms. Lashley."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "God is always watching."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_3:
    show pov neutral at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "Good morning. I wasn't expecting you this morning."
    show pov smirk_talk at left
    show pri confused at right
    pov "Oh, hey! I wasn't expecting you here either."
    show pov neutral at left
    show pri smirk_talk at right
    pri "Well, this {i}is{/i} my office after all."
    show pri neutral_talk at right
    pri "Are you looking for someone to talk to?"
    show pov confused_talk at left
    show pri neutral at right
    pov "Someone to talk t- what? No. I mean, no thank you."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Well, I do have some work to get done. You should head to class."
    pri "Jesus will walk beside you."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_4:
    show pov neutral_talk at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral at right
    call lbl_principaloffice_counter_check
    with dissolve
    pov "Good morning, Director Lashley."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Good morning, [povname]. Are you here for a quick prayer?"
    show pov embarrassed_talk at left
    show pri confused at right
    pov "I- um... am late for class?"
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Very well. I will pray for you and your treacherous journey."
    pri "Safe travels, [povname]. God will guide your way."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_5:
    show pov neutral_talk at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral at right
    call lbl_principaloffice_counter_check
    with dissolve
    pov "Hi, Director Lashley."
    show pov neutral at left
    show pri neutral_talk at right
    pri "Now's a perfect time. I had just finished up my morning prayers."
    show pov embarrassed_talk at left
    show pri smirk at right
    pov "I just wanted to drop by to see if you're doing well."
    show pov neutral at left
    show pri smirk_talk at right
    pri "That's very kind of you, [povname]. I am very well."
    show pri neutral_talk at right
    pri "The day has barely begun and you've already made it a terrific one."
    show pov embarrassed at left
    pri "I will put in a good word to the Lord on your behalf."

    jump lbl_principaloffice_day

## Afternoon Exclusive
label lbl_principaloffice_day_principallashley_6:
    show pov neutral at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "Good afternoon, [povname]. How were your classes today?"
    show pov neutral_talk at left
    show pri neutral at right
    pov "Oh, y'know. Same old class, same old teacher, same old work."
    show pov confused at left
    show pri neutral_talk at right
    pri "At least it's consistently old, don't you think?"
    show pov confused_talk at left
    show pri neutral at right
    pov "I mean, I don't know. What kind of response is that?"
    show pov confused at left
    show pri neutral_talk at right
    pri "Hahaha, I'm just tickling your funny bone, [povname]."
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "Jesus loves you, yes, I know. For the bible tells me so."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_7:
    show pov neutral at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "[povname]! There you are!"
    show pov confused_talk at left
    show pri neutral at right
    pov "Afternoon, Miss Principal. Were you looking for me?"
    show pov confused at left
    show pri confused_talk at right
    pri "I- think? Didn't your teacher send you up here?"
    show pov confused_talk at left
    show pri confused at right
    pov "No, I came on my own accord."
    show pov confused at left
    show pri confused_talk at right
    pri "What for?"
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "To... wish you a blessed day?"
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "And have a blessed day to you too, [povname]."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_8:
    show pov confused at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri confused_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "What is it this time? Can't you see I'm in the middle of-"
    show pri embarrassed_talk at right
    pri "Oh! [povname]! Excuse me, I thought you were someone else."
    show pov embarrassed_talk at left
    show pri embarrassed at right
    pov "I hope I wasn't interrupting something."
    show pov embarrassed at left
    show pri shocked_talk at right
    pri "N-n-n-n-n-nooo, of course not."
    show pov confused at left
    show pri embarrassed_talk at right
    pri "I was just... working."
    show pov confused_talk at left
    show pri embarrassed at right
    pov "I should just go... um, Happy Jesus Day or something."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_9:
    show pov neutral_talk at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral at right
    call lbl_principaloffice_counter_check
    with dissolve
    pov "Hi, Director Lashley."
    show pov confused at left
    show pri neutral_talk at right
    pri "Just the person I was looking for. I can't seem to see anything on my screen. It's just black."
    show pov confused_talk at left
    show pri confused at right
    pov "I don't think I'm actually the person but did you turn on the monitor?"
    show pov shocked at left
    show pri confused_talk at right
    pri "Did you ask if I seduced the hallway monitor?"
    show pov shocked_talk at left
    show pri shocked at right
    pov "What?! No, the computer screen, I can see that it's off."
    show pov embarrassed at left
    show pri embarrassed_talk at right
    pri "Oh! Hahaha, silly me. Forgive me, God for I have thought of sinful imagery."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_10:
    show pov neutral at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "Afternoon, my beautiful student."
    show pov smirk_talk at left
    show pri neutral at right
    pov "Afternoon, my beautiful administrator."
    show pov smirk at left
    show pri smirk_talk at right
    pri "Well, aren't you an angel sent down from the heavens."
    pri "Are you always making people's days?"
    show pov smirk_talk at left
    show pri smirk at right
    pov "Only always."
    show pov smirk at left
    show pri neutral_talk at right
    pri "Well, don't let me get in your way. May the prayers be with you."

    jump lbl_principaloffice_day

## Interchangable
label lbl_principaloffice_day_principallashley_11:
    show pov confused at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri confused_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "Hey, [povname]. In trouble again?"
    show pov smirk_talk at left
    show pri neutral at right
    pov "Not this time. I just came by to see if {i}you're{/i} the one in need of assistance."
    show pov neutral at left
    show pri neutral_talk at right
    pri "Oh, that's very kind of you but nothing at the moment. Just some paperwork that I have to do myself."
    show pri confused_talk at right
    pri "Don't you have some coursework assignment yourself? You should get on that.."
    show pov embarrassed_talk at left
    show pri smirk at right
    pov "Don't worry, I will."
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "Remember, God will look out for you in your time of need."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_12:
    show pov confused_talk at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral at right
    call lbl_principaloffice_counter_check
    with dissolve
    pov "It's really hot in here, isn't it?"
    show pov confused at left
    show pri neutral_talk at right
    pri "I like it. I prefer a little heat than an annoying cold."
    show pov smirk_talk at left
    show pri neutral at right
    pov "Can't argue with that I guess. It's your office."
    show pov embarrassed at left
    show pri confused_talk at right
    pri "Speaking of, why are you in here? You come here more often than necessary."
    show pov smirk_talk at left
    show pri smirk at right
    pov "I really don't know. Your office just has this unbelievable force that pulls me in."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "The power of the Lord is a mighty one, [povname]. You know you're always welcome here."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_13:
    show pov neutral_talk at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral at right
    call lbl_principaloffice_counter_check
    with dissolve
    pov "Hi, Ms. Lashley."
    show pov smirk_talk at left
    pov "Lots of paperwork to get through?"
    show pov shocked at left
    show pri smirk_talk at right
    pri "Why? Are you offering to assist me with them."
    show pov embarrassed_talk at left
    show pri smirk at right
    pov "I think I would screw something up."
    show pov confused at left
    show pri smirk_talk at right
    pri "There are no mistakes, [povname]. Just happy little accidents."
    show pov embarrassed at left
    pri "Anyway, I have to get back to work. Happy studying, and God bless."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_14:
    show pov neutral_talk at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri neutral at right
    call lbl_principaloffice_counter_check
    with dissolve
    pov "Hey, did you eat yet?"
    show pov embarrassed at left
    show pri confused_talk at right
    pri "Why do you ask? Did you make something for me?"
    show pov embarrassed_talk at left
    show pri smirk at right
    pov "Oh, sorry, no. It's just a habit of mine to talk about food."
    show pov confused at left
    show pri smirk_talk at right
    pri "I can't argue with that. Food is love, food is life."
    show pov confused_talk at left
    show pri confused at right
    pov "Did you just quote a meme."
    show pov bored at left
    show pri confused_talk at right
    pri "God is the creator of love, God is the creator of life."

    jump lbl_principaloffice_day

label lbl_principaloffice_day_principallashley_15:
    show pov shocked at left
    with dissolve
    hide btn principaloffice_day_principallashley_idle
    show pri confused_talk at right
    call lbl_principaloffice_counter_check
    with dissolve
    pri "[povname]? What are you doing here?"
    show pov embarrassed_talk at left
    show pri confused at right
    pov "I saw that the door was open so I-"
    show pov embarrassed at left
    show pri confused_talk at right
    pri "Decided to barge in here without knocking?"
    show pri confused at right
    pov "..."
    show pov embarrassed_talk at left
    pov "I knocked, didn't I?"
    show pov embarrassed at left
    show pri confused_talk at right
    pri "You never knock."
    show pov embarrassed_talk at left
    show pri bored at right
    pov "Then I wonder why you're so surprised."

    jump lbl_principaloffice_day

## GIFT GIVING
label lbl_principallashley_giftgiving:
    ##if inventory.has_item(selecteditem):
        ##if principallashleyAcceptedItems():
    if selecteditem.id ==  Items.kidsbible.id:
        $ principallashley_gift_like_level += 60
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if day <= 4:
            show pri neutral_talk at right
        else:
            show pri neutral_talk at right
        with dissolve
        pri "[povname]! This is fantastic, I can give this out as a prize to the kids at Youth group!"
    elif selecteditem.id ==  Items.bible.id:
        $ principallashley_gift_like_level += 90
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        if day <= 4:
            show pri neutral_talk at right
        else:
            show pri neutral_talk at right
        with dissolve
        pri "Oh, bless your kind soul, [povname]. Although I won't keep it for myself, I can give it to a lost soul who needs it."
    # elif selecteditem.id ==  Items.pornmag.id:
    #     if day == 1 or day == 3:
    #         $ principallashley_gift_like_level += 40
    #     elif day == 2:
    #         $ principallashley_gift_like_level += 35
    #     else:
    #         $ principallashley_gift_like_level += 40
    #     $ inventory.drop(selecteditem)
    #     $ selecteditem = None
    #     show pov neutral at left
    #     with dissolve
    #     if day <= 4:
    #         show pri neutral_talk at right
    #     else:
    #         show pri neutral_talk at right
    #     with dissolve
    #     pri "Lightnight socks? And they're fluffy? I love them! Thanks so much, [povname]."
    else:
        show pov embarrassed at left
        with dissolve
        if day <= 4:
            show pri confused_talk at right
        else:
            show pri confused_talk at right
        with dissolve
        if day == 3 or day == 5:
            pri "Bless your heart, [povname] but I can't accept that, it's too much."
        elif day == 2 or day == 6:
            pri "May I suggest donating this to the local thrift store. Someone may come to find it more useful than I."
        else:
            pri "How sweet but I'll have to respectfully decline this gift, there are people who need it more than me."
        show pri confused at right
        pov "{i}Hmmm.. maybe she'd like something else.{/i}"
        $ selecteditem = None

        jump lbl_principaloffice_day

    ##else:#incase selcted item is not non but item not in inventory
    ##    jump lbl_comicbookstore_day_setup

    if principallashley_points == 0 and principallashley_gift_like_level >= 20:
        if principallashley_path >= 1:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 1 and principallashley_gift_like_level >= 40:
        if principallashley_path >= 3:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 2 and principallashley_gift_like_level >= 60:
        if principallashley_path >= 5:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 3 and principallashley_gift_like_level >= 80:
        if principallashley_path >= 7:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 4 and principallashley_gift_like_level >= 100:
        if principallashley_path >= 9:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 5 and principallashley_gift_like_level >= 120:
        if principallashley_path >= 11:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 6 and principallashley_gift_like_level >= 140:
        if principallashley_path >= 13:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 7 and principallashley_gift_like_level >= 160:
        if principallashley_path >= 15:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 8 and principallashley_gift_like_level >= 180:
        if principallashley_path >= 18:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    elif principallashley_points == 9 and principallashley_gift_like_level >= 200:
        if principallashley_path >= 20:
            call lbl_principallashley_giftgiving_success
        else:
            pov "{i}I don't think our relationship can go further at this stage.{/i}"
    else:
        pov "{i}Our relationship doesn't seem to have changed just yet.{/i}"
        pov "{i}A few more gifts may help us move to the next step.{/i}"

    jump lbl_principaloffice_day

label lbl_principallashley_giftgiving_success:
    $ principallashley_points += 1
    $ principallashley_gift_like_level = 0
    $ renpy.notify("Relationship with Director Lashley Increased")
    pov "{i}I can feel us getting closer.{/i}"
    return
