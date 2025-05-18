## Mom Midnight Fun ##
label lbl_mom_midnight_fun:
    #default mommidnightfunbj_counter = 0
    if inventory.has_item(Items.fbpwmag1) and mum_path > 26:
        $ mommidnightfun = 2
        $ fbpwmag1 = 1
        $ inventory.drop(Items.fbpwmag1)
        $ hardpause(0.3)
        jump lbl_mom_midnight_fun_grind
    else:
        jump lbl_mom_midnight_fun_bj


label lbl_mom_midnight_fun_bj:

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

label lbl_mom_midnight_fun_bj_0:
    #$ mommidnightfunbj_counter = 0

label lbl_mom_midnight_fun_bj_1:
    #$ mommidnightfunbj_counter += 1
    #show bg mommidnightfunbj_3
    #$ renpy.pause(0.3,hard=True)
    #show bg mommidnightfunbj_4
    #$ renpy.pause(0.1,hard=True)
    #show bg mommidnightfunbj_5
    #$ renpy.pause(0.2,hard=True)
    #show bg mommidnightfunbj_6
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and mommidnightfunbj_counter == 4:
    #    jump lbl_mom_midnight_fun_bj_cum
    #elif skill_sta <= 14 and mommidnightfunbj_counter == 6:
    #    jump lbl_mom_midnight_fun_bj_2
    #elif skill_sta <= 20 and mommidnightfunbj_counter == 8:
    #    jump lbl_mom_midnight_fun_bj_2
    #else:
    #    jump lbl_mom_midnight_fun_bj_1
    scene img_mom_midnight_fun_bj_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_midnight_fun_bj_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_midnight_fun_bj_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_midnight_fun_bj_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_midnight_fun_bj_1

image img_mom_midnight_fun_bj_1:
    "bg mommidnightfunbj_3"
    pause 0.3
    "bg mommidnightfunbj_4"
    pause 0.1
    "bg mommidnightfunbj_5"
    pause 0.2
    "bg mommidnightfunbj_6"
    pause 0.3
    repeat

label lbl_mom_midnight_fun_bj_2:
    #$ mommidnightfunbj_counter += 1
    #show bg mommidnightfunbj_3
    #$ renpy.pause(0.3,hard=True)
    #show bg mommidnightfunbj_5
    #$ renpy.pause(0.2,hard=True)
    #show bg mommidnightfunbj_6
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mommidnightfunbj_counter == 14:
    #    jump lbl_mom_midnight_fun_bj_cum
    #elif skill_sta <= 20 and mommidnightfunbj_counter == 16:
    #    jump lbl_mom_midnight_fun_bj_3
    #else:
    #    jump lbl_mom_midnight_fun_bj_2
    scene img_mom_midnight_fun_bj_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_midnight_fun_bj_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_midnight_fun_bj_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_midnight_fun_bj_2

image img_mom_midnight_fun_bj_2:
    "bg mommidnightfunbj_3"
    pause 0.3
    "bg mommidnightfunbj_5"
    pause 0.2
    "bg mommidnightfunbj_6"
    pause 0.2
    repeat

label lbl_mom_midnight_fun_bj_3:
    #$ mommidnightfunbj_counter += 1
    #show bg mommidnightfunbj_3
    #$ renpy.pause(0.2,hard=True)
    #show bg mommidnightfunbj_5
    #$ renpy.pause(0.1,hard=True)
    #show bg mommidnightfunbj_6
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mommidnightfunbj_counter == 24:
    #    jump lbl_mom_midnight_fun_bj_cum
    #else:
    #    jump lbl_mom_midnight_fun_bj_3
    scene img_mom_midnight_fun_bj_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_midnight_fun_bj_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_midnight_fun_bj_3

image img_mom_midnight_fun_bj_3:
    "bg mommidnightfunbj_3"
    pause 0.2
    "bg mommidnightfunbj_5"
    pause 0.1
    "bg mommidnightfunbj_6"
    pause 0.2
    repeat

