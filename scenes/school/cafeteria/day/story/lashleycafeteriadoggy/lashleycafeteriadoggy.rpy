## Lashley Cafeteria Doggy
label lbl_lashley_cafeteria_doggy:
    if hscene_xray == 0:
        scene bg lashleycafeteriadoggy_1
        with fade
    else:
        scene bg lashleycafeteriadoggy_1_0
        with fade

    jump lbl_lashley_cafeteria_doggy_0

####################
## Doggy Pre
label lbl_lashley_cafeteria_doggy_0_0:
    "Error 'lashleycafeteria_pre'"

    jump lbl_lashley_cafeteria_doggy_0

label lbl_lashley_cafeteria_doggy_0:
    #$ lashley_cafeteria_doggy_counter = 0
    if hscene_xray == 0:
        jump lbl_lashley_cafeteria_doggy_1
    else:
        jump lbl_lashley_cafeteria_doggy_1_0

####################
## Doggy Stage 1
label lbl_lashley_cafeteria_doggy_1:
    scene img_lashley_cafeteria_doggy_stage_1
    #$ lashley_cafeteria_doggy_counter += 1
    #show bg lashleycafeteriadoggy_1
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_2
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_3
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_4
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and lashley_cafeteria_doggy_counter == 4:
    #    jump lbl_lashley_cafeteria_doggy_cum
    #elif skill_sta <= 14 and lashley_cafeteria_doggy_counter == 6:
    #    jump lbl_lashley_cafeteria_doggy_2
    #elif skill_sta <= 20 and lashley_cafeteria_doggy_counter == 8:
    #    jump lbl_lashley_cafeteria_doggy_2
    #else:
    #    jump lbl_lashley_cafeteria_doggy_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_cafeteria_doggy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_cafeteria_doggy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_1

image img_lashley_cafeteria_doggy_stage_1:
    "bg lashleycafeteriadoggy_1"
    pause 0.2
    "bg lashleycafeteriadoggy_2"
    pause 0.2
    "bg lashleycafeteriadoggy_3"
    pause 0.3
    "bg lashleycafeteriadoggy_4"
    pause 0.3
    "bg lashleycafeteriadoggy_5"
    pause 0.2
    repeat

####################
## Doggy Stage 1 XRAY
label lbl_lashley_cafeteria_doggy_1_0:
    scene img_lashley_cafeteria_doggy_stage_1_0
    #$ lashley_cafeteria_doggy_counter += 1
    #show bg lashleycafeteriadoggy_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_3_0
    #$ renpy.pause(0.3,hard=True)
    #show bg lashleycafeteriadoggy_4_0
    #$ renpy.pause(0.3,hard=True)
    #show bg lashleycafeteriadoggy_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and lashley_cafeteria_doggy_counter == 4:
    #    jump lbl_lashley_cafeteria_doggy_cum
    #elif skill_sta <= 14 and lashley_cafeteria_doggy_counter == 6:
    #    jump lbl_lashley_cafeteria_doggy_2_0
    #elif skill_sta <= 20 and lashley_cafeteria_doggy_counter == 8:
    #    jump lbl_lashley_cafeteria_doggy_2_0
    #else:
    #    jump lbl_lashley_cafeteria_doggy_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_cafeteria_doggy_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_cafeteria_doggy_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_1_0

image img_lashley_cafeteria_doggy_stage_1_0:
    "bg lashleycafeteriadoggy_1_0"
    pause 0.2
    "bg lashleycafeteriadoggy_2_0"
    pause 0.2
    "bg lashleycafeteriadoggy_3_0"
    pause 0.3
    "bg lashleycafeteriadoggy_4_0"
    pause 0.3
    "bg lashleycafeteriadoggy_5_0"
    pause 0.2
    repeat

####################
## Doggy Stage 2
label lbl_lashley_cafeteria_doggy_2:
    scene img_lashley_cafeteria_doggy_stage_2
    #$ lashley_cafeteria_doggy_counter += 1
    #show bg lashleycafeteriadoggy_1
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_2
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_4
    #$ renpy.pause(0.3,hard=True)
    #show bg lashleycafeteriadoggy_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and lashley_cafeteria_doggy_counter == 14:
    #    jump lbl_lashley_cafeteria_doggy_cum
    #elif skill_sta <= 20 and lashley_cafeteria_doggy_counter == 16:
    #    jump lbl_lashley_cafeteria_doggy_3
    #else:
    #    jump lbl_lashley_cafeteria_doggy_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_cafeteria_doggy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_cafeteria_doggy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_2

image img_lashley_cafeteria_doggy_stage_2:
    "bg lashleycafeteriadoggy_1"
    pause 0.2
    "bg lashleycafeteriadoggy_2"
    pause 0.2
    "bg lashleycafeteriadoggy_4"
    pause 0.3
    "bg lashleycafeteriadoggy_5"
    pause 0.2
    repeat

####################
## Doggy Stage 2 XRAY
label lbl_lashley_cafeteria_doggy_2_0:
    scene img_lashley_cafeteria_doggy_stage_2_0
    #$ lashley_cafeteria_doggy_counter += 1
    #show bg lashleycafeteriadoggy_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_4_0
    #$ renpy.pause(0.3,hard=True)
    #show bg lashleycafeteriadoggy_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and lashley_cafeteria_doggy_counter == 14:
    #    jump lbl_lashley_cafeteria_doggy_cum
    #elif skill_sta <= 20 and lashley_cafeteria_doggy_counter == 16:
    #    jump lbl_lashley_cafeteria_doggy_3_0
    #else:
    #    jump lbl_lashley_cafeteria_doggy_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_cafeteria_doggy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_cafeteria_doggy_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_2_0

