## Don't Blame Yourself
label lbl_dont_blame_yourself:
    scene bg forestsafehouseinside_night
    with fade
    show pov angry at left
    show jac angry_talk at Position(xpos=1200)
    show edw embarrassed at Position(xpos=1700)
    with dissolve
    jac "Knock it off, [povname]!"
    show jac embarrassed at Position(xpos=1200)
    jac "This isn’t anyone’s fault, especially not yours."
    show pov confused at left
    show jac bored_talk at Position(xpos=1200)
    jac "You going alone right now is exactly what VI wants you to do."
    show jac bored at Position(xpos=1200)
    show edw embarrassed_talk at Position(xpos=1700)
    edw "Unprepared and alone without a clue on what to do next?"
    show edw smirk_talk at Position(xpos=1700)
    edw "Sounds like a recipe for a successful bait-and-catch."
    show pov angry_talk at left
    show edw smirk at Position(xpos=1700)
    pov "Effie would run after me."
    show pov confused_talk at left
    show jac embarrassed at Position(xpos=1200)
    pov "..."
    show pov bored_talk at left
    show edw embarrassed at Position(xpos=1700)
    pov "She wouldn’t hesitate to take action and go after what she wants."
    show pov confused_talk at left
    show jac neutral at Position(xpos=1200)
    pov "That’s the person I know she is."
    show pov confused at left
    show jac neutral_talk at Position(xpos=1200)
    jac "That’s true, but she isn’t stupid either."
    show jac smirk_talk at Position(xpos=1200)
    show edw neutral at Position(xpos=1700)
    jac "She’s one of the smartest people I know and I’ll tell you that she knows anything is better than running off too hastily."
    show pov smirk_talk at left
    show jac confused at Position(xpos=1200)
    pov "The more time we sit here arguing about whether to chase after her or not, the less time we have before she becomes in grave danger."
    show pov embarrassed_talk at left
    show edw bored at Position(xpos=1700)
    pov "It’s me that they want."
    show jac embarrassed at Position(xpos=1200)
    pov "Effie shouldn’t have to put up with any torture they’re gonna do to her."
    show pov smirk_talk at left
    show edw sad at Position(xpos=1700)
    pov "Whether I go tonight or next week, they WILL get me."
    show pov embarrassed_talk at left
    show jac sad at Position(xpos=1200)
    pov "So I might as well do it tonight."
    show pov confused at left
    show edw confused_talk at Position(xpos=1700)
    edw "[povname]!"
    show pov shocked at left
    show jac confused at Position(xpos=1200)
    show edw angry_talk at Position(xpos=1700)
    edw "No."
    edw "That’s not the right mindset to have right now."
    show pov smirk at left
    show jac embarrassed at Position(xpos=1200)
    show edw smirk_talk at Position(xpos=1700)
    edw "We need to play smart, not fast. This is a chess match, not a race."
    show pov smirk_talk at left
    show jac smirk at Position(xpos=1200)
    show edw shocked at Position(xpos=1700)
    pov "Chess matches have timers."
    show pov neutral_talk at left
    show edw neutral at Position(xpos=1700)
    pov "It’s on our time now and we’re running out of it."

    #-POV dashes out towards the park-
    hide pov
    with dissolve
    show jac smirk_talk at Position(xpos=1200)
    show edw embarrassed at Position(xpos=1700)
    jac "Yo? Did he just bolt out the door?!"
    show jac shocked at Position(xpos=1200)
    show edw smirk_talk at Position(xpos=1700)
    edw "Go after him!"
    show jac shocked_talk at Position(xpos=1200)
    show edw neutral at Position(xpos=1700)
    jac "Right! Fuck-"

    $ main_story = 124

    jump lbl_dont_be_too_hasty
