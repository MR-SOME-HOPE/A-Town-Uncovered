####################
## Beanbags
label lbl_postcamgurlsubstitute_beanbags:
    #default postcamgurlsubstitute_beanbags_counter = 0

    scene bg postcamgurlsubstitute_beanbags_cumout_1
    with fade
    $ renpy.pause()
    pov "Comfortable, [sister]?"
    sis "Not until you put it inside-"

    jump postcamgurlsubstitute_beanbags_fuck_options

label lbl_postcamgurlsubstitute_beanbags_0:
    #$ postcamgurlsubstitute_beanbags_counter = 0
    if hscene_xray == 0:
        jump lbl_postcamgurlsubstitute_beanbags_1
    else:
        jump lbl_postcamgurlsubstitute_beanbags_1_0

menu postcamgurlsubstitute_beanbags_fuck_options:
    "Pussy fuck":
        jump lbl_postcamgurlsubstitute_beanbags_0
    "Anal fuck":
        jump lbl_postcamgurlsubstitute_beanbags_anal_0

####################
## Beanbags Stage 1
label lbl_postcamgurlsubstitute_beanbags_1:
    scene img_postcamgurlsubstitute_beanbags_stage_1
    #$ postcamgurlsubstitute_beanbags_counter += 1
    #show bg postcamgurlsubstitute_beanbags_pussy_1
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_2
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_3
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_2
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and postcamgurlsubstitute_beanbags_counter == 4:
    #    jump lbl_postcamgurlsubstitute_beanbags_cum
    #elif skill_sta <= 14 and postcamgurlsubstitute_beanbags_counter == 6:
    #    jump lbl_postcamgurlsubstitute_beanbags_2
    #elif skill_sta <= 20 and postcamgurlsubstitute_beanbags_counter == 8:
    #    jump lbl_postcamgurlsubstitute_beanbags_2
    #else:
    #    jump lbl_postcamgurlsubstitute_beanbags_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_1

image img_postcamgurlsubstitute_beanbags_stage_1:
    "bg postcamgurlsubstitute_beanbags_pussy_1"
    pause 0.3
    "bg postcamgurlsubstitute_beanbags_pussy_2"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_3"
    pause 0.3
    "bg postcamgurlsubstitute_beanbags_pussy_2"
    pause 0.3
    repeat

####################
## Beanbags Stage 1 XRAY
label lbl_postcamgurlsubstitute_beanbags_1_0:
    scene img_postcamgurlsubstitute_beanbags_stage_1_0
    #$ postcamgurlsubstitute_beanbags_counter += 1
    #show bg postcamgurlsubstitute_beanbags_pussy_1_0
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_3_0
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_2_0
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and postcamgurlsubstitute_beanbags_counter == 4:
    #    jump lbl_postcamgurlsubstitute_beanbags_cum
    #elif skill_sta <= 14 and postcamgurlsubstitute_beanbags_counter == 6:
    #    jump lbl_postcamgurlsubstitute_beanbags_2_0
    #elif skill_sta <= 20 and postcamgurlsubstitute_beanbags_counter == 8:
    #    jump lbl_postcamgurlsubstitute_beanbags_2_0
    #else:
    #    jump lbl_postcamgurlsubstitute_beanbags_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_1_0

image img_postcamgurlsubstitute_beanbags_stage_1_0:
    "bg postcamgurlsubstitute_beanbags_pussy_1_0"
    pause 0.3
    "bg postcamgurlsubstitute_beanbags_pussy_2_0"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_3_0"
    pause 0.3
    "bg postcamgurlsubstitute_beanbags_pussy_2_0"
    pause 0.3
    repeat

####################
## Beanbags Stage 2
label lbl_postcamgurlsubstitute_beanbags_2:
    scene img_postcamgurlsubstitute_beanbags_stage_2
    #$ postcamgurlsubstitute_beanbags_counter += 1
    #show bg postcamgurlsubstitute_beanbags_pussy_4
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_5
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_6
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and postcamgurlsubstitute_beanbags_counter == 14:
    #    jump lbl_postcamgurlsubstitute_beanbags_cum
    #elif skill_sta <= 20 and postcamgurlsubstitute_beanbags_counter == 16:
    #    jump lbl_postcamgurlsubstitute_beanbags_3
    #else:
    #    jump lbl_postcamgurlsubstitute_beanbags_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_2

image img_postcamgurlsubstitute_beanbags_stage_2:
    "bg postcamgurlsubstitute_beanbags_pussy_4"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_5"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_6"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_5"
    pause 0.2
    repeat

####################
## Beanbags Stage 2 XRAY
label lbl_postcamgurlsubstitute_beanbags_2_0:
    scene img_postcamgurlsubstitute_beanbags_stage_2_0
    #$ postcamgurlsubstitute_beanbags_counter += 1
    #show bg postcamgurlsubstitute_beanbags_pussy_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_5_0
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_6_0
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and postcamgurlsubstitute_beanbags_counter == 14:
    #    jump lbl_postcamgurlsubstitute_beanbags_cum
    #elif skill_sta <= 20 and postcamgurlsubstitute_beanbags_counter == 16:
    #    jump lbl_postcamgurlsubstitute_beanbags_3_0
    #else:
    #    jump lbl_postcamgurlsubstitute_beanbags_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_2_0

image img_postcamgurlsubstitute_beanbags_stage_2_0:
    "bg postcamgurlsubstitute_beanbags_pussy_4_0"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_5_0"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_6_0"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_5_0"
    pause 0.2
    repeat

