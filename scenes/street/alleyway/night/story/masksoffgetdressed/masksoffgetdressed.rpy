## Masks Off Get Dressed
label lbl_masks_off_get_dressed:
    ## CG
    ## As passerbyers are walking past yall, you quickly get dressed
    scene bg masksoffgetdressed_1_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg masksoffgetdressed_1_2
    with dissolve

    "Passerby #1" "Did those guys have an orgy?"

    ## CG of all of them getting dressed
    show bg masksoffgetdressed_2

    "Passerby #2" "Oh my god, that’s such a huge cock."

    "Passerby #3" "In an alleyway? Disgusting."

    "Passerby #4" "Ughh, the drugged up homeless are at it again."

    col "We need to get to the hideout, they could be right on our tail."

    edw "Quick, let’s run far far away from here."
    edw "There’s no knowing who around us is a spy."

    jac "I’d call you paranoid but what will that make me."
    jac "Let’s get the fuck outta here."

    ## SCENE END straight to the next one

    $ main_story = 163
    $ gtime = 3

    jump lbl_theorizing_the_cult