label lbl_mom_midnight_fun_bj_cum:
    call screen scr_mom_midnight_fun_bj_cum

screen scr_mom_midnight_fun_bj_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_bj_cumchoice")

label lbl_mom_midnight_fun_bj_cumchoice:

    menu:
        "Cum Inside":
            jump lbl_mom_midnight_fun_bj_cumin
        "Cum Outside":
            jump lbl_mom_midnight_fun_bj_cumout

label lbl_mom_midnight_fun_bj_cumin:
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
    $ renpy.pause()

    jump lbl_mom_midnight_fun_bj_end

label lbl_mom_midnight_fun_bj_cumout:
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
    $ renpy.pause()

label lbl_mom_midnight_fun_bj_end:
    if mum_path == 23:
        $ townmap_enabled = 0
        $ mum_path = 24

    jump lbl_mybedroom_night_sleep

label lbl_mom_midnight_fun_grind:
    scene black
    with fade
    $ renpy.pause

    scene bg mommidnightfungrind_1
    with fade
    show bg mommidnightfungrind_3
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_1
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_1
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_1
    $ renpy.pause()
    if mommidnightfun == 2:
        mum "Oh.. hey, honey."
        mum "I found this in your bag and well..."
        show bg mommidnightfungrind_3
        mum "Hehe, I can't help but find it weird how you could pick me over any of these beautiful young women."
        show bg mommidnightfungrind_1
        mum "You must love me a lot, don't you?"
    else:
        show bg mommidnightfungrind_3
        mum "Just relax, alright, sweetie?"
        show bg mommidnightfungrind_1
        mum "Let Mom enjoy herself..."

label lbl_mom_midnight_fun_grind_0:
    $ mommidnightfungrind_counter = 0

label lbl_mom_midnight_fun_grind_1:
    $ mommidnightfungrind_counter += 1
    show bg mommidnightfungrind_1
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.4,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 7 and mommidnightfungrind_counter == 4:
        jump lbl_mom_midnight_fun_grind_cum
    elif skill_sta <= 14 and mommidnightfungrind_counter == 6:
        jump lbl_mom_midnight_fun_grind_2
    elif skill_sta <= 20 and mommidnightfungrind_counter == 8:
        jump lbl_mom_midnight_fun_grind_2
    else:
        jump lbl_mom_midnight_fun_grind_1

label lbl_mom_midnight_fun_grind_2:
    $ mommidnightfungrind_counter += 1
    show bg mommidnightfungrind_1
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.3,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 14 and mommidnightfungrind_counter == 14:
        jump lbl_mom_midnight_fun_grind_cum
    elif skill_sta <= 20 and mommidnightfungrind_counter == 16:
        jump lbl_mom_midnight_fun_grind_3
    else:
        jump lbl_mom_midnight_fun_grind_2

label lbl_mom_midnight_fun_grind_3:
    $ mommidnightfungrind_counter += 1
    show bg mommidnightfungrind_1
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_3
    $ renpy.pause(0.2,hard=True)
    show bg mommidnightfungrind_2
    $ renpy.pause(0.2,hard=True)
    if skill_sta <= 20 and mommidnightfungrind_counter == 24:
        jump lbl_mom_midnight_fun_grind_cum
    else:
        jump lbl_mom_midnight_fun_grind_3

label lbl_mom_midnight_fun_grind_cum:
    call screen scr_mom_midnight_fun_grind_cum

screen scr_mom_midnight_fun_grind_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_grind_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_midnight_fun_grind_cumout")

label lbl_mom_midnight_fun_grind_cumout:
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
    $ renpy.pause()
    pov "."
    pov ".."
    pov "..."
    pov "Worth the money..."
    if mum_points <= 9:
        $ mum_points += 1
        $ renpy.notify("Your relationship with Mom has increased")
    else:
        $ mum_points = 10
    $ mommidnightfun = 0

    jump lbl_mybedroom_night_sleep
