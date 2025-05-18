####################
## Missionary
label lbl_postcamgurlsubstitute_missionary:
    #default postcamgurlsubstitute_missionary_counter = 0
    #default postcamgurlsubstitute_anal_counter = 0

    scene bg postcamgurlsubstitute_missionary_cumout_1
    with fade
    $ renpy.pause()
    pov "Ready, [sister]?"
    sis "Shut up and put your money where your mouth is."

    jump postcamgurlsubstitute_missionary_fuck_options

label lbl_postcamgurlsubstitute_missionary_0:
    #$ postcamgurlsubstitute_missionary_counter = 0
    jump postcamgurlsubstitute_missionary_fuck_options

label lbl_postcamgurlsubstitute_missionary_anal_0:
    #$ postcamgurlsubstitute_anal_counter = 0
    jump postcamgurlsubstitute_missionary_fuck_options

menu postcamgurlsubstitute_missionary_fuck_options:
    "Pussy fuck":
        jump lbl_postcamgurlsubstitute_missionary_1
    "Anal fuck":
        jump lbl_postcamgurlsubstitute_missionary_anal_1

####################
## Missionary Stage 1
label lbl_postcamgurlsubstitute_missionary_1:
    scene img_postcamgurlsubstitute_missionary_stage_1
    #$ postcamgurlsubstitute_missionary_counter += 1
    #show bg postcamgurlsubstitute_missionary_1
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_2
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_3
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_4
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_5
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and postcamgurlsubstitute_missionary_counter == 4:
    #    jump lbl_postcamgurlsubstitute_missionary_cum
    #elif skill_sta <= 14 and postcamgurlsubstitute_missionary_counter == 6:
    #    jump lbl_postcamgurlsubstitute_missionary_2
    #elif skill_sta <= 20 and postcamgurlsubstitute_missionary_counter == 8:
    #    jump lbl_postcamgurlsubstitute_missionary_2
    #else:
    #    jump lbl_postcamgurlsubstitute_missionary_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_1

image img_postcamgurlsubstitute_missionary_stage_1:
    "bg postcamgurlsubstitute_missionary_1"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_2"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_3"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_4"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_5"
    pause 0.3
    repeat

####################
## Missionary Stage 1 ANAL
label lbl_postcamgurlsubstitute_missionary_anal_1:
    scene img_postcamgurlsubstitute_missionary_anal_stage_1
    #$ postcamgurlsubstitute_anal_counter += 1
    #show bg postcamgurlsubstitute_missionary_anal_1
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_2
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_3
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_4
    #$ renpy.pause(0.3,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_5
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and postcamgurlsubstitute_anal_counter == 4:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_cum
    #elif skill_sta <= 14 and postcamgurlsubstitute_anal_counter == 6:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_2
    #elif skill_sta <= 20 and postcamgurlsubstitute_anal_counter == 8:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_2
    #else:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_1

image img_postcamgurlsubstitute_missionary_anal_stage_1:
    "bg postcamgurlsubstitute_missionary_anal_1"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_anal_2"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_anal_3"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_anal_4"
    pause 0.3
    "bg postcamgurlsubstitute_missionary_anal_5"
    pause 0.3
    repeat

####################
## Missionary Stage 2
label lbl_postcamgurlsubstitute_missionary_2:
    scene img_postcamgurlsubstitute_missionary_stage_2
    #$ postcamgurlsubstitute_missionary_counter += 1
    #show bg postcamgurlsubstitute_missionary_1
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_2
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_3
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and postcamgurlsubstitute_missionary_counter == 14:
    #    jump lbl_postcamgurlsubstitute_missionary_cum
    #elif skill_sta <= 20 and postcamgurlsubstitute_missionary_counter == 16:
    #    jump lbl_postcamgurlsubstitute_missionary_3
    #else:
    #    jump lbl_postcamgurlsubstitute_missionary_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_2

image img_postcamgurlsubstitute_missionary_stage_2:
    "bg postcamgurlsubstitute_missionary_1"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_2"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_3"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_4"
    pause 0.2
    repeat

