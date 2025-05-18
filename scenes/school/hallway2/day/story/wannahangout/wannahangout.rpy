## Wanna Hang Out?
label lbl_wanna_hang_out:
    image eff confused flip = im.Flip("//assets/character/effie/eff_confused.png", horizontal=True)
    image eff confused_talk flip = im.Flip("//assets/character/effie/eff_confused_talk.png", horizontal=True)
    image eff bored_talk flip = im.Flip("//assets/character/effie/eff_bored_talk.png", horizontal=True)
    image eff bored flip = im.Flip("//assets/character/effie/eff_bored.png", horizontal=True)
    image eff shocked_talk flip = im.Flip("//assets/character/effie/eff_shocked_talk.png", horizontal=True)
    image eff shocked flip = im.Flip("//assets/character/effie/eff_shocked.png", horizontal=True)
    image eff smirk_talk flip = im.Flip("//assets/character/effie/eff_smirk_talk.png", horizontal=True)
    image eff smirk flip = im.Flip("//assets/character/effie/eff_smirk.png", horizontal=True)
    image eff neutral_talk flip = im.Flip("//assets/character/effie/eff_neutral_talk.png", horizontal=True)
    image eff neutral flip = im.Flip("//assets/character/effie/eff_neutral.png", horizontal=True)
    image eff sad_talk flip = im.Flip("//assets/character/effie/eff_sad_talk.png", horizontal=True)
    image eff sad flip = im.Flip("//assets/character/effie/eff_sad.png", horizontal=True)
    image jac bored_talk flip = im.Flip("//assets/character/jacob/jac_bored_talk.png", horizontal=True)
    image jac bored flip = im.Flip("//assets/character/jacob/jac_bored.png", horizontal=True)
    image pov bored_talk flip = im.Flip("//assets/character/pov/pov_bored_talk.png", horizontal=True)
    image pov bored flip = im.Flip("//assets/character/pov/pov_bored.png", horizontal=True)
    image pov neutral_talk flip = im.Flip("//assets/character/pov/pov_neutral_talk.png", horizontal=True)
    image pov neutral flip = im.Flip("//assets/character/pov/pov_neutral.png", horizontal=True)
    image pov angry_talk flip = im.Flip("//assets/character/pov/pov_angry_talk.png", horizontal=True)
    image pov angry flip = im.Flip("//assets/character/pov/pov_angry.png", horizontal=True)
    image pov sad_talk flip = im.Flip("//assets/character/pov/pov_sad_talk.png", horizontal=True)
    image pov confused_talk flip = im.Flip("//assets/character/pov/pov_confused_talk.png", horizontal=True)
    image pov confused flip = im.Flip("//assets/character/pov/pov_confused.png", horizontal=True)

    #-The screen fades back in after a loud ring signifying the end of the day. The Mc now finds himself in the hallway outside Lashley’s office talking to her on his way out-
    scene black
    scene bg schoolhallway2_day with fade
    show pov neutral at center
    with dissolve
    show pri neutral_talk at right
    pri "Well, that should be all for today, [povname]."
    pri "I enjoyed our little talk. And the data you filled in will help with getting all this overwatch we have on you, over in a jiffy!"
    show pri neutral
    show pov smirk_talk
    pov "Well, I guess it wasn’t too bad…"
    show pov smirk
    show pri smirk_talk
    pri "I’m glad to know you think that! Next time I want to focus more on your relationship with your family and your home life."
    show pri smirk
    show pov confused_talk
    pov "There is going to be a next time?"
    show pov confused
    show pri bored_talk
    pri "A few actually, nothing too intrusive, just me gathering some information to prove you are the good kid I’m sure you are."
    show pri bored
    show pov sad_talk
    pov "Fantastic…"
    show pov sad
    show pri neutral_talk
    pri "Well, I must go back to work now. Please get home safe and be sure to remember that I’m here for you if you need to talk."
    show pri neutral
    show pov neutral_talk
    pov "Of course, Director Lashley."

    #-Lashley heads back into her office, leaving you on your own once again-
    hide pri with dissolve
    show pov bored
    pov "{i}Sigh.{/i}"
    show pov bored_talk at center with dissolve
    pov "Well, I have therapy now…"
    show pov shocked flip at Position(xpos=900) with dissolve
    #-You turn to leave only to the spot Effie and Jacob making their way towards you-
    show jac shocked_talk flip at Position(xpos=300) with dissolve
    show eff confused flip at Position(xpos=0) with dissolve
    jac "Dude, about time she let you out!"
    jac "You have been in there all day!"
    show jac shocked flip
    show pov bored_talk flip
    pov "Don’t remind me…"
    show pov bored flip
    show eff confused_talk flip
    eff "What were you two doing in there?"
    show eff confused flip
    show pov bored_talk flip
    pov "She was giving me a whole psychological evaluation."
    show pov angry_talk flip
    pov "I swear, if I see anymore ink stains on paper, I’m going to lose it."
    show pov angry flip
    show eff confused_talk flip
    eff "Free therapy doesn’t sound so bad."
    show eff confused flip
    show pov bored_talk flip
    pov "It isn’t, I’d just rather not talk about certain stuff right now."
    show pov confused_talk flip
    pov "It’s been a long night, and being asked a hundred abstract questions is not really my idea of relaxing."
    show pov confused flip
    show eff confused_talk flip
    eff "Fair enough, I guess."
    show eff confused flip
    show pov bored_talk flip
    pov "Did I miss anything interesting?"
    show pov bored flip
    show jac bored_talk flip
    jac "Not really. Allaway just had us share how we felt about all that’s going on in town and after that it was just study hall where we did some light reading for the topics ahead."
    jac "She gave us a list of chapters for you to read, to catch up with us."
    show eff bored flip
    show jac bored flip
    show pov sad_talk flip
    pov "Gee, thanks."
    show pov sad flip
    show eff sad_talk flip
    eff "You feeling alright there, bud?"
    show eff sad flip
    show pov sad_talk flip
    pov "Not really, I’d rather just go home and rest for the day."
    pov "Maybe have some coffee or something."
    show pov sad flip
    show eff neutral_talk flip
    eff "That’s not a bad idea."
    eff "How about we go to the mall and get something to drink?"
    eff "It could help ease your nerves."

    if mainstory_62_crossroads_hangout:

        #-If the MC chose to go with them in the previous crossroads-
        show eff smirk_talk flip
        eff "I dunno about you guys, but hanging out with you two definitely did a number to ease my nerves, so I could totally chill out with you both again today."
        show eff smirk flip
        show jac neutral_talk flip
        jac "Last time was quite fun, and I could also go for a smoothie and some pizza from the food court, now that I think about it."
        show jac neutral flip

    else:

        #-If the MC didn’t go with them in the previous crossroads-

        eff "It’s been a while since we last hung out just the three of us, after all."
        eff "I would be down to hanging out with you two if you guys are up for it today."
        show eff neutral flip
        show jac smirk_talk flip
        jac "That sounds fun. Count me in!"
        jac "Some drinks and food court pizza are always welcomed in my stomach."
        show jac smirk flip

    #=RESULT END=
    show eff neutral_talk flip
    eff "What do you say, [povname]?"
    show eff neutral flip

    menu:
        "Go with them now":

            pov "…"
            show pov smirk_talk flip
            pov "You know what? Screw it."
            pov "I’m not going to let a rough night not let me enjoy some time with my best buds."
            pov "I’m down."
            show pov smirk flip
            show eff smirk_talk flip
            eff "Sweet!"
            eff "Don’t worry, [povname], It’ll be just some drinks and you’ll feel much better, I guarantee it!"
            show eff smirk flip
            show jac smirk_talk flip
            jac "Alright! Day out with my buds!"
            jac "First round is on me, come on!"
            scene black with fade
            #-You all head out towards the mall-

            jump lbl_mall_with_friends

        "Take a raincheck":
            #(Choosing this option represents a natural break and allows the player to roam around to their leisure, they can find Effie and Jacob in the hallways at school once they are ready to continue the main story)

            pov "…"
            show pov sad_talk flip
            pov "I’m sorry, guys. Maybe next time, guys."
            show eff sad flip
            show jac sad flip
            pov "I really feel like shit and I think I just need to rest a bit before going all social"
            pov "I wouldn’t want to bring the mood down and all…"
            show pov sad flip
            show eff shocked_talk flip
            eff "Dude, it’s okay. No need to apologize."
            show eff shocked flip
            show jac bored_talk flip
            jac "It’s more than obvious you had a rough night, dude. Be sure to get home and rest!"
            jac "You can always just let us know when you feel better and we can go out together then!"
            show jac bored flip
            show eff bored_talk flip
            eff "Yeah!"
            eff "I have my schedule wide open, so just let us know and we can head out after uni, no problem!"
            show eff bored flip
            show pov neutral_talk flip
            pov "Thanks guys, you are the best."
            show pov neutral flip
            show eff neutral_talk flip
            eff "Naturally!"
            eff "Now, let’s get you home."
            eff "We don’t want you passing out in the middle of the street or something."
            scene black with fade

            $ main_story = 75.5

            $ gtime = 1

            jump lbl_townmap_setup
