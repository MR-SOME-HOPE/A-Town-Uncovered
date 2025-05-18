## Bedroom Desk/PC ##
label lbl_mybedroom_desk:
    scene bg mybedroompc1
    with fade

label lbl_mybedroom_desk_1:

    scene bg mybedroompc1
    call screen scr_mybedroompc

screen scr_mybedroompc():
    ## If Steam Version (b)
    imagebutton auto "btn mybedroompc_changelog_%s" xpos 95 ypos 531 focus_mask True action Jump("lbl_mybedroompc_changelog")
    imagebutton auto "btn mybedroompc_counters_%s" xpos 102 ypos 681 focus_mask True action Jump("lbl_mybedroompc_counters")
    imagebutton auto "btn mybedroompc_hscenexray_%s" xpos 108 ypos 832 focus_mask True action Jump("lbl_mybedroompc_xray")
    imagebutton auto "btn mybedroompc_acx_%s" xpos 260 ypos 69 focus_mask True action Jump("lbl_mybedroompc_acx")
    imagebutton auto "btn mybedroompc_bugs_%s" xpos 269 ypos 228 focus_mask True action OpenURL("https://goo.gl/forms/BwjturN2K0nYwl0O2")
    imagebutton auto "btn mybedroompc_camgurl_%s" xpos 268 ypos 385 focus_mask True action Jump("lbl_mybedroompc_camgurl")
    imagebutton auto "btn mybedroompc_foridiots_%s" xpos 263 ypos 537 focus_mask True action Jump("lbl_mybedroompc_foridiots")
    imagebutton auto "btn mybedroompc_sugarservice_%s" xpos 253 yalign 0.7049 focus_mask True action Jump("lbl_mybedroompc_sugarservice")
    imagebutton auto "btn mybedroompc_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_exit")

    ## If Patreon Version (a)
    # imagebutton auto "btn mybedroompc_trash_%s" xpos 100 ypos 75 focus_mask True action Jump("lbl_mybedroompc_trash")
    # imagebutton auto "btn mybedroompc_cheatcode_%s" xpos 100 ypos 233 focus_mask True action Jump("lbl_mybedroompc_cheatcode")
    # imagebutton auto "btn mybedroompc_gallery_%s" xpos 81 ypos 378 focus_mask True action Jump("lbl_mybedroompc_gallery")
    # imagebutton auto "btn mybedroompc_changelog_%s" xpos 95 ypos 531 focus_mask True action Jump("lbl_mybedroompc_changelog")
    # imagebutton auto "btn mybedroompc_counters_%s" xpos 102 ypos 681 focus_mask True action Jump("lbl_mybedroompc_counters")
    # imagebutton auto "btn mybedroompc_hscenexray_%s" xpos 108 ypos 832 focus_mask True action Jump("lbl_mybedroompc_xray")
    # imagebutton auto "btn mybedroompc_acx_%s" xpos 260 ypos 69 focus_mask True action Jump("lbl_mybedroompc_acx")
    # imagebutton auto "btn mybedroompc_bugs_%s" xpos 269 ypos 228 focus_mask True action OpenURL("https://goo.gl/forms/BwjturN2K0nYwl0O2")
    # imagebutton auto "btn mybedroompc_camgurl_%s" xpos 268 ypos 385 focus_mask True action Jump("lbl_mybedroompc_camgurl")
    # imagebutton auto "btn mybedroompc_foridiots_%s" xpos 263 ypos 537 focus_mask True action Jump("lbl_mybedroompc_foridiots")
    # imagebutton auto "btn mybedroompc_timetravel_%s" xpos 259 ypos 683 focus_mask True action Jump("lbl_mybedroompc_timetravel")
    # imagebutton auto "btn mybedroompc_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_exit")
    # imagebutton auto "btn mybedroompc_sugarservice_%s" xpos 257 ypos 842 focus_mask True action Jump("lbl_mybedroompc_sugarservice")

    

## Trash Bin - Old Art Assets and Screenshots
label lbl_mybedroompc_trash:
    # show img inconstruction # Fixed
    with hpunch
    $ renpy.pause()

    jump lbl_mybedroom_desk_1

