## The Text ##
label lbl_the_text:
    default thetext_reject = 0

    scene bg thetext_1
    with fade
    pov "{i}Hmm, I wonder what she wants. Maybe some outdoor fun, I suppose?{/i}"

    menu:
        "Not tonight.":
            scene bg thetext_3
            $ renpy.pause ()
            $ thetext_reject = 1

            jump lbl_mybedroom_night_setup
        "Sure.":
            scene bg thetext_2
            $ renpy.pause ()
            $ renpy.notify("New Objective: Meet Effie at the Park")
            $ main_story = 23

            jump lbl_mybedroom_night_setup
        "Busy all week.":
            scene bg thetext_4
            $ renpy.pause ()
            $ thetext_reject = 2

            jump lbl_mybedroom_night_setup
