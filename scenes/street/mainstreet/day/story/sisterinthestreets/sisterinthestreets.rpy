## Sister in the Streets ##
label lbl_sister_in_the_streets:

    scene bg sisterinthestreets_1
    with fade
    $ renpy.pause()
    pov "[sister]-?!"
    show bg sisterinthestreets_2
    pov "What are you doing her-"
    show bg sisterinthestreets_3
    with hpunch
    $ renpy.pause()
    $ townmap_enabled = 0
    $ sister_path = 17.5

    jump lbl_street_day_setup
