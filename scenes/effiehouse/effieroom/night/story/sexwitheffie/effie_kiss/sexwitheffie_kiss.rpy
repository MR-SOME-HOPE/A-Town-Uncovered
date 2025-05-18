## Sex with Effie ##
label lbl_sex_with_effie:
    default sexwitheffie_bj = 0

## Set sex counters to 0
    $ effie_bj = 0
    $ effie_exib = 0
    $ effie_mish = 0

    jump lbl_effie_kiss_1

## KISS
label lbl_effie_kiss_1:

    scene bg hsceneeffiekiss_1
    with fade
    show bg hsceneeffiekiss_1
    $ renpy.pause (2,hard=True)
    show bg hsceneeffiekiss_2
    $ renpy.pause (2,hard=True)
    show bg hsceneeffiekiss_3
    $ renpy.pause ()

    jump lbl_effie_kiss_1_if

label lbl_effie_kiss_1_if:
    if effie_points <= 0:
        jump lbl_effie_kiss_1_0
    else:
        jump lbl_effie_kiss_1_1

label lbl_effie_kiss_1_0:
    show bg hsceneeffiekiss_5
    eff "Sorry I shouldn't have done that."
    show bg hsceneeffiekiss_7
    pov "Uhm.. it's oka-"

    jump lbl_effie_kiss_1_0_1

label lbl_effie_kiss_1_0_1:
    show bg hsceneeffiekiss_9
    effdad "Effie? Are you home?"
    eff "Oh, shit.. hold on."
    eff "Don't come in! I'm changing!"
    effdad "Alright. I'm just checking up on you. How's work and university?"
    eff "It's good. Nothing new!"
    effdad "Alright. Well, I've got company with me tonight so, goodnight!"
    eff "G'night, Dad!"
    if main_story == 12:
        $ main_story = 13
    elif main_story >= 14:
        $ effie_funlater = 0
        $ effie_path = 2

    jump lbl_effieroom_night_setup

label lbl_effie_kiss_1_1:
    show bg hsceneeffiekiss_5
    eff "Sorry, but I ALWAYS get what I want."
    eff "You're not going to leave early, are you?"

    menu:
        "I'll stay.":
            show bg hsceneeffiekiss_6
            pov "I'm going to stay for as long as you want me to."
            show bg hsceneeffiekiss_8
            eff "Good boy."

            jump lbl_effie_bj_1
        "I think it's best that I leave now.":
            if effie_points >= 1:
                $ effie_points -= 1
            else:
                $ effie_points = 0
            $ renpy.notify("Your relationship with Effie has decreased")
            show bg hsceneeffiekiss_7
            pov "Actually, I think it's best that I leave now."
            show bg hsceneeffiekiss_1
            eff "I-I was expecting you to go along with that. Welp. You just kinda ruined the mood."

            jump lbl_effie_kiss_1_0_1