####################
## Missionary Stage 2 ANAL
label lbl_postcamgurlsubstitute_missionary_anal_2:
    scene img_postcamgurlsubstitute_missionary_anal_stage_2
    #$ postcamgurlsubstitute_anal_counter += 1
    #show bg postcamgurlsubstitute_missionary_anal_1
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_2
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_3
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and postcamgurlsubstitute_anal_counter == 14:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_cum
    #elif skill_sta <= 20 and postcamgurlsubstitute_anal_counter == 16:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_3
    #else:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_2

image img_postcamgurlsubstitute_missionary_anal_stage_2:
    "bg postcamgurlsubstitute_missionary_anal_1"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_anal_2"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_anal_3"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_anal_4"
    pause 0.2
    repeat

####################
## Missionary Stage 3
label lbl_postcamgurlsubstitute_missionary_3:
    scene img_postcamgurlsubstitute_missionary_stage_3
    #$ postcamgurlsubstitute_missionary_counter += 1
    #show bg postcamgurlsubstitute_missionary_1
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_3
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and postcamgurlsubstitute_missionary_counter == 24:
    #    jump lbl_postcamgurlsubstitute_missionary_cum
    #else:
    #    jump lbl_postcamgurlsubstitute_missionary_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_3

image img_postcamgurlsubstitute_missionary_stage_3:
    "bg postcamgurlsubstitute_missionary_1"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_3"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_4"
    pause 0.2
    repeat

####################
## Missionary Stage 3 ANAL
label lbl_postcamgurlsubstitute_missionary_anal_3:
    scene img_postcamgurlsubstitute_missionary_anal_stage_3
    #$ postcamgurlsubstitute_anal_counter += 1
    #show bg postcamgurlsubstitute_missionary_anal_1
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_3
    #$ renpy.pause(0.2,hard=True)
    #show bg postcamgurlsubstitute_missionary_anal_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and postcamgurlsubstitute_anal_counter == 24:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_cum
    #else:
    #    jump lbl_postcamgurlsubstitute_missionary_anal_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_postcamgurlsubstitute_missionary_anal_3

image img_postcamgurlsubstitute_missionary_anal_stage_3:
    "bg postcamgurlsubstitute_missionary_anal_1"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_anal_3"
    pause 0.2
    "bg postcamgurlsubstitute_missionary_anal_4"
    pause 0.2
    repeat

####################
## Missionary Cum
label lbl_postcamgurlsubstitute_missionary_cum:
    if sister_points <= 7:
        jump lbl_postcamgurlsubstitute_missionary_cum_2
    else:
        jump lbl_postcamgurlsubstitute_missionary_cum_3

label lbl_postcamgurlsubstitute_missionary_cum_2:

    #scene bg postcamgurlsubstitute_missionary_1
    call screen scr_postcamgurlsubstitute_missionary_cum_2

screen scr_postcamgurlsubstitute_missionary_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_cumchoice")

label lbl_postcamgurlsubstitute_missionary_cum_3:

    #scene bg postcamgurlsubstitute_missionary_1
    call screen scr_postcamgurlsubstitute_missionary_cum_3

screen scr_postcamgurlsubstitute_missionary_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_cumchoice")

####################
## Missionary Cum ANAL
label lbl_postcamgurlsubstitute_missionary_anal_cum:
    if sister_points <= 7:
        jump lbl_postcamgurlsubstitute_missionary_anal_cum_2
    else:
        jump lbl_postcamgurlsubstitute_missionary_anal_cum_3

label lbl_postcamgurlsubstitute_missionary_anal_cum_2:

    #scene bg postcamgurlsubstitute_missionary_anal_1
    call screen scr_postcamgurlsubstitute_missionary_anal_cum_2

screen scr_postcamgurlsubstitute_missionary_anal_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_anal_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_anal_cumchoice")

label lbl_postcamgurlsubstitute_missionary_anal_cum_3:

    #scene bg postcamgurlsubstitute_missionary_anal_1
    call screen scr_postcamgurlsubstitute_missionary_anal_cum_3

screen scr_postcamgurlsubstitute_missionary_anal_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_anal_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_anal_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_postcamgurlsubstitute_missionary_anal_cumchoice")

