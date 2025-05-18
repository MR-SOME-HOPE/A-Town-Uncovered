## Incest Porno with Mom ##
label lbl_incest_porno_with_mom:
    #default incestpornowithmom_counter = 0
    default incestpornowithmom = 0

    scene bg incestpornowithmom_1
    with fade
    if mum_points <= 7:
        if winc == 0:
            $ renpy.notify("Points too low with [missus]: [mum_points]/8")
        else:
            $ renpy.notify("Points too low with Mom: [mum_points]/8")
        show bg incestpornowithmom_2
        if winc == 0:
            pov "..[missus]?"
        else:
            pov "..Mom?"
        show bg incestpornowithmom_3
        with hpunch
        mum "Oh my God! Close the door!"
        scene bg myhallway_day
        with hpunch
        "{i}*Thuud!*{/i}"
        pov "..."
        pov "{i}Oh. Let's pretend that didn't happen.{/i}"
        $ mum_path = 22.5

        jump lbl_myhallway_day_setup
    else:
        pass
    show bg incestpornowithmom_2
    if winc == 0:
        pov "..[missus]? What are yo-"
    else:
        pov "..Mom? What are yo-"
    show bg incestpornowithmom_4
    mum "Hush up and shut the door, [povname]. Come over here."

    menu:
        "Close the door":
            $ incestpornowithmom = 1
        "Leave":
            show bg incestpornowithmom_5
            pov "Actually, I think it's better if I just leave you to... uhm... it."
            show bg incestpornowithmom_6
            mum "Bu-"
            scene bg myhallway_day
            with hpunch
            "{i}*Thuud!*{/i}"
            pov "{i}I'm just going to... pretend I didn't see that...{/i}"
            $ mum_path = 25

            jump lbl_myhallway_day_setup

    scene bg incestpornowithmom_7
    with fade
    pov "A-are you alright?"
    show bg incestpornowithmom_8
    mum "Now that you're here."
    show bg incestpornowithmom_7
    mum "..."
    show bg incestpornowithmom_9
    mum "Did I leave you speechless or are you naturally awkward? Hehehe."
    show bg incestpornowithmom_8
    mum "C'mon, baby. I won't bite."

    scene bg incestpornowithmom_10
    with fade
    $ renpy.pause()
    show bg incestpornowithmom_11
    mum "Like what you see, baby?"

    menu:
        "Yes, Mommy." if winc == 1:
            show bg incestpornowithmom_12
            pov "Yes, Mommy."
            show bg incestpornowithmom_13
            mum "Mmm... call me Mommy again."
            show bg incestpornowithmom_12
            pov "I'll call you anything you want, Mommy."
            show bg incestpornowithmom_13
            mum "I-I'm a little ashamed to admit, but that making me so wet."
        "Yes, thot." if winc == 0:
            show bg incestpornowithmom_12
            pov "Yes, thot."
            show bg incestpornowithmom_13
            mum "Mmm... call me thot again."
            show bg incestpornowithmom_12
            pov "I'll call you anything you want, thot."
            show bg incestpornowithmom_13
            mum "I-I'm a little ashamed to admit, but that making me so wet."
        "I love what I see.":
            show bg incestpornowithmom_12
            pov "I love what I see."
            show bg incestpornowithmom_11
            mum "I'm glad you do."
            show bg incestpornowithmom_13
            mum "You're so lucky to be able to see down there without using a mirror."
            show bg incestpornowithmom_12
            if winc == 0:
                pov "You look amazing, [missus]. More than amazing."
            else:
                pov "You look amazing, Mom. More than amazing."
            pov "The sexiest I've ever seen."
        "I bet you taste even better.":
            show bg incestpornowithmom_12
            pov "I bet you taste even better."
            show bg incestpornowithmom_13
            mum "Oh? Who said you're allowed to have a taste?"
            show bg incestpornowithmom_10
            pov "..."
            show bg incestpornowithmom_12
            pov "I can lick you right now if I want to."
            show bg incestpornowithmom_11
            mum "I'm joking, honey. Of course I want your tongue."
    show bg incestpornowithmom_13
    mum "Would you mind, sweetie?"
    mum "Would you mind taking care of me while I enjoy what's on TV?"
    show bg incestpornowithmom_14
    if winc == 0:
        pov "Is that the... what is it called again? “Milf fucks..'"
    else:
        pov "Is that the... what is it called again? “Mom fucks..'"
    show bg incestpornowithmom_15
    mum "Yeah, yeah, less talking, more eating."

#label lbl_incest_porno_with_mom_0:
    #$ skill_sta = 15#TEMP TEST
    #$ incestpornowithmom_counter = 0

    #jump lbl_incest_porno_with_mom_1

#label lbl_incest_porno_with_mom_0_2:
    #if skill_sta <= 14:
    #    $ incestpornowithmom_counter = 8
    #else:
    #    $ incestpornowithmom_counter = 10

    #jump lbl_incest_porno_with_mom_2

#label lbl_incest_porno_with_mom_0_3:
    #$ incestpornowithmom_counter = 18

    #jump lbl_incest_porno_with_mom_3

