## Allaway Under The Desk ##
label lbl_allaway_under_the_desk:
    #default allaway_under_the_desk_counter = 0

    scene black
    with fade
    $ renpy.pause()
    "Later at night, after everyone is gone..."

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

####################
## Under the Desk Stage 1
label lbl_allaway_under_the_desk_1:
    scene img_allaway_under_the_desk_stage_1
    #$ allaway_under_the_desk_counter += 1
    #show bg allawayunderthedesk_1
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayunderthedesk_2
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayunderthedesk_3
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayunderthedesk_4
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayunderthedesk_2
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_under_the_desk_counter == 4:
    #    jump lbl_allaway_under_the_desk_next
    #elif skill_sta <= 14 and allaway_under_the_desk_counter == 6:
    #    jump lbl_allaway_under_the_desk_2
    #elif skill_sta <= 20 and allaway_under_the_desk_counter == 8:
    #    jump lbl_allaway_under_the_desk_2
    #else:
    #    jump lbl_allaway_under_the_desk_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_under_the_desk_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_under_the_desk_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_under_the_desk_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_under_the_desk_1

image img_allaway_under_the_desk_stage_1:
    "bg allawayunderthedesk_1"
    pause 0.3
    "bg allawayunderthedesk_2"
    pause 0.1
    "bg allawayunderthedesk_3"
    pause 0.3
    "bg allawayunderthedesk_4"
    pause 0.3
    "bg allawayunderthedesk_2"
    pause 0.3
    repeat

####################
## Under the Desk Stage 2
label lbl_allaway_under_the_desk_2:
    scene img_allaway_under_the_desk_stage_2
    #$ allaway_under_the_desk_counter += 1
    #show bg allawayunderthedesk_1
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayunderthedesk_2
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayunderthedesk_3
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayunderthedesk_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_under_the_desk_counter == 14:
    #    jump lbl_allaway_under_the_desk_next
    #elif skill_sta <= 20 and allaway_under_the_desk_counter == 16:
    #    jump lbl_allaway_under_the_desk_3
    #else:
    #    jump lbl_allaway_under_the_desk_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_under_the_desk_next

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_under_the_desk_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_under_the_desk_2

image img_allaway_under_the_desk_stage_2:
    "bg allawayunderthedesk_1"
    pause 0.2
    "bg allawayunderthedesk_2"
    pause 0.1
    "bg allawayunderthedesk_3"
    pause 0.2
    "bg allawayunderthedesk_2"
    pause 0.2
    repeat

####################
## Under the Desk Stage 3
label lbl_allaway_under_the_desk_3:
    scene img_allaway_under_the_desk_stage_3
    #$ allaway_under_the_desk_counter += 1
    #show bg allawayunderthedesk_1
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayunderthedesk_3
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayunderthedesk_2
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and allaway_under_the_desk_counter == 24:
    #    jump lbl_allaway_under_the_desk_next
    #else:
    #    jump lbl_allaway_under_the_desk_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_under_the_desk_next

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_under_the_desk_3

image img_allaway_under_the_desk_stage_3:
    "bg allawayunderthedesk_1"
    pause 0.1
    "bg allawayunderthedesk_3"
    pause 0.1
    "bg allawayunderthedesk_2"
    pause 0.1
    repeat

####################
## Under the Desk Next
label lbl_allaway_under_the_desk_next:
    scene bg allawayunderthedesk_6
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
    mis "Hey, why don't you use my mouth, [povname]?"
    show bg allawayunderthedesk_5
    pov "You offering a blowjob?"
    show bg allawayunderthedesk_1
    mis "Nope, not a blowjob."
    mis "You'll have to do all the work."
    mis "I'm offering you a face fuck."

    menu:
        "I'll take you up on that offer.":
            show bg allawayunderthedesk_6
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_7
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_8
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_6
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_5
            pov "I'll take you up on that offer."

            jump lbl_allaway_school_sex_facefuck
        "I'd rather shove it in your pussy.":
            show bg allawayunderthedesk_6
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_7
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_8
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_6
            $ renpy.pause(0.2,hard=True)
            show bg allawayunderthedesk_5
            pov "I'd rather shove it in your pussy right now if I'm honest."

            jump lbl_allaway_school_sex_farshots