## Cheatcode - $7+ Patron Cheats
## Cheat_on == 0 is OFF but toggleable
## Cheat_on == 1 is ON and toggleable
## Cheat_on == 2 is UNAVAILABLE and NEEDS CODE
## Cheat_on == 3 is UNAVAILABLE but DOESN'T NEED CODE
label lbl_mybedroompc_cheatcode:
    ## Check to see if ch3@t$ are on
    # python:
    if renpy.exists('steamver321.rpy'):
        call lbl_steamver321
    else:
        pass

    if cheat_on <= 1:
        call screen scr_mybedroompc_cheatcode_toggle
    else:
        call screen scr_desktop_cheatcode_input
        if isinstance(_return, basestring):
            $ player_try = _return
        $ secret_code = ("thankyousm")
        if player_try == secret_code:
            $ cheat_on = 1
            call screen scr_mybedroompc_cheatcode_toggle
        elif not player_try:
            "Nothing entered."
        else:
            "Wrong code."

        jump lbl_mybedroom_desk_1

screen scr_mybedroompc_cheatcode_toggle():
    add "img mybedroompc_togglewindow" align (0.5,0.407)
    hbox align (0.5,0.2) spacing 20:
        text "TOGGLE CHEATS" color "201f1f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    if cheat_on == 0:
        add "img mybedroompc_togglewindow_cheatsoff" align (0.5,0.675)
        imagebutton auto "btn mybedroompc_toggleoff_%s" align (0.5,0.32) focus_mask True action SetVariable("cheat_on", 1)
    else:
        add "img mybedroompc_togglewindow_cheatson" align (0.5,0.675)
        imagebutton auto "btn mybedroompc_toggleon_%s" align (0.5,0.32) focus_mask True action SetVariable("cheat_on", 0)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1205 ypos 135 focus_mask True action Jump("lbl_mybedroom_desk_1")

## Photo Gallery - Fan art
label lbl_mybedroompc_gallery:
    # show img inconstruction # Fixed
    with hpunch
    $ renpy.pause()

    jump lbl_mybedroom_desk_1

## Counters - Toggle Counters
label lbl_mybedroompc_counters:
    call screen scr_mybedroompc_counters_toggle

screen scr_mybedroompc_counters_toggle():
    add "img mybedroompc_togglewindow" align (0.5,0.407)
    hbox align (0.5,0.2) spacing 20:
        text "TOGGLE COUNTERS" color "201f1f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    if store_counter == 0:
        add "img mybedroompc_togglewindow_countersoff" align (0.5,0.675)
        imagebutton auto "btn mybedroompc_toggleoff_%s" align (0.5,0.32) focus_mask True action SetVariable("store_counter", 1)
    else:
        add "img mybedroompc_togglewindow_counterson" align (0.5,0.675)
        imagebutton auto "btn mybedroompc_toggleon_%s" align (0.5,0.32) focus_mask True action SetVariable("store_counter", 0)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1205 ypos 135 focus_mask True action Jump("lbl_mybedroom_desk_1")

## Xrays - Toggle Xrays
label lbl_mybedroompc_xray:
    call screen scr_mybedroompc_xray_toggle

screen scr_mybedroompc_xray_toggle():
    add "img mybedroompc_togglewindow" align (0.5,0.407)
    hbox align (0.5,0.2) spacing 20:
        text "TOGGLE XRAY" color "201f1f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    if hscene_xray == 0:
        add "img mybedroompc_togglewindow_xrayoff" align (0.5,0.675)
        imagebutton auto "btn mybedroompc_toggleoff_%s" align (0.5,0.32) focus_mask True action SetVariable("hscene_xray", 1)
    else:
        add "img mybedroompc_togglewindow_xrayon" align (0.5,0.675)
        imagebutton auto "btn mybedroompc_toggleon_%s" align (0.5,0.32) focus_mask True action SetVariable("hscene_xray", 0)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1205 ypos 135 focus_mask True action Jump("lbl_mybedroom_desk_1")

##Report a Bug - Bug Reporter
#Opens the Bug Report URL

