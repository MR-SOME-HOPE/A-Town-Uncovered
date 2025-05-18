## Ara Asika H-scene

default araasika_hscene = 0

label lbl_ara_asika_hscene:
    ## PRE STORY
    if araasika_hscene == 0:
        $ araasika_hscene = 1

label lbl_ara_asika_hscene_0:
    jump lbl_ara_asika_hscene_1
    # if hscene_xray == 0:
    #     jump lbl_ara_asika_hscene_1
    # else:
    #     jump lbl_ara_asika_hscene_1_0

####################
## Stage 1
label lbl_ara_asika_hscene_1:
    scene img_ara_asika_hscene_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_ara_asika_hscene_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_ara_asika_hscene_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_ara_asika_hscene_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_ara_asika_hscene_1

image img_ara_asika_hscene_stage_1:
    "bg araasika_hscene_1"
    pause 0.2
    "bg araasika_hscene_2"
    pause 0.2
    "bg araasika_hscene_3"
    pause 0.2
    "bg araasika_hscene_4"
    pause 0.2
    "bg araasika_hscene_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_ara_asika_hscene_2:
    scene img_ara_asika_hscene_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_ara_asika_hscene_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_ara_asika_hscene_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_ara_asika_hscene_2

image img_ara_asika_hscene_stage_2:
    "bg araasika_hscene_1"
    pause 0.2
    "bg araasika_hscene_3"
    pause 0.2
    "bg araasika_hscene_4"
    pause 0.2
    "bg araasika_hscene_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_ara_asika_hscene_3:
    scene img_ara_asika_hscene_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_ara_asika_hscene_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_ara_asika_hscene_3

image img_ara_asika_hscene_stage_3:
    "bg araasika_hscene_1"
    pause 0.2
    "bg araasika_hscene_3"
    pause 0.2
    "bg araasika_hscene_5"
    pause 0.2
    repeat

####################
## Cum
label lbl_ara_asika_hscene_menu:
    call screen scr_ara_asika_hscene_menu

screen scr_ara_asika_hscene_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_ara_asika_hscene_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_ara_asika_hscene_cumchoice")

label lbl_ara_asika_hscene_cumchoice:
    jump lbl_ara_asika_hscene_cumin
    # menu:
    #     "Cum inside":
    #         if hscene_xray == 0:
    #             jump lbl_ara_asika_hscene_cumin
    #         else:
    #             jump lbl_ara_asika_hscene_cumin_0
    #     "Cum on her":
    #         jump lbl_ara_asika_hscene_cumout

####################
## Cum In
label lbl_ara_asika_hscene_cumin:
    scene bg araasika_hscene_5
    show white
    with dissolve
    $ renpy.pause(0.2,hard=True)
    hide white
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show white
    with dissolve
    $ renpy.pause(0.5,hard=True)
    hide white
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show white
    with dissolve
    $ renpy.pause(0.8,hard=True)
    hide white
    with dissolve
    ara "FUCKING HELL!"
    ara "That was amazing!!"
    pov "{i}*Huff huff huff*{/i}"
    ara "You really are a good fuck."
    ara "Did you all enjoy the show?!"
    "Crowd" "YEAAH!!"
    "Crowd" "I wanna cum so hard!!"
    "Crowd" "Ara we love you!!"
    scene black
    with fade
    $ renpy.pause()
    "After kicking some sand over the cum pool..."

    jump lbl_violettes_law
