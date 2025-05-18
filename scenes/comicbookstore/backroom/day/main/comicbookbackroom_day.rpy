###############
## Setup
## Story Path
label lbl_comicbookbackroom_day_setup:
    ## Make sure Luck doesn't go over 20
    if skill_lucmax >= 20:
        $ skill_lucmax = 20

    ## The Roleplayers
    if main_story == 19:
        ## Show the comic book backroom during the day.
        scene bg comicbookbackroom_day
        with fade

        jump lbl_the_roleplayers
    ## Request & Reveal
    elif main_story == 100:
        jump lbl_request_and_reveal
    ## The Effie Charm
    elif hitomi_path == 15:
        jump lbl_the_effie_charm
    ## Intense Modeling
    elif hitomi_path == 16:
        jump lbl_intense_modeling
    ## Dude Where's My Hitomi
    elif hitomi_path == 17.5:
        jump lbl_dude_wheres_my_hitomi
    ## No Event
    else:
        jump lbl_comicbookbackroom_day

###############
## Room Navigation
## This is the map for comic book backroom during the day.
label lbl_comicbookbackroom_day:

    scene bg comicbookbackroom_day
    call screen scr_comicbookbackroom_day

screen scr_comicbookbackroom_day():
    imagebutton auto "btn comicbookbackroom_day_crugeon_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookbackroom_day_crugeon")
    imagebutton auto "btn comicbookbackroom_day_davendithas_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookbackroom_day_davendithas")
    imagebutton auto "btn comicbookbackroom_day_lordkev_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookbackroom_day_lordkev")
    imagebutton auto "btn comicbookbackroom_day_table_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookbackroom_day_table")
    imagebutton auto "btn comicbookbackroom_day_store_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookstore_day_setup")
    use hud_overlay

###############
## Labels
