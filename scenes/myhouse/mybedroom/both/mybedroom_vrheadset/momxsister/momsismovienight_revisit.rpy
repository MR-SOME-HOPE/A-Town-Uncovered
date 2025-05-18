## Mom Sis Movie Night
####################
## CHOICE
label lbl_mom_sis_movie_night_revisit_choice:
    menu:
        "Stick it in Mom" if winc == 1:
            jump lbl_mom_sis_movie_night_revisit_mom_pre
        "Stick it in [missus]" if winc == 0:
            jump lbl_mom_sis_movie_night_revisit_mom_pre
        "Stick it in [sister]":
            jump lbl_mom_sis_movie_night_revisit_sister_pre

label lbl_mom_sis_movie_night_revisit_choice2:
    menu:
        "Stick it in Mom" if winc == 1:
            jump lbl_mom_sis_movie_night_revisit_mom_0
        "Stick it in [missus]" if winc == 0:
            jump lbl_mom_sis_movie_night_revisit_mom_0
        "Stick it in [sister]":
            jump lbl_mom_sis_movie_night_revisit_sister_0

############################################################
############################################################
## Mom Pre
label lbl_mom_sis_movie_night_revisit_mom_pre:
    if hscene_xray == 0:
        scene bg momsismovienight_hscenemom_1
    else:
        scene bg momsismovienight_hscenemom_1_0


    pov "Don't mind me, [missus]."

    if hscene_xray == 0:
        show bg momsismovienight_hscenemom_4
        with hpunch
    else:
        show bg momsismovienight_hscenemom_4_0
        with hpunch

    mum "Mmph!"
    mum "Oh, [sister]?"
    mum "I don't remember you having such a huge cock."
    if hscene_xray == 0:
        show bg momsismovienight_hscenemom_5
    else:
        show bg momsismovienight_hscenemom_5_0
    pov "What?"
    if hscene_xray == 0:
        show bg momsismovienight_hscenemom_1
    else:
        show bg momsismovienight_hscenemom_1_0
    mum "Mmm... mph- go on, sweetie. Make love to me."

    jump lbl_mom_sis_movie_night_revisit_mom_0

label lbl_mom_sis_movie_night_revisit_mom_0:
    #$ mom_sis_movie_night_counter = 0
    if hscene_xray == 0:
        jump lbl_mom_sis_movie_night_revisit_mom_1
    else:
        jump lbl_mom_sis_movie_night_revisit_mom_1_0

####################
## Mom Stage 1
label lbl_mom_sis_movie_night_revisit_mom_1:
    scene img_mom_sis_movie_night_revisit_mom_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_1

image img_mom_sis_movie_night_revisit_mom_stage_1:
    "bg momsismovienight_hscenemom_1"
    pause 0.2
    "bg momsismovienight_hscenemom_2"
    pause 0.2
    "bg momsismovienight_hscenemom_3"
    pause 0.2
    "bg momsismovienight_hscenemom_4"
    pause 0.2
    "bg momsismovienight_hscenemom_5"
    pause 0.2
    repeat

####################
## Mom Stage 1 XRAY
label lbl_mom_sis_movie_night_revisit_mom_1_0:
    scene img_mom_sis_movie_night_revisit_mom_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_1_0

image img_mom_sis_movie_night_revisit_mom_stage_1_0:
    "bg momsismovienight_hscenemom_1_0"
    pause 0.2
    "bg momsismovienight_hscenemom_2_0"
    pause 0.2
    "bg momsismovienight_hscenemom_3_0"
    pause 0.2
    "bg momsismovienight_hscenemom_4_0"
    pause 0.2
    "bg momsismovienight_hscenemom_5_0"
    pause 0.2
    repeat


####################
## Mom Stage 2
label lbl_mom_sis_movie_night_revisit_mom_2:
    scene img_mom_sis_movie_night_revisit_mom_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_2

image img_mom_sis_movie_night_revisit_mom_stage_2:
    "bg momsismovienight_hscenemom_1"
    pause 0.2
    "bg momsismovienight_hscenemom_2"
    pause 0.2
    "bg momsismovienight_hscenemom_4"
    pause 0.2
    "bg momsismovienight_hscenemom_5"
    pause 0.2
    repeat

####################
## Mom Stage 2 XRAY
label lbl_mom_sis_movie_night_revisit_mom_2_0:
    scene img_mom_sis_movie_night_revisit_mom_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_2_0

image img_mom_sis_movie_night_revisit_mom_stage_2_0:
    "bg momsismovienight_hscenemom_1_0"
    pause 0.2
    "bg momsismovienight_hscenemom_2_0"
    pause 0.2
    "bg momsismovienight_hscenemom_4_0"
    pause 0.2
    "bg momsismovienight_hscenemom_5_0"
    pause 0.2
    repeat

