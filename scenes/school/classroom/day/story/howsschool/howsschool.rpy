## How's School ##
label lbl_hows_school:
    show pov neutral at left
    with dissolve
    show mis neutral_talk at right
    with dissolve
    mis "[povname]! Just the person I want to talk to."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Morning, Miss Allaway."
    show pov neutral at left
    show mis neutral_talk at right
    mis "How are you?"
    show pov neutral_talk at left
    show mis neutral at right
    pov "I'm feeling good. Yourself?"
    show pov neutral at left
    show mis neutral_talk at right
    mis "Good, good. I just wanted to see how you like the university so far."

    menu:
        "It's going good.":
            if missallaway_points <= 9:
                $ missallaway_points += 1
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased")
            show pov neutral_talk at left
            show mis neutral at right
            pov "It's going good so far, I like it here."
            show pov neutral at left
            show mis neutral_talk at right
            mis "I'm really pleased to hear that. I've been teaching here for 4 years and have no reason to leave."

            jump lbl_hows_school_end
        "It's alright.":
            show pov neutral_talk at left
            show mis neutral at right
            pov "It's alright, no problem, no complaints."
            show pov neutral at left
            show mis neutral_talk at right
            mis "Well, that's good. Feeling pretty neutral is never good nor bad."
            show pov neutral_talk at left
            show mis neutral at right
            pov "Haha, yeah, exactly. Give it a few more days and maybe my thoughts will skew one way."

            jump lbl_hows_school_end
        "Not too good.":
            if missallaway_points <= 9:
                $ missallaway_points += 1
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased")
            show pov embarrassed_talk at left
            show mis neutral at right
            pov "Not too good, haven't really met anyone I connected with yet."
            show pov embarrassed at left
            show mis embarrassed_talk at right
            mis "Naww really? That's a shame. Isn't Effie being a nice enough host for you?"

            menu:
                "I stayed over at her place.":
                    if missallaway_points >= 1:
                        $ missallaway_points -= 1
                    else:
                        $ missallaway_points = 0
                    $ renpy.notify("Your relationship with Miss Allaway has decreased")
                    show pov embarrassed_talk at left
                    show mis bored at right
                    pov "I stayed over at her place last night, had some fun."
                    show pov sad at left
                    show mis angry_talk at right
                    mis "Excuse me! That's not something I want to hear; or is appropriate for university grounds!"
                    mis "I don't know how you were raised or how it was like back home but we do openly speak of that here."
                    show pov sad_talk at left
                    show mis angry at right
                    pov "Right, sorry."
                    show pov sad at left
                    show mis angry at right
                    mis "I'll pretend like you didn't say that. Now get to your seat."
                    show pov sad_talk at left
                    show mis bored at right
                    pov "Alright, Miss."
                    $ main_story = 17

                    jump lbl_classroom_day_setup
                "She's doing great.":
                    show pov neutral_talk at left
                    show mis neutral at right
                    pov "She's doing a great job actually."
                    show pov neutral at left
                    show mis neutral_talk at right
                    mis "Well, as I said before, you can always come to me. Don't view me as just a teacher of authority, I'm a pretty chill person off duty, chill and fun."
                    show mis smirk_talk at right
                    mis "Or at least that's what I tell myself."

                    menu:
                        "You're pretty cool for a teacher.":
                            show pov neutral_talk at left
                            show mis confused at right
                            pov "I think you're pretty cool for a teacher."
                            show pov neutral at left
                            show mis smirk_talk at right
                            mis "Oh? For a teacher, huh?"
                            show pov embarrassed_talk at left
                            show mis smirk at right
                            pov "No, that's not what I mean."
                            show pov embarrassed at left
                            show mis neutral_talk at right
                            mis "Don't worry, [povname]. I got you, I'm just kidding."

                            jump lbl_hows_school_end
                        "That makes the both of us.":
                            if missallaway_points <= 9:
                                $ missallaway_points += 1
                            else:
                                $ missallaway_points = 10
                            $ renpy.notify("Your relationship with Miss Allaway has increased")
                            show pov neutral_talk at left
                            show mis neutral at right
                            pov "That makes the both of us."
                            show pov neutral at left
                            show mis neutral_talk at right
                            mis "Hahaha."

                            jump lbl_hows_school_end

label lbl_hows_school_end:
    show pov neutral at left
    show mis neutral_talk at right
    mis "Well alright, [povname]. That's all I really wanted to ask you about."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Alright, Miss."
    $ main_story = 17
    $ townmap_enabled = 0

    jump lbl_classroom_day_setup
