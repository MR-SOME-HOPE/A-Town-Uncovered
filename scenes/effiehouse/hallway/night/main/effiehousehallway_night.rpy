###############
## Setup
## Story Path
label lbl_effiehousehallway_night_setup:
    jump lbl_effiehousehallway_night

###############
## Room Navigation
## This is the map for effie hallway during the night
label lbl_effiehousehallway_night:

    scene bg effiehousehallway_night
    call screen scr_effiehousehallway_night

screen scr_effiehousehallway_night():
    imagebutton auto "btn effiehousehallway_night_frontdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehousehallway_night_frontdoor")
    imagebutton auto "btn effiehousehallway_night_garage_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehousehallway_night_garage")
    imagebutton auto "btn effiehousehallway_night_effieroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effieroom_night_setup")
    use hud_overlay

###############
## Labels
## Locations
label lbl_effiehousehallway_night_frontdoor:
    if main_story == 12:
        jump lbl_effie_house_hallway_night_frontdoor_presex
    else:
        jump lbl_effiehouseoutside_night_setup

label lbl_effiehousehallway_night_garage:
    jump lbl_effie_house_hallway_night_garage_presex
