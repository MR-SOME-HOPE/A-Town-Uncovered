###############
## Setup
## Story Path
label lbl_mybasement_day_setup:

    ## Basement is locked
    if sister_path <= 8.5:
        pov "{i}It's locked. It hasn't been open since we moved in.{/i}"

        jump lbl_mylivingroom_day_setup

    ## Pre-Ask Sister Back Home
    elif sister_path == 30 and fursuitforboxjob_boxes >= 50:
        scene bg mybasement_lightsonwreck
        with fade
        pov "{i}Before I start, I want to talk to Effie and see if she can get [sister] around the idea of visiting sometime.{/i}"

        jump lbl_mybasement_day

    ## Twin Fortress Rebuild
    elif sister_path == 32:
        jump lbl_twin_fortress_rebuild

    ## Fort Rebuild Reveal
    elif sister_path == 33.5:
        jump lbl_fort_rebuild_reveal

    ## Mom Left Out Twin Fortress Setup
    if mumsis_path == 9 and mum_path >= 24 and sister_path >= 34:
        scene bg mybasement_lightson2 with fade
        $ townmap_enabled = 0
        $ mumsis_path = 9.1
        pov "{i}Why did I come down here...?{/i}"
        jump lbl_mybasement_day

    ## Eventless
    else:
        jump lbl_mybasement_day

###############
## Room Navigation
## This is the map for my livingroom during the day
label lbl_mybasement_day:
    if sister_path <= 10:
        scene bg mybasement_lightsonmessy
    elif sister_path <= 26.5:
        scene bg mybasement_lightson
    elif sister_path <= 32:
        scene bg mybasement_lightsonwreck
    else:
        scene bg mybasement_lightson2
    call screen scr_mybasement_day

screen scr_mybasement_day():
    imagebutton auto "btn mybasement_lightson_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_day_setup")
    if main_story <= 4:
        pass
    else:
        use hud_overlay
