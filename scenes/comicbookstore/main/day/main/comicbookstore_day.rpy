###############
## Setup
## Story Path
label lbl_comicbookstore_day_setup:

    ## Welcome to Hendai's
    if main_story == 18:
        default abouthitomi_dating = 0
        default abouthitomi_magazine = 0
        default abouthitomi_work = 0
        default abouthitomi_go = 1
        ## Show the comic book store during the day.
        scene bg comicbookstore_day
        with fade

        jump lbl_welcome_to_hendais

    ## Sexworld Find Answers Around TOwn
    elif main_story == 33:
        if sexaroundtowncomicbookstore == 0:
            scene bg comicbookstore_daysexworld
            with fade

            jump lbl_sex_around_town_comicbookstore
        else:
            scene bg comicbookstore_daysexworld

            jump lbl_comicbookstore_day

    ## Store Takeover
    elif hitomi_path == 7:
        jump lbl_store_takeover
    ## Picking Up Hitomi
    elif hitomi_path == 10:
        jump lbl_picking_up_hitomi
    ## Dude Where's My Hitomi PRE
    elif hitomi_path == 15: #hitomi not at counter - in back room
        scene bg comicbookstore_day
        with fade
        pov "{i}Hitomi must be in the back room…{/i}"
        jump lbl_comicbookstore_day
    ## Art Inside The Video Camera
    elif hitomi_path == 17: #hitomi not at counter
        scene bg comicbookstore_day
        with fade
        show pov confused
        with dissolve
        pov "{i}Huh, that’s weird…{/i}"
        pov "{i}The store is open but Hitomi isn’t at the counter… Perhaps the nerds know where she is?{/i}"
        $ hitomi_path = 17.5 #hitomi not shown in store
        jump lbl_comicbookstore_day

    ## Store Rendezvous
    elif hitomi_path == 29:
       if 1 <= day <= 3:
           jump lbl_store_rendezvous
    ## No Event
    else:
        jump lbl_comicbookstore_day

###############
## Room Navigation
## This is the map for comic book store during the day
label lbl_comicbookstore_day:
    if main_story == 33:
        scene bg comicbookstore_daysexworld
    else:
        scene bg comicbookstore_day
    call screen scr_comicbookstore_day

screen scr_comicbookstore_day():

    if main_story != 33:
        imagebutton auto "btn comicbookstore_day_backroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookstore_day_backroom")
        if main_story != 84 and hitomi_path not in (15,17,17.2,17.5):
            if not (day == 5 and hitomibeach_day == 0 and insexworld == 0):
                imagebutton auto "btn comicbookstore_day_hitomi_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookstore_day_hitomi")
            if main_story != 100 and hitomi_path != 8:
                if ( gtime == 1 and (main_story in (16,17,18,19,20,21,22,24,25,26,27) or main_story >= 35) ) or (gtime == 0 and day >= 5):
                    imagebutton auto "btn comicbookstore_day_jacob_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookstore_day_jacob")
        elif main_story == 84:
            imagebutton auto "btn comicbookstore_day_hitomi_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_investigations_hitomi")
            imagebutton auto "btn comicbookstore_day_jacob_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_investigations_jacob")
    else:
        imagebutton auto "btn comicbookstore_daysexworld_backroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookstore_day_backroom")

    imagebutton auto "btn comicbookstore_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_day_setup")
    use hud_overlay

###############
## Labels
## Locations
label lbl_comicbookstore_day_backroom:
    if main_story == 33:
        if sexaroundtowncomicbookstore == 2:
            jump lbl_sex_around_town_comicbookstore_1
        else:
            jump lbl_sex_around_town_comicbookstore_2
    else:
        jump lbl_comicbookbackroom_day_setup

## Stores
################################################################################
## HENDAI'S ##
label lbl_comicbookstoremenu:
    #scene bg comicbookstore_day behind bg comicbookstoremenu
    show bg comicbookstore_day behind hit
    call screen scr_comicbookstoremenu
    #scene bg comicbookstore_day behind scr_comicbookstoremenu

screen scr_comicbookstoremenu():
    add "bg comicbookstoremenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_comicbookstoremenu"), Jump("lbl_comicbookstore_day")]

## Items
    imagebutton auto "btn menuitems_fbpwmag1_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_comicbookstoremenu_fbpwmag1")
    if abouthitomi_magazine == 1:
        imagebutton auto "btn menuitems_fbpwmag2_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_comicbookstoremenu_fbpwmag2")
        imagebutton auto "btn menuitems_fbpwmag3_%s" xpos 532 ypos 312 focus_mask True action Jump("lbl_comicbookstoremenu_fbpwmag3")
        imagebutton auto "btn menuitems_fbpwmag4_%s" xpos 708 ypos 312 focus_mask True action Jump("lbl_comicbookstoremenu_fbpwmag4")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # FBPWMag1
    hbox xpos 235 ypos 476 spacing 20:
        text "$30" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    if abouthitomi_magazine == 1:
        # FBPWMag2
        hbox xpos 411 ypos 476 spacing 20:
            text "$30" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"
        # FBPWMag3
        hbox xpos 589 ypos 476 spacing 20:
            text "$30" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"
        # FBPWMag4
        hbox xpos 766 ypos 476 spacing 20:
            text "$30" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## FBPWMag1
label lbl_comicbookstoremenu_fbpwmag1:
    hide screen scr_comicbookstoremenu
    if inventory.has_item(Items.fbpwmag1):
        #show bg comicbookstoremenu
        "You already have that item."
    elif inventory.money >= 30:
        $ inventory.buy(Items.fbpwmag1)
        $ renpy.notify("New Item Obtained: Fuck Bitches Pay Weekly, Issue no. 147")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    if abouthitomi_magazine == 0 and inventory.has_item(Items.fbpwmag1):
        $ abouthitomi_magazine = 1
        jump lbl_about_hitomi_2
    else:
        call screen scr_comicbookstoremenu

## FBPWMag2
label lbl_comicbookstoremenu_fbpwmag2:
    hide screen scr_comicbookstoremenu
    if inventory.has_item(Items.fbpwmag2):
        #show bg comicbookstoremenu
        "You already have that item."
    elif inventory.money >= 30:
        $ inventory.buy(Items.fbpwmag2)
        $ renpy.notify("New Item Obtained: Fuck Bitches Pay Weekly, Issue no. 152")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_comicbookstoremenu

## FBPWMag3
label lbl_comicbookstoremenu_fbpwmag3:
    hide screen scr_comicbookstoremenu
    if inventory.has_item(Items.fbpwmag3):
        #show bg comicbookstoremenu
        "You already have that item."
    elif inventory.money >= 30:
        $ inventory.buy(Items.fbpwmag3)
        $ renpy.notify("New Item Obtained: Fuck Bitches Pay Weekly, Issue no. 168")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_comicbookstoremenu

## FBPWMag4
label lbl_comicbookstoremenu_fbpwmag4:
    hide screen scr_comicbookstoremenu
    if inventory.has_item(Items.fbpwmag4):
        #show bg comicbookstoremenu
        "You already have that item."
    elif inventory.money >= 30:
        $ inventory.buy(Items.fbpwmag4)
        $ renpy.notify("New Item Obtained: Fuck Bitches Pay Weekly, Issue no. 175")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_comicbookstoremenu
