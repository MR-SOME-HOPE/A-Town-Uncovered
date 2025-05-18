## Throwaway Chat with Effie ##
label lbl_effie_house_hallway_night_frontdoor_presex:
    show pov neutral at left
    with dissolve
    show eff bored_talk at right
    with dissolve
    eff "Where are you going?"
    show pov neutral_talk at left
    show eff bored at right
    pov "Oh, nothing, I was just making sure I know where the exit is."

    jump lbl_effiehousehallway_night_setup

label lbl_effie_house_hallway_night_garage_presex:
    show pov bored at left
    with dissolve
    show eff bored_talk at right
    with dissolve
    eff "Um, don't even try to enter there."
    show pov confused_talk at left
    show eff bored at right
    pov "Oh, is that your dad's room?"
    show pov bored at left
    show eff bored_talk at right
    eff "No, that's the garage but that's also his studio where he 'works'."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Gotcha."

    jump lbl_effiehousehallway_night_setup
