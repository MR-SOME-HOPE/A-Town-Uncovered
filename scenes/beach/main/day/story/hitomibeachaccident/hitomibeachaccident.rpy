## Hitomi Beach Accident
label lbl_hitomi_beach_accident:
    default hitomi_beach_accident_counter = 0
    default hitomibeachaccident_firsttimedone = 0

    scene bg beachmain_day
    scene bg hitomibeachaccidentfrisbee_1 with fade
    "A random guy with a frisbee points at you and gestures as if he's about to throw it to you."
    $ hitomibeach_day = 1

    menu:
        "Raise your arms and give 'the nod'":
            pass
        "Shake your head politely and go on with your day":
            scene black with fade
            jump lbl_beachmain_day
    scene bg hitomibeachaccidentfrisbee_2
    "He throws it at you with all his strength and it soars right over you."
    scene bg hitomibeachaccidentfrisbee_3
    "You chase after it, eye on the red disc."
    if skill_sta >= 12 and (10 <= skill_luc <= 16):
        scene bg hitomibeachaccidentfrisbee_5
        "You successfully caught the frisbee without bumping into anyone."
        scene bg hitomibeachaccidentfrisbee_6
        "Some cute girls saw how badass your catch was and you won some hearts."
        $ skill_sta -= 2
        $ skill_luc -= 2
        if skill_cha <= 17:
            $ skill_cha += 3
        else:
            $ skill_cha = 20
        $ renpy.notify("You used 2 Stamina Points")
        $ renpy.pause(1,hard=False)
        $ renpy.notify("You used 2 Luck Points")
        $ renpy.pause(1,hard=False)
        $ renpy.notify("You gained 3 Charisma Points")
        $ renpy.pause(1,hard=False)

        jump lbl_beachmain_day

    else:
        "You were fixated on catching that frisbee that you didn't see where or who you were rocketing towards."
        jump lbl_hitomi_beach_accident_pre

####################
## Pre Dialogue
label lbl_hitomi_beach_accident_pre:
    if hitomibeachaccident_firsttimedone == 0:
        pass
    else:
        jump lbl_hitomi_beach_accident_pre_2

    if hscene_xray == 0:
        scene bg hitomibeachaccident_4
        with hpunch
    else:
        scene bg hitomibeachaccident_4_0
        with hpunch
    hit "AHhhh!"
    pov "Oof-!"
    pov "Oh my god, I'm so so-"
    pov "Hitomi?"
    hit "Egghh... [povname]?"
    hit "W-What the hell are you do-ing..?!"
    if hitomi_path == 17.8:
        pov "I- was trying to catch the pages."
    else:
        pov "I- was trying to catch a frisbee."
    pov "I'm really sorry, I didn't see where I was going."
    pov "Are you okay?"
    hit "Ughh.. Mm.. I think so...?"
    hit "{i}*Exhales*{/i} I think you knocked the wind out of me..."
    hit "My ass feels tight... do you mind getting off?"
    pov "Get off..?"
    pov "Sure-"
    if hscene_xray == 0:
        show bg hitomibeachaccident_3
        $ renpy.pause(0.4,hard=True)
        show bg hitomibeachaccident_2
        $ renpy.pause(0.4,hard=True)
        show bg hitomibeachaccident_1
    else:
        show bg hitomibeachaccident_3_0
        $ renpy.pause(0.4,hard=True)
        show bg hitomibeachaccident_2_0
        $ renpy.pause(0.4,hard=True)
        show bg hitomibeachaccident_1_0
    hit "Ahh!"
    with hpunch
    hit "What is that, what's- I feel something?"
    pov "Hmm?"
    pov "Oh- I- uh... might..."
    pov "Or might not be..."
    pov "Inside you right now..."
    hit "Whaaat?!"
    pov "Hold on-"
    if hscene_xray == 0:
        show bg hitomibeachaccident_2
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_3
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_4
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_1
        $ renpy.pause(0.3,hard=True)
    else:
        show bg hitomibeachaccident_2_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_3_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_4_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_1_0
        $ renpy.pause(0.3,hard=True)
    hit "{i}*Moans*{/i} Ay- wh- I tol- you to get off!"
    pov "I am getting off on you."
    pov "That's what you told me to do, right?"
    if hscene_xray == 0:
        show bg hitomibeachaccident_2
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_3
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_4
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_1
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_3
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_4
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_1
        $ renpy.pause(0.3,hard=True)
    else:
        show bg hitomibeachaccident_2_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_3_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_4_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_1_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_3_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_4_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_2_0
        $ renpy.pause(0.3,hard=True)
        show bg hitomibeachaccident_1_0
        $ renpy.pause(0.3,hard=True)
    hit "Fuck... Mm.."
    hit "Th- oh fuck it..."
    hit "Your cock is feels too good to say no to..."

    $ hitomibeachaccident_firsttimedone = 1

    jump lbl_hitomi_beach_accident_0

