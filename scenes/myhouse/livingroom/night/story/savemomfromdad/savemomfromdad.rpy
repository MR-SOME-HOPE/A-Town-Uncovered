default morningdad_donttalktomom = 0

## Save Mom From Dad ##
label lbl_save_mom_from_dad:
    default savemomfromdad = 0
    if winc == 0:
        jump lbl_save_mom_from_dad_winc0

    scene bg savemomfromdad_1
    with fade
    $ renpy.pause()
    show bg savemomfromdad_2
    $ renpy.pause()
    show bg savemomfromdad_1

    menu:
        "Step in and tackle dad":
            jump lbl_save_mom_from_dad_1
        "Leave":
            pov "{i}Mom told me not to come down here...{/i}"

            jump lbl_myhallway_night_setup # FUCKING PUSSY

label lbl_save_mom_from_dad_1:
    show bg savemomfromdad_3
    with hpunch
    pov "Get the fuck away from mom, you asshole!"
    if skill_str >= 8:
        $ savemomfromdad_tackle = 1
        $ skill_str -= 4
        $ renpy.notify("You used 4 Strength Points")
        show bg savemomfromdad_4
        with hpunch
        mum "{i}*cough cough*{/i} [povname]..."
        mum "S- {i}*cough*{/i} Stop..."
        $ renpy.pause(2, hard=True)

        jump lbl_save_mom_from_dad_2
    else:
        $ savemomfromdad_tackle = 0
        if skill_str > 6:
            $ skill_str -= 6
        else:
            $ skill_str = 0
        $ renpy.notify("You weren't strong enough and his counter cost you 6 Strength Points")
        show bg savemomfromdad_5
        with hpunch
        dad "Don't you even fucking come at me like that again, got it?"
        dad "I can easily fuck you up, [povname]."
        dad "You wanna be a man now, then cut this shit out."
        show bg savemomfromdad_6
        mum "H-hon... ge-get off.. him.."
        $ renpy.pause(1, hard=True)
        mum "I said GET THE FUCK OFF HIM!"
        show bg savemomfromdad_5
        dad "You're lucky your mother cares about you.."
        $ renpy.pause(1, hard=True)

        jump lbl_save_mom_from_dad_3

label lbl_save_mom_from_dad_2:

    scene bg mylivingroom_night
    with fade
    show pov angry_talk at left
    with dissolve
    show mum sad
    with dissolve
    show dadpo angry at right
    with dissolve
    pov "C'mon, Mom. You're sleeping with me tonight."
    if momfeelingabandoned_promise == 0:
        show pov angry at left
        show mum sad_talk
        show dadpo angry at right
        mum "[povname]... I told you not to come down here..."
    else:
        show pov angry at left
        show mum sad_talk
        show dadpo angry at right
        mum "You promised me you wouldn't come down here..."
    show mum sad_talk
    mum "You have to go back to your room..."
    show pov angry_talk at left
    show mum sad
    pov "Not without you, Mom."
    show pov angry at left
    mum "..."
    show dadpo angry_talk at right
    dad "You little shit. You think you can disrespect me and save your mother?"
    show mum angry
    show dadpo angry_talk at right
    dad "Well, you're in for a-"
    show mum angry_talk
    show dadpo angry at right
    mum "Hey! Don't you fucking talk to our son like that!"
    show mum angry
    show dadpo angry_talk at right
    dad "He needs to fucking learn his place in this house!"

    jump lbl_save_mom_from_dad_4

label lbl_save_mom_from_dad_3:

    scene bg mylivingroom_night
    with fade
    show pov angry at left
    with dissolve
    show mum sad
    with dissolve
    show dadpo angry_talk at right
    with dissolve
    dad "This is your warning, [povname]. You don't ever want to mess with me again."
    dad "C'mon, dear. Let's get to bed."
    show mum sad_talk
    show dadpo angry at right
    mum "B-"
    show mum angry
    show dadpo angry_talk at right
    dad "Don't. Fucking talk back at m-"
    show mum angry_talk
    show dadpo angry at right
    mum "Don't FUCKING TELL ME WHAT TO DO!"
    show mum angry
    show dadpo neutral at right
    mum "..."
    show mum angry_talk
    mum "Y-You do not own me, I am not your property to use and mistreat."
    mum "I'm your fucking wife, treat me with the fucking respect I fucking deserve!"

    jump lbl_save_mom_from_dad_4

label lbl_save_mom_from_dad_4:
    show pov angry at left
    show mum angry_talk
    show dadpo angry at right
    mum "JUST.... Just..."
    show pov sad at left
    show mum sad_talk
    show dadpo neutral at right
    mum "Just let me be... okay?"
    mum "Please."
    mum "I'm... I'm exhausted..."
    show mum sad
    mum "..."
    if morningdad_donttalktomom == 1 or momfeelingabandoned_promise == 0 and mum_points >= 4:
        show pov neutral at left
        show mum sad_talk
        show dadpo angry at right
        mum "Let's go, [povname]."
        $ savemomfromdad = 1
        $ mum_path = 10

        jump lbl_mybedroom_night_setup
    else:
        show pov sad at left
        show mum sad_talk
        show dadpo neutral at right
        mum "I- I'm going to bed now.. Let me sleep, please..."
        mum "I- I need t- to sleep..."
        $ savemomfromdad = 0
        $ mum_path = 10
        $ gtime = 3

        jump lbl_mylivingroom_night_setup

