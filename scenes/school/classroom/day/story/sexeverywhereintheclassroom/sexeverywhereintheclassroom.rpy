## Sex Everywhere in the Classroom ##
label lbl_sex_everywhere_in_the_classroom:
    #$ renpy.pause ()
    show pov sad_talk at left
    with dissolve
    show mis neutral at right
    with dissolve
    pov "Miss Allaway... what's going on around here?"
    show pov sad at left
    show mis neutral_talk at right
    mis "Good morning, [povname]. Nothing much, we're just about to start class."
    show pov sad_talk at left
    show mis confused at right
    pov "No, I mean.. why is everyone... fucking around here?"
    show pov sad at left
    show mis confused_talk at right
    mis "Are you okay, [povname]? You look like you've seen a ghost."

    menu:
        "I did see a ghost!":
            show pov shocked_talk at left
            show mis confused at right
            pov "I did see a ghost! L-Last night! At the park!"
            show pov shocked at left
            show mis neutral_talk at right
            mis "Oooh, spooky. Did it look like a bedsheet ghost, or the ghost from ‘The Grudge'?"

            menu:
                "Bedsheet ghost.":
                    show pov angry_talk at left
                    show mis neutral at right
                    pov "Definitely a bedsheet ghost."
                    show pov angry at left
                    show mis neutral_talk at right
                    mis "Huh... you don't see those too often nowadays, apparently it's too ‘mainstream' and ‘cliché'?"
                    show pov confused at left
                    show mis confused_talk at right
                    mis "Well excuse me, dear sir, I ain't seen a bedsheet ghost since clipart."
                    show pov confused at left
                    show mis sad at right
                    pov "..."
                    show pov confused at left
                    show mis embarrassed_talk at right
                    mis "Sorry, I had a bad Halloween experience."

                    jump lbl_sex_everywhere_in_the_classroom_2
                "‘The Grudge'.":
                    show pov angry_talk at left
                    show mis neutral at right
                    pov "Definitely ‘The Grudge'."
                    show pov bored at left
                    show mis neutral_talk at right
                    mis "Scary, yet pretty."
                    show pov confused_talk at left
                    show mis neutral at right
                    pov "I don't know about that."
                    show pov confused at left
                    show mis smirk_talk at right
                    mis "Have you ever had sex with a ghost before, [povname]?"
                    show pov confused_talk at left
                    show mis smirk at right
                    pov "Uh what..?"
                    show pov confused at left
                    show mis confused_talk at right
                    mis "It might be a little strange to think but what if that's what a wet dream is?"
                    show mis bored_talk at right
                    mis "Just a ghost using our body for sexual satisfaction?"
                    show pov confused_talk at left
                    show mis neutral at right
                    pov "It's... plausible?"
                    show pov bored at left
                    show mis smirk_talk at right
                    mis "Food for thought."

                    jump lbl_sex_everywhere_in_the_classroom_2
        "Am I alive?":
            show pov sad_talk at left
            show mis confused at right
            pov "Am I alive?"
            show pov sad at left
            show mis confused_talk at right
            mis "Are you dead?"
            show pov sad_talk at left
            show mis confused at right
            pov "I don't know."
            show pov sad at left
            show mis confused_talk at right
            mis "Am I dead?"
            show pov sad_talk at left
            show mis confused at right
            pov "Possibly? Are you?"
            show pov sad at left
            show mis confused_talk at right
            mis "I don't know."
            show pov bored at left
            show mis smirk_talk at right
            mis "These are the many questions we ask ourselves as we go through life with the very dreams and desires that distract us from what could be illusions of the mind."
            show pov confused at left
            show mis neutral_talk at right
            mis "You should talk to your philosophy teacher about that."
            show pov confused_talk at left
            show mis embarrassed at right
            pov "We don't have philosophy in high school."
            show pov bored at left
            show mis neutral_talk at right
            mis "Oh right, sorry. I was thinking of the college days."
            show pov embarrassed at left
            show mis confused_talk at right
            mis "I got a lot of dick after people found out that I was studying to become a teacher. Hmm, must be a fetish or something?"

            jump lbl_sex_everywhere_in_the_classroom_2
        "Stay silent":
            show pov sad at left
            show mis confused at right
            pov "..."
            show pov sad at left
            show mis confused_talk at right
            mis "Not in the mood to talk? That's understandable. We all have those days."
            show pov embarrassed at left
            mis "I'm not in a position to delve into your personal life."

            jump lbl_sex_everywhere_in_the_classroom_2

label lbl_sex_everywhere_in_the_classroom_2:
    show pov bored at left
    show mis neutral_talk at right
    mis "With that being said. Please take your seat, [povname]."
    show pov shocked at left
    show mis neutral_talk at right
    mis "Everyone, could you please pull out or finish up quickly, class is about to start."
    $ main_story = 32
    $ townmap_enabled = 0

    jump lbl_classroom_day_setup
