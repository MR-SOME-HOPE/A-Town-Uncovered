## Throwaway Chat with Brock ##
label lbl_cafeinside_day_brock:
    if brock_path == 0:
        jump lbl_cafeinside_day_brock_idk
    if brock_path >= 1:
        if gtime == 0:
            jump lbl_cafeinside_day_brock_0
        elif gtime == 1:
            jump lbl_cafeinside_day_brock_morningshift

label lbl_cafeinside_day_brock_idk:
    show pov neutral at left
    with dissolve
    show brow neutral_talk at right
    call lbl_cafeinside_counter_check
    with dissolve

    idk "Hey, bro. What can I get for you today?"
    menu:
        "Where's Effie?":
            jump lbl_cafeinside_day_brock_whereseffie
        "I've seen you at the fight club before." if jack_path >= 2:
            jump lbl_cafeinside_day_brock_seenatclub
        "Office Coffee Orders" if on_coffee_run_blocking and not bought_coffee_run_drinks:
            jump lbl_get_coffee_from_cafe

label lbl_cafeinside_day_brock_0:
    show pov neutral at left
    with dissolve
    show brow neutral_talk at right
    call lbl_cafeinside_counter_check
    with dissolve

    bro "Hey, bro. What can I get for you today?"
    menu:
        "Where's Effie?":
            jump lbl_cafeinside_day_brock_whereseffie
        "Spare Boxes?" if sister_path == 29 and cafeinside_spareboxes == 0:
            jump lbl_cafeinside_day_brock_spareboxes
        "Office Coffee Orders" if on_coffee_run_blocking and not bought_coffee_run_drinks:
            jump lbl_get_coffee_from_cafe
