###############
## Setup
## Story Path
label lbl_myhallway_day_setup:
    ## NOT IN THE SEX WORLD
    if insexworld == 0:
        ###### MAIN STORY #######
        # if main_story == 148:
        #     jump lbl_edwards_stolen_evidence
        ###### SIDE STORY #######
        ## About Last Night
        if mum_path == 1:
            jump lbl_about_last_night
        ## Mom in bedroom
        if mum_path == 11 and sister_path >= 26:#Destroyed fort
            pov "{i}What's that noise coming from [missus]\'s bedroom?{/i}"
            jump lbl_myhallway_day
        ## Healed Eye
        elif mum_path == 17 and day == 4:
            jump lbl_healed_eye
        ## Post Mom Midnight Fun
        elif mum_path == 24:
            jump lbl_post_mom_midnight_fun
        ## Just a Friend?
        if sister_path == 0 and main_story >= 17 and not (gtime == 0 and day in (0,3)) and not (gtime == 1 and day == 4):
            jump lbl_just_a_friend
        ## Don't Kiss and Tell
        elif sister_path == 13 and gtime == 1 and day != 4:
            jump lbl_dont_kiss_and_tell
        ## Hows Sister and Effie
        elif sister_path == 22:
            jump lbl_hows_sister_and_effie
        ## Dad Apologizing
        elif sister_path == 37 and day != 2:
            jump lbl_dad_apologizing
        ## Stressed from Work
        if mumsis_path == 2.5:
            jump lbl_stressed_from_work
        ## Stressed from Work (TIMEJUMP)
        elif mumsis_path == 3 and mumsis_stressedfromwork == 0:
            jump lbl_stressed_from_work
        ## Unusually Sleepy
        elif mumsis_path == 4:
            jump lbl_unusually_sleepy
        ## Mom Sis Movie Invite
        elif mumsis_path == 12 and mum_path >= 28 and sister_path >= 40 and gtime == 0:
            jump lbl_mom_sis_movie_invite
    else:
        jump lbl_myhallway_day

###############
## Room Navigation
## This is the map for my hallway during the day
label lbl_myhallway_day:

    scene bg myhallway_day
    call screen scr_myhallway_day

screen scr_myhallway_day():
    imagebutton auto "btn myhallway_day_parentsroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_day_setup")
    imagebutton auto "btn myhallway_day_sisterroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sisterbedroom_day_setup")
    imagebutton auto "btn myhallway_day_mybedroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_day_setup")
    imagebutton auto "btn myhallway_day_bathroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybathroom_day_setup")
    imagebutton auto "btn myhallway_day_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mykitchen_day_setup")

    ## Teddy Bear
    if mum_path == 15:
        if cheermomup_doorbear == 0:
            pass
        elif cheermomup_doorbear == 3:
            add "img myhallway_day_teddybear3"
        elif cheermomup_doorbear == 2:
            add "img myhallway_day_teddybear2"
        elif cheermomup_doorbear == 1:
            add "img myhallway_day_teddybear1"
    use hud_overlay

###############
## Label
