﻿################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True
    font "fonts/KGSorryNotSorryChub.ttf"

style correction_text:
    color '#000000'
    size 24
    hover_color '#000000'
    underline False
    hover_underline False
    font "fonts/KGSorryNotSorryChub.ttf"


style gui_text:
    #font gui.interface_font
    font "fonts/KGSorryNotSorryChub.ttf"
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    # If there's a side image, display it above the text. Do not display
    # on the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image(im.Alpha("gui/gui_textbox.png", 0.85, xalign=0.5, yalign=0.8))

style window_narr:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image(im.Alpha("gui/gui_textbox.png", 0.85, xalign=0.5, yalign=0.8))

style input_window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image(im.Alpha("gui/gui_textbox.png", 0.85, xalign=0.5, yalign=0.8))

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    # xsize 300
    # ypos -0.225
    # ysize 60
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font "fonts/KGSorryNotSorryChub.ttf"
    size gui.name_text_size
    xalign 0.2
    yalign 0.5

style say_dialogue:
    color "2c2b2b"
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

#screen input(prompt):
#    style_prefix "input"
#
#    window:
#
#        vbox:
#            xpos gui.text_xpos
#            xanchor gui.text_xalign
#            ypos gui.text_ypos
#
#            text prompt style "input_prompt"
#            input id "input"

screen input(prompt, someText = ""):

    window:

        style "nvl_window"

        text prompt xalign 0.5 yalign 0.44
        input id "input" xalign 0.5 yalign 0.5

    use quick_menu

style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    #vbox:
    #    for i in items:
    #        textbutton i.caption action i.action
    #vbox:
    #    for i in items:
    #        if i.action:
    #            if " (disabled)" in i.caption:
    #                textbutton i.caption.replace(" (disabled)", "")
    #            else:
    #                textbutton i.caption action i.action
    #        else:
    #            textbutton i.caption
    #style_prefix "menu_choice_button"
    vbox:
        for i in items:

            if " (disabled)" in i.caption:
                textbutton i.caption.replace(" (disabled)", "") action None # style menu_choice
            else:
                textbutton i.caption action i.action
        spacing 10


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    # Add an in-game quick menu.
    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("History") action ShowMenu('history')
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    font "fonts/KGSorryNotSorryChub.ttf"

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font "fonts/KGSorryNotSorryChub.ttf"


################################################################################
# Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Controls") action ShowMenu("help")

        textbutton _("Credits") action ShowMenu("about")

        #textbutton _("Website") action OpenURL("https://www.atownuncovered.com/")

        textbutton _("Report a Bug") action OpenURL("https://goo.gl/forms/BwjturN2K0nYwl0O2")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android.
            #textbutton _("Quit") action Quit(confirm=not main_menu)
#######################################################################################
            textbutton _("Quit") action Show("quitconfirmscreen")


#######################################################################################
## Screen Version
screen scr_version():
    if main_menu:
        vbox:
            xalign 0.05 yalign 0.98
            text "[config.version]" xalign 0.0 yalign 0.0 color "#FFFFFF" size 50 font "fonts/KGSorryNotSorryChub.ttf"

# CROSS PROMOTE
# screen scr_crosspromote():
#     if main_menu:
#         ## DETECTED AFTER DARK
#         add "img detectedad_background" xalign 0.98 yalign 0.05
#         vbox:
#             xalign 1.0 yalign 0.1
#             text "Try Our New Game for FREE!" xalign 0.5 yalign 0.0 color "#151616" size 44 font "fonts/KGSorryNotSorryChub.ttf"
#             imagebutton auto "btn detectedad_%s" xalign 1.0 yalign 0.0 focus_mask True action OpenURL("https://www.patreon.com/GeeSekiVN")

## DETECTED AFTER DARK BTN
image btn detectedad_idle:
    "assets/crosspromote/img_detectedad_promote_2.jpg"
    pause 1.0
    "assets/crosspromote/img_detectedad_promote_3.jpg"
    pause 1.0
    "assets/crosspromote/img_detectedad_promote_4.jpg"
    pause 1.0
    "assets/crosspromote/img_detectedad_promote_5.jpg"
    pause 1.0
    "assets/crosspromote/img_detectedad_promote_6.jpg"
    pause 1.0
    repeat

