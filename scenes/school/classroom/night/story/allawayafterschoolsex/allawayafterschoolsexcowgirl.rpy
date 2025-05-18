## Cowgirl  ##
label lbl_allaway_after_school_sex_cowgirl:
    if hscene_xray == 0:
        scene bg allawayposthscene_cowgirl_1
        with fade
    else:
        scene bg allawayposthscene_cowgirl_1_0
        with fade

label lbl_allaway_after_school_sex_cowgirl_choice:
    jump lbl_allaway_after_school_sex_cowgirl_pussy

####################
## Cowgirl Pussy Pre
label lbl_allaway_after_school_sex_cowgirl_pussy:
    if hscene_xray == 0:
        show bg allawayposthscene_cowgirl_2
        mis "F- uuuhh- cckk-"
        mis "Excuse my French, but fuck... you're soo big"
        show bg allawayposthscene_cowgirl_3
        mis "{i}*Moan*{/i}"
    else:
        show bg allawayposthscene_cowgirl_2_0
        mis "F- uuuhh- cckk-"
        mis "Excuse my French but fuck... you're soo big"
        show bg allawayposthscene_cowgirl_3_0
        mis "{i}*Moan*{/i}"
    mis "Mmmm..."
    mis "I love feeling you twitch all the way inside me."
    mis "Rubbing against the walls-"
    if hscene_xray == 0:
        show bg allawayposthscene_cowgirl_4
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_5
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_1
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_2
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_3
    else:
        show bg allawayposthscene_cowgirl_4_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_5_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_1_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_2_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_3_0
    mis "Ahh-"
    pov "I love how you can take it all, Miss Allaway."
    mis "Do you want me to-"
    pov "Yes. Just fuck me hard, Miss."

    jump lbl_allaway_after_school_sex_cowgirl_pussy_0

label lbl_allaway_after_school_sex_cowgirl_pussy_0:
    #$ allaway_after_school_sex_cowgirl_counter = 0
    if hscene_xray == 0:
        jump lbl_allaway_after_school_sex_cowgirl_pussy_1
    else:
        jump lbl_allaway_after_school_sex_cowgirl_pussy_1_0

####################
## Cowgirl Stage 1
label lbl_allaway_after_school_sex_cowgirl_pussy_1:
    scene img_allaway_after_school_sex_cowgirl_pussy_stage_1
    #$ allaway_after_school_sex_cowgirl_counter += 1
    #show bg allawayposthscene_cowgirl_1
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_cowgirl_2
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_3
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_cowgirl_4
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_cowgirl_5
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_after_school_sex_cowgirl_counter == 4:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    #elif skill_sta <= 14 and allaway_after_school_sex_cowgirl_counter == 6:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_2
    #elif skill_sta <= 20 and allaway_after_school_sex_cowgirl_counter >= 8:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_2
    #else:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_1

image img_allaway_after_school_sex_cowgirl_pussy_stage_1:
    "bg allawayposthscene_cowgirl_1"
    pause 0.3
    "bg allawayposthscene_cowgirl_2"
    pause 0.1
    "bg allawayposthscene_cowgirl_3"
    pause 0.3
    "bg allawayposthscene_cowgirl_4"
    pause 0.3
    "bg allawayposthscene_cowgirl_5"
    pause 0.3
    repeat

####################
## Cowgirl Stage 1 XRAY
label lbl_allaway_after_school_sex_cowgirl_pussy_1_0:
    scene img_allaway_after_school_sex_cowgirl_pussy_stage_1_0
    #$ allaway_after_school_sex_cowgirl_counter += 1
    #show bg allawayposthscene_cowgirl_1_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_cowgirl_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_3_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_cowgirl_4_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_cowgirl_5_0
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_after_school_sex_cowgirl_counter == 4:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    #elif skill_sta <= 14 and allaway_after_school_sex_cowgirl_counter == 6:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_2_0
    #elif skill_sta <= 20 and allaway_after_school_sex_cowgirl_counter >= 8:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_2_0
    #else:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_1_0

image img_allaway_after_school_sex_cowgirl_pussy_stage_1_0:
    "bg allawayposthscene_cowgirl_1_0"
    pause 0.3
    "bg allawayposthscene_cowgirl_2_0"
    pause 0.1
    "bg allawayposthscene_cowgirl_3_0"
    pause 0.3
    "bg allawayposthscene_cowgirl_4_0"
    pause 0.3
    "bg allawayposthscene_cowgirl_5_0"
    pause 0.3
    repeat

