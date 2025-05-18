###############
## Setup
## Story Path
label lbl_schoolgym_day_setup:
    ## Iron Fist of the Law
    if main_story == 60:
       jump lbl_iron_fist_of_the_law

    ## Artistic Expression
    if effie_path == 7:
        jump lbl_artistic_expression
    ## NOT ALLOWED IN (WHILE ART EXHIBITION IS IN PLACE)
    if effie_path == 8:
        pov "{i}*The art exhibition is still happening*{/i}"
        jump lbl_schoolyard_day

    ## NO EVENT
    else:
        jump lbl_schoolgym_day

###############
## Room Navigation
## This is the map for schoolgym during the day
label lbl_schoolgym_day:
    if 28 <= main_story <= 33:
        scene bg schoolgym_daysexworld
    else:
        scene bg schoolgym_day
    call screen scr_schoolgym_day

screen scr_schoolgym_day():
    if gtime == 0 and insexworld == 1:
        imagebutton auto "btn schoolgym_day_jaidensexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_day_jaiden_sexworld")
    elif gtime == 0 and main_story >= 12 and insexworld == 0:
        if jaiden_path == 0:
            imagebutton auto "btn schoolgym_day_jaiden_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_jaiden")
        else:
            imagebutton auto "btn schoolgym_day_jaiden_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_day_jaiden")
    imagebutton auto "btn schoolgym_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_setup")
    use hud_overlay

###############
## Labels
