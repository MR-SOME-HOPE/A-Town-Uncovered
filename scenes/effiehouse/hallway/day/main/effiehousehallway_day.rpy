###############
## Setup
## Story Path
label lbl_effiehousehallway_day_setup:
    jump lbl_effiehousehallway_day

###############
## Room Navigation
## This is the map for effie hallway during the day.
label lbl_effiehousehallway_day:

    scene bg effiehousehallway_day
    call screen scr_effiehousehallway_day

screen scr_effiehousehallway_day():
    imagebutton auto "btn effiehousehallway_day_frontdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehouseoutside_day_setup")
    imagebutton auto "btn effiehousehallway_day_garage_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehousehallway_day_garage")
    imagebutton auto "btn effiehousehallway_day_effieroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effieroom_day_setup")
    use hud_overlay

###############
## Labels
## Locations
label lbl_effiehousehallway_day_garage:
    pov "{i}I think I should listen to Effie and not go in there.{/i}"

    jump lbl_effiehousehallway_day_setup
