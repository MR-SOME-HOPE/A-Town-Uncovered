###############
## Setup
label lbl_mygarden_day_setup:
    ## In Trouble with Mom
    if main_story == 15:
        pov "{i}I shouldn't be sneaking around - especially after staying out without permission.{/i}"
        jump lbl_myhousefront_day_setup
    ## This Town is Crazy
    elif main_story == 34:
        if winc == 0:
            pov "{i}I need to talk to [missus] inside the house.{/i}"
        else:
            pov "{i}I need to talk to Mom inside the house.{/i}"
        jump lbl_myhousefront_day_setup
    ## Welcome Home Asshat
    elif main_story == 40:
        pov "{i}I shouldn't be sneaking around, I should just head in the front like a normal person.{/i}"
        jump lbl_myhousefront_day_setup
    ## Mom is Freaking Out
    elif main_story == 55:
        pov "{i}I shouldn't be sneaking around, I should just head in the front like a normal person.{/i}"
        jump lbl_myhousefront_day_setup
    ## Mom is Freaking Out
    elif main_story == 63.3:
        pov "{i}I shouldn't be sneaking around, I should just head in the front like a normal person.{/i}"
        jump lbl_myhousefront_day_setup
    ## Girls' Upstairs
    elif main_story == 77:
        pov "{i}I shouldn't be sneaking around, I should just head in the front like a normal person.{/i}"
        jump lbl_myhousefront_day_setup
    ## Investigations
    elif main_story == 84 and investigations_complete == 1:
        pov "{i}No time to be screwing around in the garden.{/i}"
        jump lbl_myhousefront_day_setup
    # ## Modern Day Parental Punishment
    # elif main_story == 141:
    #     pov "{i}I should enter through the front.{/i}"
    #     jump lbl_myhousefront_day_setup
    ## In Trouble With Mom School Trap
    elif missallaway_path == 9:
        pov "{i}I shouldn't be sneaking around - especially after staying out without permission.{/i}"
        jump lbl_myhousefront_day_setup
    ## NO EVENT
    else:
        jump lbl_mygarden_day

###############
## Room Navigation
label lbl_mygarden_day:
    if mowed_lawn:
        scene bg mygarden_day
    else:
        scene bg mygarden_day_grassy
    call screen scr_mygarden_day

screen scr_mygarden_day():
    use hud_overlay
    imagebutton auto "btn mygarden_day_dining_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mydiningroom_day_setup")
    imagebutton auto "btn mygarden_day_front_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhousefront_day_setup")
    if mowed_lawn:
        imagebutton auto "btn mygarden_day_shed_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_day_shed")
        imagebutton auto "btn mygarden_day_pond_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_day_pond")
    else:
        imagebutton auto "btn mygarden_day_grassy_shed_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_day_shed")

label lbl_mygarden_day_pond:
    pov "{i}It is a pond.{/i}"
    call screen scr_mygarden_day

label lbl_mygarden_day_shed:
    if mowed_lawn:
        pov "{i}It's locked.{/i}"
    else:
        pov "{i}The garden is too overgrown to get to.{/i}"
    call screen scr_mygarden_day
