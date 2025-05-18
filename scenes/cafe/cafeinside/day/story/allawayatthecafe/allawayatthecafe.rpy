## Allaway at the Cafe  ##
label lbl_allaway_at_the_cafe:

    scene bg cafeinside_day
    with fade
    show pov shocked at left
    with dissolve
    pov "..."
    if gtime == 0:
        pov "{i}Is- is that Miss Allaway talking to Brock?{/i}"
    else:
        pov "{i}Is- is that Miss Allaway talking to Effie?{/i}"

    menu:
        "Say hello":
            show pov neutral_talk at left
            show misc shocked at right
            with dissolve
            pov "Hey, Miss. Fancy seeing you here."
            show pov neutral at left
            show misc neutral_talk at right
            mis "Hey, [povname]. Haven't seen you in here before. You come here often?"
            show pov neutral_talk at left
            show misc neutral at right
            pov "I stop by from time to time."
            show pov neutral at left
            show misc neutral_talk at right
            mis "Oh, really? I come here every weekend, it's my favourite place to eat brunch at."
        "Wait for her to finish ordering":
            show pov embarrassed at left
            pov "..."
            if gtime == 0:
                bro "Hey, [povname]! Will be with you in a sec."
            else:
                eff "Hey, [povname]! Will be with you in a sec."
            show pov neutral at left
            show misc neutral_talk at right
            mis "Oh, hey, [povname]. Fancy seeing you here."
            show pov smirk_talk at left
            show misc neutral at right
            pov "I haven't seen you here before, Miss."
            show pov neutral at left
            show misc neutral_talk at right
            mis "Oh, I come here quite often actually, every weekend."
            mis "This place is my favourite place in town to eat brunch."
    show pov neutral at left
    show misc smirk_talk at right
    mis "Their coffee cakes are criminally good."
    show pov smirk_talk at left
    show misc confused at right
    pov "The abundance of drugs?"
    show pov embarrassed at left
    show misc confused_talk at right
    mis "What? No? What makes you assume that?"
    show pov embarrassed_talk at left
    show misc confused at right
    pov "It's uh- y'know. Caffeine is a drug..."
    show pov embarrassed at left
    show misc smirk_talk at right
    mis "Hmmm, you need to work on your execution."
    show pov neutral_talk at left
    show misc smirk at right
    pov "I win some, I lose some."
    show pov neutral at left
    show misc confused_talk at right
    mis "Are you meeting someone here?"
    show pov embarrassed_talk at left
    show misc confused at right
    pov "No, not particularly. I usually just like to roam around and see what shenanigans I can happen upon."
    show pov neutral at left
    show misc neutral_talk at right
    mis "Fair enough."
    show misc smirk_talk at right
    mis "Have you eaten yet?"
    show pov neutral_talk at left
    show misc neutral at right
    pov "Not yet."
    show pov neutral at left
    show misc neutral_talk at right
    mis "Then join me for brunch? I usually eat alone, which sounds sadder now that I've said it out loud."
    show misc embarrassed_talk at right
    mis "I could use some company, if that's not too awkward for you."
    show pov embarrassed at left
    mis "Just two people grabbing a bite to eat, don't think too much of me as a teacher for today."

    menu:
        "Flirting is on the table?":
            show pov smirk_talk at left
            show misc neutral at right
            pov "So flirting is on the table?"
            show pov smirk at left
            show misc smirk_talk at right
            mis "If you have to ask that, then you probably need to work on your flirting skills."
        "Can I call you by your first name?":
            show pov smirk_talk at left
            show misc neutral at right
            pov "Can I call you by your first name?"
            show pov embarrassed at left
            show misc bored_talk at right
            mis "Still no."
        "I can deal with it.":
            show pov embarrassed_talk at left
            show misc confused at right
            pov "A little awkward but I can deal with it."
            show pov embarrassed at left
            show misc bored_talk at right
            mis "Wonderful, I'm glad I asked."
        # "No thanks": ## Skip the scene
    show pov neutral at left
    show misc neutral_talk at right
    mis "Let's head outside, get some fresh air."

    jump lbl_allaway_at_the_cafe_date
