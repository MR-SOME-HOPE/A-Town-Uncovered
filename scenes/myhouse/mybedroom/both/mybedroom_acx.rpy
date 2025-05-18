## A City X-posed - My Favourite Game ##
label lbl_mybedroompc_acx:
    pov "{i}Alright... where am I up to- oh! Right the sex scene.{/i}"
    pov "{i}I have to make sure I don't cum inside her or else it's game over.{/i}"

label lbl_mybedroompc_acx_retry:
    call screen scr_desktop_acx_input
    if isinstance(_return, basestring):
        $ acx_answer = _return
    call screen scr_mybedroompc_acx

screen scr_mybedroompc_acx():
    add "img mybedroompc_acx" align (0.5,0.45)
    imagebutton auto "btn mybedroompc_acxwindow_%s" align (0.5,0.45) focus_mask True action Jump("lbl_mybedroompc_acx_result")
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 98 focus_mask True action Jump("lbl_mybedroom_desk_1")
    if acx_answer == "cum inside" or acx_answer == "cum":
        hbox xpos 200 ypos 700 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer == "don't cum inside" or acx_answer == "don't cum" or acx_answer == "dont cum inside" or acx_answer == "dont cum":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "You overestimated your self-control." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer == "pull out" or acx_answer == "pull dick out" or acx_answer == "pull penis out":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "She wraps her legs around you and locks you in." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer == "go slow" or acx_answer == "go slower":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "The feeling of going slow excentuates the sensation." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer == "go faster" or acx_answer == "go fast" or acx_answer == "go harder" or acx_answer == "go hard":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "You fucked her faster and harder." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer == "keep fucking" or acx_answer == "continue" or acx_answer == "keep going":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "You kept going." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer == "don't move" or acx_answer == "stop moving" or acx_answer == "stop" or acx_answer == "dont move":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "She rolls her body and grinds her hips against you." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer == "die":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "You died. Your muscles relaxed." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer.startswith("think"):
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "You tried thinking of anything but cumming inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer.startswith("say") or acx_answer == "talk":
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "The sound of your own breathy voice turned her on and she scratches your back." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer.startswith("look"):
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "The lack of sight in the darkness excentuates the physical sensation." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer.startswith("dance"):
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "You moved your body to the rhythm in your head." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer.startswith("kill") or acx_answer == "kill her" or acx_answer == "kill girl" or acx_answer.startswith("murder"):
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "You killed her. The adrenaline rushes over you." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer.startswith("tease") or acx_answer.startswith("rub") or acx_answer.startswith("grab") or acx_answer.startswith("kiss") or acx_answer.startswith("slap"):
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "She moaned. Her moan pierced your ears." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    elif acx_answer.startswith("shit"):
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "Without pulling out, you threw your pants on and shat in it." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "The exertion made you cum." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    else:
        hbox xpos 200 ypos 650 spacing 20:
            text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 700 spacing 20:
            text "Your actions were too confusing. Your body took over your mind." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 750 spacing 20:
            text "You came inside." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
        hbox xpos 200 ypos 800 spacing 20:
            text "Game Over." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"

label lbl_mybedroompc_acx_result:
    pov "Dammit, lemme reload and try again."

    jump lbl_mybedroompc_acx_retry

## A CITY XPOSED INPUT SCREEN

screen scr_desktop_acx_input():
    add "img mybedroompc_acx" align (0.5,0.45)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 98 focus_mask True action Jump("lbl_mybedroom_desk_1")
    hbox xpos 200 ypos 800 spacing 20:
        text "..LOADED SAVE #36 - Don't Cum Inside.." color "eeebeb" size 38 font "fonts/KGSorryNotSorryChub.ttf"
    window:
        style "nvl_window"
        input id "input" xpos 200 ypos 840 exclude "QWERTYUIOPASDFGHJKLZXCVBNM"
    use quick_menu
