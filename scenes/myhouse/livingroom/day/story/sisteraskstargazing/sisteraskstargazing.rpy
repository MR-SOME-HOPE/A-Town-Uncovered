## Sister Ask Stargazing ##
label lbl_sister_ask_stargazing:

    scene bg mylivingroom_day
    with fade
    show pov neutral at left
    with dissolve
    show sis neutral_talk at right
    with dissolve
    sis "Hey, [povname]."
    show sis confused_talk at right
    sis "Are you busy tonight?"
    show pov smirk_talk at left
    show sis neutral at right
    pov "I'm usually spontaneous with my plans so I'm open for anything you have in mind."
    show pov confused at left
    show sis neutral_talk at right
    if winc == 0:
        sis "That's great! I got [missus] to let us borrow her car and figured we could ride around town for a bit and then hit the beach."
    else:
        sis "That's great! I got Mom to let us borrow her car and figured we could ride around town for a bit and then hit the beach."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "Sure... but what brought this up if you don't mind me asking?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "W-Well, I have somethings I need to get off my chest and I would like some extra privacy for it."
    show pov confused_talk at left
    show sis confused at right
    pov "Why are we taking the car though? We could just walk."
    show pov confused at left
    show sis embarrassed_talk at right
    if winc == 0:
        sis "[missus] doesn't like the idea of us walking back home late and I wanted to do things the right way."
    else:
        sis "Mom doesn't like the idea of us walking back home late and I wanted to do things the right way."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "What things?"
    show pov shocked at left
    show sis embarrassed_talk at right
    if winc == 0:
        sis "Remember when we used to go camping with [missus] and [dadname]?"
        show pov smirk at left
        sis "How he always struggled so much putting up the tent that it ended up getting dark and we stayed up watching the stars on the hood of the car while [missus] helped him out?"
    else:
        sis "Remember when we used to go camping with Mom and Dad?"
        show pov smirk at left
        sis "How he always struggled so much putting up the tent that it ended up getting dark and we stayed up watching the stars on the hood of the car while Mom helped him out?"
    show sis neutral_talk at right
    sis "Remember how there was a meteor shower that night and we were blown away by how clear they looked?"
    show pov neutral_talk at left
    show sis smirk at right
    pov "Yeah! Oh my God, how could I forget?! That night was awesome!"
    show pov shocked at left
    show sis smirk_talk at right
    sis "Well, tonight there's supposed to be a meteor shower so I figured we could go have a look like in the old days."
    show pov shocked_talk at left
    show sis smirk at right
    pov "That... That sounds amazing!"
    show pov neutral_talk at left
    show sis embarrassed at right
    pov "Sure, I would love to go!"
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "Great!"
    show sis neutral_talk at right
    #if gtime == 1:
    sis "Meet me outside the house later tonight and we'll get going."
    #else:
    #    sis "Alright, meet me outside and we'll get going right now!"
    show pov neutral_talk at left
    show sis neutral at right
    pov "You bet!"
    #$ sister_path = 36
    #if gtime == 1:
    #    $ gtime = 2
    $ townmap_enabled = 1
    jump lbl_pre_stargazing_heart_to_heart
