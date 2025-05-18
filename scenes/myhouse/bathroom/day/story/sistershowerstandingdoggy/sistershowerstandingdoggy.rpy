## Sister Shower Standing Doggy
label lbl_sister_shower_standing_doggy:
    #default sister_shower_standing_doggy_counter = 0

    jump lbl_sister_shower_standing_doggy_pre

####################
## Pre Dialogue
label lbl_sister_shower_standing_doggy_pre:
    if hscene_xray == 0:
        scene bg sistershowerstandingdoggy_1
        with hpunch
    else:
        scene bg sistershowerstandingdoggy_1_0
        with hpunch
    sis "Ah- that was quick-"
    sis "Already sticking it inside me?"
    pov "You looked so wet, I couldn't resist."
    sis "I'm taking a shower. Of course I'm wet."
    pov "Shh- shhh- shhh"
    if hscene_xray == 0:
        show bg sistershowerstandingdoggy_1
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_2
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_3
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_4
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_2
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_1
    else:
        show bg sistershowerstandingdoggy_1_0
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_2_0
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_3_0
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_4_0
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_2_0
        $ renpy.pause(0.3,hard=True)
        show bg sistershowerstandingdoggy_1_0
    sis "{i}*Moans*{/i}"
    pov "I just wanna hear you moan."
    sis "Mmm~ Keep going then.."

    jump lbl_sister_shower_standing_doggy_0

label lbl_sister_shower_standing_doggy_0:
    #$ sister_shower_standing_doggy_counter = 0
    if hscene_xray == 0:
        jump lbl_sister_shower_standing_doggy_1
    else:
        jump lbl_sister_shower_standing_doggy_1_0

####################
## Stage 1
label lbl_sister_shower_standing_doggy_1:
    scene img_sister_shower_standing_doggy_stage_1
    #$ sister_shower_standing_doggy_counter += 1
    #show bg sistershowerstandingdoggy_1
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_2
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_3
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_4
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and sister_shower_standing_doggy_counter == 4:
    #    jump lbl_sister_shower_standing_doggy_cum
    #elif skill_sta <= 14 and sister_shower_standing_doggy_counter == 6:
    #    jump lbl_sister_shower_standing_doggy_2
    #elif skill_sta <= 20 and sister_shower_standing_doggy_counter == 8:
    #    jump lbl_sister_shower_standing_doggy_2
    #else:
    #    jump lbl_sister_shower_standing_doggy_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sister_shower_standing_doggy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sister_shower_standing_doggy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_1

image img_sister_shower_standing_doggy_stage_1:
    "bg sistershowerstandingdoggy_1"
    pause 0.2
    "bg sistershowerstandingdoggy_2"
    pause 0.2
    "bg sistershowerstandingdoggy_3"
    pause 0.2
    "bg sistershowerstandingdoggy_4"
    pause 0.2
    "bg sistershowerstandingdoggy_2"
    pause 0.2
    repeat
####################
## Stage 1 XRAY
label lbl_sister_shower_standing_doggy_1_0:
    scene img_sister_shower_standing_doggy_stage_1_0
    #$ sister_shower_standing_doggy_counter += 1
    #show bg sistershowerstandingdoggy_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_2_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and sister_shower_standing_doggy_counter == 4:
    #    jump lbl_sister_shower_standing_doggy_cum
    #elif skill_sta <= 14 and sister_shower_standing_doggy_counter == 6:
    #    jump lbl_sister_shower_standing_doggy_2_0
    #elif skill_sta <= 20 and sister_shower_standing_doggy_counter == 8:
    #    jump lbl_sister_shower_standing_doggy_2_0
    #else:
    #    jump lbl_sister_shower_standing_doggy_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sister_shower_standing_doggy_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sister_shower_standing_doggy_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_1_0

image img_sister_shower_standing_doggy_stage_1_0:
    "bg sistershowerstandingdoggy_1_0"
    pause 0.2
    "bg sistershowerstandingdoggy_2_0"
    pause 0.2
    "bg sistershowerstandingdoggy_3_0"
    pause 0.2
    "bg sistershowerstandingdoggy_4_0"
    pause 0.2
    "bg sistershowerstandingdoggy_2_0"
    pause 0.2
    repeat
