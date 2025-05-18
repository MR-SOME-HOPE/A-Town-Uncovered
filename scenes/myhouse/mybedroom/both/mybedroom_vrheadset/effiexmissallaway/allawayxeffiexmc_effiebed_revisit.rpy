## Allaway x Effie x MC Effie Bed

####################
## Missionary Pre
label lbl_allawayxeffiexmc_effiebed_revisit_pre:
    if hscene_xray == 0:
        scene bg allawayxeffiexmc_effiebed_1
        with fade
    else:
        scene bg allawayxeffiexmc_effiebed_1_0
        with fade

    jump lbl_allawayxeffiexmc_effiebed_revisit_0

label lbl_allawayxeffiexmc_effiebed_revisit_0:
    #$ allawayxeffiexmc_effiebed_counter = 0
    if hscene_xray == 0:
        jump lbl_allawayxeffiexmc_effiebed_revisit_1
    else:
        jump lbl_allawayxeffiexmc_effiebed_revisit_1_0

####################
## Stage 1
label lbl_allawayxeffiexmc_effiebed_revisit_1:
    scene img_allawayxeffiexmc_effiebed_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_1

image img_allawayxeffiexmc_effiebed_revisit_stage_1:
    "bg allawayxeffiexmc_effiebed_1"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_2"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_3"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_allawayxeffiexmc_effiebed_revisit_1_0:
    scene img_allawayxeffiexmc_effiebed_revisit_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_2_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_2_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_1_0

image img_allawayxeffiexmc_effiebed_revisit_stage_1_0:
    "bg allawayxeffiexmc_effiebed_1_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_2_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_3_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_allawayxeffiexmc_effiebed_revisit_2:
    scene img_allawayxeffiexmc_effiebed_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_2

image img_allawayxeffiexmc_effiebed_revisit_stage_2:
    "bg allawayxeffiexmc_effiebed_1"
    pause 0.1
    "bg allawayxeffiexmc_effiebed_2"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6"
    pause 0.1
    repeat

####################
## Stage 2 XRAY
label lbl_allawayxeffiexmc_effiebed_revisit_2_0:
    scene img_allawayxeffiexmc_effiebed_revisit_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_3_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_2_0

image img_allawayxeffiexmc_effiebed_revisit_stage_2_0:
    "bg allawayxeffiexmc_effiebed_1_0"
    pause 0.1
    "bg allawayxeffiexmc_effiebed_2_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6_0"
    pause 0.1
    repeat

####################
## Stage 3
label lbl_allawayxeffiexmc_effiebed_revisit_3:
    scene img_allawayxeffiexmc_effiebed_revisit_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_3

image img_allawayxeffiexmc_effiebed_revisit_stage_3:
    "bg allawayxeffiexmc_effiebed_6"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_allawayxeffiexmc_effiebed_revisit_3_0:
    scene img_allawayxeffiexmc_effiebed_revisit_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_revisit_3_0

image img_allawayxeffiexmc_effiebed_revisit_stage_3_0:
    "bg allawayxeffiexmc_effiebed_6_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5_0"
    pause 0.2
    repeat

####################
## Missionary Cum
label lbl_allawayxeffiexmc_effiebed_revisit_cum:
    jump lbl_allawayxeffiexmc_effiebed_revisit_cum_2

label lbl_allawayxeffiexmc_effiebed_revisit_cum_2:
    call screen scr_allawayxeffiexmc_effiebed_revisit_cum_2

screen scr_allawayxeffiexmc_effiebed_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allawayxeffiexmc_effiebed_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allawayxeffiexmc_effiebed_revisit_cumchoice")

label lbl_allawayxeffiexmc_effiebed_revisit_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allawayxeffiexmc_effiebed_revisit_cumin
            else:
                jump lbl_allawayxeffiexmc_effiebed_revisit_cumin_0
        "Cum on them":
            jump lbl_allawayxeffiexmc_effiebed_revisit_cumout

