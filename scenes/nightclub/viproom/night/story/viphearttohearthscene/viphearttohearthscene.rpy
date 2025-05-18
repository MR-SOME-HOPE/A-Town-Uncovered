## VIP Heart To Heart H-Scene

default viphearttohearthscene = 0

label lbl_vip_heart_to_heart_hscene:
    ## PRE STORY

label lbl_vip_heart_to_heart_hscene_0:
    jump lbl_vip_heart_to_heart_hscene_1
    # if hscene_xray == 0:
    #     jump lbl_vip_heart_to_heart_hscene_1
    # else:
    #     jump lbl_vip_heart_to_heart_hscene_1_0

####################
## Stage 1
label lbl_vip_heart_to_heart_hscene_1:
    scene img_vip_heart_to_heart_hscene_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_vip_heart_to_heart_hscene_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_vip_heart_to_heart_hscene_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_vip_heart_to_heart_hscene_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_vip_heart_to_heart_hscene_1

image img_vip_heart_to_heart_hscene_stage_1:
    "bg viphearttohearthscene_1"
    pause 0.2
    "bg viphearttohearthscene_2"
    pause 0.2
    "bg viphearttohearthscene_3"
    pause 0.2
    "bg viphearttohearthscene_4"
    pause 0.2
    "bg viphearttohearthscene_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_vip_heart_to_heart_hscene_2:
    scene img_vip_heart_to_heart_hscene_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_vip_heart_to_heart_hscene_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_vip_heart_to_heart_hscene_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_vip_heart_to_heart_hscene_2

image img_vip_heart_to_heart_hscene_stage_2:
    "bg viphearttohearthscene_6"
    pause 0.2
    "bg viphearttohearthscene_8"
    pause 0.2
    "bg viphearttohearthscene_9"
    pause 0.2
    "bg viphearttohearthscene_10"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_vip_heart_to_heart_hscene_3:
    scene img_vip_heart_to_heart_hscene_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_vip_heart_to_heart_hscene_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_vip_heart_to_heart_hscene_3

image img_vip_heart_to_heart_hscene_stage_3:
    "bg viphearttohearthscene_11"
    pause 0.2
    "bg viphearttohearthscene_13"
    pause 0.2
    "bg viphearttohearthscene_15"
    pause 0.2
    repeat

####################
## Cum
label lbl_vip_heart_to_heart_hscene_menu:
    call screen scr_vip_heart_to_heart_hscene_menu

screen scr_vip_heart_to_heart_hscene_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_vip_heart_to_heart_hscene_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_vip_heart_to_heart_hscene_cumchoice")

label lbl_vip_heart_to_heart_hscene_cumchoice:
    jump lbl_vip_heart_to_heart_hscene_cumin
    # menu:
    #     "Cum inside":
    #         if hscene_xray == 0:
    #             jump lbl_vip_heart_to_heart_hscene_cumin
    #         else:
    #             jump lbl_vip_heart_to_heart_hscene_cumin_0
    #     "Cum on her":
    #         jump lbl_vip_heart_to_heart_hscene_cumout

####################
## Cum In
label lbl_vip_heart_to_heart_hscene_cumin:
    scene bg viphearttohearthscene_9
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
    hit "Oh wow- {i}*pants*{/i}"
    hit "You really just came inside, huh?"
    pov "Sorry, I couldn't help myself."
    pov "{i}*pants*{/i} Your pussy was just too fucking good, Hitomi."
    hit "Mmm... {i}*exhale*{/i} It's okay, [povname]."
    hit "I was really hoping you'd give me your cum."
    hit "I wanted it inside me, I wanted to feel it so bad."
    hit "Can't we stay like this a little longer?"
    pov "I'm worried someone might come check in on us to make sure we're not doing-"
    pov "Exactly this..."
    hit "{i}*Sigh*{/i} You're right."
    hit "I don't wanna get blacklisted-"
    hit "Alright, let's clean up."
    scene black
    with fade
    $ renpy.pause()
    "After a bit of cleaning up and parting ways for the night..."
    scene bg townmap_night
    with fade

    $ viphearttohearthscene = 0

    jump lbl_townmap_setup
