label lbl_momaftersunset_massage:
    show bg momaftersunset_63
    pov "It'll be my pleasure."
    show bg momaftersunset_massage_1
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_2
    mum "I'm ready, baby."
    show bg momaftersunset_massage_3
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_4
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_5
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_3
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_4
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_5
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_6
    mum "Mmm... yeah, like that, baby."
    show bg momaftersunset_massage_7
    mum "Do they feel good?"
    show bg momaftersunset_massage_5
    pov "They feel amazing..."
    show bg momaftersunset_massage_6
    mum "I'll let you play with them as much as you want..."
    show bg momaftersunset_massage_7
    mum "In exchange, we do this every single night."
    show bg momaftersunset_massage_8
    if winc == 0:
        mum "Remember, our time starts when the sun sets and the rest of the house sleeps."
    else:
        mum "Remember, our time starts when the sun sets and the rest of the family sleeps."

    jump lbl_momaftersunset_massage_1

label lbl_momaftersunset_massage_1:
    $ count = 1
    $ num = 4
    while count <= num:
        $ count += 1
        show bg momaftersunset_massage_3
        $ renpy.pause(0.333,hard=True)
        show bg momaftersunset_massage_4
        $ renpy.pause(0.333,hard=True)
        show bg momaftersunset_massage_5
        $ renpy.pause(0.333,hard=True)

    jump lbl_momaftersunset_massage_2

label lbl_momaftersunset_massage_2:
    $ count = 1
    $ num = 4
    while count <= num:
        $ count += 1
        show bg momaftersunset_massage_9
        $ renpy.pause(0.266,hard=True)
        show bg momaftersunset_massage_10
        $ renpy.pause(0.266,hard=True)
        show bg momaftersunset_massage_11
        $ renpy.pause(0.266,hard=True)

    jump lbl_momaftersunset_massage_3

label lbl_momaftersunset_massage_3:
    $ count = 1
    $ num = 8
    while count <= num:
        $ count += 1
        show bg momaftersunset_massage_12
        $ renpy.pause(0.2,hard=True)
        show bg momaftersunset_massage_13
        $ renpy.pause(0.2,hard=True)
        show bg momaftersunset_massage_14
        $ renpy.pause(0.2,hard=True)

    jump lbl_momaftersunset_massage_4

label lbl_momaftersunset_massage_4:
    show bg momaftersunset_massage_15
    $ renpy.pause(0.333,hard=True)
    show bg momaftersunset_massage_16
    $ renpy.pause(0.333,hard=True)
    show bg momaftersunset_massage_17
    $ renpy.pause(0.333,hard=True)

    scene black
    $ renpy.pause()
    if winc == 0:
        "You massaged [missus]'s boobs for the remainder of the night."
    else:
        "You massaged mom's boobs for the remainder of the night."
    if mompastsunset_attend == 0:
        "She didn't return the favor anytime afterwards but you can tell that just from the sounds of her deep, breathy panting..."
        if winc == 0:
            "She is very thankful to have you as her [povmumrole]."
        else:
            "She is very thankful to have you as her son."
    else:
        "Again, she didn't return the favor afterwards but maybe tomorrow night could be the night you'll get lucky."
        "All you have to do is treat her like a queen and obey her every command."
        "One day..."
    if mum_points <= 9:
        $ mum_points += 1
    else:
        $ mum_points = 10
    if skill_str >= 1:
        $ skill_str -= 1
    else:
        $ skill_str = 0
    if winc == 0:
        $ renpy.notify("You used a Strength Point\nYour relationship with [missus] has increased")
    else:
        $ renpy.notify("You used a Strength Point\nYour relationship with Mom has increased")
    $ renpy.pause(3,hard=True)
    $ mompastsunset_attend = 4

    jump lbl_mom_past_sunset_end