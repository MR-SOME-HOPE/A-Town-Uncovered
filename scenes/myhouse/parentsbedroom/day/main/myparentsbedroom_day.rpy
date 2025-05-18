###############
## Setup
## Story Path
label lbl_parentsbedroom_day_setup:
    ## First Morning
    if main_story <= 4:
        if winc == 0:
            pov "{i}It's locked. [dadname] must still be in there.{/i}"
        else:
            pov "{i}It's locked. Dad must still be in there.{/i}"
        call screen scr_myhallway_day
    ##
    elif main_story == 28:
        pov "{i}It's locked.{/i}"
        call screen scr_myhallway_day
    ## Quality Family Time
    elif main_story == 78:
        jump lbl_quality_family_time
    ## Sister in the Basement
    if sister_path == 10 or sister_path == 16 or sister_path == 33.5:
        pov "{i}I really should head down to the basement right now.{/i}"
        call screen scr_myhallway_day
    ##
    if mum_path == 7:
        pov "{i}It's locked.{/i}"
        call screen scr_myhallway_day
    ## Cheer Mom Up
    elif 11 <= mum_path <= 14:
        if mum_path == 11:
            jump lbl_cheermomup_pt1
        elif mum_path == 12:
            if inventory.has_item(Items.icecream1):
                jump lbl_cheermomup_pt2
            elif inventory.has_item(Items.icecream2):
                jump lbl_cheermomup_pt2
            elif inventory.has_item(Items.icecream3):
                jump lbl_cheermomup_pt2
            elif inventory.has_item(Items.icecream4):
                jump lbl_cheermomup_pt2
            else:
                pov "{i}Mom's expecting some icecream.{/i}"
        elif mum_path == 13:
            if inventory.has_item(Items.smarttvbox):
                jump lbl_cheermomup_pt3
            else:
                pov "{i}I need to buy something so Mom can watch WebFlicks on TV.{/i}"
        elif mum_path == 14:
            if inventory.has_item(Items.teddybear1) or inventory.has_item(Items.teddybear2) or inventory.has_item(Items.teddybear3):
                default cheermomup_doorbear = 0
                jump lbl_open_the_door
            else:
                pov "{i}She said she wants a teddy.{/i}"
                pov "{i}I have no teddy to give...{/i}"
                pov "{i}I see what the problem is.{/i}"
        call screen scr_myhallway_day
    ## Instantly After Open the Damn Door
    elif mum_path == 15:
        pov "{i}I should leave her alone, seems like she doesn't want a proper face to face conversation just yet.{/i}"
        call screen scr_myhallway_day
    ## Post Cheer Mom Up
    elif mum_path == 17:
        pov "{i}She'll come out in her own time. I don't wanna push things.{/i}"
        call screen scr_myhallway_day
    ## Incest Porno with Mom
    elif mum_path == 22 and day == 4:
        jump lbl_incest_porno_with_mom
    ## Incest Porno Fail
    elif mum_path == 22.5:
        pov "{i}I'll give her some privacy for now.{/i}"
        if mum_points <= 7:
            if winc == 0:
                $ renpy.notify("You need 8 [missus] Relationship Points")
            else:
                $ renpy.notify("You need 8 Mom Relationship Points")
        else:
            pov "{i}I'll check back in another day.{/i}"
        jump lbl_myhallway_day_setup
    ## No Event
    else:
        jump lbl_parentsbedroom_day

###############
## Room Navigation
## This is the map for my parents's bedroom during the day
label lbl_parentsbedroom_day:

    scene bg parentsbedroom_day
    call screen scr_parentsbedroom_day

screen scr_parentsbedroom_day():

## Dad Absent
    ## Dad Living Room or Out
    if day <= 4 or gtime == 0:
        pass

    ## Dad Out of Town / Dad Kicked Out for Destroying Fort
    elif 20 <= mum_path <= 24 or 27 <= sister_path <= 36:
        pass

    ## Dad in the bedroom in the Afternoon Weekends
    elif gtime == 1 and day >= 5:
        imagebutton auto "btn parentsbedroom_day_dad_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_day_dad")

    ## Laptop - Fix Mom's Laptop
    if 2 <= mum_path <= 3.5 and not (gtime == 1 and day >= 5):
        imagebutton auto "btn parentsbedroom_day_laptop_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parentsbedroom_day_laptop")
    imagebutton auto "btn parentsbedroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")
    use hud_overlay

###############
## Labels
## Conversations
## Items
label lbl_parentsbedroom_day_laptop:
    if mum_path == 2:
        jump lbl_the_virus
    elif 3 <= mum_path <= 3.5:
        if mum_path == 3.5:
            if inventory.has_item(Items.antiviruscd):
                jump lbl_the_antivirus
            else:
                pov "{i}I know how to get rid of the virus now. I just have to buy the antivirus CD.{/i}"
        elif mum_path == 3:
            if inventory.has_item(Items.antiviruscd):
                pov "{i}I have the antivirus CD, I just need to figure out how to use it.{/i}"
            else:
                pov "{i}I have to buy the antivirus CD and I need to research online how to use it.{/i}"

        jump lbl_parentsbedroom_day
    elif 3 <= mum_path <= 3.5 and not inventory.has_item(Items.antiviruscd):
        if mum_path == 3.5:
            pov "{i}I will need to buy an antivirus CD and install it that way since the viruses are messing with the network settings.{/i}"

            jump lbl_parentsbedroom_day
        elif mum_path == 3:
            pov "{i}I will need to buy an antivirus CD and figure out how to use it...{/i}"

            jump lbl_parentsbedroom_day