label lbl_hitomi_beach_accident_pre_2:
    if hscene_xray == 0:
        scene bg hitomibeachaccident_4
        with hpunch
    else:
        scene bg hitomibeachaccident_4_0
        with hpunch
    hit "Ahh! Fuck!"
    hit "Again, [povname]?!"
    hit "Why the fuck do you keep running into me?"
    pov "I could ask you why you keep standing in the same place."
    hit "Oh just shut up and ram your cock into me."
    hit "I gotta head back to work soon."

    jump lbl_hitomi_beach_accident_0

label lbl_hitomi_beach_accident_0:
    $ hitomi_beach_accident_counter = 0
    if hscene_xray == 0:
        jump lbl_hitomi_beach_accident_1
    else:
        jump lbl_hitomi_beach_accident_1_0

####################
## Stage 1
label lbl_hitomi_beach_accident_1:
    $ hitomi_beach_accident_counter += 1
    scene img_hitomi_beach_accident_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_1

image img_hitomi_beach_accident_stage_1:
    "bg hitomibeachaccident_1"
    pause 0.2
    "bg hitomibeachaccident_2"
    pause 0.2
    "bg hitomibeachaccident_3"
    pause 0.2
    "bg hitomibeachaccident_4"
    pause 0.2
    "bg hitomibeachaccident_2"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_hitomi_beach_accident_1_0:
    $ hitomi_beach_accident_counter += 1
    scene img_hitomi_beach_accident_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_2_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_2_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_cum

image img_hitomi_beach_accident_stage_1_0:
    "bg hitomibeachaccident_1_0"
    pause 0.2
    "bg hitomibeachaccident_2_0"
    pause 0.2
    "bg hitomibeachaccident_3_0"
    pause 0.2
    "bg hitomibeachaccident_4_0"
    pause 0.2
    "bg hitomibeachaccident_2_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_hitomi_beach_accident_2:
    $ hitomi_beach_accident_counter += 1
    scene img_hitomi_beach_accident_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_2

image img_hitomi_beach_accident_stage_2:
    "bg hitomibeachaccident_5"
    pause 0.2
    "bg hitomibeachaccident_6"
    pause 0.1
    "bg hitomibeachaccident_7"
    pause 0.2
    "bg hitomibeachaccident_6"
    pause 0.2
    repeat
####################
## Stage 2 XRAY
label lbl_hitomi_beach_accident_2_0:
    $ hitomi_beach_accident_counter += 1
    scene img_hitomi_beach_accident_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_3_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_2_0

image img_hitomi_beach_accident_stage_2_0:
    "bg hitomibeachaccident_5_0"
    pause 0.2
    "bg hitomibeachaccident_6_0"
    pause 0.1
    "bg hitomibeachaccident_7_0"
    pause 0.2
    "bg hitomibeachaccident_6_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_hitomi_beach_accident_3:
    $ hitomi_beach_accident_counter += 1
    scene img_hitomi_beach_accident_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_3
image img_hitomi_beach_accident_stage_3:
    "bg hitomibeachaccident_8"
    pause 0.2
    "bg hitomibeachaccident_9"
    pause 0.1
    "bg hitomibeachaccident_10"
    pause 0.2

    repeat
####################
## Stage 3 XRAY
label lbl_hitomi_beach_accident_3_0:
    $ hitomi_beach_accident_counter += 1
    scene img_hitomi_beach_accident_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_3_0

image img_hitomi_beach_accident_stage_3_0:
    "bg hitomibeachaccident_8_0"
    pause 0.2
    "bg hitomibeachaccident_9_0"
    pause 0.1
    "bg hitomibeachaccident_10_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_hitomi_beach_accident_cum:
    if hitomi_points <= 8:
        jump lbl_hitomi_beach_accident_cum_2
    else:
        jump lbl_hitomi_beach_accident_cum_2
        #jump lbl_hitomi_beach_accident_cum_3

label lbl_hitomi_beach_accident_cum_2:
    #if hscene_xray == 0:
    #    scene bg hitomibeachaccident_1
    #else:
    #    scene bg hitomibeachaccident_1_0
    call screen scr_hitomi_beach_accident_cum_2

screen scr_hitomi_beach_accident_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_cumchoice")

