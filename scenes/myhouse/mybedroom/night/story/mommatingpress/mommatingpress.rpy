## Mom Mating Press
label lbl_mom_mating_press:
    ## PRE STORY
    scene bg mommatingpress_1
    with fade

    jump lbl_mom_mating_press_0

label lbl_mom_mating_press_0:
    # if hscene_xray == 0:
    #     jump lbl_mom_mating_press_1
    # else:
    #     jump lbl_mom_mating_press_1_0

    jump lbl_mom_mating_press_1

####################
## Stage 1
label lbl_mom_mating_press_1:
    scene img_mom_mating_press_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_mating_press_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_mating_press_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_mating_press_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_mating_press_1

image img_mom_mating_press_stage_1:
    "bg mommatingpress_1"
    pause 0.2
    "bg mommatingpress_2"
    pause 0.2
    "bg mommatingpress_3"
    pause 0.2
    "bg mommatingpress_4"
    pause 0.2
    "bg mommatingpress_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_mom_mating_press_2:
    scene img_mom_mating_press_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_mating_press_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_mating_press_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_mating_press_2

image img_mom_mating_press_stage_2:
    "bg mommatingpress_5"
    pause 0.2
    "bg mommatingpress_7"
    pause 0.2
    "bg mommatingpress_8"
    pause 0.2
    "bg mommatingpress_6"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_mom_mating_press_3:
    scene img_mom_mating_press_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_mating_press_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_mating_press_3

image img_mom_mating_press_stage_3:
    "bg mommatingpress_9"
    pause 0.2
    "bg mommatingpress_12"
    pause 0.2
    "bg mommatingpress_10"
    pause 0.2
    repeat

####################
## Cum
label lbl_mom_mating_press_menu:
    call screen scr_mom_mating_press_menu

screen scr_mom_mating_press_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_mating_press_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_mating_press_cum")

label lbl_mom_mating_press_cum:
    if winc == 1:
        pov "Ah- mom- I'm gonna cum-"
    else:
        pov "Ah- [missus]- I'm gonna cum-"
    menu:
        "Cum inside":
            mum "Just let it all inside me."
            mum "I want to feel it all."
            pov "{i}*Mmmfphh*{/i}"
            jump lbl_mom_mating_press_cumin
        "Cum all over her":
            mum "Pull it out, sweetie."
            mum "Cover me in it."
            pov "{i}*Mmmfphh*{/i}"
            jump lbl_mom_mating_press_cumout

####################
## CUM IN
label lbl_mom_mating_press_cumin:
    scene bg mommatingpress_8
    $ renpy.pause(2.0,hard=True)
    show bg mommatingpress_14_1
    $ renpy.pause(0.4,hard=True)
    show bg mommatingpress_14_2
    $ renpy.pause(0.4,hard=True)
    show bg mommatingpress_14_3
    $ renpy.pause(0.4,hard=True)
    show bg mommatingpress_14_4
    $ renpy.pause()
    mum "Oh- gosh, [povname]."
    mum "It feels so hot tonight."
    pov "{i}*Pants*{/i}"
    pov "Yeah?"
    pov "Is- is that good?"
    mum "Hehehe~ Yes, baby."
    mum "It feels really nice inside me."
    mum "You did so good~"
    if winc == 1:
        pov "You too, mom."
    else:
        pov "You too, [missus]."
    mum "Hehe~ I just laid here."
    pov "Yeah but you getting as wet as you did made it feel so much better."
    mum "I love you, [povname]."
    mum "Always will."
    pov "I love you too~"
    mum "Now, let's get cleaned up. I'm about to sleep like a rock."
    pov "Okay, give me a second."

    scene black
    with fade
    $ renpy.pause()
    "After cleaning up..."
    scene bg mybedroom_night
    with fade

    $ gtime = 3

    jump lbl_mybedroom_night_setup

####################
## CUM OUT
label lbl_mom_mating_press_cumout:
    scene bg mommatingpress_5
    $ renpy.pause(0.3,hard=True)
    show bg mommatingpress_13_1
    $ renpy.pause(0.5,hard=True)
    show bg mommatingpress_13_2
    $ renpy.pause(0.3,hard=True)
    show bg mommatingpress_13_3
    $ renpy.pause(0.3,hard=True)
    show bg mommatingpress_13_4
    $ renpy.pause(0.3,hard=True)
    show bg mommatingpress_13_5
    $ renpy.pause(0.3,hard=True)
    show bg mommatingpress_13_6
    $ renpy.pause(0.3,hard=True)
    show bg mommatingpress_13_7
    $ renpy.pause()
    mum "Oh- gosh, [povname]."
    mum "It feels so hot tonight."
    pov "{i}*Pants*{/i}"
    pov "Yeah?"
    pov "Is- is that good?"
    mum "Hehehe~ Yes, baby."
    mum "It feels really nice all over me."
    mum "You did so good~"
    if winc == 1:
        pov "You too, mom."
    else:
        pov "You too, [missus]."
    mum "Hehe~ I just laid here."
    pov "Yeah but you getting as wet as you did made it feel so much better."
    mum "I love you, [povname]."
    mum "Always will."
    pov "I love you too~"
    mum "Now, let's get cleaned up. I'm about to sleep like a rock."
    mum "Quick, it's dripping down my chest."
    pov "Okay, give me a second."

    scene black
    with fade
    $ renpy.pause()
    "After cleaning up..."
    scene bg mybedroom_night
    with fade

    $ gtime = 3

    jump lbl_mybedroom_night_setup
