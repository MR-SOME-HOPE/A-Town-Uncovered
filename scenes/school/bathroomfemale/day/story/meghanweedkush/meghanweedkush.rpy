####################
## Meghan Weed Kush
default had_meg_weed_kush = 0

####################
## Pre
label lbl_meghan_weed_kush:
    scene bg schoolhallway1_day
    show btn schoolhallway1_day_zariah_idle
    $ renpy.pause(0.001)

    scene bg schoolbathroomfemale_day
    show meg smirk at right
    with fade

    show pov neutral at left
    with dissolve

    show meg shocked_talk

    #"You see Meghan smoking."
    meg "Oh fuck-"
    show meg angry_talk
    show pov confused
    meg "What the fuck are you doing here?"
    show pov shocked
    show meg angry
    pov "{i}*Sniff*{/i}"
    show meg embarrassed
    show pov smirk_talk
    pov "Is that..."
    show pov smirk
    show meg angry_talk
    meg "Yes, it's pot, you little shit."
    meg "Don't be a fucking snitch."
    show meg angry
    show pov shocked_talk
    pov "Don't worry, I ain't no rat."
    show pov neutral_talk
    show meg confused
    pov "Just prove to me that you know my name and we'll call it a fair deal."
    show pov neutral
    show meg embarrassed
    meg "..."
    if had_meg_weed_kush == 1:
        show pov bored_talk
        show meg bored
        pov "Seriously? Still can't remember after last time?"
        show pov shocked
        show meg bored_talk
        meg "I'll let you fuck me again."
    else:
        show pov shocked
        show meg bored_talk
        meg "I'll let you fuck me."
    show meg bored

    menu:
        "Fuck yeah":
            $ had_meg_weed_kush = 1
            show pov smirk_talk
            show meg sad
            pov "You've got a deal, missy."

            scene black with fade

            jump lbl_meghan_weed_kush_0

        "Nah, you're good":
            $ had_meg_weed_kush = 1
            show pov bored_talk
            show meg confused
            pov "Nah, don't worry. I'm not in the mood."
            pov "I'll keep your little secret for now."
            show pov neutral
            meg "..."
            show meg bored_talk
            show pov confused
            meg "A little privacy, please. I can't having you standing there staring at me."

            jump lbl_schoolhallway1_day_setup

## RESET
label lbl_meghan_weed_kush_0:
    jump lbl_meghan_weed_kush_1

####################
## Stage 1
label lbl_meghan_weed_kush_1:
    scene img_meghan_weed_kush_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_meghan_weed_kush_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_meghan_weed_kush_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_1

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
label lbl_meghan_weed_kush_2:
    scene img_meghan_weed_kush_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_meghan_weed_kush_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_meghan_weed_kush_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_2

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
label lbl_meghan_weed_kush_3:
    scene img_meghan_weed_kush_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_meghan_weed_kush_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_meghan_weed_kush_3

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
label lbl_meghan_weed_kush_cum:
    jump lbl_meghan_weed_kush_cum_2

label lbl_meghan_weed_kush_cum_2:
    call screen scr_meghan_weed_kush_cum_2

screen scr_meghan_weed_kush_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meghan_weed_kush_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meghan_weed_kush_cumin")

####################
## Cum In
label lbl_meghan_weed_kush_cumin:
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

    jump lbl_schoolhallway1_day_setup
