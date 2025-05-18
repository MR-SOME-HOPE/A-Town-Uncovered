## Grundle Sam Main Story Throwaway Conversations Stuff Store ##
default stuffstore_ajob = 0
default sexaroundtowngrundlesam = 0

## A Job
label lbl_stuffstore_day_grundlesam_ajob:
    show pov embarrassed_talk at left
    with dissolve
    show sam neutral at right
    call lbl_stuffstore_counter_check
    with dissolve
    pov "Um...."
    show pov embarrassed at left
    pov "{i}Am I that desperate that I'm asking him for a job?{/i}"
    show pov embarrassed_talk at left
    show sam shocked at right
    pov "Are you... hiring?"
    show pov embarrassed at left
    show sam sad_talk at right
    sam "Not at the moment, ma good sir."
    show pov bored at left
    show sam embarrassed_talk at right
    sam "Business is barely afloat so I can't afford to pay you anything. Hehehehe~"
    show sam embarrassed at right
    pov "{i}Am I that surprised?{/i}"
    show pov embarrassed_talk at left
    pov "Alright, thanks anyways."
    show pov embarrassed at left
    show sam confused_talk at right
    sam "Are you not going to buy anything, ma good sir?"
    show pov embarrassed_talk at left
    show sam confused at right
    pov "Maybe.. later?"
    show pov embarrassed at left
    show sam smirk_talk at right
    sam "I'll hold you to it, ma good sir. Hehehehe~"
    show pov bored at left
    sam "If you would like some more luck in finding a job. This bronze rabbit totem-"
    show pov bored_talk at left
    show sam shocked at right
    pov "I'll see you, Sam."

    $ stuffstore_ajob = 1

    jump lbl_stuffstore_day_setup

## Sex Around Town Grundle Sam
label lbl_stuffstore_day_grundlesam_sexworld:
    if sexaroundtowngrundlesam == 0:
        ## Sprite Start
        show pov shocked_talk at left
        with dissolve
        show samsw neutral at right
        call lbl_stuffstore_counter_check
        with dissolve

        pov "Jesus Christ!"
        show pov embarrassed_talk at left
        show samsw confused at right
        pov "Why are you naked, Sam?"
        show pov embarrassed at left
        show samsw neutral_talk at right
        sam "Good day, ma good sir!"
        show pov embarrassed at left
        show samsw confused_talk at right
        sam "This is what I always wear?"
        sam "You've never commented on my attire before."
        show pov confused_talk at left
        show samsw neutral at right
        pov "A single leaf?"
        show pov confused at left
        show samsw embarrassed_talk at right
        sam "I know it's tacky."
        sam "Some say those shirts with a printed tuxedo on it is tacky."
        show pov neutral at left
        show samsw neutral_talk at right
        sam "But in some parallel universe I would wear that every single day."
        show pov shocked_talk at left
        show samsw neutral at right
        pov "Oh my god! You actually do!"
        show pov neutral at left
        show samsw neutral_talk at right
        sam "Hahaha! That's funny, ma good sir."
        show pov sad at left
        show samsw sad_talk at right
        sam "People usually walk out as soon as I make interesting conversation."
        show pov smirk_talk at left
        show samsw neutral at right
        pov "'Interesting' is one way to put it."
        show pov neutral at left
        show samsw neutral_talk at right
        sam "What can I help you with today?"
        show pov confused_talk at left
        show samsw confused at right
        pov "Yes, in fact you can. I wouldn't ask if I wasn't desperate for answers but maybe you could shed some light on the subject."
        show pov neutral at left
        show samsw confused_talk at right
        sam "Proceed...?"
        show pov confused_talk at left
        show samsw neutral at right
        pov "Why is everyone so... naked... and having sex out in the open?"
        pov "Is there a festival going on today?"
        show pov confused at left
        show samsw neutral_talk at right
        sam "There is actually! It'll be awesome! We get to witness this year's chosen one and watch as they fuck like it's their last!"
        sam "I hope to see you there, I'll take my chance and try and sell some of my totems."
        show pov embarrassed_talk at left
        show samsw neutral at right
        pov "Oh-kay... weird 'festival'... We'll see if I show up."

        $ sexaroundtowngrundlesam = 1

    else:
        show pov neutral at left
        with dissolve
        show samsw neutral_talk at right
        call lbl_stuffstore_counter_check
        with dissolve

        sam "Hello, ma good sir."
        sam "Here to trade in your totem?"
        show pov confused_talk at left
        show samsw neutral at right
        pov "Not really."
        pov "I'm just... I kinda just walked back in here for some reason."

    jump lbl_stuffstore_day

