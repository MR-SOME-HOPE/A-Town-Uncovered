## Allaway Under The Desk ##
label lbl_allaway_under_the_desk_revisit:
    scene bg allawayunderthedesk_1
    with fade
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_1
    mis "Ah-"
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_1
    mis "Mmmmm-"
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_1
    mis "{i}*Gasp*{/i}"
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_1
    mis "Mmm.. your dick feels so nice against my clit, [povname]."
    mis "I can feel how badly you wanna stick it in."


label lbl_allaway_under_the_desk_revisit_reset:
    $ vrheadset_revisitcounter = 0
    jump lbl_allaway_under_the_desk_revisit_counter

####################
## Under the Desk Stage 1
label lbl_allaway_under_the_desk_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg allawayunderthedesk_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.1,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.3,hard=True)
    jump lbl_allaway_under_the_desk_revisit_counter

####################
## Under the Desk Stage 2
label lbl_allaway_under_the_desk_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg allawayunderthedesk_1
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.1,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    jump lbl_allaway_under_the_desk_revisit_counter

####################
## Under the Desk Stage 3
label lbl_allaway_under_the_desk_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg allawayunderthedesk_1
    $ renpy.pause(0.1,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.1,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.1,hard=True)
    jump lbl_allaway_under_the_desk_revisit_counter


label lbl_allaway_under_the_desk_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_allaway_under_the_desk_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_allaway_under_the_desk_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_allaway_school_under_the_desk_revisit_cum_revisit
    else:
        jump lbl_allaway_under_the_desk_revisit_1

screen scr_allaway_school_under_the_desk_revisit_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_under_the_desk_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_under_the_desk_revisit_next")


####################
## Under the Desk Next
label lbl_allaway_under_the_desk_revisit_next:
    show bg allawayunderthedesk_6
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_7
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_8
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_6
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_5
    pov "Heh- heh- Mmm... you've caught me red-handed."
    mis "Hehehe~"
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_1
    mis "As if I'll let you inside so early {i}*moan*{/i}..."
    mis "Mmm.. fuck..."
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_1
    mis "I'm surprised it hasn't accidentally slipped in itself with how wet I am."
    mis "Fuck..."
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_4
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayunderthedesk_1
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