####################
## Cum In
label lbl_allawayxeffiexmc_effiebed_revisit_cumin:
    scene bg allawayxeffiexmc_effiebed_8_0
    $ renpy.pause(1.5,hard=True)
    show bg allawayxeffiexmc_effiebed_8_1
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_2
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_3
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_4
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_5
    $ renpy.pause(1,hard=True)
    mis "Ohhh- fuck..."
    mis "Oh- sh-shit..."
    pov "{i}*Pants*{/i}"
    eff "Fuck that looks so fucking hot..."
    eff "Mmm.. I'm so jealous..."
    pov "Cumming in your pussy feels so good, Miss."
    mis "{i}*Pants*{/i} Oh God.. my legs..."
    mis "I feel so full of your cum, [povname]."
    eff "It's seeped out, Miss Allaway."
    eff "[povname] really is the god of cum."
    pov "You girls are making me blush."
    eff "Hehehe~"
    mis "I'm such a mess right now."
    mis "Effie you weren't kidding about being dripping wet, my tongue couldn't keep up."
    pov "You both did great, mind cleaning me up Effie?"
    mis "No- don't pull out."
    mis "Maybe I'm crazy but I feel really comfortable like this."
    eff "Then keep on licking, Miss."
    
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_allawayxeffiexmc_effiebed_revisit_cumin_0:
    scene bg allawayxeffiexmc_effiebed_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayxeffiexmc_effiebed_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayxeffiexmc_effiebed_7_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_10
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_11
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_12
    $ renpy.pause(0.3,hard=True)
    mis "Ohhh- fuck..."
    mis "Oh- sh-shit..."
    pov "{i}*Pants*{/i}"
    eff "Fuck that looks so fucking hot..."
    eff "Mmm.. I'm so jealous..."
    pov "Cumming in your pussy feels so good, Miss."
    mis "{i}*Pants*{/i} Oh God.. my legs..."
    mis "I feel so full of your cum, [povname]."
    eff "It's seeped out, Miss Allaway."
    eff "[povname] really is the god of cum."
    pov "You girls are making me blush."
    eff "Hehehe~"
    mis "I'm such a mess right now."
    mis "Effie you weren't kidding about being dripping wet, my tongue couldn't keep up."
    pov "You both did great, mind cleaning me up Effie?"
    mis "No- don't pull out."
    mis "Maybe I'm crazy but I feel really comfortable like this."
    eff "Then keep on licking, Miss."
    
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Cum Out
label lbl_allawayxeffiexmc_effiebed_revisit_cumout:
    pov "Ahh- I'm cumming-"
    scene bg allawayxeffiexmc_effiebed_9_0
    $ renpy.pause(0.6,hard=True)
    show bg allawayxeffiexmc_effiebed_9_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_10
    $ renpy.pause(0.8,hard=True)
    eff "[povname]!"
    mis "Holy shit, why is there so much-?"
    eff "You almost got me in the face-"
    pov "{i}*Pants*{/i}"
    pov "Guys-"
    pov "Can you-"
    pov "I just busted my entire load all over you-"
    pov "{i}*Pants*{/i} Give me some fucking slack."
    eff "Hmm.."
    mis "My pussy is completely covered with your cum..."
    eff "And how much I just want to bury my face and push it inside you with my tongue, Miss Allaway."
    mis "Don't tease me like that Effie.."
    mis "If you're gonna do it, just do it."
    mis "You're driving me crazy."
    pov "Mind cleaning me up, Effie?"
    eff "Bitch please, your cock looks spotless apart from that glistening highlight."
    mis "Here's an idea, [povname]. Why don't you take your mouth and clean both of us up."
    pov "No, thanks. I'll just go ahead and quickly grab some tissues."
    eff "Ughh- use the old towel, [povname]. Tissues won't cut this."
    pov "Hold tight, you don't want it getting everywhere."
    show bg allawayxeffiexmc_effiebed_9_11
    with dissolve
    mis "Effie? Can you see if it's going inside me."
    eff "Miss Allaway, there's no doubt it's going in."
    mis "Damn, can I borrow a pill?"

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