## Camgurl.com - Access Sister's Camgurl Page
label lbl_mybedroompc_camgurl:
    if sister_path <= 4:
        pov "{i}Checked out a few cam girls on here a while ago. Apparently the site requires a membership fee.{/i}"
        pov "{i}Pretty lame if you ask me. Why should I pay someone to have them entertain me?{/i}"
        pov "{i}People should do things for free and for the passion.{/i}"

        jump lbl_mybedroom_desk_1
    else:
        jump lbl_camgurl_stream

## TimeTravel.exe - Skip a Chapter or Manually Enter one (Bug Testing Fail Safe)
label lbl_mybedroompc_timetravel:
    jump lbl_bug_testing_fail_safe

## Sugar Service Trailer:
label lbl_mybedroompc_sugarservice:
    stop music
    show black:
        alpha 0.7
    show sugarservicetrailer:
        xalign 0.5
        yalign 0.35
    $ renpy.pause(61,hard=False)
    hide sugarservicetrailer

    play music "audio/music/a_family_home.ogg"

    # "Dev" "Hi, this is GeeSeki, creator and developer of A Town Uncovered."
    # "Dev" "Sugar Service is my new 'big' game that I'm currently focused on."
    # "Dev" "It's a project that I have a ton of passion and creative motivation for."
    # "Dev" "It is the game that I wish A Town Uncovered could have been if I had the same game-dev knowledge and experience I have now but almost a decade ago."
    # "Dev" "You can call it a love letter or a big brother to A Town Uncovered and I just know that if you love ATU, you'll DEFINITELY love Sugar Service way more."
    # "Dev" "Give it a shot and let me know what you think, I would greatly appreciate it."
    menu:
        "Do you want to try this new game?"
        "Take me to the website!":
            $ open_url()
        "No, thanks. Not right now.":
            pass

    jump lbl_mybedroom_desk_1

## Exit
label lbl_mybedroompc_exit:
    if gtime <= 1:
        scene bg mybedroom_day
        with fade

        jump lbl_mybedroom_day_setup
    else:
        scene bg mybedroom_night
        with fade

        jump lbl_mybedroom_night_setup

## CHEATCODE INPUT SCREEN
screen scr_desktop_cheatcode_input():
    window:
        style "nvl_window"
        add "img mybedroompc_cheatinputwindow" align (0.5,0.447)
        input id "input" xalign 0.5 yalign 0.5 length 14
        imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1115 ypos 371 focus_mask True action Jump("lbl_mybedroom_desk_1")
    use quick_menu

###############################################################
label lbl_mybedroom_desk_2:

    menu:
        "Enable/Disable...":
            "Hello"
        #"Get Skill Item":
        #    menu:
        #        "Skill Item 1":
        #            $ inventory.buy(Items.skillitem1)
        #        "Skill Item 2":
        #            $ inventory.buy(Items.skillitem2)
        #        "Skill Item 3":
        #            $ inventory.buy(Items.skillitem3)
        #        "Skill Item 4":
        #            $ inventory.buy(Items.skillitem4)
        #        "Skill Item 5":
        #            $ inventory.buy(Items.skillitem5)
        #        "Skill Item 6":
        #            $ inventory.buy(Items.skillitem6)
        #        "Skill Item 7":
        #            $ inventory.buy(Items.skillitem7)
        #        "Skill Item 8":
        #            $ inventory.buy(Items.skillitem8)
        #        "Skill Item 9":
        #            $ inventory.buy(Items.skillitem9)
        #        "Skill Item 10":
        #            $ inventory.buy(Items.skillitem10)
        "Nothing":
            pass

    jump lbl_mybedroom_desk


#####################################################################
## IMAGES
image btn mybedroompc_sugarservice_idle:
    "scenes/myhouse/mybedroom/both/assets/button/btn_mybedroompc_sugarservice_idle.png"

image btn mybedroompc_sugarservice_hover = im.MatrixColor(
    "scenes/myhouse/mybedroom/both/assets/button/btn_mybedroompc_sugarservice_idle.png",
    im.matrix.brightness(0.2)*
    im.matrix.opacity(1.0))
