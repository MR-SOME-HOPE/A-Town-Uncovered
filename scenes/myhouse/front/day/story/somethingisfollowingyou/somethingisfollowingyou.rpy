## Something is Following You
label lbl_something_is_following_you:
    image bg somethingisfollowingyou_2_anim = Animation(
    "//scenes/myhouse/front/day/story/somethingisfollowingyou/assets/bg_somethingisfollowingyou_2.jpg", 0.8,
    "//scenes/myhouse/front/day/story/somethingisfollowingyou/assets/bg_somethingisfollowingyou_2-5.jpg", 0.8
    )## bg somethingisfollowingyou_2, bg somethingisfollowingyou_2-5
    ## Front of House Day
    ## Sprite start
    scene bg myhousefront_day
    with fade
    show pov sad
    with dissolve
    pov "{i}*Sigh*{/i}"
    show pov sad_talk
    pov "I should have stayed in bed today."
    pov "Beats everything that has been going on so far for sure."
    show pov sad
    pov "{i}Thank God I haven't shared my Twatter with anyone.{/i}"
    show pov embarrassed
    pov "{i}Wouldn’t hear the end of it from the guys back home.{/i}"
    pov "…"
    show pov sad
    pov "{i}Then again, I guess this is my home now.{/i}"
    pov "{i}Where I am known as a nudist pervert.{/i}"
    show pov angry_talk
    pov "Fucking fantastic."
    show pov neutral
    pov "{i}*Sigh*{/i}"
    ##scene bg somethingisfollowingyou_temp1
    scene bg somethingisfollowingyou_1
    with fade
    $ renpy.pause(0.1,hard=True)
    scene bg themysteriousfigure_4_2
    $ renpy.pause(0.1,hard=True)
    show bg survivedthedrowning_1_5
    $ renpy.pause(0.1,hard=True)
    show bg girlatthedoor_1
    $ renpy.pause(0.1,hard=True)
    show bg girlatthedoor_6
    $ renpy.pause(0.1,hard=True)
    show bg takenforsacrifice_4
    $ renpy.pause(0.1,hard=True)
    show bg takenforsacrifice_14
    $ renpy.pause(0.1,hard=True)
    show bg takenforsacrifice_40
    $ renpy.pause(0.1,hard=True)
    show bg takenforsacrifice_48
    $ renpy.pause(0.1,hard=True)
    show bg backtosafety_5
    $ renpy.pause(0.1,hard=True)
    show bg backtosafety_6
    $ renpy.pause(0.1,hard=True)
    show bg theresnakedpictures_1
    $ renpy.pause(0.1,hard=True)
    show bg discussingtheincident_2
    $ renpy.pause(0.1,hard=True)
    ##show bg somethingisfollowingyou_temp1
    show bg somethingisfollowingyou_1
    $ renpy.pause(1,hard=True)
    scene bg myhousefront_day
    with fade
    ## Sprites start
    ## Back to normal/sprites
    show pov confused
    with dissolve
    pov "{i}I…{/i}"
    pov "{i}I did get drugged that night, right?{/i}"
    show pov shocked
    pov "{i}None of what I saw happened, right?{/i}"
    show pov neutral_talk
    pov "It was all a hallucination.. Yeah."
    pov "For sure."
    show pov smirk_talk
    pov "There is no sex world or murderous sex cult."
    pov "There are no psycho anal obsessed freaks or superhuman naked ghost ladies after me."
    show pov confused
    pov "{i}I must have taken a drink meant for someone else and just raved about naked, for the whole night before passing out in the lake.{/i}"
    show pov neutral
    pov "{i}Nothing more, nothing less.{/i}"
    show pov angry
    pov "{i}Just the after effects of a really bad trip from a really bad prank.{/i}"
    show pov neutral_talk
    pov "No need to panic!"

    ## CG Scene start
    ##scene bg somethingisfollowingyou_temp1
    scene bg somethingisfollowingyou_1
    with fade
    ##"You hear behind you the sounds of bushes moving, making you turn at them clearly afraid"
    pov "Huh?"
    scene bg somethingisfollowingyou_2
    show bg somethingisfollowingyou_2_anim with dissolve
    $ renpy.pause(2.0, hard=True)
    pov "W-Who’s there?!" with dissolve
    ##show bg somethingisfollowingyou_temp2
    scene bg somethingisfollowingyou_2 with dissolve
    ##"After the bushes stop moving and you stay in silence for a while"

    pov "..."
    pov "...."
    pov "....."
    pov "J-Just a racoon."
    pov "Right?"

    menu:
        "Go investigate the bush":
            pass
        "Get the fuck inside":
            pass

    pov "I-"

    ##show bg somethingisfollowingyou_temp3
    scene bg somethingisfollowingyou_3
    with vpunch
    ##"You are interrupted by the sudden movement of the bushes and out of the trees, the familiar figure of Vi coming out the shadow of the trees and staring you down, her hair hiding her robotic features ring girl style"
    scene bg somethingisfollowingyou_4 with dissolve
    scene bg somethingisfollowingyou_5 with dissolve
    pov "Wha-!"



    ##"As you stay stiff, frozen in fear, VI starts to make her way towards you menacingly, finally snapping you out of it"

    ##show bg somethingisfollowingyou_temp4
    scene bg somethingisfollowingyou_6 with hpunch
    $ renpy.pause(0.3,hard=True)
    ##show bg somethingisfollowingyou_temp5
    scene bg somethingisfollowingyou_6-5
    with hpunch
    $ renpy.pause(0.2,hard=True)
    scene bg somethingisfollowingyou_7 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene bg somethingisfollowingyou_8
    $ renpy.pause(2.0)
    scene bg somethingisfollowingyou_9
    $ renpy.pause(2.0)

    ##show bg somethingisfollowingyou_temp6
    show bg somethingisfollowingyou_10
    pov "WHAT THE FUCK?!"
    ##"You scream as you run away as fast as you can inside the safety of your home."

    ##show bg somethingisfollowingyou_temp7
    show bg somethingisfollowingyou_11 with hpunch
    pov "Waaaaaahhhhh!!"
    $ renpy.pause(1.0)
    scene bg somethingisfollowingyou_10 with hpunch
    scene black with fade

    $ main_story = 46

    jump lbl_paranoid_entrance
