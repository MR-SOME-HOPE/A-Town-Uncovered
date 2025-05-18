## Pre Mom Movie Date ##
label lbl_pre_mom_movie_date:

    scene bg movieusher_night_2
    with dissolve
    ush "Yo, welcome. What can I get you this fine night?"
    show bg movieusher_night_1
    pov "Hey. Can I get two tickets."
    show bg movieusher_night_2
    ush "Sure, dude. That'll be $60 for two. What film are you feeling for tonight?"
    show bg movieusher_night_1

label lbl_pre_mom_movie_date_0:

    menu:
        "Action Movie." if inventory.money >= 60:
            pov "Tonight's action movie."
            show bg movieusher_night_3
            mum "Oooh, action movie, huh?"
            show bg movieusher_night_1
            pov "Yeah, figured it'd be a fun watch. How can you go wrong with martial arts and explosions."
            show bg movieusher_night_3
            mum "You sure you're not just looking for some ‘other' action? Y'know, with the love-interest."
            show bg movieusher_night_1
            if winc == 0:
                pov "Oh, please, [missus]. If I wanted that, we'd go to a romance movie."
            else:
                pov "Oh, please, Mom. If I wanted that, we'd go to a romance movie."
            show bg movieusher_night_2
            ush "Brother knows what he wants. You can't go wrong with the 3 B's. Bullets, Boobs and ka-Booms."
            show bg movieusher_night_1
            pov "Besides, the hero is always a Bond-esque looking hunk."
            show bg movieusher_night_3
            mum "Alright, I'm sold."
            $ moviedate_choice = 1

            jump lbl_mom_movie_date
        "Horror Movie." if inventory.money >= 60:
            pov "Tonight's horror movie."
            show bg movieusher_night_3
            mum "Oooh? Horror movie, huh? You know I'm not great with scary stuff."
            show bg movieusher_night_1
            pov "You can cling onto me if you want."
            show bg movieusher_night_3
            mum "Tch, sounds like you just read the first page of the ‘101 Date Night Ideas' book."
            show bg movieusher_night_1
            pov "Nyehehehe."
            show bg movieusher_night_2
            ush "She's onto you, man. You two enjoy the movie. No refunds if you choose to leave because it's too spoopy."
            show bg movieusher_night_1
            pov "Thanks. I'll take note of that."
            $ moviedate_choice = 2

            jump lbl_mom_movie_date
        "Romance Movie." if inventory.money >= 60:
            pov "Tonight's romance movie."
            show bg movieusher_night_3
            mum "Ooooh, romance movie huh? You're not just choosing that because you're with a girl are you?"
            show bg movieusher_night_1
            pov "Why? Would you rather not watch a romance movie?"
            show bg movieusher_night_3
            mum "You know me, I love my melancholy romantics."
            show bg movieusher_night_1
            pov "See?"
            show bg movieusher_night_2
            ush "Remember to hold her tight, my man. Here you guys go. Enjoy! And no funny business."
            show bg movieusher_night_1
            pov "Don't worry, we'll behave."
            $ moviedate_choice = 3

            jump lbl_mom_movie_date
        "Sci-fi Movie." if inventory.money >= 60:
            "This isn't available at the moment."

            jump lbl_pre_mom_movie_date_0
        "Indie Arthouse Movie" if inventory.money >= 60:
            "This isn't available at the moment."

            jump lbl_pre_mom_movie_date_0
        "I've changed my mind." if premoviedate_changemind == 0:
            pov "Actually, I've changed my mind. I don't want to buy any tickets."
            show bg movieusher_night_3
            mum "What...?!"
            show bg movieusher_night_1
            mum "Are you serious, [povname]? You made me get ready and come all the way down here to not watch a movie?"
            show bg movieusher_night_3
            mum "I'll pay for the movie if you're really that broke."

            menu:
                "Could you take tonight's ticket?":
                    show bg movieusher_night_1
                    pov "Could you take tonight's ticket actually? I promise it's just for tonight."
                    show bg movieusher_night_3
                    mum "{i}*Sigh*{/i} Fine. Only because I don't want to go home and have wasted my time."
                    show bg movieusher_night_1
                    mum "You choose the movie."
                    $ premoviedate_changemind = 1
                    $ inventory.money += 60

                    jump lbl_pre_mom_movie_date_0
                "I feel ill.":
                    show bg movieusher_night_1
                    pov "I actually, feel pretty ill all of a sudden. I'm sorry to ruin your night."
                    pov "I just don't think I'll be able to make it through the entire movie without passing out."
                    show bg movieusher_night_3
                    mum "... Oh. Okay... I guess we can go out another night then?"
                    show bg movieusher_night_1
                    pov "Yeah, definitely. I really am sorry."
                    show bg movieusher_night_3
                    mum "Let's go home then."
                    show bg movieusher_night_2
                    ush "Well... thanks for stopping by."
                    scene black
                    with dissolve
                    $ renpy.pause()
                    scene bg myhousefront_night
                    with dissolve
                    if mum_points >= 1:
                        $ mum_points -= 1
                    else:
                        $ mum_points = 0
                    if winc == 0:
                        $ renpy.notify("Your relationship with [missus] has decreased")
                    else:
                        $ renpy.notify("Your relationship with Mom has decreased")
                    $ moviedate = 0

                    jump lbl_myhousefront_night_setup
