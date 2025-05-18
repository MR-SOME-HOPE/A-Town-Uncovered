####################
## Zariah Stage Reverse Cowgirl
#default zariah_stage_reverse_cowgirl_counter = 0

label lbl_zariah_stage_reverse_cowgirl:
    ## PRE STORY
    show pov neutral_talk at left
    show zar neutral at right
    call lbl_dancefloor_counter_check
    pov "Yo, Zar!"
    show pov neutral at left
    show zar neutral_talk at right
    zar "Yooo!"
    show pov smirk_talk at left
    show zar confused at right
    pov "You free later?"
    show pov shocked at left
    show zar shocked_talk at right
    zar "You're gonna have to shout in my ear!"
    show pov shocked_talk at left
    show zar neutral at right
    pov "I said are you free later?!"
    show pov neutral at left
    show zar smirk_talk at right
    zar "I'm here all night, baby!"
    show pov embarrassed_talk at left
    show zar confused at right
    pov "I was hoping we could have some fun!"
    show pov shocked at left
    show zar smirk_talk at right
    zar "You talking like a date or sex?"
    zar "Or both!"
    show pov embarrassed_talk at left
    show zar neutral at right
    pov "Uhmm-"
    show pov shocked at left
    show zar shocked_talk at right
    zar "Cause' I could use a quick fuck right about now!"
    show pov shocked_talk at left
    show zar neutral at right
    pov "OH!"
    show zar smirk at right
    pov "Oh-!"
    show pov neutral_talk at left
    show zar neutral at right
    pov "I- we can-"
    show pov confused_talk at left
    show zar smirk at right
    pov "Where?"
    show pov shocked at left
    show zar neutral_talk at right
    zar "Right here, dude!"
    zar "Take your pants off and take a seat!"
    show pov shocked_talk at left
    show zar smirk at right
    pov "Oh my God- you're actually for real!"
    show pov shocked at left
    show zar smirk_talk at right
    zar "Don't worry! No one can tell, I do this all the time!"
    show pov smirk_talk at left
    show zar neutral at right
    pov "If you say so!"

    jump lbl_zariah_stage_reverse_cowgirl_0

label lbl_zariah_stage_reverse_cowgirl_0:
    if hscene_xray == 0:
        scene bg zariahstagereversecowgirl_1
        with fade
        jump lbl_zariah_stage_reverse_cowgirl_1
    else:
        scene bg zariahstagereversecowgirl_1_0
        with fade
        jump lbl_zariah_stage_reverse_cowgirl_1_0

####################
## Stage 1
label lbl_zariah_stage_reverse_cowgirl_1:
    scene img_zariah_stage_reverse_cowgirl_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_1

image img_zariah_stage_reverse_cowgirl_stage_1:
    "bg zariahstagereversecowgirl_1"
    pause 0.2
    "bg zariahstagereversecowgirl_2"
    pause 0.2
    "bg zariahstagereversecowgirl_3"
    pause 0.2
    "bg zariahstagereversecowgirl_4"
    pause 0.2
    "bg zariahstagereversecowgirl_5"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_zariah_stage_reverse_cowgirl_1_0:
    scene img_zariah_stage_reverse_cowgirl_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_1_0

image img_zariah_stage_reverse_cowgirl_stage_1_0:
    "bg zariahstagereversecowgirl_1_0"
    pause 0.2
    "bg zariahstagereversecowgirl_2_0"
    pause 0.2
    "bg zariahstagereversecowgirl_3_0"
    pause 0.2
    "bg zariahstagereversecowgirl_4_0"
    pause 0.2
    "bg zariahstagereversecowgirl_5_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_zariah_stage_reverse_cowgirl_2:
    scene img_zariah_stage_reverse_cowgirl_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_2

image img_zariah_stage_reverse_cowgirl_stage_2:
    "bg zariahstagereversecowgirl_6"
    pause 0.2
    "bg zariahstagereversecowgirl_7"
    pause 0.1
    "bg zariahstagereversecowgirl_9"
    pause 0.2
    "bg zariahstagereversecowgirl_10"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_zariah_stage_reverse_cowgirl_2_0:
    scene img_zariah_stage_reverse_cowgirl_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_2_0