####################
## Cowgirl Stage 2
label lbl_allaway_after_school_sex_cowgirl_pussy_2:
    scene img_allaway_after_school_sex_cowgirl_pussy_stage_2
    #$ allaway_after_school_sex_cowgirl_counter += 1
    #show bg allawayposthscene_cowgirl_1
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_cowgirl_3
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_4
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_cowgirl_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_after_school_sex_cowgirl_counter == 18:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    #elif skill_sta <= 20 and allaway_after_school_sex_cowgirl_counter >= 20:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_3
    #else:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_2

image img_allaway_after_school_sex_cowgirl_pussy_stage_2:
    "bg allawayposthscene_cowgirl_1"
    pause 0.2
    "bg allawayposthscene_cowgirl_3"
    pause 0.1
    "bg allawayposthscene_cowgirl_4"
    pause 0.2
    "bg allawayposthscene_cowgirl_5"
    pause 0.2
    repeat

####################
## Cowgirl Stage 2 XRAY
label lbl_allaway_after_school_sex_cowgirl_pussy_2_0:
    scene img_allaway_after_school_sex_cowgirl_pussy_stage_2_0
    #$ allaway_after_school_sex_cowgirl_counter += 1
    #show bg allawayposthscene_cowgirl_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_cowgirl_3_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_cowgirl_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_after_school_sex_cowgirl_counter == 18:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    #elif skill_sta <= 20 and allaway_after_school_sex_cowgirl_counter >= 20:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_3_0
    #else:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_2_0

image img_allaway_after_school_sex_cowgirl_pussy_stage_2_0:
    "bg allawayposthscene_cowgirl_1_0"
    pause 0.2
    "bg allawayposthscene_cowgirl_3_0"
    pause 0.1
    "bg allawayposthscene_cowgirl_4_0"
    pause 0.2
    "bg allawayposthscene_cowgirl_5_0"
    pause 0.2
    repeat

####################
## Cowgirl Stage 3
label lbl_allaway_after_school_sex_cowgirl_pussy_3:
    scene img_allaway_after_school_sex_cowgirl_pussy_stage_3
    #$ allaway_after_school_sex_cowgirl_counter += 1
    #show bg allawayposthscene_cowgirl_1
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_3
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_5
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and allaway_after_school_sex_cowgirl_counter >= 36:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    #else:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_3

image img_allaway_after_school_sex_cowgirl_pussy_stage_3:
    "bg allawayposthscene_cowgirl_1"
    pause 0.1
    "bg allawayposthscene_cowgirl_3"
    pause 0.1
    "bg allawayposthscene_cowgirl_5"
    pause 0.1
    repeat

####################
## Cowgirl Stage 3 XRAY
label lbl_allaway_after_school_sex_cowgirl_pussy_3_0:
    scene img_allaway_after_school_sex_cowgirl_pussy_stage_3_0
    #$ allaway_after_school_sex_cowgirl_counter += 1
    #show bg allawayposthscene_cowgirl_1_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_3_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_cowgirl_5_0
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and allaway_after_school_sex_cowgirl_counter >= 36:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_cum
    #else:
    #    jump lbl_allaway_after_school_sex_cowgirl_pussy_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_cowgirl_pussy_3_0

image img_allaway_after_school_sex_cowgirl_pussy_stage_3_0:
    "bg allawayposthscene_cowgirl_1_0"
    pause 0.1
    "bg allawayposthscene_cowgirl_3_0"
    pause 0.1
    "bg allawayposthscene_cowgirl_5_0"
    pause 0.1
    repeat

####################
## Cowgirl Cum
label lbl_allaway_after_school_sex_cowgirl_pussy_cum:
    if missallaway_points <= 6:
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum_2
    else:
        jump lbl_allaway_after_school_sex_cowgirl_pussy_cum_3

label lbl_allaway_after_school_sex_cowgirl_pussy_cum_2:
    #if hscene_xray == 0:
    #    scene bg allawayposthscene_cowgirl_3
    #else:
    #    scene bg allawayposthscene_cowgirl_3_0
    call screen scr_allaway_after_school_sex_cowgirl_pussy_cum_2

screen scr_allaway_after_school_sex_cowgirl_pussy_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_cowgirl_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_cowgirl_pussy_cumchoice")

