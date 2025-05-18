## Cheer Mom Up Payback ##
label lbl_cheer_mom_up_payback:
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Hey, [povname]. Here's the money I owe you for the Webflicks box thingy."
    show pov smirk_talk at left
    show mum neutral at right
    pov "The Smart TV?"
    show pov neutral at left
    show mum neutral_talk at right
    mum "Yup, that's the one."
    show mum confused_talk at right
    mum "What was it again?"
    if cheermomup_owe == 1:
        mum "$100, right?"
    else:
        mum "$200, right?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "I believe so."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Here you go."
    if cheermomup_owe == 1:
        $ inventory.money += 200
        $ renpy.notify("Current Balance: $[inventory.money]")
    else:
        $ inventory.money += 300
        $ renpy.notify("Current Balance: $[inventory.money]")
    $ cheermomup_owe = 0

    jump lbl_mykitchen_day_setup
