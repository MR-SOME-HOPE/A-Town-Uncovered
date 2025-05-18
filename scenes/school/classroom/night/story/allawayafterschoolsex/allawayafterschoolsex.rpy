## Allaway After School Sex ##
label lbl_allaway_after_school_sex:
    default allaway_after_school_sex_stairs_counter = 0
    default allaway_after_school_sex_desk_counter = 0
    default allaway_after_school_sex_cowgirl_counter = 0

    scene bg classroom_day
    show pov smirk_talk at left
    with dissolve
    show mis confused at right
    with dissolve
    pov "Wanna have some fun tonight?"
    show pov shocked at left
    show mis sad_talk at right
    mis "[povname]! Please-!"
    show pov smirk at left
    show mis embarrassed_talk at right
    mis "Not too loud..."
    show mis smirk_talk at right
    mis "Even though deep down I'd want you to- y'know..."
    show mis sad_talk at right
    mis "Right now."
    show pov embarrassed at left
    mis "But we can't..."
    show pov embarrassed_talk at left
    show mis shocked at right
    pov "Oh- maybe next ti-"
    show pov shocked at left
    show mis embarrassed_talk at right
    mis "No, I meant not now. Later, definitely."
    show pov smirk at left
    show mis smirk at right
    mis "..."
    show mis smirk_talk at right
    mis "After... class... tutoring?"
    show pov smirk_talk at left
    show mis embarrassed at right
    pov "I can't wait!"
    show pov neutral_talk at left
    show mis smirk at right
    pov "To... get my grades up. Hehehe~"

    scene black
    with fade
    "Later tonight..."
    "After some..."
    "'Tutoring'..."

    menu:
        "Start at the Stairs":
            jump lbl_allaway_after_school_sex_stairs
        "Start on the Desk":
            jump lbl_allaway_after_school_sex_desk
        "Start on the Floor":
            jump lbl_allaway_after_school_sex_cowgirl

####################
## Scene Choice
label lbl_allaway_after_school_sex_scenechoice_stairs:

    menu:
        "Go to the Desk":
            jump lbl_allaway_after_school_sex_desk
        "Get on the Floor":
            jump lbl_allaway_after_school_sex_cowgirl

label lbl_allaway_after_school_sex_scenechoice_desk:

    menu:
        "Go to the Stairs":
            jump lbl_allaway_after_school_sex_stairs
        "Get on the Floor":
            jump lbl_allaway_after_school_sex_cowgirl

label lbl_allaway_after_school_sex_scenechoice_cowgirl:

    menu:
        "Go to the Stairs":
            jump lbl_allaway_after_school_sex_stairs
        "Go to the Desk":
            jump lbl_allaway_after_school_sex_desk

####################
## End

label lbl_allaway_after_school_sex_end:

    scene black
    with fade
    $ renpy.pause()
    "After cleaning up..."

    scene bg classroom_night
    with fade
    show povn smirk_talk at left
    with dissolve
    show misn neutral at right
    with dissolve
    pov "Thanks for tonight, Miss Allaway."
    pov "It was fun."
    show povn neutral at left
    show misn smirk_talk at right
    mis "I had fun as well."
    show povn confused_talk at left
    show misn smirk at right
    pov "You got a key to get us out of here, right?"
    show povn smirk at left
    show misn embarrassed_talk at right
    mis "Yup, made sure to keep one on my person ever since that night."
    mis "Well.. hehehe~"
    mis "Not {i}now{/i} now."
    show povn smirk_talk at left
    show misn smirk at right
    pov "I can feel around inside you to make sure it didn't accidentally get lost."
    show povn smirk at left
    show misn bored_talk at right
    mis "Shush before you get me wet, I have coursework and assignments to mark tonight."
    show povn neutral at left
    show misn embarrassed_talk at right
    mis "Let's get changed and outta here before anyone at the gym catches us."

    scene bg schoolyard_night
    with fade
    $ renpy.pause()
    $ gtime = 2

    jump lbl_schoolyard_night_setup
