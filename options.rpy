﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("ATownUncovered")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "Version_1.04b"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "ATownUncovered"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "//audio/music/MainMenuMusic.ogg"



## Save Slots Grid #################################################################
define gui.slot_button_width = 313
define gui.slot_button_height = 235

define gui.slot_button_borders = Borders(0, 0, 0, 0)

define config.thumbnail_width = 290
define config.thumbnail_height = 166

define gui.file_slot_cols = 4
define gui.file_slot_rows = 2



## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur. Each
## variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = dissolve


## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Email Minigame Style ###########################################################
##
init python:
    #style.menu_choice_button.background = Frame("choice_idle.jpg",28,19)
    #style.menu_choice_button.hover_background = Frame("choice_hover.jpg",28,19)
    #style.menu_choice.color = "#fff"
    #style.menu_choice.hover_color = "#000"
    #style.menu_choice_button.yminimum = 59
    #email_word_1 = "motherfuckers"#fine people
    #email_word_2 = "shit for brains"#unprofessionalism
    #email_word_3 = "head-fuckwad"#management
    #email_word_4 = "dumbass"#busy_hands
    #email_word_5 = "assholes"#busy_hands
    #cntdwn_number_of_correcting_tries = 6
    #cntdwn_number_of_swears_to_fix = 5

    #def turn_on_email_correcting_hyperlink_functions():
        #style.default.hyperlink_functions = (hyperlink_styler, hyperlink_callback, None)
    #    config.hyperlink_callback = hyperlink_callback
    #    config.hyperlink_styler = hyperlink_styler
        #return
    #def turn_off_email_correcting_hyperlink_functions():
    #    config.hyperlink_callback = None
    #    config.hyperlink_styler = None
        #style.default.hyperlink_functions = (None, None, None)
        #return

    def hyperlink_styler(target):
        if target.startswith("http"):
            return style.http_hyperlink
        elif target.startswith("email_word"):
            return style.correction_text
        else:
            return style.hyperlink_text

        #return style.correction_text

    def hyperlink_callback(target):
        if target.startswith("http:"):
            "http"
            return
        global email_word_1
        global email_word_2
        global email_word_3
        global email_word_4
        global email_word_5
        global cntdwn_number_of_correcting_tries
        global cntdwn_number_of_swears_to_fix
        # handle click.
        #renpy.hide_screen('scr_typing_emails_tutorial')
        if target != None:
            cntdwn_number_of_swears_to_fix -= 1
            #renpy.hide_screen('scr_typing_emails_tutorial')
            if target == "email_word_1":
                if grind_stage == 0:
                    email_word_1 = "fine people"
                elif grind_stage == 1:
                    email_word_1 = "rowdy employees"
                elif grind_stage == 2:
                    email_word_1 = "world"
                elif grind_stage == 3:
                    email_word_1 = "unprofessional bullies"
            elif target == "email_word_2":
                if grind_stage == 0:
                    email_word_2 = "unprofessionalism"
                elif grind_stage == 1:
                    email_word_2 = "enormous"
                elif grind_stage == 2:
                    email_word_2 = "sexually proactive minds"
                elif grind_stage == 3:
                    email_word_2 = "immature"
            elif target == "email_word_3":
                if grind_stage == 0:
                    email_word_3 = "management"
                elif grind_stage == 1:
                    email_word_3 = "inappropriate imagery"
                elif grind_stage == 2:
                    email_word_3 = "uncalled for"
                elif grind_stage == 3:
                    email_word_3 = "young-blood"
            elif target == "email_word_4":
                if grind_stage == 0:
                    email_word_4 = "busy hands"
                elif grind_stage == 1:
                    email_word_4 = "extreme flirting"
                elif grind_stage == 2:
                    email_word_4 = "amateur"
                elif grind_stage == 3:
                    email_word_4 = "confusing"
            elif target == "email_word_5":
                if grind_stage == 0:
                    email_word_5 = "gentlemen"
                elif grind_stage == 1:
                    email_word_5 = "prank"
                elif grind_stage == 2:
                    email_word_5 = "members of society"
                elif grind_stage == 3:
                    email_word_5 = "inexpensive"
            elif target == "email_word_6":
                if grind_stage == 2:
                    email_word_6 = "say a prayer"
                elif grind_stage == 3:
                    email_word_6 = "proper"
            elif target == "email_word_7":
                if grind_stage == 3:
                    email_word_5 = "coffee breaks"
                #renpy.pause(0.01)

                #MainMenu(confirm=False)()
            #renpy.show_screen('scr_typing_emails_tutorial')
            #renpy.hide_screen('scr_typing_emails_tutorial')
        cntdwn_number_of_correcting_tries -= 1


        #renpy.show_screen('scr_typing_emails_tutorial')
        #renpy.show_screen('scr_typing_emails_tutorial')
        #renpy.block_rollback()
        #renpy.fix_rollback()
        #renpy.checkpoint(hard=True)
        renpy.call_in_new_context('lbl_email_proofread_hyperlink_return')#lbl_email_proofread_tutorial

        #renpy.jump_out_of_context('lbl_typing_emails_tutorial')
        #return

    style.default.hyperlink_functions = (hyperlink_styler, hyperlink_callback, None)
    #config.hyperlink_styler = hyperlink_styler

## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 100


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "ATownUncovered-1481961794"


## Icon
## ########################################################################'

## The icon displayed on the taskbar or dock.

define config.window_icon = "ATownUncoveredLogo.ico"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('clean.exe', None)
    build.classify('index.exe', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.md', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpyc', 'archive')
    build.classify('**.ttf', 'font')
    build.classify('**.otf', 'font')
    build.classify('**.txt', 'text')

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.mp3', 'music')
    build.classify('game/**.ogg', 'music')
    build.classify('game/**.wav', 'music')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpt', 'archive')

    ## Archive Categories

    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("music", "all")
    build.archive("font", "all")
    build.archive("text", "all")


    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

###############################################################################
## Windows close button executes confirm close screen
init python:
    config.quit_action = Show("quitconfirmscreen")

###############################################################################
## Automatically turns Developer Mode off when the game is built so that the public won't have access to the images and sounds
## True = ON ## Can SHIFT+R to reload
## False = OFF
    config.developer = "auto"
