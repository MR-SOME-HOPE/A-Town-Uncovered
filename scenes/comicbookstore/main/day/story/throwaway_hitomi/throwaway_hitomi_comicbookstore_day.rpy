## Throwaway Hitomi Comic Book Store Day Conversation ##
label lbl_comicbookstore_day_hitomi:
    default buyhitomi_points = 0

## Main Story Conversation
    ## Buukakki Followers Are Everywhere
    # if main_story == 151:
    #     jump lbl_buukakki_followers_are_everywhere_hitomi

## Side Story Conversation
    ## About Hitomi
    if hitomi_path == 0:
        jump lbl_about_hitomi
    ## Do You Know About Webcomics
    elif hitomi_path == 1:
        jump lbl_do_you_know_about_webcomics
    ## The Start of Something New
    elif hitomi_path == 2:
        jump lbl_the_start_of_something_new
    ## The Struggles of a Small Artist
    elif hitomi_path == 3:
        jump lbl_the_struggles_of_a_small_artist
    ## A Gift for Hitomi
    elif hitomi_path == 5 and model_level > 0:
        jump lbl_a_gift_for_hitomi
    ## A Gift for Hitomi Pt 2
    elif hitomi_path == 5.5 and inventory.has_item(Items.drawinganatomy):
        jump lbl_a_gift_for_hitomi_pt2
    elif hitomi_path == 6.1 or hitomi_path == 6.5:
        jump lbl_modelling_opportunities
    elif hitomi_path == 9:
        jump lbl_nerd_rebellion
    elif hitomi_path == 12:
        jump lbl_lewd_inspiration
    elif hitomi_path == 13:
        jump lbl_artistic_block
    elif hitomi_path == 18:
        jump lbl_art_inside_the_video_camera
    ## Invitation To Her Place
    elif hitomi_path == 22:
        if inventory.has_item(Items.hdcamera) and inventory.has_item(Items.lightingequipment):
            jump lbl_invitation_to_her_place
        else:
            pov "{i}I need to get both the hd camera and lighting equipment for Hitomi.{/i}"



    ## MENU
    #else:
    show btn_comicbookstore_day_hitomi_idle2
    if ( gtime == 1 and (main_story in (16,17,18,19,20,21,22,24,25,26,27) or main_story >= 35) ) or (gtime == 0 and day >= 5):
        show btn_comicbookstore_day_jacob_idle2
    menu:
        "A job" if 16 <= main_story <= 21 and nextday_ajob == 0 and comicbookstore_ajob == 0:
            hide btn_comicbookstore_day_hitomi_idle2
            jump lbl_comicbookstore_day_hitomi_ajob
        "Spare Boxes?" if sister_path == 29 and comicbookstore_spareboxes == 0:
            hide btn_comicbookstore_day_hitomi_idle2
            jump lbl_comicbookstore_day_hitomi_spareboxes
        "Talk":
            hide btn_comicbookstore_day_hitomi_idle2
            jump lbl_comicbookstore_day_hitomi_convo
        "Shop":
            show pov neutral at left
            with dissolve
            hide btn_comicbookstore_day_hitomi_idle2
            show hit neutral_talk at right
            with dissolve
            hit "Here's what we have."
            jump lbl_comicbookstoremenu
        "Give Gift" if selecteditem != None:
            jump lbl_hitomi_giftgiving
        "Nude Modeling"if hitomi_path > 7:
            if hitomi_path == 7.1:
                pov "{i}I should come back another day.{/i}"
                jump lbl_comicbookstore_day
            elif hitomi_path == 7.5:
                pov "I think I'm ready to try some more modeling."
                hit "Great! Give me a moment to set things up."
                jump skip_strike_a_pose
            else:
                pov "{i}Not right now.{/i}"
                jump lbl_comicbookstore_day
        "Invite to House for some fun" if hitomi_livingroomdoggy == 0:
            if hitomi_points <= 5:
                "You need 6 RP with Hitomi to access this scene."
                jump lbl_comicbookstore_day_hitomi
            else:
                #"Developer Note: This is a temporary feature and this'll be implemented more seemlessly in the future."
                "Meet Hitomi in your livingroom."
                $ hitomi_livingroomdoggy = 1
                jump lbl_comicbookstore_day_setup
        "Buy Relationship Points":
            #"Developer Note: This is a temporary feature that allows you to have enough points to view Hitomi's new h-scene."
            if hitomi_points <= 5:
                "You have [hitomi_points] and you need at least 6."
                menu:
                    "Buy +1 for $100":
                        if inventory.money <= 99:
                            pov "{i}I don't have enough money at the moment.{/i}"
                            jump lbl_comicbookstore_day_hitomi
                        else:
                            $ buyhitomi_points += 1
                            $ inventory.money -= 100
                            $ hitomi_points += 1
                            $ renpy.notify("Relationship with Hitomi Increased")
                            $ renpy.pause(1,hard=False)
                            $ renpy.notify("Current Balance: $[inventory.money]")
                            $ renpy.pause(1,hard=False)
                    "Nevermind":
                        jump lbl_comicbookstore_day
            else:
                "You already have enough Relationship Points."
            jump lbl_comicbookstore_day_hitomi

        "Decrease Bought Points" if buyhitomi_points >= 1:
            #"Developer Note: This is a temporary feature that allows you decrease her points by 1."
            #"Developer Note: You can only decrease the same amount of points that you've bought."
            menu:
                "Decrease by 1 point":
                    $ buyhitomi_points -= 1
                    if hitomi_points >= 1:
                        $ hitomi_points -= 1
                    else:
                        $ hitomi_points = 0
                    $ renpy.notify("Relationship with Hitomi Decreased")
                "Nevermind":
                    pass
            jump lbl_comicbookstore_day_hitomi

        "Nevermind.":
            jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 1 or date == 11 or date == 28 or date == 0:
            jump lbl_comicbookstore_day_hitomi_1
        elif date == 9 or date == 12 or date == 27:
            jump lbl_comicbookstore_day_hitomi_2
        elif date == 2 or date == 18 or date == 29:
            jump lbl_comicbookstore_day_hitomi_3
        elif date == 10 or date == 13 or date == 26:
            jump lbl_comicbookstore_day_hitomi_4
        elif date == 3 or date == 14 or date == 25:
            jump lbl_comicbookstore_day_hitomi_5
        elif date == 8 or date == 19 or date == 24:
            jump lbl_comicbookstore_day_hitomi_11
        elif date == 4 or date == 15 or date == 30:
            jump lbl_comicbookstore_day_hitomi_12
        elif date == 7 or date == 16 or date == 23:
            jump lbl_comicbookstore_day_hitomi_13
        elif date == 5 or date == 20 or date == 22:
            jump lbl_comicbookstore_day_hitomi_14
        elif date == 6 or date == 17 or date == 21:
            jump lbl_comicbookstore_day_hitomi_15
    elif gtime == 1:
        if date == 10 or date == 19 or date == 21 or date == 0:
            jump lbl_comicbookstore_day_hitomi_6
        elif date == 5 or date == 11 or date == 22:
            jump lbl_comicbookstore_day_hitomi_7
        elif date == 9 or date == 18 or date == 29:
            jump lbl_comicbookstore_day_hitomi_8
        elif date == 4 or date == 12 or date == 23:
            jump lbl_comicbookstore_day_hitomi_9
        elif date == 8 or date == 20 or date == 24:
            jump lbl_comicbookstore_day_hitomi_10
        elif date == 3 or date == 17 or date == 30:
            jump lbl_comicbookstore_day_hitomi_11
        elif date == 7 or date == 13 or date == 25:
            jump lbl_comicbookstore_day_hitomi_12
        elif date == 2 or date == 16 or date == 26:
            jump lbl_comicbookstore_day_hitomi_13
        elif date == 6 or date == 15 or date == 28:
            jump lbl_comicbookstore_day_hitomi_14
        elif date == 1 or date == 14 or date == 27:
            jump lbl_comicbookstore_day_hitomi_15

