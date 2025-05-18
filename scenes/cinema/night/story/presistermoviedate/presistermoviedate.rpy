## Pre Sister Movie Date ##
label lbl_pre_sister_movie_date:

    scene bg movieusher_night_2
    with dissolve
    ush "Yo, welcome. What can I get you this fine night?"
    show bg movieusher_night_1
    pov "Hey. Can I get two tickets."
    show bg movieusher_night_2
    ush "Sure, dude. That'll be $60 for two. What film are you feeling for tonight?"
    show bg movieusher_night_1

    jump lbl_pre_sister_movie_date_0

label lbl_pre_sister_movie_date_0:
    menu:
        "Action Movie." if inventory.money >= 60:
            pov "Tonight's action movie."
            show bg movieusher_night_3
            sis "Nice! I can turn my brain off and look at hot shit flying everywhere. Explosions too."
            show bg movieusher_night_1
            pov "I figured we could use some extreme eye-candy."
            show bg movieusher_night_3
            sis "How to make the prehistoric brain go brrrr 101."
            show bg movieusher_night_1
            pov "Keep it simple stupid, the cavemen know what's up when they invented fire."
            show bg movieusher_night_2
            ush "If fire and flames is what you want then you can't go wrong with tonight's foreign film."
            show bg movieusher_night_1
            pov "Is there subtitles?"
            show bg movieusher_night_3
            sis "Who needs subtitles when you've got heart."
            show bg movieusher_night_2
            ush "D-don't worry, sir. There will be subtitles. Enjoy!"

            $ moviedate_choice = 1

            jump lbl_sister_movie_date

        "Horror Movie." if inventory.money >= 60:
            pov "Tonight's horror movie."
            show bg movieusher_night_3
            sis "Ooooh fuck yeah!"
            show bg movieusher_night_1
            pov "Guessing I picked the right movie."
            show bg movieusher_night_3
            sis "Fuck yeah you picked the right one, been meaning to watch tonight's showing."
            show bg movieusher_night_2
            ush "Eff- yeah you picked the right one. This one's got raging reviews."
            show bg movieusher_night_3
            sis "They say it brings back the same feelings as watching the classics back when they came out."
            show bg movieusher_night_2
            ush "So they say, I haven't seen it myself yet."
            show bg movieusher_night_3
            sis "Hurry up and pay the man, [povname]. We're gonna miss the movie!"
            show bg movieusher_night_1
            pov "We're literally not, calm down, Jesus Christ."

            $ moviedate_choice = 2

            jump lbl_sister_movie_date

        "Romance Movie." if inventory.money >= 60:
            pov "Tonight's romance movie."
            show bg movieusher_night_3
            sis "Romance, really?"
            show bg movieusher_night_2
            ush "Oh, this one's a real good one, I've heard."
            show bg movieusher_night_3
            sis "He's my [povsisrole]."
            show bg movieusher_night_2
            ush "Oh-"
            show bg movieusher_night_1
            pov "Hey! I just- like a good love story."
            pov "This has nothing to do with you."
            show bg movieusher_night_2
            ush "Hey, no judgements here, [povsisrole]."
            show bg movieusher_night_3
            sis "God save me."

            $ moviedate_choice = 3

            jump lbl_sister_movie_date

        "I've changed my mind." if premoviedate_changemind == 0:
            pov "Actually, I've changed my mind. I don't want to buy any tickets."
            show bg movieusher_night_3
            sis "What...?!"
            show bg movieusher_night_1
            sis "Are you serious, [povname]. Tell me you're fucking with me."
            show bg movieusher_night_3
            sis "You've got to be kidding, right? This was your idea."

            menu:
                "Could you take tonight's ticket?":
                    show bg movieusher_night_1
                    pov "Could you take tonight's tickets? I promise it's just for tonight."
                    show bg movieusher_night_3
                    sis "{i}*Sigh*{/i} I'm telling [missus] when we get home, asshole."
                    sis "You're lucky I have a job."
                    show bg movieusher_night_1
                    sis "Alright, go on and choose."

                    $ premoviedate_changemind = 1
                    $ inventory.money += 60

                    jump lbl_pre_sister_movie_date_0

                "I feel ill.":
                    show bg movieusher_night_1
                    pov "I actually, feel pretty ill all of a sudden. I'm sorry to ruin your night."
                    pov "I just don't think I'll be able to make it through the entire movie without passing out."
                    show bg movieusher_night_3
                    sis "Was it something you ate for dinner? I told you you shouldn't have eaten leftover."
                    show bg movieusher_night_1
                    pov "Yeah, I just need to lie down... I really am sorry."
                    show bg movieusher_night_3
                    sis "Can you walk or do I have to pay for a ride...?"
                    show bg movieusher_night_2
                    ush "Uhm- sorry to hear about that, guys. But please, can we have the next in line."
                    scene black
                    with dissolve
                    $ renpy.pause()
                    scene bg myhousefront_night
                    with dissolve
                    if sister_points >= 1:
                        $ sister_points -= 1
                    else:
                        $ sister_points = 0
                    $ renpy.notify("Your relationship with [sister] has decreased")
                    $ moviedate = 0

                    jump lbl_myhousefront_night_setup
