## The Getaway ##
label lbl_the_getaway_0:
    if allawayprivatetalk_telltruth == 0:
        jump lbl_the_getaway_1
    else:
        jump lbl_the_getaway_2

label lbl_the_getaway_1:
    show bg thegetaway_1
    with fade

    menu:
        "Apologize":
            show bg thegetaway_2
            pov "I'm sorry..."
            show bg thegetaway_1
            mis "Oh, you're sorry now?"
            mis "Whatever could you be sorry for?"
            mis "Hiding things from me?"
            show bg thegetaway_3
            mis "Agreeing to do insane stunts, and put yourself in danger?"
            mis "Please, enlighten me!"
            mis "What is [povname] sorry about?"
            pov "..."
            show bg thegetaway_4
            pov "I-I guess..."
            show bg thegetaway_2
            pov "I'm sorry for always being a burden to you."
            show bg thegetaway_1
            mis "..."
            show bg thegetaway_2
            pov "From day one, I have been nothing but a constant pain in your neck and-"
            pov "And I even dragged you into this mess, for my own selfish reasons."
            pov "Even when I try to make things right, it seems I can't do anything but give you a headache."
            show bg thegetaway_4
            pov "I'm sorry I'm such a disappointment to you."
            show bg thegetaway_3
            mis "I-I... [povname], I didn't mean it like that."
            mis "You're not a burden to me, we just got dealt a bad hand of cards and now we have to make the most of it."
            show bg thegetaway_2
            pov "How can I not be a burden, Allaway?"
            pov "I keep hurting you when I try to protect you; and I get us into deeper messes when I try to fix things."
            show bg thegetaway_3
            mis "Well, that's because you keep trying to fix everything on your own!"
            show bg thegetaway_1
            mis "That's why I'm so mad at you."
            mis "If you had told me what was happening, from the beginning we could have found a way to work things out together."
            show bg thegetaway_2
            pov "I didn't want to bring you anymore stress."
            pov "Every day, you look exhausted."
            pov "You barely put any effort in your lessons."
            pov "You look like you're about to have a nervous breakdown during class."
            show bg thegetaway_4
            pov "I had to do something, even at the risk of bringing harm to myself."
            show bg thegetaway_3
            if missallaway_points <= 9:
                $ missallaway_points += 1
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased")
            mis "..."
            mis "I guess I can see where your heart was when making all these choices."
            show bg thegetaway_1
            mis "You had good intentions, but it backfired on you."
            show bg thegetaway_2_1
            pov "Are you still angry with me?"
            show bg thegetaway_1_2
            mis "Oh, absolutely."
            show bg thegetaway_1_3
            mis "But..."
            show bg thegetaway_5_4
            mis "I'd say you have made a good start to help me move past it."
        "Explain yourself":
            show bg thegetaway_6
            pov "Look, I had an opportunity."
            pov "One I couldn't just refuse with everything that was at stake, so I took it."
            pov "I knew the dangers and what it meant to fail, but I took it anyway because I wanted to protect you."
            pov "How can you be mad at me for that?"
            show bg thegetaway_7
            mis "..."
            mis "You still don't get it, do you?"
            mis "I'm not mad that you agreed to do this."
            mis "If anything, I'm glad we may get out of this."
            show bg thegetaway_8
            mis "What I'm angry about is that you lied to me!"
            mis "I feel betrayed. Betrayed, [povname]."
            mis "I thought we were on the same page about you staying out of this and letting me handle it."
            show bg thegetaway_7
            mis "How can you -of all people- not understand how I'm feeling right now?"
            show bg thegetaway_6
            pov "I did it to protect you, so you could {i}stop{/i} this!"
            show bg thegetaway_9
            mis "In case you haven't noticed, I have been through absolute hell, these past few weeks!"
            mis "Just spending my days, trying to stay awake and alert, while waiting for Jack's errand calls on burner phones."
            show bg thegetaway_8
            mis "The only silver lining I had was you..."
            mis "You kept me going, just by giving me that smile of yours."
            mis "I didn't break because I kept you in my mind and in my heart."
            mis "And now I find that you find it so easy to lie and deceive me too?"
            mis "How can you not expect me to react to that?"
            show bg thegetaway_1
            mis "To not be absolutely hurt by that?"
            pov "..."
            show bg thegetaway_2_1
            pov "Allaway, I-"
            show bg thegetaway_1_2
            mis "Don't-"
            show bg thegetaway_2_3
            mis "Just... shut up and think about what I just said."
            show bg thegetaway_3_4
            mis "And remember it next time you think I'm exaggerating my reaction."

    jump lbl_the_getaway_3

