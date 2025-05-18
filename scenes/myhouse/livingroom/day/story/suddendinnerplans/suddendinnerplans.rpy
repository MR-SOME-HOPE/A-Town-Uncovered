##[Living room, afternoon - “Sudden Dinner Plans”  - main_story =85]

##-After all main scenes are over, the player is instructed to go back home-
label lbl_sudden_dinner_plans:

    scene bg mylivingroom_day
    with fade
    show pov neutral at left
    with dissolve
    show pov neutral_talk at left
    pov "Well, those were all my options available."
    pov "I just hope that Edward keeps his word and that manages to bring out something from the cameras."
    show pov embarrassed_talk at left
    pov "I hope this wasn’t all for nothing…"
    show pov neutral_talk
    pov "I should also wait for Jacob’s call, hopefully he manages to win Effie over for me to fix this with her."

    ##-Missus calls the Mc from another room-

    mum "[povname], are you home?"
    show pov neutral_talk at left
    pov "Yeah, [missus]. I just got here."

    mum "Good. Do you have any plans for dinner tonight?"
    show pov neutral_talk at left
    pov "Nothing at the moment that I know of, why?"

    ##-Missus walks into scene-

    show mum neutral_talk at right
    with dissolve
    mum "Because we apparently have some now."

    if mum_path < 31:
    #-If Missus has not been Romanced-
        show pov neutral_talk at left
        show mum neutral at right
        pov "Oh are we going out or got invited somewhere?"
        show pov confused_talk
        pov "Or are we gonna celebrate someone’s birthday out of the blue or something?"
        show pov confused at left
        show mum embarrassed_talk at right
        mum "Nothing of the sort, actually."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "Then what’s the occasion in that case?"

        #=RESULT END=

    elif mum_path >= 31:
    #-If Missus has been Romanced-
        show pov neutral_talk at left
        show mum neutral at right
        pov "You asking me out?"
        show pov smirk_talk at left
        pov "I don’t mind or anything, but if we are having fun afterwards I should probably cancel my plans for tomorrow too."
        show pov smirk at left
        show mum smirk_talk at right
        mum "My, that does sound like a good time~"
        mum "Do put a pin on that for later."
        show mum embarrassed_talk
        mum "Sadly we are booked for the night, so I doubt we’ll have time for any fun of that sort."
        show pov confused_talk
        pov "Alright, then what’s the occasion?"

        #=RESULT END=

    show pov neutral at left
    show mum neutral_talk at right
    with dissolve
    mum "It’s your father."
    show mum confused_talk
    mum "He just called me out of the blue asking for us to have family dinner all together."
    show pov confused_talk at left
    show mum confused at right
    pov "Did he get a promotion or something?"
    pov "We haven’t had one of those in forever."
    show pov embarrassed_talk at left
    pov "Much less one dad is present."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "He didn’t say, but he did mention he had an announcement that he wanted you to hear specifically."
    show mum shocked_talk at right
    mum "He even asked me to go full out and prepare him some of my homemade lasagna!"
    mum "Because that doesn’t take time for preparation and time to make and isn’t a total chore for me, which is why I rarely make it."
    show pov bored_talk at left
    show mum embarrassed at right
    pov "Not the family reunion you wanted, huh?"
    show pov bored at left
    show mum angry_talk at right
    mum "I swear to God he has me about to explode."
    mum "I still haven’t been able to talk to him about the whole alarm system thing, much less about everything he has been doing lately."
    show mum bored_talk
    mum "Now he just calls out of nowhere and demands me to make dinner for him. Treat him like nothing is wrong and he expects me to be the good 50’s housewife, without complaining about it?"
    show mum angry_talk
    mum "He is walking a very thin line here and he keeps playing chicken with the edge!"
    show pov bored_talk at left
    show mum angry at right
    pov "We can bring all of this to his face tonight."
    show pov smirk_talk at left
    pov "You know that neither [sister] or I have any intention to keep quiet about all his bullshit if you give us the chance."
    pov "There is plenty we have to say to him and I think him getting some consequences for his actions is well deserved by now."
    show pov smirk at left
    show mum bored_talk at right
    mum "Best not for now, [povname]."
    mum "He is already hostile as all hell, but if he is bombarded with all of our frustration the moment he comes home, I’m genuinely afraid of what he’ll do."
    show pov confused_talk at left
    show mum bored at right
    pov "This can’t continue, [missus]…"
    show pov confused at left
    show mum bored_talk at right
    mum "I know, I know…"
    show mum embarrassed_talk at right
    mum "But for now, let me handle it in a way that doesn’t completely tear us apart."
    show mum smirk_talk at right
    mum "I’m tougher than you think, you know?"
    show pov bored_talk at left
    show mum embarrassed at right
    pov "We’ve had this conversation already but I still don’t like it."
    show pov confused_talk at left
    pov "I know you want me to trust you and all, but what if you get hurt?"
    pov "How am I supposed to live with myself if he hurts you and we are not able to stop him?"
    show pov smirk_talk at left
    pov "Don’t pretend the possibility doesn’t scare you too."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "Of course it does, but it's because of the possibility of him lashing out at you or your sister which has me even more scared than being scared for my own safety."
    show mum sad_talk at right
    mum "I’m asking you to trust me on this despite your own fear."
    show mum embarrassed_talk at right
    mum "It’s my duty as your [mumrole] to protect you guys, not the other way around."
    show pov smirk_talk at left
    show mum embarrassed at right
    pov "That really isn’t making me feel any better about all of this whatsoever."
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "I know it doesn’t."
    mum "I’m sorry, I really wish I could say anything that would get you to trust me…"
    show mum sad_talk at right
    mum "But for now that is all I have."
    show pov sad_talk at left
    show mum sad at right
    pov "[missus]…"
    show pov sad at left
    show mum neutral_talk at right
    mum "It will all be okay, I promise."
    show mum embarrassed_talk at right
    mum "I know he may seem to be about to cross that one line, but…"
    show mum neutral_talk at right
    mum "I also want to trust that there is still a piece of the man I knew before all of this."
    show pov shocked_talk at left
    show mum neutral at right
    pov "How can you be so sure about all this?"
    pov "Why keep giving him chances?"
    show pov shocked at left
    show mum embarrassed_talk at right
    mum "Because something must be wrong, for him to be like this."
    mum "Besides, you never know."
    show pov bored at left
    show mum bored_talk at right
    mum "Who is to say you won’t have a similar unexplainable behaviour out of nowhere?"
    show pov confused at left
    show mum confused_talk at right
    mum "One where you put yourself in danger or do something you would have never done before?"
    show mum smirk_talk at right
    mum "Like going around nude after disappearing for a whole day, perhaps?"
    show pov shocked_talk at left
    show mum smirk at right
    pov "I…"
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I know, but still, wouldn’t you be hoping someone gives you a chance to redeem yourself afterwards?"
    mum "Even if it is a second, third, or fourth chance afterwards?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "I’m not planning on that thing happening again, you know?"
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I do. But if it does happen, I have to be there to give you the chance to fix things."
    mum "Call me naive or even stupid if you want, but…"
    show mum neutral_talk at right
    mum "Well, that’s just the kind of woman I am."
    show mum embarrassed_talk at right
    mum "As long as that one line, that tiny little line in the sand; in this case him becoming actually violent at us, being that line."
    mum "As long as that line isn’t crossed."
    show mum neutral_talk at right
    mum "Then I’ll keep giving him a chance for him to fix things."
    show mum embarrassed_talk at right
    mum "We are only human and we all deserve a second chance."
    show pov sad at left
    show mum embarrassed at right
    pov "…"
    show mum embarrassed_talk at right
    mum "It’s the choices who make us who we are, and we can always choose to do what’s right."
    mum "So I’ll still offer him a chance to fix things."
    show pov bored_talk at left
    show mum embarrassed at right
    pov "I see..."
    show pov bored at left
    show mum embarrassed at right
    mum "Everything will be okay, I promise."
    mum "Whatever happens, at least [sister], you and I are together."
    show mum neutral_talk at right
    mum "So I know we can move on from anything that may come."
    show pov bored at left
    show mum neutral at right
    pov "…"
    show pov bored at left
    show mum embarrassed_talk at right
    mum "Look, just be here and try to have a nice dinner for me, okay?"
    show mum neutral_talk at right
    mum "It is still lasagna, and it’s still gonna be good."
    show mum embarrassed_talk at right
    mum "Whatever he wants to bring up to you, just take it and we’ll figure out how to deal with it later on."
    show mum sad_talk at right
    mum "That and…"
    show pov smirk_talk at left
    show mum sad at right
    pov "And?"
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "Just…"
    mum "Just promise me you are not going to grow up to be like him…"
    show pov sad at left
    show mum sad_talk at right
    mum "That you won’t treat those who love you like a doormat whenever you feel like it."
    show mum embarrassed_talk at right
    mum "You still have a good head on your shoulders, so don’t ruin that image, of the people who depend on you."
    show pov sad_talk at left
    show mum embarrassed at right
    pov "Of course, [missus]."
    pov "I don’t ever want to be anything close to what he is becoming."
    show pov embarrassed_talk at left
    pov "I promise."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Good…"
    mum "Okay, will you help me with dinner? I really need an extra pair of hands due to the short notice."
    show mum neutral_talk at right
    mum "I won’t leave anything too difficult, I promise."
    show pov neutral_talk at left
    show mum embarrassed at right
    pov "Sure, [missus]."
    show pov embarrassed_talk at left
    pov "You don’t even have to ask."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Thank you, [povname]."
    mum "I love you."
    show pov neutral_talk at left
    show mum embarrassed at right
    pov "I love you too."

    $ main_story = 85
    $ gtime = 2
    # $ townmap_enabled = 0 #TEMP until fix?

    jump lbl_an_awkward_dinner_situation
