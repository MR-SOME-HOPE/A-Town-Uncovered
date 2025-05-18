## Hitomi Counter Cunnilingus

default hitomi_countercunnilingus = 0

label lbl_hitomi_counter_cunnilingus:
    ## PRE STORY
    if hitomi_countercunnilingus == 0:
        $ hitomi_countercunnilingus = 1

label lbl_hitomi_counter_cunnilingus_0:
    jump lbl_hitomi_counter_cunnilingus_1
    # if hscene_xray == 0:
    #     jump lbl_hitomi_counter_cunnilingus_1
    # else:
    #     jump lbl_hitomi_counter_cunnilingus_1_0

####################
## Stage 1
label lbl_hitomi_counter_cunnilingus_1:
    scene img_hitomi_counter_cunnilingus_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_counter_cunnilingus_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_counter_cunnilingus_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_counter_cunnilingus_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_counter_cunnilingus_1

image img_hitomi_counter_cunnilingus_stage_1:
    "bg hitomicountercunnilingus_1"
    pause 0.2
    "bg hitomicountercunnilingus_2"
    pause 0.2
    "bg hitomicountercunnilingus_3"
    pause 0.2
    "bg hitomicountercunnilingus_4"
    pause 0.2
    "bg hitomicountercunnilingus_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_hitomi_counter_cunnilingus_2:
    scene img_hitomi_counter_cunnilingus_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_counter_cunnilingus_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_counter_cunnilingus_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_counter_cunnilingus_2

image img_hitomi_counter_cunnilingus_stage_2:
    "bg hitomicountercunnilingus_1"
    pause 0.2
    "bg hitomicountercunnilingus_3"
    pause 0.2
    "bg hitomicountercunnilingus_4"
    pause 0.2
    "bg hitomicountercunnilingus_2"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_hitomi_counter_cunnilingus_3:
    scene img_hitomi_counter_cunnilingus_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_counter_cunnilingus_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_counter_cunnilingus_3

image img_hitomi_counter_cunnilingus_stage_3:
    "bg hitomicountercunnilingus_1"
    pause 0.2
    "bg hitomicountercunnilingus_3"
    pause 0.2
    "bg hitomicountercunnilingus_2"
    pause 0.2
    repeat

####################
## Cum
label lbl_hitomi_counter_cunnilingus_menu:
    call screen scr_hitomi_counter_cunnilingus_menu

screen scr_hitomi_counter_cunnilingus_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_counter_cunnilingus_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_counter_cunnilingus_cumchoice")

label lbl_hitomi_counter_cunnilingus_cumchoice:
    jump lbl_hitomi_counter_cunnilingus_cumin
    # menu:
    #     "Cum inside":
    #         if hscene_xray == 0:
    #             jump lbl_hitomi_counter_cunnilingus_cumin
    #         else:
    #             jump lbl_hitomi_counter_cunnilingus_cumin_0
    #     "Cum on her":
    #         jump lbl_hitomi_counter_cunnilingus_cumout

####################
## Cum In
label lbl_hitomi_counter_cunnilingus_cumin:
    scene bg hitomicountercunnilingus_4
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