####################
## Beanbags Stage 3
label lbl_postcamgurlsubstitute_beanbags_3:
    scene img_postcamgurlsubstitute_beanbags_stage_3
    #$ postcamgurlsubstitute_beanbags_counter += 1
    #show bg postcamgurlsubstitute_beanbags_pussy_7
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_9
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_8
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and postcamgurlsubstitute_beanbags_counter == 24:
    #    jump lbl_postcamgurlsubstitute_beanbags_cum
    #else:
    #    jump lbl_postcamgurlsubstitute_beanbags_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_3

image img_postcamgurlsubstitute_beanbags_stage_3:
    "bg postcamgurlsubstitute_beanbags_pussy_7"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_9"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_8"
    pause 0.2
    repeat

####################
## Beanbags Stage 3 XRAY
label lbl_postcamgurlsubstitute_beanbags_3_0:
    scene img_postcamgurlsubstitute_beanbags_stage_3_0
    #$ postcamgurlsubstitute_beanbags_counter += 1
    #show bg postcamgurlsubstitute_beanbags_pussy_7_0
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_9_0
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_beanbags_pussy_8_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and postcamgurlsubstitute_beanbags_counter == 24:
    #    jump lbl_postcamgurlsubstitute_beanbags_cum
    #else:
    #    jump lbl_postcamgurlsubstitute_beanbags_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_beanbags_3_0

image img_postcamgurlsubstitute_beanbags_stage_3_0:
    "bg postcamgurlsubstitute_beanbags_pussy_7_0"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_9_0"
    pause 0.2
    "bg postcamgurlsubstitute_beanbags_pussy_8_0"
    pause 0.2
    repeat

####################
## Beanbags Cum
label lbl_postcamgurlsubstitute_beanbags_cum:
    if sister_points <= 8:
        jump lbl_postcamgurlsubstitute_beanbags_cum_2
    else:
        jump lbl_postcamgurlsubstitute_beanbags_cum_3

label lbl_postcamgurlsubstitute_beanbags_cum_2:
    #if hscene_xray == 0:
    #    scene bg postcamgurlsubstitute_beanbags_pussy_1
    #else:
    #    scene bg postcamgurlsubstitute_beanbags_pussy_1_0
    call screen scr_postcamgurlsubstitute_beanbags_cum_2

screen scr_postcamgurlsubstitute_beanbags_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_beanbags_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_beanbags_cumchoice")

label lbl_postcamgurlsubstitute_beanbags_cum_3:
    #if hscene_xray == 0:
    #    scene bg postcamgurlsubstitute_beanbags_pussy_1
    #else:
    #    scene bg postcamgurlsubstitute_beanbags_pussy_1_0
    call screen scr_postcamgurlsubstitute_beanbags_cum_3

screen scr_postcamgurlsubstitute_beanbags_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_beanbags_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_beanbags_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_beanbags_cumchoice")

####################
## Cum Choice
label lbl_postcamgurlsubstitute_beanbags_cumchoice:
    menu:
        "Cum Inside":
            if hscene_xray == 0:
                jump lbl_postcamgurlsubstitute_beanbags_cumin
            else:
                jump lbl_postcamgurlsubstitute_beanbags_cumin_0

        "Cum Outside":
            jump lbl_postcamgurlsubstitute_beanbags_cumout

####################
## Beanbags Cum In
label lbl_postcamgurlsubstitute_beanbags_cumin:
    scene bg postcamgurlsubstitute_beanbags_pussy_3
    $ renpy.pause(1.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_6
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_7
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_8
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_9
    $ renpy.pause(1,hard=True)
    sis "Oh fuck- oh fuck- oh fuck--!"
    sis "Mmmm-"
    sis "[povname]... did-"
    sis "{i}*Pants*{/i}"
    sis "Did you just..."
    sis "Cum inside me...?"
    pov "..."
    pov "I may or may not have..."
    sis "Fuck, man!"
    sis "Shit..."
    sis "Now I need to take an emergency pill."
    pov "Sorry. I think it was worth it though."
    sis "Shut up."
    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## Beanbags Cum In XRAY
label lbl_postcamgurlsubstitute_beanbags_cumin_0:
    scene bg postcamgurlsubstitute_beanbags_pussy_10_0_1
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_3
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_4
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_5
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_6
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_7
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_8
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_pussy_10_0_9
    $ renpy.pause(1,hard=True)
    sis "Oh fuck- oh fuck- oh fuck--!"
    sis "Mmmm-"
    sis "[povname]... did-"
    sis "{i}*Pants*{/i}"
    sis "Did you just..."
    sis "Cum inside me...?"
    pov "..."
    pov "I may or may not have..."
    sis "Fuck, man!"
    sis "Shit..."
    sis "Now I need to take an emergency pill."
    pov "Sorry. I think it was worth it though."
    sis "Shut up."
    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## Beanbags Cum Out
label lbl_postcamgurlsubstitute_beanbags_cumout:
    scene bg postcamgurlsubstitute_beanbags_cumout_1
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_3
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_4
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_5
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_6
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_7
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_8
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_9
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_10
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_11
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_beanbags_cumout_12
    $ renpy.pause(1,hard=True)
    sis "Oh god.. oh my god..."
    sis "It's so fucking hot.."
    sis "{i}*Pants*{/i}"
    sis "You are so lucky you didn't mess up my rug..."
    pov "Lots of target practice."
    sis "Target practice..."
    sis "Frikkin' loser..."
    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## Beanbag Next
label lbl_postcamgurlsubstitute_beanbags_next:
    scene bg postcamgurlsubstitute_beanbags_cumout_1
    sis "{i}*Pants*{/i}"
    pov "Let's swap positions."
    sis "T-tooo what?"

    jump lbl_postcamgurlsubstitute_scenechoice_beanbags
