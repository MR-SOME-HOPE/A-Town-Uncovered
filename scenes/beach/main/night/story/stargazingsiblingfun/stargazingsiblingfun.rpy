## Stargazing Sibling Fun ##
label lbl_stargazing_fun:
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

    jump lbl_stargazing_fun_0

label lbl_stargazing_fun_repeat:
    scene black
    with fade
    $ renpy.pause()
    "At the beach with a lot less clothes on..."
    if hscene_xray == 0:
        scene bg stargazingfun_1
        with dissolve
    else:
        scene bg stargazingfun_1_0
        with dissolve
    sis "I- can't wait any longer, [povname]."
    pov "[sister], we just got here."
    sis "I know- I know, just shut up and help me get warm."

    jump lbl_stargazing_fun_0

label lbl_stargazing_fun_0:
    #$ stargazing_fun_counter = 0
    if hscene_xray == 0:
        jump lbl_stargazing_fun_1
    else:
        jump lbl_stargazing_fun_1_0

####################
## Stage 1
label lbl_stargazing_fun_1:
    scene img_stargazing_fun_stage_1
    #$ stargazing_fun_counter += 1
    #show bg stargazingfun_1
    #$ renpy.pause(0.3,hard=True)
    #show bg stargazingfun_2
    #$ renpy.pause(0.1,hard=True)
    #show bg stargazingfun_3
    #$ renpy.pause(0.3,hard=True)
    #show bg stargazingfun_4
    #$ renpy.pause(0.3,hard=True)
    #show bg stargazingfun_5
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and stargazing_fun_counter == 4:
    #    jump lbl_stargazing_fun_cum
    #elif skill_sta <= 14 and stargazing_fun_counter == 6:
    #    jump lbl_stargazing_fun_2
    #elif skill_sta <= 20 and stargazing_fun_counter == 8:
    #    jump lbl_stargazing_fun_2
    #else:
    #    jump lbl_stargazing_fun_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_stargazing_fun_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_stargazing_fun_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_1

image img_stargazing_fun_stage_1:
    "bg stargazingfun_1"
    pause 0.3
    "bg stargazingfun_2"
    pause 0.1
    "bg stargazingfun_3"
    pause 0.3
    "bg stargazingfun_4"
    pause 0.3
    "bg stargazingfun_5"
    pause 0.3
    repeat

####################
## Stage 1 XRAY
label lbl_stargazing_fun_1_0:
    scene img_stargazing_fun_stage_1_0
    #$ stargazing_fun_counter += 1
    #show bg stargazingfun_1_0
    #$ renpy.pause(0.3,hard=True)
    #show bg stargazingfun_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg stargazingfun_3_0
    #$ renpy.pause(0.3,hard=True)
    #show bg stargazingfun_4_0
    #$ renpy.pause(0.3,hard=True)
    #show bg stargazingfun_5_0
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and stargazing_fun_counter == 4:
    #    jump lbl_stargazing_fun_cum
    #elif skill_sta <= 14 and stargazing_fun_counter == 6:
    #    jump lbl_stargazing_fun_2_0
    #elif skill_sta <= 20 and stargazing_fun_counter == 8:
    #    jump lbl_stargazing_fun_2_0
    #else:
    #    jump lbl_stargazing_fun_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_stargazing_fun_2_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_stargazing_fun_2_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_1_0

image img_stargazing_fun_stage_1_0:
    "bg stargazingfun_1_0"
    pause 0.3
    "bg stargazingfun_2_0"
    pause 0.1
    "bg stargazingfun_3_0"
    pause 0.3
    "bg stargazingfun_4_0"
    pause 0.3
    "bg stargazingfun_5_0"
    pause 0.3
    repeat

####################
## Stage 2
label lbl_stargazing_fun_2:
    scene img_stargazing_fun_stage_2
    #$ stargazing_fun_counter += 1
    #show bg stargazingfun_1
    #$ renpy.pause(0.2,hard=True)
    #show bg stargazingfun_2
    #$ renpy.pause(0.1,hard=True)
    #show bg stargazingfun_3
    #$ renpy.pause(0.2,hard=True)
    #show bg stargazingfun_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and stargazing_fun_counter == 16:
    #    jump lbl_stargazing_fun_cum
    #elif skill_sta <= 20 and stargazing_fun_counter == 18:
    #    jump lbl_stargazing_fun_3
    #else:
    #    jump lbl_stargazing_fun_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_stargazing_fun_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_stargazing_fun_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_2

