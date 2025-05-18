## Movie Dream - Mom Action ##
label lbl_movie_dream_allaway_action:
    if skill_str <= 13:
        jump lbl_movie_dream_allaway_action_1
    else:
        jump lbl_movie_dream_allaway_action_2

label lbl_movie_dream_allaway_action_1:

    scene black
    $ renpy.pause(1.5)

    show bg allawaydream_action_1
    pause
    show bg allawaydream_action_2
    pause
    show bg allawaydream_action_3
    pause
    show bg allawaydream_action_4
    pause
    show bg allawaydream_action_5
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_action_6
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_action_7
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_action_10
    $ renpy.pause(1.0,hard=True)
    show bg allawaydream_action_11
    $ renpy.pause(2.0,hard=True)
    scene white
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg dream_wakeup_1
    $ renpy.pause(1,hard=True)
    show bg dream_wakeup_2
    pov "{i}Fuck...{/i}"

    jump lbl_movie_dream_allaway_action_end

label lbl_movie_dream_allaway_action_2:

    scene black
    $ renpy.pause(1.5)
    show bg allawaydream_action_1
    pause
    show bg allawaydream_action_2
    pause
    show bg allawaydream_action_3
    pause
    show bg allawaydream_action_4
    pause
    show bg allawaydream_action_5
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_action_6
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_action_7
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_action_8
    $ renpy.pause(1.0,hard=True)
    show bg allawaydream_action_9
    $ renpy.pause(2.0,hard=True)
    scene white
    with dissolve
    show bg dream_wakeup_1
    "{i}*Beep Beep Beep*{/i}"
    pov "..."
    pov "{i}Fuck me...{/i}"

    jump lbl_movie_dream_allaway_action_end

label lbl_movie_dream_allaway_action_end:
    $ moviedate = 0
    $ moviedate_choice = 0

    jump lbl_mybedroom_night_sleep_1
