################################################################################
label lbl_start_name_pov:
    scene bg namingfamily_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg namingfamily_4
    with dissolve
    ## Ask for the player's name
    "What is your name?"
    menu:
        "John":
            $ povname = "John"

            jump lbl_start_name_sister

        "Enter my name":
            pass

    define pov = Character("[povname]", color="#5e8fb4")

    show img namingbox at Position(xalign=0.5,yalign=0.456)
    python:
        povname = renpy.input("What's your name?", length=21)
        povname = povname.strip()

        if not povname:
            povname = "John"
    hide img namingbox

    # if povname == "tester":
    #     $ main_story = 10
    #     $ winc = 1
    #     $ month = 5
    #     $ date = 9
    #     $ day = 6
    #     $ gtime = 0
    #     $ hscene_xray = 1
    #     $ inventory.money = 500
    #     $ skill_luc = 10
    #     $ skill_str = 10
    #     $ skill_sta = 10
    #     $ skill_int = 10
    #     $ skill_cha = 10
    #     $ skill_lucmax = 10
    #     $ skill_strmax = 10
    #     $ skill_stamax = 10
    #     $ skill_intmax = 10
    #     $ skill_chamax = 10
    #     $ sister = "Jane"
    #     $ missus = "Mom"

    #     jump lbl_mybedroom_day_setup

################################################################################
label lbl_start_name_sister:
    default sisrole = "rival"
    default sister = "Jane"
    default povsisrole = "rival"

    ## Name Sister
    show bg namingfamily_3
    with dissolve

label lbl_start_name_sister_1:
    "Who is this character to you?"
    menu:
        "Rival":
            python:
                sisrole = "rival"
                povsisrole = "rival"
        "Roommate":
            python:
                sisrole = "roommate"
                povsisrole = "roommate"
        "Friend":
            python:
                sisrole = "friend"
                povsisrole = "friend"
        "Other":
            show img namingbox at Position(xalign=0.5,yalign=0.456)
            python:
                sisrole = renpy.input("Enter your relationship with this character:")
                sisrole = sisrole.strip()
                povsisrole = "associate"

                if not sisrole:
                    sisrole = "roommate"
                    povsisrole = "roommate"
            hide img namingbox

            if sisrole == "sister" or sisrole == "Sister" or sisrole == "sis" or sisrole == "Sis" or sisrole == "sibling" or sisrole == "Sibling":
                "We do not condone incest in our game. We recommend you set the relationship of this character to either 'rival', 'roommate', or 'friend'."
                "Are you sure you want your relationship to be [sisrole]?"
                menu:
                    "Yes":
                        "Do you, the player understand and agree that this is completely your choice and there were no other factors that influenced your decision making or your free will?"
                        menu:
                            "I agree that it is completely my decision.":
                                $ povsisrole = "brother"
                            "I do not agree, let me choose again.":
                                jump lbl_start_name_sister_1
                    "No":
                        jump lbl_start_name_sister_1

            else:
                "Are you sure you want your relationship to be [sisrole]?"
                menu:
                    "Yes":
                        pass
                    "No":
                        jump lbl_start_name_sister_1

    menu:
        "Name her 'Jane'":
            $ sister = "Jane"

            jump lbl_start_name_mother

        "Enter her name":
            pass

    show img namingbox at Position(xalign=0.5,yalign=0.456)
    python:
        sister = renpy.input("What name do you want to give your [sisrole]?")
        sister = sister.strip()

        if not sister:
            sister = "Jane"
    hide img namingbox

################################################################################
label lbl_start_name_mother:
    ## Name Mother
    show bg namingfamily_2
    with dissolve