####################
## Stage 2
label lbl_sister_shower_standing_doggy_2:
    scene img_sister_shower_standing_doggy_stage_2
    #$ sister_shower_standing_doggy_counter += 1
    #show bg sistershowerstandingdoggy_5
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_6
    #$ renpy.pause(0.1,hard=True)
    #show bg sistershowerstandingdoggy_8
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_6
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and sister_shower_standing_doggy_counter == 14:
    #    jump lbl_sister_shower_standing_doggy_cum
    #elif skill_sta <= 20 and sister_shower_standing_doggy_counter == 16:
    #    jump lbl_sister_shower_standing_doggy_3
    #else:
    #    jump lbl_sister_shower_standing_doggy_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sister_shower_standing_doggy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sister_shower_standing_doggy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_2

image img_sister_shower_standing_doggy_stage_2:
    "bg sistershowerstandingdoggy_5"
    pause 0.2
    "bg sistershowerstandingdoggy_6"
    pause 0.1
    "bg sistershowerstandingdoggy_8"
    pause 0.2
    "bg sistershowerstandingdoggy_6"
    pause 0.2
    repeat
####################
## Stage 2 XRAY
label lbl_sister_shower_standing_doggy_2_0:
    scene img_sister_shower_standing_doggy_stage_2_0
    #$ sister_shower_standing_doggy_counter += 1
    #show bg sistershowerstandingdoggy_5_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_6_0
    #$ renpy.pause(0.1,hard=True)
    #show bg sistershowerstandingdoggy_8_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_6_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and sister_shower_standing_doggy_counter == 14:
    #    jump lbl_sister_shower_standing_doggy_cum
    #elif skill_sta <= 20 and sister_shower_standing_doggy_counter == 16:
    #    jump lbl_sister_shower_standing_doggy_3_0
    #else:
    #    jump lbl_sister_shower_standing_doggy_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sister_shower_standing_doggy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sister_shower_standing_doggy_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_2_0

image img_sister_shower_standing_doggy_stage_2_0:
    "bg sistershowerstandingdoggy_5_0"
    pause 0.2
    "bg sistershowerstandingdoggy_6_0"
    pause 0.1
    "bg sistershowerstandingdoggy_8_0"
    pause 0.2
    "bg sistershowerstandingdoggy_6_0"
    pause 0.2
    repeat
####################
## Stage 3
label lbl_sister_shower_standing_doggy_3:
    scene img_sister_shower_standing_doggy_stage_3
    #$ sister_shower_standing_doggy_counter += 1
    #show bg sistershowerstandingdoggy_9
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_11
    #$ renpy.pause(0.1,hard=True)
    #show bg sistershowerstandingdoggy_10
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and sister_shower_standing_doggy_counter == 24:
    #    jump lbl_sister_shower_standing_doggy_cum
    #else:
    #    jump lbl_sister_shower_standing_doggy_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sister_shower_standing_doggy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_3

image img_sister_shower_standing_doggy_stage_3:
    "bg sistershowerstandingdoggy_9"
    pause 0.2
    "bg sistershowerstandingdoggy_11"
    pause 0.1
    "bg sistershowerstandingdoggy_10"
    pause 0.2
    repeat
####################
## Stage 3 XRAY
label lbl_sister_shower_standing_doggy_3_0:
    scene img_sister_shower_standing_doggy_stage_3_0
    #$ sister_shower_standing_doggy_counter += 1
    #show bg sistershowerstandingdoggy_9_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sistershowerstandingdoggy_11_0
    #$ renpy.pause(0.1,hard=True)
    #show bg sistershowerstandingdoggy_10_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and sister_shower_standing_doggy_counter == 24:
    #    jump lbl_sister_shower_standing_doggy_cum
    #else:
    #    jump lbl_sister_shower_standing_doggy_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sister_shower_standing_doggy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sister_shower_standing_doggy_3_0
image img_sister_shower_standing_doggy_stage_3_0:
    "bg sistershowerstandingdoggy_9_0"
    pause 0.2
    "bg sistershowerstandingdoggy_11_0"
    pause 0.1
    "bg sistershowerstandingdoggy_10_0"
    pause 0.2
    repeat
####################
## Cum
label lbl_sister_shower_standing_doggy_cum:
    jump lbl_sister_shower_standing_doggy_cum_2

