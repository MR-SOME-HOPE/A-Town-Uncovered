## Mom Midnight Fun ##


label lbl_mom_midnight_fun_bj_revisit:
    $ vrheadset_revisitcounter = 0
    scene black
    with fade
    $ renpy.pause
    idk "{i}*Slurp-p-p-p*{/i}"
    pov "Mmmm...?"
    scene bg mommidnightfunbj_3
    with fade
    $ renpy.pause()
    show bg mommidnightfunbj_1
    mum "Hi, honey."
    mum "Sorry if I disturbed you, I'm trying to be as quiet as I can."
    show bg mommidnightfunbj_2
    if winc == 0:
        pov "[missus]-?"
    else:
        pov "Mom-?"
    mum "Shh shh shh, just relax, honey."
    jump lbl_mom_midnight_fun_bj_revisit_0

label lbl_mom_midnight_fun_bj_revisit_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_mom_midnight_fun_bj_revisit_1

label lbl_mom_midnight_fun_bj_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg mommidnightfunbj_3
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_4
    $ renpy.pause(0.1,hard=True)
    show bg mommidnightfunbj_5
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfunbj_6
    $ renpy.pause(0.3,hard=True)
    jump lbl_mom_midnight_fun_bj_revisit_counter

label lbl_mom_midnight_fun_bj_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg mommidnightfunbj_3
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_5
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfunbj_6
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_midnight_fun_bj_revisit_counter

label lbl_mom_midnight_fun_bj_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg mommidnightfunbj_3
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfunbj_5
    $ renpy.pause(0.1,hard=True)
    show bg mommidnightfunbj_6
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_midnight_fun_bj_revisit_counter


label lbl_mom_midnight_fun_bj_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_mom_midnight_fun_bj_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_mom_midnight_fun_bj_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_mom_midnight_fun_bj_revisit
    else:
        jump lbl_mom_midnight_fun_bj_revisit_1


screen scr_mom_midnight_fun_bj_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_bj_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_bj_revisit_cumchoice")

label lbl_mom_midnight_fun_bj_revisit_cumchoice:

    menu:
        "Cum Inside":
            jump lbl_mom_midnight_fun_bj_revisit_cumin
        "Cum Outside":
            jump lbl_mom_midnight_fun_bj_revisit_cumout

label lbl_mom_midnight_fun_bj_revisit_cumin:
    show bg mommidnightfunbj_3
    $ renpy.pause(0.5,hard=True)
    show bg mommidnightfunbj_6
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_7
    $ renpy.pause(1,hard=True)
    show bg mommidnightfunbj_8
    $ renpy.pause(0.7,hard=True)
    show bg mommidnightfunbj_9
    $ renpy.pause(0.7,hard=True)
    show bg mommidnightfunbj_10
    $ renpy.pause()
    show bg mommidnightfunbj_11
    $ renpy.pause(1.5,hard=True)
    show bg mommidnightfunbj_12
    $ renpy.pause()
    mum "Goodnight, sweetie."
    mum "Hope you have a good night sleep."
    mum "Sorry if I interrupted a good dream."
    if winc == 0:
        pov "Don't worry, [missus]... I wasn't missing out on anything."
    else:
        pov "Don't worry, Mom... I wasn't missing out on anything."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

label lbl_mom_midnight_fun_bj_revisit_cumout:
    show bg mommidnightfunbj_3
    $ renpy.pause(0.5,hard=True)
    show bg mommidnightfunbj_13
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_14
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_15
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_16
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_17
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_18
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_19
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_20
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfunbj_21
    $ renpy.pause()
    if winc == 0:
        pov "Are you alive, [missus]?"
    else:
        pov "Are you alive, Mom?"
    show bg mommidnightfunbj_22
    mum "Yes, [povname]. Just in a... sticky situation."
    pov "I would laugh but I'm sleepy, tired, and exhausted."
    mum "Naww, goodnight, honey. Sweet dreams. I'll go clean up."

    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection


label lbl_mom_midnight_fun_grind_revisit:
    $ vrheadset_revisitcounter = 0
    scene bg mommidnightfungrind_1
    with fade
    show bg mommidnightfungrind_3
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_1
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_1
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_1
    $ renpy.pause()
    mum "Oh.. hey, honey."
    mum "I found this in your bag and well..."
    show bg mommidnightfungrind_3
    mum "Hehe, I can't help but find it weird how you could pick me over any of these beautiful young women."
    show bg mommidnightfungrind_1
    mum "You must love me a lot, don't you?"
    jump lbl_mom_midnight_fun_grind_revisit_0

label lbl_mom_midnight_fun_grind_revisit_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_mom_midnight_fun_grind_revisit_1

label lbl_mom_midnight_fun_grind_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg mommidnightfungrind_2
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.22,hard=True)
    show bg mommidnightfungrind_1
    $ renpy.pause(0.22,hard=True)
    jump lbl_mom_midnight_fun_grind_revisit_counter

label lbl_mom_midnight_fun_grind_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg mommidnightfungrind_1
    $ renpy.pause(0.195,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.195,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.195,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.195,hard=True)
    jump lbl_mom_midnight_fun_grind_revisit_counter

label lbl_mom_midnight_fun_grind_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg mommidnightfungrind_1
    $ renpy.pause(0.15,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.15,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.085,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.15,hard=True)
    jump lbl_mom_midnight_fun_grind_revisit_counter

label lbl_mom_midnight_fun_grind_revisit_counter:
    if vrheadset_revisitcounter >= 30 and vrheadset_revisitcounter <= 69:
        jump lbl_mom_midnight_fun_grind_revisit_2
    if vrheadset_revisitcounter >= 70 and vrheadset_revisitcounter <= 119:
        jump lbl_mom_midnight_fun_grind_revisit_3
    elif vrheadset_revisitcounter >= 120:
        call screen scr_mom_midnight_fun_grind_revisit
    else:
        jump lbl_mom_midnight_fun_grind_revisit_1

screen scr_mom_midnight_fun_grind_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_grind_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_grind_revisit_cumout")

label lbl_mom_midnight_fun_grind_revisit_cumout:
    show bg mommidnightfungrind_4
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_5
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_6
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_7
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_8
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_9
    $ renpy.pause()
    mum "What a mess, hehehe. Sorry about that but I've gotta get back to my room."
    mum "Don't stain the bedsheets, honey."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
