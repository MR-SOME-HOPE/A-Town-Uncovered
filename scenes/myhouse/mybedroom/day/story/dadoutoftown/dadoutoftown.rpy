## Dad Out of Town ##
label lbl_dad_out_of_town:
    if winc == 0:
        jump lbl_dad_out_of_town_winc0

    scene bg mybedroom_day
    with hpunch
    dad "[povname]!"

    menu:
        "Yes, Dad?":
            show pov shocked_talk at left
            with dissolve
            show dad neutral at right
            with dissolve
            pov "Yes, Dad? What is it?"
            show pov bored at left
            show dad neutral_talk at right
            dad "I'm going to be out of town for a few days."
            show pov neutral at left
            dad "Not sure how long but you're the man of the house until I'm back."
            dad "You understand?"
            show pov neutral_talk at left
            show dad neutral at right
            pov "Yes, Dad. I understand."
            show pov bored at left
            show dad neutral_talk at right
            dad "Good. Behave yourself."
        "What?!":
            show pov shocked_talk at left
            with dissolve
            show dad angry at right
            with dissolve
            pov "What?!"
            show pov bored at left
            show dad neutral_talk at right
            dad "Don't be rude. I'm letting you know that I'll be out of town for a few days."
            dad "Not sure how long but you're the man of the house until I'm back."
            show pov angry at left
            dad "Don't be a pussy, you got it?"
            show pov shocked at left
            dad "If someone comes in and wants to rape your mother or [sister], you either fight or get your ass fucked before they do."
            show dad angry_talk at right
            dad "Understood?"
            show pov sad_talk at left
            show dad angry at right
            pov "What the hell, Dad?! Fine, fine. Jesus."
            show pov angry at left
            show dad angry_talk at right
            dad "Time for you to man up."
        "Get out of my room!":
            show pov angry_talk at left
            with dissolve
            show dad angry at right
            with dissolve
            pov "Get out of my room, Dad!"
            show pov angry at left
            show dad angry_talk at right
            dad "Shut the fuck up for a second, you ungrateful piece of-"
            show pov confused at left
            dad "Look, I'm going to be out of town for a few days."
            show dad neutral_talk at right
            dad "Not sure how long but you're the man of the house until I'm back."
            show pov bored at left
            dad "And I use the term ‘man' lightly."
            dad "Basically, if something goes wrong, I'm looking at you for answers."
            show dad angry_talk at right
            dad "Don't be a fuck."
            dad "Understand?"
            show pov angry_talk at left
            show dad angry at right
            pov "Yeah, whatever."
            show pov angry at left
            show dad angry_talk at right
            dad "Fuckin', why couldn't I have two boys instead?"
    $ mum_path = 20

    jump lbl_mybedroom_day_setup

### NO WINC ###
label lbl_dad_out_of_town_winc0:

    scene bg mybedroom_day
    with hpunch
    dad "[povname]!"

    menu:
        "Yes, [dadname]?":
            show pov shocked_talk at left
            with dissolve
            show dad neutral at right
            with dissolve
            pov "Yes, [dadname]? What is it?"
            show pov bored at left
            show dad neutral_talk at right
            dad "I'm going to be out of town for a few days."
            show pov neutral at left
            dad "Not sure how long but you're the man of the house until I'm back."
            dad "You understand?"
            show pov neutral_talk at left
            show dad neutral at right
            pov "Yes, [dadname]. I understand."
            show pov bored at left
            show dad neutral_talk at right
            dad "Good. Behave yourself."
        "What?!":
            show pov shocked_talk at left
            with dissolve
            show dad angry at right
            with dissolve
            pov "What?!"
            show pov bored at left
            show dad neutral_talk at right
            dad "Don't be rude. I'm letting you know that I'll be out of town for a few days."
            dad "Not sure how long but you're the man of the house until I'm back."
            show pov angry at left
            dad "Don't be a pussy, you got it?"
            show pov shocked at left
            dad "If someone comes in and wants to rape your [mumrole] or your [sisrole], you either fight or get your ass fucked before they do."
            show dad angry_talk at right
            dad "Understood?"
            show pov sad_talk at left
            show dad angry at right
            pov "What the hell, [dadname]?! Fine, fine. Jesus."
            show pov angry at left
            show dad angry_talk at right
            dad "Time for you to man up."
        "Get out of my room!":
            show pov angry_talk at left
            with dissolve
            show dad angry at right
            with dissolve
            pov "Get out of my room, [dadname]!"
            show pov angry at left
            show dad angry_talk at right
            dad "Shut the fuck up for a second, you ungrateful piece of-"
            show pov confused at left
            dad "Look, I'm going to be out of town for a few days."
            show dad neutral_talk at right
            dad "Not sure how long but you're the man of the house until I'm back."
            show pov bored at left
            dad "And I use the term ‘man' lightly."
            dad "Basically, if something goes wrong, I'm looking at you for answers."
            show dad angry_talk at right
            dad "Don't be a fuck."
            dad "Understand?"
            show pov angry_talk at left
            show dad angry at right
            pov "Yeah, whatever."
            show pov angry at left
            show dad angry_talk at right
            dad "Fuckin', why couldn't I have two boys instead?"
    $ mum_path = 20

    jump lbl_mybedroom_day_setup
