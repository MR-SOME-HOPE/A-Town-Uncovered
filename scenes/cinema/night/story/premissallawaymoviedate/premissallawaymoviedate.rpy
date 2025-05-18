## Pre Miss Allaway Movie Date ##
label lbl_pre_missallaway_movie_date:

    scene bg movieusher_night_2
    with dissolve
    ush "Yo, welcome. What can I get you this fine night?"
    show bg movieusher_night_1
    pov "Hey. Can I get two tickets."
    show bg movieusher_night_2
    ush "Sure, dude. That'll be $60 for two. What film are you feeling for tonight?"
    show bg movieusher_night_1

label lbl_pre_missallaway_movie_date_0:

    menu:
        "Action Movie." if inventory.money >= 60:
            pov "Tonight's action movie."
            show bg movieusher_night_3
            mis "Hell yeah!"
            show bg movieusher_night_1
            pov "I figured tonight will be about guns and explosions."
            show bg movieusher_night_3
            mis "{i}*Sniff*{/i} You know me so well."
            show bg movieusher_night_1
            pov "Oh, please, Miss. If I wanted your sappy side, we'd go to a romance movie."
            show bg movieusher_night_2
            ush "Brother knows what's what. You can't go wrong with the 3 B's. Bullets, Boobs and ka-Booms."
            show bg movieusher_night_1
            pov "Besides, the hero is always a Bond-esque lookin-"
            show bg movieusher_night_3
            mis "Screw the hero, I just hope there's a sexy ass-kicking girl."
            show bg movieusher_night_2
            ush "Sounds like you have a keeper, my man."
            $ moviedate_choice = 1

            jump lbl_missallaway_movie_date
        "Horror Movie." if inventory.money >= 60:
            pov "Tonight's horror movie."
            show bg movieusher_night_3
            mis "Really...? Horror...?."
            show bg movieusher_night_1
            pov "You can cling onto me if you want."
            show bg movieusher_night_3
            mis "As long as it's not about ghosts. I have a thing about ghosts..."
            mis "I will legit leave mid-way if you do any scary pranks on me, y'know how jump I can get."
            show bg movieusher_night_2
            ush "Hey, just an FYI. No refunds if you choose to leave mid-way."
            show bg movieusher_night_1
            mis "Don't worry, my date here knows what he's paying for."
            show bg movieusher_night_1
            pov "I kinda, maybe, might regret this later..."
            $ moviedate_choice = 2

            jump lbl_missallaway_movie_date
        "Romance Movie." if inventory.money >= 60:
            pov "Tonight's romance movie."
            show bg movieusher_night_3
            mis "You're not just picking that because I'm a girl, right?"
            show bg movieusher_night_1
            pov "Why? Would you rather not watch a romance movie?"
            show bg movieusher_night_3
            mis "N-no. No, it's up to you. Heck, maybe I'll end up enjoying it."
            show bg movieusher_night_1
            pov "Yeah, who knows? Maybe it'll surprise you and pull on your heart strings."
            show bg movieusher_night_2
            ush "Remember to hold her tight, my man. Here you guys go. Enjoy! And no funny business."
            show bg movieusher_night_1
            pov "Don't worry, we'll behave."
            $ moviedate_choice = 3

            jump lbl_missallaway_movie_date
        "Sci-fi Movie." if inventory.money >= 60:
            "This isn't available at the moment."

            jump lbl_pre_missallaway_movie_date_0
        "Indie Arthouse Movie" if inventory.money >= 60:
            "This isn't available at the moment."

            jump lbl_pre_missallaway_movie_date_0
        "I've changed my mind." if premoviedate_changemind == 0:
            pov "Actually, I've changed my mind. I don't want to buy any tickets."
            show bg movieusher_night_3
            mis "What...?!"
            show bg movieusher_night_1
            mis "C'mon! Don't be like that, I was really looking forward for tonight's movie!"
            show bg movieusher_night_3
            mis "What's wrong?"

            menu:
                "Could you take tonight's ticket?":
                    show bg movieusher_night_1
                    pov "Could you take tonight's tickets? I promise it's just for tonight."
                    show bg movieusher_night_3
                    mis "{i}*Sigh*{/i} I figured you'd be a little low on cash... Just for tonight."
                    show bg movieusher_night_1
                    mis "Alright, go on and choose."
                    $ premoviedate_changemind = 1
                    $ inventory.money += 60

                    jump lbl_pre_missallaway_movie_date_0
                "I feel ill.":
                    show bg movieusher_night_1
                    pov "I actually, feel pretty ill all of a sudden. I'm sorry to ruin your night."
                    pov "I just don't think I'll be able to make it through the entire movie without passing out."
                    show bg movieusher_night_3
                    mis "Oh my God... are you okay?"
                    show bg movieusher_night_1
                    pov "Yeah, I just need to lie down... I really am sorry."
                    show bg movieusher_night_3
                    mis "I'll give you a ride home, you poor thing."
                    show bg movieusher_night_2
                    ush "Well... thanks for stopping by."
                    scene black
                    with dissolve
                    $ renpy.pause()
                    scene bg myhousefront_night
                    with dissolve
                    if principallashley_points >= 1:
                        $ principallashley_points -= 1
                    else:
                        $ principallashley_points = 0
                    $ renpy.notify("Your relationship with Miss Allaway has decreased")
                    $ moviedate = 0

                    jump lbl_myhousefront_night_setup
