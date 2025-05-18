## Hazen Main Story Throwaway Conversations Adult Store ##
default adultstore_ajob = 0
default sexaroundtownhazel = 0

## A Job
label lbl_adultstore_day_hazel_ajob:
    show pov neutral_talk at left
    with dissolve
    show haz neutral at right
    call lbl_adultstore_counter_check
    with dissolve
    pov "Hey, Hazel."
    show pov neutral at left
    show haz neutral_talk at right
    haz "Hey, honey. What can I do you for."
    show pov confused at left
    show haz bored_talk at right
    haz "Except that thing that a lot of guys ask for and leave disappointed."
    show pov embarrassed_talk at left
    show haz shocked at right
    pov "Erm, is that 'thing' a job? Because that's what I'm looking for."
    show pov smirk at left
    show haz neutral_talk at right
    haz "Oh, a job."
    show pov embarrassed at left
    show haz embarrassed_talk at right
    haz "Sorry, [povname]. Nothing here for you. We're pretty much covered for hands."
    show pov confused at left
    show haz confused_talk at right
    haz "Are you even legally allowed to work here?"
    show pov confused_talk at left
    show haz confused at right
    pov "Barely."
    show pov embarrassed at left
    show haz confused_talk at right
    haz "Well, either way. We're not hiring. Sorry."
    show pov confused at left
    show haz neutral_talk at right
    haz "Have you tried the comic book store next door?"
    haz "Hitomi may need an extra hand."
    if comicbookstore_ajob == 0:
        show pov neutral_talk at left
        show haz neutral at right
        pov "I have not asked her yet. I'll check, thanks."
    else:
        show pov embarrassed_talk at left
        show haz embarrassed at right
        pov "I did, she actually referred me to you but I guess I still have to keep looking."
    show pov neutral at left
    show haz neutral_talk at right
    haz "Good luck, honey. It's a brutal dog eat dog world out there."

    $ adultstore_ajob = 1

    jump lbl_adultstore_day_setup

## Sex Around Town Hazel
label lbl_adultstore_day_hazel_sexworld:
    if sexaroundtownhazel == 0:
        ## Sprite Start
        show pov neutral at left
        with dissolve
        show hazsw neutral_talk at right
        hide btn adultstore_day_hazelsexworld_idle
        call lbl_adultstore_counter_check
        with dissolve
        haz "Hey, honey. Like what you see?"
        show pov embarrassed at left
        show hazsw bored_talk at right
        haz "And I mean the merchandise, not me."
        show pov neutral at left
        show hazsw neutral_talk at right
        haz "This is not that kind of store."
        show pov embarrassed at left
        show hazsw smirk_talk at right
        haz "I come without charge."
        show pov embarrassed_talk at left
        show hazsw smirk at right
        pov "Hazel! I-uh..."
        pov "That's a nice... outfit you have there."
        show pov neutral_talk at left
        show hazsw neutral at right
        pov "Is that... new?"
        show pov neutral at left
        show hazsw bored_talk at right
        haz "I just haven't worn this in a while. Thought it'd look the cutest on me."
        show pov embarrassed at left
        show hazsw smirk_talk at right
        haz "It's great, right? Really emphasises my girls."
        show pov smirk_talk at left
        show hazsw neutral at right
        pov "I can, with utmost confidence say that I like that better than what you usually wear."
        show pov smirk at left
        show hazsw neutral_talk at right
        haz "Really? That's kinda sweet of you."
        show pov neutral at left
        show hazsw neutral_talk at right
        haz "Not many would think so since this is less revealing."
        show pov embarrassed at left
        show hazsw smirk_talk at right
        haz "Though guys are guys and you can't say no to Secret's Victory's thread-thin g-string."
        show pov neutral at left
        show hazsw neutral_talk at right
        haz "I feel like a Princess wearing this, hahaha!"
        show pov embarrassed at left
        show hazsw smirk_talk at right
        haz "Hashtag - feeling cute, might cum all night."
        show pov neutral at left
        show hazsw smirk at right
        pov "..."
        show pov bored at left
        show hazsw bored_talk at right
        haz "Anyway, I suggest checking out the 'brand-new' aisle. We got some sweet-sweet stuff."

        $ sexaroundtownhazel = 1

    else:
        show pov neutral at left
        with dissolve
        show hazsw neutral_talk at right
        hide btn adultstore_day_hazelsexworld_idle
        call lbl_adultstore_counter_check
        with dissolve
        haz "Ayee, [povname]. Anything I can scan for ya?"
        show pov bored_talk at left
        show hazsw bored at right
        pov "Nothing at the moment."
        show pov shocked at left
        show hazsw smirk_talk at right
        haz "Shame, I'm a little busy doing inventory so maybe we could fuck later?"
        show pov embarrassed_talk at left
        show hazsw smirk at right
        pov "..! S-sure!"

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_bdsmgear:
    show pov embarrassed_talk at left
    show haz neutral at right
    with dissolve
    pov "Hey, do you have a special on like- 5 sets of BDSM gear?"
    show pov embarrassed
    show haz confused_talk
    haz "Erm..."
    show haz sad_talk
    haz "We don't have a special going on but..."
    show haz confused_talk
    haz "Hmm, lemme think what I can do for you."
    show haz confused
    haz "..."
    show pov shocked
    show haz neutral_talk
    haz "I can sell you a box full of used BDSM pieces that you can mix and match?"
    haz "How's about $2000 for them?"
    show pov shocked_talk
    show haz shocked
    pov "$2000!?"
    show pov angry_talk
    show haz confused
    pov "Why is it so expensive."
    show pov bored
    show haz confused_talk
    haz "Well, a set of BDSM gear is already pricey and you're asking for 5 sets."
    show pov bored_talk
    show haz confused
    pov "But they're used?"
    show pov bored
    haz "..."

    menu:
        "Buy it" if inventory.money >= 2000:
            show pov bored_talk
            show haz neutral
            pov "Fine. Here."
            show pov bored
            show haz smirk_talk
            haz "Pleasure doing business."
            haz "May I ask why do you-"
            show pov bored_talk
            show haz embarrassed
            pov "Nope."
            show pov bored
            show haz embarrassed_talk
            haz "Right, sorry. Curiosity got the better of me."

            $ inventory.buy(Items.bdsmgear)

            jump lbl_adultstore_day_setup

        "Nevermind":
            show pov bored_talk
            show haz confused
            pov "Nevermind, I'll look somewhere else."
            show pov bored
            show haz smirk_talk
            haz "This is probably the best deal you're gonna get."

            jump lbl_adultstore_day_setup