## Morning Exclusive
label lbl_comicbookstore_day_hitomi_1:
    show pov neutral at left
    with dissolve
    show hit neutral_talk at right
    with dissolve
    hit "Good morning, [povname]. Just browsing?"
    show pov neutral_talk at left
    show hit neutral at right
    pov "Morning, hitomi. Yeah. Just looking around for stuff."
    show pov neutral at left
    show hit smirk_talk at right
    hit "Manga? Comics? Other... misc... behind the counter stuff?"
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "Nothing specific. I'll let you know if something comes up."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_2:
    show pov neutral at left
    with dissolve
    show hit neutral_talk at right
    with dissolve
    hit "Morning there. You meeting up with the guys?"
    show pov confused_talk at left
    show hit neutral at right
    pov "The guys?"
    show pov confused at left
    show hit confused_talk at right
    hit "Kevin and the boys?"
    show pov confused_talk at left
    show hit confused at right
    pov "Lord Kevlamin? It's weird calling them 'the guys'."
    show pov confused at left
    show hit confused_talk at right
    hit "What do prefer to call them?"
    show pov smirk_talk at left
    show hit smirk at right
    pov "'The kids', 'children', 'losers'. Just something more appropriate."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_3:
    show pov confused at left
    with dissolve
    show hit neutral_talk at right
    with dissolve
    hit "Did you you see the latest volume of Kira-Kira-Hapi-Hapi."
    show pov confused_talk at left
    show hit neutral at right
    pov "I'm guessing that came out recently?"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Just now actually, I'm reading it at the moment and my heart..."
    show pov smirk at left
    hit "I love this series."
    hit "If bubblegum flavoured icecream covered with rose infused white chocolate was a book-"
    show hit neutral_talk at right
    hit "This would be it."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_4:
    show pov smirk_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Morning starshine, the Earth says 'hello!'"
    show pov neutral at left
    show hit neutral_talk at right
    hit "Billy Bonka, right?"
    show pov smirk_talk at left
    show hit neutral at right
    pov "The legend himself."
    show pov confused at left
    show hit smirk_talk at right
    hit "Where do you think Billy Bonka ranks in richest person on Earth?"
    show pov smirk_talk at left
    show hit smirk at right
    pov "Superior technology, universally loved products, killer haircut and top hat."
    pov "I bet he's richer than the next two people combined."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_5:
    show pov neutral_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Hey, sleep well last night?"
    show pov confused at left
    show hit neutral_talk at right
    hit "Like a baby."
    show pov embarrassed_talk at left
    show hit smirk at right
    pov "I don't think babies are the best example of a good night's rest."
    show pov smirk at left
    show hit confused_talk at right
    hit "I blame the TV, I wish Webflix didn't stop midthrough a binge-watch to ask if you're still watching."
    hit "I rely on the white noise to get me through the night."
    show pov neutral_talk at left
    show hit neutral at right
    pov "Hear hear."

    jump lbl_comicbookstore_day

