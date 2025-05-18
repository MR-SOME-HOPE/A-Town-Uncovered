## Desk ##
label lbl_allaway_after_school_sex_desk:

    scene bg allawayposthscene_desk_0_1
    with fade

label lbl_allaway_after_school_sex_desk_choice:
    jump lbl_allaway_after_school_sex_desk_pussy

####################
## Desk Pussy Pre
label lbl_allaway_after_school_sex_desk_pussy:
    pov "You ready, Miss Allaway?"
    show bg allawayposthscene_desk_0_2
    mis "Just do it, [povname]. Fuck me like you want revenge-"
    mis "For- for..."
    mis "Giving you an 'F'"
    show bg allawayposthscene_desk_0_3
    mis "Yeah! A big, fat 'F' for 'Fuck Me Har-'."
    if hscene_xray == 0:
        show bg allawayposthscene_desk_1
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_desk_2
        $ renpy.pause(0.1,hard=True)
        show bg allawayposthscene_desk_3
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_desk_4
        $ renpy.pause(0.3,hard=True)
    else:
        show bg allawayposthscene_desk_1_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_desk_2_0
        $ renpy.pause(0.1,hard=True)
        show bg allawayposthscene_desk_3_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_desk_4_0
        $ renpy.pause(0.3,hard=True)
    pov "Oooh- way ahead of you, Miss."
    mis "Ah! You fuckin' bastard..."
    mis "Keep goin'."

    jump lbl_allaway_after_school_sex_desk_pussy_0

label lbl_allaway_after_school_sex_desk_pussy_0:
    #$ allaway_after_school_sex_desk_counter = 0
    if hscene_xray == 0:
        jump lbl_allaway_after_school_sex_desk_pussy_1
    else:
        jump lbl_allaway_after_school_sex_desk_pussy_1_0

####################
## Desk Stage 1
label lbl_allaway_after_school_sex_desk_pussy_1:
    scene img_allaway_after_school_sex_desk_pussy_stage_1
    #$ allaway_after_school_sex_desk_counter += 1
    #show bg allawayposthscene_desk_1
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_desk_2
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_3
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_desk_4
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_desk_2
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_after_school_sex_desk_counter == 4:
    #    jump lbl_allaway_after_school_sex_desk_pussy_cum
    #elif skill_sta <= 14 and allaway_after_school_sex_desk_counter == 6:
    #    jump lbl_allaway_after_school_sex_desk_pussy_2
    #elif skill_sta <= 20 and allaway_after_school_sex_desk_counter == 8:
    #    jump lbl_allaway_after_school_sex_desk_pussy_2
    #else:
    #    jump lbl_allaway_after_school_sex_desk_pussy_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_1

image img_allaway_after_school_sex_desk_pussy_stage_1:
    "bg allawayposthscene_desk_1"
    pause 0.3
    "bg allawayposthscene_desk_2"
    pause 0.1
    "bg allawayposthscene_desk_3"
    pause 0.3
    "bg allawayposthscene_desk_4"
    pause 0.3
    "bg allawayposthscene_desk_2"
    pause 0.3
    repeat

####################
## Desk Stage 1 XRAY
label lbl_allaway_after_school_sex_desk_pussy_1_0:
    scene img_allaway_after_school_sex_desk_pussy_stage_1_0
    #$ allaway_after_school_sex_desk_counter += 1
    #show bg allawayposthscene_desk_1_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_desk_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_3_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_desk_4_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_desk_2_0
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_after_school_sex_desk_counter == 4:
    #    jump lbl_allaway_after_school_sex_desk_pussy_cum
    #elif skill_sta <= 14 and allaway_after_school_sex_desk_counter == 6:
    #    jump lbl_allaway_after_school_sex_desk_pussy_2_0
    #elif skill_sta <= 20 and allaway_after_school_sex_desk_counter == 8:
    #    jump lbl_allaway_after_school_sex_desk_pussy_2_0
    #else:
    #    jump lbl_allaway_after_school_sex_desk_pussy_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_1_0

image img_allaway_after_school_sex_desk_pussy_stage_1_0:
    "bg allawayposthscene_desk_1_0"
    pause 0.3
    "bg allawayposthscene_desk_2_0"
    pause 0.1
    "bg allawayposthscene_desk_3_0"
    pause 0.3
    "bg allawayposthscene_desk_4_0"
    pause 0.3
    "bg allawayposthscene_desk_2_0"
    pause 0.3
    repeat

