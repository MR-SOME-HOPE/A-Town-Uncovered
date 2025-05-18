## Alanna Cuddle Fuck
label lbl_alanna_cuddle_fuck_revisit:
    if hscene_xray == 0:
        scene bg alannacuddlefuck_1
        with fade
    else:
        scene bg alannacuddlefuck_1_0
        with fade

    jump lbl_alanna_cuddle_fuck_revisit_0

####################
## Cuddle Fuck Pussy Pre
label lbl_alanna_cuddle_fuck_revisit_0_0:
    "Error 'alannacuddle_pre'"

    jump lbl_alanna_cuddle_fuck_revisit_0

label lbl_alanna_cuddle_fuck_revisit_0:
    #$ alanna_cuddle_fuck_counter = 0
    if hscene_xray == 0:
        jump lbl_alanna_cuddle_fuck_revisit_1
    else:
        jump lbl_alanna_cuddle_fuck_revisit_1_0

####################
## Cuddle Fuck Stage 1
label lbl_alanna_cuddle_fuck_revisit_1:
    scene img_alanna_cuddle_fuck_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_1

image img_alanna_cuddle_fuck_stage_1:
    "bg alannacuddlefuck_1"
    pause 0.2
    "bg alannacuddlefuck_2"
    pause 0.2
    "bg alannacuddlefuck_3"
    pause 0.3
    "bg alannacuddlefuck_4"
    pause 0.3
    "bg alannacuddlefuck_2"
    pause 0.2
    repeat

####################
## Cuddle Fuck Stage 1 XRAY
label lbl_alanna_cuddle_fuck_revisit_1_0:
    scene img_alanna_cuddle_fuck_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_1_0

image img_alanna_cuddle_fuck_stage_1_0:
    "bg alannacuddlefuck_1_0"
    pause 0.2
    "bg alannacuddlefuck_2_0"
    pause 0.2
    "bg alannacuddlefuck_3_0"
    pause 0.3
    "bg alannacuddlefuck_4_0"
    pause 0.3
    "bg alannacuddlefuck_2_0"
    pause 0.2
    repeat
####################
## Cuddle Fuck Stage 2
label lbl_alanna_cuddle_fuck_revisit_2:
    scene img_alanna_cuddle_fuck_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_2

image img_alanna_cuddle_fuck_stage_2:
    "bg alannacuddlefuck_1"
    pause 0.2
    "bg alannacuddlefuck_2"
    pause 0.2
    "bg alannacuddlefuck_4"
    pause 0.3
    "bg alannacuddlefuck_2"
    pause 0.2
    repeat
####################
## Cuddle Fuck Stage 2 XRAY
label lbl_alanna_cuddle_fuck_revisit_2_0:
    scene img_alanna_cuddle_fuck_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_2_0

image img_alanna_cuddle_fuck_stage_2_0:
    "bg alannacuddlefuck_1_0"
    pause 0.2
    "bg alannacuddlefuck_2_0"
    pause 0.2
    "bg alannacuddlefuck_4_0"
    pause 0.3
    "bg alannacuddlefuck_2_0"
    pause 0.2
    repeat
####################
## Cuddle Fuck Stage 3
label lbl_alanna_cuddle_fuck_revisit_3:
    scene img_alanna_cuddle_fuck_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_3
image img_alanna_cuddle_fuck_stage_3:
    "bg alannacuddlefuck_1"
    pause 0.2
    "bg alannacuddlefuck_4"
    pause 0.2
    "bg alannacuddlefuck_2"
    pause 0.2
    repeat
####################
## Cuddle Fuck Stage 3 XRAY
label lbl_alanna_cuddle_fuck_revisit_3_0:
    scene img_alanna_cuddle_fuck_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_alanna_cuddle_fuck_revisit_3_0

image img_alanna_cuddle_fuck_stage_3_0:
    "bg alannacuddlefuck_1_0"
    pause 0.2
    "bg alannacuddlefuck_4_0"
    pause 0.2
    "bg alannacuddlefuck_2_0"
    pause 0.2
    repeat