label lbl_sister_shower_standing_doggy_cum_2:
    #if hscene_xray == 0:
    #    scene bg sistershowerstandingdoggy_5
    #else:
    #    scene bg sistershowerstandingdoggy_5_0
    call screen scr_sister_shower_standing_doggy_cum_2

screen scr_sister_shower_standing_doggy_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sister_shower_standing_doggy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sister_shower_standing_doggy_cumchoice")

# label lbl_sister_shower_standing_doggy_cum_3:
#     if hscene_xray == 0:
#         scene bg sistershowerstandingdoggy_1
#     else:
#         scene bg sistershowerstandingdoggy_1_0
#     call screen scr_sister_shower_standing_doggy_cum_3
#
# screen scr_sister_shower_standing_doggy_cum_3():
#     imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sister_shower_standing_doggy_scenechoice_mish")
#     imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sister_shower_standing_doggy_mish_0")
#     imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sister_shower_standing_doggy_cumchoice")

label lbl_sister_shower_standing_doggy_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_sister_shower_standing_doggy_cumin
            else:
                jump lbl_sister_shower_standing_doggy_cumin_0
        "Cum on her":
            jump lbl_sister_shower_standing_doggy_cumout

####################
## Cum In
label lbl_sister_shower_standing_doggy_cumin:
    scene bg sistershowerstandingdoggy_5
    $ renpy.pause(0.2,hard=True)
    show bg sistershowerstandingdoggy_6
    $ renpy.pause(0.2,hard=True)
    show bg sistershowerstandingdoggy_7
    $ renpy.pause(0.2,hard=True)
    show bg sistershowerstandingdoggy_14_0
    $ renpy.pause(1.5,hard=True)
    show bg sistershowerstandingdoggy_14_1
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_14_2
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_14_3
    $ renpy.pause(0.3,hard=True)
    pov "{i}*Exhales*{/i} Ah fuck..."
    pov "{i}*Pants*{/i} Oh my God, that felt so good."
    if sister_path != 36:
        sis "{i}*Pants*{/i} Do you think [missus] heard us?"
        pov "Hopefully not."
        if mumsis_path >= 7:
            sis "Even so, wouldn't it be so hot if she was just there watching us?"
            pov "Don't say that, I'll literally fill you with a second round."
            sis "Hehe~ I bet [missus]'ll appreciate the audio-visual of that."
        else:
            sis "She can't know about this."
            sis "We'll totally be disowned by her."
            pov "I'll miss her cooking if she does."
            sis "That's your concern?"
            pov "Hahaha~ Just post-sex hunger to be honest."
    sis "C'mon, let's clean up. It's the whole reason I'm in the frikkin shower after all."
    pov "Righto."
    scene black
    with fade
    if sister_points < 10:
        $ sister_points += 1
        $ renpy.notify("Your relationship with [sister] has increased")
    $ renpy.pause()
    "After a splash of the shower to clean up..."
    scene bg myhallway_day
    with fade

    if sister_path == 36:
        show povne smirk at left with dissolve
        show sisn smirk at center with dissolve
        $ renpy.pause(1.0)
        show sisn shocked_talk
        sis "Jesus, [pov], didn't you just cum?"
        show sisn neutral_talk
        sis "Well, it will have to wait. [missus] will be back soon with dinner. It sounded like we both needed to be there."
        show sisn bored_talk
        sis "Yeah, you might want to put some clothes on before that."
        show sisn neutral_talk
        sis "I'll be doing the same. See you at dinner, [pov]."
        $ sister_path = 36.1
        $ townmap_enabled = 1
        scene bg mybedroom_day with fade
        jump lbl_mybedroom_day_setup

    jump lbl_myhallway_day

