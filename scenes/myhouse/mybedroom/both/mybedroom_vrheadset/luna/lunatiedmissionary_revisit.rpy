## Luna Tied Missionary
label lbl_luna_tied_missionary_revisit:
    if hscene_xray == 0:
        scene bg lunatiedmissionaryanal_1
        with fade
    else:
        scene bg lunatiedmissionaryanal_1_0
        with fade

    jump lbl_luna_tied_missionary_revisit_0

####################
## Doggy Pre
label lbl_luna_tied_missionary_revisit_0_0:
    "Error 'lunatied_pre'"

    jump lbl_luna_tied_missionary_revisit_0

label lbl_luna_tied_missionary_revisit_0:
    #$ luna_tied_missionary_counter = 0
    if hscene_xray == 0:
        jump lbl_luna_tied_missionary_revisit_1
    else:
        jump lbl_luna_tied_missionary_revisit_1_0

####################
## Doggy Stage 1
label lbl_luna_tied_missionary_revisit_1:
    scene img_luna_tied_missionary_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_tied_missionary_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_tied_missionary_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_1

image img_luna_tied_missionary_stage_1:
    "bg lunatiedmissionaryanal_1"
    pause 0.2
    "bg lunatiedmissionaryanal_2"
    pause 0.2
    "bg lunatiedmissionaryanal_3"
    pause 0.3
    "bg lunatiedmissionaryanal_4"
    pause 0.3
    "bg lunatiedmissionaryanal_2"
    pause 0.2
    repeat

####################
## Doggy Stage 1 XRAY
label lbl_luna_tied_missionary_revisit_1_0:
    scene img_luna_tied_missionary_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_tied_missionary_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_tied_missionary_revisit_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_1_0

image img_luna_tied_missionary_stage_1_0:
    "bg lunatiedmissionaryanal_1_0"
    pause 0.2
    "bg lunatiedmissionaryanal_2_0"
    pause 0.2
    "bg lunatiedmissionaryanal_3_0"
    pause 0.3
    "bg lunatiedmissionaryanal_4_0"
    pause 0.3
    "bg lunatiedmissionaryanal_2_0"
    pause 0.2
    repeat

####################
## Doggy Stage 2
label lbl_luna_tied_missionary_revisit_2:
    scene img_luna_tied_missionary_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_tied_missionary_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_tied_missionary_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_2

image img_luna_tied_missionary_stage_2:
    "bg lunatiedmissionaryanal_5"
    pause 0.2
    "bg lunatiedmissionaryanal_6"
    pause 0.1
    "bg lunatiedmissionaryanal_7"
    pause 0.2
    "bg lunatiedmissionaryanal_8"
    pause 0.2
    "bg lunatiedmissionaryanal_6"
    pause 0.2
    repeat

####################
## Doggy Stage 2 XRAY
label lbl_luna_tied_missionary_revisit_2_0:
    scene img_luna_tied_missionary_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_luna_tied_missionary_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_tied_missionary_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_2_0

image img_luna_tied_missionary_stage_2_0:
    "bg lunatiedmissionaryanal_5_0"
    pause 0.2
    "bg lunatiedmissionaryanal_6_0"
    pause 0.1
    "bg lunatiedmissionaryanal_7_0"
    pause 0.2
    "bg lunatiedmissionaryanal_8_0"
    pause 0.2
    "bg lunatiedmissionaryanal_6_0"
    pause 0.2
    repeat

####################
## Doggy Stage 3
label lbl_luna_tied_missionary_revisit_3:
    scene img_luna_tied_missionary_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_tied_missionary_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_3

image img_luna_tied_missionary_stage_3:
    "bg lunatiedmissionaryanal_9"
    pause 0.1
    "bg lunatiedmissionaryanal_10"
    pause 0.1
    "bg lunatiedmissionaryanal_11"
    pause 0.1
    "bg lunatiedmissionaryanal_12"
    pause 0.1
    "bg lunatiedmissionaryanal_10"
    pause 0.1
    repeat

