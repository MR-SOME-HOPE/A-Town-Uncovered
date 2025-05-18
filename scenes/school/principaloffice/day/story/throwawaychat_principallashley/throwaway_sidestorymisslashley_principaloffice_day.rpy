## Director Lashley Side Story Throwaway Conversations Director Office ##
default principaloffice_spareboxes = 0

## Spare Boxes
label lbl_principaloffice_day_principallashley_spareboxes:
    show pov neutral_talk at left
    with dissolve
    show pri neutral at right
    with dissolve
    pov "Hi, Director Lashley."
    show pov neutral at left
    show pri neutral_talk at right
    pri "[povname]. What a pleasant surprise."
    pri "Blessed be thy name."
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Uh- yeah. Hallelujah! Hehehe..."
    show pov neutral_talk at left
    show pri confused at right
    pov "Listen, I was wondering if you have any spare cardboard boxes sitting around collecting dust."
    show pov neutral at left
    show pri confused_talk at right
    pri "Why do you ask? Do you need some."
    show pov neutral_talk at left
    show pri confused at right
    pov "Yes, I do. Yes, please."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Hmmm, well I can't see any around me right now."
    show pri embarrassed_talk at right
    pri "Sorry I couldn't be of any more help right now."
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Alright, don't worry about it. I'll keep looking."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "I'll pray for your search."
    show pri bored_talk at right
    pri "And if you see a sign, take it. God is watching over all of us."
    show pov embarrassed_talk at left
    show pri smirk at right
    pov "Duly... noted. Thanks, Director L."

    $ principaloffice_spareboxes = 1

    jump lbl_principaloffice_day_setup

## Lashley Movie Date
label lbl_principaloffice_day_lashley_moviedate:
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show pri neutral at right
    with dissolve
    pov "Hey, Director Lashley. I was wondering if you wanted to accompany me with a movie tonight?"
    show pov neutral at left
    show pri confused_talk at right
    pri "[povname], you do know how busy I am."
    show pov smirk_talk at left
    show pri neutral at right
    pov "I know, I was just hoping to strengthen our bond together and- with the Lord."
    show pov smirk at left
    show pri neutral_talk at right
    pri "Hmm- I guess we can discuss the bible and the Lord's word before and after the movie."
    pov "Yeah! And I'm sure a smart, wise mind like yours can help decypher a movie's message and how it relates to the Lord."
    pri "That's true, that'll be a good exercise for us."
    pri "Alright, [povname]. You've convinced me, I'll meet you there tonight."
    pri "I best get all the work I need done by then, God bless your sweet heart, [povname]."

    scene black
    with fade
    $ renpy.pause(1.5)
    "At the cinema..."
    stop music fadeout 2.0
    $ moviedate = 4
    $ gtime = 2

    jump lbl_cinema_night_setup