####################
## Cum Choice
label lbl_postcamgurlsubstitute_missionary_cumchoice:
    menu:
        "Cum Inside":
            jump lbl_postcamgurlsubstitute_missionary_cumin
        "Cum Outside":
            jump lbl_postcamgurlsubstitute_missionary_cumout

####################
## Cum Choice ANAL
label lbl_postcamgurlsubstitute_missionary_anal_cumchoice:
    menu:
        "Cum Inside":
            jump lbl_postcamgurlsubstitute_missionary_anal_cumin
        "Cum Outside":
            jump lbl_postcamgurlsubstitute_missionary_cumout

####################
## Missionary Cum In
label lbl_postcamgurlsubstitute_missionary_cumin:
    scene bg postcamgurlsubstitute_missionary_1
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumin_1
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumin_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumin_3
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumin_4
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumin_5
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumin_6
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumin_7
    $ renpy.pause(1,hard=True)
    sis "Oh fuck- oh fuck- oh fuck--!"
    sis "Mmmm-"
    sis "[povname]... did-"
    sis "{i}*Pants*{/i}"
    sis "Did you just..."
    sis "Cum inside me...?"
    pov "..."
    pov "I may or may not have..."
    sis "Fuck, man!"
    sis "Shit..."
    sis "Now I need to take an emergency pill."
    pov "Sorry. I think it was worth it though."
    sis "Shut up."
    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## Missionary Cum In ANAL
label lbl_postcamgurlsubstitute_missionary_anal_cumin:
    scene bg postcamgurlsubstitute_missionary_anal_1
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_anal_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_anal_6_1
    $ renpy.pause(0.5,hard=True)
    show bg postcamgurlsubstitute_missionary_anal_6_2
    $ renpy.pause(0.5,hard=True)
    show bg postcamgurlsubstitute_missionary_anal_6_3
    $ renpy.pause(0.5,hard=True)
    show bg postcamgurlsubstitute_missionary_anal_6_4
    $ renpy.pause()
    sis "Oh fuck- oh fuck- oh fuck--!"
    sis "Mmmm-"
    sis "[povname]... did-"
    sis "{i}*Pants*{/i}"
    sis "Did you just..."
    sis "Cum inside me...?"
    pov "..."
    pov "I may or may not have..."
    sis "Fuck, man!"
    sis "Shit..."
    sis "At least it was in my ass."
    pov "Now you don't need dinner! Hehehe~"
    sis "Shut up."
    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## Missionary Cum Out
label lbl_postcamgurlsubstitute_missionary_cumout:
    scene bg postcamgurlsubstitute_missionary_cumout_1
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumout_2
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumout_3
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumout_4
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumout_5
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumout_6
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumout_7
    $ renpy.pause(0.2,hard=True)
    show bg postcamgurlsubstitute_missionary_cumout_8
    $ renpy.pause(1,hard=True)
    sis "Oh God.. it's so fucking hot."
    sis "Oh shit!!"
    sis "Oh shit! Oh shit- oh shit!"
    pov "{i}*Pants*{/i}"
    pov "W-what's the matter?"
    sis "My fucking sheets is what, you asshole!"
    sis "Why don't you fucking wipe your ass with my pillow while you're at it."
    pov "You have a really weird way of orgasming."
    sis "I hate you and your big dick, you big dick."
    scene black
    with fade
    "After a bit of cleaning up..."
    $ renpy.pause(1.5)
    scene bg myhallway_day
    with fade
    $ sister_path = 41

    jump lbl_myhallway_day_setup

####################
## Missionary Next
label lbl_postcamgurlsubstitute_missionary_next:
    scene bg postcamgurlsubstitute_missionary_cumout_1
    sis "{i}*Pants*{/i}"
    pov "Let's swap positions."
    sis "T-tooo what?"

    jump lbl_postcamgurlsubstitute_scenechoice_missionary
## Missionary Anal Next
label lbl_postcamgurlsubstitute_missionary_anal_next:
    scene bg postcamgurlsubstitute_missionary_cumout_1
    sis "{i}*Pants*{/i}"
    pov "Let's swap positions."
    sis "T-tooo what?"
    jump lbl_postcamgurlsubstitute_scenechoice_missionary
