####################
## Lashley Bent Over
default lashley_bentoverdesk = 0

label lbl_lashley_bent_over_desk:
    ## PRE STORY
    show pov neutral at left
    show pri sad at right
    pov "Hey, Ms Lashley."
    pov "You busy?"
    show pov neutral
    show pri sad_talk
    pri "Ughhh- a little swamped. Yes."
    show pov confused_talk
    show pri sad
    pov "When's the last time you took a break?"
    show pov confused
    show pri sad_talk
    pri "I don't know, I prayed this morning?"
    show pov confused_talk
    show pri sad
    pov "That doesn't really count."
    show pov confused
    show pri sad_talk
    pri "Well, I don't know, [povname]."
    show pov confused
    show pri bored_talk
    pri "I don't really have time to answer your questions, you know?"
    show pov smirk_talk
    show pri bored
    pov "I can help you de-stress."
    show pov shocked
    show pri angry_talk
    pri "I'M NOT STRESSED!"
    show pri angry
    pov "..."
    show pov shocked
    show pri sad_talk
    pri "{i}*Sigh*{/i}"
    show pov embarrassed
    pri "Sorry I snapped."
    show pov embarrassed_talk
    show pri embarrassed
    pov "C'mon... you know you want to."
    show pov smirk
    pri "..."
    show pri embarrassed_talk
    pri "Maybe... it's a good idea."

    scene black with fade
    $ renpy.pause()

    scene img_lashley_bent_over_desk_stage_1 with fade

    jump lbl_lashley_bent_over_desk_1

label lbl_lashley_bent_over_desk_0:
    jump lbl_lashley_bent_over_desk_1
    # if hscene_xray == 0:
    #     jump lbl_lashley_bent_over_desk_1
    # else:
    #     jump lbl_lashley_bent_over_desk_1_0

####################
## Stage 1
label lbl_lashley_bent_over_desk_1:
    scene img_lashley_bent_over_desk_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_bent_over_desk_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_bent_over_desk_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_1

image img_lashley_bent_over_desk_stage_1:
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
label lbl_lashley_bent_over_desk_2:
    scene img_lashley_bent_over_desk_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_bent_over_desk_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_bent_over_desk_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_2

image img_lashley_bent_over_desk_stage_2:
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
label lbl_lashley_bent_over_desk_3:
    scene img_lashley_bent_over_desk_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_bent_over_desk_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_bent_over_desk_3

image img_lashley_bent_over_desk_stage_3:
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
label lbl_lashley_bent_over_desk_menu:
    jump lbl_lashley_bent_over_desk_menu_2

label lbl_lashley_bent_over_desk_menu_2:
    call screen scr_lashley_bent_over_desk_cum

screen scr_lashley_bent_over_desk_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashley_bent_over_desk_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashley_bent_over_desk_cumchoice")

label lbl_lashley_bent_over_desk_cumchoice:
    jump lbl_lashley_bent_over_desk_cumin
    # menu:
    #     "Cum inside":
    #         if hscene_xray == 0:
    #             jump lbl_lashley_bent_over_desk_cumin
    #         else:
    #             jump lbl_lashley_bent_over_desk_cumin_0
    #     "Cum on her":
    #         jump lbl_lashley_bent_over_desk_cumout

####################
## Cum In
label lbl_lashley_bent_over_desk_cumin:
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
    "After a bit of cleaning up..."
    scene bg principaloffice_day
    with fade

    $ lashley_bentoverdesk = 0

    jump lbl_principaloffice_day_setup
