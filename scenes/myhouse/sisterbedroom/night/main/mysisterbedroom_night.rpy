###############
## Setups
## Story Path
label lbl_sisterbedroom_night_setup:

    ## NOT IN SEX WORLD (Mom is at the Park)
    if insexworld == 0 and main_story >= 16 and not (mum_path == 21):
        ## Sent a Link
        if sister_path == 2 and gtime == 2:
            jump lbl_sent_a_link
        ## Post Sent a Link
        elif sister_path == 3:
            pov "{i}I should leave her.{/i}"

            jump lbl_myhallway_night_setup
        ## Invite Sister to Fort (20 Questions Setup)
        elif sister_path == 15:
            jump lbl_invite_sister_to_fort
        ## Post Invite Sister to Fort (20 Questions Setup)
        elif sister_path == 16:
            pov "{i}She's changing. I'll just meet her down in the basement.{/i}"
            call screen scr_myhallway_night

    ## IN SEX WORLD
    elif insexworld == 1:
        pov "{i}That's weird, it's locked... She doesn't usually lock the door.{/i}"
        call screen scr_myhallway_night

    ## No Event
    else:
        jump lbl_sisterbedroom_night

###############
## Room Navigation
## This is the map for my sister's bedroom during the night
label lbl_sisterbedroom_night:
    if gtime == 2:
        ## Evening
        ## Lights Out - Out on a Weekend Night / Sister at Effie's House
        if day >= 5 or 26.5 <= sister_path <= 34:
            scene bg sisterbedroom_night
        ## Camgurl Substitute Favour (FAIL RESTART)
        elif sister_path == 39 and day == 2:
            scene black
            jump lbl_camgurl_substitute_favour_fail_sis_room
        ## Lights On - NO EVENT
        else:
            scene bg sisterbedroom_nightlightson
    else:
        ## Late Night
        ## Sister's Absent - Sister In the Basement / Sister at Effie's House
        scene bg sisterbedroom_night
        if sister_path == 10 or 26.5 <= sister_path <= 34:
            pass
        ## No Event
        else:
            show img sisterbedroom_night_bedsister
    call screen scr_sisterbedroom_night

screen scr_sisterbedroom_night():
    if gtime == 2:
        ## Evening
        ## Lights Out - Out on a Weekend Night / Sister at Effie's House
        if day >= 5 or 26.5 <= sister_path <= 34:
            imagebutton auto "btn sisterbedroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
        ## Lights On - NO EVENT
        else:
            imagebutton auto "btn sisterbedroom_night_sister_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sisterbedroom_night_sister")
            imagebutton auto "btn sisterbedroom_nightlightson_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
    else:
        ## Late Night
        ## Sister's Absent - Sister In the Basement / Sister at Effie's House
        if sister_path == 10 or 26.5 <= sister_path <= 33:
            pass
        ## No Event
        else:
            imagebutton auto "btn sisterbedroom_night_sistersleep_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sisterbedroom_night_sister_sleep")
        imagebutton auto "btn sisterbedroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
    use hud_overlay

###############
## Labels