label lbl_incest_porno_with_mom_1:
    #$ incestpornowithmom_counter += 1
    #scene bg incestpornowithmom_16
    #$ renpy.pause(0.7,hard=True)
    #show bg incestpornowithmom_17
    #$ renpy.pause(0.7,hard=True)
    #if skill_sta <= 7 and incestpornowithmom_counter == 6:
    #    jump lbl_incest_porno_with_mom_finish
    #elif skill_sta <= 14 and incestpornowithmom_counter == 8:
    #    jump lbl_incest_porno_with_mom_1_2
    #elif skill_sta <= 20 and incestpornowithmom_counter == 10:
    #    jump lbl_incest_porno_with_mom_1_2
    #else:
    #    jump lbl_incest_porno_with_mom_1
    scene img_incest_porno_with_mom_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_incest_porno_with_mom_finish
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_incest_porno_with_mom_1_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_incest_porno_with_mom_1_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_incest_porno_with_mom_1

image img_incest_porno_with_mom_1:
    "bg incestpornowithmom_16"
    pause 0.7
    "bg incestpornowithmom_17"
    pause 0.7
    repeat


label lbl_incest_porno_with_mom_1_2:
    call screen scr_incest_porno_with_mom_1_2

screen scr_incest_porno_with_mom_1_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_incest_porno_with_mom_2")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_incest_porno_with_mom_1")

label lbl_incest_porno_with_mom_2:
    #$ incestpornowithmom_counter += 1
    #show bg incestpornowithmom_18
    #$ renpy.pause(0.7,hard=True)
    #show bg incestpornowithmom_19
    #$ renpy.pause(0.7,hard=True)
    #if skill_sta <= 14 and incestpornowithmom_counter == 16:
    #    jump lbl_incest_porno_with_mom_finish
    #elif skill_sta <= 20 and incestpornowithmom_counter == 18:
    #    jump lbl_incest_porno_with_mom_2_2
    #else:
    #    jump lbl_incest_porno_with_mom_2
    scene img_incest_porno_with_mom_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_incest_porno_with_mom_finish
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_incest_porno_with_mom_2_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_incest_porno_with_mom_2

image img_incest_porno_with_mom_2:
    "bg incestpornowithmom_18"
    pause 0.7
    "bg incestpornowithmom_19"
    pause 0.7
    repeat

label lbl_incest_porno_with_mom_2_2:
    call screen scr_incest_porno_with_mom_2_2

screen scr_incest_porno_with_mom_2_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_incest_porno_with_mom_3")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_incest_porno_with_mom_2")

label lbl_incest_porno_with_mom_3:
    #$ incestpornowithmom_counter += 1
    #show bg incestpornowithmom_20
    #$ renpy.pause(0.7,hard=True)
    #show bg incestpornowithmom_21
    #$ renpy.pause(0.7,hard=True)
    #if skill_sta <= 20 and incestpornowithmom_counter == 26:
    #    jump lbl_incest_porno_with_mom_3_2
    #else:
    #    jump lbl_incest_porno_with_mom_3
    scene img_incest_porno_with_mom_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_incest_porno_with_mom_3_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_incest_porno_with_mom_3
image img_incest_porno_with_mom_3:
    "bg incestpornowithmom_20"
    pause 0.7
    "bg incestpornowithmom_21"
    pause 0.7
    repeat

label lbl_incest_porno_with_mom_3_2:
    call screen scr_incest_porno_with_mom_3_2

screen scr_incest_porno_with_mom_3_2():
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_incest_porno_with_mom_cum")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_incest_porno_with_mom_3")

label lbl_incest_porno_with_mom_cum:
    scene bg incestpornowithmom_22 with vpunch
    with dissolve
    mum "Fucck..."
    mum "Fuck.. fu-mmm"
    mum "Ah-.. Mmm..."
    show bg incestpornowithmom_23
    mum "Fu... that felt good..."
    mum "..."
    show bg incestpornowithmom_24
    mum "Clean me up, baby. You're not done yet."
    pov "..."
    show bg incestpornowithmom_25
    $ renpy.pause(0.7,hard=True)
    show bg incestpornowithmom_26
    $ renpy.pause(0.7,hard=True)
    show bg incestpornowithmom_25
    $ renpy.pause(0.7,hard=True)
    show bg incestpornowithmom_26
    $ renpy.pause(0.7,hard=True)

label lbl_incest_porno_with_mom_finish:

    scene black
    with fade
    $ renpy.pause()
    "You mindlessly lap and suck up all of her juices as she continues to watch till the end of her ‘program'."
    "Nothing more, nothing less."
    "For now."
    if mum_points <= 9:
        $ mum_points += 1
    else:
        $ mum_points = 10
    if winc == 0:
        $ renpy.notify("Your relationship with [missus] has increased")
    else:
        $ renpy.notify("Your relationship with Mom has increased")
    $ mum_path = 23
    if gtime == 0:
        $ gtime += 1
        scene bg myhallway_day
        with fade

        jump lbl_myhallway_day_setup
    else:
        $ gtime = 2
        scene bg myhallway_night
        with fade

        jump lbl_myhallway_night_setup