image btn detectedad_hover:
    "assets/crosspromote/img_detectedad_promote_1.jpg"

image img detectedad_background = im.MatrixColor(
    "assets/crosspromote/img_detectedad_promote_1.jpg",
    im.matrix.brightness(1.0)*
    im.matrix.opacity(1))

#label quitconfirm:
    #call screen quitconfirmscreen

screen quitconfirmscreen():
    modal True

    add "bg quitmenu"
    add "img specialthanksbox"
    vbox xpos 40 ypos 265 spacing -5: ##1920x1080
        text "-dav" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-kidd" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-non" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-cole" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-dx88" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-stdk" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-mdge" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-ukph" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-andy" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-maru" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-selix" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-fares" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-rob c" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-xana" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-chris" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-hefty" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 125 ypos 265 spacing -5: ##1920x1080

        text "-Mydus" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-tadhg" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-epmrc" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-darkd" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-matty" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-smaug" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-albert" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-what?" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-chisps" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-castor" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Sampix" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-nekoli" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-gray85" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-mcleod" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Askard" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-seraph" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 225 ypos 265 spacing -5: ##1920x1080
        text "-misery" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf" # Alpha 0.49
        text "-bustin" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-kakuga" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-joseph" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-sfnc45" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-boof57" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Z Payne" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-lagoon" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-w00lly" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jakaa9" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-tarakis" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-itiipau" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-valen s." color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-cipheos" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-rohoma" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-neolust" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 335 ypos 265 spacing -5: ##1920x1080
        text "-zurakci" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Xalibur" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-evillak" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-xix xhix" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-roseguy" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-burnsey" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-DrNearo" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-nacario" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-mrmelon" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-itchiesr" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Nemo032" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-wes8226" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-allen ray" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-lancer86" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-willtero" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-koroshi1" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 460 ypos 265 spacing -5: ##1920x1080
        text "-toneds80" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-joepanda" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-desertfox" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-logbuilul" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-annier34" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jonny lee" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Saulatear" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-dusti_333" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-kidd video" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-confuddle" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-cereal yum" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-houa yang" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-epictoasta" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-samwitch" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jkornacki" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-kindering" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 600 ypos 265 spacing -5: ##1920x1080
        text "-spiderdadd" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-driftdevil" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-darkseid98" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-roninaura" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-frostiorca" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-garlendolf" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf" # Alpha 0.49
        text "-devastator." color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-dunhill542" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-rickyrich98" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-mazterlith" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-carter otto" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-racalan942" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-370hssv123" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-slayerfreak" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Omni Omega" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-og_hazarrd" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 750 ypos 265 spacing -5: ##1920x1080
        text "-purple flare" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Gdogger777" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-CruelKairos" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-giantbacon" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-WallEWorld" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-darththorn" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-kingu korin" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-tigerknight" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-cheesemasta" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-austin yang" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-the_spegget" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-alex patreon" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-john myer jr" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-YandereKxng" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-theguardian" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-masterglitch" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 915 ypos 265 spacing -5: ##1920x1080
        text "-seymour nuts" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-travis bowen" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Devon Ramsey" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-coldbluecrow" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Fenryl Saylem" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-acosmicotaku" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-zacefronfan3" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Soulfulcobalt" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-GamerNerd247" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Fabulous Aura" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-eric bollacker" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-zach johnson" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-dark wanderer" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-sural argonis" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-george's chins" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jae hyung park" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        

    vbox xpos 1100 ypos 265 spacing -5: ##1920x1080
        text "-moviebuff3000" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jeff 'gray fox' s." color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-distinktknopf" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-aldo longdong" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Tahxickannoli" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jessica nohava" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-grimm kurosaki" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Cthulhuplays21" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-trucker_guy257" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-harry fukogawa" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-masterkenobi43" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jayden sherman" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Nightingale172" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-jairo palomares" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 1305 ypos 265 spacing -5: ##1920x1080
        
        text "-hallowed_ghost" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-crimsondeath45" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-gabriel withers" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-whiskey-fanatic" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-biohazard victim" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-nightpopcorn456" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Andrew J Pollara" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-blackmageshadow" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Mikeplayz Studios" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-shadow lockheart" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-thelastatalntian" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    vbox xpos 1545 ypos 265 spacing -5: ##1920x1080
        
        text "-MasteringTheBlaze" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-AzTheDemonIntern" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-therealriasgremory" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-dillion washington" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-Georges Big Ol' Chins" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-thekillercreamcheese" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-bruno thought leader" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"
        text "-bigbootydongerbanger" color "#ece5e2" size 26 font "fonts/KGSorryNotSorryChub.ttf"

    imagebutton auto "btn quitmenu_yes_%s" xpos 0 ypos 0 focus_mask True action Quit(False)
    imagebutton auto "btn quitmenu_no_%s" xpos 0 ypos 0 focus_mask True action Hide("quitconfirmscreen")