## Afternoon Exclusive
label lbl_comicbookstore_day_hitomi_6:
    show pov smirk_talk at left
    with dissolve
    show hit confused at right
    with dissolve
    pov "Hey, Hitomi. I see Jacob glancing at you from over there."
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "He always does that."
    show pov confused_talk at left
    show hit embarrassed at right
    pov "I feel like at some point, it's gotten creepy, hasn't it?"
    show pov confused at left
    show hit neutral_talk at right
    hit "He's harmless for the most part."
    show pov embarrassed at left
    hit "I find it amusing actually."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_7:
    show pov neutral_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Afternoon to you. Your hair looks great today."
    show pov neutral at left
    show hit neutral_talk at right
    hit "Thanks! I retouched the ends last night."
    show pov smirk_talk at left
    show hit confused at right
    pov "Have you tried any other colour besides green?"
    show pov shocked at left
    show hit confused_talk at right
    hit "Why do you not like green?"
    show pov shocked_talk at left
    show hit smirk at right
    pov "No, not at all! I- mean yes! Yes, I like green."
    show pov embarrassed at left
    show hit confused_talk at right
    hit "Don't tell me you want me to have purple streaks. There's enough of those in the media."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_8:
    show pov neutral at left
    with dissolve
    show hit neutral_talk at right
    with dissolve
    hit "What are you doing later tonight, [povname]?"
    show pov embarrassed_talk at left
    show hit smirk at right
    pov "I have no idea. I'll let the flow of the universe take me where ever."
    show pov neutral at left
    show hit smirk_talk at right
    hit "You're always in the hands of someone else, aren't you?"
    show pov confused_talk at left
    show hit confused at right
    pov "It kinda feels that way, doesn't it? At the most subconscious of subconscious levels."
    show pov shocked at left
    show hit smirk_talk at right
    hit "Sort of like 'The Falseman Show'."
    show pov bored_talk at left
    show hit embarrassed at right
    pov "...Great. Now I'm wondering if you're just an actor and I'm the star of my own TV show..."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_9:
    show pov neutral_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Whatcha reading this afternoon, Miss Hitomi?"
    show pov neutral at left
    show hit neutral_talk at right
    hit "Just this manga called 'Chan-chan-sama'."
    show pov confused at left
    hit "It's about this girl named Chan-chan who has the power of having powers."
    show pov confused_talk at left
    show hit neutral at right
    pov "The power of having powers?"
    show pov bored at left
    show hit smirk_talk at right
    hit "Yeah, she's the only one with powers in this universe so it automatically makes her powerful."
    show pov bored_talk at left
    show hit smirk at right
    pov "That doesn't even make sense."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_10:
    show pov confused at left
    with dissolve
    show hit confused_talk at right
    with dissolve
    hit "Have you heard?"
    show pov confused_talk at left
    show hit confused at right
    pov "About what? Did something happen around here?"
    show pov shocked at left
    show hit confused_talk at right
    hit "Yeah, someone broke in here last night. Same guy, didn't steal anything though."
    show pov confused_talk at left
    show hit confused at right
    pov "Why'd he break in here?"
    show pov shocked at left
    show hit sad_talk at right
    hit "He was just staring at the anime figurines like a total hypnotized, demonic creep-show."
    show pov confused at left
    show hit confused_talk at right
    hit "And then he just... left. What the actual hell, right?"

    jump lbl_comicbookstore_day

