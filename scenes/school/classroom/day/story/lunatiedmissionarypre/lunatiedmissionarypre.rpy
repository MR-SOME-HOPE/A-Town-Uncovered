## Luna Tied Missionary Pre
label lbl_luna_tied_missionary_pre:
    #"Developer Note: This is a temporary Patron-voted h-scene that will be grounded and properly implemented into the game at a later date."
    #scene bg classroom_day
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_luna_idle2
    show lun neutral at right
    with dissolve
    pov "Hey, Luna. Doing anything tonight?"
    show pov confused at left
    show lun neutral_talk at right
    lun "I was just going to spend some time with my darlings."
    show pov confused_talk at left
    show lun neutral at right
    pov "Your darlings?"
    show pov shocked at left
    show lun neutral_talk at right
    lun "Yeah, the spirits who inhabit my soft toys."
    show pov embarrassed_talk at left
    show lun confused at right
    pov "Riiight..."
    show pov embarrassed at left
    lun "..."
    show pov confused at left
    show lun smirk_talk at right
    lun "Wanna meet them?"
    show pov confused_talk at left
    show lun smirk at right
    pov "Like, now?"
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "They only come out at night."
    show pov embarrassed_talk at left
    show lun smirk at right
    pov "Uh- sure."
    show pov embarrassed at left
    show lun smirk_talk at right
    lun "Great, meet me after class, and we'll head to my place."

    $ gtime = 2
    scene black
    with fade
    $ renpy.pause()
    "Later that night in Luna's bedroom..."
    $ renpy.pause()

    stop music
    stop ambience

    jump lbl_luna_tied_missionary
