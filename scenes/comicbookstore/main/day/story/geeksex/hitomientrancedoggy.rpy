## Hitomi Entrance Doggy

default hitomi_entrancedoggy = 0

label lbl_hitomi_entrance_doggy:
    ## PRE STORY
    if hitomi_entrancedoggy == 0:
        $ hitomi_entrancedoggy = 1

label lbl_hitomi_entrance_doggy_0:
    jump lbl_hitomi_entrance_doggy_1
    # if hscene_xray == 0:
    #     jump lbl_hitomi_entrance_doggy_1
    # else:
    #     jump lbl_hitomi_entrance_doggy_1_0

####################
## Stage 1
label lbl_hitomi_entrance_doggy_1:
    scene img_hitomi_entrance_doggy_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_entrance_doggy_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_entrance_doggy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_entrance_doggy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_entrance_doggy_1

image img_hitomi_entrance_doggy_stage_1:
    "bg hitomientrancedoggy_1"
    pause 0.2
    "bg hitomientrancedoggy_2"
    pause 0.2
    "bg hitomientrancedoggy_3"
    pause 0.2
    "bg hitomientrancedoggy_4"
    pause 0.2
    "bg hitomientrancedoggy_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_hitomi_entrance_doggy_2:
    scene img_hitomi_entrance_doggy_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_entrance_doggy_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_entrance_doggy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_entrance_doggy_2

image img_hitomi_entrance_doggy_stage_2:
    "bg hitomientrancedoggy_1"
    pause 0.2
    "bg hitomientrancedoggy_3"
    pause 0.2
    "bg hitomientrancedoggy_4"
    pause 0.2
    "bg hitomientrancedoggy_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_hitomi_entrance_doggy_3:
    scene img_hitomi_entrance_doggy_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_entrance_doggy_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_entrance_doggy_3

image img_hitomi_entrance_doggy_stage_3:
    "bg hitomientrancedoggy_1"
    pause 0.2
    "bg hitomientrancedoggy_3"
    pause 0.2
    "bg hitomientrancedoggy_5"
    pause 0.2
    repeat

####################
## Cum
label lbl_hitomi_entrance_doggy_menu:
    call screen scr_hitomi_entrance_doggy_menu

screen scr_hitomi_entrance_doggy_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_entrance_doggy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_entrance_doggy_cumchoice")

label lbl_hitomi_entrance_doggy_cumchoice:
    jump lbl_hitomi_entrance_doggy_cumin
    # menu:
    #     "Cum inside":
    #         if hscene_xray == 0:
    #             jump lbl_hitomi_entrance_doggy_cumin
    #         else:
    #             jump lbl_hitomi_entrance_doggy_cumin_0
    #     "Cum on her":
    #         jump lbl_hitomi_entrance_doggy_cumout

####################
## Cum In
label lbl_hitomi_entrance_doggy_cumin:
    scene bg hitomientrancedoggy_4
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
    hit "{i}*Huff huff huff*{/i}"
    hit "Fuuuck-"
    pov "{i}*Huff huff gulps*{/i}"
    hit "That was- amazing-"
    pov "Hehehe~"
    pov "I'm glad you like it-"
    hit "Like it? I fucking want more!"
    pov "You might get addicted to my tongue."
    scene black
    with fade
    $ renpy.pause()
    "After a few more rounds..."

    jump lbl_geek_sex
