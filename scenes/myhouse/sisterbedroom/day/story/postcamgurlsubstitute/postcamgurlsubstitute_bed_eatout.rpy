####################
## Eat Out
label lbl_postcamgurlsubstitute_eatout:
    #default postcamgurlsubstitute_eatout_counter = 0

    scene bg postcamgurlsubstitute_eatout_5
    with fade
    $ renpy.pause(1.2,hard=True)

    jump lbl_postcamgurlsubstitute_eatout_0

label lbl_postcamgurlsubstitute_eatout_0:
    #$ postcamgurlsubstitute_eatout_counter = 0

    jump lbl_postcamgurlsubstitute_eatout_1

####################
## Eat Out Stage 1
label lbl_postcamgurlsubstitute_eatout_1:
    scene img_postcamgurlsubstitute_eatout_stage_1
    #$ postcamgurlsubstitute_eatout_counter += 1
    #show bg postcamgurlsubstitute_eatout_1
    #$ renpy.pause(0.4,hard=True)
    #show bg postcamgurlsubstitute_eatout_2
    #$ renpy.pause(0.4,hard=True)
    #show bg postcamgurlsubstitute_eatout_3
    #$ renpy.pause(0.4,hard=True)
    #show bg postcamgurlsubstitute_eatout_4
    #$ renpy.pause(0.4,hard=True)
    #show bg postcamgurlsubstitute_eatout_5
    #$ renpy.pause(0.4,hard=True)
    #if skill_sta <= 7 and postcamgurlsubstitute_eatout_counter == 4:
    #    jump lbl_postcamgurlsubstitute_eatout_cum
    #elif skill_sta <= 14 and postcamgurlsubstitute_eatout_counter == 6:
    #    jump lbl_postcamgurlsubstitute_eatout_2
    #elif skill_sta <= 20 and postcamgurlsubstitute_eatout_counter == 8:
    #    jump lbl_postcamgurlsubstitute_eatout_2
    #else:
    #    jump lbl_postcamgurlsubstitute_eatout_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_1

image img_postcamgurlsubstitute_eatout_stage_1:
    "bg postcamgurlsubstitute_eatout_1"
    pause 0.4
    "bg postcamgurlsubstitute_eatout_2"
    pause 0.4
    "bg postcamgurlsubstitute_eatout_3"
    pause 0.4
    "bg postcamgurlsubstitute_eatout_4"
    pause 0.4
    "bg postcamgurlsubstitute_eatout_5"
    pause 0.4
    repeat

####################
## Eat Out Stage 2
label lbl_postcamgurlsubstitute_eatout_2:
    scene img_postcamgurlsubstitute_eatout_stage_2
    #$ postcamgurlsubstitute_eatout_counter += 1
    #show bg postcamgurlsubstitute_eatout_1
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_eatout_2
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_eatout_3
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_eatout_4
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_eatout_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and postcamgurlsubstitute_eatout_counter == 14:
    #    jump lbl_postcamgurlsubstitute_eatout_cum
    #elif skill_sta <= 20 and postcamgurlsubstitute_eatout_counter == 16:
    #    jump lbl_postcamgurlsubstitute_eatout_3
    #else:
    #    jump lbl_postcamgurlsubstitute_eatout_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_2

image img_postcamgurlsubstitute_eatout_stage_2:
    "bg postcamgurlsubstitute_eatout_1"
    pause 0.2
    "bg postcamgurlsubstitute_eatout_2"
    pause 0.2
    "bg postcamgurlsubstitute_eatout_3"
    pause 0.2
    "bg postcamgurlsubstitute_eatout_4"
    pause 0.2
    "bg postcamgurlsubstitute_eatout_5"
    pause 0.2
    repeat

####################
## Eat Out Stage 3
label lbl_postcamgurlsubstitute_eatout_3:
    scene img_postcamgurlsubstitute_eatout_stage_3
    #$ postcamgurlsubstitute_eatout_counter += 1
    #show bg postcamgurlsubstitute_eatout_1
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_eatout_2
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_eatout_3
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_eatout_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and postcamgurlsubstitute_eatout_counter == 24:
    #    jump lbl_postcamgurlsubstitute_eatout_cum
    #else:
    #    jump lbl_postcamgurlsubstitute_eatout_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_eatout_3

image img_postcamgurlsubstitute_eatout_stage_3:
    "bg postcamgurlsubstitute_eatout_1"
    pause 0.2
    "bg postcamgurlsubstitute_eatout_2"
    pause 0.2
    "bg postcamgurlsubstitute_eatout_3"
    pause 0.2
    "bg postcamgurlsubstitute_eatout_2"
    pause 0.2
    repeat

####################
## Cum
label lbl_postcamgurlsubstitute_eatout_cum:
    if sister_points <= 4:
        jump lbl_postcamgurlsubstitute_eatout_cum_2
    else:
        jump lbl_postcamgurlsubstitute_eatout_cum_3

label lbl_postcamgurlsubstitute_eatout_cum_2:

    #scene bg postcamgurlsubstitute_eatout_cum_1
    call screen scr_postcamgurlsubstitute_eatout_cum_2

screen scr_postcamgurlsubstitute_eatout_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_eatout_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_eatout_cum_1")

label lbl_postcamgurlsubstitute_eatout_cum_3:

    #scene bg postcamgurlsubstitute_eatout_cum_1
    call screen scr_postcamgurlsubstitute_eatout_cum_3

screen scr_postcamgurlsubstitute_eatout_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_scenechoice_eatout")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_eatout_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_eatout_cum_1")

label lbl_postcamgurlsubstitute_eatout_cum_1:
    scene bg postcamgurlsubstitute_eatout_cum_1
    $ renpy.pause(0.6,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_3
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_4
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_5
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_6
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_7
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_8
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_9
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_10
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_11
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_12
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_eatout_cum_13
    $ renpy.pause(1.2,hard=True)
    jump lbl_postcamgurlsubstitute_eatout_end

label lbl_postcamgurlsubstitute_eatout_end:
    pov "Oh, wow- thanks for the warning.."
    sis "Mmhm... sorry..."
    sis "I was too busy feeling good. I bet you understand-"
    menu:
        "I still didn't cum.":
            pov "Y'know, I still didn't cum yet."
            sis "I hear you, [povname]."
            jump lbl_postcamgurlsubstitute_scenechoice_eatout
        "Glad to be of service.":
            pov "Glad to be of service, [sister]. Hehehe~"
            pov "You taste really nice by the way."
            pov "Like a really addicting drug."
            sis "Hahaha, um- thanks? I think?"

    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## Missionary Next
label lbl_postcamgurlsubstitute_eatout_next:
    sis "{i}*Pants*{/i}"
    pov "Let's swap positions."
    sis "T-tooo what?"

    jump lbl_postcamgurlsubstitute_scenechoice_eatout
