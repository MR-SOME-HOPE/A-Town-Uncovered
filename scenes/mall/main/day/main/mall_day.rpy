###############
## Setup
## Story Path
label lbl_mall_day_setup:
    ## First Day of School
    if main_story <= 5:
        pov "{i}I can't go there yet. I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In Trouble By Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## Sexworld
    elif insexworld == 1 and main_story == 33:
        jump lbl_mall_day
    ## Mall with Friends
    elif main_story == 76:
        jump lbl_mall_with_friends
    # ## Followers of Master Buukakki
    # elif main_story == 146:
    #     jump lbl_followers_of_master_buukakki
    # ## Buukakki Followers Are Everywhere
    # elif main_story == 151 and buukakkifollowers_flyer == 0:
    #     jump lbl_buukakki_followers_are_everywhere
    ## NO EVENT
    else:
        ## Effie Off Duty
        if day >= 5 and gtime == 0:
            if 12 <= date <= 15 and randomencounter == 0:
                $ randomencounter = 1
                scene bg mall_day
                jump lbl_randomevent_mall_effie_1
        else:
            jump lbl_mall_day

###############
## Room Navigation
## This is the map for mall during the day
label lbl_mall_day:
    if insexworld == 1 and main_story <= 35:
        scene bg mall_daysexworld
        if gtime == 1:
            show btn_mall_day_meghansexworld_idle2
            show btn_mall_day_teghansexworld_idle2
            show btn_mall_day_chieghansexworld_idle2
            show btn mall_daysexworld_icecreamstore_idle
    else:
        scene bg mall_day
        if (16 <= main_story <= 21) and grundlesam_path == 0:
            show btn mall_day_icecreamstorebeback_idle
        if gtime == 1:
            show btn_mall_day_meghan_idle2
            show btn_mall_day_teghan_idle2
            show btn_mall_day_chieghan_idle2
    call screen scr_mall_day

screen scr_mall_day():
    if main_story == 84:
        imagebutton auto "btn mall_day_meghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_investigations_eghans")
        imagebutton auto "btn mall_day_teghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_investigations_eghans")
        imagebutton auto "btn mall_day_chieghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_investigations_eghans")
    elif gtime == 1:
        if insexworld == 1 and main_story <= 35:
            imagebutton auto "btn mall_day_meghansexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_sexworld_meghan")
            imagebutton auto "btn mall_day_teghansexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_sexworld_teghan")
            imagebutton auto "btn mall_day_chieghansexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_sexworld_chieghan")
        else:
            if main_story >= 12 and (meghan_path >=1 and teghan_path >=1 and chieghan_path >=1):
                imagebutton auto "btn mall_day_meghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_meghan")
                imagebutton auto "btn mall_day_teghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_teghan")
                imagebutton auto "btn mall_day_chieghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_chieghan")
            else:
                pass
    imagebutton auto "btn mall_day_stuffstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_stuffstore_day_setup")
    imagebutton auto "btn mall_day_mallstores_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_day_setup")
    if insexworld == 0:
        if (16 <= main_story <= 21) and grundlesam_path == 0:
            imagebutton auto "btn mall_day_icecreamstorebeback_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_be_back_in_fifteen")
        else:
            imagebutton auto "btn mall_day_icecreamstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_alanna")
    else:
        imagebutton auto "btn mall_daysexworld_icecreamstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_alanna")
    imagebutton auto "btn mall_day_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup")
    use hud_overlay

###############
## Labels
## Throwaway Chat
label lbl_mall_day_sexworld_meghan:
    $ nyi()
    #hide btn_mall_day_meghansexworld_idle2#TODO
    jump lbl_mall_day

label lbl_mall_day_sexworld_teghan:
    $ nyi()
    #hide btn_mall_day_teghansexworld_idle2#TODO
    jump lbl_mall_day


label lbl_mall_day_sexworld_chieghan:
    $ nyi()
    #hide btn_mall_day_chieghansexworld_idle2#TODO
    jump lbl_mall_day



## Ice Cream'py Counter
label lbl_icecreampy_counter_check:
    if store_counter == 1:
        show counter icecreampy at right
        with dissolve
    else:
        pass
    return
