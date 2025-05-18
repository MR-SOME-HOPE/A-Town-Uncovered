## The Sexworld Side Effect Setup
label lbl_the_sexworld_side_effect_setup:
    show pov confused_talk at left
    show jac neutral at right
    with dissolve
    pov "Hey, we ready to head to Davendithas' family?"
    show pov neutral
    show jac neutral_talk
    jac "Yeah, I'll text Edward to meet up, he's been ready since he was born."
    show pov smirk_talk
    show jac neutral
    pov "Love to hear it."

    scene black
    with fade
    $ renpy.pause()
    "After meeting up with Edward and heading to Davendithas' place."

    jump lbl_the_sexworld_side_effect
