## Second Night Camping

label lbl_second_night_camping_hscene_revisit:
    scene img_secondnightcamping_1
    with fade
    $ renpy.pause()
    show img_secondnightcamping_2
    $ renpy.pause()
    show img_secondnightcamping_3
    $ renpy.pause()
    show white
    with dissolve
    $ renpy.pause(2,hard=True)
    show bg secondnightcamping_cum
    with dissolve
    $ renpy.pause()
    
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

image img_secondnightcamping_1:
    "bg secondnightcamping_1"
    pause 0.3
    "bg secondnightcamping_2"
    pause 0.1
    "bg secondnightcamping_3"
    pause 0.1
    "bg secondnightcamping_4"
    pause 0.2
    "bg secondnightcamping_5"
    pause 0.2
    repeat

image img_secondnightcamping_2:
    "bg secondnightcamping_1"
    pause 0.3
    "bg secondnightcamping_3"
    pause 0.1
    "bg secondnightcamping_4"
    pause 0.2
    "bg secondnightcamping_5"
    pause 0.2
    repeat

image img_secondnightcamping_3:
    "bg secondnightcamping_1"
    pause 0.2
    "bg secondnightcamping_4"
    pause 0.1
    "bg secondnightcamping_5"
    pause 0.2
    repeat