label lbl_allaway_after_school_sex_cowgirl_pussy_cum_3:
    #if hscene_xray == 0:
    #    scene bg allawayposthscene_cowgirl_3
    #else:
    #    scene bg allawayposthscene_cowgirl_3_0
    call screen scr_allaway_after_school_sex_cowgirl_pussy_cum_3

screen scr_allaway_after_school_sex_cowgirl_pussy_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_scenechoice_cowgirl")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_cowgirl_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_cowgirl_pussy_cumchoice")

label lbl_allaway_after_school_sex_cowgirl_pussy_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allaway_after_school_sex_cowgirl_pussy_cumin
            else:
                jump lbl_allaway_after_school_sex_cowgirl_pussy_cumin_0
        "Cum outside":
            jump lbl_allaway_after_school_sex_cowgirl_pussy_cumout

####################
## Cowgirl Cum In
label lbl_allaway_after_school_sex_cowgirl_pussy_cumin:
    scene bg allawayposthscene_cowgirl_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_3
    $ renpy.pause(1.5,hard=True)
    show bg allawayposthscene_cowgirl_7_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_7_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_7_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_7_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_7_5
    $ renpy.pause()
    pov "{i}*Pants*{/i}"
    pov "Fuck... that felt so good."
    mis "You- you came inside me... {i}*pants*{/i}"
    pov "Fuck... shit... sorry."
    mis "{i}*Pants*{/i} Watch- your language.."
    mis "{i}*Pants*{/i}"
    mis "It's okay... I've been on the pill-"
    mis "For a while now..."
    mis "Mmm... what a mess."
    mis "How are we gonna get out of this predicament..?"
    pov "Look on the bright side, most of it is inside you."
    pov "Just cup your hands and-"
    mis "[povname]!"

    jump lbl_allaway_after_school_sex_end

####################
## Cowgirl Cum In XRAY
label lbl_allaway_after_school_sex_cowgirl_pussy_cumin_0:
    scene bg allawayposthscene_cowgirl_1_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_2_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_3_0
    $ renpy.pause(0.5,hard=True)
    show bg allawayposthscene_cowgirl_6_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_10
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_6_11
    $ renpy.pause()
    pov "{i}*Pants*{/i}"
    pov "Fuck... that felt so good."
    mis "You- you came inside me... {i}*pants*{/i}"
    pov "Fuck... shit... sorry."
    mis "{i}*Pants*{/i} Watch- your language.."
    mis "{i}*Pants*{/i}"
    mis "It's okay... I've been on the pill-"
    mis "For a while now..."
    mis "Mmm... what a mess."
    mis "How are we gonna get out of this predicament..?"
    pov "Look on the bright side, most of it is inside you."
    pov "Just cup your hands and-"
    mis "[povname]!"

    jump lbl_allaway_after_school_sex_end

####################
## Cowgirl Cum Out
label lbl_allaway_after_school_sex_cowgirl_pussy_cumout:
    if hscene_xray == 0:
        show bg allawayposthscene_cowgirl_4
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_5
        $ renpy.pause(0.3,hard=True)
    else:
        show bg allawayposthscene_cowgirl_4_0
        $ renpy.pause(0.3,hard=True)
        show bg allawayposthscene_cowgirl_5_0
        $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_0
    $ renpy.pause(0.6,hard=True)
    show bg allawayposthscene_cowgirl_8_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_cowgirl_8_8
    $ renpy.pause()
    pov "{i}*Pants*{/i}"
    mis "{i}*Pants*{/i}"
    mis "That..."
    pov "Felt..."
    mis "So..."
    mis "Goo-"
    pov "Amazing..."
    mis "{i}*Pants*{/i} Yeah..."
    pov "Oh- crap. I'm a mess."
    mis "Me too..."
    pov "No you're not!"
    mis "My vagina's a little moist and sticky."
    pov "Oh, poor you."

    jump lbl_allaway_after_school_sex_end

####################
## Cowgirl Next
label lbl_allaway_after_school_sex_stairs_cowgirl_next:
    if hscene_xray == 0:
        show bg allawayposthscene_cowgirl_3
        pov "C'mon, Miss. Let's get off the floor."
    else:
        show bg allawayposthscene_cowgirl_3_0
        pov "C'mon, Miss. Let's get off the floor."

    jump lbl_allaway_after_school_sex_scenechoice_stairs