####################
## Mom Stage 3
label lbl_mom_sis_movie_night_revisit_mom_3:
    scene img_mom_sis_movie_night_revisit_mom_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_3

image img_mom_sis_movie_night_revisit_mom_stage_3:
    "bg momsismovienight_hscenemom_1"
    pause 0.2
    "bg momsismovienight_hscenemom_3"
    pause 0.2
    "bg momsismovienight_hscenemom_5"
    pause 0.2
    repeat

####################
## Mom Stage 3 XRAY
label lbl_mom_sis_movie_night_revisit_mom_3_0:
    scene img_mom_sis_movie_night_revisit_mom_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_mom_3_0

image img_mom_sis_movie_night_revisit_mom_stage_3_0:
    "bg momsismovienight_hscenemom_1_0"
    pause 0.2
    "bg momsismovienight_hscenemom_3_0"
    pause 0.2
    "bg momsismovienight_hscenemom_5_0"
    pause 0.2
    repeat

####################
## Mom Cum
label lbl_mom_sis_movie_night_revisit_mom_cum:
    if mum_points <= 6 or sister_points <= 6:
        jump lbl_mom_sis_movie_night_revisit_mom_cum_2
    else:
        jump lbl_mom_sis_movie_night_revisit_mom_cum_3

label lbl_mom_sis_movie_night_revisit_mom_cum_2:

    call screen scr_mom_sis_movie_night_revisit_mom_cum_2

screen scr_mom_sis_movie_night_revisit_mom_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_mom_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_mom_cumchoice")

label lbl_mom_sis_movie_night_revisit_mom_cum_3:

    call screen scr_mom_sis_movie_night_revisit_mom_cum_3

screen scr_mom_sis_movie_night_revisit_mom_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_choice2")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_mom_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_mom_cumchoice")

label lbl_mom_sis_movie_night_revisit_mom_cumchoice:
    jump lbl_mom_sis_movie_night_revisit_cumout


############################################################
############################################################
## Sister Pre
label lbl_mom_sis_movie_night_revisit_sister_pre:
    if hscene_xray == 0:
        scene bg momsismovienight_hscenesister_1
    else:
        scene bg momsismovienight_hscenesister_1_0

    pov "At ease, [sister]."

    if hscene_xray == 0:
        show bg momsismovienight_hscenesister_4
        with hpunch
    else:
        show bg momsismovienight_hscenesister_4_0
        with hpunch

    sis "Argh!"
    if winc:
        sis "Mm- mommy..."
    else:
        sis "[mumrole]..."
    sis "I can't believe how big your cock is..."
    if hscene_xray == 0:
        show bg momsismovienight_hscenesister_5
    else:
        show bg momsismovienight_hscenesister_5_0
    pov "W-wait- What?"
    if hscene_xray == 0:
        show bg momsismovienight_hscenesister_1
    else:
        show bg momsismovienight_hscenesister_1_0
    sis "Make me feel good, [missus]."

    jump lbl_mom_sis_movie_night_revisit_sister_0

label lbl_mom_sis_movie_night_revisit_sister_0:
    #$ mom_sis_movie_night_counter = 0
    if hscene_xray == 0:
        jump lbl_mom_sis_movie_night_revisit_sister_1
    else:
        jump lbl_mom_sis_movie_night_revisit_sister_1_0

####################
## Sister Stage 1
label lbl_mom_sis_movie_night_revisit_sister_1:
    scene img_mom_sis_movie_night_revisit_sister_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_1

image img_mom_sis_movie_night_revisit_sister_stage_1:
    "bg momsismovienight_hscenesister_1"
    pause 0.2
    "bg momsismovienight_hscenesister_2"
    pause 0.2
    "bg momsismovienight_hscenesister_3"
    pause 0.2
    "bg momsismovienight_hscenesister_4"
    pause 0.2
    "bg momsismovienight_hscenesister_5"
    pause 0.2
    repeat

####################
## Sister Stage 1 XRAY
label lbl_mom_sis_movie_night_revisit_sister_1_0:
    scene img_mom_sis_movie_night_revisit_sister_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_1_0

image img_mom_sis_movie_night_revisit_sister_stage_1_0:
    "bg momsismovienight_hscenesister_1_0"
    pause 0.2
    "bg momsismovienight_hscenesister_2_0"
    pause 0.2
    "bg momsismovienight_hscenesister_3_0"
    pause 0.2
    "bg momsismovienight_hscenesister_4_0"
    pause 0.2
    "bg momsismovienight_hscenesister_5_0"
    pause 0.2
    repeat