####################
## Doggy Stage 3 XRAY
label lbl_luna_tied_missionary_revisit_3_0:
    scene img_luna_tied_missionary_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_luna_tied_missionary_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_luna_tied_missionary_revisit_3_0

image img_luna_tied_missionary_stage_3_0:
    "bg lunatiedmissionaryanal_9_0"
    pause 0.1
    "bg lunatiedmissionaryanal_10_0"
    pause 0.1
    "bg lunatiedmissionaryanal_11_0"
    pause 0.1
    "bg lunatiedmissionaryanal_12_0"
    pause 0.1
    "bg lunatiedmissionaryanal_10_0"
    pause 0.1
    repeat

####################
## Doggy Cum
label lbl_luna_tied_missionary_revisit_cum:
    jump lbl_luna_tied_missionary_revisit_cum_2

label lbl_luna_tied_missionary_revisit_cum_2:

    call screen scr_luna_tied_missionary_revisit_cum_2

screen scr_luna_tied_missionary_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_luna_tied_missionary_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action If(hscene_xray == 0, Jump("lbl_luna_tied_missionary_revisit_cumin"), Jump("lbl_luna_tied_missionary_revisit_cumin_0"))

####################
## Doggy Cum In
label lbl_luna_tied_missionary_revisit_cumin:
    scene bg lunatiedmissionaryanal_14_0
    $ renpy.pause(1.5,hard=True)
    show bg lunatiedmissionaryanal_14_1
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_14_2
    $ renpy.pause()
    lun "{i}*Pants*{/i}"
    pov "{i}*Pants*{/i}"
    show bg lunatiedmissionaryanal_14_3
    lun "Heheh.. so? Should I introduce you to my darlings?"
    pov "Oh, I'm sure we're all well aquainted by now. They've seen me fuck you silly."
    lun "You don't wanna be rude, [povname]. They're spirits, remember."
    lun "They could literally convince your soul to leave your body if they really wanted to."
    pov "Seems a bit excessive."
    lun "How do you think I have so many darlings."
    pov "..."
    pov "You know, Luna. This has been fun but I've gotta skidaddle."
    lun "They'll see you in your dreams then."
    pov "It's a date."

    jump lbl_luna_tied_missionary_revisit_post

####################
## Doggy Cum In XRAY
label lbl_luna_tied_missionary_revisit_cumin_0:
    scene bg lunatiedmissionaryanal_13_0
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_1
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_2
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_3
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_4
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_5
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_6
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_7
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_8
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_9
    $ renpy.pause(0.3,hard=True)
    show bg lunatiedmissionaryanal_13_10
    $ renpy.pause()
    lun "{i}*Pants*{/i}"
    pov "{i}*Pants*{/i}"
    show bg lunatiedmissionaryanal_13_11
    lun "Heheh.. so? Should I introduce you to my darlings?"
    pov "Oh, I'm sure we're all well aquainted by now. They've seen me fuck you silly."
    lun "You don't wanna be rude, [povname]. They're spirits, remember."
    lun "They could literally convince your soul to leave your body if they really wanted to."
    pov "Seems a bit excessive."
    lun "How do you think I have so many darlings."
    pov "..."
    pov "You know, Luna. This has been fun but I've gotta skidaddle."
    lun "They'll see you in your dreams then."
    pov "It's a date."

    jump lbl_luna_tied_missionary_revisit_post

####################
## Doggy Cum Out
label lbl_luna_tied_missionary_revisit_cumout:
    "Error 'lunatied_out'"

    jump lbl_luna_tied_missionary_revisit_post

####################
## Doggy Next
label lbl_luna_tied_missionary_revisit_next:
    "Error 'lunatied_next'"

    jump lbl_luna_tied_missionary_revisit_post

####################
## Doggy Post
label lbl_luna_tied_missionary_revisit_post:
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
