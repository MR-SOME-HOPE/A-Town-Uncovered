## Bug Testing Fail Safe ##
label lbl_bug_testing_fail_safe:
    "This feature is mainly to be used to skip over sections where a trigger has failed and you can't continue, or that an error has occured."
    "Please let GeeSeki know about said problem and go through the next steps."
    "Which story are you having trouble with?"

    $ townmap_enabled = 1

label lbl_bug_testing_fail_safe_1:

    menu:
        "Main Story":
            "Your current Chapter Number for the Main story is [main_story]."
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(main_story).is_integer:
                            main_story += 1
                        else:
                            main_story += 0.5
                    "Your current Chapter Number for Main story is now [main_story]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for Main story is [main_story]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ main_story = int(_return)
                        "Your current Chapter Number for Main story is now [main_story]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "Mom" if winc == 1:
            "Your current Chapter Number for Mom's story is [mum_path]"
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(mum_path).is_integer:
                            mum_path += 1
                        else:
                            mum_path += 0.5
                    "Your current Chapter Number for Mom's story is now [mum_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for Mom's story is [mum_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ mum_path = int(_return)
                        "Your current Chapter Number for Mom's story is now [mum_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "[missus]" if winc == 0:
            "Your current Chapter Number for [missus]'s story is [mum_path]"
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(mum_path).is_integer:
                            mum_path += 1
                        else:
                            mum_path += 0.5
                    "Your current Chapter Number for Mom's story is now [mum_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for [missus]'s story is [mum_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ mum_path = int(_return)
                        "Your current Chapter Number for [missus]'s story is now [mum_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "[sister]":
            "Your current Chapter Number for [sister]'s story is [sister_path]."
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(sister_path).is_integer:
                            sister_path += 1
                        else:
                            sister_path += 0.5
                    "Your current Chapter Number for [sister]'s story is now [sister_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for [sister]'s story is [sister_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ sister_path = int(_return)
                        "Your current Chapter Number for [sister]'s story is now [sister_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "Miss Allaway":
            "Your current Chapter Number for Miss Allaway's story is [missallaway_path]."
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(missallaway_path).is_integer:
                            missallaway_path += 1
                        else:
                            missallaway_path += 0.5
                    "Your current Chapter Number for Miss Allaway's story is now [missallaway_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for Miss Allaway's story is [missallaway_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ missallaway_path = int(_return)
                        "Your current Chapter Number for Miss Allaway's story is now [missallaway_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "Director Lashley":
            "Your current Chapter Number for Director Lashley's story is [principallashley_path]."
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(principallashley_path).is_integer:
                            principallashley_path += 1
                        else:
                            principallashley_path += 0.5
                    "Your current Chapter Number for Director Lashley's story is now [principallashley_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for Director Lashley's story is [principallashley_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ principallashley_path = int(_return)
                        "Your current Chapter Number for Director Lashley's story is now [principallashley_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "Hitomi":
            "Your current Chapter Number for Hitomi's story is [hitomi_path]."
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(hitomi_path).is_integer:
                            hitomi_path += 1
                        else:
                            hitomi_path += 0.5
                    "Your current Chapter Number for Hitomi's story is now [hitomi_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for Hitomi's story is [hitomi_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ hitomi_path = int(_return)
                        "Your current Chapter Number for Hitomi's story is now [hitomi_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "Mom & Sister" if winc == 1:
            "Your current Chapter Number for Mom & Sister's story is [mumsis_path]."
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(mumsis_path).is_integer:
                            mumsis_path += 1
                        else:
                            mumsis_path += 0.5
                    "Your current Chapter Number for Mom & Sister's story is now [mumsis_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for Mom & Sister's story is [mumsis_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ mumsis_path = int(_return)
                        "Your current Chapter Number for Mom & Sister's story is now [mumsis_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "[missus] & [sister]" if winc == 0:
            "Your current Chapter Number for [missus] & [sister]'s story is [mumsis_path]."
            "Do you want to skip over to the next chapter or manually enter your own chapter number?"
            "It is advised that you save your game and or ask GeeSeki on what to enter."

            menu:
                "Skip over to the next chapter":
                    python:
                        if float(mumsis_path).is_integer:
                            mumsis_path += 1
                        else:
                            mumsis_path += 0.5
                    "Your current Chapter Number for [missus] & [sister]'s story is now [mumsis_path]."
                    "Sorry for the inconvinience."
                "Manually enter a Chapter Number":
                    if cheat_on == 1:
                        "Your current Chapter Number for [missus] & [sister]'s story is [mumsis_path]."
                        call screen scr_desktop_chapter_input
                        if isinstance(_return, basestring):
                            $ mumsis_path = int(_return)
                        "Your current Chapter Number for [missus] & [sister]'s story is now [mumsis_path]."
                        "Sorry for the inconvinience."
                    else:
                        "Sorry, this feature is only available with the cheat code enabled."

                        jump lbl_bug_testing_fail_safe_1
                "Wrong Problem":
                    jump lbl_bug_testing_fail_safe_1

        "No problem.":
            jump lbl_mybedroom_desk_1

    jump lbl_mybedroom_desk_1

## CHAPTER INPUT SCREEN
screen scr_desktop_chapter_input():
    window:
        style "nvl_window"
        add "img mybedroompc_chapterinputwindow" align (0.5,0.447)
        input id "input" xalign 0.5 yalign 0.5 exclude "qwertyuiopasdfghjklzxcvbnm!@#$%^&*()-=_+[]{};':,./<>?" length 4
        imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1115 ypos 371 focus_mask True action Jump("lbl_mybedroom_desk_1")
    use quick_menu