image img_zariah_stage_reverse_cowgirl_stage_2_0:
    "bg zariahstagereversecowgirl_6_0"
    pause 0.2
    "bg zariahstagereversecowgirl_7_0"
    pause 0.1
    "bg zariahstagereversecowgirl_9_0"
    pause 0.2
    "bg zariahstagereversecowgirl_10_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_zariah_stage_reverse_cowgirl_3:
    scene img_zariah_stage_reverse_cowgirl_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_3

image img_zariah_stage_reverse_cowgirl_stage_3:
    "bg zariahstagereversecowgirl_11"
    pause 0.2
    "bg zariahstagereversecowgirl_14"
    pause 0.2
    "bg zariahstagereversecowgirl_15"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_zariah_stage_reverse_cowgirl_3_0:
    scene img_zariah_stage_reverse_cowgirl_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_3_0

image img_zariah_stage_reverse_cowgirl_stage_3_0:
    "bg zariahstagereversecowgirl_11_0"
    pause 0.2
    "bg zariahstagereversecowgirl_14_0"
    pause 0.2
    "bg zariahstagereversecowgirl_15_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_zariah_stage_reverse_cowgirl_menu:
    call screen scr_zariah_stage_reverse_cowgirl_menu

screen scr_zariah_stage_reverse_cowgirl_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariah_stage_reverse_cowgirl_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action If(hscene_xray == 0, Jump("lbl_zariah_stage_reverse_cowgirl_cumin"), Jump("lbl_zariah_stage_reverse_cowgirl_cumin_0"))
# label lbl_zariah_stage_reverse_cowgirl_cumchoice:
#     menu:
#         "Cum inside":
#             if hscene_xray == 0:
#                 jump lbl_zariah_stage_reverse_cowgirl_cumin
#             else:
#                 jump lbl_zariah_stage_reverse_cowgirl_cumin_0
#         "Cum on her":
#             jump lbl_zariah_stage_reverse_cowgirl_cumout

####################
## Cum In
label lbl_zariah_stage_reverse_cowgirl_cumin:
    pov "I'm- gonna cum-"
    zar "..."
    pov "Zar-! I'm gonna cum-"
    zar "Huh-?"
    zar "I can't- what-?"
    pov "Zar!!"
    scene bg zariahstagereversecowgirl_8
    $ renpy.pause(1.5,hard=True)
    show bg zariahstagereversecowgirl_16_1
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_16_2
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_16_3
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_16_4
    zar "Oh- [povname]! Did you just-?"
    pov "{i}*Huffs*{/i} I'm sorry- I tried to warn you."
    zar "It's okay!"
    zar "I prefer it this way!"
    zar "My boss would kill me if I made a mess on the equipment!"
    pov "Are you safe?"
    zar "Yeah, I'm taking shit, don't worry about it, dude!"
    zar "Nice fuck sesh!"
    pov "Thanks, you too! Riding to the beat is a really immersive experience!"
    zar "I'm glad you think so too!"
    zar "There should be some paper rolls on the floor! Clean us up but don't make it obvious!"
    pov "Gotcha!"
    scene black
    with fade
    $ renpy.pause()
    "After a bit of stealthy cleaning up..."
    scene bg nightclubdancefloor_night
    with fade

    jump lbl_nightclubdancefloor_night

####################
## Cum In XRAY
label lbl_zariah_stage_reverse_cowgirl_cumin_0:
    pov "I'm- gonna cum-"
    zar "..."
    pov "Zar-! I'm gonna cum-"
    zar "Huh-?"
    zar "I can't- what-?"
    pov "Zar!!"
    scene bg zariahstagereversecowgirl_8_0
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_1
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_2
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_3
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_4
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_5
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_6
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_7
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_8
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_9
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_10
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_11
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_12
    zar "Oh- [povname]! Did you just-?"
    pov "{i}*Huffs*{/i} I'm sorry- I tried to warn you."
    zar "It's okay!"
    zar "I prefer it this way!"
    zar "My boss would kill me if I made a mess on the equipment!"
    pov "Are you safe?"
    zar "Yeah, I'm taking shit, don't worry about it, dude!"
    zar "Nice fuck sesh!"
    pov "Thanks, you too! Riding to the beat is a really immersive experience!"
    zar "I'm glad you think so too!"
    zar "There should be some paper rolls on the floor! Clean us up but don't make it obvious!"
    pov "Gotcha!"
    scene black
    with fade
    $ renpy.pause()
    "After a bit of stealthy cleaning up..."
    scene bg nightclubdancefloor_night
    with fade

    jump lbl_nightclubdancefloor_night
