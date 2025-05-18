default mainstory_62_crossroads_hangout = 0
default mainstory_62_crossroads_stay = 0
default mainstory_62_crossroads_home = 0

label lbl_crossroads_of_the_day:
    scene bg schoolhallway1_daytrashed
    with fade
    show pov sad_talk at left
    with dissolve
    show jac confused at right
    with dissolve
    show eff confused at Position(xpos=1300)
    with dissolve
    pov "Dude, I swear I am being watched more than normal."
    show pov bored at left
    show jac smirk at right
    show eff smirk_talk at Position(xpos=1300)
    eff "This coming from the dude who just a few days ago got the whole town to gaze upon his cock and balls?"
    show pov bored_talk at left
    show eff smirk at Position(xpos=1300)
    pov "Okay, seriously. Enough with that."
    show pov bored at left
    show eff smirk_talk at Position(xpos=1300)
    eff "Nyehehehe."
    show pov confused at left
    show jac neutral_talk at right
    show eff smirk at Position(xpos=1300)
    jac "I wouldn’t give it much thought, [povname]."
    show pov confused_talk at left
    show jac neutral at right
    show eff neutral at Position(xpos=1300)
    pov "How so?"
    show pov bored at left
    show jac neutral_talk at right
    show eff confused at Position(xpos=1300)
    jac "It’s a small town, dude - whenever bad shit happens, people tend to blame it on the outsiders."
    show pov bored_talk at left
    show jac neutral at right
    pov "Well, that sure isn’t rude or anything."
    show pov bored at left
    show eff smirk_talk at Position(xpos=1300)
    eff "Be thankful it's just the look, in the old days they would have pulled the pitchforks and torches and ran you guys out of town."
    show pov bored_talk at left
    show jac smirk at right
    show eff smirk at Position(xpos=1300)
    pov "Yay. I'm so lucky. How do I celebrate?"
    show pov sad_talk at left
    show jac confused at right
    show eff embarrassed at Position(xpos=1300)
    pov "I am still not sure why they associate me with the kidnapping."
    show pov sad at left
    show eff embarrassed_talk at Position(xpos=1300)
    eff "Well, you have a record, after all."
    show pov shocked_talk at left
    show jac smirk at right
    show eff smirk at Position(xpos=1300)
    pov "For public indecency; not kidnapping!"
    show pov angry at left
    show jac neutral at right
    show eff confused_talk at Position(xpos=1300)
    eff "Tomato potato."
    if missallaway_path >= 20:
        show pov sad_talk at left
        show jac confused at right
        show eff confused at Position(xpos=1300)
        pov "I mean, if anything, shouldn't they looking towards Jack?"
        show pov confused_talk at left
        pov "He is the criminal around here, right?"
        show pov sad at left
        show jac confused_talk at right
        jac "Oh, they do. A window gets smashed around here and Officer Mina is already on his ass."
        show pov confused at left
        jac "She's been trying to get him to Juvie permanently ever since she became an officer."
        show pov shocked at left
        show jac embarrassed at right
        show eff confused_talk at Position(xpos=1300)
        eff "I wouldn’t be surprised if she scraped the bottom of the barrel to find any links for him or his whole 'operation'."
        show pov shocked_talk at left
        show jac confused at right
        show eff confused at Position(xpos=1300)
        pov "And you guys think he is connected to all of this?"
        show pov shocked at left
        show jac confused_talk at right
        show eff confused at Position(xpos=1300)
        jac "I doubt it, he is a crook and a drug dealer but I don't think he'd snoop so low as to kidnap anyone."
        show pov sad at left
        show jac shocked at right
        show eff sad_talk at Position(xpos=1300)
        eff "Then again, I'm sure he has people for that job."
    show pov sad at left
    show jac embarrassed at right
    show eff embarrassed_talk at Position(xpos=1300)
    eff "Should we get going. Being here makes me so depressed."
    show pov confused at left
    show jac neutral at right
    show eff neutral_talk at Position(xpos=1300)
    eff "We can stop for a few drinks at the mall once I am done cleaning."
    show pov embarrassed at left
    show jac shocked at right
    show eff smirk_talk at Position(xpos=1300)
    eff "Jacob’s treat."
    show pov smirk at left
    show jac bored_talk at right
    show eff neutral at Position(xpos=1300)
    jac "Aye- not cool. I'll shout ya'll since you cornered me - but not cool, Effie."

    menu:
        "Go with them":
            $ add_points("jacob_points",1)
            $ add_points("effie_points",1)

            show pov smirk_talk at left
            show jac bored at right
            show eff neutral at Position(xpos=1300)
            pov "Free drinks courtesy of Jacob?"
            show pov neutral_talk at left
            pov "How could I refuse that?"
            show pov smirk at left
            show jac bored_talk at right
            show eff smirk at Position(xpos=1300)
            jac "Y-yeah.. no worries, dude. Happy to."
            show pov neutral at left
            show jac bored at right
            show eff neutral_talk at Position(xpos=1300)
            eff "Sweet! Let’s get going then."

            $ main_story = 63.1
            $ kidnapping_assembly_crossroad = 1

            jump lbl_chilling_at_mall_with_the_guys

        "Clear things up with others at uni.":
            show pov embarrassed_talk at left
            show jac confused at right
            show eff confused at Position(xpos=1300)
            pov "I’ll take a rain check on that you guys."
            pov "I better clear things out with some of the guys before they start thinking ill of me or something."
            show pov embarrassed at left
            show jac confused_talk at right
            show eff embarrassed at Position(xpos=1300)
            jac "That’s probably the smart move right now man."
            jac "There are enough rumours going around the university, regarding you already."
            show pov confused_talk at left
            show jac shocked at right
            show eff shocked at Position(xpos=1300)
            pov "Wait, what rumors?"
            show pov bored at left
            show eff embarrassed_talk at Position(xpos=1300)
            eff "Best if you don’t know, dude."
            show pov embarrassed at left
            show jac embarrassed at right
            eff "Anyway, It’s getting late so see you tomorrow, [povname]!"
            show jac embarrassed_talk at right
            show eff embarrassed at Position(xpos=1300)
            jac "Yeah man, take it easy!"
            show pov embarrassed_talk at left
            show jac embarrassed at right
            pov "Goodbye, you guys…"

            $ main_story = 63.2
            $ kidnapping_assembly_crossroad = 2

            jump lbl_awkward_hallway_conversations

        "Head home early" if winc == 1:
            show pov embarrassed_talk at left
            show jac confused at right
            show eff confused at Position(xpos=1300)
            pov "Sorry guys, maybe next time."
            pov "I am being kept on a really tight leash back home."
            show jac embarrassed at right
            if sister_path >= 27:
                show eff smirk at Position(xpos=1300)
            else:
                show eff embarrassed at Position(xpos=1300)
            pov "Don’t want to add more fuel to the fire and get my mom and [sister] all anxious."
            show pov embarrassed at left
            if sister_path >= 27:
                show jac confused at right
                show eff smirk_talk at Position(xpos=1300)
            else:
                show eff embarrassed_talk at Position(xpos=1300)
            eff "I totally get it, [povname]."
            if sister_path >= 27:
                show pov shocked at left
                eff "No biggie."
                show pov embarrassed at left
                show jac confused_talk at right
                show eff smirk at Position(xpos=1300)
                jac "Am- I missing something? You two wanna fill me in?"
                show jac confused at right
                pov "..."
                show eff smirk_talk at Position(xpos=1300)
                eff "I'm just fucking around, don't worry. Right, [povname]?"
                show pov embarrassed_talk at left
                show eff smirk at Position(xpos=1300)
                pov "Ye-eah."
                show pov embarrassed at left
                show jac bored at right
                show eff smirk_talk at Position(xpos=1300)
            else:
                pass
                eff "No biggie."
                show pov embarrassed at left
                show jac neutral at right
                show eff embarrassed_talk at Position(xpos=1300)
            eff "We all got overprotective parents after all."
            show pov bored at left
            show jac confused_talk at right
            show eff smirk at Position(xpos=1300)
            jac "Yeah, I can only imagine how your mom is now that she discovered this whole new exhibitionism fetish you have."
            show pov bored_talk at left
            show jac smirk at right
            show eff neutral at Position(xpos=1300)
            pov "Oh, come on dude, this again?"
            show pov bored at left
            show jac neutral_talk at right
            jac "Never gets old!"
            show pov confused at left
            show jac smirk at right
            show eff neutral_talk at Position(xpos=1300)
            eff "You should have seen the look his mom gave me when we were walking home that day."
            show pov embarrassed at left
            eff "I thought she would shoot lasers out her eyes and made me explode or something!"
            show pov sad_talk at left
            show eff neutral at Position(xpos=1300)
            pov "She was real scared back then, please don’t hold it against her."
            show pov embarrassed at left
            show jac neutral at right
            show eff neutral_talk at Position(xpos=1300)
            eff "Nah, it’s cool."
            eff "If I am being honest, my dad would have meet you with a crowbar or something if he saw you walking me home after that."
            show pov smirk at left
            show jac smirk at right
            eff "He barely tolerates Jacob."
            show jac smirk_talk at right
            show eff neutral at Position(xpos=1300)
            jac "What can I say? I am a people person."
            show pov smirk_talk at left
            show jac bored at right
            show eff smirk at Position(xpos=1300)
            pov "Or he knows you have no chance with Effie."
            show pov smirk at left
            show eff smirk_talk at Position(xpos=1300)
            eff "Ooof, that's a third degree burn right there!"
            show pov neutral at left
            show jac bored_talk at right
            show eff smirk at Position(xpos=1300)
            jac "What's with you two getting up in my grill so much lately!"
            show pov confused_talk at left
            show jac bored at right
            show eff neutral at Position(xpos=1300)
            pov "It’s easy when you keep attacking me with nudist jokes."
            show pov neutral at left
            show jac embarrassed at right
            show eff neutral_talk at Position(xpos=1300)
            eff "Like shooting fish in a glass barrel with a rocket launcher 2 feet away."
            show pov smirk at left
            show jac smirk_talk at right
            show eff neutral at Position(xpos=1300)
            jac "Oh, come on!"
            show pov neutral_talk at left
            show jac neutral at right
            pov "Hehehe, see you later guys."
            show pov neutral at left
            show jac smirk_talk at right
            show eff smirk at Position(xpos=1300)
            jac "Later, master-bater."
            show pov embarrassed at left
            show jac smirk at right
            show eff smirk_talk at Position(xpos=1300)
            eff "Later, master-bater- also. That's a good one."
            show pov bored at left
            show jac smirk_talk at right
            show eff neutral at Position(xpos=1300)
            jac "Thanks, I made it up just now."

            $ main_story = 63.3
            $ kidnapping_assembly_crossroad = 3

            jump lbl_home_early
