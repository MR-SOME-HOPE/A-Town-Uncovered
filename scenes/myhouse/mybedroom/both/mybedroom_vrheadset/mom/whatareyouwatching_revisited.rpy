## What are you Watching? ##
label lbl_what_are_you_watching_revisit:
    show bg momdrama_77
    with fade
    jump lbl_what_are_you_watching_revisit_wank_0

label lbl_what_are_you_watching_revisit_wank_0:
    $ vrheadset_revisitcounter = 0

    jump lbl_what_are_you_watching_revisit_wank_1

####################
## Wank Stage 1
label lbl_what_are_you_watching_revisit_wank_1:
    $ vrheadset_revisitcounter += 1
    show bg momdrama_76
    $ renpy.pause(0.5,hard=True)
    show bg momdrama_77
    $ renpy.pause(0.5,hard=True)
    jump lbl_what_are_you_watching_revisit_wank_counter

####################
## Wank Stage 2
label lbl_what_are_you_watching_revisit_wank_2:
    $ vrheadset_revisitcounter += 1
    show bg momdrama_76
    $ renpy.pause(0.3,hard=True)
    show bg momdrama_77
    $ renpy.pause(0.3,hard=True)
    jump lbl_what_are_you_watching_revisit_wank_counter

####################
## Wank Stage 3
label lbl_what_are_you_watching_revisit_wank_3:
    $ vrheadset_revisitcounter += 1
    show bg momdrama_78
    $ renpy.pause(0.2,hard=True)
    show bg momdrama_79
    $ renpy.pause(0.2,hard=True)
    jump lbl_what_are_you_watching_revisit_wank_counter

label lbl_what_are_you_watching_revisit_wank_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_what_are_you_watching_revisit_wank_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_what_are_you_watching_revisit_wank_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_what_are_you_watching_wank_revisit
    else:
        jump lbl_what_are_you_watching_revisit_wank_1


label lbl_what_are_you_watching_revisit_wank_4:
    if winc == 0:
        jump lbl_what_are_you_watching_revisit_7_winc0
    else:
        jump lbl_what_are_you_watching_revisit_7


screen scr_what_are_you_watching_wank_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_what_are_you_watching_revisit_wank_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_what_are_you_watching_revisit_wank_4")

####################
label lbl_what_are_you_watching_revisit_7:
    show bg momdrama_80
    $ renpy.pause(0.5,hard=True)
    show bg momdrama_80
    with vpunch
    dad "Honey, why aren't you in bed?"
    show bg momdrama_81
    mum "O-Oh! I was just watching my drama with [povname]. I'll be up in a bit."
    show bg momdrama_82
    dad "Alright, I need to ‘talk' to you about something."
    dad "Something big came up."
    show bg momdrama_81
    mum "Oh, um sure."
    mum "I guess it's bed time, [povname]. Thanks for staying the night with me."
    mum "I love you."
    show bg momdrama_83
    pov "I love you too, Mom."
    show bg momdrama_84
    $ renpy.pause()
    dad "Get to bed, [povname]."
    dad "Now."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
label lbl_what_are_you_watching_revisit_7_winc0:
    show bg momdrama_80
    $ renpy.pause(0.5,hard=True)
    show bg momdrama_80
    with vpunch
    dad "Honey, why aren't you in bed?"
    show bg momdrama_81
    mum "O-Oh! I was just watching my drama with [povname]. I'll be up in a bit."
    show bg momdrama_82
    dad "Alright, I need to ‘talk' to you about something."
    dad "Something big came up."
    show bg momdrama_81
    mum "Oh, um sure."
    mum "I guess it's bed time, [povname]. Thanks for staying the night with me."
    mum "I love you."
    show bg momdrama_83
    pov "I love you too, [missus]."
    show bg momdrama_84
    $ renpy.pause()
    dad "Get to bed, [povname]."
    dad "Now."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
