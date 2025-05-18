###############
## Setup
## Story Path
label lbl_myhallway_night_setup:
    ## NOT IN SEX WORLD
    if insexworld == 0 and main_story >= 15:
        ## What are you Watching? (Setup)
        if (mum_path == 0 and day != 1 and trustandsafety_shield == 0) and not (sister_path != 10 or sister_path != 15 or sister_path != 16):
            scene bg myhallway_night
            pov "{i}Hmm.. it sounds like the TV is on in the living room.{/i}"

            jump lbl_myhallway_night
        ## Mom Fallen Asleep (Setup)
        elif mum_path == 4 and day != 1:
            scene bg myhallway_night
            pov "{i}I can hear the TV in the living room again.{/i}"

            jump lbl_myhallway_night
        ## Caught Parents (Setup)
        elif mum_path == 7 and main_story > 44:
            scene bg myhallway_night
            pov "{i}There are some noises coming from downstairs...{/i}"

            jump lbl_myhallway_night
        ## Get Ready for Bed
        elif mum_path == 27:
            scene bg myhallway_night
            with fade

            jump lbl_get_ready_for_bed
        ## Post Twin Scolding
        if sister_path == 22:
            pov "{i}I- wanna go to bed and rest my hea- hehehehaha that rhymes!{/i}"

            jump lbl_mybedroom_night_setup
        ## Fort Destroyed
        elif sister_path == 26 and day <= 2 and not (20 <= mum_path <= 24 or mum_path == 12):
            scene bg myhallway_night
            with fade
            sis "STOOP IT!!"
            with hpunch
            sis "PLEEEEASSSEE!! GEET AWWAAYY!!"
            pov "{i}That came from downstairs! I hope [sister] is okay.{/i}"
            $ townmap_enabled = 0
            $ sister_path = 26.5

            jump lbl_myhallway_night
        ## No Event
        else:
            jump lbl_myhallway_night

    ## No Event
    else:
        jump lbl_myhallway_night

###############
## Room Navigation
## This is the map for my hallway during the night
label lbl_myhallway_night:

    scene bg myhallway_night
    call screen scr_myhallway_night

screen scr_myhallway_night():
    imagebutton auto "btn myhallway_night_parentsroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_setup")
    imagebutton auto "btn myhallway_night_sisterroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sisterbedroom_night_setup")
    imagebutton auto "btn myhallway_night_mybedroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_night_setup")
    imagebutton auto "btn myhallway_night_bathroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybathroom_night_setup")
    imagebutton auto "btn myhallway_night_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mykitchen_night_setup")

    ## Teddy Bear
    if mum_path == 15:
        if cheermomup_doorbear == 0:
            pass
        elif cheermomup_doorbear == 3:
            add "img myhallway_night_teddybear3"
        elif cheermomup_doorbear == 2:
            add "img myhallway_night_teddybear2"
        elif cheermomup_doorbear == 1:
            add "img myhallway_night_teddybear1"
    use hud_overlay

###############
## Labels
