####################
## Doggy (Mish)
label lbl_intense_modeling_hscene:
    ## PRE STORY

label lbl_intense_modeling_hscene_0:
    jump lbl_intense_modeling_hscene_1

####################
## Stage 1
label lbl_intense_modeling_hscene_1:
    scene img_intense_modeling_hscene_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_intense_modeling_hscene_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_intense_modeling_hscene_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_intense_modeling_hscene_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_intense_modeling_hscene_1

image img_intense_modeling_hscene_stage_1:
    "bg intensemodeling_hscene_1"
    pause 0.2
    "bg intensemodeling_hscene_2"
    pause 0.2
    "bg intensemodeling_hscene_3"
    pause 0.2
    "bg intensemodeling_hscene_4"
    pause 0.2
    "bg intensemodeling_hscene_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_intense_modeling_hscene_2:
    scene img_intense_modeling_hscene_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_intense_modeling_hscene_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_intense_modeling_hscene_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_intense_modeling_hscene_2

image img_intense_modeling_hscene_stage_2:
    "bg intensemodeling_hscene_5"
    pause 0.2
    "bg intensemodeling_hscene_7"
    pause 0.2
    "bg intensemodeling_hscene_8"
    pause 0.2
    "bg intensemodeling_hscene_6"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_intense_modeling_hscene_3:
    scene img_intense_modeling_hscene_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_intense_modeling_hscene_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_intense_modeling_hscene_3

image img_intense_modeling_hscene_stage_3:
    "bg intensemodeling_hscene_9"
    pause 0.2
    "bg intensemodeling_hscene_12"
    pause 0.2
    "bg intensemodeling_hscene_10"
    pause 0.2
    repeat

####################
## Cum
label lbl_intense_modeling_hscene_menu:
    if intense_modeling == 1:
        jump lbl_intense_modeling_2
    else:
        call screen scr_intense_modeling_hscene_menu

screen scr_intense_modeling_hscene_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_intense_modeling_hscene_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_intense_modeling_hscene_cumchoice")

label lbl_intense_modeling_hscene_cumchoice:
    menu:
        "Cum inside":
            jump lbl_intense_modeling_hscene_cumin
        "Cum on her":
            jump lbl_intense_modeling_hscene_cumout

####################
## Cum In
label lbl_intense_modeling_hscene_cumin:
    scene bg intensemodeling_hscene_14_0
    $ renpy.pause(1.5,hard=True)
    show bg intensemodeling_hscene_14_1
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_14_2
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_14_3
    eff "{i}*Huff huff huff*{/i}"
    pov "{i}*Pant pant*{/i}"
    eff "Fuck- it feels so hot-"
    pov "H-heh yeah~"
    pov "God, that felt so good to release it all in you."
    eff "Mmmm~"
    hit "Wow..."
    hit "Mhmm..."
    hit "Alright."
    hit "I think I got it!"
    hit "Ya'll can clean yourselves up now."
    eff "Give us a sec-"
    scene black
    with fade
    $ renpy.pause()
    "After a bit of cleaning up..."
    scene bg street_night
    with fade

    jump lbl_street_night_setup

####################
## Cum Out
label lbl_intense_modeling_hscene_cumout:
    scene bg intensemodeling_hscene_13_0
    $ renpy.pause(0.3,hard=True)
    show bg intensemodeling_hscene_13_1
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_2
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_3
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_4
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_5
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_6
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_7
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_8
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_9
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_10
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_11
    $ renpy.pause(0.4,hard=True)
    show bg intensemodeling_hscene_13_12
    eff "{i}*Huff huff huff*{/i}"
    pov "{i}*Pant pant*{/i}"
    eff "Fuck- it feels so hot-"
    pov "H-heh yeah~"
    pov "God, I made a real mess, didn't I?."
    eff "Mmmm~"
    hit "Wow..."
    hit "Mhmm..."
    hit "Alright."
    hit "I think I got it!"
    hit "Ya'll can clean yourselves up now."
    hit "Aaaand the table too."
    hit "The cleaning stuff should be in one of the cabinets here."
    eff "Give us a sec-"
    scene black
    with fade
    $ renpy.pause()
    "After a bit of cleaning up..."
    scene bg street_night
    with fade

    jump lbl_street_night_setup
