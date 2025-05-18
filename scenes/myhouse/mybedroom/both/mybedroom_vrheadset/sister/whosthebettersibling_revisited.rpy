

label lbl_whos_the_better_sibling_revisit_1:
    $ vrheadset_revisitcounter = 0
    scene bg whosthebettersibling_8
    with fade
    $ renpy.pause(1,hard=True)
    show bg whosthebettersibling_3
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_4
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_5
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_6
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_7
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_3
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_4
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_5
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_6
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_7
    $ renpy.pause(0.3,hard=True)
    jump lbl_whos_the_better_sibling_revisit_continue

label lbl_whos_the_better_sibling_revisit_continue:
    $ vrheadset_revisitcounter = 0

    jump lbl_whos_the_better_sibling_revisit_2

####################
## 69 Stage 1
label lbl_whos_the_better_sibling_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg whosthebettersibling_3
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_4
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_5
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_6
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_7
    $ renpy.pause(0.3,hard=True)
    jump lbl_whos_the_better_sibling_revisit_counter

####################
## 69 Stage 2
label lbl_whos_the_better_sibling_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg whosthebettersibling_3
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_5
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_6
    $ renpy.pause(0.2,hard=True)
    show bg whosthebettersibling_7
    $ renpy.pause(0.2,hard=True)
    jump lbl_whos_the_better_sibling_revisit_counter

####################
## 69 Stage 3
label lbl_whos_the_better_sibling_revisit_4:
    $ vrheadset_revisitcounter += 1
    show bg whosthebettersibling_3
    $ renpy.pause(0.2,hard=True)
    show bg whosthebettersibling_5
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_7
    $ renpy.pause(0.2,hard=True)
    jump lbl_whos_the_better_sibling_revisit_counter

label lbl_whos_the_better_sibling_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_whos_the_better_sibling_revisit_3
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_whos_the_better_sibling_revisit_4
    elif vrheadset_revisitcounter >= 90:
        call screen scr_whos_the_better_sibling_5_revisit
    else:
        jump lbl_whos_the_better_sibling_revisit_2

screen scr_whos_the_better_sibling_5_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_whos_the_better_sibling_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_whos_the_better_sibling_revisit_cumchoice")


label lbl_whos_the_better_sibling_revisit_cumchoice:

    menu:
        "She Cums":
            jump lbl_whos_the_better_sibling_revisit_cumsis
        "Cum inside":
            jump lbl_whos_the_better_sibling_revisit_cumin
        "Cum on her":
            jump lbl_whos_the_better_sibling_revisit_cumout


label lbl_whos_the_better_sibling_revisit_cumsis:
    show bg whosthebettersibling_8
    sis "Oh, fuck... fuck- fuck... [povname].. [povname]..."
    sis "Oh my God... keep going- keep-"
    sis "..."
    sis "...."
    sis "Arrghhh! Fucckk! Hooo... fuck!"
    show bg whosthebettersibling_9
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_10
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_11
    $ renpy.pause(0.8,hard=True)
    sis "Shit..."
    show bg whosthebettersibling_12
    sis "Oh my God.. Naww... dude.. Fu- oh God... I'm soo sorry..."
    sis "I didn't mean to squirt all over you...."
    sis "A- are you okay?"
    sis "Can you breathe?"
    show bg whosthebettersibling_13
    pov "I'm okay."
    pov "Daamn, girl. You really covered me..."
    pov "I win! Hahaha-"
    show bg whosthebettersibling_14
    pov "Ow.. oww... my eyes... it stings!"
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

label lbl_whos_the_better_sibling_revisit_cumin:
    show bg whosthebettersibling_3
    pov "Oh... fucckk! I'm cumming, [sister]!"
    show bg whosthebettersibling_4
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_15
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_16
    $ renpy.pause(0.5,hard=True)
    show bg whosthebettersibling_17
    $ renpy.pause(0.5,hard=True)
    show bg whosthebettersibling_18
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_19
    $ renpy.pause(0.4,hard=True)
    show bg whosthebettersibling_20
    $ renpy.pause(0.5,hard=True)
    pov "Holy shit..."
    pov "..."
    pov "[sister]?"
    pov "You alright there?"
    show bg whosthebettersibling_21
    sis "{i}*Murmur*{/i}"
    pov "Huh?"
    sis "{i}*Murmur*{/i}"
    show bg whosthebettersibling_22
    pov "Sorry I jizzed a lot... I hope it taste as good as your $100."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

label lbl_whos_the_better_sibling_revisit_cumout:
    show bg whosthebettersibling_3
    pov "Oh... fucckk! I'm cumming, [sister]!"
    show bg whosthebettersibling_23
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_24
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_25
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_26
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_27
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_28
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_29
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_30
    $ renpy.pause(0.8,hard=True)
    pov "Holy shit..."
    pov "..."
    show bg whosthebettersibling_31
    sis "Holy shit is right, [povname]..."
    sis "It shot straight up my nose."
    sis "Ow.. oh, God... I think I snorted your cum."
    sis "Fuck..."
    show bg whosthebettersibling_32
    sis "Totally worth the $100 though."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
