label lbl_mybedroom_chest_day:
    scene bg chest_day
    call screen scr_mybedroom_chest_day

screen scr_mybedroom_chest_day():
    imagebutton auto "btn chest_day_vrheadset_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_vrheadset_startup")
    imagebutton auto "btn chest_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_day")

label lbl_mybedroom_chest_night:
    scene bg chest_night
    call screen scr_mybedroom_chest_night

screen scr_mybedroom_chest_night():
    imagebutton auto "btn chest_night_vrheadset_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_vrheadset_startup")
    imagebutton auto "btn chest_night_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_night")