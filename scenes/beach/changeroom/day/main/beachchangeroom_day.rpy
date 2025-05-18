###############
## Setup
label lbl_beachchangeroom_blue_day_setup:
    call lbl_beachchangeroom_day_setup ("blue")

label lbl_beachchangeroom_purple_day_setup:
    call lbl_beachchangeroom_day_setup ("purple")

label lbl_beachchangeroom_green_day_setup:
    call lbl_beachchangeroom_day_setup ("green")

label lbl_beachchangeroom_red_day_setup:
    call lbl_beachchangeroom_day_setup ("red")

label lbl_beachchangeroom_day_setup(color):
    scene
    $ renpy.show("bg beachchangeroom_%s_day" % color)
    if color != "red":
        call lbl_beachchangeroom_day_random_event
    elif beach_naked == 1:
        call lbl_beachchangeroom_day_random_event_blowjob
    call lbl_beachchangeroom_day_strip
    call lbl_beachchangeroom_day (color)

label lbl_beachchangeroom_day_random_event:
    if not 23 <= main_story <= 35:
        if beachchangeroom_visit == 0:
            $ beachchangeroom_visit = 1
            if date == 1 or date == 11 or date == 15 or date == 20 or date == 30 or date == 0:
                if 26.5 <= sister_path <= 34:
                    jump lbl_beachchangeroom_timetraveller
                else:
                    jump lbl_beachchangeroom_sistergloryhole
            elif date == 2 or date == 12 or date == 16 or date == 21 or date == 25:
                jump lbl_beachchangeroom_timetraveller
            elif date == 3 or date == 7 or date == 17 or date == 22 or date == 26:
                if 26.5 <= sister_path <= 34:
                    jump lbl_beachchangeroom_lillian
                else:
                    jump lbl_beachchangeroom_sisteraltgirl
            elif date == 4 or date == 8 or date == 18 or date == 23 or date == 27:
                jump lbl_beachchangeroom_missallawaypeeking
            elif date == 5 or date == 9 or date == 13 or date == 24 or date == 28:
                jump lbl_beachchangeroom_ashmom
            elif date == 6 or date == 10 or date == 14 or date == 19 or date == 29:
                jump lbl_beachchangeroom_lillian
    return

label lbl_beachchangeroom_day_random_event_blowjob:
    if not 23 <= main_story <= 35:
        $ random_event = renpy.random.randint(0, 1)
        if random_event >= 1:
            if beachgloryhole_visit == 0:
                pov "{i}Hmmm...{/i}"
                "Would you like to stick your dick in the hole?"

                menu:
                    "Yes":
                        $ beachgloryhole_visit = 1
                        scene bg beachchangeroom_gloryhole_day
                        if date == 6 or date == 11 or date == 18 or date == 25:
                            if main_story >= 12:
                                jump lbl_beachchangeroom_gloryhole_day_effiebj
                            else:
                                jump lbl_beachchangeroom_gloryhole_day_violettebj
                        elif date == 7 or date == 12 or date == 17:
                            if 26.5 <= sister_path <= 34:
                                jump lbl_beachchangeroom_gloryhole_day_drunkbj
                            else:
                                jump lbl_beachchangeroom_gloryhole_day_sisbj
                        elif date == 8 or date == 13 or date == 24 or date == 26:
                            jump lbl_beachchangeroom_gloryhole_day_violettebj
                        elif date == 1 or date == 14 or date == 23 or date == 0:
                            jump lbl_beachchangeroom_gloryhole_day_drunkbj
                        elif date == 2 or date == 15 or date == 22 or date == 27:
                            if mum_path >= 23:
                                jump lbl_beachchangeroom_gloryhole_day_mombj
                            else:
                                jump lbl_beachchangeroom_gloryhole_day_drunkbj
                        elif date == 3 or date == 16 or date == 21 or date == 30:
                            jump lbl_beachchangeroom_gloryhole_day_lillianbj
                        elif date == 4 or date == 9 or date == 20 or date == 28:
                            jump lbl_beachchangeroom_gloryhole_day_missallawaybj
                        elif date == 5 or date == 10 or date == 19 or date == 29:
                            jump lbl_beachchangeroom_gloryhole_day_nursehollickbj
                    "No":
                        pass
    return

label lbl_beachchangeroom_day_strip:
    pov "{i}It's empty.{/i}"
    if beach_naked <= 0 and not 23 <= main_story <= 35:
        "Would you like to strip off?"

        menu:
            "Yes":
                $ beach_naked = 1
                show pov neutral
                with dissolve
                $ renpy.pause(0.5, hard=True)
                hide pov neutral
                show povn neutral
                with fade
                $ renpy.pause()
                hide povn neutral
            "No":
                pass
    return

###############
## Room Navigation
label lbl_beachchangeroom_day(color):
    call screen scr_beachchangeroom_day(color)
    screen scr_beachchangeroom_day(color):
        imagebutton auto ("btn beachchangeroom_day_%s_%%s" % color) xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_day_setup")
