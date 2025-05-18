###############
## Setup
label lbl_mydiningroom_day_setup:
    ## Post News Breakfast
    if main_story == 83:
        jump lbl_post_news_breakfast

    ## Mom Under Table Trio
    if mumsis_path >= 13 and day == 5 and gtime == 0 and had_under_table_trio_that_day == 0:
        jump lbl_mom_under_table_trio

    ## NO EVENT
    else:
        jump lbl_mydiningroom_day

###############
## Room Navigation
label lbl_mydiningroom_day:
    if mowed_lawn == 1:
        scene bg mydiningroom_day
    else:
        scene bg mydiningroom_day_grassy
    call screen scr_mydiningroom_day

screen scr_mydiningroom_day():
    use hud_overlay
    imagebutton auto "btn mydiningroom_day_kitchen_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mykitchen_day_setup")
    if mowed_lawn == 1:
        imagebutton auto "btn mydiningroom_day_backyard_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_day_setup")
    else:
        imagebutton auto "btn mydiningroom_day_backyardgrassy_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_day_setup")