####################
## Desk Stage 2
label lbl_allaway_after_school_sex_desk_pussy_2:
    scene img_allaway_after_school_sex_desk_pussy_stage_2
    #$ allaway_after_school_sex_desk_counter += 1
    #show bg allawayposthscene_desk_1
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_desk_2
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_3
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_desk_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_after_school_sex_desk_counter == 18:
    #    jump lbl_allaway_after_school_sex_desk_pussy_cum
    #elif skill_sta <= 20 and allaway_after_school_sex_desk_counter == 20:
    #    jump lbl_allaway_after_school_sex_desk_pussy_3
    #else:
    #    jump lbl_allaway_after_school_sex_desk_pussy_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_2

image img_allaway_after_school_sex_desk_pussy_stage_2:
    "bg allawayposthscene_desk_1"
    pause 0.2
    "bg allawayposthscene_desk_2"
    pause 0.1
    "bg allawayposthscene_desk_3"
    pause 0.2
    "bg allawayposthscene_desk_2"
    pause 0.2
    repeat

####################
## Desk Stage 2 XRAY
label lbl_allaway_after_school_sex_desk_pussy_2_0:
    scene img_allaway_after_school_sex_desk_pussy_stage_2_0
    #$ allaway_after_school_sex_desk_counter += 1
    #show bg allawayposthscene_desk_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_desk_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_desk_2_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_after_school_sex_desk_counter == 18:
    #    jump lbl_allaway_after_school_sex_desk_pussy_cum
    #elif skill_sta <= 20 and allaway_after_school_sex_desk_counter == 20:
    #    jump lbl_allaway_after_school_sex_desk_pussy_3_0
    #else:
    #    jump lbl_allaway_after_school_sex_desk_pussy_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_2_0

image img_allaway_after_school_sex_desk_pussy_stage_2_0:
    "bg allawayposthscene_desk_1_0"
    pause 0.2
    "bg allawayposthscene_desk_2_0"
    pause 0.1
    "bg allawayposthscene_desk_3_0"
    pause 0.2
    "bg allawayposthscene_desk_2_0"
    pause 0.2
    repeat

####################
## Desk Stage 3
label lbl_allaway_after_school_sex_desk_pussy_3:
    scene img_allaway_after_school_sex_desk_pussy_stage_3
    #$ allaway_after_school_sex_desk_counter += 1
    #show bg allawayposthscene_desk_1
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_3
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_2
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and allaway_after_school_sex_desk_counter == 36:
    #    jump lbl_allaway_after_school_sex_desk_pussy_cum
    #else:
    #    jump lbl_allaway_after_school_sex_desk_pussy_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_3

image img_allaway_after_school_sex_desk_pussy_stage_3:
    "bg allawayposthscene_desk_1"
    pause 0.1
    "bg allawayposthscene_desk_3"
    pause 0.1
    "bg allawayposthscene_desk_2"
    pause 0.1
    repeat

####################
## Desk Stage 3 XRAY
label lbl_allaway_after_school_sex_desk_pussy_3_0:
    scene img_allaway_after_school_sex_desk_pussy_stage_3_0
    #$ allaway_after_school_sex_desk_counter += 1
    #show bg allawayposthscene_desk_1_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_3_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_desk_2_0
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and allaway_after_school_sex_desk_counter == 36:
    #    jump lbl_allaway_after_school_sex_desk_pussy_cum
    #else:
    #    jump lbl_allaway_after_school_sex_desk_pussy_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_desk_pussy_3_0

image img_allaway_after_school_sex_desk_pussy_stage_3_0:
    "bg allawayposthscene_desk_1_0"
    pause 0.1
    "bg allawayposthscene_desk_3_0"
    pause 0.1
    "bg allawayposthscene_desk_2_0"
    pause 0.1
    repeat

####################
## Desk Cum
label lbl_allaway_after_school_sex_desk_pussy_cum:
    if missallaway_points <= 6:
        jump lbl_allaway_after_school_sex_desk_pussy_cum_2
    else:
        jump lbl_allaway_after_school_sex_desk_pussy_cum_3

label lbl_allaway_after_school_sex_desk_pussy_cum_2:
    #if hscene_xray == 0:
    #    scene bg allawayposthscene_desk_3
    #else:
    #    scene bg allawayposthscene_desk_3_0
    call screen scr_allaway_after_school_sex_desk_pussy_cum_2

screen scr_allaway_after_school_sex_desk_pussy_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_desk_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_desk_pussy_cumchoice")

label lbl_allaway_after_school_sex_desk_pussy_cum_3:
    #if hscene_xray == 0:
    #    scene bg allawayposthscene_desk_3
    #else:
    #    scene bg allawayposthscene_desk_3_0
    call screen scr_allaway_after_school_sex_desk_pussy_cum_3