########################################################################################

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    font "fonts/KGSorryNotSorryChub.ttf"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    font "fonts/KGSorryNotSorryChub.ttf"
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    # This empty frame darkens the main menu.
    frame:
        pass
    imagemap:
        alpha True
        ground  "new_ui/title_idle.png"
        hover "new_ui/title_hover.png"


        hotspot (35, 225, 80, 75) action Start()            #start
        hotspot (35, 315, 80, 75) action ShowMenu("load")   #load
        hotspot (35, 410, 80, 75) action ShowMenu("preferences") #pref
        hotspot (35, 500, 80, 75) action ShowMenu("help") #controls
        hotspot (35, 595, 80, 75) action ShowMenu("about") #credits
        hotspot (35, 685, 80, 75) action OpenURL("https://goo.gl/forms/BwjturN2K0nYwl0O2") #report_a_bug
        hotspot (35, 780, 80, 75) action If( renpy.variant("pc"), Show("quitconfirmscreen"), NullAction() ) #quit

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    use scr_version

    # use scr_crosspromote

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background renpy.random.choice(["bg atu_school", "bg atu_nightclub", "bg atu_cards", "bg atu_cinema", "bg atu_park", "bg atu_beach"])

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When this
## screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    add gui.main_menu_background

    # Add the backgrounds.
    if main_menu:
        add gui.main_menu_background
    elif title == "Load":
        add gui.load_menu_background
    elif title == "Save":
        add gui.save_menu_background
    elif title == "preferences":
        add gui.settings_menu_background
    elif title == "help":
        add gui.controls_menu_background
    elif title == "about":
        add gui.credits_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            # Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background renpy.random.choice(["bg atu_school_0", "bg atu_nightclub_0", "bg atu_cards_0", "bg atu_cinema_0", "bg atu_park_0", "bg atu_beach_0"]) #"gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -150


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    if main_menu:
        add renpy.random.choice(["bg atu_school_0", "bg atu_nightclub_0", "bg atu_cards_0", "bg atu_cinema_0", "bg atu_park_0", "bg atu_beach_0"])

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    #use game_menu(_("Credits"), scroll="viewport"):

    imagemap:
        add gui.credits_menu_background
        ground "new_ui/nav_idle.png"
        hover "new_ui/nav_hover.png"

        add "new_ui/nav_setn_perm.png"


        hotspot (1210, 150, 85, 85) action ShowMenu("save")#save
        hotspot (1315, 150, 85, 85) action ShowMenu("load")#load
        hotspot (1520, 150, 85, 85) action MainMenu()
        hotspot (1625, 150, 85, 85) action If( renpy.variant("pc"), Show("quitconfirmscreen"), NullAction() ) #quit
        hotspot (205, 150, 85, 85) action Return()#back

        if main_menu:
            add "new_ui/nav_main_menu_block.png"

        viewport:
            style_prefix "about"
            area (400, 270, 1300, 660)
            scrollbars "vertical"
            mousewheel True
            draggable True

            # side_yfill True

            vbox:

                text _("-A TEAM UNCOVERED-\n") xalign 0.5 color "344b68"

                text _("Lead Artist, Creator, and Director by GeeSeki\n") color "344b68"

                text _("Lead Writer by Robert Hawkins\n") color "344b68"

                text _("QA Testing, Technical Programming by DarkMage\n") color "344b68"

                text _("Story Programming by Wabeesabi\n") color "344b68"

                text _("Music by Marek Domagala\n") color "344b68"

                text _("-PREVIOUS CONTRIBUTORS-\n") xalign 0.5 color "344b68"

                text _("Music by Fealow\n") color "344b68"

                text _("Coding Structure by Cipheos\n") color "344b68"

                text _("CG Art Assistance by Smear\n") color "344b68"

                text _("Scene/Sprite Posing and Programming by Epadder\n") color "344b68"

                text _("Dialogue Conversion by MorahZamora\n") color "344b68"

                text _("Background Art Assistance by Dexter\n") color "344b68"

                text _("CG Scene Art Assistance by Rivinca\n") color "344b68"

                text _("-----------------------------------\n") xalign 0.5 color "344b68"

                label "[config.name!t]"
                text _("Version [config.version!t]\n") color "344b68"

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n" color "344b68"

                #text _("Android Porting and Coding Help by {a=https://patreon.com/booom313}Booom313{/a}\n")

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") color "344b68"


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    if main_menu:
        add renpy.random.choice(["bg atu_school_0", "bg atu_nightclub_0", "bg atu_cards_0", "bg atu_cinema_0", "bg atu_park_0", "bg atu_beach_0"])

    use file_slots(_("Save"))


