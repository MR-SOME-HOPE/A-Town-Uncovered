####################
## Luna Doggy Bedroom
label lbl_luna_doggy_bedroom_revisit_0:
    jump lbl_luna_doggy_bedroom_revisit_1

####################
## Stage 1
label lbl_luna_doggy_bedroom_revisit_1:
    scene img_luna_doggy_bedroom_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_1

image img_luna_doggy_bedroom_stage_1:
    "bg lunadoggybedroom_1"
    pause 0.2
    "bg lunadoggybedroom_2"
    pause 0.2
    "bg lunadoggybedroom_3"
    pause 0.2
    "bg lunadoggybedroom_4"
    pause 0.2
    "bg lunadoggybedroom_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_luna_doggy_bedroom_revisit_2:
    scene img_luna_doggy_bedroom_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_2

image img_luna_doggy_bedroom_stage_2:
    "bg lunadoggybedroom_6"
    pause 0.2
    "bg lunadoggybedroom_8"
    pause 0.2
    "bg lunadoggybedroom_9"
    pause 0.2
    "bg lunadoggybedroom_10"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_luna_doggy_bedroom_revisit_3:
    scene img_luna_doggy_bedroom_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_revisit_3

image img_luna_doggy_bedroom_stage_3:
    "bg lunadoggybedroom_11"
    pause 0.2
    "bg lunadoggybedroom_13"
    pause 0.1
    "bg lunadoggybedroom_14"
    pause 0.1
    "bg lunadoggybedroom_15"
    pause 0.2
    repeat

####################
## Cum
label lbl_luna_doggy_bedroom_revisit_menu:
    jump lbl_luna_doggy_bedroom_revisit_menu_2

label lbl_luna_doggy_bedroom_revisit_menu_2:
    call screen scr_luna_doggy_bedroom_revisit_cum

screen scr_luna_doggy_bedroom_revisit_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_luna_doggy_bedroom_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_luna_doggy_bedroom_revisit_cumchoice")

label lbl_luna_doggy_bedroom_revisit_cumchoice:

    menu:
        "Cum inside":
            jump lbl_luna_doggy_bedroom_revisit_cumin

        "Cum on her":
            jump lbl_luna_doggy_bedroom_revisit_cumout

####################
## Cum In
label lbl_luna_doggy_bedroom_revisit_cumin:
    pov "Fuck- I'm gonna cum, Luna."
    lun "Cum!"
    lun "Cum for me, [povname]!"
    lun "I WANT YOUR CUM!"
    scene bg lunadoggybedroom_16_0
    $ renpy.pause(1.5,hard=True)
    show bg lunadoggybedroom_16_1
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_2
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_3
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_4
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_5
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_6
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_7
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_8
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_16_9
    $ renpy.pause(0.4,hard=True)
    pov "{i}*Huff huff*{/i}"
    lun "Oh my GOD! It's so fucking hot."
    lun "Your cum feels so good~"
    pov "You- you're not gonna get pregnant are you?"
    lun "Oh- we're for sure having a baby!"
    pov "Wait- wha-"
    lun "I'm kidding, I've got some Plan B."
    lun "You sounded so shook~ Hahahaha~"
    pov "Justified."
    lun "Alright, well. Do you have some tissues near by."
    lun "This was fun but I gotta meet up with someone."

    scene black
    with fade
    $ renpy.pause()
    "After a bit of cleaning up..."
    scene bg mybedroom_day
    with fade

    $ luna_doggybedroom = 0

    jump lbl_mybedroom_day_setup

####################
## Doggy Cum Out
label lbl_luna_doggy_bedroom_revisit_cumout:
    pov "Fuck- I'm gonna cum, Luna."
    lun "Cum!"
    lun "Cum for me, [povname]!"
    lun "I WANT YOUR CUM ALL OVER ME!"
    scene bg lunadoggybedroom_3
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_2
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_1
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_0
    $ renpy.pause(0.6,hard=True)
    show bg lunadoggybedroom_17_1
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_2
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_3
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_4
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_5
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_6
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_7
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_8
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_9
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_10
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_11
    $ renpy.pause(0.4,hard=True)
    show bg lunadoggybedroom_17_12
    $ renpy.pause(0.4,hard=True)

    pov "{i}*Huff huff*{/i}"
    lun "Oh my GOD! It's so fucking hot."
    lun "Your cum feels so good~"
    pov "You look good glazed."
    lun "Why thank you."
    lun "I'd turn around but I don't wanna get your bedsheets dirty."
    pov "I'll go grab something to clean up."
    lun "Well hurry up, I'm in the mood for a good rolling around."
    pov "No! Don't! HOLD ON!"

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
