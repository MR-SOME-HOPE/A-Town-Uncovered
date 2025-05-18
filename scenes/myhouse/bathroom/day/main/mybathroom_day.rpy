###############
## Setup
## Story Path
label lbl_mybathroom_day_setup:
    #family dinner day
    if sister_path == 36:
        scene bg mybathroom_day_sister1_1
        pov "{i}Oh, here she is.{/i}"
        scene bg mybathroom_day_sister1_2
        pov "Hey, [sis]."
        scene bg mybathroom_day_sister1_4
        sis "Oh, hey [pov], just getting up?"
        scene bg mybathroom_day_sister1_5
        pov "Yeah, I guess I was really worn out after last night."
        scene bg mybathroom_day_sister1_6
        sis "You could do with a shower too. Get your sexy ass in here."

        scene black with fade

        jump lbl_sister_shower_standing_doggy

    ## Bath with Mom
    if mum_path == 16:
        jump lbl_bath_with_mom

    ## Skip All Scenes
    #if mum_path == 17 or sister_path == 6:
    #    jump lbl_mybathroom_day

    ## Mom Sis Bathing Together
    if mumsis_path == 5 and mum_path >= 17.5 and sister_path >= 18 and date <= 12:
        jump lbl_mom_sis_bathing_together

    ## Mom Sis Bathing Together
    if mumsis_path == 6:
        "I shouldn't peek in again. They know I'm right outside."
        jump lbl_myhallway_day

    elif gtime == 0:
        ## Bath Voyeurism
        if day == 1 or day == 4:
            if main_story == 16 or main_story == 28 or main_story == 81:
                jump lbl_mybathroom_day
            else:
                if not 26.5 <= sister_path <= 34 and not sister_path == 6:
                    jump lbl_mybathroom_day_setup_sistershower
                else:
                    jump lbl_mybathroom_day
        elif day == 2:
            if main_story == 28 or 11 <= mum_path <= 15 or mum_path == 17 or main_story == 81:
                jump lbl_mybathroom_day
            else:
                jump lbl_mybathroom_day_setup_momshower
        else:
            jump lbl_mybathroom_day
    elif gtime == 1:
        if day == 0 or day == 6:
            if mum_path == 6 or 11 <= mum_path <= 15 or mum_path == 17:
                jump lbl_mybathroom_day
            else:
                jump lbl_mybathroom_day_setup_momshower
        elif day == 5:
            if not 26.5 <= sister_path <= 34 and not sister_path == 6:
                jump lbl_mybathroom_day_setup_sistershower
            else:
                jump lbl_mybathroom_day
        else:
            jump lbl_mybathroom_day
    else:
        jump lbl_mybathroom_day

## Sister Stand Up Shower Scene
label lbl_mybathroom_day_setup_sistershower:
    scene bg mybathroom_day_sister1_1
    jump lbl_mybathroom_day_sister1

## Mother Stand Up Shower Scene
label lbl_mybathroom_day_setup_momshower:
    scene bg mybathroom_day_mother1_1
    jump lbl_mybathroom_day_mother1

###############
## Room Navigation
## This is the map for my bedroom during the day with the door closed
label lbl_mybathroom_day:

    scene bg mybathroom_day_open
    call screen scr_mybathroom_day

screen scr_mybathroom_day():
    imagebutton auto "btn mybathroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybathroom_day_dooropen")
    imagebutton auto "btn mybathroom_day_wall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")
    if main_story <= 4:
        pass
    else:
        if main_story == 28 or mum_path == 5 or (mum_path == 17 and day == 4): ## Townmap Disabled
            pass
        else:
            use hud_overlay

## This is the map for my bathroom during the day with the door open
label lbl_mybathroom_day_1:
    scene bg mybathroom_day_open
    call screen scr_mybathroom_day_1

screen scr_mybathroom_day_1():
    imagebutton auto "btn mybathroom_day_wall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")
    if main_story <= 4:
        pass
    elif main_story == 28 or mum_path == 5 or (mum_path == 17 and day == 4): ## Townmap Disabled
        pass
    else:
        use hud_overlay

###############
## Labels
label lbl_mybathroom_day_dooropen:
    pov "{i}There seems to be no one here.{/i}"

    jump lbl_mybathroom_day_1
