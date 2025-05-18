## Hitomi Backroom Mating Press

label lbl_hitomi_backroom_matingpress_revisit:
    ## PRE STORY
    if hitomi_backroommatingpress == 0:
        $ hitomi_backroommatingpress = 1

label lbl_hitomi_backroom_matingpress_revisit_0:
    jump lbl_hitomi_backroom_matingpress_revisit_1

####################
## Stage 1
label lbl_hitomi_backroom_matingpress_revisit_1:
    scene img_hitomi_backroom_matingpress_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_1

image img_hitomi_backroom_matingpress_revisit_stage_1:
    "bg hitomibackroommatingpress_1"
    pause 0.2
    "bg hitomibackroommatingpress_2"
    pause 0.2
    "bg hitomibackroommatingpress_3"
    pause 0.2
    "bg hitomibackroommatingpress_4"
    pause 0.2
    "bg hitomibackroommatingpress_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_hitomi_backroom_matingpress_revisit_2:
    scene img_hitomi_backroom_matingpress_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_2

image img_hitomi_backroom_matingpress_revisit_stage_2:
    "bg hitomibackroommatingpress_6"
    pause 0.2
    "bg hitomibackroommatingpress_8"
    pause 0.2
    "bg hitomibackroommatingpress_9"
    pause 0.2
    "bg hitomibackroommatingpress_10"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_hitomi_backroom_matingpress_revisit_3:
    scene img_hitomi_backroom_matingpress_revisit_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_revisit_3

image img_hitomi_backroom_matingpress_revisit_stage_3:
    "bg hitomibackroommatingpress_11"
    pause 0.2
    "bg hitomibackroommatingpress_13"
    pause 0.2
    "bg hitomibackroommatingpress_15"
    pause 0.2
    repeat

####################
## Cum
label lbl_hitomi_backroom_matingpress_revisit_menu:
    call screen scr_hitomi_backroom_matingpress_revisit_menu

screen scr_hitomi_backroom_matingpress_revisit_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_backroom_matingpress_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_backroom_matingpress_revisit_cumchoice")

label lbl_hitomi_backroom_matingpress_revisit_cumchoice:
    jump lbl_hitomi_backroom_matingpress_revisit_cumin

####################
## Cum In
label lbl_hitomi_backroom_matingpress_revisit_cumin:
    scene bg hitomibackroommatingpress_9
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
    hit "{i}*Pants*{/i}"
    hit "I-"
    pov "{i}*Huff huff*{/i}"
    hit "I-"
    pov "I-?."
    hit "{i}*Exhale*{/i} I- think I love you."
    pov "Hehehe~"
    pov "I think I love you too."
    hit "Let's keep going."
    pov "Mhmm-"

    scene black
    with fade
    $ renpy.pause()
    
    jump lbl_vrheadset_character_selection
