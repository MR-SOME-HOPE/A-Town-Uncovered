###############
## Setup
default schoolbathroom_randomevent = 0

## Story Path
label lbl_schoolbathroomfemale_day_setup:
    $ schoolbathroom_randomevent =  renpy.random.randint(1,6)
    ## MEET THE THREEGHANS
    if gtime == 0 and (meghan_path == 0 or teghan_path == 0 or chieghan_path == 0) and main_story >= 12:
        jump lbl_meet_threeghans
    ## NOT INSIDE THE SEXWORLD
    if not 31 <= main_story <= 35:
        ## Caught in Girls' Bathroom
        if missallaway_path == 4:
            jump lbl_caught_in_girls_bathroom
        ## RANDOM MEGHAN ENCOUNTER
        elif meghan_path > 0 and (day == 0 or day == 3) and gtime <= 1 and schoolbathroom_randomevent == 1:
            jump lbl_meghan_weed_kush
        ## RANDOM TEGHAN ENCOUNTER
        elif day == 1 or day == 4 and gtime <= 1 and schoolbathroom_randomevent == 2:
            jump lbl_teghan_stall_reverse_seated_cowgirl

    ## Eventless
    else:
        jump lbl_schoolbathroomfemale_day

###############
## Room Navigation
## This is the map for school bathroom female during the day
label lbl_schoolbathroomfemale_day:

    scene bg schoolbathroomfemale_day
    if gtime == 0:
        if insexworld == 1 and main_story <= 35:
            show btn_schoolbathroom_day_meghansexworld_idle2
            show btn_schoolbathroom_day_teghansexworld_idle2
            show btn_schoolbathroom_day_chieghansexworld_idle2
        else:
            if main_story >= 12:
                show btn_schoolbathroom_day_meghan_idle2
                show btn_schoolbathroom_day_teghan_idle2
                show btn_schoolbathroom_day_chieghan_idle2
    call screen scr_schoolbathroomfemale_day

screen scr_schoolbathroomfemale_day():
    if gtime == 0:
        if insexworld == 1 and main_story <= 35:
            imagebutton auto "btn schoolbathroom_day_meghansexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroomfemale_day_meghan_sexworld")
            imagebutton auto "btn schoolbathroom_day_teghansexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroomfemale_day_teghan_sexworld")
            imagebutton auto "btn schoolbathroom_day_chieghansexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroomfemale_day_chieghan_sexworld")
        else:
            if main_story >= 12:
                imagebutton auto "btn schoolbathroom_day_meghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroomfemale_day_meghan")
                imagebutton auto "btn schoolbathroom_day_teghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroomfemale_day_teghan")
                imagebutton auto "btn schoolbathroom_day_chieghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroomfemale_day_chieghan")
    imagebutton auto "btn schoolbathroom_day_hallway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway1_day_setup")
    use hud_overlay

###############
