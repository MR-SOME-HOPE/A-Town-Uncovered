## A Health Scare
label lbl_a_health_scare:
    ## On a particularly hot day

    show vio confused_talk at right
    with dissolve
    vio "*Huff*"
    show vio bored_talk at right
    vio "Where is, [povname]."
    vio "He should be here by now."
    show povn neutral_talk at left
    with dissolve
    show vio confused at right
    pov "Present!"
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "Sorry it took a while to get here, it’s pretty hot today."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "It’s pretty damn hot, but that’s no excuse."
    show povn neutral at left
    vio "You have to be more diligent and punctual when it comes to being a lifeguard."
    show vio bored_talk at right
    vio "Even as a trainee."
    show povn bored at left
    show vio shocked_talk at right
    vio "*Huff*"
    show povn confused at left
    show vio shocked at right
    pov "You alright, Violette?"
    show vio confused_talk at right
    vio "Yeah, yeah…"
    show vio embarrassed_talk at right
    vio "Just make sure you’re drinking plenty of water."
    show povn embarrassed_talk at left
    show vio embarrassed at right
    pov "Gotcha."
    show povn embarrassed at left
    show vio shocked_talk at right
    vio "Now hurry up and get changed, I’ll meet you-"
    show povn confused at left
    show vio confused_talk at right
    vio "*Huff*"
    show vio shocked_talk at right
    vio "I’ll meet you by the-"
    show vio embarrassed_talk at right
    vio "By the shore…"
    show povn smirk at left
    show vio shocked_talk at right
    vio "For water training…"
    show vio bored_talk at right
    vio "*Huff huff*"
    show povn confused at left
    vio "That’ll be best for a day like today…"

    ## Vio faints with a thud

    show povn shocked_talk at left
    hide vio
    with vpunch
    pov "Violette?!"
    show povn confused_talk at left
    pov "Oh my God-"
    show povn shocked_talk at Position(xpos=800)
    pov "Are you okay?"
    show povn confused_talk flip at Position(xpos=1300)
    pov "HEY! SOMEBODY HELP!"
    pov "SHE JUST FAINTED!"
    show povn sad_talk at Position(xpos=900)
    pov "HELP!"

    ## SCENE END
    $ violette_path = 7

    jump lbl_lack_of_water