screen load():

    tag menu

    if main_menu:
        add renpy.random.choice(["bg atu_school_0", "bg atu_nightclub_0", "bg atu_cards_0", "bg atu_cinema_0", "bg atu_park_0", "bg atu_beach_0"])

    use file_slots(_("Load"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue()
    if title == "Load":
        add gui.load_menu_background
    elif title == "Save":
        add gui.save_menu_background

    add "new_ui/saveload_ground.png"
    if renpy.variant("pc"):
        text "*To delete a save, hover your mouse over the slot and press [[DEL] on your keyboard" xalign 0.22 yalign 0.904 font "fonts/KGSorryNotSorryChub.ttf"
    # text "Dev Note: Due to the new UI, old save file thumbnails may look disproportioned. They can be fixed by overwriting them." xalign 0.28 yalign 0.95 font "fonts/KGSorryNotSorryChub.ttf"

    imagemap:
        ground "new_ui/nav_idle.png"
        hover "new_ui/nav_hover.png"
        if title == "Save":
            add "new_ui/nav_save_perm.png"
        else:
            hotspot (1210, 150, 85, 85) action ShowMenu("save")#save
        if title == "Load":
            add "new_ui/nav_load_perm.png"
        else:
            hotspot (1315, 150, 85, 85) action ShowMenu("load")#load

        hotspot (1420, 150, 85, 85) action ShowMenu("preferences")#preferences

        hotspot (1520, 150, 85, 85) action MainMenu()

        hotspot (1625, 150, 85, 85) action If( renpy.variant("pc"), Show("quitconfirmscreen"), NullAction() ) #quit



        hotspot (205, 150, 85, 85) action Return()#back

        if main_menu:
            add "new_ui/nav_main_menu_block.png"


            #imagebutton:
            #    idle "new_ui/confirm_button_yes_idle.png"
            #    hover "new_ui/confirm_button_yes_hover.png"
            #    focus_mask True
            #    action yes_action

    #use navigation
    imagemap:
        alpha True
        idle "new_ui/SaveLoadbar_4.png"
        hover "new_ui/SaveLoadbar_2.png"
        #if config.has_quicksave:
        hotspot (455, 865 , 80, 30) action FilePage("quick") #Q
        #if config.has_autosave:
        hotspot (580, 865 , 80, 30) action FilePage("auto") #A #Hide("player_phone") activate_sound "sounds/se_phonelocked.ogg"
        hotspot (685, 850 , 55, 60) action FilePagePrevious() #PREV
        hotspot (785, 865, 40, 30) action FilePage(1) #1
        hotspot (855, 865, 40, 30) action FilePage(2) #2
        hotspot (920, 865, 40, 30) action FilePage(3) #3
        hotspot (985, 865, 40, 30) action FilePage(4) #4
        hotspot (1060, 865, 40, 30) action FilePage(5) #5
        hotspot (1125, 865, 40, 30) action FilePage(6) #6
        hotspot (1195, 865, 40, 30) action FilePage(7) #7
        hotspot (1260, 865, 40, 30) action FilePage(8) #8
        hotspot (1325, 865, 40, 30) action FilePage(9) #9
        hotspot (1400, 850, 55, 60) action FilePageNext() #NEXT
#    use game_menu(title):

        fixed:

            # ## This ensures the input will get the enter event before any of the
            # ## buttons do.
            # order_reverse True
            #
            # # The page name, which can be edited by clicking on a button.
            # button:
            #     style "page_label"
            #
            #     key_events True
            #     xalign 0.5
            #     action page_name_value.Toggle()
            #
            #     input:
            #         style "page_label_text"
            #         value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.48

                xspacing 38
                yspacing 5
                # spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot)
                        xalign 0.50
                        yalign 0.56

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
#            hbox:
#                style_prefix "page"

#                xalign 0.5
#                yalign 1.0

#                spacing gui.page_spacing

#                textbutton _("<") action FilePagePrevious()

#                textbutton _("{#auto_page}A") action FilePage("auto")

#                textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
#                for page in range(1, 10):
#                    textbutton "[page]" action FilePage(page)

#                textbutton _(">") action FilePageNext()



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    font "fonts/KGSorryNotSorryChub.ttf"
    size 50

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    font "fonts/KGSorryNotSorryChub.ttf"
    size 22
    xalign 0.5
    ypos 20


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if main_menu:
        add renpy.random.choice(["bg atu_school_0", "bg atu_nightclub_0", "bg atu_cards_0", "bg atu_cinema_0", "bg atu_park_0", "bg atu_beach_0"])

    #use navigation

    imagemap:
        add gui.settings_menu_background
        ground "new_ui/nav_idle.png"
        hover "new_ui/nav_hover.png"

        add "new_ui/nav_setn_perm.png"


        hotspot (1210, 150, 85, 85) action ShowMenu("save")#save
        hotspot (1315, 150, 85, 85) action ShowMenu("load")#load
        hotspot (1520, 150, 85, 85) action MainMenu()
        hotspot (1625, 150, 85, 85) action If( renpy.variant("pc"), Show("quitconfirmscreen"), NullAction() ) #quit
        hotspot (205, 150, 85, 85) action Return()#back

        if main_menu:
            add "new_ui/nav_main_menu_block.png"

        imagebutton:
            idle "new_ui/settings_display_fullscreen_idle.png"
            selected_idle "new_ui/settings_display_fullscreen_selected.png"
            selected_hover "new_ui/settings_display_fullscreen_selected.png"
            hover "new_ui/settings_display_fullscreen_hover.png"
            focus_mask True
            action Preference("display", "fullscreen")
            selected preferences.fullscreen
        imagebutton:
            idle "new_ui/settings_display_windowed_idle.png"
            selected_idle "new_ui/settings_display_windowed_selected.png"
            selected_hover "new_ui/settings_display_windowed_selected.png"
            hover "new_ui/settings_display_windowed_hover.png"
            focus_mask True
            action Preference("display", "window")
            selected not preferences.fullscreen
            #action [SelectedIf( InvertSelected(Preference('display', 'fullscreen')) ), Preference('display', 'window')]
            #action Preference("rollback side", "left")


            #action Preference("rollback side", "disable")
            #                    textbutton _("Left") action Preference("rollback side", "left")
            #                    textbutton _("Right") action Preference("rollback side", "right")

        imagebutton:
            idle "new_ui/settings_rollback_left_idle.png"
            selected_idle "new_ui/settings_rollback_left_selected.png"
            selected_hover "new_ui/settings_rollback_left_selected.png"
            hover "new_ui/settings_rollback_left_hover.png"
            focus_mask True
            action [SelectedIf(Preference("rollback side", "left")), Preference("rollback side", "left")]
            #selected preferences.fullscreen
        imagebutton:
            idle "new_ui/settings_rollback_right_idle.png"
            selected_idle "new_ui/settings_rollback_right_selected.png"
            selected_hover "new_ui/settings_rollback_right_selected.png"
            hover "new_ui/settings_rollback_right_hover.png"
            focus_mask True
            action [SelectedIf(Preference("rollback side", "right")), Preference("rollback side", "right")]
            #selected preferences.fullscreen
        imagebutton:
            idle "new_ui/settings_rollback_disable_idle.png"
            selected_idle "new_ui/settings_rollback_disable_selected.png"
            selected_hover "new_ui/settings_rollback_disable_selected.png"
            hover "new_ui/settings_rollback_disable_hover.png"
            focus_mask True
            action [SelectedIf(Preference("rollback side", "disable")), Preference("rollback side", "disable")]
            #selected preferences.fullscreen

        imagebutton:
            idle "new_ui/settings_skipping_afterchoices_idle.png"
            selected_idle "new_ui/settings_skipping_afterchoices_selected.png"
            #selected_hover "new_ui/settings_skipping_afterchoices_selected.png"
            hover "new_ui/settings_skipping_afterchoices_hover.png"
            focus_mask True
            action Preference("after choices", "toggle")
            selected preferences.skip_after_choices
        imagebutton:
            idle "new_ui/settings_skipping_allmessages_idle.png"
            selected_idle "new_ui/settings_skipping_allmessages_selected.png"
            hover "new_ui/settings_skipping_allmessages_hover.png"
            focus_mask True
            action  Preference("skip", "toggle")
            selected preferences.skip_unseen
        imagebutton:
            idle "new_ui/settings_skipping_transitions_idle.png"
            selected_idle "new_ui/settings_skipping_transitions_selected.png"
            hover "new_ui/settings_skipping_transitions_hover.png"
            focus_mask True
            action InvertSelected(Preference("transitions", "toggle"))
            selected preferences.transitions



    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4
    vbox:
        xalign 0.5
        yalign 0.68
        # if config.has_music or config.has_sound or config.has_voice:
        #     #null height gui.pref_spacing
        #
        #     textbutton _("Mute All"):
        #         action Preference("all mute", "toggle")
        #         style "mute_all_button"

    grid 2 2:
        style_prefix "slider"
        xalign 0.55
        yalign 0.73
        yspacing 180
        xspacing 230

        #box_wrap True
        if config.has_music:
            #label _("Music Volume")

            hbox:
                bar value Preference("music volume")
        #null height 90

        if config.has_sound:

            #label _("Sound Volume")

            hbox:
                bar value Preference("sound volume")

        #####

        hbox:
            bar value Preference("text speed")

        hbox:
            bar value Preference("auto-forward time")


        #null height 320

        #null height 90


        #if config.sample_sound:
        #    textbutton _("Test") action Play("sound", config.sample_sound)

            #null height 90
            ###if config.has_voice:
                #label _("Voice Volume")

            ###    hbox:
            ###        bar value Preference("voice volume")

            ###        if config.sample_voice:
            ###            textbutton _("Test") action Play("voice", config.sample_voice)



#    use game_menu(_("Options"), scroll="viewport"):

#        vbox:

#            hbox:
#                box_wrap True

#                if renpy.variant("pc"):

#                    vbox:
#                        style_prefix "radio"
#                        label _("Display")
#                        textbutton _("Window") action Preference("display", "window")
#                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

#                vbox:
#                    style_prefix "radio"
#                    label _("Rollback Side")
#                    textbutton _("Disable") action Preference("rollback side", "disable")
#                    textbutton _("Left") action Preference("rollback side", "left")
#                    textbutton _("Right") action Preference("rollback side", "right")

#                vbox:
#                    style_prefix "check"
#                    label _("Skip")
#                    textbutton _("Unseen Text") action Preference("skip", "toggle")
#                    textbutton _("After Choices") action Preference("after choices", "toggle")
#                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

#            null height (4 * gui.pref_spacing)

#            hbox:
#                style_prefix "slider"
#                box_wrap True

#                vbox:

#                    label _("Text Speed")

#                    bar value Preference("text speed")

#                    label _("Auto-Forward Time")

#                    bar value Preference("auto-forward time")

#                vbox:

#                    if config.has_music:
#                        label _("Music Volume")

#                        hbox:
#                            bar value Preference("music volume")

#                    if config.has_sound:

#                        label _("Sound Volume")

#                        hbox:
#                            bar value Preference("sound volume")

#                            if config.sample_sound:
#                                textbutton _("Test") action Play("sound", config.sample_sound)


#                    if config.has_voice:
#                        label _("Voice Volume")

#                        hbox:
#                            bar value Preference("voice volume")

#                            if config.sample_voice:
#                                textbutton _("Test") action Play("voice", config.sample_voice)

#                    if config.has_music or config.has_sound or config.has_voice:
#                        null height gui.pref_spacing

#                        textbutton _("Mute All"):
#                            action Preference("all mute", "toggle")
#                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "fonts/KGSorryNotSorryChub.ttf"

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "fonts/KGSorryNotSorryChub.ttf"

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    if main_menu:
        add renpy.random.choice(["bg atu_school_0", "bg atu_nightclub_0", "bg atu_cards_0", "bg atu_cinema_0", "bg atu_park_0", "bg atu_beach_0"])

    default device = "keyboard"

    imagemap:
        add gui.controls_menu_background
        ground "new_ui/nav_idle.png"
        hover "new_ui/nav_hover.png"

        add "new_ui/nav_setn_perm.png"


        hotspot (1210, 150, 85, 85) action ShowMenu("save")#save
        hotspot (1315, 150, 85, 85) action ShowMenu("load")#load
        hotspot (1520, 150, 85, 85) action MainMenu()
        hotspot (1625, 150, 85, 85) action If( renpy.variant("pc"), Show("quitconfirmscreen"), NullAction() ) #quit
        hotspot (205, 150, 85, 85) action Return()#back

        if main_menu:
            add "new_ui/nav_main_menu_block.png"

    #use game_menu(_("Controls"), scroll="viewport"):
        viewport:
            style_prefix "help"
            area (400, 270, 1300, 660)
            scrollbars "vertical"
            mousewheel True
            draggable True

            # side_yfill True

            vbox:
                spacing 23

                hbox:

                    textbutton _("Keyboard") text_color "70a4d9" action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse") text_color "70a4d9" action SetScreenVariable("device", "mouse")

                    if GamepadExists():
                        textbutton _("Gamepad") text_color "70a4d9" action SetScreenVariable("device", "gamepad")

                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.") color "70a4d9"

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.") color "70a4d9"

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.") color "70a4d9"

    hbox:
        label _("Escape")
        text _("Accesses the game menu.") color "70a4d9"

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.") color "70a4d9"

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.") color "70a4d9"

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.") color "70a4d9"

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.") color "70a4d9"

    hbox:
        label "H"
        text _("Hides the user interface.") color "70a4d9"

    hbox:
        label "S"
        text _("Takes a screenshot.") color "70a4d9"

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.") color "70a4d9"


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.") color "70a4d9"

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.") color "70a4d9"

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.") color "70a4d9"

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.") color "70a4d9"

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.") color "70a4d9"


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advance dialogue and activates the interface.") color "70a4d9"

    hbox:
        label ("Left Trigger\nLeft Shoulder")
        text _("Roll back to earlier dialogue.") color "70a4d9"

    hbox:
        label _("Right Shoulder")
        text _("Roll forward to later dialogue.") color "70a4d9"

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.") color "70a4d9"

    hbox:
        label _("Start, Guide")
        text _("Access the game menu.") color "70a4d9"

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.") color "70a4d9"

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")
    font "fonts/KGSorryNotSorryChub.ttf"

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
    color "#344b68"



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    #add "gui/overlay/confirm.png"
    add "new_ui/confirm.png"


    #frame:

    #    vbox:
    #        xalign .5
    #        yalign .5
    #        spacing 45

    label _(message):
        style "confirm_prompt"
        xalign 0.5
        yalign 0.45

    #        hbox:
    #            xalign 0.5
    #            spacing 150

                #textbutton _("Yes") action yes_action
    imagebutton:
        idle "new_ui/confirm_button_yes_idle.png"
        hover "new_ui/confirm_button_yes_hover.png"
        focus_mask True
        action yes_action
                #textbutton _("No") action no_action
    imagebutton:
        idle "new_ui/confirm_button_no_idle.png"
        hover "new_ui/confirm_button_no_hover.png"
        focus_mask True
        action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    font "fonts/KGSorryNotSorryChub.ttf"


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    #ypos gui.notify_ypos
    ypos 600

    background Frame("gui/gui_notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    #background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0
        
        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Menu") action ShowMenu()
        textbutton _("Auto") action Preference("auto-forward", "toggle")


style window:
    variant "small"
    background Frame("gui/phone/textbox.png")

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
