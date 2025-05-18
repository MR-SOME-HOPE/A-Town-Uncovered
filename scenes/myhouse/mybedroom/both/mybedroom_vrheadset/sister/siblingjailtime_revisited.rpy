
label lbl_sibling_jail_time_revisit:
    $ vrheadset_revisitcounter = 0
    scene bg handyinjail_1
    with fade
    sis "Hey, I knew it. It's almost a perfect fit."
    show bg handyinjail_2
    sis "A little loose though.."
    show bg handyinjail_3
    pov "Don't worry, I can make it fit more snugged."
    show bg handyinjail_4
    pov "Check this shit out!"
    show bg handyinjail_5
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg handyinjail_6
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg handyinjail_7
    sis "Whoa!!"
    show bg handyinjail_8
    pov "Ah- ah- ahhh... [sister], it's tight... ge- get it off!"
    show bg handyinjail_9
    with hpunch
    mina "HEY! WHAT THE HELL ARE YOU BOTH DOING?!"
    mina "WHERE DID YOU GET THOSE KEYS?!"
    mina "ARE YOU FUCKING SERIOUS, PAUL?! WHERE ARE THE SPARE KEYS?!"
    show bg handyinjail_10
    pau "Those... are the spare keys."
    mina "And what the fuck were you doing? You were supposed to keep an eye on these two."
    mina "Is that a nudie mag you're sitting on?!"
    show bg handyinjail_11
    mina "For God's sakes, Paul."
    mina "Gimme those fucking keys or you'll get into extra trouble!"
    show bg handyinjail_12
    sis "I- I can't, I think it's stuck."
    show bg handyinjail_13
    pov "It feels very very very..."
    pov "Very much stuck..."
    show bg handyinjail_14
    mina "I can't fucking believe this... I hate dealing with drunk teenagers."
    mina "I'll be right back, I'll get some soap or something to slip it off."
    show bg handyinjail_15
    $ renpy.pause()
    show bg handyinjail_16
    $ renpy.pause(0.4,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.4,hard=True)
    show bg handyinjail_18
    $ renpy.pause(0.2,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.4,hard=True)
    show bg handyinjail_20
    pau "Hey! Stop doing that!"
    show bg handyinjail_19
    sis "Shut up, Paul."
    show bg handyinjail_20
    pov "Yeah, shut up... Stev-"
    show bg handyinjail_19
    sis "Paul."
    show bg handyinjail_20
    pov "Paul!"
    show bg handyinjail_21
    sis "You know you wanna watch..."
    show bg handyinjail_22
    sis "Sit there and keep quiet, I know what I'm doing."

    jump lbl_handy_in_jail_revisit_0

label lbl_handy_in_jail_revisit_0:
    $ vrheadset_revisitcounter = 0

    jump lbl_handy_in_jail_revisit_1

####################
## Stage 1
label lbl_handy_in_jail_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg handyinjail_15
    $ renpy.pause(0.15,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_18
    $ renpy.pause(0.15,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.15,hard=True)
    show bg handyinjail_15
    $ renpy.pause(0.15,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_18
    $ renpy.pause(0.15,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.15,hard=True)
    jump lbl_handy_in_jail_revisit_counter

####################
## Stage 2
label lbl_handy_in_jail_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg handyinjail_15
    $ renpy.pause(0.15,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_18
    $ renpy.pause(0.1,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.1,hard=True)
    show bg handyinjail_15
    $ renpy.pause(0.15,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_18
    $ renpy.pause(0.1,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.1,hard=True)
    jump lbl_handy_in_jail_revisit_counter

####################
## Stage 3
label lbl_handy_in_jail_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg handyinjail_15
    $ renpy.pause(0.1,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.1,hard=True)
    show bg handyinjail_15
    $ renpy.pause(0.1,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.05,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.1,hard=True)
    jump lbl_handy_in_jail_revisit_counter

label lbl_handy_in_jail_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_handy_in_jail_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_handy_in_jail_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_handy_in_jail_cum_revisit
    else:
        jump lbl_handy_in_jail_revisit_1

screen scr_handy_in_jail_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_handy_in_jail_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_handy_in_jail_revisit_cum_1")

label lbl_handy_in_jail_revisit_cum_1:
    show bg handyinjail_23_0
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_1
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_2
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_3
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_4
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_5
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_6
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_7
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_8
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_9
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_10
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_11
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_12
    $ renpy.pause()
    show bg handyinjail_24
    sis "There we go. That should do it"
    show bg handyinjail_25
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg handyinjail_26
    with dissolve
    $ renpy.pause(0.5,hard=True)
    pov "Ahh.. that feels a ton better..."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