image img_stargazing_fun_stage_2:
    "bg stargazingfun_1"
    pause 0.2
    "bg stargazingfun_2"
    pause 0.1
    "bg stargazingfun_3"
    pause 0.2
    "bg stargazingfun_4"
    pause 0.2
    repeat
####################
## Stage 2 XRAY
label lbl_stargazing_fun_2_0:
    scene img_stargazing_fun_stage_2_0
    #$ stargazing_fun_counter += 1
    #show bg stargazingfun_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg stargazingfun_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg stargazingfun_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg stargazingfun_4_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and stargazing_fun_counter == 16:
    #    jump lbl_stargazing_fun_cum
    #elif skill_sta <= 20 and stargazing_fun_counter == 18:
    #    jump lbl_stargazing_fun_3_0
    #else:
    #    jump lbl_stargazing_fun_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_stargazing_fun_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_stargazing_fun_3_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_2_0

image img_stargazing_fun_stage_2_0:
    "bg stargazingfun_1_0"
    pause 0.2
    "bg stargazingfun_2_0"
    pause 0.1
    "bg stargazingfun_3_0"
    pause 0.2
    "bg stargazingfun_4_0"
    pause 0.2
    repeat
####################
## Stage 3
label lbl_stargazing_fun_3:
    scene img_stargazing_fun_stage_3
    #$ stargazing_fun_counter += 1
    #show bg stargazingfun_1
    #$ renpy.pause(0.2,hard=True)
    #show bg stargazingfun_3
    #$ renpy.pause(0.1,hard=True)
    #show bg stargazingfun_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and stargazing_fun_counter == 30:
    #    jump lbl_stargazing_fun_cum
    #else:
    #    jump lbl_stargazing_fun_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_stargazing_fun_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_3

image img_stargazing_fun_stage_3:
    "bg stargazingfun_1"
    pause 0.2
    "bg stargazingfun_3"
    pause 0.1
    "bg stargazingfun_4"
    pause 0.2
    repeat
####################
## Stage 3 XRAY
label lbl_stargazing_fun_3_0:
    scene img_stargazing_fun_stage_3_0
    #$ stargazing_fun_counter += 1
    #show bg stargazingfun_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg stargazingfun_3_0
    #$ renpy.pause(0.1,hard=True)
    #show bg stargazingfun_4_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and stargazing_fun_counter == 24:
    #    jump lbl_stargazing_fun_cum
    #else:
    #    jump lbl_stargazing_fun_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_stargazing_fun_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_stargazing_fun_3_0

image img_stargazing_fun_stage_3_0:
    "bg stargazingfun_1_0"
    pause 0.2
    "bg stargazingfun_3_0"
    pause 0.1
    "bg stargazingfun_4_0"
    pause 0.2
    repeat
####################
## Cum Menu
label lbl_stargazing_fun_cum:
    #if hscene_xray == 0:
    #    scene bg stargazingfun_1
    #else:
    #    scene bg stargazingfun_1_0
    call screen scr_stargazing_fun_cum

screen scr_stargazing_fun_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_stargazing_fun_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_stargazing_fun_cumchoice")

label lbl_stargazing_fun_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_stargazing_fun_cumin
            else:
                jump lbl_stargazing_fun_cumin_0
        "Cum outside":
            jump lbl_stargazing_fun_cumout

####################
## Cum In
label lbl_stargazing_fun_cumin:
    scene bg stargazingfun_3
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

    if sister_hscenerevisit == 1:
        $ sister_hscenerevisit = 0
        scene black
        with fade
        "You both laid next to each and watched the night sky for a few minutes..."
        "Gently massaging each other's privates..."
        "..."
        "An hour later..."
        jump lbl_myhousefront_night
    else:
        jump lbl_stargazing_heart_to_heart_2

####################
## Cum In XRAY
label lbl_stargazing_fun_cumin_0:
    scene bg stargazingfun_3_0
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

    if sister_hscenerevisit == 1:
        $ sister_hscenerevisit = 0
        scene black
        with fade
        "You both laid next to each and watched the night sky for a few minutes..."
        "Gently massaging each other's privates..."
        "..."
        "An hour later..."
        jump lbl_myhousefront_night
    else:
        jump lbl_stargazing_heart_to_heart_2

####################
## Cum Out
label lbl_stargazing_fun_cumout:
    scene bg stargazingfun_3
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

    if sister_hscenerevisit == 1:
        $ sister_hscenerevisit = 0
        scene black
        with fade
        "You both laid next to each and watched the night sky for a few minutes..."
        "Gently massaging each other's privates..."
        "..."
        "An hour later..."
        jump lbl_myhousefront_night
    else:
        jump lbl_stargazing_heart_to_heart_2
