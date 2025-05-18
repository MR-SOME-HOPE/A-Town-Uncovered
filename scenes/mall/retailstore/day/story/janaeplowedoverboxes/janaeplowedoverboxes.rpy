## Janae Plowed Over Boxes
label lbl_janae_plowed_over_boxes:
    ## PRE STORY
    show pov smirk_talk at left
    show jan confused at right
    pov "When's your break? I'm hoping we could get to know each other a little more."
    show pov smirk
    show jan smirk
    jan "Hmmm~"
    show pov confused
    show jan smirk_talk
    jan "You know what? I actually need to check on some inventory in the back if you- wanna meet me there."
    show pov confused_talk
    show jan smirk
    pov "Am I allowed in the backrooms?"
    show pov smirk
    show jan smirk_talk
    jan "Technically no but, that won't stop you. Will it?"
    show pov smirk_talk
    show jan smirk
    pov "Hehe, nope."
    show pov neutral
    show jan neutral_talk
    jan "Figured."
    show pov smirk
    show jan smirk_talk
    jan "Well, I'll meet you there?"
    show pov neutral_talk
    show jan smirk
    pov "Sure."
    show pov smirk
    show jan confused_talk
    jan "Don't be too obvious."

    scene black
    with fade
    $ renpy.pause()
    "After sneaking into the backrooms..."

    jump lbl_janae_plowed_over_boxes_0

label lbl_janae_plowed_over_boxes_0:
    # if hscene_xray == 0:
    #     jump lbl_janae_plowed_over_boxes_1
    # else:
    #     jump lbl_janae_plowed_over_boxes_1_0

    scene bg janaeplowedoverboxes_1
    with fade

    jump lbl_janae_plowed_over_boxes_1

####################
## Stage 1
label lbl_janae_plowed_over_boxes_1:
    scene img_janae_plowed_over_boxes_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_janae_plowed_over_boxes_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_janae_plowed_over_boxes_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_janae_plowed_over_boxes_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_janae_plowed_over_boxes_1

image img_janae_plowed_over_boxes_stage_1:
    "bg janaeplowedoverboxes_1"
    pause 0.2
    "bg janaeplowedoverboxes_2"
    pause 0.2
    "bg janaeplowedoverboxes_3"
    pause 0.2
    "bg janaeplowedoverboxes_4"
    pause 0.2
    "bg janaeplowedoverboxes_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_janae_plowed_over_boxes_2:
    scene img_janae_plowed_over_boxes_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_janae_plowed_over_boxes_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_janae_plowed_over_boxes_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_janae_plowed_over_boxes_2

image img_janae_plowed_over_boxes_stage_2:
    "bg janaeplowedoverboxes_6"
    pause 0.2
    "bg janaeplowedoverboxes_8"
    pause 0.2
    "bg janaeplowedoverboxes_9"
    pause 0.2
    "bg janaeplowedoverboxes_10"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_janae_plowed_over_boxes_3:
    scene img_janae_plowed_over_boxes_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_janae_plowed_over_boxes_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_janae_plowed_over_boxes_3

image img_janae_plowed_over_boxes_stage_3:
    "bg janaeplowedoverboxes_11"
    pause 0.2
    "bg janaeplowedoverboxes_14"
    pause 0.2
    "bg janaeplowedoverboxes_15"
    pause 0.2
    repeat

####################
## Cum
label lbl_janae_plowed_over_boxes_menu:
    call screen scr_janae_plowed_over_boxes_menu

screen scr_janae_plowed_over_boxes_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_janae_plowed_over_boxes_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_janae_plowed_over_boxes_cum")

label lbl_janae_plowed_over_boxes_cum:
    pov "Oh fuck- I'm gonna cum, Jan."
    menu:
        "Cum inside":
            jan "Oh shit- um, just do it inside!"
            jan "Don't leave any evidence."
            pov "Mhmm- okay-"
            jump lbl_janae_plowed_over_boxes_cumin

        "Cum outside":
            jan "Oh shit- um pull out!"
            jan "I'm not on any pills."
            pov "Mhmm- okay-"
            jump lbl_janae_plowed_over_boxes_cumout

####################
## CUM IN
label lbl_janae_plowed_over_boxes_cumin:
    scene bg janaeplowedoverboxes_9
    $ renpy.pause(1.5,hard=True)
    show bg janaeplowedoverboxes_17_1
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_17_2
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_17_3
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_17_4
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_17_5
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_17_6
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_17_7
    $ renpy.pause()
    jan "Oh- my god."
    jan "Oh my god oh my god."
    pov "{i}*Huff huff*{/i}"
    jan "Fuck- is it dripping?"
    pov "Mmmm- I think so, a little."
    jan "{i}*Pants*{/i} God- I'll have to do a little clean up anyway..."
    pov "Sorry"
    jan "It's fine, [povname]. I had fun."
    pov "Me too, Janae."
    pov "Wanna go again?"
    jan "I have to get back to work. Maybe another time."
    pov "Alright."

    scene black
    with fade
    $ renpy.pause()
    "After leaving the crime scene..."

    $ gtime += 1

    if gtime <= 1:
        scene bg mall_day
        with fade

        jump lbl_mall_day_setup

    else:
        scene bg townmap_night
        with fade

        jump lbl_townmap_setup

####################
## CUM OUT
label lbl_janae_plowed_over_boxes_cumout:
    scene bg janaeplowedoverboxes_6
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_0
    $ renpy.pause(0.5,hard=True)
    show bg janaeplowedoverboxes_16_1
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_2
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_3
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_4
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_5
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_6
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_7
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_8
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_9
    $ renpy.pause(0.3,hard=True)
    show bg janaeplowedoverboxes_16_10
    $ renpy.pause()
    jan "Oh- my god."
    jan "Oh my god oh my god."
    pov "{i}*Huff huff*{/i}"
    jan "Where- did you cum?"
    pov "I pulled out, don't worry."
    jan "Wait- did you hit the box?"
    pov "Uhhmmmmmmm"
    jan "Oh- fuck."
    jan "That's gonna soak in."
    jan "I better take whatever is in here and dispose of the box."
    pov "Sorry... I should've aimed at the floor."
    jan "It's fine. I had fun."
    pov "Me too, Janae."
    pov "Wanna go again?"
    jan "I have to get back to work. Maybe another time."
    pov "Alright."

    scene black
    with fade
    $ renpy.pause()
    "After leaving the crime scene..."

    $ gtime += 1

    if gtime <= 1:
        scene bg mall_day
        with fade

        jump lbl_mall_day_setup

    else:
        scene bg townmap_night
        with fade

        jump lbl_townmap_setup
