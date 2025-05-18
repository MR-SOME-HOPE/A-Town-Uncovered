## Mom Kitchen Seat Fun
default mom_kitchenseatfun = 0

## PRE STORY
label lbl_mom_kitchen_seat_fun:
    show pov embarrassed_talk at left
    show mum neutral at right
    if winc == 1:
        pov "Mom... can I-"
    else:
        pov "[missus]... can I-"
    show mum confused at right
    pov "Can we..."
    pov "Can we have a quickie right now?"
    show pov embarrassed at left
    show mum confused_talk at right
    mum "Right now, honey?"
    show pov sad_talk at left
    show mum confused at right
    pov "Yeah- I got a boner that won't go away."
    show pov sad at left
    show mum confused_talk at right
    mum "I'm reading, sweetie..."
    show pov sad_talk at left
    show mum embarrassed at right
    pov "Please?"
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "{i}*Sigh*{/i} Alright, my baby."
    show mum neutral_talk at right
    mum "Let me just turn my seat around and you can take me from behind."
    mum "Okay?"
    show pov neutral_talk at left
    show mum neutral at right
    if winc == 1:
        pov "Thanks, mom."
    else:
        pov "Thanks, [missus]."

    scene bg momkitchenseatfun_pre
    with fade
    pov "Your butt looks so nice from this angle."
    mum "Oh hush, you're gonna make me blush, [povname]."
    pov "Your lips feels really soft today~"
    mum "Unlike your cock."
    pov "Opposites attract as they say."
    if winc == 1:
        pov "I'm ready to stick it in, [missus]."
    else:
        pov "I'm ready to stick it in, mom."
    mum "Be gentle, sweetie."
    mum "And try and be quick, I have to cook soon."
    pov "I know, I know."

    jump lbl_mom_kitchen_seat_fun_1

image bg momkitchenseatfun_pre:
    "bg momkitchenseatfun_0_1"
    pause 0.6
    "bg momkitchenseatfun_0_2"
    pause 0.6
    repeat

label lbl_mom_kitchen_seat_fun_0:
    jump lbl_mom_kitchen_seat_fun_1
    # if hscene_xray == 0:
    #     jump lbl_mom_kitchen_seat_fun_1
    # else:
    #     jump lbl_mom_kitchen_seat_fun_1_0

####################
## Stage 1
label lbl_mom_kitchen_seat_fun_1:
    scene img_mom_kitchen_seat_fun_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_kitchen_seat_fun_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_kitchen_seat_fun_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_kitchen_seat_fun_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_kitchen_seat_fun_1

image img_mom_kitchen_seat_fun_stage_1:
    "bg momkitchenseatfun_1"
    pause 0.2
    "bg momkitchenseatfun_2"
    pause 0.2
    "bg momkitchenseatfun_3"
    pause 0.2
    "bg momkitchenseatfun_4"
    pause 0.2
    "bg momkitchenseatfun_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_mom_kitchen_seat_fun_2:
    scene img_mom_kitchen_seat_fun_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_kitchen_seat_fun_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_kitchen_seat_fun_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_kitchen_seat_fun_2

image img_mom_kitchen_seat_fun_stage_2:
    "bg momkitchenseatfun_1"
    pause 0.2
    "bg momkitchenseatfun_2"
    pause 0.2
    "bg momkitchenseatfun_4"
    pause 0.2
    "bg momkitchenseatfun_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_mom_kitchen_seat_fun_3:
    scene img_mom_kitchen_seat_fun_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_kitchen_seat_fun_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_kitchen_seat_fun_3

image img_mom_kitchen_seat_fun_stage_3:
    "bg momkitchenseatfun_1"
    pause 0.2
    "bg momkitchenseatfun_3"
    pause 0.2
    "bg momkitchenseatfun_5"
    pause 0.2
    repeat

####################
## Cum
label lbl_mom_kitchen_seat_fun_menu:
    call screen scr_mom_kitchen_seat_fun_menu

