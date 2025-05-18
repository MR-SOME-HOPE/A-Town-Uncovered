####################
## Mom Shower Standing Leg Up

label lbl_mom_shower_standing_legup:
    ## PRE STORY
    scene bg momshowerstandinglegup_1
    mum "Have any plans for tonight, honey?"
    pov "Not sure yet."
    mum "Well, I'm home to hang out with if you want."
    if winc == 0:
        "I know, [missus]."
    else:
        "I know, mom."
    mum "Let me wash you up, sweetie."
    mum "Just relax."

    jump lbl_mom_shower_standing_legup_0

label lbl_mom_shower_standing_legup_0:
    scene bg momshowerstandinglegup_1
    with fade
    jump lbl_mom_shower_standing_legup_1

####################
## Stage 1
label lbl_mom_shower_standing_legup_1:
    scene img_mom_shower_standing_legup_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_shower_standing_legup_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_shower_standing_legup_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_shower_standing_legup_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_shower_standing_legup_1

image img_mom_shower_standing_legup_stage_1:
    "bg momshowerstandinglegup_1"
    pause 0.2
    "bg momshowerstandinglegup_2"
    pause 0.2
    "bg momshowerstandinglegup_3"
    pause 0.2
    "bg momshowerstandinglegup_4"
    pause 0.2
    "bg momshowerstandinglegup_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_mom_shower_standing_legup_2:
    scene img_mom_shower_standing_legup_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_shower_standing_legup_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_shower_standing_legup_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_shower_standing_legup_2

image img_mom_shower_standing_legup_stage_2:
    "bg momshowerstandinglegup_5"
    pause 0.2
    "bg momshowerstandinglegup_7"
    pause 0.1
    "bg momshowerstandinglegup_8"
    pause 0.2
    "bg momshowerstandinglegup_6"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_mom_shower_standing_legup_3:
    scene img_mom_shower_standing_legup_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_shower_standing_legup_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_shower_standing_legup_3

image img_mom_shower_standing_legup_stage_3:
    "bg momshowerstandinglegup_9"
    pause 0.2
    "bg momshowerstandinglegup_12"
    pause 0.2
    "bg momshowerstandinglegup_10"
    pause 0.2
    repeat

####################
## Cum
label lbl_mom_shower_standing_legup_menu:
    call screen scr_mom_shower_standing_legup_menu

screen scr_mom_shower_standing_legup_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_shower_standing_legup_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_shower_standing_legup_cumin")

####################
## Cum In
label lbl_mom_shower_standing_legup_cumin:
    if winc == 0:
        pov "[missus]- I'm gonna cum..."
    else:
        pov "Mom- I'm gonna cum..."
    mum "Let it all out, cupcake."
    mum "Give me your creampie."
    mum "I want to feel it inside me!"
    pov "Mmm--"
    pov "Fu--"
    scene bg momshowerstandinglegup_5
    $ renpy.pause(1.5,hard=True)
    show bg momshowerstandinglegup_13_1
    $ renpy.pause(0.4,hard=True)
    show bg momshowerstandinglegup_13_2
    $ renpy.pause(0.4,hard=True)
    show bg momshowerstandinglegup_13_3
    $ renpy.pause(0.4,hard=True)
    show bg momshowerstandinglegup_13_4
    $ renpy.pause(0.4,hard=True)
    show bg momshowerstandinglegup_13_5
    mum "Oh my- Mmmmm~"
    mum "Good boy~"
    mum "Hehe~ You did so good, honey!"
    pov "{i}*Huff huff*{/i} Thanks..."
    pov "You-"
    pov "-too.."
    pov "Fuuc-!"
    mum "[povname]..?!"
    mum "Must I say it again?"
    pov "Sorry... no cursing, I know."
    mum "Mhmm-"
    mum "Now, pull out and let's wash off."
    mum "I have to go out grocery shopping."
    pov "Alright."
    scene black
    with fade
    $ renpy.pause()
    "After washing off..."
    $ gtime += 1
    if gtime == 1:
        scene bg myhallway_day
        with fade
        jump lbl_myhallway_day_setup
    else:
        scene bg myhallway_night
        with fade
        jump lbl_myhallway_night_setup
