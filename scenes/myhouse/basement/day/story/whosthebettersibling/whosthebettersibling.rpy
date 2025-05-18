## Who's The Better Sibling ##
label lbl_whos_the_better_sibling:
    default whosthebettersibling_win = 0
    #default whosthebettersibling_counter = 0
    default whosthebettersibling_owe = 0
    default whosthebettersibling_bet = 0

    scene bg whosthebettersibling_1
    with fade
    sis "Whoa, whoa, whoa! Dude, what the hell are you bring that out for?"
    show bg whosthebettersibling_1
    with hpunch
    sis "I am not sucking you off!"
    pov "Hey, hey, hey! Dude."
    pov "Not so loud. I thought that maybe we could get even."
    sis "What do you mean even?"
    pov "I've watched you play with yourself many times on stream."
    show bg whosthebettersibling_2
    pov "I figured that I should play with myself in front of you to get..."
    show bg whosthebettersibling_1
    sis "Even."
    show bg whosthebettersibling_2
    pov "Mhmm..."
    show bg whosthebettersibling_1
    pov "..."
    show bg whosthebettersibling_2
    sis "..."
    show bg whosthebettersibling_1
    if winc == 0:
        pov "Do you like it when you watch your [povsisrole] stroke it?"
    else:
        pov "Do you like it when you watch your baby brother stroke it?"
    show bg whosthebettersibling_2
    sis "It's a lot bigger than I remember..."
    show bg whosthebettersibling_1
    pov "..."
    show bg whosthebettersibling_2
    pov "What do you feel?"
    show bg whosthebettersibling_1
    sis "..."
    show bg whosthebettersibling_2
    sis "I feel..."
    show bg whosthebettersibling_1
    sis "I.. feel..."
    show bg whosthebettersibling_2
    pov "Do you feel turned on?"
    show bg whosthebettersibling_1
    pov "Because that's how I felt when I watch you..."
    show bg whosthebettersibling_2
    pov "This-"
    show bg whosthebettersibling_1
    pov "This is how big I got from watching you tease me."
    show bg whosthebettersibling_2
    sis "You're aiming it at me..."
    show bg whosthebettersibling_1
    sis "The head is staring at me, hehehe~"
    show bg whosthebettersibling_2
    pov "It's throbbing just for you, [sister]."
    show bg whosthebettersibling_1
    pov "..."
    show bg whosthebettersibling_2
    pov "Just sit back- and enjoy watching me jack off for you."
    show bg whosthebettersibling_1
    if winc == 0:
        pov "Watch your [povsisrole] stroke his hard cock for you."
    else:
        pov "Watch your baby brother stroke his hard cock for you."
    show bg whosthebettersibling_2
    pov "Shit..."
    show bg whosthebettersibling_1
    pov "We are so fucked up..."
    show bg whosthebettersibling_2
    pov "And I'm so fucking horny watching you watch me..."
    show bg whosthebettersibling_1
    sis "I know you want to grab my head and shove it straight in my mouth, [povname]."
    show bg whosthebettersibling_2
    pov "Fuck... don't say that, [sister]. Don't fucking tempt me..."
    show bg whosthebettersibling_1
    pov "I'm doing this for you..."
    show bg whosthebettersibling_2
    sis "..."
    show bg whosthebettersibling_1
    sis "I appreciate the private show you're giving me.. But I wanna relieve myself..."
    show bg whosthebettersibling_2
    pov "You're free to DJ on that clit if you want."
    show bg whosthebettersibling_1
    sis "Hahaha, ‘DJ on that clit'."
    show bg whosthebettersibling_2
    sis "No, I want to play a game. Wanna play?"
    pov "What's the game?"
    show bg whosthebettersibling_1
    if winc == 0:
        sis "It's a little game that I like to call ‘Who's the better [povsisrole]? Oral Edition'."
    else:
        sis "It's a little game that I like to call ‘Who's the better sibling? Oral Edition'."
    sis "It's simple."
    show bg whosthebettersibling_2
    sis "No hands, mouths only."
    pov "The winner is the one that gets to cum?"
    show bg whosthebettersibling_1
    sis "No...? The winner is the one that manages to hold their own."
    pov "That doesn't sound like much of a win. I say the loser gets the satisfaction."
    show bg whosthebettersibling_2
    sis "Winner gets $200."
    pov "Where are you gonna get $200 from?"
    show bg whosthebettersibling_1
    if winc == 0:
        sis "$100 each. That's the bet. You in, or you out, [povname]?"
    else:
        sis "$100 each. That's the bet. You in, or you out, bro-bro?"
    sis "And don't say you're out because I wanna get my pussy eaten just as badly as I wanna taste your losing cum."
    if inventory.money <= 99:
        pov "I don't have... $100..."
        sis "Fuck you, I'm too fucking horny now."

        menu:
            "Play":
                pov "Great, let's do it!"

                jump lbl_whos_the_better_sibling_1
            "Don't play":
                pov "Sorry, [sister]. Can't let you get your way this time."
                pov "I'm your tease for the night."
                sis "..."
                sis "You're a fucking tease... asshole..."
                sis "I thought we were supposed to be fucked up together."
                sis "I'm going upstairs, and I'm gonna cum multiple times."
                sis "Without you!"
                sis "Hmph!"
                $ sister_path = 26

                jump lbl_mybasement_day_setup
    else:
        menu:
            "Bet $100":
                jump lbl_whos_the_better_sibling_1
            "Don't bet":
                pov "Sorry, [sister]. I'll have to pass on the bet this time."
                sis "Why? You know you'll be down $100?"
                pov "I have a strong feeling."
                sis "Fucking weaksauce, bro... Any other guy would pass on $100 for this opportunity in a heartbeat."
                if winc == 0:
                    sis "I thought we were supposed to be the messed up, perverted [povsisrole]s.."
                else:
                    sis "I thought we were supposed to be the messed up, perverted twins.."
                sis "I'm going upstairs, and I'm gonna cum so hard."
                sis "Without you!"
                sis "Hmph!"
                $ sister_path = 26

                jump lbl_mybasement_day_setup

