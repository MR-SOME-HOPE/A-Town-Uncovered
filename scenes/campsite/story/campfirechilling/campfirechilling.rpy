## Campfire Chilling
label lbl_campfire_chilling:
    ## You’re all surrounding the campfire with marshmallows on sticks.
    scene bg campsite_4
    with fade

    stop music fadeout 2.0
    play ambience 'audio/ambience/quietexteriornight_ambience.ogg' fadein 2.0

    $ renpy.pause()

    show pov embarrassed_talk at left
    show sis neutral at Position(xpos=1300)
    show mumc neutral at right
    with dissolve
    pov "Thanks for uh- bringing that lighter."
    pov "I have absolutely no idea how to make a fire."

    show pov embarrassed at left
    show sis smirk_talk at Position(xpos=1300)
    show mumc neutral at right
    sis "Yeah, we could tell. It was really sad to watch."

    show pov bored at left
    show sis smirk at Position(xpos=1300)
    show mumc smirk_talk at right
    mum "I thought it was funny."
    show mumc shocked_talk at right
    mum "Cute!"
    show mumc neutral_talk at right
    mum "I thought it was cute. Hehehe~"

    show pov bored_talk at left
    show mumc smirk at right
    pov "Tch, you guys just love seeing me physically suffer."
    pov "First the tent, then the picnic, and lastly the fire."

    show pov bored at left
    show mumc smirk_talk at right
    mum "Oh, sweetie. It’s only because we love you."
    mum "And because-"
    show mumc embarrassed_talk at right
    mum "Well, I thought if you believed in yourself and worked at it for long enough you’d get that fire going."
    mum "A fire made the old fashioned way would’ve been very rewarding, wouldn’t it?"

    show pov embarrassed at left
    show sis neutral_talk at Position(xpos=1300)
    show mumc neutral at right
    sis "Like that scene in Castaway starring Hom Tanks."

    show pov embarrassed_talk at left
    show sis neutral at Position(xpos=1300)
    show mumc neutral at right
    pov "Well, I gave it my best shot."
    pov "Maybe next time we go on another camping trip, I would’ve learnt how to make a fire on my own."

    show pov neutral at left
    show mumc neutral_talk at right
    mum "That’d be nice."

    show sis shocked_talk at Position(xpos=1300)
    show mumc neutral at right
    sis "I can’t remember the last time I had s’mores."
    show sis embarrassed_talk at Position(xpos=1300)
    sis "At least not like this."
    sis "I’ve never had s’mores over an open campfire."

    show pov confused at left
    show sis shocked at Position(xpos=1300)
    show mumc neutral_talk at right
    mum "We used to make them over our gas heater when you were really young during the winter."

    show pov neutral_talk at left
    show sis neutral at Position(xpos=1300)
    show mumc neutral at right
    pov "This beats that by a long shot."

    show pov smirk at left
    show sis smirk_talk at Position(xpos=1300)
    sis "Hell yeah."

    show sis smirk at Position(xpos=1300)
    show mumc embarrassed at right
    mum "..."
    show pov neutral at left
    show sis neutral at Position(xpos=1300)
    show mumc embarrassed_talk at right
    mum "This-"
    mum "You guys are making me so happy right now."
    show pov embarrassed at left
    show sis embarrassed at Position(xpos=1300)
    mum "This image of us 3, smiling and laughing around the fire, having had an amazing day out in nature."
    mum "This is what I hoped for."
    mum "And-"
    show mumc sad at right
    mum "{i}*Sniff*{/i}"
    show mumc sad_talk at right
    mum "I just-"
    mum "Love you both so much."

    show sis sad_talk at Position(xpos=1300)
    show mumc sad at right
    if winc == 0:
        sis "Oh my God, [missus]."
    else:
        sis "Oh my God, mom."
    sis "You’re such an emotional mess."
    sis "You’re gonna make me cry!"

    show pov embarrassed_talk at left
    show sis sad at Position(xpos=1300)
    show mumc sad at right
    pov "You two are gonna make me cry too."
    show sis embarrassed at Position(xpos=1300)
    show mumc sad at right
    pov "And not cause I’m emotional but because I’m an empath."
    
    show pov neutral at left
    show sis smirk_talk at Position(xpos=1300)
    show mumc embarrassed at right
    sis "Pffft, get that outta here, dude."

    show pov shocked at left
    show sis embarrassed at Position(xpos=1300)
    show mumc sad_talk at right
    mum "Oh my God. I love my babies so much."
    show pov embarrassed at left
    mum "And you both are growing up so fast."
    mum "Please-"
    mum "Please promise me that you’ll always stay my babies and we’ll go on fun adventures like this often."
    mum "Promise me."

    show pov embarrassed_talk at left
    show mumc embarrassed at right
    if winc == 0:
        pov "We promise, [missus]."
    else:
        pov "We promise, mom."

    show pov embarrassed at left
    show sis embarrassed_talk at Position(xpos=1300)
    sis "Yeah, we promise."
    sis "It took some time to win me over with this camping idea but you really did."
    sis "I’m happy to be here with you both."

    show pov embarrassed_talk at left
    show sis embarrassed at Position(xpos=1300)
    pov "Ditto."
    pov "Ms Sobby sob."
    pov "Tears running down all over your face."
    pov "Good thing there’s no one else here to see you, that’d be really embarrassing."

    show pov neutral at left
    show mumc embarrassed_talk at right
    mum "I can’t help it."
    mum "You both mean the world to me."

    show sis neutral_talk at Position(xpos=1300)
    show mumc embarrassed at right
    if winc == 0:
        sis "I love you too, [missus]."

        show pov neutral_talk at left
        show sis embarrassed at Position(xpos=1300)
        pov "I love you too, [missus]."

    else:
        sis "I love you too, mom."

        show pov neutral_talk at left
        show sis embarrassed at Position(xpos=1300)
        pov "I love you too, mom."

    show pov neutral at left
    show sis neutral at Position(xpos=1300)
    show mumc sad_talk at right
    mum "I love you both so much."
    if winc == 0:
        mum "Right now, I feel like the world’s greatest [mumrole]."
    else:
        mum "Right now, I feel like the world’s greatest mom."

    show pov neutral_talk at left
    show mumc shocked at right
    pov "You even have a mug to prove it."

    show pov neutral at left
    show sis neutral at Position(xpos=1300)
    show mumc sad_talk at right
    mum "I love that mug."

    show sis smirk_talk at Position(xpos=1300)
    show mumc embarrassed at right
    if winc == 0:
        sis "Yeah, cause I made it myself in school for Xmas day."
    else:
        sis "Yeah, cause I made it myself in school for mother’s day."

    show sis neutral at Position(xpos=1300)
    show mumc embarrassed_talk at right
    mum "I love that mug."

    show sis confused_talk at Position(xpos=1300)
    show mumc sad at right
    sis "You never use it though."

    show sis confused at Position(xpos=1300)
    show mumc shocked_talk at right
    mum "It’s a display piece!"

    show pov bored_talk at left
    show sis bored at Position(xpos=1300)
    show mumc embarrassed at right
    pov "It has holes in it, [sister]. How is she supposed to keep liquid in it?"

    show pov smirk at left
    show sis sad_talk at Position(xpos=1300)
    show mumc smirk at right
    sis "You could at least try."

    show pov neutral at left
    show sis embarrassed at Position(xpos=1300)
    show mumc neutral_talk at right
    mum "Hahahaha!"

    show sis shocked_talk at Position(xpos=1300)
    show mumc neutral at right
    sis "Hey, put more sticks on the fire, it’s getting smaller."

    show pov neutral_talk at left
    show sis neutral at Position(xpos=1300)
    show mumc embarrassed at right
    pov "On it."

    ## SCENE END

    $ mumsiscamp_path = 7

    jump lbl_first_night_camping