####################
## Cum In XRAY
label lbl_sister_shower_standing_doggy_cumin_0:
    scene bg sistershowerstandingdoggy_1_0
    $ renpy.pause(0.2,hard=True)
    show bg sistershowerstandingdoggy_2_0
    $ renpy.pause(0.2,hard=True)
    show bg sistershowerstandingdoggy_3_0
    $ renpy.pause(0.2,hard=True)
    show bg sistershowerstandingdoggy_13_0
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_1
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_2
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_3
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_4
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_5
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_6
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_7
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_8
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_9
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_13_10
    $ renpy.pause(0.8,hard=True)
    pov "{i}*Exhales*{/i} Ah fuck..."
    pov "{i}*Pants*{/i} Oh my god, that felt so good."
    if sister_path != 36:
        sis "{i}*Pants*{/i} Do you think [missus] heard us?"
        pov "Hopefully not."
        if mumsis_path >= 7:
            sis "Even so, wouldn't it be so hot if she was just there watching us?"
            pov "Don't say that, I'll literally fill you with a second round."
            sis "Hehe~ I bet [missus]'ll appreciate the audio-visual of that."
        else:
            sis "She can't know about this."
            sis "We'll totally be disowned by her."
            pov "I'll miss her cooking if she does."
            sis "That's your concern?"
            pov "Hahaha~ Just post-sex hunger to be honest."
    sis "C'mon, let's clean up. It's the whole reason I'm in the frikkin shower after all."
    pov "Righto."
    scene black
    with fade
    if sister_points < 10:
        $ sister_points += 1
        $ renpy.notify("Your relationship with [sister] has increased")
    $ renpy.pause()
    "After a splash of the shower to clean up..."
    scene bg myhallway_day
    with fade

    if sister_path == 36:
        show povne smirk at left with dissolve
        show sisn smirk at center with dissolve
        $ renpy.pause(1.0)
        show sisn shocked_talk
        sis "Jesus, [pov], didn't you just cum?"
        show sisn neutral_talk
        sis "Well, it will have to wait. [missus] will be back soon with dinner. It sounded like we both needed to be there."
        show sisn bored_talk
        sis "Yeah, you might want to put some clothes on before that."
        show sisn neutral_talk
        sis "I'll be doing the same. See you at dinner, [pov]."
        $ sister_path = 36.1
        $ townmap_enabled = 1
        scene bg mybedroom_day with fade
        jump lbl_mybedroom_day_setup

    jump lbl_myhallway_day

####################
## Missionary Cum Out
label lbl_sister_shower_standing_doggy_cumout:
    pov "I'm gonna cum, [sister]-"
    sis "Quick, pull out~"
    sis "Cover my ass in your cum."
    scene bg sistershowerstandingdoggy_15_0
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_1
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_2
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_3
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_4
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_5
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_6
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_7
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_8
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_9
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_10
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_11
    $ renpy.pause(0.3,hard=True)
    show bg sistershowerstandingdoggy_15_12
    $ renpy.pause(0.8,hard=True)
    pov "{i}*Exhales*{/i} Ah fuck..."
    show bg sistershowerstandingdoggy_15_13
    pov "{i}*Pants*{/i} Oh my god, that felt so good."
    if sister_path != 36:
        sis "{i}*Pants*{/i} Do you think [missus] heard us?"
        pov "Hopefully not."
        if mumsis_path >= 7:
            sis "Even so, wouldn't it be so hot if she was just there watching us?"
            pov "Don't say that, I'll literally fill you with a second round."
            sis "Hehe~ I bet [missus]'ll appreciate the audio-visual of that."
        else:
            sis "She can't know about this."
            sis "We'll totally be disowned by her."
            pov "I'll miss her cooking if she does."
            sis "That's your concern?"
            pov "Hahaha~ Just post-sex hunger to be honest."
    sis "C'mon, let's clean up. It's the whole reason I'm in the frikkin shower after all."
    pov "Righto."
    scene black
    with fade
    if sister_points < 10:
        $ sister_points += 1
        $ renpy.notify("Your relationship with [sister] has increased")
    $ renpy.pause()
    "After a splash of the shower to clean up..."
    scene bg myhallway_day
    with fade

    if sister_path == 36:
        show povne smirk at left with dissolve
        show sisn smirk at center with dissolve
        $ renpy.pause(1.0)
        show sisn shocked_talk
        sis "Jesus, [pov], didn't you just cum?"
        show sisn neutral_talk
        sis "Well, it will have to wait. [missus] will be back soon with dinner. It sounded like we both needed to be there."
        show sisn bored_talk
        sis "Yeah, you might want to put some clothes on before that."
        show sisn neutral_talk
        sis "I'll be doing the same. See you at dinner, [pov]."
        $ sister_path = 36.1
        $ townmap_enabled = 1
        scene bg mybedroom_day with fade
        jump lbl_mybedroom_day_setup

    jump lbl_myhallway_day
