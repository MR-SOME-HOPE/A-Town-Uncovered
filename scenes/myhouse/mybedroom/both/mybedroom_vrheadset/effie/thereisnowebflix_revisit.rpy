## There is No Webflix
label lbl_there_is_no_webflix_sex_revisit:
    $ thereisnowebflix_sex = 1

    scene bg thereisnowebflix_sex_1
    with fade

label lbl_there_is_no_webflix_sex_revisit_0:
    jump lbl_there_is_no_webflix_sex_revisit_1


label lbl_there_is_no_webflix_sex_revisit_1:
    scene img_there_is_no_webflix_sex_revisit_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_1

image img_there_is_no_webflix_sex_revisit_1:
    "bg thereisnowebflix_sex_1"
    pause 0.3
    "bg thereisnowebflix_sex_2"
    pause 0.1
    "bg thereisnowebflix_sex_3"
    pause 0.1
    "bg thereisnowebflix_sex_4"
    pause 0.2
    "bg thereisnowebflix_sex_2"
    pause 0.2
    repeat

label lbl_there_is_no_webflix_sex_revisit_2:
    scene img_there_is_no_webflix_sex_revisit_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_2

image img_there_is_no_webflix_sex_revisit_2:
    "bg thereisnowebflix_sex_1"
    pause 0.3
    "bg thereisnowebflix_sex_2"
    pause 0.1
    "bg thereisnowebflix_sex_4"
    pause 0.2
    "bg thereisnowebflix_sex_2"
    pause 0.2
    repeat

label lbl_there_is_no_webflix_sex_revisit_3:
    scene img_there_is_no_webflix_sex_revisit_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_revisit_3

image img_there_is_no_webflix_sex_revisit_3:
    "bg thereisnowebflix_sex_1"
    pause 0.2
    "bg thereisnowebflix_sex_4"
    pause 0.1
    "bg thereisnowebflix_sex_2"
    pause 0.2
    repeat

label lbl_there_is_no_webflix_sex_revisit_cum:
    call screen scr_there_is_no_webflix_sex_revisit_cum

screen scr_there_is_no_webflix_sex_revisit_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_there_is_no_webflix_sex_revisit_0")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_there_is_no_webflix_sex_revisit_cumming")
    else:
        pass

label lbl_there_is_no_webflix_sex_revisit_cumming:
    scene bg thereisnowebflix_sex_5_1
    $ renpy.pause(1.5,hard=True)
    show bg thereisnowebflix_sex_5_2
    $ renpy.pause(0.6,hard=True)
    show bg thereisnowebflix_sex_5_3
    $ renpy.pause(0.6,hard=True)
    $ renpy.pause()

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
