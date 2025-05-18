label lbl_newspaper_day:
    scene bg newspaper_1
    call screen scr_newspaper

screen scr_newspaper():
    imagebutton auto "btn newspaper_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhousefront_day")
