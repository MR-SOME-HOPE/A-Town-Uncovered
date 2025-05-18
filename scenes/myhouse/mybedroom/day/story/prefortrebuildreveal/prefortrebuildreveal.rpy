## Pre Fort Rebuild Reveal ##
label lbl_pre_fort_rebuild_reveal:
    scene bg prefortrebuildreveal_1
    with fade
    $ renpy.pause()

    $ townmap_enabled = 0

    $ sister_path = 33.5

    jump lbl_mybedroom_day_setup