image img_lashley_cafeteria_doggy_stage_2_0:
    "bg lashleycafeteriadoggy_1_0"
    pause 0.2
    "bg lashleycafeteriadoggy_2_0"
    pause 0.2
    "bg lashleycafeteriadoggy_4_0"
    pause 0.3
    "bg lashleycafeteriadoggy_5_0"
    pause 0.2
    repeat

####################
## Doggy Stage 3
label lbl_lashley_cafeteria_doggy_3:
    scene img_lashley_cafeteria_doggy_stage_3
    #$ lashley_cafeteria_doggy_counter += 1
    #show bg lashleycafeteriadoggy_1
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_4
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and lashley_cafeteria_doggy_counter == 24:
    #    jump lbl_lashley_cafeteria_doggy_cum
    #else:
    #    jump lbl_lashley_cafeteria_doggy_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_cafeteria_doggy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_3

image img_lashley_cafeteria_doggy_stage_3:
    "bg lashleycafeteriadoggy_1"
    pause 0.2
    "bg lashleycafeteriadoggy_4"
    pause 0.2
    "bg lashleycafeteriadoggy_5"
    pause 0.2
    repeat

####################
## Doggy Stage 3 XRAY
label lbl_lashley_cafeteria_doggy_3_0:
    scene img_lashley_cafeteria_doggy_stage_3_0
    #$ lashley_cafeteria_doggy_counter += 1
    #show bg lashleycafeteriadoggy_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg lashleycafeteriadoggy_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and lashley_cafeteria_doggy_counter == 24:
    #    jump lbl_lashley_cafeteria_doggy_cum
    #else:
    #    jump lbl_lashley_cafeteria_doggy_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_cafeteria_doggy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_cafeteria_doggy_3_0

image img_lashley_cafeteria_doggy_stage_3_0:
    "bg lashleycafeteriadoggy_1_0"
    pause 0.2
    "bg lashleycafeteriadoggy_4_0"
    pause 0.2
    "bg lashleycafeteriadoggy_5_0"
    pause 0.2
    repeat

####################
## Doggy Cum
label lbl_lashley_cafeteria_doggy_cum:
    jump lbl_lashley_cafeteria_doggy_cum_2

label lbl_lashley_cafeteria_doggy_cum_2:
    #if hscene_xray == 0:
    #    scene bg lashleycafeteriadoggy_4
    #else:
    #    scene bg lashleycafeteriadoggy_4_0
    call screen scr_lashley_cafeteria_doggy_cum_2

screen scr_lashley_cafeteria_doggy_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashley_cafeteria_doggy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action If(hscene_xray == 0, Jump("lbl_lashley_cafeteria_doggy_cumin"), Jump("lbl_lashley_cafeteria_doggy_cumin_0"))

####################
## Doggy Cum In
label lbl_lashley_cafeteria_doggy_cumin:
    scene bg lashleycafeteriadoggy_7_0
    $ renpy.pause(1.5,hard=True)
    show bg lashleycafeteriadoggy_7_1
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_7_2
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_7_3
    $ renpy.pause()
    pri "{i}*Pants*{/i}"
    pov "{i}*Pants*{/i}"
    pov "Damn- that felt so good..."
    pri "[povname]?"
    pov "Yeah?"
    pri "Watch your language."
    pov "Can you blame me?"
    pov "I just came inside your-"
    pri "Don't you dare say it."
    pri "God's watching you."
    pov "Like... right now?"
    pri "All the time."
    pov "{i}*Gulp*{/i}"
    pri "Let's clean up and get outta here before someone else sees us."
    pov "Good idea."
    pov "Note to self, don't eat at this table."

    jump lbl_lashley_cafeteria_doggy_post

####################
## Doggy Cum In XRAY
label lbl_lashley_cafeteria_doggy_cumin_0:
    scene bg lashleycafeteriadoggy_6_0
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_1
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_2
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_3
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_4
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_5
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_6
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_7
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_8
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_9
    $ renpy.pause(0.3,hard=True)
    show bg lashleycafeteriadoggy_6_10
    $ renpy.pause()
    pri "{i}*Pants*{/i}"
    pov "{i}*Pants*{/i}"
    pov "Damn- that felt so good..."
    pri "[povname]?"
    pov "Yeah?"
    pri "Watch your language."
    pov "Can you blame me?"
    pov "I just came inside your-"
    pri "Don't you dare say it."
    pri "God's watching you."
    pov "Like... right now?"
    pri "All the time."
    pov "{i}*Gulp*{/i}"
    pri "Let's clean up and get outta here before someone else sees us."
    pov "Good idea."
    pov "Note to self, don't eat at this table."

    jump lbl_lashley_cafeteria_doggy_post

####################
## Doggy Cum Out
label lbl_lashley_cafeteria_doggy_cumout:
    "Error 'lashleycafeteria_out'"

    jump lbl_lashley_cafeteria_doggy_post

####################
## Doggy Next
label lbl_lashley_cafeteria_doggy_next:
    "Error 'lashleycafeteria_next'"

    jump lbl_lashley_cafeteria_doggy_post

####################
## Doggy Post
label lbl_lashley_cafeteria_doggy_post:
    scene bg schoolyard_night
    with fade

    $ gtime = 2

    jump lbl_schoolyard_night_setup
