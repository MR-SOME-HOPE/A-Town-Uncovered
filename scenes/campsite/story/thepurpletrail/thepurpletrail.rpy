## The Purple Trail
label lbl_the_purple_trail:
    ## Scene black cuz I don’t wanna animate it.
    scene black
    with fade
    $ renpy.pause()
    "After a while in the natural spring..."

    mum "This trail doesn’t seem too hard."

    sis "Yeah actually, it’s pretty chill."
    sis "There’s also a really nice breeze."

    pov "And the smell of nature."

    sis "I feel myself growing a third lung from how good the air is."

    mum "I should’ve brought binoculars so we can bird watch."

    sis "Bird watch."
    sis "[povname]. Bird watch."

    if winc == 0:
        pov "Yeah, as if you’d be into bird watching, [missus]."
    else:
        pov "Yeah, as if you’d be into bird watching, mom."
    pov "You’re not that old."

    mum "It’s not an old people thing, is it?"

    pov "They say that bird watching is a milestone in any man’s life."

    sis "And clearly it’s not something that women usually get into."
    sis "No offense."

    mum "Hey, I just thought looking at birds close up would be a cool thing to do."
    mum "Nothing about recognizing their call or trying to distinguish the species from a book."

    pov "I just find it funny."

    sis "What is this camping spot anyway?"
    sis "Please tell me it’s another natural spring to soak in for another 2 hours."

    mum "It’s not. But we can definitely go back there tomorrow for another relaxation session if you want."

    pov "Are we there yet?"

    mum "Are your legs getting tired already?"
    mum "Did we empty you too early in the day?"

    pov "No- I’m just hungry."

    sis "Same."

    mum "We’re almost there, just a little further."

    sis "How do you know?"

    mum "I don’t. I’m just saying stuff to get you to keep going."

    sis "UGHHHH!"

    ## Time skip
    "Reaching the picnic spot..."
    
    scene bg thepurpletrail_1
    with fade

    pov "Wow- I have never seen a place like this. "
    pov "It kind reminds me of something you get out of a children’s story book."

    mum "They called it The Purple Trail and I now see why."

    sis "They shoulda called it the Lavender Trail for more obvious reasons."

    pov "I think that would’ve spoiled the surprise, would it not."

    if winc == 0:
        mum "You guys do so much talking for someone that was complaining about being starving."
    else:
        mum "You kids do so much talking for someone that was complaining about being starving."
    mum "Eat your sandwiches, there’s plenty packed and I also got some of those hotdog pastries you both love."

    sis "Oooh yes! Those things should be banned for how addicting they are."

    pov "Don’t hog it all."

    ## Time skip
    scene black
    with fade
    $ renpy.pause()
    "After lunch…"

    scene bg thepurpletrail_2
    with fade

    pov "Well, I’m stuffed. Should we head back?"

    mum "Let’s just sit here for a few minutes, I don’t wanna walk back right after eating."

    sis "Same."
    sis "But hey, there’s no more of the hotdog pastries."

    pov "I ate the last one."

    sis "The hell, dude?"
    sis "You had way more than me."

    pov "We had an even amount I was counting."

    if winc == 0:
        sis "Well even so, you should’ve given me the last one because you’re such a nice guy."
    else:
        sis "Well even so, you should’ve given me the last one because you’re such a nice baby brother."

    pov "I’m only younger by a few minutes, remember."

    mum "I should’ve packed exclusively hotdog pastries…"

    sis "Screw you man, you get the satisfaction of having the last one and I’m still craving it."

    pov "You can get all the hotdog pastries you want when we get back home."
    pov "This is so stupid to argue over."

    mum "Yes, I agree. [sister] honey. Be civil."

    sis "You’ll have to give me your hotdog instead you selfish prick."

    pov "Ah?! Excuse you."

    if winc == 0:
        sis "[missus], tell [povname] he has to feed me his hotdog."
    else:
        sis "Mom, tell [povname] he has to feed me his hotdog."

    if winc == 0:
        mum "Why are you two acting like such goonies."
    else:
        mum "Why are you two acting like such children."
    mum "We just had a nice meal together."
    mum "You should both be passed out in food coma in the grass."

    pov "That actually sounds really nice."
    pov "Lemme just lay on the grass."

    sis "..."
    sis "Hmph.."

    ## Time skip
    scene black
    with fade
    $ renpy.pause()
    "A few minutes later…"

    pov "Aye?!"
    pov "Get off me!"

    if winc == 0:
        sis "[missus] said I can have you."
    else:
        sis "Mom said I can have you."

    mum "I said no such thing."

    sis "Just close your eyes and let me feast."
    if winc == 0:
        sis "You want in on this, [missus]?"
    else:
        sis "You want in on this, mom?"

    mum "*Sigh*"
    mum "Fine."
    mum "Stay still, [povname]."
    if winc == 0:
        mum "[sister] has that scary look in her eye."
    else:
        mum "Your sister has that scary look in her eye."

    pov "Pfft, you’ve got to be kidding me."

    mum "I didn’t pack dessert so you’re our next best thing."

    ## Mom and Sister gives you a BJ in the grass.
    scene thepurpletrail_bj1
    with fade
    $ renpy.pause()
    show thepurpletrail_bj2
    $ renpy.pause()
    show bg thepurpletrail_3_6
    with vpunch
    $ renpy.pause()
    
    pov "Fuck-"
    pov "Hope you guys got your dessert fill."

    sis "Oooh surprise icing."

    mum "Yummy, just enough to hit the spot."

    $ mumsiscamp_path = 6

    jump lbl_campfire_chilling

image thepurpletrail_bj1:
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_1.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_5.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.3
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.3
    repeat

image thepurpletrail_bj2:
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_1.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_5.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_4.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_3.jpg"
    pause 0.2
    "/scenes/campsite/story/thepurpletrail/assets/bg_thepurpletrail_3_2.jpg"
    pause 0.2
    repeat
