###############
## Setup
## Story Path
label lbl_sisterbedroom_day_setup:
    ## First Morning
    if main_story == 2:
        pov "{i}I shouldn't disturb her, she's still sleeping.{/i}"
        call screen scr_myhallway_day

    ## Wake Up Sister
    elif main_story == 3:
        jump lbl_wake_up_sister

    ## Post Wake Up Sister
    elif main_story == 4 or main_story == 5:
        pov "{i}Uhm.. let's not go back in there for a while.{/i}"
        call screen scr_myhallway_day

    ## Camgurl Streaming Time
    if day == 2 and gtime == 1:
        ## Camgurl Substitute
        if sister_path == 39:
            jump lbl_camgurl_substitute
        elif sister_path == 40:
            jump lbl_postcamgurl_substitute
        else:
            pov "{i}It's locked.{/i}"
            scene bg myhallway_day
            call screen scr_myhallway_day
    ## IN SEX WORLD
    elif insexworld == 1:
        pov "{i}That's weird, it's locked... She doesn't usually lock the door.{/i}"
        call screen scr_myhallway_day
    ## No Event
    else:
        jump lbl_sisterbedroom_day

###############
## Room Navigation
## This is the map for my sister's bedroom during the day
label lbl_sisterbedroom_day:

    scene bg sisterbedroom_day
    if sister_path == 35 and not (date < 14 and month == 5):#sister ask stargazing
        pov "{i}Huh, she's not here. She must be around somewhere.{/i}"
    call screen scr_sisterbedroom_day

screen scr_sisterbedroom_day():

    ## Paper Note
    if sister_path == 4 or sister_path == 5:
        ## Sister's at Work
        if ((day == 0 or day == 3) and gtime == 0) or (day == 4 and gtime == 1):
            imagebutton auto "btn sisterbedroom_day_note_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_found_camgurl_info")
        ## Sister's in the Shower
        elif ((day == 1 or day == 4) and gtime == 0) or (day == 5 and gtime == 1):
            if mum_path == 16:#mum in bath after locked in her room
                imagebutton auto "btn sisterbedroom_day_sister_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sisterbedroom_day_sister")
            elif not 26.5 <= sister_path <= 34:#sister in shower
                imagebutton auto "btn sisterbedroom_day_note_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_found_camgurl_info")
            else:
                pass
        ## No Papyer Note
        else:
            pass

    ## Work Schedule
    if ((day == 0 or day == 3) and gtime == 0) or (day == 4 and gtime == 1):
        pass

    ## Shower Schedule
    elif ((day == 1 or day == 4) and gtime == 0) or (day == 5 and gtime == 1):
        pass

    ## Breaking into the Basement / Sister's at Effie's House / Sister Ask Stargazing / Sister in Shower after stargazing night
    elif sister_path == 7 or 26.5 <= sister_path <= 33 or sister_path == 35 or sister_path == 36:
        pass

    ## No Event
    else:
        imagebutton auto "btn sisterbedroom_day_sister_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sisterbedroom_day_sister")
    imagebutton auto "btn sisterbedroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")
    use hud_overlay

###############
## Labels
