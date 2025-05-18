## Beach Sparks After Dark BJ
label lbl_beach_sparks_after_dark_bj_revisit:
    scene bg beachsparksafterdarkbj_1
    with fade

label lbl_beach_sparks_after_dark_bj_revisit_1:
    scene img_beach_sparks_after_dark_bj_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_1

image img_beach_sparks_after_dark_bj_1:
    "bg beachsparksafterdarkbj_1"
    pause 0.3
    "bg beachsparksafterdarkbj_2"
    pause 0.1
    "bg beachsparksafterdarkbj_3"
    pause 0.1
    "bg beachsparksafterdarkbj_4"
    pause 0.2
    "bg beachsparksafterdarkbj_2"
    pause 0.2
    repeat

label lbl_beach_sparks_after_dark_bj_revisit_2:
    scene img_beach_sparks_after_dark_bj_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_2

image img_beach_sparks_after_dark_bj_2:
    "bg beachsparksafterdarkbj_1"
    pause 0.3
    "bg beachsparksafterdarkbj_3"
    pause 0.1
    "bg beachsparksafterdarkbj_4"
    pause 0.2
    "bg beachsparksafterdarkbj_2"
    pause 0.2
    repeat

label lbl_beach_sparks_after_dark_bj_revisit_3:
    scene img_beach_sparks_after_dark_bj_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_beach_sparks_after_dark_bj_revisit_3

image img_beach_sparks_after_dark_bj_3:
    "bg beachsparksafterdarkbj_1"
    pause 0.2
    "bg beachsparksafterdarkbj_4"
    pause 0.1
    "bg beachsparksafterdarkbj_2"
    pause 0.2
    repeat

label lbl_beach_sparks_after_dark_bj_revisit_cum:
    call screen scr_beach_sparks_after_dark_bj_revisit_cum

screen scr_beach_sparks_after_dark_bj_revisit_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beach_sparks_after_dark_bj_revisit_1")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beach_sparks_after_dark_bj_revisit_cumming")
    else:
        pass

label lbl_beach_sparks_after_dark_bj_revisit_cumming:
    scene bg beachsparksafterdarkbj_4
    $ renpy.pause(1,hard=True)
    show bg beachsparksafterdarkbj_5_1
    $ renpy.pause(0.4,hard=True)
    show bg beachsparksafterdarkbj_5_2
    $ renpy.pause(0.4,hard=True)
    show bg beachsparksafterdarkbj_5_3
    $ renpy.pause(0.4,hard=True)
    show bg beachsparksafterdarkbj_5_4
    $ renpy.pause(0.4,hard=True)
    show bg beachsparksafterdarkbj_5_5
    $ renpy.pause()

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