label lbl_whos_the_better_sibling_revisit:
    scene black
    with fade
    $ renpy.pause()
    sis "So, are we playing for the hundo again?"
    sis "Remember the deal, whoever cums first loses."

    if inventory.money <= 99:
        pov "I don't have... $100..."
        sis "You're poor and yet I'm still gonna suck your dick..."
        sis "That's how horny I am."

    else:
        menu:
            "Bet $100":
                $ whosthebettersibling_bet = 1

                pov "Your wallet's about to get lighter."

            "Don't bet":
                pov "Nah, I have a feeling that I'm gonna cum all over you."
                sis "Ugh- fine..."
                sis "Guess my Azamon wishlist is gonna have to wait a lil' while longer."

    jump lbl_whos_the_better_sibling_1

label lbl_whos_the_better_sibling_1:
    scene bg whosthebettersibling_8
    with fade
    $ renpy.pause(1,hard=True)
    show bg whosthebettersibling_3
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_4
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_5
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_6
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_7
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_3
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_4
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_5
    $ renpy.pause(0.1,hard=True)
    show bg whosthebettersibling_6
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_7
    $ renpy.pause(0.3,hard=True)

    menu:
        "Distract your thoughts":
            if skill_sta >= 8 and skill_int >= 6:
                $ skill_sta -= 8
                $ skill_int -= 6
                $ whosthebettersibling_win = 1
            else:
                if skill_sta >= 8:
                    $ skill_sta -= 8
                else:
                    $ skill_sta = 0
                if skill_int >= 6:
                    $ skill_int -= 6
                else:
                    $ skill_int = 0
            $ renpy.notify("You used 8 Stamina Points\nYou used 6 Intelligence Points")
            $ renpy.pause(1,hard=False)
        "Focus on giving her your best":
            if sister_points <= 8:
                $ sister_points += 2
            else:
                $ sister_points = 10
            if skill_sta >= 10 and skill_cha >= 8:
                $ skill_sta -= 10
                $ skill_cha -= 8
                $ whosthebettersibling_win = 1
            else:
                if skill_sta >= 10:
                    $ skill_sta -= 10
                else:
                    $ skill_sta = 0
                if skill_cha >= 8:
                    $ skill_cha -= 8
                else:
                    $ skill_cha = 0
            $ renpy.notify("You used 8 Charisma Points\nYou used 10 Stamina Points\nYour relationship with [sister] has increased by 2")

    jump lbl_whos_the_better_sibling_continue

label lbl_whos_the_better_sibling_continue:
    #$ whosthebettersibling_counter = 0
    
    jump lbl_whos_the_better_sibling_2

####################
## 69 Stage 1
label lbl_whos_the_better_sibling_2:
    scene img_whos_the_better_sibling_stage_1
    #$ whosthebettersibling_counter += 1
    #show bg whosthebettersibling_3
    #$ renpy.pause(0.3,hard=True)
    #show bg whosthebettersibling_4
    #$ renpy.pause(0.1,hard=True)
    #show bg whosthebettersibling_5
    #$ renpy.pause(0.1,hard=True)
    #show bg whosthebettersibling_6
    #$ renpy.pause(0.3,hard=True)
    #show bg whosthebettersibling_7
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and whosthebettersibling_counter == 4:
    #    jump lbl_whos_the_better_sibling_cum
    #elif skill_sta <= 14 and whosthebettersibling_counter == 6:
    #    jump lbl_whos_the_better_sibling_3
    #elif skill_sta <= 20 and whosthebettersibling_counter == 8:
    #    jump lbl_whos_the_better_sibling_3
    #else:
    #    jump lbl_whos_the_better_sibling_2
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_whos_the_better_sibling_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_whos_the_better_sibling_3

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_whos_the_better_sibling_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_whos_the_better_sibling_2

image img_whos_the_better_sibling_stage_1:
    "bg whosthebettersibling_3"
    pause 0.3
    "bg whosthebettersibling_4"
    pause 0.1
    "bg whosthebettersibling_5"
    pause 0.1
    "bg whosthebettersibling_6"
    pause 0.3
    "bg whosthebettersibling_7"
    pause 0.3
    repeat
####################
## 69 Stage 2
label lbl_whos_the_better_sibling_3:
    scene img_whos_the_better_sibling_stage_2
    #$ whosthebettersibling_counter += 1
    #show bg whosthebettersibling_3
    #$ renpy.pause(0.3,hard=True)
    #show bg whosthebettersibling_5
    #$ renpy.pause(0.1,hard=True)
    #show bg whosthebettersibling_6
    #$ renpy.pause(0.2,hard=True)
    #show bg whosthebettersibling_7
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and whosthebettersibling_counter == 14:
    #    jump lbl_whos_the_better_sibling_cum
    #elif skill_sta <= 20 and whosthebettersibling_counter == 16:
    #    jump lbl_whos_the_better_sibling_4
    #else:
    #    jump lbl_whos_the_better_sibling_3
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_whos_the_better_sibling_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_whos_the_better_sibling_4

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_whos_the_better_sibling_3

image img_whos_the_better_sibling_stage_2:
    "bg whosthebettersibling_3"
    pause 0.3
    "bg whosthebettersibling_5"
    pause 0.1
    "bg whosthebettersibling_6"
    pause 0.2
    "bg whosthebettersibling_7"
    pause 0.2
    repeat
####################
## 69 Stage 3
label lbl_whos_the_better_sibling_4:
    scene img_whos_the_better_sibling_stage_3
    #$ whosthebettersibling_counter += 1
    #show bg whosthebettersibling_3
    #$ renpy.pause(0.2,hard=True)
    #show bg whosthebettersibling_5
    #$ renpy.pause(0.1,hard=True)
    #show bg whosthebettersibling_7
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and whosthebettersibling_counter == 24:
    #    jump lbl_whos_the_better_sibling_cum
    #else:
    #    jump lbl_whos_the_better_sibling_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_whos_the_better_sibling_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_whos_the_better_sibling_3

image img_whos_the_better_sibling_stage_3:
    "bg whosthebettersibling_3"
    pause 0.2
    "bg whosthebettersibling_5"
    pause 0.1
    "bg whosthebettersibling_7"
    pause 0.2
    repeat
####################
## BJ Cum
label lbl_whos_the_better_sibling_cum:
    if whosthebettersibling_win == 0:
        call screen scr_whos_the_better_sibling_5_0
        screen scr_whos_the_better_sibling_5_0():
            imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_whos_the_better_sibling_continue")
            imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_whos_the_better_sibling_cumchoice")
    else:
        jump lbl_whos_the_better_sibling_cumsis