label lbl_the_getaway_2:
    show bg thegetaway_1
    with fade

    menu:
        "Apologize":
            pov "..."
            show bg thegetaway_2
            pov "I'm sorry."
            pov "I just seem to keep making things more difficult for you, don't I?"
            show bg thegetaway_1
            mis "Hmm? What are you talking about?"
            show bg thegetaway_4
            pov "I'm just... Thinking about how much I seem to screw things up for you."
            show bg thegetaway_2
            pov "So far, I have been nothing but a whirlwind of destruction and danger for you."
            pov "Sometimes I wonder if it would be best to just get out of your life and leave you be."
            show bg thegetaway_3
            pov "Maybe it would make things easier for yo-"
            if missallaway_points <= 8:
                $ missallaway_points += 2
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased by 2")
            show bg thegetaway_8
            mis "I'm going to stop you right there, because everything coming out of your mouth is a gigantic load of horse poo."
            mis "You're not a mistake. We have talked about this!"
            mis "We have bad luck with the initial hand but I'm sure we can turn it into something better."
            mis "What happened isn't your fault, [povname]."
            show bg thegetaway_5
            mis "I don't blame you for any of it and I couldn't have asked for anyone better to share this mess with."
            show bg thegetaway_5_1
            mis "We are together and I love you."
            show bg thegetaway_5_2
            mis "Nothing is going to change that."
            show bg thegetaway_5_3
            mis "I don't regret meeting you and what we started is one of the only things that still brings me joy."
            show bg thegetaway_5_4
            mis "So there is nothing to apologize for."
        "Reassure her":
            show bg thegetaway_10
            pov "We'll get through this."
            show bg thegetaway_11
            pov "No matter what happens now, we will get through this together..."
            show bg thegetaway_5
            mis "Just... please promise to not do anymore crazy stunts once this is over."
            show bg thegetaway_12
            pov "What's life without a bit of uncertainty?"
            show bg thegetaway_13
            mis "One where I don't have to worry about having a heart attack before reaching my 30's."
            show bg thegetaway_12
            pov "Can't say I'm a boring lover though, can you?"
            show bg thegetaway_13_1
            mis "I can't. I really can't."
            show bg thegetaway_12_2
            pov "Hehehe, alright."
            show bg thegetaway_12_3
            pov "No more crazy stunts after this."
            show bg thegetaway_5_4
            mis "You don't know how happy that makes me feel right now."

    jump lbl_the_getaway_3

label lbl_the_getaway_3:
    show bg thegetaway_14
    with hpunch
    mis "AAAAHHH!"
    pov "Jesus fuck!"
    show bg thegetaway_15
    pov "Who the fuck-"
    show bg thegetaway_16
    goon "I'm with Jack! Take this fucking bag!"
    show bg thegetaway_17
    goon "I messed up! I-I think people saw me take the drugs."
    show bg thegetaway_16
    goon "I feel like they're on to me, dude!"
    show bg thegetaway_17
    goon "Take the stuff and take it to Jack as soon as you can - I think the police are coming!"
    show bg thegetaway_15
    pov "WHAT?!"
    show bg thegetaway_16
    mis "WHAT?!"
    show bg thegetaway_17
    goon "I gotta hide, dude. What the fuck are you two still doing here! Drive, bitch!"

    scene bg allawaytruck_6
    with vpunch
    mis "Oh my God, oh my God, oh my God!"
    show bg allawaytruck_7
    pov "A-Allaway, slow down!"
    show bg allawaytruck_6
    pov "We are going to crash into something!"
    show bg allawaytruck_7
    mis "How can you tell me to slow down?!"
    show bg allawaytruck_6
    mis "We have the police after us and a bag of fucking drugs!"
    show bg allawaytruck_7
    pov "They'll stop us for speeding before they even realize we have drugs on us!"
    show bg allawaytruck_1
    pov "That is if we don't crash into some guy or the side of a building first!"
    show bg allawaytruck_2
    mis "How did we get involved in this?!"
    show bg allawaytruck_1
    mis "How did we agree to any of this?!"
    show bg allawaytruck_2
    pov "I don't know!"
    show bg allawaytruck_1
    pov "J-Jacob gave me a phrase from a fortune cookie, and things just spiralled out of control from there!"
    show bg allawaytruck_2
    mis "And you listened to him?!"
    show bg allawaytruck_1
    mis "Jacob?!"
    show bg allawaytruck_2
    mis "And a frikkin' fortune cookie?!"
    show bg allawaytruck_1
    pov "W-Well, you know: ancient Chinese knowledge!"
    show bg allawaytruck_2
    pov "It's not my fault that the Chinese chose such a weird method to spread their philosophy and message!"
    show bg allawaytruck_1
    mis "Ancient chinese- what?!"
    show bg allawaytruck_2
    mis "Fortune cookies were invented in the 19th century in Kyoto, Japan and then popularized in the 1900's by a bakery in San Francisco!"
    show bg allawaytruck_1
    mis "They have nothing to do with the Chinese!"
    show bg allawaytruck_2
    pov "Oh well, whooptiy fuckin' doo! Miss Allaway, thank you for that knowledge!"
    show bg allawaytruck_1
    pov "I'll remember that for the test tomorrow!"
    show bg allawaytruck_2
    mis "Don't you fucking give me sass, boy!"
    show bg allawaytruck_1
    mis "We have a bag filled with drugs in our car."
    show bg allawaytruck_2
    mis "What we need to do is get them to whoever the frik- probably fuckin' Dr Zuess and the Cat with a Hat."
    show bg thegetaway_street_1
    pov "You're right, you're right!"
    pov "I'm sorry!"
    pov "Quick, turn here!"
    pov "Shit shit shit-"
    mis "Are they still following us? You're making me fucking panicky, [povname]! Stop that!"
    $ renpy.pause()
    show bg thegetaway_street_2
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg thegetaway_street_3
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg thegetaway_street_4
    with dissolve
    $ renpy.pause(1,hard=True)

    jump lbl_the_drop_off
