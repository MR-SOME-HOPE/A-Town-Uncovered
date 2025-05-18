####################
## Meghan Weed Kush
default found_teghan_weed = 0

####################
## Pre
label lbl_teghan_stall_reverse_seated_cowgirl:
    scene bg schoolhallway1_day
    show btn schoolhallway1_day_zariah_idle
    $ renpy.pause(0.001)

    scene bg schoolbathroomfemale_day
    show teg smirk at right
    with fade

    show pov neutral at left
    with dissolve

    #"You see Teghan smoking."
    show teg neutral_talk
    teg "Yooo~ [povname]."
    teg "This is the little girl's room."
    show pov confused
    show teg neutral
    pov "{i}*Sniff*{/i}"
    show pov confused_talk
    pov "Is that weed I smell?"
    show pov confused
    teg "Yeah, duuuuude!"
    show teg confused_talk
    teg "But uh- The last girl that was in here totally was smoking it and absolutely not me."
    show pov bored
    show teg neutral_talk
    teg "I 100%% just walked in just now-"
    show pov smirk
    show teg neutral
    pov "Mhmm-"
    show pov neutral
    show teg bored_talk
    teg "Aye you ain't a nark- I know I ain't supposed to be smoking it on the premises but what's a girl gotta do."
    teg "Look- I'd offer you some which I never had in the first place FYI-"
    show pov neutral
    show teg neutral_talk
    teg "But if I did, I just finished it."
    teg "Sorry, my man."
    show teg neutral
    pov "..."
    show pov shocked
    show teg angry_talk
    teg "Alright! Alright! You caught me- don't tell Lashley about it, I hate when she gets into my shit."
    show pov smirk
    show teg neutral_talk
    teg "I'll let you fuck me in exchange for some silence, deal?"
    teg "Sex feels so good when high- which I am not!"
    show pov embarrassed_talk
    show teg bored
    if found_teghan_weed == 0:
        pov "Why are you still trying to defend yourself, you just admitted to it."
    else:
        pov "You know you don't have to defend yourself over and over again."
    show pov shocked
    show teg bored_talk
    teg "Do you wanna fuck me or not, broseph?"

    $ found_teghan_weed = 0

    menu:
        "Fuck yeah":
            show pov smirk_talk
            show teg neutral
            pov "You've got a deal."

            scene black with fade

            jump lbl_teghan_stall_reverse_seated_cowgirl_0

        "Nah, you're good":
            show pov neutral_talk
            show teg bored
            pov "Nah, you're all good."
            pov "I'll keep your name out of my mouth, promise."
            show pov neutral
            teg "..."
            show pov embarrassed
            show teg sad_talk
            teg "Ughhhhh- but I want that high-high... I'll just do it myself-"

            jump lbl_schoolhallway1_day_setup

## RESET
label lbl_teghan_stall_reverse_seated_cowgirl_0:
    if hscene_xray == 0:
        jump lbl_teghan_stall_reverse_seated_cowgirl_1
    else:
        jump lbl_teghan_stall_reverse_seated_cowgirl_1_0

####################
## Stage 1
label lbl_teghan_stall_reverse_seated_cowgirl_1:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_1

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
label lbl_teghan_stall_reverse_seated_cowgirl_1_0:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_1

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
label lbl_teghan_stall_reverse_seated_cowgirl_2:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_2

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
label lbl_teghan_stall_reverse_seated_cowgirl_2_0:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_2_0

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
label lbl_teghan_stall_reverse_seated_cowgirl_3:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_3

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
label lbl_teghan_stall_reverse_seated_cowgirl_3_0:
    scene img_teghan_stall_reverse_seated_cowgirl_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_teghan_stall_reverse_seated_cowgirl_3_0

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
label lbl_teghan_stall_reverse_seated_cowgirl_menu:
    call screen scr_teghan_stall_reverse_seated_cowgirl_menu

screen scr_teghan_stall_reverse_seated_cowgirl_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_teghan_stall_reverse_seated_cowgirl_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_teghan_stall_reverse_seated_cowgirl_cum_menu")

label lbl_teghan_stall_reverse_seated_cowgirl_cum_menu:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_teghan_stall_reverse_seated_cowgirl_cumin
            else:
                jump lbl_teghan_stall_reverse_seated_cowgirl_cumin_0

        "Pull out and cum":
            jump lbl_teghan_stall_reverse_seated_cowgirl_cumout

####################
## Cum In
label lbl_teghan_stall_reverse_seated_cowgirl_cumin:
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
    "After cleaning yourselves up..."

    jump lbl_schoolhallway1_day_setup

####################
## Cum In XRAY
label lbl_teghan_stall_reverse_seated_cowgirl_cumin_0:
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
    "After cleaning yourselves up..."

    jump lbl_schoolhallway1_day_setup

####################
## Cum Out
label lbl_teghan_stall_reverse_seated_cowgirl_cumout:
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
    "After cleaning up the floor..."

    jump lbl_schoolhallway1_day_setup