### NO WINC ###
label lbl_save_mom_from_dad_winc0:

    scene bg savemomfromdad_1
    with fade
    $ renpy.pause()
    show bg savemomfromdad_2
    $ renpy.pause()
    show bg savemomfromdad_1

    menu:
        "Step in and tackle [dadname]":
            jump lbl_save_mom_from_dad_1_winc0
        "Leave":
            pov "{i}[missus] told me not to come down here...{/i}"

            jump lbl_myhallway_night_setup # FUCKING PUSSY

label lbl_save_mom_from_dad_1_winc0:
    show bg savemomfromdad_3
    with hpunch
    pov "Get the fuck away from [missus], you asshole!"
    if skill_str >= 8:
        $ savemomfromdad_tackle = 1
        $ skill_str -= 4
        $ renpy.notify("You used 4 Strength Points")
        show bg savemomfromdad_4
        with hpunch
        mum "{i}*cough cough*{/i} [povname]..."
        mum "S- {i}*cough*{/i} Stop..."
        $ renpy.pause(2, hard=True)

        jump lbl_save_mom_from_dad_2_winc0
    else:
        $ savemomfromdad_tackle = 0
        if skill_str > 6:
            $ skill_str -= 6
        else:
            $ skill_str = 0
        $ renpy.notify("You weren't strong enough and his counter cost you 6 Strength Points")
        show bg savemomfromdad_5
        with hpunch
        dad "Don't you even fucking come at me like that again, got it?"
        dad "I can easily fuck you up, [povname]."
        dad "You wanna be a man now, then cut this shit out."
        show bg savemomfromdad_6
        mum "H-hon... ge-get off.. him.."
        $ renpy.pause(1, hard=True)
        mum "I said GET THE FUCK OFF HIM!"
        show bg savemomfromdad_5
        dad "You're lucky your [mumrole] cares about you.."
        $ renpy.pause(1, hard=True)

        jump lbl_save_mom_from_dad_3_winc0

label lbl_save_mom_from_dad_2_winc0:

    scene bg mylivingroom_night
    with fade
    show pov angry_talk at left
    with dissolve
    show mum sad
    with dissolve
    show dadpo angry at right
    with dissolve
    pov "C'mon, [missus]. You're sleeping with me tonight."
    if momfeelingabandoned_promise == 0:
        show pov angry at left
        show mum sad_talk
        show dadpo angry at right
        mum "[povname]... I told you not to come down here..."
    else:
        show pov angry at left
        show mum sad_talk
        show dadpo angry at right
        mum "You promised me you wouldn't come down here..."
    show mum sad_talk
    mum "You have to go back to your room..."
    show pov angry_talk at left
    show mum sad
    pov "Not without you, [missus]."
    show pov angry at left
    mum "..."
    show dadpo angry_talk at right
    dad "You little shit. You think you can disrespect me and save your [mumrole]?"
    show mum angry
    show dadpo angry_talk at right
    dad "Well, you're in for a-"
    show mum angry_talk
    show dadpo angry at right
    mum "Hey! Don't you fucking talk to our [povdadrole] like that!"
    show mum angry
    show dadpo angry_talk at right
    dad "He needs to fucking learn his place in this house!"

    jump lbl_save_mom_from_dad_4_winc0

label lbl_save_mom_from_dad_3_winc0:

    scene bg mylivingroom_night
    with fade
    show pov angry at left
    with dissolve
    show mum sad
    with dissolve
    show dadpo angry_talk at right
    with dissolve
    dad "This is your warning, [povname]. You don't ever want to mess with me again."
    dad "C'mon, dear. Let's get to bed."
    show mum sad_talk
    show dadpo angry at right
    mum "B-"
    show mum angry
    show dadpo angry_talk at right
    dad "Don't. Fucking talk back at m-"
    show mum angry_talk
    show dadpo angry at right
    mum "Don't FUCKING TELL ME WHAT TO DO!"
    show mum angry
    show dadpo neutral at right
    mum "..."
    show mum angry_talk
    mum "Y-You do not own me, I am not your property to use and mistreat."
    mum "I'm your fucking wife, treat me with the fucking respect I fucking deserve!"

    jump lbl_save_mom_from_dad_4_winc0

label lbl_save_mom_from_dad_4_winc0:
    show pov angry at left
    show mum angry_talk
    show dadpo angry at right
    mum "JUST.... Just..."
    show pov sad at left
    show mum sad_talk
    show dadpo neutral at right
    mum "Just let me be... okay?"
    mum "Please."
    mum "I'm... I'm exhausted..."
    show mum sad
    mum "..."
    if morningdad_donttalktomom == 1 or momfeelingabandoned_promise == 0 and mum_points >= 4:
        show pov neutral at left
        show mum sad_talk
        show dadpo angry at right
        mum "Let's go, [povname]."
        $ savemomfromdad = 1
        $ mum_path = 10

        jump lbl_mybedroom_night_setup
    else:
        show pov sad at left
        show mum sad_talk
        show dadpo neutral at right
        mum "I- I'm going to bed now.. Let me sleep, please..."
        mum "I- I need t- to sleep..."
        $ savemomfromdad = 0
        $ mum_path = 10
        $ gtime = 3

        jump lbl_mylivingroom_night_setup
