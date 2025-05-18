## Invite Sister to Fort ##
label lbl_invite_sister_to_fort:

    scene bg invitesistertofort_1
    with fade
    pov "Hey..."
    pov "[sister]..."
    pov "Wake up..."
    pov "Let's head down to the fort tonight..."
    pov "..."
    pov "Can you hear me?"
    pov "..."

    menu:
        "Keep talking":
            pov "Hey."
            pov "Heey."
            pov "Heeey.."
            pov "[sister]."
            pov "Hello?"
            pov "Wake."
            pov "Up."
            pov "Wake."
            pov "Up."
            pov "Wake-"
            show bg invitesistertofort_2
            sis "Don't-"
            sis "Fuckin' say it."
            show bg invitesistertofort_3
            pov "..."

            menu:
                "Say it":
                    if sister_points >= 9:
                        $ sister_points -= 1
                    else:
                        $ sister_points = 0
                    $ renpy.notify("Your relationship with [sister] has decreased")
                    pov "...Up"
                    show bg invitesistertofort_4
                    with hpunch
                    sis "YOU FUCKING DONE DID IT!"
                    show bg invitesistertofort_2
                    sis "I- {i}*Deep inhale*{/i}"
                    show bg invitesistertofort_3
                    sis "..."
                    show bg invitesistertofort_5
                    sis "Ughh... what do you want?"
                "Stay silent":
                    pov "..."
                    sis "..."
                    show bg invitesistertofort_2
                    sis "What do you want, [povname]?"
            show bg invitesistertofort_6
            pov "I wanted to see if you wanted to come down to the fort tonight?"
            show bg invitesistertofort_7
            sis "Couldn't you have asked me that earlier?"
            show bg invitesistertofort_6
            pov "Well..."
            pov "I wanted a pity revenge for you waking me up that other night."
            pov "...Tah-dah~"
            sis "..."
            show bg invitesistertofort_2
            sis "Fine. I'll meet you there in a second."
            sis "Let me put on some clothes."
            show bg invitesistertofort_8
            pov "You can come down without them on if you want."
            if skill_cha >= 5 and sister_points >= 5:
                show bg invitesistertofort_9
                sis "Can I now?"

                jump lbl_invite_sister_to_fort_1
            else:
                jump lbl_invite_sister_to_fort_2
        "Pull her sheets off":
            if sister_points >= 8:
                $ sister_points -= 2
            else:
                $ sister_points = 0
            $ renpy.notify("Your relationship with [sister] has decreased by 2")
            show bg invitesistertofort_10
            $ renpy.pause(1,hard=True)
            show bg invitesistertofort_11
            $ renpy.pause(0.5,hard=True)
            show bg invitesistertofort_12
            sis "What the fuck, [povname]?!"
            sis "How many times are you going to do this?!"
            sis "You know I don't have any clothes on!"
            show bg invitesistertofort_13
            pov "I wanted to see if you wanted to come down to the fort tonight?"
            show bg invitesistertofort_12
            sis "Couldn't you have asked me that earlier?"
            show bg invitesistertofort_13
            pov "Well..."
            pov "I wanted a pity revenge for you waking me up that other night."
            pov "...Tah-dah~"
            sis "..."
            show bg invitesistertofort_14
            sis "Fine. I'll meet you there in a second."
            sis "Let me put on some clothes."
            show bg invitesistertofort_15
            pov "You can come down without them on if you want."
            if skill_cha >= 5 and sister_points >= 5:
                show bg invitesistertofort_16
                sis "Can I now?"

                jump lbl_invite_sister_to_fort_1
            else:
                jump lbl_invite_sister_to_fort_3

label lbl_invite_sister_to_fort_1:

    scene bg sisterbedroom_night
    with fade
    show pov shocked at left
    with dissolve
    show sisn confused_talk at right
    with dissolve
    sis "Like this?"
    show sisn smirk at right
    pov "..."
    show sisn confused_talk at right
    sis "This is what you wanted, right?"
    show sisn smirk_talk at right
    if winc == 0:
        sis "To see your own [sisrole] naked?"
    else:
        sis "To see your own sister naked?"
    show sisn angry_talk at right
    sis "Want me to spread my cheeks for you too?"
    show pov embarrassed at left
    sis "Pervert."
    show pov shocked at left
    if winc == 0:
        sis "Get the hell outta my room before I tell [missus] you're ogling me."
    else:
        sis "Get the hell outta my room before I tell Mom you're ogling me."
    show pov embarrassed_talk at left
    show sisn angry at right
    pov "No worries, bab- I meant..."
    show pov shocked_talk at left
    show sisn shocked at right
    pov "What the fuck."
    show pov embarrassed_talk at left
    show sisn bored at right
    pov "Uh- yeah."
    pov "See you there."

    jump lbl_invite_sister_to_fort_end

label lbl_invite_sister_to_fort_2:
    show bg invitesistertofort_7
    sis "In your dreams, flapjack."
    sis "It's funny when I say but when you say it..."
    show bg invitesistertofort_18
    sis "I've got the woman's pass."
    show bg invitesistertofort_4
    sis "Now get out of my room. I'll meet you downstairs."

    jump lbl_invite_sister_to_fort_end

label lbl_invite_sister_to_fort_3:
    show bg invitesistertofort_14
    sis "In your dreams, flapjack."
    sis "It's funny when I say but when you say it..."
    show bg invitesistertofort_17
    sis "I've got the woman's pass."
    show bg invitesistertofort_12
    sis "Now get out of my room. I'll meet you downstairs."

    jump lbl_invite_sister_to_fort_end

label lbl_invite_sister_to_fort_end:
    $ sister_path = 16
    $ townmap_enabled = 0

    jump lbl_myhallway_night_setup
