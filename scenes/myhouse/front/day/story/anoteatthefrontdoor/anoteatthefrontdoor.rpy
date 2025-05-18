## A Note At The Front Door
label lbl_a_note_at_the_front_door:
    ## CG
    ## When MC arrives home, he sees a note at the front door with a polaroid of the group from a distance.

    scene bg anoteatthefrontdoor_1
    with fade
    $ renpy.pause()

    ## “We’re still here.” is what the note says.

    pov "..."
    pov "We know, Xina. We’re very aware."
    pov "Fucking stalker."

    $ main_story = 157

    scene bg myhousefront_day
    with fade

    jump lbl_myhousefront_day_setup
