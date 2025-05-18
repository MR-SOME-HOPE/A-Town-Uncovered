####################
## BJ
label lbl_postcamgurlsubstitute_bj:
    #default postcamgurlsubstitute_bj_counter = 0

    scene bg postcamgurlsubstitute_bj_0
    with fade
    $ renpy.pause(1.2,hard=True)

    jump lbl_postcamgurlsubstitute_bj_0

label lbl_postcamgurlsubstitute_bj_0:
    #$ postcamgurlsubstitute_bj_counter = 0

    jump lbl_postcamgurlsubstitute_bj_1

####################
## BJ Stage 1
label lbl_postcamgurlsubstitute_bj_1:
    scene img_postcamgurlsubstitute_bj_stage_1
    #$ postcamgurlsubstitute_bj_counter += 1
    #show bg postcamgurlsubstitute_bj_1
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_bj_2
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_bj_3
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_bj_4
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_bj_2
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and postcamgurlsubstitute_bj_counter == 4:
    #    jump lbl_postcamgurlsubstitute_bj_cum
    #elif skill_sta <= 14 and postcamgurlsubstitute_bj_counter == 6:
    #    jump lbl_postcamgurlsubstitute_bj_2
    #elif skill_sta <= 20 and postcamgurlsubstitute_bj_counter == 8:
    #    jump lbl_postcamgurlsubstitute_bj_2
    #else:
    #    jump lbl_postcamgurlsubstitute_bj_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_bj_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_bj_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_bj_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_bj_1

image img_postcamgurlsubstitute_bj_stage_1:
    "bg postcamgurlsubstitute_bj_1"
    pause 0.3
    "bg postcamgurlsubstitute_bj_2"
    pause 0.3
    "bg postcamgurlsubstitute_bj_3"
    pause 0.3
    "bg postcamgurlsubstitute_bj_4"
    pause 0.3
    "bg postcamgurlsubstitute_bj_2"
    pause 0.3
    repeat

####################
## BJ Stage 2
label lbl_postcamgurlsubstitute_bj_2:
    scene img_postcamgurlsubstitute_bj_stage_2
    #$ postcamgurlsubstitute_bj_counter += 1
    #show bg postcamgurlsubstitute_bj_5
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_bj_6
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_bj_7
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_bj_6
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and postcamgurlsubstitute_bj_counter == 14:
    #    jump lbl_postcamgurlsubstitute_bj_cum
    #elif skill_sta <= 20 and postcamgurlsubstitute_bj_counter == 16:
    #    jump lbl_postcamgurlsubstitute_bj_3
    #else:
    #    jump lbl_postcamgurlsubstitute_bj_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_bj_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_bj_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_bj_2

image img_postcamgurlsubstitute_bj_stage_2:
    "bg postcamgurlsubstitute_bj_5"
    pause 0.2
    "bg postcamgurlsubstitute_bj_6"
    pause 0.2
    "bg postcamgurlsubstitute_bj_7"
    pause 0.2
    "bg postcamgurlsubstitute_bj_6"
    pause 0.2
    repeat

####################
## BJ Stage 3
label lbl_postcamgurlsubstitute_bj_3:
    scene img_postcamgurlsubstitute_bj_stage_3
    #$ postcamgurlsubstitute_bj_counter += 1
    #show bg postcamgurlsubstitute_bj_1
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_bj_2
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_bj_4
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_bj_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and postcamgurlsubstitute_bj_counter == 24:
    #    jump lbl_postcamgurlsubstitute_bj_cum
    #else:
    #    jump lbl_postcamgurlsubstitute_bj_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_bj_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_bj_3

image img_postcamgurlsubstitute_bj_stage_3:
    "bg postcamgurlsubstitute_bj_1"
    pause 0.2
    "bg postcamgurlsubstitute_bj_2"
    pause 0.2
    "bg postcamgurlsubstitute_bj_4"
    pause 0.2
    "bg postcamgurlsubstitute_bj_2"
    pause 0.2
    repeat

####################
## BJ Cum
label lbl_postcamgurlsubstitute_bj_cum:
    if sister_points <= 4:
        jump lbl_postcamgurlsubstitute_bj_cum_2
    else:
        jump lbl_postcamgurlsubstitute_bj_cum_3

label lbl_postcamgurlsubstitute_bj_cum_2:

    #scene bg postcamgurlsubstitute_bj_1
    call screen scr_postcamgurlsubstitute_bj_cum_2

screen scr_postcamgurlsubstitute_bj_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_bj_cum_1")

label lbl_postcamgurlsubstitute_bj_cum_3:

    #scene bg postcamgurlsubstitute_bj_1
    call screen scr_postcamgurlsubstitute_bj_cum_3

screen scr_postcamgurlsubstitute_bj_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_bj_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_bj_cum_1")

####################
## BJ Cum in
label lbl_postcamgurlsubstitute_bj_cum_1:
    scene bg postcamgurlsubstitute_bj_cumshot_0
    $ renpy.pause(0.6,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_1
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_3
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_4
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_5
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_6
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_7
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_8
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_9
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_10
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_11
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_bj_cumshot_12
    $ renpy.pause(0.2,hard=True)
    sis "{i}*Mumbles*{/i}"
    pov "{i}*Pants*{/i}"
    sis "{i}*Mummurs*{/i}"
    pov "[sister]."
    pov "I can't hear the fuck you're saying..."
    sis "A-ye-shaad! -UCCKEYUOUU!"
    pov "Naww, I love you too, [sister]."
    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## BJ Next
label lbl_postcamgurlsubstitute_bj_next:
    scene bg postcamgurlsubstitute_bj_9
    sis "{i}*Pants*{/i}"
    pov "Let's swap positions."
    sis "T-tooo what?"

    jump lbl_postcamgurlsubstitute_scenechoice_bj

####################
## Scene Choice
label lbl_postcamgurlsubstitute_scenechoice_bj:
    menu:
        "Have her Lay Down":
            jump lbl_postcamgurlsubstitute_bed_choice
        "Play in the Bean Bags":
            jump lbl_postcamgurlsubstitute_beanbags

label lbl_postcamgurlsubstitute_scenechoice_eatout:
    menu:
        "Sit on the Bed":
            jump lbl_postcamgurlsubstitute_bj
        "Get on Top of Her":
            jump lbl_postcamgurlsubstitute_missionary
        "Play in the Bean Bags":
            jump lbl_postcamgurlsubstitute_beanbags

label lbl_postcamgurlsubstitute_scenechoice_missionary:
    menu:
        "Sit on the Bed":
            jump lbl_postcamgurlsubstitute_bj
        "Eat Her Out":
            jump lbl_postcamgurlsubstitute_eatout
        "Play in the Bean Bags":
            jump lbl_postcamgurlsubstitute_beanbags

label lbl_postcamgurlsubstitute_scenechoice_beanbags:
    menu:
        "Sit on the Bed":
            jump lbl_postcamgurlsubstitute_bj
        "Have her Lay Down":
            jump lbl_postcamgurlsubstitute_bed_choice

####################
## Bed Choice
label lbl_postcamgurlsubstitute_bed_choice:

    menu:
        "Eat Her Out":
            jump lbl_postcamgurlsubstitute_eatout
        "Get On Top":
            jump lbl_postcamgurlsubstitute_missionary
        #"Anal Fuck":
        #    jump lbl_postcamgurlsubstitute_missionary_anal_1#lbl_postcamgurlsubstitute_missionary_anal
