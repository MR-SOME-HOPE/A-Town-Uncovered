## Dateish Night
label lbl_dateish_night:
    ## SPRITEWORK

    pov "{i}Well, here goes nothing...{/i}"
    "{i}Knock, knock, knock{/i}"

    #-Effie appears into the scene-
    show pov embarrassed at left
    show eff neutral_talk at right
    eff "Hey, you actually showed up."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "You didn't think I was going to?"
    show pov embarrassed at left
    show eff smirk_talk at right
    eff "Well, with the way this whole thing was set up on us out of nowhere by [sister], I wouldn't have blamed you if you did."
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "Well, I guess I'm just used to her type of hijinks."
    show pov neutral_talk at left
    show eff confused at right
    pov "But that aside, you know me better than to think I would just bail on you like that out of nowhere."
    show pov smirk_talk at left
    pov "I'm not the type to stand someone up in general."
    show pov confused at left
    show eff neutral_talk at right
    eff "I know, I know."
    show eff smirk_talk at right
    eff "Sorry, this whole thing just has me a bit out of my groove."
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "If you are not comfortable we could always call it a night here and pretend nothing ever happened too."
    show pov embarrassed at left
    show eff bored_talk at right
    eff "That's definitely not something I want but I appreciate the sentiment."
    show pov embarrassed at left
    show eff neutral_talk at right
    eff "Anyway, how about if we head inside then?"
    show pov smirk_talk at left
    show eff confused at right
    pov "Is your dad really gone? I don't wanna have to practically jump out the window if he finds out I'm here."
    show pov smirk at left
    show eff neutral at right
    eff "Yeah, he's out for the whole night and shouldn't be coming back home til tomorrow in the afternoon."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "How are you so sure?"
    show pov embarrassed at left
    show eff neutral_talk at right
    eff "He does it from time to time for work."
    show eff smirk_talk at right
    eff "Usually it's the time I can invite people over without getting caught so we should be good!"
    show pov neutral_talk at left
    show eff smirk at right
    pov "Alright, sounds good then."
    show pov smirk_talk at left
    show eff shocked at right
    pov "Are we going to the living room then?"
    show pov smirk at left
    show eff embarrassed_talk at right
    eff "Nope, straight to my room."
    show pov embarrassed at left
    show eff smirk_talk at right
    eff "Can't risk leaving evidence on the actual living room. He is like a bloodhound regarding that whole place and just knows when things are out of order."
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "You can't be serious."
    show pov embarrassed at left
    show eff bored_talk at right
    eff "I really wish I was…"
    show pov confused at left
    show eff smirk_talk at right
    eff "It's probably because he spends most of his time there when he is home but if even one of the cushions is out of place on the couch he gets super suspicious."
    show pov embarrassed at left
    show eff neutral_talk at right
    eff "Anyway, it's not like you haven't been in my room before or something."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "Fair enough."

    #-Scene fades to Black and transition's to Effie's room-
    scene black
    with fade
    $ renpy.pause()
    "Into Effie's room..."

    jump lbl_dateish_night_room
