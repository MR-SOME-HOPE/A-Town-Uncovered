## Post Sister's Nightmare ##
label lbl_post_sisters_nightmare:

    scene bg postsistersnightmare_1
    with fade
    $ renpy.pause()
    pov "Mm.."
    show bg postsistersnightmare_2
    pov "Hmm..?"
    show bg postsistersnightmare_3
    pov "..."
    show bg postsistersnightmare_4
    pov "[sister]?"
    if winc == 0:
        show bg postsistersnightmare_6
        with dissolve
    else:
        show bg postsistersnightmare_5
        with dissolve
    $ renpy.pause()
    pov "Heh, iconic."
    $ sister_path = 35
    if date < 14 and month == 5:
        pass
    else:
        $ townmap_enabled = 0

    jump lbl_mybedroom_day_setup