screen scr_mom_kitchen_seat_fun_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_kitchen_seat_fun_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_kitchen_seat_fun_cumchoice")

label lbl_mom_kitchen_seat_fun_cumchoice:
    menu:
        "Cum inside":
            jump lbl_mom_kitchen_seat_fun_cumin
            # if hscene_xray == 0:
            #     jump lbl_mom_kitchen_seat_fun_cumin
            # else:
            #     jump lbl_mom_kitchen_seat_fun_cumin_0
        "Cum on her":
            jump lbl_mom_kitchen_seat_fun_cumout

####################
## Cum In
label lbl_mom_kitchen_seat_fun_cumin:
    pov "I'm gonna cum inside-"
    mum "That's alright, baby."
    pov "I'm cummi-"
    pov "{i}*Arrgghh*{/i}"
    scene bg momkitchenseatfun_3
    $ renpy.pause(0.2,hard=True)
    show bg momkitchenseatfun_4
    $ renpy.pause(1.5,hard=True)
    show bg momkitchenseatfun_4_1
    $ renpy.pause(0.4,hard=True)
    show bg momkitchenseatfun_4_2
    $ renpy.pause(0.4,hard=True)
    show bg momkitchenseatfun_4_3
    $ renpy.pause(0.4,hard=True)
    show bg momkitchenseatfun_4_4
    mum "Oh my-"
    mum "I can feel my tummy expanding."
    pov "{i}*Pants*{/i}"
    mum "Good job, cupcake-"
    if winc == 1:
        pov "{i}*Pants*{/i} Mooom- don't call me cupcake when my cum's inside you..."
    else:
        pov "{i}*Pants*{/i} [missus]- don't call me cupcake when my cum's inside you..."
    pov "It's embarrasing."
    mum "I'm sorry, my little creampie."
    pov "..."
    pov "I'll go grab some tissues."
    pov "What's for dinner by the way."
    mum "{i}*Groan*{/i} Every day with that question."

    scene black
    with fade
    $ renpy.pause()
    "After a bit of cleaning up..."
    scene bg mykitchen_day
    with fade

    $ mom_kitchenseatfun = 1

    jump lbl_mykitchen_day_setup

####################
## Cum Out
label lbl_mom_kitchen_seat_fun_cumout:
    pov "I'm gonna cum-"
    mum "Cum all over my pussy lips, baby."
    pov "I'm cummi-"
    pov "{i}*Arrgghh*{/i}"
    scene bg momkitchenseatfun_3
    $ renpy.pause(0.2,hard=True)
    show bg momkitchenseatfun_2
    $ renpy.pause(0.2,hard=True)
    show bg momkitchenseatfun_1
    $ renpy.pause(0.2,hard=True)
    show bg momkitchenseatfun_0_1
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_1
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_2
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_3
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_4
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_5
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_6
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_7
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_8
    $ renpy.pause(0.3,hard=True)
    show bg momkitchenseatfun_6_9
    mum "Oh my-"
    mum "That feels so hot-."
    pov "{i}*Pants*{/i}"
    mum "Good job, muffincake-"
    if winc == 1:
        pov "{i}*Pants*{/i} Mooom- don't call me muffincake when my cum's all over you..."
    else:
        pov "{i}*Pants*{/i} [missus]- don't call me cupcake when my cum's all over you..."
    pov "It's embarrasing."
    mum "You're embarrassed? Right after having coitous with me?"
    pov "..."
    pov "I'll go grab some tissues."
    mum "Yes, please do. You made a mess all over my seat."
    mum "None got on my dress, right?"
    pov "You're good, don't worry."
    pov "What's for dinner by the way."
    mum "{i}*Groan*{/i} Every day with that question."

    scene black
    with fade
    $ renpy.pause()
    "After a bit of cleaning up..."
    scene bg mylivingroom_day
    with fade

    $ mom_kitchenseatfun = 1

    jump lbl_mykitchen_day_setup