## Interchangeable
label lbl_comicbookstore_day_hitomi_11:
    show pov confused_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Do those dudes in the back ever come out into the sun?"
    show pov confused at left
    show hit embarrassed_talk at right
    hit "I- don't know."
    show pov smirk at left
    show hit neutral_talk at right
    hit "I honestly forget that they're even back there sometimes."
    show pov confused_talk at left
    show hit neutral at right
    pov "Kevlamin seems pretty loud though."
    show pov smirk at left
    show hit smirk_talk at right
    hit "It's like a ticking clock. After a while, your brain just sorta ignores what it deems irrelevant."
    show pov smirk_talk at left
    show hit smirk at right
    pov "Coudln't have said it better myself."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_12:
    show pov neutral at left
    with dissolve
    show hit shocked_talk at right
    with dissolve
    hit "Oh! [povname]. Thank Buddude you're here."
    show pov smirk_talk at left
    show hit neutral at right
    pov "Hey, what's up?"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "It's just good to see a face that I don't want to punch."
    show pov smirk_talk at left
    show hit embarrassed at right
    pov "Hashtag such a mood."
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "{i}*Sigh*{/i} I can't wait to peace out of this job."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_13:
    show pov sad_talk at left
    with dissolve
    show hit bored at right
    with dissolve
    pov "What's that smell?"
    show pov sad at left
    show hit bored_talk at right
    hit "The dungeon dwellers in there got some food delivered here."
    show pov confused at left
    hit "It's either some really funky Chinese takeout or they're eating goat testicles."
    show pov smirk_talk at left
    show hit bored at right
    pov "What's the difference, am I right?! Hahahaha."
    show pov smirk at left
    hit "..."
    show pov bored at left
    show hit bored_talk at right
    hit "Everyone knows goat testicles is a North African delicacy."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_14:
    show pov confused_talk at left
    with dissolve
    show hit confused at right
    with dissolve
    pov "Hey, what's the deal with Davendithas?"
    show pov confused at left
    show hit confused_talk at right
    hit "Realistically, I think he's a mute."
    show pov embarrassed_talk at left
    show hit confused at right
    pov "Yeah, that's what I figured as well."
    show pov shocked at left
    show hit confused_talk at right
    hit "But legend has it that he's been heard by a some and has the voice of God."
    show hit smirk_talk at right
    hit "Although those who {i}have{/i} heard his voice haven't lived to tell such tale."
    show pov smirk_talk at left
    show hit smirk at right
    pov "God damn... he's suddenly the most interesting person I've ever met."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_hitomi_15:
    show pov neutral_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Any recommendations for today?"
    show pov confused at left
    show hit neutral_talk at right
    hit "Have you heard of 'The Horny Huntress'?"
    show pov confused_talk at left
    show hit smirk at right
    pov "What's that about?"
    show pov neutral at left
    show hit smirk_talk at right
    hit "An old-school rogue assassin who time travelled two centuries into the future."
    show pov confused at left
    show hit smirk_talk at right
    hit "She got the title of 'Horny Huntress' not because she was horny but because of her signature move, 'the viking headbutt'."
    show pov smirk_talk at left
    show hit smirk at right
    pov "Sounds kinky, I'll check it out sometime."

    jump lbl_comicbookstore_day

