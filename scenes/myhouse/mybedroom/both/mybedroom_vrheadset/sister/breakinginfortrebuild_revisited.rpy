label lbl_breakinginfortrebuild_bj_revisit_pre:
    $ vrheadset_revisitcounter = 0
    show bg breakinginfortrebuild_5
    with fade
    $ renpy.pause()
    show bg breakinginfortrebuild_29
    $ renpy.pause()
    show bg breakinginfortrebuild_30
    $ renpy.pause(2,hard=True)
    show bg breakinginfortrebuild_31
    $ renpy.pause(1,hard=True)
    show bg breakinginfortrebuild_32
    $ renpy.pause(1,hard=True)
    show bg breakinginfortrebuild_33
    pov "H-Hey!"
    pov "[sister], what are you doing?"
    show bg breakinginfortrebuild_34
    sis "D-Do you not want to?"
    show bg breakinginfortrebuild_39
    pov "I'll keep quiet."
    show bg breakinginfortrebuild_40
    sis "Mhmm, that's what I thought, baby-bro."

    scene bg breakinginfortrebuild_bj_1
    with fade
    sis "W-Woah... It's-"
    sis "It's actually bigger than I remembered."
    sis "Like it feels really thick."
    pov "Sorry, I'm a grower, not a shower."
    show bg breakinginfortrebuild_bj_23
    sis "Tch- hashtag humble brag."
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_4
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_4
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    sis "It's not fair, you know?"
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_4
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_23
    sis "When did you become this charming?"
    sis "How is a girl not supposed to..."
    show bg breakinginfortrebuild_bj_24
    sis "To-"

label lbl_breakinginfortrebuild_bj_revisit_0:
    $ vrheadset_revisitcounter = 0

    jump lbl_breakinginfortrebuild_bj_revisit_1

####################
## BJ Stage 1
label lbl_breakinginfortrebuild_bj_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg breakinginfortrebuild_bj_5
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_6
    $ renpy.pause(0.1,hard=True)
    show bg breakinginfortrebuild_bj_8
    $ renpy.pause(0.1,hard=True)
    show bg breakinginfortrebuild_bj_7
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_6
    $ renpy.pause(0.3,hard=True)
    jump lbl_breakinginfortrebuild_bj_revisit_counter

####################
## BJ Stage 2
label lbl_breakinginfortrebuild_bj_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg breakinginfortrebuild_bj_9
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_11
    $ renpy.pause(0.1,hard=True)
    show bg breakinginfortrebuild_bj_10
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_12
    $ renpy.pause(0.2,hard=True)
    jump lbl_breakinginfortrebuild_bj_revisit_counter

####################
## BJ Stage 3
label lbl_breakinginfortrebuild_bj_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg breakinginfortrebuild_bj_13
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_14
    $ renpy.pause(0.1,hard=True)
    show bg breakinginfortrebuild_bj_15
    $ renpy.pause(0.2,hard=True)
    jump lbl_breakinginfortrebuild_bj_revisit_counter

label lbl_breakinginfortrebuild_bj_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_breakinginfortrebuild_bj_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_breakinginfortrebuild_bj_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_breakinginfortrebuild_bj_cum_revisit
    else:
        jump lbl_breakinginfortrebuild_bj_revisit_1


screen scr_breakinginfortrebuild_bj_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_breakinginfortrebuild_bj_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_breakinginfortrebuild_bj_revisit_cumchoice")


label lbl_breakinginfortrebuild_bj_revisit_cumchoice:
    menu:
        "Cum inside mouth":
            jump lbl_breakinginfortrebuild_bj_revisit_cumin
        "Cum outside on face":
            jump lbl_breakinginfortrebuild_bj_revisit_cumout

####################
## BJ Cum in

label lbl_breakinginfortrebuild_bj_revisit_cumin:
    show bg breakinginfortrebuild_bj_14
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_14_1
    $ renpy.pause(1,hard=True)
    show bg breakinginfortrebuild_bj_14_2
    $ renpy.pause(0.5,hard=True)
    show bg breakinginfortrebuild_bj_14_3
    $ renpy.pause()
    show bg breakinginfortrebuild_bj_16
    $ renpy.pause(0.7,hard=True)
    show bg breakinginfortrebuild_bj_17
    $ renpy.pause(0.7,hard=True)
    show bg breakinginfortrebuild_bj_18
    $ renpy.pause(0.7,hard=True)
    show bg breakinginfortrebuild_bj_19
    $ renpy.pause()
    sis "Well..."
    sis "I ain't having lunch today..."
    show bg breakinginfortrebuild_bj_20
    sis "Fuck-"
    show bg breakinginfortrebuild_bj_21
    sis "Seriously dude, it's way too much cum for a single guy."
    pov "It's a gift."
    show bg breakinginfortrebuild_bj_22
    sis "No kidding."
    sis "What's the secret? Vitamin tablets? Iron?"
    sis "Are you always on... edge?"
    pov "It keeps you on edge, doesn't it?"
    sis "..."
    show bg breakinginfortrebuild_bj_21
    sis "Fuck... that actually turns me on."
    sis "Mmmm... Can you pass me a towel or something to clean up?"
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## BJ Cum out

label lbl_breakinginfortrebuild_bj_revisit_cumout:
    show bg breakinginfortrebuild_bj_25_0
    $ renpy.pause(0.5,hard=True)
    show bg breakinginfortrebuild_bj_25_1
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_2
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_3
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_4
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_5
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_6
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_7
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_8
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_9
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_10
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_11
    $ renpy.pause(0.5,hard=True)
    sis "Ah!"
    sis "Crappers!"
    show bg breakinginfortrebuild_bj_25_12
    sis "Damn, dude-!"
    sis "My fuckin' nose!"
    show bg breakinginfortrebuild_bj_25_11
    sis "I accidentally snorted your crack cum!"
    pov "Sounds like Squideward is blowing me down there."
    show bg breakinginfortrebuild_bj_25_12
    sis "Fuck off."
    show bg breakinginfortrebuild_bj_25_11
    sis "How does one guy cum so much?!"
    sis "I should have swallowed."
    pov "Maybe we should retry it."
    show bg breakinginfortrebuild_bj_25_12
    sis "Again, fuck off."
    show bg breakinginfortrebuild_bj_25_11
    sis "Gaaghh... Can you pass me a towel or something to clean up?"
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
