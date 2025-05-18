## Dateish Night (Room)
label lbl_dateish_night_room_sex_revisit:
    $ dateishnight_sex = 1

    scene bg dateishnight_sex_1
    with fade

label lbl_dateish_night_room_sex_revisit_0:
    jump lbl_dateish_night_room_sex_revisit_1

label lbl_dateish_night_room_sex_revisit_1:
    scene img_dateish_night_room_sex_revisit_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_dateish_night_room_sex_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_dateish_night_room_sex_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_revisit_1

image img_dateish_night_room_sex_revisit_1:
    "bg dateishnight_sex_1"
    pause 0.3
    "bg dateishnight_sex_2"
    pause 0.1
    "bg dateishnight_sex_3"
    pause 0.1
    "bg dateishnight_sex_4"
    pause 0.2
    "bg dateishnight_sex_2"
    pause 0.2
    repeat

label lbl_dateish_night_room_sex_revisit_2:
    scene img_dateish_night_room_sex_revisit_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_dateish_night_room_sex_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_dateish_night_room_sex_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_revisit_2

image img_dateish_night_room_sex_revisit_2:
    "bg dateishnight_sex_1"
    pause 0.3
    "bg dateishnight_sex_2"
    pause 0.1
    "bg dateishnight_sex_4"
    pause 0.2
    "bg dateishnight_sex_2"
    pause 0.2
    repeat

label lbl_dateish_night_room_sex_revisit_3:
    scene img_dateish_night_room_sex_revisit_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_dateish_night_room_sex_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_revisit_3

image img_dateish_night_room_sex_revisit_3:
    "bg dateishnight_sex_1"
    pause 0.2
    "bg dateishnight_sex_4"
    pause 0.1
    "bg dateishnight_sex_2"
    pause 0.2
    repeat

label lbl_dateish_night_room_sex_revisit_cum:
    call screen scr_dateish_night_room_sex_revisit_cum

screen scr_dateish_night_room_sex_revisit_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_dateish_night_room_sex_revisit_0")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_dateish_night_room_sex_revisit_cumming")
    else:
        pass

label lbl_dateish_night_room_sex_revisit_cumming:
    scene bg dateishnight_sex_5
    $ renpy.pause(3,hard=True)

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection


