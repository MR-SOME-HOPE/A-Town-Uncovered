###############
## Setup
## Story Path
label lbl_schoolgym_night_setup:
    if jack_path == 0:
        pass
    else:
        play ambience 'audio/ambience/schoolgymnight_ambience.ogg' fadein 1.0
## Make sure Strength doesn't go over 20
    if skill_strmax >= 20:
        $ skill_strmax = 20

## Sex World
    if 28 <= main_story <= 33:
        pov "{i}The lights are on but the door is locked...{/i}"
        pov "Hello?! Can I come in?!"
        pov "..."
        pov "I guess not?"

        jump lbl_schoolyard_night_setup

## Before meeting Jack
    if jack_path == 0:
        pov "{i}Hmm, there must be some basketball game going on tonight. I'm not really interested.{/i}"

        jump lbl_schoolyard_night_setup

## Fight Club
    elif jack_path == 1:
        scene bg schoolgym_nightlightson
        with fade

        jump lbl_fight_club

## Miss Allaway Watching Gym Setup
    if main_story >= 17 and missallaway_path == 0:
        $ missallaway_path = 0.5
        $ townmap_enabled = 0

## Allaway Wants a Warrior
    elif main_story >= 17 and missallaway_path == 11:
        $ missallaway_path = 11.5
        $ townmap_enabled = 0

## I Become the Warrior
    elif missallaway_path == 12:
        $ missallaway_path = 12.5
        $ ibecomethewarrior_beatbrock = 0

## Beat the Shit out of Jack
    elif missallaway_path == 19:
        jump lbl_beat_the_shit_out_of_jack

## Normal
    else:
        jump lbl_schoolgym_night

###############
## Room Navigation
## This is the map for schoolgym during the night.

label lbl_schoolgym_night:

    scene bg schoolgym_nightlightson
    call screen scr_schoolgym_night

screen scr_schoolgym_night():
    imagebutton auto "btn schoolgym_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_night_door")
    imagebutton auto "btn schoolgym_night_crowd_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_night_crowd")
    imagebutton auto "btn schoolgym_night_phil_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_night_phil")
    imagebutton auto "btn schoolgym_night_jack_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_night_jack")
    imagebutton auto "btn schoolgym_night_brock_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_night_brock")
    imagebutton auto "btn schoolgym_night_coach_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_night_coachfistem")
    use hud_overlay

###############
## Labels
label lbl_schoolgym_night_door:
    play ambience 'audio/ambience/quietexteriornight_ambience.ogg' fadein 2.0
    jump lbl_schoolyard_night_setup

label lbl_schoolgym_night_phil:
    show btn_schoolgym_night_brock_idle2
    show btn_schoolgym_night_coach_idle2
    show btn_schoolgym_night_jack_idle2
    show btn_schoolgym_night_phil_idle2
    $ renpy.pause(0.001)
    hide btn_schoolgym_night_phil_idle2
    show pov shocked at left
    with dissolve
    show phi bored_talk at right
    with dissolve
    phi "Go away, I'm watching the fight-"
    phi "Ayo! Fuck his shit up!"

    jump lbl_schoolgym_night

label lbl_schoolgym_night_jack:
    show btn_schoolgym_night_brock_idle2
    show btn_schoolgym_night_coach_idle2
    show btn_schoolgym_night_jack_idle2
    show btn_schoolgym_night_phil_idle2
    $ renpy.pause(0.001)
    hide btn_schoolgym_night_jack_idle2
    show pov bored at left
    with dissolve
    show jack bored_talk at right
    with dissolve
    jack "Fuck off, I have no interest in you."

    jump lbl_schoolgym_night

label lbl_schoolgym_night_brock:
    show btn_schoolgym_night_brock_idle2
    show btn_schoolgym_night_coach_idle2
    show btn_schoolgym_night_jack_idle2
    show btn_schoolgym_night_phil_idle2
    $ renpy.pause(0.001)
    hide btn_schoolgym_night_brock_idle2
    show pov embarrassed at left
    with dissolve
    show bro confused_talk at right
    with dissolve
    bro "Hey, little man. Can't talk now, I'm in the middle of my sets."

    jump lbl_schoolgym_night

label lbl_schoolgym_night_coachfistem:
    show btn_schoolgym_night_brock_idle2
    show btn_schoolgym_night_coach_idle2
    show btn_schoolgym_night_jack_idle2
    show btn_schoolgym_night_phil_idle2
    $ renpy.pause(0.001)
    hide btn_schoolgym_night_coach_idle2
    show pov confused at left
    with dissolve
    show coa bored_talk at right
    with dissolve
    coa "Are you ready to fight? If you are, get into the middle."

    jump lbl_schoolgym_night
