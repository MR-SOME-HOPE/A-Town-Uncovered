## Pouring Rain
label lbl_pouring_rain:
    scene black
    with fade
    $ renpy.pause()
    "Later that night..."

    ## CG
    #-Scene takes place during the night a week after the last scene-

    #- We open the scene with Mom, Sister, and you sitting together in the living room
    # while watching tv all the while there is a heavy thunderstorm going on
    # outside. The Mc is in the kitchen and about to enter the scene-

    sis "It's about time, how long does it take to make popcorn?"

    pov "Hey, you are the one who wanted me to make my secret popcorn recipe out of nowhere."
    pov "I’ll have you know that culinary genius of this level takes time to come together!"

    sis "You just sprinkle a bunch of random spices on the bowl, dude. Don’t go jerking yourself too hard about it either."

    pov "Funny how you say that despite the fact You are the one who asked me to make em in the first place."

    mum "Okay, you two. If you are going to be arguing about snacks in the middle of movie night, I’m gonna just skip the movie and get straight to one of my dramas."

    "Both" "Sorry…"

    mum "Good, that’s much better."

    #-Suddenly a sudden thunder shakes the screen and takes the group by surprise-

    "{i}*Distant crackling*{/i}"

    pov "Jesus, it’s raining sideways out there…"

    sis "We are not in an area with a threat of hurricanes, right?"

    mum "Nothing to worry you two, I saw on the weather forecast that this seems to be a random storm and that it should dissipate by tomorrow morning."

    sis "Right, because the weather man is Never wrong or anything."

    mum "Well, our opinions on our weather person aside, it’s not like we can do much about it anyway."
    mum "Though I do feel sorry for anyone still out in this weather, that thunder sounds quite angry, let alone the rain."

    sis "Hey, Isn’t the old man still out working tonight?"

    mum "Oh yes, he wanted to do overtime today despite I informed him we were having movie night."
    mum "He quite rudely informed me he was behind on some metrics or something."

    pov "So he is sleeping in the office again?"

    mum "Well, he better, because I certainly won’t be going to open the door for him in the middle of the rain."

    sis "Eh, he deserves worse lately."

    #-Suddenly there is a knock on the door-

    "{i}*Knock Knock Knock*{/i}"

    sis "Speak of the devil…"

    mum "That’s weird, I was certain he said he would be staying at the office…"

    sis "[povname], go check who it is."

    pov "Wha- Why me?!"
    pov "I already got up to get us popcorn, it’s your turn!"

    sis "Well, what if it’s some crazy killer with a machete or someone trying to sell us a timeshare?"

    pov "How do both scenarios even compare to one another?"

    sis "Both are scenarios I’d rather avoid by having you deal with to then throw you into the door before running away."
    sis "Duh."
    sis "Besides, only weird people would be knocking on our door at this time of night and during a storm."
    sis "You are the man of the house now that the old geezer is gone, so go do something!"

    mum "She has a point on that last part, [povname]."
    mum "You are the man of the house and who knows who it might be at this hour, especially unannounced like this."

    pov "Funny how none of that 'Man of the House' stuff is valid when it benefits me but it’s a law when it does you…"

    "{i}*Knock Knock Knock*{/i}"

    sis "Stop complaining and check who it is already!"

    pov "Alright, alright. Don’t go yelling at me either!"

    #-Scene changes to a pov view of the front door-

    "{i}*Knock Knock Knock*{/i}"

    pov "Im coming, I’m coming, hang on!"
    pov "Geez, who would ever be out on this weather…"
    pov "Yes, can I help yo-?"

    #-Door opens to revealed an absolutely soaked Effie, mascara running down her eyes and holding onto herself for warmth-

    eff "..."

    pov "OH MY GOD, EFFIE?!"

    eff "H-Hi…"
    eff "Nice weather we are having, am I right?"
    eff "Could I please come in? I don't have anywhere else to go."

    #-Shot goes back to regular stand in view-
    ## SPRITEWORK

    show pov shocked_talk at left
    show eff embarrassed at right
    with dissolve
    pov "Good god, what the hell happened to you?!"
    show pov confused at left
    show eff smirk_talk at right
    eff "I got wet, dude."
    eff "Sadly not in the kind you and I like but you know what I mean."

    #-Sister and Mom appear on the scene-
    show pov confused at left
    show eff shocked at Position(xpos=1200)
    show mum shocked_talk at Position(xpos=1300)
    show sis embarrassed at Position(xpos=1700)
    mum "Oh, dear lord. Don't just stand there out in the cold, dear! Come in, come in!"
    show eff embarrassed at Position(xpos=1200)
    show mum shocked at Position(xpos=1300)
    show sis neutral_talk at Position(xpos=1700)
    sis "I'll go fetch some towels!"

    #-Sister leaves the scene-
    show eff embarrassed_talk at Position(xpos=1200)
    show mum neutral at Position(xpos=1300)
    hide sis
    with dissolve
    eff "Thanks for letting me in…"
    show pov embarrassed at left
    show eff embarrassed at Position(xpos=1200)
    show mum confused_talk at Position(xpos=1300)
    mum "Sweetie, don't even mention it. You must be freezing!"
    show eff shocked at Position(xpos=1200)
    show mum smirk_talk at Position(xpos=1300)
    mum "What in god's name are you even doing outside at this hour? Not to mention in this weather!"
    show eff embarrassed_talk at Position(xpos=1200)
    show mum smirk at Position(xpos=1300)
    eff "C-Can I say that I was out on a stroll and just decided to pop in and say hi?"
    show eff embarrassed at Position(xpos=1200)
    show mum smirk_talk at Position(xpos=1300)
    mum "Not when you look like you've been crying, you can't."
    show eff embarrassed at Position(xpos=1200)
    show mum neutral_talk at Position(xpos=1300)
    mum "Dear, can you talk to me? Is everything ok?"
    show pov neutral at left
    show mum shocked_talk at Position(xpos=1300)
    mum "Oh, your family must be worried sick about you!"
    show mum confused_talk at Position(xpos=1300)
    mum "[povname], pass me the phone. I'll call her father and we'll-"
    show eff shocked_talk at Position(xpos=1200)
    show mum confused at Position(xpos=1300)
    eff "N-NO, PLEASE DO NOT DO THAT!"
    show pov shocked at left
    show eff bored_talk at Position(xpos=1200)
    eff "P-Please, don't call my dad…"
    show eff embarrassed at Position(xpos=1200)
    show mum confused_talk at Position(xpos=1300)
    mum "..."
    show pov confused_talk at left
    show mum confused at Position(xpos=1300)
    pov "..."
    show pov confused at left
    show mum neutral_talk at Position(xpos=1300)
    mum "Alright, I will not call him if you don't want me to."
    show mum neutral_talk at Position(xpos=1300)
    mum "Can I assume that the reason you are out in this weather is because of him?"
    show eff embarrassed_talk at Position(xpos=1200)
    show mum neutral at Position(xpos=1300)
    eff "Y-Yeah."
    show eff bored_talk at Position(xpos=1200)
    eff "We kind of had a really big fight and I just had to get out of there."
    show pov confused_talk at left
    show eff bored at Position(xpos=1200)
    pov "Did he do something to you or-"
    show pov confused at left
    show eff embarrassed at Position(xpos=1200)
    eff "No! No, no, no. Good god, no."
    show eff neutral_talk at Position(xpos=1200)
    show mum embarrassed at Position(xpos=1300)
    eff "We just yell at each other and sometimes say really hurtful stuff but he would never raise a hand on me or anything, please don't assume that!"
    show eff neutral at Position(xpos=1200)
    show mum embarrassed_talk at Position(xpos=1300)
    mum "No one is assuming anything, Dear. We just want to know what happened."
    show mum smirk_talk at Position(xpos=1300)
    mum "Or at least, we want to know as much as you are willing to tell us that is."
    show eff embarrassed_talk at Position(xpos=1200)
    show mum smirk at Position(xpos=1300)
    eff "I-"
    show mum neutral at Position(xpos=1300)
    eff "I'm so sorry for barging in like this, I usually go to Jacob's house when this happens and cool off there but the weather is really bad and-"
    show eff embarrassed at Position(xpos=1200)
    show mum neutral_talk at Position(xpos=1300)
    mum "That's more than alright, Dear. There's no way I'm sending you out there when the sky is falling like this."
    show pov neutral at left
    show eff shocked at Position(xpos=1200)
    show mum smirk_talk at Position(xpos=1300)
    mum "Would you like to spend the night here?"
    show eff shocked_talk at Position(xpos=1200)
    show mum smirk at Position(xpos=1300)
    eff "I-I really don't want to impose."
    show eff embarrassed_talk at Position(xpos=1200)
    eff "I kinda came here on auto pilot cuz I know [povname] and [sister]."
    show eff embarrassed at Position(xpos=1200)
    show mum neutral_talk at Position(xpos=1300)
    mum "And because of that, I'm sure neither of them will have any trouble with having you here."
    show pov shocked at left
    show mum smirk_talk at Position(xpos=1300)
    mum "Isn't that right, [povname]?"
    show pov neutral_talk at left
    show mum neutral at Position(xpos=1300)
    pov "Sure! You don't even have to ask"
    show pov neutral at left
    show eff embarrassed at Position(xpos=1200)
    show mum neutral_talk at Position(xpos=1300)
    mum "Great! She can stay in [sister]'s room then!"
    show eff embarrassed_talk at Position(xpos=1200)
    show mum neutral at Position(xpos=1300)
    eff "I-Is it really ok? I mean, we haven't even asked her and-"

    #-Sister reappears on the scene-
    show eff embarrassed at Position(xpos=1200)
    show sis neutral_talk at Position(xpos=1700)
    with dissolve
    sis "I got the towels!"
    show mum smirk_talk at Position(xpos=1300)
    show sis shocked at Position(xpos=1700)
    mum "Honey, you wouldn't mind if Effie stayed in your room for tonight, right? She doesn't want to return home for the night."
    show mum neutral at Position(xpos=1300)
    show sis smirk_talk at Position(xpos=1700)
    sis "Oh, sure thing!"
    show sis neutral_talk at Position(xpos=1700)
    sis "Of course I wouldn't mind! Hell, I was about to ask if she needed to crash somewhere if she was out in this rain."
    show pov neutral_talk at left
    show sis neutral at Position(xpos=1700)
    pov "Well, that settles it then!"
    show mum neutral_talk at Position(xpos=1300)
    mum "Wonderful! I'll heat up some dinner for you."
    show eff embarrassed_talk at Position(xpos=1200)
    eff "I-Is it really ok for me to stay here? I don't really-"
    show eff shocked at Position(xpos=1200)
    show mum bored_talk at Position(xpos=1300)
    mum "Not another word, missy."
    show mum neutral_talk at Position(xpos=1300)
    mum "You'll always be welcome under this room and that's the end of it."
    show mum confused_talk at Position(xpos=1300)
    show sis confused at Position(xpos=1700)
    mum "Now, [sister]. I want you to take her upstairs and to the bathroom so she can have a warm shower and so you can retrieve her clothes and lend her a fresh change for the night."
    mum "I'll set them to wash up so they are nice and dry tomorrow morning. After that, Effie is gonna have a nice warm meal and she's going to join us on our movie night before bed."
    show eff neutral at Position(xpos=1200)
    show mum smirk_talk at Position(xpos=1300)
    show sis smirk at Position(xpos=1700)
    mum "Is that clear for everyone?"
    show mum neutral at Position(xpos=1300)
    show sis smirk_talk at Position(xpos=1700)
    sis "Sounds good to me!"
    show pov neutral_talk at left
    show sis smirk at Position(xpos=1700)
    pov "Crystal clear!"
    show pov neutral at left
    show eff embarrassed_talk at Position(xpos=1200)
    eff "I-I really don't know what to say…"
    show pov smirk_talk at left
    show eff embarrassed at Position(xpos=1200)
    pov "Just say thanks, it's impossible to say no to her when she gets like this."
    show pov smirk at left
    show eff embarrassed_talk at Position(xpos=1200)
    show sis neutral at Position(xpos=1700)
    eff "I-I see."
    show pov neutral at left
    show eff neutral_talk at Position(xpos=1200)
    show mum smirk at Position(xpos=1300)
    eff "Then, thank you."
    show eff neutral at Position(xpos=1200)
    show mum smirk_talk at Position(xpos=1300)
    mum "With pleasure, dear."
    show mum neutral_talk at Position(xpos=1300)
    mum "Now, off you go to get out of those wet clothes. [povname], help me warm up some dinner for her and [sister] you bring me her wet clothes once she is out of them and hand her some dry ones for tonight."
    show pov smirk_talk at left
    show mum neutral at Position(xpos=1300)
    pov "You got it."
    show eff embarrassed at Position(xpos=1200)
    show sis neutral_talk at Position(xpos=1700)
    sis "Come on, Effie. Let's hope you don't catch a cold."

    scene black
    with fade
    $ renpy.pause()
    "Up in your room..."

    # Once the scene is over it will be late night where everyone is asleep and
    # to continue the storyline the Player will need to click on their bed to
    # immediately start the next scene-

    $ effie_path = 5

    jump lbl_close_to_you_like_this
