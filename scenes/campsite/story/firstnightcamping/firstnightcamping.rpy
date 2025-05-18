## First Night Camping
label lbl_first_night_camping:
    ## You’re all snuggled up together in the dark
    scene black
    with fade
    $ renpy.pause()
    "Later that cold night..."
    
    scene bg campsite_5
    with fade
    $ renpy.pause

    pov "{i}*Shiver*{/i}"
    pov "..."
    pov "A-am I the only one shivering?"

    sis "N-n-no... you and me b-both-"

    mum "M-make it all of us..."

    sis "D-did we really have to put out the fire?"

    pov "Y-yes-"
    pov "It’s dangerous to have it g-going while we sleep-"

    mum "W-we just have to huddle a little closer-"

    sis "We’re huddling as close as possible-"
    sis "I’m s-still freezing my tits off."

    pov "I can feel your nips poking through all those layers."

    mum "L-listen..."
    mum "Th-this might sound counterintuitive..."
    mum "B-but we’ll have to strip naked and cuddle each other skin to skin."

    sis "That does sound counterintuitive-"

    pov "No, she’s right."
    pov "And I’m not just saying that cause we get to be naked."
    pov "T-trust me, the thought of stripping my clothes now is the last thing I want."
    pov "But the skin on skin will help spread the body heat better."

    sis "F-fine..."
    sis "It’s not like I can get any colder."

    if winc == 0:
        mum "Hurry, guys. The sooner we get bare, the faster we can warm up properly."
    else:
        mum "Hurry, kids. The sooner we get bare, the faster we can warm up properly."

    ## CG now of them in this order; MC, Sister, Mom.
    scene bg firstnightcamping_1
    with fade
    $ renpy.pause()

    mum "Get closer to each other."
    mum "[povname], keep [sister] warm."

    pov "I am- I am."

    sis "{i}*Exhale*{/i}"
    sis "This- this is working actually."
    if winc == 0:
        sis "Hug me tighter, [missus]."
    else:
        sis "Hug me tighter, mom."

    mum "I’m trying, my boobs are too big."

    sis "[povname]. Get closer, seriously."

    pov "If I get any closer, I’d be inside you."

    sis "I don’t care, put it inside me."

    mum "Do it, honey."

    pov "I’m not even hard."

    sis "C’mon, [povname]."

    mum "You can get hard inside her, sweetie. Just put it in."

    pov "I’ll try-"

    show bg firstnightcamping_2_1
    with hpunch

    sis "Ah-"
    sis "{i}*Exhale*{/i}"
    sis "Careful, [povname]."

    pov "Can’t you get a little wetter for me? It would make this a lot easier."

    mum "Go slowly, [povname]."

    pov "I know, I know."

    sis "Mmhph-"

    pov "Alright, it’s in."

    mum "Good boy."
    mum "You feeling better, [sister]?"

    sis "A little-"

    mum "You’re starting to heat up more, I can feel it on your back."

    sis "Is-"
    if winc == 0:
        sis "Is it okay if [povname] and I fucked, [missus]?"
    else:
        sis "Is it okay if [povname] and I fucked, mommy?"

    mum "You go right ahead, only if [povname] wants to of course."
    mum "It’ll warm up the tent even more."

    pov "I got this."

    ## You both start fucking with mom holding you both.
    scene firstnightcamping_hscene1
    $ renpy.pause()

    sis "Mmmm-"

    pov "{i}*Moans*{/i}"
    
    mum "Goodnight, my darlings."

    ## SCENE END

    scene black
    with fade
    $ renpy.pause()
    "You continued to fuck until you tired each other out and fell asleep in each other's warmth..."
    "Neither one came, but you were both definitely on the edge..."

    $ mumsiscamp_path = 8

    $ renpy.pause()

    jump lbl_naked_yoga

image firstnightcamping_hscene1:
    "/scenes/campsite/story/firstnightcamping/assets/bg_firstnightcamping_2_1.jpg"
    pause 0.3
    "/scenes/campsite/story/firstnightcamping/assets/bg_firstnightcamping_2_2.jpg"
    pause 0.3
    "/scenes/campsite/story/firstnightcamping/assets/bg_firstnightcamping_2_3.jpg"
    pause 0.3
    "/scenes/campsite/story/firstnightcamping/assets/bg_firstnightcamping_2_4.jpg"
    pause 0.3
    "/scenes/campsite/story/firstnightcamping/assets/bg_firstnightcamping_2_2.jpg"
    pause 0.3
    repeat