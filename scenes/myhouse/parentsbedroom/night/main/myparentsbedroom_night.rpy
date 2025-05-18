###############
## Setup
## Story Path
label lbl_parentsbedroom_night_setup:

    ## Parents Bedroom Movie Threesome Post-sex
    if main_story == 80:
        pov "I've had my fun tonight. Time to sleep."

    ## Post Watching Tv With Mom
    if mum_path == 1:
        if gtime == 3:
            dad "Oh, yeah! Fuck..."
            mum "Mmm. Mm.. Huun.."
            dad "You like my huge cock inside you, you dirty whore?"
            mum "Ye.. yes.. yes..."
        else:
            pov "{i}It's locked.{/i}"

    ## Cheer Mom Up - Locked Herself In
    elif 11 <= mum_path <= 14:
        if winc == 0:
            pov "[missus]?"
        else:
            pov "Mom?"
        pov "..."
        pov "She must be sleeping. I shouldn't disturb her."

    ## Post Cheery mom Up
    elif mum_path == 15 or mum_path == 16:
        pov "{i}I should leave her alone, seems like she doesn't want a proper face to face conversation.{/i}"

    ## Post Bath Time with Mom
    elif mum_path == 17:
        pov "{i}She'll come out in her own time. I don't wanna push things.{/i}"

    ## Dad's Gone - Mom's Missing
    elif mum_path == 20 and not (sister_path == 9 or sister_path == 16 or sister_path == 19):
        "{i}*Knock knock*{/i}"
        if winc == 0:
            pov "[missus]?"
            pov "[dadname]'s gone."
        else:
            pov "Mom?"
            pov "Dad's gone."
        pov "Can I come in?"
        pov "..."
        pov "Hello?"
        pov "..."
        scene bg parentsbedroom_night
        with fade
        $ renpy.pause()
        pov "{i}Where the hell is she?{/i}"
        $ mum_path = 21
        if winc == 0:
            $ renpy.notify("New Objective: Find [missus]")
        else:
            $ renpy.notify("New Objective: Find Mom")

        jump lbl_parentsbedroom_night
    elif mum_path == 28:
        pov "We had such a great night. I shouldn't ruin it by doing something I might regret."

    ## Mom Coddling Sister
    elif mumsis_path == 3 and mum_path >= 3 and sister_path >= 11:
        jump lbl_mom_coddling_sister

    ## Mom Sis Movie Night
    elif mumsis_path == 13 and gtime == 2:
        jump lbl_mom_sis_movie_night

    ## No Events
    else:
        jump lbl_parentsbedroom_night
    call screen scr_myhallway_night

###############
## Room Navigation
## This is the map for my parents's bedroom during the night
label lbl_parentsbedroom_night:
    if gtime == 2:
        #if main_story == 22:
        #    scene bg parentsbedroom_night
        #    show img parentsbedroom_night_bedmom
        ## Lights On TV Off - Mom Absent
        if (insexworld == 0 and mum_path == 0 and sister_path != 10):
            scene bg parentsbedroom_nightlightson
        elif mum_path == 1 or mum_path == 4 or 7 <= mum_path <= 9 or mum_path == 21:
            scene bg parentsbedroom_nightlightson

        ## Lights Off TV On - Mom Watching
        else:
            scene bg parentsbedroom_nightlightsontvon
    else:
        ## Lights Off TV Off
        scene bg parentsbedroom_night

        ## Both Absent
        if 7 <= mum_path <= 9:
            pass
        ## Mom Absent
        elif (mum_path == 0 and sister_path != 10) or mum_path == 21:
            show img parentsbedroom_night_beddad
        ## Dad Absent
        elif 20 <= mum_path <= 24 or 27 <= sister_path <= 36:
            show img parentsbedroom_night_bedmom
        ## No Event
        else:
            show img parentsbedroom_night_bedparents
    call screen scr_parentsbedroom_night

screen scr_parentsbedroom_night():

    ## NOT IN THE SEX WORLD
    if (main_story >= 16 and insexworld == 0):
        ## Both Absent
        ## Caught Parents Having Sex / Mom at the Park
        if 7 <= mum_path <= 9 or mum_path == 21:
            pass
        ## Mom Absent
        ## Watching TV / Mom Fallen Asleep / Caught Parents Having Sex and Post Fight / Mom at the Park
        elif (mum_path == 0 and sister_path != 10) or mum_path == 4 or 7 <= mum_path <= 9 or mum_path == 21:
            if gtime == 2:
                pass
            else:
                #imagebutton auto "btn parentsbedroom_night_mothersleep_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_mother_sleep")##
                imagebutton auto "btn parentsbedroom_night_dadsleep_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_dad_sleep")
        ## Dad Absent
        ## Dad Out of Town / Dad Kicked Out for Destroying Fort
        elif 20 <= mum_path <= 24 or 27 <= sister_path <= 36:
            if gtime == 2:
                imagebutton auto "btn parentsbedroom_night_mother_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_mother")
            else:
                imagebutton auto "btn parentsbedroom_night_mothersleep_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_mother_sleep")

        else:
            if gtime == 2:
                imagebutton auto "btn parentsbedroom_night_mother_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_mother")
            else:
                imagebutton auto "btn parentsbedroom_night_parentssleep_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_parents_sleep")
    else:
        if gtime == 2:
            imagebutton auto "btn parentsbedroom_night_mother_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_mother")
        else:
            imagebutton auto "btn parentsbedroom_night_parentssleep_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_night_parents_sleep")
    imagebutton auto "btn parentsbedroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
    use hud_overlay

###############
## Labels
