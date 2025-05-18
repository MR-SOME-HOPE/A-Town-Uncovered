## Split Up Cover More Ground
label lbl_split_up_cover_more_ground:
    ### CGS
    ## As the team enters the Office Lobby, they see the two receptionists being assaulted as well.
    scene bg officelobby_day #TEMP
    with fade

    show povn shocked_talk at left
    show coln neutral at Position(xpos=1000)
    show jacn confused at Position(xpos=1300)
    show effn neutral at Position(xpos=1500)
    show edwn embarrassed at Position(xpos=1800)
    with dissolve
    pov "Quick. Move, move."
    show povn neutral at left
    show edwn embarrassed_talk at Position(xpos=1800)
    edw "Where do we go?"
    show coln neutral_talk at Position(xpos=1000)
    show edwn confused at Position(xpos=1800)
    col "There’s a map over here."

    ## Shot of the office building map.

    show coln embarrassed at Position(xpos=1000)
    show jacn embarrassed at Position(xpos=1300)
    show effn confused_talk at Position(xpos=1500)
    eff "Hmm, it’s not really helpful. It doesn’t say where the server room is."
    show effn confused at Position(xpos=1500)
    show edwn smirk_talk at Position(xpos=1800)
    edw "It’d be pretty stupid to put something that important on a public map."
    show edwn bored_talk at Position(xpos=1800)
    edw "Not to mention this is a tech company."
    show povn confused_talk at left
    show edwn bored at Position(xpos=1800)
    pov "We’ll have to split up and cover ground."
    pov "Venture off to different floors until we find it."
    show povn confused at left
    show coln smirk at Position(xpos=1000)
    show jacn bored_talk at Position(xpos=1300)
    jac "Oh man, more running."
    show povn confused at left
    show jacn shocked at Position(xpos=1300)
    pov "You tired?"
    show povn embarrassed at left
    show jacn embarrassed_talk at Position(xpos=1300)
    show edwn neutral at Position(xpos=1800)
    jac "A little bit."
    show coln smirk_talk at Position(xpos=1000)
    show jacn embarrassed at Position(xpos=1300)
    show effn smirk at Position(xpos=1500)
    col "Hey, little man. You got this."
    show povn neutral at left
    show coln neutral at Position(xpos=1000)
    show edwn neutral at Position(xpos=1800)
    col "If I can do it, so can you."
    show povn neutral_talk at left
    show jacn confused at Position(xpos=1300)
    show effn shocked at Position(xpos=1500)
    pov "Jacob and Effie, you take the bottom 3rd floors."
    show povn smirk_talk at left
    show coln smirk at Position(xpos=1000)
    show edwn neutral at Position(xpos=1800)
    pov "Cole and Edward, you take the next 3rd."
    show povn shocked_talk at left
    show effn confused at Position(xpos=1500)
    pov "I’ll take the top 3rd."
    show povn shocked at left
    show effn confused_talk at Position(xpos=1500)
    eff "You’re going alone?"
    show povn embarrassed_talk at left
    show effn confused at Position(xpos=1500)
    pov "I gotta."
    show povn embarrassed_talk at left
    show edwn embarrassed at Position(xpos=1800)
    pov "I want everyone else in pairs, it’s dangerous here."
    show povn neutral_talk at left
    show coln neutral at Position(xpos=1000)
    show jacn embarrassed at Position(xpos=1300)
    pov "Have each other’s back."
    show povn smirk_talk at left
    pov "I’ll be fine."
    show povn neutral at left
    show jacn neutral_talk at Position(xpos=1300)
    jac "Don’t die on me, dude."
    show povn smirk at left
    show coln smirk at Position(xpos=1000)
    show jacn smirk_talk at Position(xpos=1300)
    jac "I’ll miss you."
    show povn smirk_talk at left
    show jacn smirk at Position(xpos=1300)
    show effn neutral at Position(xpos=1500)
    show edwn neutral at Position(xpos=1800)
    pov "Thanks, bro."
    pov "I’ll miss me too."
    show povn neutral at left
    pov "Let’s go!"

    ## Everyone heads to different elevators and starts searching for the server room…

    ## SCENE ENDS

    $ main_story = 184

    jump lbl_eloise_at_the_control
