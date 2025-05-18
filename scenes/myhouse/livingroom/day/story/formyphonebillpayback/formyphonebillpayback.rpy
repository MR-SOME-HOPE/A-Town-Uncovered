## For My Phone Bill Payback ##
label lbl_for_my_phone_bill_payback:
    show pov neutral at left
    with dissolve
    show sis neutral_talk at right
    with dissolve
    if winc == 0:
        sis "Hey, [povname]."
    else:
        sis "Hey, bro-bro."
    sis "I got the money I owe you for my phone recharge."
    show pov smirk_talk at left
    show sis smirk at right
    pov "Awesome, I was starting to think that you would go as far as you can without mentioning it again."
    show pov neutral at left
    show sis smirk_talk at right
    sis "It's better if we're both on good standing terms."
    show pov embarrassed at left
    sis "Who knows when there'll be a day when I need much more than $50."
    $ inventory.money += 50
    $ renpy.notify("Current Balance: $[inventory.money]")
    $ formyphonebill_owe = 0

    jump lbl_mylivingroom_day_setup
