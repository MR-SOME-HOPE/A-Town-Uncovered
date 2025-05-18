## Hitomi Backroom Mating Press

default hitomi_backroommatingpress = 0

label lbl_hitomi_backroom_matingpress:
    ## PRE STORY
    if hitomi_backroommatingpress == 0:
        $ hitomi_backroommatingpress = 1

label lbl_hitomi_backroom_matingpress_0:
    jump lbl_hitomi_backroom_matingpress_1
    # if hscene_xray == 0:
    #     jump lbl_hitomi_backroom_matingpress_1
    # else:
    #     jump lbl_hitomi_backroom_matingpress_1_0

####################
## Stage 1
label lbl_hitomi_backroom_matingpress_1:
    scene img_hitomi_backroom_matingpress_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_backroom_matingpress_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_backroom_matingpress_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_1

image img_hitomi_backroom_matingpress_stage_1:
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
label lbl_hitomi_backroom_matingpress_2:
    scene img_hitomi_backroom_matingpress_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_backroom_matingpress_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_backroom_matingpress_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_2

image img_hitomi_backroom_matingpress_stage_2:
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
label lbl_hitomi_backroom_matingpress_3:
    scene img_hitomi_backroom_matingpress_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_backroom_matingpress_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_backroom_matingpress_3

image img_hitomi_backroom_matingpress_stage_3:
    "bg hitomibackroommatingpress_11"
    pause 0.2
    "bg hitomibackroommatingpress_13"
    pause 0.2
    "bg hitomibackroommatingpress_15"
    pause 0.2
    repeat

####################
## Cum
label lbl_hitomi_backroom_matingpress_menu:
    call screen scr_hitomi_backroom_matingpress_menu

screen scr_hitomi_backroom_matingpress_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_backroom_matingpress_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_backroom_matingpress_cumchoice")

label lbl_hitomi_backroom_matingpress_cumchoice:
    jump lbl_hitomi_backroom_matingpress_cumin
    # menu:
    #     "Cum inside":
    #         if hscene_xray == 0:
    #             jump lbl_hitomi_backroom_matingpress_cumin
    #         else:
    #             jump lbl_hitomi_backroom_matingpress_cumin_0
    #     "Cum on her":
    #         jump lbl_hitomi_backroom_matingpress_cumout

####################
## Cum In
label lbl_hitomi_backroom_matingpress_cumin:
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
    "After a few more rounds..."

    jump lbl_geek_sex


# ####################
# ## Doggy Cum Out
# label lbl_hitomi_backroom_matingpress_cumout:
#     scene bg hitomibackroommatingpress_15_0
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_1
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_2
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_3
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_4
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_5
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_6
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_7
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_8
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_9
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_10
#     $ renpy.pause(0.3,hard=True)
#     show bg hitomibackroommatingpress_15_11
#     hit "Fuck that's hot-"
#     hit "{i}*Chuckles*{/i} Like literally... it actually feels kinda nice."
#     hit "As if you're about to give me a full body Swedish massage."
#     pov "{i}*Pants*{/i} Hahaha! I can if you want."
#     pov "I hear sperm is great for the skin."
#     hit "I don't know what kinda person told you that."
#     hit "Everyone knows it's a great teeth whitener."
#     hit "Ugh- anyway. I gotta head back to the store, I can't leave those idiots in charge for too long."
#     hit "Be an angel and grab me a towel."
#     pov "It's the least I can do for you."
#     scene black
#     with fade
#     $ renpy.pause()
#     "After a bit of cleaning up..."
#     scene bg mylivingroom_day
#     with fade
#
#     $ hitomi_backroommatingpress = 0
#
#     jump lbl_mylivingroom_day_setup
