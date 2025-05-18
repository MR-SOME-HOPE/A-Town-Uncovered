## Never Again ##
label lbl_never_again:
    #"Mom is leaning against the car."
    scene bg neveragain_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg neveragain_2
    #"MC is heading towards the house."
    mum "..."
    mum "[povname], wait-"
    pov "Hhm-?"
    #"Mom falls into your arms and gives you a tight hug."
    #"Mom falls into your arms and gives you a tight hug around the neck."
    scene bg neveragain_3
    with hpunch
    $ renpy.pause(0.5,hard=True)
    show bg neveragain_4
    mum "Never scare me like this again... {i}Never{/i}!"
    show bg neveragain_6
    pov "Never again."
    show bg neveragain_5
    pov "I promise."
    if mum_points >= 7 and mum_path >= 9:
        #"Mom pulls you into a passionate kiss."
        #"She breaks the kiss and you rest your forhead on hers."
        scene bg neveragain_9
        with hpunch
        $ renpy.pause(0.3,hard=True)
        show bg neveragain_10
        $ renpy.pause(0.3,hard=True)
        show bg neveragain_9
        $ renpy.pause(0.5,hard=True)
        show bg neveragain_10
        $ renpy.pause(0.9,hard=True)
        show bg neveragain_4
        mum "I'm so glad you're home safe and sound but I'm still mad at you."
        show bg neveragain_5
        if winc == 1:
            pov "I know, Mom. I'm glad to be back home too."
        else:
            pov "I know, [missus]. I'm glad to be back home too."
    show bg neveragain_8
    mum "You're lucky I love you so much."
    show bg neveragain_7
    if winc == 1:
        pov "Hehehe, I love you too, Mom. And again, I'm really sorry for everything."
    else:
        pov "Hehehe, I love you too, [missus]. And again, I'm really sorry for everything."
    $ main_story = 40
    $ townmap_enabled = 0

    jump lbl_myhousefront_day_setup
