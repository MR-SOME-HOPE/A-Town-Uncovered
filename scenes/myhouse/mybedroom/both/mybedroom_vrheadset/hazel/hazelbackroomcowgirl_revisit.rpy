## Hazel Backroom Cowgirl
label lbl_hazel_backroom_cowgirl_revisit_0:
    # if hscene_xray == 0:
    #     jump lbl_hazel_backroom_cowgirl_revisit_1
    # else:
    #     jump lbl_hazel_backroom_cowgirl_revisit_1_0

    jump lbl_hazel_backroom_cowgirl_revisit_1

####################
## Stage 1
label lbl_hazel_backroom_cowgirl_revisit_1:
    scene img_hazel_backroom_cowgirl_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_1

image img_hazel_backroom_cowgirl_stage_1:
    "bg hazelbackroomcowgirl_1"
    pause 0.2
    "bg hazelbackroomcowgirl_2"
    pause 0.2
    "bg hazelbackroomcowgirl_3"
    pause 0.2
    "bg hazelbackroomcowgirl_4"
    pause 0.2
    "bg hazelbackroomcowgirl_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_hazel_backroom_cowgirl_revisit_2:
    scene img_hazel_backroom_cowgirl_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_2

image img_hazel_backroom_cowgirl_stage_2:
    "bg hazelbackroomcowgirl_1"
    pause 0.2
    "bg hazelbackroomcowgirl_3"
    pause 0.2
    "bg hazelbackroomcowgirl_4"
    pause 0.2
    "bg hazelbackroomcowgirl_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_hazel_backroom_cowgirl_revisit_3:
    scene img_hazel_backroom_cowgirl_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hazel_backroom_cowgirl_revisit_3

image img_hazel_backroom_cowgirl_stage_3:
    "bg hazelbackroomcowgirl_1"
    pause 0.2
    "bg hazelbackroomcowgirl_4"
    pause 0.2
    "bg hazelbackroomcowgirl_5"
    pause 0.2
    repeat

####################
## Cum
label lbl_hazel_backroom_cowgirl_revisit_menu:
    call screen scr_hazel_backroom_cowgirl_revisit_menu

screen scr_hazel_backroom_cowgirl_revisit_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hazel_backroom_cowgirl_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hazel_backroom_cowgirl_revisit_cum")

label lbl_hazel_backroom_cowgirl_revisit_cum:
    pov "Oh fuck- Hazel, I'm about to cum..."
    menu:
        "Cum inside":
            haz "Mhmm? And what do you want me to do about it?"
            pov "Fuck-"
            jump lbl_hazel_backroom_cowgirl_revisit_cumin

        "Cum outside":
            haz "Okay okay, hold your horses."
            pov "Mhmphh-"
            jump lbl_hazel_backroom_cowgirl_revisit_cumout

####################
## CUM IN
label lbl_hazel_backroom_cowgirl_revisit_cumin:
    scene bg hazelbackroomcowgirl_4
    $ renpy.pause(1.5,hard=True)
    show bg hazelbackroomcowgirl_6_1
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_6_2
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_6_3
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_6_4
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_6_5
    $ renpy.pause()
    haz "Oh~ There we go, [povname]."
    haz "{i}*Pants*{/i} That feels so hot and gooey."
    pov "{i}*Huff*{/i} That felt amazing."
    haz "Yeah- how the fuck do you manage to cum so much it overspills?"
    pov "I don't know-"
    pov "Healthy mind, healthy body?"
    haz "Tch- You put cum-toys to shame, [povname]."
    haz "Jesus Christ, I'm so fucking full."
    pov "Can we stay like this for a bit?"
    haz "I've gotta make sure no one steals anything, [povname]."
    haz "Oh- and also, don't forget to buy that lube."
    haz "You've felt first hand how good it is."
    pov "Alright, alright."

    scene black
    with fade
    $ renpy.pause()
    "After cleaning up..."

    $ gtime += 1

    if gtime <= 1:
        scene bg adultstore_day
        with fade

        jump lbl_adultstore_day_setup

    else:
        scene bg street_night
        with fade

        jump lbl_street_night_setup

####################
## CUM OUT
label lbl_hazel_backroom_cowgirl_revisit_cumout:
    scene bg hazelbackroomcowgirl_4
    $ renpy.pause(0.3,hard=True)
    scene bg hazelbackroomcowgirl_5
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_0
    $ renpy.pause(0.5,hard=True)
    show bg hazelbackroomcowgirl_7_1
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_2
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_3
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_4
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_5
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_6
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_7
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_8
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_9
    $ renpy.pause(0.3,hard=True)
    show bg hazelbackroomcowgirl_7_10
    $ renpy.pause()
    haz "Oh~ There we go, [povname]."
    haz "{i}*Pants*{/i} God- the way your cock felt pushing all that out."
    pov "{i}*Huff*{/i} I'm- a- fucking- mess."
    haz "Hahahaha~ Yeah, yeah you are."
    pov "Can you- get me a towel?"
    haz "Nah, I'll just leave you like this."
    haz "See ya [povname]."
    pov "Hey!"
    haz "I'm joking, stupid."
    haz "God, you came so fucking much."
    haz "Tch- You put cum-toys to shame, [povname]."
    haz "Oh- that reminds me, don't forget to buy that lube."
    haz "You've felt first hand how good it is."
    pov "Alright, alright."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