## GIFT GIVING
label lbl_hitomi_giftgiving:
    ##if inventory.has_item(selecteditem):
        ##if HitomiAcceptedItems():
    #"Developer Note: Because Hitomi doesn't have an official side story yet, you may currently max out her stats to access the community-suggested H-scenes that she has available."
    if selecteditem.id == Items.hairdyegreen.id:
        $ hitomi_gift_like_level += 65
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show hit neutral_talk at right
        with dissolve
        hit "Damn! Thanks a ton, [povname]. This will make sure my hair stays vibrant AF."
    elif selecteditem.id ==  Items.essentialoilcitrus.id:
        if day == 1 or day == 4:
            $ hitomi_gift_like_level += 45
        elif day == 6:
            $ hitomi_gift_like_level += 35
        else:
            $ hitomi_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show hit neutral_talk at right
        with dissolve
        hit "Mmm~ This smells so good. Definitely will help mask the readdit smell in here."
    elif selecteditem.id ==  Items.essentialoilpeppermint.id:
        if day == 0 or day == 3:
            $ hitomi_gift_like_level += 45
        elif day == 2:
            $ hitomi_gift_like_level += 35
        else:
            $ hitomi_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show hit neutral_talk at right
        with dissolve
        hit "Oooh~ Minty. I can never say no to essential oils. I'd pass out from all the male musk otherwise."
    elif selecteditem.id ==  Items.essentialoillavender.id:
        if day == 2 or day == 5:
            $ hitomi_gift_like_level += 45
        elif day == 4:
            $ hitomi_gift_like_level += 35
        else:
            $ hitomi_gift_like_level += 40
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show hit neutral_talk at right
        with dissolve
        hit "Is it weird that I kinda wanna down this. I'm joking, don't worry. Thanks, [povname]!"
    elif selecteditem.id == Items.pepperochocolate.id:
        if day == 3 or day == 6:
            $ hitomi_gift_like_level += 20
        elif day == 2:
            $ hitomi_gift_like_level += 10
        else:
            $ hitomi_gift_like_level += 15
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show hit neutral_talk at right
        with dissolve
        hit "Oooh! Yummo, I love these! Spicy chocolate is honestly so underrated."
    elif selecteditem.id == Items.pepperopeanutbutter.id:
        if day == 0 or day == 4:
            $ hitomi_gift_like_level += 20
        elif day == 1:
            $ hitomi_gift_like_level += 10
        else:
            $ hitomi_gift_like_level += 15
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show hit neutral_talk at right
        with dissolve
        hit "You. Are. The bomb, [povname]. I love peanut butter pepper-os."
    elif selecteditem.id == Items.pepperostrawberry.id:
        if day == 1 or day == 5:
            $ hitomi_gift_like_level += 20
        elif day == 0:
            $ hitomi_gift_like_level += 10
        else:
            $ hitomi_gift_like_level += 15
        $ inventory.drop(selecteditem)
        $ selecteditem = None
        show pov neutral at left
        with dissolve
        show hit neutral_talk at right
        with dissolve
        hit "Strawberry flavour's usually a hit or a miss but these are amaze-balls. Snack break!"
    else:
        show pov embarrassed at left
        with dissolve
        show hit embarrassed_talk at right
        with dissolve
        if day == 1 or day == 4:
            hit "No thanks. You can keep it."
        elif day == 2 or day == 5:
            hit "Thanks, but I don't have a need for it."
        else:
            hit "Sorry, I don't really like those."
        show hit embarrassed at right
        pov "{i}Hmmm.. maybe she'd like something else.{/i}"
        $ selecteditem = None

        jump lbl_comicbookstore_day

    ##else:#incase selcted item is not non but item not in inventory
    ##    jump lbl_comicbookstore_day_setup

    if hitomi_points == 0 and hitomi_gift_like_level >= 20:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 1 and hitomi_gift_like_level >= 40:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 2 and hitomi_gift_like_level >= 60:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 3 and hitomi_gift_like_level >= 80:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 4 and hitomi_gift_like_level >= 100:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 5 and hitomi_gift_like_level >= 120:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 6 and hitomi_gift_like_level >= 140:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 7 and hitomi_gift_like_level >= 160:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 8 and hitomi_gift_like_level >= 180:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    elif hitomi_points == 9 and hitomi_gift_like_level >= 200:
        $ hitomi_points += 1
        $ hitomi_gift_like_level = 0
        $ renpy.notify("Relationship with Hitomi Increased")
        pov "{i}I can feel us getting closer.{/i}"
    else:
        pov "{i}Our relationship doesn't seem to have changed just yet.{/i}"
        pov "{i}A few more gifts may help us move to the next step.{/i}"

    jump lbl_comicbookstore_day