####################
## Cuddle Fuck Cum
label lbl_alanna_cuddle_fuck_revisit_cum:
    jump lbl_alanna_cuddle_fuck_revisit_cum_2

label lbl_alanna_cuddle_fuck_revisit_cum_2:
    call screen scr_alanna_cuddle_fuck_revisit_cum_2

screen scr_alanna_cuddle_fuck_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_alanna_cuddle_fuck_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action If(hscene_xray == 0, Jump("lbl_alanna_cuddle_fuck_revisit_cumin"), Jump("lbl_alanna_cuddle_fuck_revisit_cumin_0"))

####################
## Cuddle Fuck Cum In
label lbl_alanna_cuddle_fuck_revisit_cumin:
    scene bg alannacuddlefuck_6_0
    $ renpy.pause(2,hard=True)
    show bg alannacuddlefuck_6_1
    $ renpy.pause()
    ala "Uhm... I feel really warm inside."
    pov "{i}*Pants*{/i}"
    pov "Good... glad I can help-"
    ala "Did you-?"
    pov "..."
    pov "Yeah but you feel much warmer, don't you?"
    ala "{i}*Sigh*{/i}"
    ala "Does sperm die in freezing cold conditions?"
    pov "I don't exactly know the science behind it."
    ala "Remind me to buy an after pill when we get out."
    pov "You're not mad?"
    ala "Don't push it."

    jump lbl_alanna_cuddle_fuck_revisit_post

####################
## Cuddle Fuck Cum In XRAY
label lbl_alanna_cuddle_fuck_revisit_cumin_0:
    scene bg alannacuddlefuck_5_0
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_1
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_2
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_3
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_4
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_5
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_6
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_7
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_8
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_9
    $ renpy.pause(0.3,hard=True)
    show bg alannacuddlefuck_5_10
    $ renpy.pause()
    ala "Uhm... I feel really warm inside."
    pov "{i}*Pants*{/i}"
    pov "Good... glad I can help-"
    ala "Did you-?"
    pov "..."
    pov "Yeah but you feel much warmer, don't you?"
    ala "{i}*Sigh*{/i}"
    ala "Does sperm die in freezing cold conditions?"
    pov "I don't exactly know the science behind it."
    ala "Remind me to buy an after pill when we get out."
    pov "You're not mad?"
    ala "Don't push it."

    jump lbl_alanna_cuddle_fuck_revisit_post

####################
## Cuddle Fuck Cum Out
label lbl_alanna_cuddle_fuck_revisit_cumout:
    "Error 'alannacuddle_out'"

    jump lbl_alanna_cuddle_fuck_revisit_post

####################
## Cuddle Fuck Next
label lbl_alanna_cuddle_fuck_revisit_next:
    "Error 'alannacuddle_next'"

    jump lbl_alanna_cuddle_fuck_revisit_post

####################
## Cuddle Fuck Post
label lbl_alanna_cuddle_fuck_revisit_post:
    scene black
    with fade
    "{i}*Creeeaak*{/i}"
    icman "Hey, are you guys al-"
    icman "Uhm... what are you too doing...?"
    ala "It's not what it looks like!"
    ala "We were just using each other's body heat for warmth-"
    icman "..."
    icman "Oh! I remember Barry Grills saying that in that one episode."
    pov "Yes! Barry Grills!"
    ala "Purely survival, I swear to God."
    ala "We would never otherwise do this, sir."
    pov "Yeah- wait- reall-"
    ala "Shush."
    icman "Look, I'll pretend that this didn't happen because..."
    icman "Well, let's be honest, no one needs to know my employees were trapped in a walk-in freezer."
    icman "One that I was meant to fix for a while."
    ala "A few years isn't a while, dude."
    icman "Look, get out of here before we all get trapped in."
    icman "Actually, get dressed first."
    icman "Wai- get out... first?"
    ala "We're going!"
    pov "Yeah- what she said."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