label lbl_hitomi_beach_accident_cum_3:
    if hscene_xray == 0:
        scene bg hitomibeachaccident_1
    else:
        scene bg hitomibeachaccident_1_0
    call screen scr_hitomi_beach_accident_cum_3

screen scr_hitomi_beach_accident_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_scenechoice_mish")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_mish_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_cumchoice")

label lbl_hitomi_beach_accident_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_hitomi_beach_accident_cumin
            else:
                jump lbl_hitomi_beach_accident_cumin_0
        "Cum on her":
            jump lbl_hitomi_beach_accident_cumout

####################
## Cum In
label lbl_hitomi_beach_accident_cumin:
    scene bg hitomibeachaccident_1
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_2
    $ renpy.pause(1.5,hard=True)
    show bg hitomibeachaccident_11_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_11_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_11_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_11_4
    $ renpy.pause(0.8,hard=True)
    hit "Ahh- you actually came inside me!"
    pov "Sorry, didn't think you'd mind."
    hit "I need to go get a Plan B pill."
    hit "I wasn't expecting to get creampied today."
    hit "Usually guys put on a condom."
    pov "The lifeguard made it loud and clear that we must all be completely naked."
    hit "She also preaches no littering and yet you've made a mess inside of me."
    hit "{i}*Sigh*{/i} You better come by and buy some comics sometime."
    pov "Happy to see you more often."
    scene black
    with fade
    if hitomi_points < 10:
        $ hitomi_points += 1
        $ renpy.notify("Your relationship with Hitomi has increased")
    $ renpy.pause()
    "After cleaning up..."
    "And by cleaning up, I mean letting all my cum drip onto the sand and burying it with our feet..."

    if hitomi_path == 17.8:
        ## Naughty Winds
        jump lbl_naughty_winds_2
    else:
        scene bg beachmain_day
        with fade

    jump lbl_beachmain_day

####################
## Cum In XRAY
label lbl_hitomi_beach_accident_cumin_0:
    scene bg hitomibeachaccident_1_0
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_2_0
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_3_0
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_12_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_4
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_5
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_6
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_7
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_8
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_9
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_10
    $ renpy.pause(0.8,hard=True)
    hit "Ahh- you actually came inside me!"
    pov "Sorry, didn't think you'd mind."
    hit "I need to go get a Plan B pill."
    hit "I wasn't expecting to get creampied today."
    hit "Usually guys put on a condom."
    pov "The lifeguard made it loud and clear that we must all be completely naked."
    hit "She also preaches no littering and yet you've made a mess inside of me."
    hit "{i}*Sigh*{/i} You better come by and buy some comics sometime."
    pov "Happy to see you more often."
    scene black
    with fade
    if hitomi_points < 10:
        $ hitomi_points += 1
        $ renpy.notify("Your relationship with Hitomi has increased")
    $ renpy.pause()
    "After cleaning up..."
    "And by cleaning up, I mean letting all my cum drip onto the sand and burying it with our feet..."

    if hitomi_path == 17.8:
        ## Naughty Winds
        jump lbl_naughty_winds_2
    else:
        scene bg beachmain_day
        with fade

    jump lbl_beachmain_day

####################
## Missionary Cum Out
label lbl_hitomi_beach_accident_cumout:
    if hscene_xray == 0:
        scene bg hitomibeachaccident_1
        $ renpy.pause(0.2,hard=True)
    else:
        scene bg hitomibeachaccident_1_0
        $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_13_0
    $ renpy.pause(1.5,hard=True)
    show bg hitomibeachaccident_13_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_4
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_5
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_6
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_7
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_8
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_9
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_10
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_11
    $ renpy.pause(0.8,hard=True)
    hit "Ahh- you actually came all over me!"
    pov "Sorry, didn't think you'd mind."
    hit "This is a public beach!"
    hit "We're not supposed to be littering and making a mess."
    hit "I can't move, you're gonna have to go grab a towel or something."
    pov "Oh- uhm, I didn't bring a towel."
    hit "You came to the beach and you didn't bring a towel?"
    pov "I didn't expect to find myself in this situation-"
    hit "{i}*Sigh*{/i} Go grab mine from over there... ugh...."
    pov "Sure thing! Don't move, you stay right there."
    hit "Shut up."
    scene black
    with fade
    if hitomi_points < 10:
        $ hitomi_points += 1
        $ renpy.notify("Your relationship with Hitomi has increased")
    $ renpy.pause()
    "After cleaning up..."

    if hitomi_path == 17.8:
        ## Naughty Winds
        jump lbl_naughty_winds_2
    else:
        scene bg beachmain_day
        with fade

    jump lbl_beachmain_day
