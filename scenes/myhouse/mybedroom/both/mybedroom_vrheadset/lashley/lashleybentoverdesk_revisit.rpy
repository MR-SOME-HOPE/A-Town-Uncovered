####################
## Lashley Bent Over
label lbl_lashley_bent_over_desk_revisit_0:
    jump lbl_lashley_bent_over_desk_revisit_1

####################
## Stage 1
label lbl_lashley_bent_over_desk_revisit_1:
    scene img_lashley_bent_over_desk_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_1

image img_lashley_bent_over_desk_revisit_stage_1:
    "bg lashleybentoverdesk_1"
    pause 0.2
    "bg lashleybentoverdesk_2"
    pause 0.2
    "bg lashleybentoverdesk_3"
    pause 0.2
    "bg lashleybentoverdesk_4"
    pause 0.2
    "bg lashleybentoverdesk_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_lashley_bent_over_desk_revisit_2:
    scene img_lashley_bent_over_desk_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_2

image img_lashley_bent_over_desk_revisit_stage_2:
    "bg lashleybentoverdesk_1"
    pause 0.2
    "bg lashleybentoverdesk_3"
    pause 0.2
    "bg lashleybentoverdesk_4"
    pause 0.2
    "bg lashleybentoverdesk_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_lashley_bent_over_desk_revisit_3:
    scene img_lashley_bent_over_desk_revisit_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_revisit_3

image img_lashley_bent_over_desk_revisit_stage_3:
    "bg lashleybentoverdesk_1"
    pause 0.2
    "bg lashleybentoverdesk_3"
    pause 0.1
    "bg lashleybentoverdesk_4"
    pause 0.1
    "bg lashleybentoverdesk_5"
    pause 0.2
    repeat

####################
## Cum
label lbl_lashley_bent_over_desk_revisit_menu:
    jump lbl_lashley_bent_over_desk_revisit_menu_2

label lbl_lashley_bent_over_desk_revisit_menu_2:
    call screen scr_lashley_bent_over_desk_revisit_cum

screen scr_lashley_bent_over_desk_revisit_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashley_bent_over_desk_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashley_bent_over_desk_revisit_cumchoice")

label lbl_lashley_bent_over_desk_revisit_cumchoice:
    jump lbl_lashley_bent_over_desk_revisit_cumin

####################
## Cum In
label lbl_lashley_bent_over_desk_revisit_cumin:
    pov "I'm gonna cum-"
    pri "Do it inside me, [povname]."
    pri "We must've make a mess in my office."
    pov "O-"
    pov "Okay-"
    pov "{i}*Muffled wince*{/i}"
    pov "Gaahhghh-!"
    show bg lashleybentoverdesk_3
    show white
    $ renpy.pause(1.5,hard=True)
    hide white with dissolve
    show bg lashleybentoverdesk_6_1
    $ renpy.pause(0.4,hard=True)
    show bg lashleybentoverdesk_6_2
    $ renpy.pause(0.4,hard=True)
    show bg lashleybentoverdesk_6_3
    $ renpy.pause(0.4,hard=True)
    show bg lashleybentoverdesk_6_4
    $ renpy.pause(0.5,hard=True)
    pov "Oh f-"
    pri "Ah- [povname]!"
    pov "Oh- fuuuun~"
    pov "Praise the Lord!"
    pov "{i}*Huff huff*{/i} Heheh~"
    pri "Oh, shut up."
    pri "Quick, grab some tissues and clean us up."
    pri "I need to get some stuff done."
    pov "Alright. Hang on."

    scene black
    with fade
    $ renpy.pause()
    
    jump lbl_vrheadset_character_selection
