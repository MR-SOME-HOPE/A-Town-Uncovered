## Pre Lashley Movie Date ##
label lbl_pre_lashley_movie_date:

    scene bg movieusher_night_2
    with dissolve
    ush "Yo, welcome. What can I get you this fine night?"
    show bg movieusher_night_1
    pov "Hey. Can I get two tickets."
    show bg movieusher_night_2
    ush "Sure, dude. That'll be $60 for two. What film are you feeling for tonight?"
    show bg movieusher_night_1

label lbl_pre_lashley_movie_date_0:

    menu:
        "Action Movie." if inventory.money >= 60:
            pov "Tonight's action movie."
            show bg movieusher_night_3
            pri "Don't you think that'll be a little- violent?"
            show bg movieusher_night_1
            pov "I figured tonight will be about guns and explosions."
            show bg movieusher_night_3
            pri "I mean sure, though I do not condone violence."
            show bg movieusher_night_1
            pov "Oh, you know it's all stunts and for show. It'll be fun!"
            show bg movieusher_night_2
            ush "Hey, just an FYI. No refunds if you choose to leave mid-way."
            show bg movieusher_night_1
            pov "Besides, the hero is always a Bond-esque lookin-"
            show bg movieusher_night_3
            pri "[povname], I couldn't care less about what they look like, as long as they're doing it for the right reasons."
            show bg movieusher_night_2
            ush "H-have fun, you guys!"
            $ moviedate_choice = 1

            jump lbl_lashley_movie_date

        "Horror Movie." if inventory.money >= 60:
            pov "Tonight's horror movie."
            show bg movieusher_night_3
            pri "I don't mind a horror, they're scary but it's interesting to see how filmmakers depict spiritual beings."
            show bg movieusher_night_1
            pov "Really? I never took you for a horror gal."
            show bg movieusher_night_3
            pri "I'm not HUGE into it, but I don't hate it per se."
            pri "It might sound a little unusual but I always come out of a horror feeling closer to the Lord."
            show bg movieusher_night_2
            ush "Amen, sister. You're gonna love tonight's showing."
            show bg movieusher_night_1
            pri "You look like a sweet, trustful, young man. I'll take your word for it!"
            show bg movieusher_night_1
            pov "This is gonna be- fun?"
            $ moviedate_choice = 2

            jump lbl_lashley_movie_date

        "Romance Movie." if inventory.money >= 60:
            pov "Tonight's romance movie."
            show bg movieusher_night_3
            pri "R-romance- Oh my- [povname]..."
            show bg movieusher_night_1
            pov "Why? Would you rather not watch a romance movie?"
            show bg movieusher_night_3
            pri "N-no. No, it's just- am I blushing, I'm not blushing am I?"
            pri "Curse my pale skin."
            pri "I'm joking, Lord I adore myself as I am your creation."
            show bg movieusher_night_1
            pov "Ahaha- no, don't worry. You're not blushing-"
            pov "-that much."
            show bg movieusher_night_2
            ush "I hear this film's gonna bring out some truth within it's viewers. Prepare for that."
            show bg movieusher_night_1
            pov "Thanks, man. Can't wait to see where it takes us emotionally."
            $ moviedate_choice = 3

            jump lbl_lashley_movie_date

        "I've changed my mind." if premoviedate_changemind == 0:
            pov "Actually, I've changed my mind. I don't want to buy any tickets."
            show bg movieusher_night_3
            pri "What...?!"
            show bg movieusher_night_1
            pri "Are you serious, [povname]. Tell me you're kidding, you know I'm a busy person."
            pri "I cleared tonight's schedule for you."
            show bg movieusher_night_3
            pri "What's wrong?"

            menu:
                "Could you take tonight's ticket?":
                    show bg movieusher_night_1
                    pov "Could you take tonight's tickets? I promise it's just for tonight."
                    show bg movieusher_night_3
                    pri "{i}*Sigh*{/i} Is that it? Money is no object, [povname]... The least I could do for you."
                    pri "Give and you shall receive, right?"
                    show bg movieusher_night_1
                    pri "Alright, go on and choose."
                    $ premoviedate_changemind = 1
                    $ inventory.money += 60

                    jump lbl_pre_lashley_movie_date_0
                "I feel ill.":
                    show bg movieusher_night_1
                    pov "I actually, feel pretty ill all of a sudden. I'm sorry to ruin your night."
                    pov "I just don't think I'll be able to make it through the entire movie without passing out."
                    show bg movieusher_night_3
                    pri "Oh dear, are you okay? Was it something you ate?"
                    show bg movieusher_night_1
                    pov "Yeah, I just need to lie down... I really am sorry."
                    show bg movieusher_night_3
                    pri "I'll give you a ride home, you poor thing. Do you mind if I say a quick healing prayer for you?"
                    show bg movieusher_night_2
                    ush "Uhm- sorry to hear about that, guys. But please, can we have the next in line."
                    scene black
                    with dissolve
                    $ renpy.pause()
                    scene bg myhousefront_night
                    with dissolve
                    if lashley_points >= 1:
                        $ lashley_points -= 1
                    else:
                        $ lashley_points = 0
                    $ renpy.notify("Your relationship with Director Lashley has decreased")
                    $ moviedate = 0

                    jump lbl_myhousefront_night_setup