screen scr_allaway_after_school_sex_desk_pussy_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_scenechoice_desk")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_desk_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_desk_pussy_cumchoice")

label lbl_allaway_after_school_sex_desk_pussy_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allaway_after_school_sex_desk_pussy_cumin
            else:
                jump lbl_allaway_after_school_sex_desk_pussy_cumin_0
        "Cum on her":
            jump lbl_allaway_after_school_sex_desk_pussy_cumout

####################
## Desk Cum In
label lbl_allaway_after_school_sex_desk_pussy_cumin:
    scene bg allawayposthscene_desk_6_0
    $ renpy.pause(1.5,hard=True)
    show bg allawayposthscene_desk_6_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_6_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_6_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_6_4
    $ renpy.pause()
    pov "Ah shit... I accidentally came-"
    show bg allawayposthscene_desk_6_5
    mis "Inside... Thanks for the news flash, [povname]."
    pov "W-What are we gonna do?"
    show bg allawayposthscene_desk_6_6
    mis "Don't worry. I'm still on the pill, been on it for a while."
    show bg allawayposthscene_desk_6_7
    mis "Shit... umm..."
    mis "Find something to clean up the mess."
    mis "It's gonna spill out as soon as you pull out."
    show bg allawayposthscene_desk_6_8
    pov "Alright... let's waddle on the count of 3."

    jump lbl_allaway_after_school_sex_end

####################
## Desk Cum In XRAY
label lbl_allaway_after_school_sex_desk_pussy_cumin_0:
    scene bg allawayposthscene_desk_5_0
    $ renpy.pause(0.5,hard=True)
    show bg allawayposthscene_desk_5_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_5_9
    $ renpy.pause()
    pov "Ah shit... I accidentally came-"
    show bg allawayposthscene_desk_5_10
    mis "Inside... Thanks for the news flash, [povname]."
    pov "W-What are we gonna do?"
    show bg allawayposthscene_desk_5_11
    mis "Don't worry. I'm still on the pill, been on it for a while."
    show bg allawayposthscene_desk_5_12
    mis "Shit... umm..."
    mis "Find something to clean up the mess."
    mis "It's gonna spill out as soon as you pull out."
    show bg allawayposthscene_desk_5_13
    pov "Alright... let's waddle on the count of 3."

    jump lbl_allaway_after_school_sex_end

####################
## Desk Cum Out
label lbl_allaway_after_school_sex_desk_pussy_cumout:
    if hscene_xray == 0:
        scene bg allawayposthscene_desk_2
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_desk_1
        $ renpy.pause(0.3,hard=True)
    else:
        scene bg allawayposthscene_desk_2_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_desk_1_0
        $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_0
    $ renpy.pause(0.6,hard=True)
    show bg allawayposthscene_desk_7_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_10
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_11
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_7_12
    $ renpy.pause()
    show bg allawayposthscene_desk_7_13
    mis "Are you fucking kidding me?"
    mis "I guess I'm stuck here forever."
    show bg allawayposthscene_desk_7_14
    pov "Hehe, I apologise."
    show bg allawayposthscene_desk_7_15
    mis "Eh- shove it."
    show bg allawayposthscene_desk_7_14
    pov "All the way in?"
    show bg allawayposthscene_desk_7_16
    mis "No- stop."
    show bg allawayposthscene_desk_7_17
    mis "Go and find something to clean me up."
    show bg allawayposthscene_desk_7_14
    pov "But it's a masterpiece."
    show bg allawayposthscene_desk_7_15
    mis "[povname]!"
    show bg allawayposthscene_desk_7_14
    pov "Hahaha, right away, Miss."

    jump lbl_allaway_after_school_sex_end

####################
## Desk Next
label lbl_allaway_after_school_sex_desk_pussy_next:
    if hscene_xray == 0:
        show bg allawayposthscene_desk_2
        $ renpy.pause(0.5,hard=True)
        show bg allawayposthscene_desk_1
        $ renpy.pause(0.5,hard=True)
        show bg allawayposthscene_desk_0_1
        $ renpy.pause(0.5,hard=True)
        pov "C'mon, Miss. Let's move somewhere else."
    else:
        show bg allawayposthscene_desk_2_0
        $ renpy.pause(0.5,hard=True)
        show bg allawayposthscene_desk_1_0
        $ renpy.pause(0.5,hard=True)
        show bg allawayposthscene_desk_0_1
        $ renpy.pause(0.5,hard=True)
        pov "C'mon, Miss. Let's move somewhere else."

    jump lbl_allaway_after_school_sex_scenechoice_desk