label lbl_start_name_mother_1:
    default mumrole = "landlady"
    default missus = "Mrs Smith"
    default povmumrole = "tenant"

    "Who is this character to you?"
    menu:
        "Landlady":
            python:
                mumrole = "landlady"
                povmumrole = "tenant"
        "Roommate":
            python:
                mumrole = "roommate"
                povmumrole = "roommate"
        "Friend":
            python:
                mumrole = "friend"
                povmumrole = "friend"
        "Other":
            show img namingbox at Position(xalign=0.5,yalign=0.456)
            python:
                mumrole = renpy.input("Enter your relationship with this character:")
                mumrole = mumrole.strip()
                povmumrole = "assocciate"

                if not mumrole:
                    mumrole = "landlady"
                    povmumrole = "tenant"
            hide img namingbox

            ## Check Mother and Sister
            if mumrole == "mom" or mumrole == "Mom" or mumrole == "mum" or mumrole == "Mum" or mumrole == "mother" or mumrole == "Mother":
                "We do not condone incest in our game. We recommend you set the relationship of this character to either 'landlady', 'roommate', or 'friend'."
                "Are you sure you want your relationship to be [mumrole]?"
                menu:
                    "Yes":
                        "Do you, the player understand and agree that this is completely your choice and there were no other factors that influenced your decision making or your free will??"
                        menu:
                            "I agree that it is completely my decision.":
                                $ povmumrole = "son"
                            "I do not agree, let me choose again.":
                                jump lbl_start_name_mother_1
                    "No":
                        jump lbl_start_name_mother_1

                if sisrole == "sister" or sisrole == "Sister" or sisrole == "sis" or sisrole == "Sis" or sisrole == "sibling" or sisrole == "Sibling":
                    $ missus = "Mom"
                    $ winc = 1

            else:
                "Are you sure you want your relationship to be [mumrole]?"
                menu:
                    "Yes":
                        pass
                    "No":
                        jump lbl_start_name_mother_1

    if winc == 1:
        $ missus = "Mom"
    else:
        menu:
            "Name her 'Mrs Smith'":
                $ missus = "Mrs Smith"

                jump lbl_start_name_father

            "Enter her name":
                pass

        show img namingbox at Position(xalign=0.5,yalign=0.456)
        python:
            missus = renpy.input("What name do you want to give your [mumrole]?")
            missus = missus.strip()

            if not missus:
                missus = "Mrs Smith"
        hide img namingbox

    define mum = Character("[missus]", color="ae9466")

################################################################################
label lbl_start_name_father:
    default dadrole = "landlord"
    default dadname = "Mr Smith"
    default povdadrole = "tenant"

    show bg namingfamily_5
    with dissolve

    ## Name Father
    if winc == 1:
        $ dadrole = "father"
        $ dadname = "Dad"
        $ povdadrole = "son"

    else:
        "Who is this character to you?"
        menu:
            "Landlord":
                python:
                    dadrole = "landlord"
                    povdadrole = "tenant"
            "Roommate":
                python:
                    dadrole = "roommate"
                    povdadrole = "roommate"
            "Friend":
                python:
                    dadrole = "friend"
                    povdadrole = "friend"
            "Other":
                show img namingbox at Position(xalign=0.5,yalign=0.456)
                python:
                    dadrole = renpy.input("Enter your relationship with this character:")
                    dadrole = dadrole.strip()
                    povdadrole = "assocciate"

                    if not dadrole:
                        dadrole = "landlord"
                        povdadrole = "tenant"
                hide img namingbox

        "This is [missus]'s husband, and your [dadrole]."

        if winc == 1:
            $ dadname = "Dad"
        else:
            menu:
                "Name him 'Mr Smith'":
                    $ dadname = "Mr Smith"

                    jump lbl_newgame_or_preset

                "Enter his name":
                    pass

        show img namingbox at Position(xalign=0.5,yalign=0.456)
        python:
            dadname = renpy.input("What name do you want to give him?")
            dadname = dadname.strip()

            if not dadname:
                dadname = "Mr Smith"
        hide img namingbox

    define dad = Character("[dadname]", color="c9cdce")

label lbl_newgame_or_preset:
    scene black
    with fade
    if startnewgame == 1:
        jump intro_cutscene
    else:
        jump lbl_start_game_load