label lbl_whos_the_better_sibling_cumchoice:

    menu:
        "Cum inside":
            jump lbl_whos_the_better_sibling_cumin
        "Cum on her":
            jump lbl_whos_the_better_sibling_cumout

label lbl_whos_the_better_sibling_cumsis:
    scene bg whosthebettersibling_8
    sis "Oh, fuck... fuck- fuck... [povname].. [povname]..."
    sis "Oh my God... keep going- keep-"
    sis "..."
    sis "...."
    sis "Arrghhh! Fucckk! Hooo... fuck!"
    show bg whosthebettersibling_9
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_10
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_11
    $ renpy.pause(0.8,hard=True)
    sis "Shit..."
    show bg whosthebettersibling_12
    sis "Oh my God.. Naww... dude.. Fu- oh God... I'm soo sorry..."
    sis "I didn't mean to squirt all over you...."
    sis "A- are you okay?"
    sis "Can you breathe?"
    show bg whosthebettersibling_13
    pov "I'm okay."
    pov "Daamn, girl. You really covered me..."
    pov "I win! Hahaha-"
    show bg whosthebettersibling_14
    pov "Ow.. oww... my eyes... it stings!"

    jump lbl_whos_the_better_sibling_end

label lbl_whos_the_better_sibling_cumin:
    scene bg whosthebettersibling_3
    pov "Oh... fucckk! I'm cumming, [sister]!"
    show bg whosthebettersibling_4
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_15
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_16
    $ renpy.pause(0.5,hard=True)
    show bg whosthebettersibling_17
    $ renpy.pause(0.5,hard=True)
    show bg whosthebettersibling_18
    $ renpy.pause(0.8,hard=True)
    show bg whosthebettersibling_19
    $ renpy.pause(0.4,hard=True)
    show bg whosthebettersibling_20
    $ renpy.pause(0.5,hard=True)
    pov "Holy shit..."
    pov "..."
    pov "[sister]?"
    pov "You alright there?"
    show bg whosthebettersibling_21
    sis "{i}*Murmur*{/i}"
    pov "Huh?"
    sis "{i}*Murmur*{/i}"
    show bg whosthebettersibling_22
    if sister_path <= 26 or whosthebettersibling_bet == 1:
        pov "Sorry I jizzed a lot... I hope it taste as good as your $100."
    else:
        pov "Sorry I jizzed a lot, you were really asking for it."

    jump lbl_whos_the_better_sibling_end

label lbl_whos_the_better_sibling_cumout:
    scene bg whosthebettersibling_3
    pov "Oh... fucckk! I'm cumming, [sister]!"
    show bg whosthebettersibling_23
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_24
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_25
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_26
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_27
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_28
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_29
    $ renpy.pause(0.3,hard=True)
    show bg whosthebettersibling_30
    $ renpy.pause(0.8,hard=True)
    pov "Holy shit..."
    pov "..."
    show bg whosthebettersibling_31
    sis "Holy shit is right, [povname]..."
    sis "It shot straight up my nose."
    sis "Ow.. oh, God... I think I snorted your cum."
    sis "Fuck..."
    show bg whosthebettersibling_32
    if sister_path <= 26 or whosthebettersibling_bet == 1:
        sis "Totally worth the $100 though."
    else:
        sis "What's the point of a money shot without the money..."


    jump lbl_whos_the_better_sibling_end

label lbl_whos_the_better_sibling_end:
    if sister_hscenerevisit == 1:
        $ sister_hscenerevisit = 0
        $ gtime += 1
        if whosthebettersibling_bet == 1:
            if whosthebettersibling_win == 1:
                $ inventory.money += 100
                $ renpy.notify("Current Balance: $[inventory.money]")
            else:
                $ inventory.money -= 100
                $ renpy.notify("Current Balance: $[inventory.money]")
        else:
            pass
    else:
        $ sister_path = 26
        if whosthebettersibling_win == 1:
            $ inventory.money += 100
            $ renpy.notify("Current Balance: $[inventory.money]")
        else:
            if inventory.money >= 100:
                $ inventory.money -= 100
                $ renpy.notify("Current Balance: $[inventory.money]")
            else:
                $ whosthebettersibling_owe = 1
                $ renpy.notify("You owe [sister] $100.")

    if gtime <= 1:
        jump lbl_mybasement_day
    else:
        jump lbl_mybasement_night
