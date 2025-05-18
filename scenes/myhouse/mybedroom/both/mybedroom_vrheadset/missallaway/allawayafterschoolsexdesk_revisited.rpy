## Desk ##
label lbl_allaway_after_school_sex_desk_revisit:
    scene bg allawayposthscene_desk_0_1
    with fade
    jump lbl_allaway_after_school_sex_desk_revisit_pussy

####################
## Desk Pussy Pre
label lbl_allaway_after_school_sex_desk_revisit_pussy:
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
    jump lbl_allaway_after_school_sex_desk_revisit_pussy_0

label lbl_allaway_after_school_sex_desk_revisit_pussy_0:
    $ vrheadset_revisitcounter = 0
    if hscene_xray == 0:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_1
    else:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_1_0

####################
## Desk Stage 1
label lbl_allaway_after_school_sex_desk_revisit_pussy_1:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_desk_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_2
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_2
    $ renpy.pause(0.3,hard=True)
    jump lbl_allaway_after_school_sex_desk_revisit_pussy_counter

####################
## Desk Stage 1 XRAY
label lbl_allaway_after_school_sex_desk_revisit_pussy_1_0:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_desk_1_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_2_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_3_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_4_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_desk_2_0
    $ renpy.pause(0.3,hard=True)
    jump lbl_allaway_after_school_sex_desk_revisit_pussy_counter_xray


####################
## Desk Stage 2
label lbl_allaway_after_school_sex_desk_revisit_pussy_2:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_desk_1
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_desk_2
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_desk_2
    $ renpy.pause(0.2,hard=True)
    jump lbl_allaway_after_school_sex_desk_revisit_pussy_counter


####################
## Desk Stage 2 XRAY
label lbl_allaway_after_school_sex_desk_revisit_pussy_2_0:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_desk_1_0
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_desk_2_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_3_0
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_desk_2_0
    $ renpy.pause(0.2,hard=True)
    jump lbl_allaway_after_school_sex_desk_revisit_pussy_counter_xray


####################
## Desk Stage 3
label lbl_allaway_after_school_sex_desk_revisit_pussy_3:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_desk_1
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_3
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_2
    $ renpy.pause(0.1,hard=True)
    jump lbl_allaway_after_school_sex_desk_revisit_pussy_counter


####################
## Desk Stage 3 XRAY
label lbl_allaway_after_school_sex_desk_revisit_pussy_3_0:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_desk_1_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_3_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_desk_2_0
    $ renpy.pause(0.1,hard=True)
    jump lbl_allaway_after_school_sex_desk_revisit_pussy_counter_xray

label lbl_allaway_after_school_sex_desk_revisit_pussy_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_2
    if vrheadset_revisitcounter >= 70 and vrheadset_revisitcounter <= 119:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_3
    elif vrheadset_revisitcounter >= 120:
        call screen scr_allaway_after_school_sex_desk_pussy_cum_revisit
    else:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_1

label lbl_allaway_after_school_sex_desk_revisit_pussy_counter_xray:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_2_0
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_3_0
    elif vrheadset_revisitcounter >= 90:
        call screen scr_allaway_after_school_sex_desk_pussy_cum_revisit
    else:
        jump lbl_allaway_after_school_sex_desk_revisit_pussy_1_0


screen scr_allaway_after_school_sex_desk_pussy_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_desk_revisit_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_desk_revisit_pussy_cumchoice")


label lbl_allaway_after_school_sex_desk_revisit_pussy_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allaway_after_school_sex_desk_revisit_pussy_cumin
            else:
                jump lbl_allaway_after_school_sex_desk_revisit_pussy_cumin_0
        "Cum on her":
            jump lbl_allaway_after_school_sex_desk_revisit_pussy_cumout

####################
## Desk Cum In
label lbl_allaway_after_school_sex_desk_revisit_pussy_cumin:
    show bg allawayposthscene_desk_6_0
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
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Desk Cum In XRAY
label lbl_allaway_after_school_sex_desk_revisit_pussy_cumin_0:
    show bg allawayposthscene_desk_5_0
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
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Desk Cum Out
label lbl_allaway_after_school_sex_desk_revisit_pussy_cumout:
    if hscene_xray == 0:
        show bg allawayposthscene_desk_2
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_desk_1
        $ renpy.pause(0.3,hard=True)
    else:
        show bg allawayposthscene_desk_2_0
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
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
