####################
## Luna Doggy Bedroom
default luna_doggybedroom = 0

label lbl_luna_doggy_bedroom:
    ## PRE STORY
    show pov neutral_talk at left
    show lun neutral at right
    pov "Hey, Luna."
    show pov neutral
    show lun neutral_talk
    lun "Hey, [povname]. What's up on the agenda?"
    show pov smirk_talk
    show lun neutral
    pov "Wanted to see if you're free right now."
    show pov neutral
    show lun smirk_talk
    lun "You're in luck, lucky boy."
    show lun neutral_talk
    lun "My schedule is empty, well until later when I gotta meet up with a seller."
    show pov shocked
    show lun smirk_talk
    lun "New taxidermy patient."
    show pov embarrassed_talk
    show lun neutral
    pov "How- fun."
    show pov neutral_talk
    show lun confused
    pov "Speaking of fun."
    pov "You wanna stop by my place for a- beverage."
    show pov embarrassed
    lun "..."
    show pov neutral
    show lun neutral_talk
    lun "Down."
    lun "Why not, you live close to the cafe right?"
    show pov neutral_talk
    show lun neutral
    pov "Yup, just down the road."
    show pov neutral
    show lun smirk_talk
    lun "Easy then, that's my meet up spot."
    show lun neutral_talk
    lun "Let's go, [povname]."
    show pov neutral_talk
    show lun neutral
    pov "Sweet!"

    scene black with fade
    $ renpy.pause()
    "After walking together back home..."

    scene bg mybedroom_day
    with fade
    show pov neutral_talk at left
    show lun neutral at right
    with dissolve
    pov "Make yourself comfortable."
    show pov neutral
    show lun smirk_talk
    lun "What a cute room."
    show pov embarrassed
    lun "Soo- boyish."
    show pov embarrassed_talk
    show lun smirk
    pov "T-thanks?"
    show pov confused
    show lun smirk_talk
    lun "So, tell me [povname]."
    show pov shocked
    show lun smirk_talk
    lun "What do you intend to do with me now that I'm trapped in your room."
    show pov embarrassed_talk
    show lun smirk
    pov "Well-"
    show pov embarrassed
    show lun smirk_talk
    lun "Oh- and don't leave out any of the- juicy details~"

    scene black with fade
    $ renpy.pause()
    "Some juicy details later..."

    scene img_luna_doggy_bedroom_stage_1 with fade

    jump lbl_luna_doggy_bedroom_1

label lbl_luna_doggy_bedroom_0:
    jump lbl_luna_doggy_bedroom_1
    # if hscene_xray == 0:
    #     jump lbl_luna_doggy_bedroom_1
    # else:
    #     jump lbl_luna_doggy_bedroom_1_0

####################
## Stage 1
label lbl_luna_doggy_bedroom_1:
    scene img_luna_doggy_bedroom_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_doggy_bedroom_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_doggy_bedroom_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_1

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
label lbl_luna_doggy_bedroom_2:
    scene img_luna_doggy_bedroom_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_doggy_bedroom_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_doggy_bedroom_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_2

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
label lbl_luna_doggy_bedroom_3:
    scene img_luna_doggy_bedroom_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_doggy_bedroom_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_doggy_bedroom_3

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
label lbl_luna_doggy_bedroom_menu:
    jump lbl_luna_doggy_bedroom_menu_2

label lbl_luna_doggy_bedroom_menu_2:
    call screen scr_luna_doggy_bedroom_cum

screen scr_luna_doggy_bedroom_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_luna_doggy_bedroom_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_luna_doggy_bedroom_cumchoice")

label lbl_luna_doggy_bedroom_cumchoice:

    menu:
        "Cum inside":
            jump lbl_luna_doggy_bedroom_cumin
            # if hscene_xray == 0:
            #     jump lbl_luna_doggy_bedroom_cumin
            # else:
            #     jump lbl_luna_doggy_bedroom_cumin_0
        "Cum on her":
            jump lbl_luna_doggy_bedroom_cumout

####################
## Cum In
label lbl_luna_doggy_bedroom_cumin:
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
label lbl_luna_doggy_bedroom_cumout:
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
    "After a bit of cleaning up..."
    scene bg mybedroom_day
    with fade

    $ luna_doggybedroom = 0

    jump lbl_mybedroom_day_setup
