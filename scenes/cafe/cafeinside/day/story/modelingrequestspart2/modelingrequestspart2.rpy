label lbl_modelling_requests_part2:
    #[Town, Afternoon - “Modeling requests part 2”  - hitomi_path = 16.5]#14

    #-In this scene comes the various interactions and replies that take place
    # when asking the girls around town to model for Hitomi, the correct answer
    # is of course, Effie-

    #-Gee agreed to make the interactions for the rest of the girls himself so at
    # the moment only the text for Effie is present-

    scene bg cafeinside_day

    $ modeling_requests_asked_effie = 1
    $ modeling_request_people_asked_count = 2

            ## SPRITEWORK (Use effw for 'effie work clothes' because she's at work) ##

    show pov confused at left
    show effw smirk_talk at right
    with dissolve
    eff "Hey, dude!"
    show pov embarrassed at left
    eff "Nice to see you. You looking for anything sweet, because I’ll have to remind you I’m not on the menu."
    show pov neutral at left
    show effw neutral_talk at right
    eff "We do have a promotion on muffins today though! Buy two get a third one free!"
    show pov bored at left
    show effw smirk_talk at right
    eff "Though, between us, I wouldn’t try the third muffin you get."
    eff "The manager is trying to get rid of an old batch; and the third muffin we give out is from that batch - so it’s rather hard and stale."
    show effw neutral_talk at right
    eff "Only telling you this because we are friends."
    show pov bored_talk at left
    show effw neutral at right
    pov "Well, I appreciate the heads up, but that’s not why I’m here actually."
    show pov bored at left
    show effw smirk_talk at right
    eff "Then what can I get you, dude?"
    show pov bored_talk at left
    show effw confused at right
    pov "Does your shift end any time soon?"
    show pov confused at left
    show effw confused_talk at right
    eff "In about 10 minutes, but my replacement for the late noon shift is already here, why?"
    show pov bored_talk at left
    show effw confused at right
    pov "Well… I need a huge solid, Effie."
    show pov bored at left
    show effw smirk_talk at right
    eff "Oh boy, what did you got yourself into this time?"
    show pov bored_talk at left
    show effw smirk at right
    pov "It’s a really long story, but I’m helping Hitomi from the comicbook shop, out with some of her art for her webcomic and-"
    show pov bored at left
    show effw shocked_talk at right
    eff "Oh right! Jacob told me you were helping her with that."
    show pov confused at left
    show effw smirk_talk at right
    eff "Though he seemed quite salty about it…"
    show pov bored at left
    show effw bored_talk at right
    eff "Anyway, you saying she needs something?"
    show pov embarrassed_talk at left
    show effw shocked at right
    pov "Y-Yeah, we are looking for a female model for her to use as reference for some poses with a male partner."
    show pov embarrassed at left
    show effw bored_talk at right
    eff "And I can assume you are the male partner here?"
    show pov embarrassed_talk at left
    show effw confused at right
    pov "Been helping her out for a while now."
    show pov embarrassed at left
    show effw confused_talk at right
    eff "Doesn’t seem too difficult. What’s the catch?"
    show pov smirk_talk at left
    show effw smirk at right
    pov "Well, it’s nude modeling, for one…"
    show pov confused_talk at left
    show effw confused at right
    pov "And it has to be today…"
    show pov confused at left
    show effw smirk_talk at right
    eff "Woah. Today? You guys don’t even give a girl time to prepare!"
    show pov bored at left
    show effw confused_talk at right
    eff "And since when are you a nude model?"
    show pov bored_talk at left
    show effw confused at right
    pov "I’m just doing a friend a favor, here. And she tasked me with looking for a possible partner, for the poses she needs."
    show pov smirk_talk at left
    show effw shocked at right
    pov "She is even willing to pay for your time and for doing this for her, given how desperate she is."
    show pov embarrassed at left
    show effw neutral_talk at right
    eff "And how’s that coming along so far? How many people did you ask before coming to me?"

    #-RESULT-
    #-If you have talked to 3 people or less-
    if modeling_request_people_asked_count <= 3:
        show pov embarrassed_talk at left
        show effw confused at right
        pov "You are actually one of the first people I asked."

        #+1 Effie RP
        $ add_points("effie_points",1)
        show pov bored at left
        show effw embarrassed_talk at right
        eff "Awww!"
        show pov smirk at left
        show effw neutral_talk at right
        eff "So nice to know you thought of me first!"
        show effw smirk_talk at right
        eff "Always makes a girl feel special to know we are the first person to pop up on a dude’s mind!"

        #=RESULT END=


    #-If you have talked from 4 to 6 people-
    elif 4 <=modeling_request_people_asked_count <= 6:
        show pov embarrassed_talk at left
        show effw confused at right
        pov "Honestly, it isn’t going that well…"
        show pov embarrassed at left
        show effw shocked_talk at right
        eff "I can imagine not a lot of girls are down to getting nude the same day a guy asks them."
        show pov bored at left
        show effw embarrassed_talk at right
        eff "Not without at least a drink to buzz them up a little."
        eff "You definitely had your work cut out for ya'."

        #=RESULT END=


    #-If you have talked to 7 or more-
    elif modeling_request_people_asked_count >= 7:
        show pov embarrassed_talk at left
        show effw neutral at right
        pov "I’ve been going all over the place. There's likely weird rumors going on about me, and I’m really close to just giving up and going back to Hitomi."
        show pov confused_talk at left
        show effw shocked at right
        pov "You are probably my last hope."
        show pov embarrassed at left
        show effw embarrassed_talk at right
        eff "I’m not sure whether to be flattered that you didn’t want to bother me with your request, or insulted that I wasn’t around your first few options…"
        show effw smirk_talk at right
        eff "But I can see you are on your last legs, here. And you need all the help you can get."
        show pov neutral at left
        show effw embarrassed at right
        eff "Plus, with the possible rumors, you totally do deserve a break."

        #=RESULT END=
    #=END=

    show pov shocked at left
    show effw neutral_talk at right
    eff "Alright, I’m in."
    show pov confused_talk at left
    show effw bored at right
    pov "Wait, seriously?"
    show pov shocked at left
    show effw neutral_talk at right
    eff "Yeah, dude!"
    eff "This is clearly important to Hitomi, and she and I go way back. Even if I don’t stop by the shop as often anymore."
    show pov  neutral at left
    show effw smirk_talk at right
    eff "Besides, it’s not like I have any issue being in the nude around you."
    show pov smirk_talk at left
    show effw smirk at right
    pov "You are a life saver, Effie."
    show pov neutral at left
    show effw smirk_talk at right
    eff "I know, I know, I’m great!"
    show effw bored_talk at right
    eff "Now, let me just tell my replacement I’m leaving early and clock out."
    show pov embarrassed at left
    show effw neutral_talk at right
    eff "Though I’ll let you know right now: if she has me doing any silly poses, I’m actually gonna charge her!"
    show pov smirk_talk at left
    show effw neutral at right
    pov "I’m sure we can discuss that once we are there."
    show pov smirk at left
    show effw neutral at right
    eff "Alright, gimme a second, and we can leave."
    show pov neutral_talk at left
    show effw smirk at right
    pov "Alright!"

    #-Fade to black to indicate transition-
    #-Now Effie is in your “Party” until you go back to Hitomi-
    scene black
    with fade

    $ hitomi_path = 15
    $ map_blocking = True

    jump lbl_cafeoutside_day

    #=SCENE END=
