####################
## Teghan Stall Reverse Seated Cowgirl
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_0:
    if hscene_xray == 0:
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_1
    else:
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_1_0

####################
## Stage 1
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_1:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_1

image img_teghan_stall_reverse_seated_cowgirl_stage_1:
    "bg teghanstallreverseseatedcowgirl_1"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_2"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_3"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_4"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_5"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_1_0:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_1

image img_teghan_stall_reverse_seated_cowgirl_stage_1_0:
    "bg teghanstallreverseseatedcowgirl_1_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_2_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_3_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_4_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_5_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_2:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_2

image img_teghan_stall_reverse_seated_cowgirl_stage_2:
    "bg teghanstallreverseseatedcowgirl_6"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_7"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_8"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_9"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_2_0:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_2_0

image img_teghan_stall_reverse_seated_cowgirl_stage_2_0:
    "bg teghanstallreverseseatedcowgirl_6_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_7_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_8_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_9_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_3:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_3

image img_teghan_stall_reverse_seated_cowgirl_stage_3:
    "bg teghanstallreverseseatedcowgirl_10"
    pause 0.1
    "bg teghanstallreverseseatedcowgirl_11"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_12"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_3_0:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_3_0

image img_teghan_stall_reverse_seated_cowgirl_stage_3_0:
    "bg teghanstallreverseseatedcowgirl_10_0"
    pause 0.1
    "bg teghanstallreverseseatedcowgirl_11_0"
    pause 0.2
    "bg teghanstallreverseseatedcowgirl_12_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_menu:
    call screen scr_teghan_stall_reverse_seated_cowgirl_revisit_menu

screen scr_teghan_stall_reverse_seated_cowgirl_revisit_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_teghan_stall_reverse_seated_cowgirl_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_teghan_stall_reverse_seated_cowgirl_revisit_cum_menu")

label lbl_teghan_stall_reverse_seated_cowgirl_revisit_cum_menu:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_cumin
            else:
                jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_cumin_0

        "Pull out and cum":
            jump lbl_teghan_stall_reverse_seated_cowgirl_revisit_cumout

####################
## Cum In
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_cumin:
    pov "Teghan- I'm gonn-"
    teg "Cum inside- cum inside!"
    teg "I wanna be filled with euphoria!"
    scene bg teghanstallreverseseatedcowgirl_13_0
    $ renpy.pause(1.2,hard=True)
    show bg teghanstallreverseseatedcowgirl_13_1
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_13_2
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_13_3
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_13_4
    $ renpy.pause()
    teg "Fuck- fuck- fuck- fuck- shieeeeeet"
    teg "{i}*Shudders*{/i}"
    teg "God, I'm so braindead-"
    teg "Ghhhggghhh~"
    pov "{i}*Heavy panting*{/i}"
    pov "Oh my god, I can't believe you let me cum inside-"
    pov "..."
    pov "You'll be okay, right?"
    pov "..."
    pov "Teghan?"
    teg "Ghhrrrghghghhhh~"
    teg "{i}*Slurred Mumbles*{/i}"
    pov "Don't worry, I'll clean us up best I can and head off."
    pov "Thanks for the sesh."
    teg "{i}*Mumbles*{/i}"

    scene black
    with fade
    $ renpy.pause()
    
    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_cumin_0:
    pov "Teghan- I'm gonn-"
    teg "Cum inside- cum inside!"
    teg "I wanna be filled with euphoria!"
    scene bg teghanstallreverseseatedcowgirl_14_0
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_1
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_2
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_3
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_4
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_5
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_6
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_7
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_8
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_9
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_10
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_14_11
    $ renpy.pause()
    teg "Fuck- fuck- fuck- fuck- shieeeeeet"
    teg "{i}*Shudders*{/i}"
    teg "God, I'm so braindead-"
    teg "Ghhhggghhh~"
    pov "{i}*Heavy panting*{/i}"
    pov "Oh my god, I can't believe you let me cum inside-"
    pov "..."
    pov "You'll be okay, right?"
    pov "..."
    pov "Teghan?"
    teg "Ghhrrrghghghhhh~"
    teg "{i}*Slurred Mumbles*{/i}"
    pov "Don't worry, I'll clean us up best I can and head off."
    pov "Thanks for the sesh."
    teg "{i}*Mumbles*{/i}"

    scene black
    with fade
    $ renpy.pause()
    
    jump lbl_vrheadset_character_selection

####################
## Cum Out
label lbl_teghan_stall_reverse_seated_cowgirl_revisit_cumout:
    pov "Teghan- I'm gonn-"
    teg "Pull out- pull out-"
    teg "I'm not ready to be a daddy!"
    if hscene_xray == 1:
        scene bg teghanstallreverseseatedcowgirl_7_0
        $ renpy.pause(0.4,hard=True)
        show bg teghanstallreverseseatedcowgirl_6_0
        $ renpy.pause(0.4,hard=True)
    else:
        scene bg teghanstallreverseseatedcowgirl_7
        $ renpy.pause(0.4,hard=True)
        show bg teghanstallreverseseatedcowgirl_6
        $ renpy.pause(0.4,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_0
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_1
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_2
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_3
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_4
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_5
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_6
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_7
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_8
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_9
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_10
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_11
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_12
    $ renpy.pause(0.3,hard=True)
    show bg teghanstallreverseseatedcowgirl_15_13
    $ renpy.pause()
    teg "Oh. My. God."
    teg "Jeepers creepers."
    teg "What a load-"
    teg "Of fun~"
    teg "That was fun, [povname]."
    pov "{i}*Pants*{/i}"
    teg "[povname]?"
    pov "Gimme a sec- need to catch my breath."
    teg "Yeah, but you have to clean up."
    teg "I gotta head to class."
    pov "You're not gonna help."
    teg "Bro- I'm too high for this shit."
    teg "Alright, dude. Catch you later, gotta catch up on some sleep."
    pov "I thought you said you had class."
    teg "Hur- durrr~"

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
