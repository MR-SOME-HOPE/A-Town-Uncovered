## Allaway Date Cold Feet ##
label lbl_allaway_date_cold_feet:
    default allawaydatecoldfeet_movie = 0

    scene bg cinemaoutside_night
    with fade
    show pov neutral_talk at left
    with dissolve
    show miso sad at right
    with dissolve
    pov "Miss Allaway, fancy seeing you h-"
    show pov embarrassed at left
    mis "..."
    show pov sad_talk at left
    pov "A-are you okay?"
    show pov sad at left
    mis "..."
    show pov sad_talk at left
    pov "Where's your-"
    show pov shocked at left
    mis "He stood me up."
    show pov shocked_talk at left
    show miso sad at right
    pov "What?!"
    show pov shocked at left
    show miso angry_talk at right
    mis "He stood me up."
    show miso sad_talk at right
    mis "I'm such an idiot."
    mis "I feel like an idiot."
    show pov sad_talk at left
    show miso sad at right
    pov "What happened?"
    show pov sad at left
    show miso confused_talk at right
    mis "He texted me that he'll be running late and that we should meet up at the cinema instead."
    show pov shocked at left
    show miso angry_talk at right
    mis "I've been waiting here for 45 minutes."
    show pov sad at left
    mis "The movie started 20 minutes ago."
    show miso angry_talk at right
    mis "He's not replying."
    show miso sad_talk at right
    mis "I'm an idiot."
    show pov sad_talk at left
    show miso sad at right
    pov "You're not an idiot, Miss."
    show pov confused_talk at left
    pov "That guy's a fucking jerk for ditching you."
    show pov embarrassed at left
    show miso sad_talk at right
    mis "Yeah?"
    show pov sad at left
    mis "I still feel like I'm the problem here."
    mis "Like I'm not even worth rejecting properly to."

    menu:
        "Do you wanna watch a movie with me?":
            if skill_cha >= 6:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_cha -= 3
                $ renpy.notify("You used 3 Charisma Points\nYour relationship with Miss Allaway has increased")
            show pov embarrassed_talk at left
            show miso confused at right
            pov "Since I'm here, do you wanna watch a movie with me?"
            show pov embarrassed at left
            show miso sad at right
            mis "..."
            show pov confused at left
            show miso sad_talk at right
            mis "We shouldn't."
            show pov smirk_talk at left
            show miso sad at right
            pov "We should."
            pov "Unless you have anything better to do at home, why not?"
            show pov smirk at left
            show miso embarrassed_talk at right
            mis "'Why not' is right."
            show pov neutral at left
            show miso neutral_talk at right
            mis "Alright, [povname]. I'll take you up on your offer."
            show pov smirk at left
            show miso confused_talk at right
            mis "But it's not a date."
            show pov smirk_talk at left
            show miso confused at right
            pov "It's a date."
            show pov smirk at left
            show miso bored_talk at right
            mis "No, it's not."
            show pov smirk at left
            show miso embarrassed at right
            pov "You keep telling yourself that, I'm calling it a date."
        "Don't think that all guys are like that.":
            show pov embarrassed_talk at left
            show miso sad at right
            pov "I'm sorry to hear that, don't think that all guys are like that."
            show pov angry_talk at left
            pov "This one is particular is probably just some sad asshole with a micropenis."
            show pov smirk_talk at left
            show miso embarrassed at right
            pov "You're lucky that he shot you down before you even had a first date."
            show pov embarrassed_talk at left
            pov "Imagine getting to know him and possibly liking him before he rejects you."
            show pov embarrassed_talk at left
            show miso confused at right
            pov "I think that's a worst outcome."
            show pov neutral at left
            show miso embarrassed_talk at right
            mis "Never really thought of it that way."
            mis "You do have a good point, [povname]."
            show pov confused at left
            show miso neutral_talk at right
            mis "Hey, ding-ding-ding. Lightbulb."
            show miso embarrassed_talk at right
            mis "Why don't you come watch a movie with me?"

            menu:
                "You're asking ME out?":
                    show pov smirk_talk at left
                    show miso shocked at right
                    pov "You're asking ME out?"
                    show pov smirk at left
                    show miso embarrassed_talk at right
                    mis "I'm not asking you out. It's a- film excursion."
                    show pov smirk_talk at left
                    show miso bored at right
                    pov "You're asking me out, don't try to hide it."
                    show miso embarrassed at right
                    pov "It's cute when you try to hide it."
                    show pov smirk at left
                    show miso sad_talk at right
                    mis "Whatever... So, yes?"
                    show pov smirk_talk at left
                    show miso embarrassed at right
                    pov "Yes, of course."
                "No thanks.":
                    if missallaway_points >= 1:
                        $ missallaway_points -= 1
                    else:
                        $ missallaway_points = 0
                    $ renpy.notify("Your relationship with Miss Allaway has decreased by 1")
                    show pov embarrassed_talk at left
                    show miso shocked at right
                    pov "No thanks."
                    pov "As much as I'd love to, I'm not really in a movie watching mood."
                    show pov embarrassed at left
                    show miso embarrassed_talk at right
                    mis "Oh? That's a shame. Maybe some other time?"
                    mis "I thought out of all people, you'd be down for it."
                    show pov embarrassed_talk at left
                    show miso sad at right
                    pov "I-"
                    show pov embarrassed at left
                    show miso embarrassed_talk at right
                    mis "It's okay, you don't need to explain yourself."
                    mis "Hey, how about we take a slow stroll through the park?"
                    show pov embarrassed_talk at left
                    show miso sad at right
                    pov "I-"
                    show pov embarrassed at left
                    show miso bored_talk at right
                    mis "That was more of a ‘let's do this instead' than an actual question."
                    mis "Come, I'm bored and you're here already."
                    show pov embarrassed_talk at left
                    show miso embarrassed at right
                    pov "Alright, I'll accompany you."
                    $ missallaway_path = 15

                    jump lbl_deep_park_talk_with_allaway

    scene bg allawaymoviedate_action_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_1
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_1
    $ renpy.pause(0.5,hard=True)

    scene black
    with fade
    "After the movie, at the park nearby..."
    $ allawaydatecoldfeet_movie = 1

    jump lbl_deep_park_talk_with_allaway