####################
## Sister Stage 2
label lbl_mom_sis_movie_night_revisit_sister_2:
    scene img_mom_sis_movie_night_revisit_sister_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_2

image img_mom_sis_movie_night_revisit_sister_stage_2:
    "bg momsismovienight_hscenesister_1"
    pause 0.2
    "bg momsismovienight_hscenesister_2"
    pause 0.2
    "bg momsismovienight_hscenesister_4"
    pause 0.2
    "bg momsismovienight_hscenesister_5"
    pause 0.2
    repeat

####################
## Sister Stage 2 XRAY
label lbl_mom_sis_movie_night_revisit_sister_2_0:
    scene img_mom_sis_movie_night_revisit_sister_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_2_0

image img_mom_sis_movie_night_revisit_sister_stage_2_0:
    "bg momsismovienight_hscenesister_1_0"
    pause 0.2
    "bg momsismovienight_hscenesister_2_0"
    pause 0.2
    "bg momsismovienight_hscenesister_4_0"
    pause 0.2
    "bg momsismovienight_hscenesister_5_0"
    pause 0.2
    repeat

####################
## Sister Stage 3
label lbl_mom_sis_movie_night_revisit_sister_3:
    scene img_mom_sis_movie_night_revisit_sister_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_3

image img_mom_sis_movie_night_revisit_sister_stage_3:
    "bg momsismovienight_hscenesister_1"
    pause 0.2
    "bg momsismovienight_hscenesister_2"
    pause 0.2
    "bg momsismovienight_hscenesister_5"
    pause 0.2
    repeat

####################
## Sister Stage 3 XRAY
label lbl_mom_sis_movie_night_revisit_sister_3_0:
    scene img_mom_sis_movie_night_revisit_sister_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_sis_movie_night_revisit_sister_3_0

image img_mom_sis_movie_night_revisit_sister_stage_3_0:
    "bg momsismovienight_hscenesister_1_0"
    pause 0.2
    "bg momsismovienight_hscenesister_2_0"
    pause 0.2
    "bg momsismovienight_hscenesister_5_0"
    pause 0.2
    repeat

####################
## Sister Cum
label lbl_mom_sis_movie_night_revisit_sister_cum:
    if mum_points <= 6 or sister_points <= 6:
        jump lbl_mom_sis_movie_night_revisit_sister_cum_2
    else:
        jump lbl_mom_sis_movie_night_revisit_sister_cum_3

label lbl_mom_sis_movie_night_revisit_sister_cum_2:

    call screen scr_mom_sis_movie_night_revisit_sister_cum_2

screen scr_mom_sis_movie_night_revisit_sister_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_sister_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_sister_cumchoice")

label lbl_mom_sis_movie_night_revisit_sister_cum_3:

    call screen scr_mom_sis_movie_night_revisit_sister_cum_3

screen scr_mom_sis_movie_night_revisit_sister_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_choice2")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_sister_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_sis_movie_night_revisit_sister_cumchoice")

label lbl_mom_sis_movie_night_revisit_sister_cumchoice:
    jump lbl_mom_sis_movie_night_revisit_cumout

####################
## CUMOUT
label lbl_mom_sis_movie_night_revisit_cumout:
    scene bg momsismovienight_hscenecumout_0
    pov "Guys, I'm cumming-"
    show bg momsismovienight_hscenecumout_0
    $ renpy.pause(1.5,hard=True)
    show bg momsismovienight_hscenecumout_1
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_2
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_3
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_4
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_5
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_6
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_7
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_8
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_9
    $ renpy.pause(0.3,hard=True)
    show bg momsismovienight_hscenecumout_10
    $ renpy.pause()
    mum "{i}*Huff huff*{/i} Oh my- what a mess..."
    sis "{i}*Pants*{/i} You're telling me..."
    pov "{i}*Huffing*{/i} You both know how I am."
    mum "Mmm honey, you were amazing."
    if winc:
        sis "You were too, mommy."
    else:
        sis "You were too, baby."
    mum "{i}*Giggles*{/i} I love hearing you call me that."
    mum "Reminds me of my younger years."
    if winc:
        sis "Moommy~"
    mum "I love you, [sister]."
    sis "I love you too, [missus]."
    pov "Uhm... I'm here too, you know."
    mum "{i}*Giggles*{/i}"
    sis "Can you imagine if [povname] saw us right now."
    mum "I know, right. I wonder where he could be."
    pov "You guys are weird."
    pov "I'll go get a towel."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