## Buukakki Followers Are Everywhere - Grundle Sam
label lbl_buukakki_followers_are_everywhere_grundlesam:
    ## SPRITE START NO BG NEEDED
    show pov neutral_talk at left
    show sam confused at right
    pov "Hey, Grundle Sam."
    show pov neutral at left
    show sam neutral_talk at right
    with dissolve
    sam "How are you my fellow sir?"
    show pov confused_talk at left
    show sam neutral at right
    pov "What’s up with all these people handing out the same flyers?"
    show pov shocked_talk at left
    pov "The Followers of Master Buukakki."
    show pov embarrassed_talk at left
    show sam smirk at right
    pov "Have you heard anything about this Master Buukkakki?"
    show pov smirk_talk at left
    pov "What’s he a Master in?"
    show pov embarrassed at left
    show sam neutral_talk at right
    sam "One question at a time, my good sir."
    sam "I have received one of these flyers myself and I have questioned it myself."
    show pov confused at left
    show sam confused_talk at right
    sam "I know a lot about this town’s history."
    show pov shocked at left
    show sam neutral_talk at right
    sam "But unfortunately this is all new to me, my good sir."
    show pov smirk_talk at left
    show sam confused at right
    pov "Really?"
    show pov confused_talk at left
    pov "Nothing rings a bell?"
    show pov bored at left
    show sam neutral_talk at right
    sam "Not a single ding or a dong."
    show sam smirk_talk at right
    sam "I must say though, the way they’re aggressively trying to recruit people into their cult is quite astounding to say the least."
    show pov shocked_talk at left
    show sam shocked at right
    pov "So it IS a cult!"
    show pov angry at left
    show sam embarrassed_talk at right
    sam "Well, I mean, look at it objectively."
    show sam confused_talk at right
    sam "There’s no other way to call it, my good sir."
    show sam embarrassed_talk at right
    sam "Never have I seen such a forceful push for it."
    show sam bored_talk at right
    sam "And so out of nowhere."
    show pov smirk_talk at left
    show sam embarrassed at right
    pov "Right? They’re everywhere."
    show pov bored at left
    show sam smirk_talk at right
    sam "Where did they all come from?"
    show pov confused at left
    show sam shocked_talk at right
    sam "How many more people are part of this? Who in my life would be secretly part of this cult?"
    show pov confused_talk at left
    show sam shocked at right
    pov "Damn…"
    pov "I wonder if anyone I know is as well…"
    show pov shocked_talk at left
    show sam confused at right
    pov "Fuck… kinda creepy thinking about it."
    show pov smirk_talk at left
    pov "You think you know a person until you find them handing out these flyers…"
    show pov confused at left
    show sam embarrassed_talk at right
    sam "Don’t have high expectations for anyone, my good sir."
    show sam sad_talk at right
    sam "Cults prey on the weak, don’t judge people too harshly."
    show pov embarrassed_talk at left
    show sam sad at right
    pov "Thanks, Sam."
    pov "Take care now."
    show pov neutral at left
    show sam shocked_talk at right
    sam "Oh- you’re not gonna buy anything? Okay."
    show sam neutral_talk at right
    sam "Thank you for stopping by, my good sir."

    $ buukakkifollowers_grundlesam = 1

    call lbl_buukakki_followers_are_everywhere_check

    jump lbl_stuffstore_day_setup
