## Stargazing Sibling Fun ##
label lbl_stargazing_fun_revisit:
    $ vrheadset_revisitcounter = 0
    if hscene_xray == 0:
        scene bg stargazingfun_1
        with dissolve
        show bg stargazingfun_1
        with hpunch
    else:
        scene bg stargazingfun_1_0
        with dissolve
        show bg stargazingfun_1_0
        with hpunch
    pov "[sister]?"
    sis "Please don't deny me this, tonight..."
    sis "Tonight I want to remember forever."
    sis "Tonight I just want to be close as I can with you."
    jump lbl_stargazing_fun_revisit_0

label lbl_stargazing_fun_revisit_0:
    $ vrheadset_revisitcounter = 0
    if hscene_xray == 0:
        jump lbl_stargazing_fun_revisit_1
    else:
        jump lbl_stargazing_fun_revisit_1_0

####################
## Stage 1
label lbl_stargazing_fun_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg stargazingfun_1
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_2
    $ renpy.pause(0.1,hard=True)
    show bg stargazingfun_3
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_4
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_5
    $ renpy.pause(0.3,hard=True)
    jump lbl_stargazing_fun_revisit_counter

####################
## Stage 1 XRAY
label lbl_stargazing_fun_revisit_1_0:
    $ vrheadset_revisitcounter += 1
    show bg stargazingfun_1_0
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_2_0
    $ renpy.pause(0.1,hard=True)
    show bg stargazingfun_3_0
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_4_0
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_5_0
    $ renpy.pause(0.3,hard=True)
    jump lbl_stargazing_fun_revisit_counter_xray

####################
## Stage 2
label lbl_stargazing_fun_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg stargazingfun_1
    $ renpy.pause(0.2,hard=True)
    show bg stargazingfun_2
    $ renpy.pause(0.1,hard=True)
    show bg stargazingfun_3
    $ renpy.pause(0.2,hard=True)
    show bg stargazingfun_4
    $ renpy.pause(0.2,hard=True)
    jump lbl_stargazing_fun_revisit_counter_xray

####################
## Stage 2 XRAY
label lbl_stargazing_fun_revisit_2_0:
    $ vrheadset_revisitcounter += 1
    show bg stargazingfun_1_0
    $ renpy.pause(0.2,hard=True)
    show bg stargazingfun_2_0
    $ renpy.pause(0.1,hard=True)
    show bg stargazingfun_3_0
    $ renpy.pause(0.2,hard=True)
    show bg stargazingfun_4_0
    $ renpy.pause(0.2,hard=True)
    jump lbl_stargazing_fun_revisit_counter_xray

####################
## Stage 3
label lbl_stargazing_fun_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg stargazingfun_1
    $ renpy.pause(0.2,hard=True)
    show bg stargazingfun_3
    $ renpy.pause(0.1,hard=True)
    show bg stargazingfun_4
    $ renpy.pause(0.2,hard=True)
    jump lbl_stargazing_fun_revisit_counter

####################
## Stage 3 XRAY
label lbl_stargazing_fun_revisit_3_0:
    $ vrheadset_revisitcounter += 1
    show bg stargazingfun_1_0
    $ renpy.pause(0.2,hard=True)
    show bg stargazingfun_3_0
    $ renpy.pause(0.1,hard=True)
    show bg stargazingfun_4_0
    $ renpy.pause(0.2,hard=True)
    jump lbl_stargazing_fun_revisit_counter_xray

####################
## Cum Menu
label lbl_stargazing_fun_revisit_cum:
    if hscene_xray == 0:
        scene bg stargazingfun_1
    else:
        scene bg stargazingfun_1_0
    call screen scr_stargazing_fun_cum_revist

label lbl_stargazing_fun_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_stargazing_fun_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_stargazing_fun_revisit_3
    elif vrheadset_revisitcounter >= 90:
        jump lbl_stargazing_fun_revisit_cum
    else:
        jump lbl_stargazing_fun_revisit_1

label lbl_stargazing_fun_revisit_counter_xray:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_stargazing_fun_revisit_2_0
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_stargazing_fun_revisit_3_0
    elif vrheadset_revisitcounter >= 90:
        jump lbl_stargazing_fun_revisit_cum
    else:
        jump lbl_stargazing_fun_revisit_1_0


screen scr_stargazing_fun_cum_revist():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_stargazing_fun_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_stargazing_fun_revisit_cumchoice")

label lbl_stargazing_fun_revisit_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_stargazing_fun_revisit_cumin
            else:
                jump lbl_stargazing_fun_revisit_cumin_0
        "Cum outside":
            jump lbl_stargazing_fun_revisit_cumout

####################
## Cum In
label lbl_stargazing_fun_revisit_cumin:
    show bg stargazingfun_3
    $ renpy.pause(1.5,hard=True)
    show bg stargazingfun_8_1
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_8_2
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_8_3
    $ renpy.pause()
    pov "Oh- my God! [sister]-!"
    sis "It's okay, [povname]. I'm on the pill, I planned ahead of time."
    pov "{i}*Huff huff*{/i} You- evil- genius."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_stargazing_fun_revisit_cumin_0:
    show bg stargazingfun_3_0
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_1
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_2
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_3
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_4
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_5
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_6
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_7
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_8
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_7_9
    $ renpy.pause()
    pov "Oh- my God! [sister]-!"
    sis "It's okay, [povname]. I'm on the pill, I planned ahead of time."
    pov "{i}*Huff huff*{/i} You- evil- genius."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Cum Out
label lbl_stargazing_fun_revisit_cumout:
    show bg stargazingfun_3
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_4
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_5
    $ renpy.pause(0.5,hard=True)
    show bg stargazingfun_6_0
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_6_1
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_6_2
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_6_3
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_6_4
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_6_5
    $ renpy.pause(0.3,hard=True)
    show bg stargazingfun_6_6
    $ renpy.pause()
    sis "Oh- fuckkk...."
    pov "Oh, fuck- that felt so good..."
    pov "Shit... What are we gonna do about this mess? Do you have a towel?"
    sis "Nope. Don't be a pussy and just rub it in like sunscreen."
    sis "Take a shower later."
    pov "Easy for you to say, you're not the one covered in cum."
    sis "Now you know the feeling. Hahahaha!"
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
