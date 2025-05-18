####################
## Meghan Weed Kush
label lbl_meghan_weed_kush_revisit_0:
    jump lbl_meghan_weed_kush_revisit_1

####################
## Stage 1
label lbl_meghan_weed_kush_revisit_1:
    scene img_meghan_weed_kush_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_meghan_weed_kush_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_meghan_weed_kush_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_revisit_1

image img_meghan_weed_kush_stage_1:
    "bg meghanweedkush_1"
    pause 0.2
    "bg meghanweedkush_2"
    pause 0.2
    "bg meghanweedkush_3"
    pause 0.2
    "bg meghanweedkush_4"
    pause 0.2
    "bg meghanweedkush_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_meghan_weed_kush_revisit_2:
    scene img_meghan_weed_kush_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_meghan_weed_kush_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_meghan_weed_kush_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_revisit_2

image img_meghan_weed_kush_stage_2:
    "bg meghanweedkush_1"
    pause 0.2
    "bg meghanweedkush_2"
    pause 0.2
    "bg meghanweedkush_4"
    pause 0.2
    "bg meghanweedkush_2"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_meghan_weed_kush_revisit_3:
    scene img_meghan_weed_kush_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_meghan_weed_kush_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_revisit_3

image img_meghan_weed_kush_stage_3:
    "bg meghanweedkush_1"
    pause 0.1
    "bg meghanweedkush_4"
    pause 0.1
    "bg meghanweedkush_2"
    pause 0.2
    repeat

####################
## Cum
label lbl_meghan_weed_kush_revisit_cum:
    jump lbl_meghan_weed_kush_revisit_cum_2

label lbl_meghan_weed_kush_revisit_cum_2:
    call screen scr_meghan_weed_kush_revisit_cum_2

screen scr_meghan_weed_kush_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meghan_weed_kush_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meghan_weed_kush_revisit_cumin")

####################
## Cum In
label lbl_meghan_weed_kush_revisit_cumin:
    pov "Meghan- I'm gonn-"
    meg "Cum inside me! I don't want your fuckin cum staining my cashmere."
    pov "Whatever you say, princess."
    scene bg meghanweedkush_2
    $ renpy.pause(0.2,hard=True)
    show bg meghanweedkush_3
    $ renpy.pause(0.2,hard=True)
    show bg meghanweedkush_4
    $ renpy.pause(0.6,hard=True)
    show bg meghanweedkush_5_1
    $ renpy.pause(0.5,hard=True)
    show bg meghanweedkush_5_2
    $ renpy.pause(0.4,hard=True)
    show bg meghanweedkush_5_3
    $ renpy.pause(0.4,hard=True)
    meg "{i}*Sigh*{/i}"
    meg "You pleb. You better not kiss and tell."
    pov "I would {i}never{/i}."
    meg "And hush hush on the kush kush."
    pov "Gotcha gotcha."
    pov "Welp..."
    pov "Pleasure doing business with you."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
