## Post Ceremonial Orgy
label lbl_post_ceremonial_orgy:
    scene black
    with fade
    $ renpy.pause()
    "A few hours later into the night..."

    ## CG SCENE
    scene bg postceremonialorgy_1
    with fade
    $ renpy.pause()
    # Everyone is tuckered out, cockwarming and just laying about, some slowly
    # still going at it but for the most part the energy has died down.

    # Xina is on stage and giving a short concluding speech.
    show bg postceremonialorgy_2
    xin "I hope everyone still around has had fun tonight and we wish you all another happy Mingle-Mingle Festival."
    xin "Remember to hydrate yourself, take your time, and get home safe."
    xin "Thank you."

    ## SPRITEWORK (povsa & effsa)
    scene bg park_night
    show pov embarrassed_talk at left
    show eff confused at right
    with dissolve
    pov "I think this is our queue to get out of here."
    show pov embarrassed at left
    show eff confused_talk at right
    eff "I- is it safe to do so?"
    show pov shocked_talk at left
    show eff confused at right
    pov "If what they say is true, we’re free to leave anytime we want, including to the other world."
    show pov smirk_talk at left
    show eff bored at right
    pov "It’s best we sneak out anyway, just in case."
    show pov smirk at left
    show eff bored_talk at right
    eff "Alright, let’s hurry."
    eff "…"
    show pov confused at left
    show eff smirk_talk at right
    eff "Tonight was fun though, wasn’t it?"
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "… I can’t deny that."
    show pov neutral at left
    show eff smirk_talk at right
    eff "Hehehehe~"

    ## CG
    # You both enter the lake and teleport to the other dimension.
    scene bg postceremonialorgy_3
    with fade
    $ renpy.pause(1.5,hard=True)
    show bg postceremonialorgy_4
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg postceremonialorgy_5
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg postceremonialorgy_6
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg postceremonialorgy_7
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg postceremonialorgy_8
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg postceremonialorgy_3
    with dissolve
    $ renpy.pause(3,hard=True)

    scene black
    with fade
    $ renpy.pause()
    "Back in your world..."

    $ main_story = 139
    $ insexworld = 0

    jump lbl_park_party_mirroring
