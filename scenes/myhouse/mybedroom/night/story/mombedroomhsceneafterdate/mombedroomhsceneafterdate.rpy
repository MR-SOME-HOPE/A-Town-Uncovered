## Mom Bedroom Hscene After Date ##

#default mom_bedroom_hscene_bj_counter = 0
#default mom_bedroom_hscene_mish_counter = 0
#default mom_bedroom_hscene_desk_anal_counter = 0
#default mom_bedroom_hscene_desk_rimjob_counter = 0
#default mom_bedroom_hscene_desk_pussy_counter = 0

label lbl_mom_bedroom_hscene_after_date:

    scene black
    with fade
    "You changed out of your suit."

    scene bg mybedroom_night_lightson
    with fade
    "{i}*Knock knock*{/i}"
    show pov confused_talk at left
    with dissolve
    pov "Come in?"
    show pov confused at left
    show mum embarrassed_talk at right
    with dissolve
    mum "Hey, sweetie."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    if winc == 0:
        pov "Hey, [missus]..."
    else:
        pov "Hey, Mom..."
    pov "I thought you went to bed."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I couldn't see myself falling asleep until I came in here."
    show mum smirk at right
    pov "..."
    show mum smirk_talk at right
    mum "Now's my turn to make your night a night to remember."

    menu:
        "Kiss her and hit a homerun":
            $ mum_path = 30.5
        "I'm not in the mood.":
            show pov sad_talk at left
            show mum shocked at right
            pov "I'm not in the mood tonight..."
            show pov sad at left
            mum "..."
            show mum shocked_talk at right
            mum "What...?"
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Oh. Alright, I get it."
            mum "You're tired.. don't worry."
            show mum sad_talk at right
            mum "So am I.. I- I'll just go."
            show pov sad_talk at left
            mum "Goodnight, bab- [povname]."
            show pov embarrassed_talk at left
            show mum sad at right
            if winc == 0:
                pov "Goodnight, [missus]. Maybe tomorrow night?"
            else:
                pov "Goodnight, Mom. Maybe tomorrow night?"
            show mum embarrassed at right
            mum "Mmm.."
            $ mum_path = 30

            jump lbl_mybedroom_night_setup
    play sex_sounds mouth_kiss_02 noloop
    scene bg mommakeupkiss_1
    with fade
    $ renpy.pause(1.5, hard=True)
    play sex_sounds mouth_kiss_05 noloop
    show bg mommakeupkiss_2
    $ renpy.pause(1.5, hard=True)
    play sex_sounds mouth_kiss_03 noloop
    show bg mommakeupkiss_1
    $ renpy.pause(2, hard=True)

    jump lbl_mom_bedroom_hscene_after_bj

####################
## Scene Choice
label lbl_mom_bedroom_hscene_after_scenechoice_bj:

    menu:
        "Go to Bed":
            jump lbl_mom_bedroom_hscene_after_mish
        "Go to Desk":
            jump lbl_mom_bedroom_hscene_after_desk

label lbl_mom_bedroom_hscene_after_scenechoice_mish:

    menu:
        "Stay in Bed":
            stop sex_sounds
            scene bg mombedroomhscene_mish_31
            with dissolve

            jump lbl_mom_bedroom_hscene_after_mish_choice
        "Go to Desk":
            jump lbl_mom_bedroom_hscene_after_mish_next

label lbl_mom_bedroom_hscene_after_scenechoice_mishanal:

    menu:
        "Stay in Bed":
            stop sex_sounds
            scene bg mombedroomhscene_mish_31
            with dissolve

            jump lbl_mom_bedroom_hscene_after_mish_choice
        "Go to Desk":
            jump lbl_mom_bedroom_hscene_after_mishanal_next

label lbl_mom_bedroom_hscene_after_scenechoice_desk_rimjob:

    menu:
        "Go to Bed":
            jump lbl_mom_bedroom_hscene_after_desk_rimjob_next_2
        "Stay at Desk":
            stop sex_sounds
            scene bg mombedroomhscene_desk_1
            with dissolve

            jump lbl_mom_bedroom_hscene_after_desk_choice

label lbl_mom_bedroom_hscene_after_scenechoice_desk_pussy:

    menu:
        "Go to Bed":
            jump lbl_mom_bedroom_hscene_after_desk_pussy_next
        "Stay at Desk":
            stop sex_sounds
            scene bg mombedroomhscene_desk_1
            with dissolve

            jump lbl_mom_bedroom_hscene_after_desk_choice

label lbl_mom_bedroom_hscene_after_scenechoice_desk_anal:

    menu:
        "Go to Bed":
            jump lbl_mom_bedroom_hscene_after_desk_anal_next
        "Stay at Desk":
            stop sex_sounds
            scene bg mombedroomhscene_desk_1
            with dissolve

            jump lbl_mom_bedroom_hscene_after_desk_choice

####################
## Desk Choice
label lbl_mom_bedroom_hscene_after_desk:

    scene bg mombedroomhscene_desk_1
    with fade
    mum "What are you going to do, honey?"

label lbl_mom_bedroom_hscene_after_desk_choice:

    menu:
        "Rimjob":
            jump lbl_mom_bedroom_hscene_after_desk_rimjob
        "Anal Fuck":
            jump lbl_mom_bedroom_hscene_after_desk_anal
        "Pussy Fuck":
            jump lbl_mom_bedroom_hscene_after_desk_pussy
