## Confiscated Flyers
label lbl_confiscated_flyers:
    ## Lashley Enters the classroom
    ## SPRITES

    show pri bored_talk at right
    with dissolve
    pri "You guys are supposed to be quiet in detention, not having a club house party."
    show pri shocked_talk
    pri "And what is this I see?"
    show pri angry at right
    pri "{i}*Groan*{/i}"
    pri "There’s not a lot of things I despise in this world but this."
    show pri angry_talk at right
    pri "These fake religious groups are trying to recruit young men and women into their evil cults."
    show pov shocked at left
    show pri confused_talk at right
    with dissolve
    pri "I want you taking NO part in this."
    show pri angry_talk at right
    pri "Give that to me."
    show pov shocked_talk at left
    show pri angry at right
    pov "Bu-"
    show pov confused at left
    show pri angry at right
    pri "{i}*Snatch*{/i}"
    show pri angry_talk at right
    pri "Thank you, [povname]."
    show pov bored at left
    show pri bored_talk at right
    pri "You all have no business dealing with this, Master Buukakki."
    pri "The only one you need to follow is our Lord."
    show pri confused_talk at right
    pri "Follow him, and he’ll lead you into salvation."
    show pri bored_talk at right
    pri "Do not be lead into temptation and let the Lord deliver you from the evil ones."
    show pov  at left
    show pri confused_talk at right
    pri "Bless your hearts, sit down, and do your time."
    pri "This is detention, everyone. Please."
    show pri bored at right
    pri "{i}*Sigh*{/i}"
    show pri confused_talk at right
    pri "I hate having to use my authoritative voice."
    show pov sad at left
    show pri shocked_talk at right
    pri "Coach."
    show pov sad_talk at left
    show pri bored at right
    coa "I’m sorry, long day, won’t happen again."
    show pov bored at left
    show pri bored_talk at right
    pri "Mhmm-"

    ## Lashley leaves.

    show pov bored_talk at left
    hide pri
    show edw neutral at Position(xpos=1200)
    show col shocked at Position(xpos=1700)
    with dissolve
    pov "Well- fuck."
    show pov bored at left
    show col embarrassed at Position(xpos=1700)
    coa "Language!"
    show col smirk_talk at Position(xpos=1700)
    col "Oh, who are you kidding, coach."
    show pov embarrassed at left
    show col smirk at Position(xpos=1700)
    coa "I know."
    show pov confused at left
    show edw embarrassed_talk at Position(xpos=1200)
    edw "I guess we’ll just… I don’t know."
    show pov confused_talk at left
    show edw confused at Position(xpos=1200)
    pov "If Xina’s behind the robbery then we can assume the hideout is safe, or as safe as anywhere else in town would be for us."
    show pov confused at left
    show edw embarrassed_talk at Position(xpos=1200)
    edw "I’ll give it a sus myself but you’re probably right."
    show pov confused_talk at left
    show edw embarrassed at Position(xpos=1200)
    pov "We need those flyers back-"
    show pov confused at left
    show col embarrassed_talk at Position(xpos=1700)
    col "We’ll have to come up with a plan quickly."
    show pov shocked at left
    show edw shocked at Position(xpos=1200)
    show col smirk at Position(xpos=1700)
    with hpunch
    coa "QUIET!"
    coa "Since I can’t risk catching up on Zzz’s. The least everyone can do is to shut up!"
    show pov embarrassed at left
    show edw embarrassed at Position(xpos=1200)
    show col neutral at Position(xpos=1700)
    coa "…"
    coa "Thank you."

    $ main_story = 150.5

    scene black
    with fade
    $ renpy.pause()
    "After having spent your time in detention..."
    scene bg schoolyard_day
    with fade


    jump lbl_schoolyard_day_setup
