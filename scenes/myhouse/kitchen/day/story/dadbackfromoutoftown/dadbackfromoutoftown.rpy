## Dad Back from Out of Town
label lbl_dad_back_from_out_of_town:
    scene bg myhallway_day
    with fade
    show pov shocked_talk at left
    with dissolve
    show dad bored at right
    with dissolve
    if winc == 0:
        pov "Oh- [dadname], you're back."
    else:
        pov "Oh- dad, you're back."
    show pov confused at left
    show dad bored_talk at right
    dad "Yes, I'm back."
    dad "Arrived this morning before anyone was awake."
    show pov confused at left
    show dad bored at right
    pov "..."
    show pov confused_talk at left
    pov "Well, alright then. Welcome back, I guess."

    $ mum_path = 25.1

    jump lbl_myhallway_day
