## Movie Dream - Mom Action ##
label lbl_movie_dream_mom_action:
    if skill_str <= 13:
        jump lbl_movie_dream_mom_action_1
    else:
        jump lbl_movie_dream_mom_action_2

label lbl_movie_dream_mom_action_1:

    scene black
    $ renpy.pause
    mum "Save me..."
    if winc == 0:
        pov "{i}[missus]..?{/i}"
        show bg momdream_action_1
        pov "[missus]!"
        show bg momdream_action_2
        pov "Don't worry, [missus]! I'll get you out of here."
    else:
        pov "{i}Mom..?{/i}"
        show bg momdream_action_1
        pov "Mom!"
        show bg momdream_action_2
        pov "Don't worry, Mom! I'll get you out of here."
    show bg momdream_action_3
    $ renpy.pause(1,hard=True)
    show bg momdream_action_4
    mum "[povname].. how... how close is it?"
    show bg momdream_action_5
    mum "[povname]?!"

    scene white
    $ renpy.pause(0.5,hard=True)
    show bg dream_wakeup_1
    $ renpy.pause(1,hard=True)
    show bg dream_wakeup_2
    pov "{i}Fuck...{/i}"

    jump lbl_movie_dream_mom_action_end

label lbl_movie_dream_mom_action_2:

    scene black
    $ renpy.pause
    mum "Save me..."
    if winc == 0:
        pov "{i}[missus]..?{/i}"
        show bg momdream_action_1
        pov "[missus]!"
        show bg momdream_action_2
        pov "Don't worry, [missus]! I'll get you out of here."
    else:
        pov "{i}Mom..?{/i}"
        show bg momdream_action_1
        pov "Mom!"
        show bg momdream_action_2
        pov "Don't worry, Mom! I'll get you out of here."
    show bg momdream_action_3
    $ renpy.pause(1,hard=True)
    show bg momdream_action_4
    mum "[povname].. how... how close is it?"
    show bg momdream_action_5
    mum "[povname]?!"
    show bg momdream_action_6
    $ renpy.pause(0.6,hard=True)
    show bg momdream_action_7
    $ renpy.pause(0.8,hard=True)
    show bg momdream_action_8
    $ renpy.pause(0.3,hard=True)
    show bg momdream_action_9
    $ renpy.pause(0.6,hard=True)
    show bg momdream_action_10
    $ renpy.pause(1,hard=True)
    show bg momdream_action_11
    with hpunch
    $ renpy.pause()
    show bg momdream_action_12
    mum "Oh, my hero. Oh my God, [povname]."
    mum "I want you to fuck me."
    mum "I want you to fuuuccckkk mee."
    mum "Fuccckk mee."
    mum "Fucck me."
    show bg dream_wakeup_1
    "{i}*Beep Beep Beep*{/i}"
    pov "..."
    pov "{i}Fuck me...{/i}"

    jump lbl_movie_dream_mom_action_end

label lbl_movie_dream_mom_action_end:
    $ moviedate = 0
    $ moviedate_choice = 0

    jump lbl_mybedroom_night_sleep_1
