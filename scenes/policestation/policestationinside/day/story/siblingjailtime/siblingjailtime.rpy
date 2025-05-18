## Sibling Jail Time ##
label lbl_sibling_jail_time:
    default siblingjailtime_stevereveal = 0
    default siblingjailtime_hj = 1
    #default handy_in_jail_counter = 0

    scene bg siblingjailtime_0
    $ renpy.pause()
    sis "Damn..."
    sis "Turns out she wasn't a prostitute..."
    pov "M-maybe... this is her policee themed- uh- sex dungeoooon!"
    sis "[povname], that was the stupidest, most unhelpful thing you've said all night."
    show bg siblingjailtime_1
    sis "{i}*Sigh*{/i}"
    if winc == 0:
        sis "[missus] isn't going to like this..."
    else:
        sis "Mom's not going to like this..."
    show bg siblingjailtime_2
    $ renpy.pause
    show bg siblingjailtime_3
    $ renpy.pause()
    show bg siblingjailtime_4
    sis "I'll go see if I can find a way out of here..."
    show bg siblingjailtime_5
    $ renpy.pause(1,hard=True)
    show bg siblingjailtime_6
    $ renpy.pause(3,hard=True)
    show bg siblingjailtime_7
    $ renpy.pause(2,hard=True)
    show bg siblingjailtime_8
    $ renpy.pause()
    show bg siblingjailtime_9
    sis "Look what I got."
    show bg siblingjailtime_10
    pov "Oooh, it's shiny."
    show bg siblingjailtime_11
    pov "What is it?"
    show bg siblingjailtime_9
    sis "They're keys. I don't know where to though, but once I figure it out, we can bust out of here."
    show bg siblingjailtime_12
    sis "I don't know why the ring is so big though, it looks like a cock ring."
    show bg siblingjailtime_13
    pov "Mmmmmmaybe it is? Has that eeeever crossed your mind?"
    show bg siblingjailtime_14
    sis "..."
    show bg siblingjailtime_15
    sis "Pull your pants down, [povname]."

    menu:
        "Sure.":
            show bg siblingjailtime_16
            pov "Waaaay ahead of you, [sister]."

            jump lbl_sibling_jail_time_2
        "No, thanks.":
            show bg siblingjailtime_17
            pov "..."
            show bg siblingjailtime_18
            pov "I... have... thoroughly thought through your... per-por-purp-pop-porp-proposition..."
            pov "And I dun-don'-diddly want aaaanything up my butt."
            pov "Thank you for the offer though."
            show bg siblingjailtime_19
            sis "What? No, stupid! I just wanna see if the ring fits on your cock, nothing weird."
            show bg siblingjailtime_20
            pov "Ohhh! Is that it?"

            menu:
                "Alright, then.":
                    pov "For science!"

                    jump lbl_sibling_jail_time_2
                "Still no.":
                    show bg siblingjailtime_21
                    pov "I dun-don't think so, missy-moo. Nex- thing ya know, I... have a KEY- up my buttocks!"
                    pov "Nuh-uh, no maa'am."
                    $ siblingjailtime_hj = 0

                    jump lbl_sibling_jail_time_3

label lbl_sibling_jail_time_2:

    scene bg handyinjail_1
    with fade
    sis "Hey, I knew it. It's almost a perfect fit."
    show bg handyinjail_2
    sis "A little loose though.."
    show bg handyinjail_3
    pov "Don't worry, I can make it fit more snugged."
    show bg handyinjail_4
    pov "Check this shit out!"
    show bg handyinjail_5
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg handyinjail_6
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg handyinjail_7
    sis "Whoa!!"
    show bg handyinjail_8
    pov "Ah- ah- ahhh... [sister], it's tight... ge- get it off!"
    show bg handyinjail_9
    with hpunch
    mina "HEY! WHAT THE HELL ARE YOU BOTH DOING?!"
    mina "WHERE DID YOU GET THOSE KEYS?!"
    mina "ARE YOU FUCKING SERIOUS, PAUL?! WHERE ARE THE SPARE KEYS?!"
    show bg handyinjail_10
    pau "Those... are the spare keys."
    mina "And what the fuck were you doing? You were supposed to keep an eye on these two."
    mina "Is that a nudie mag you're sitting on?!"
    show bg handyinjail_11
    mina "For God's sakes, Paul."
    mina "Gimme those fucking keys or you'll get into extra trouble!"
    show bg handyinjail_12
    sis "I- I can't, I think it's stuck."
    show bg handyinjail_13
    pov "It feels very very very..."
    pov "Very much stuck..."
    show bg handyinjail_14
    mina "I can't fucking believe this... I hate dealing with drunk teenagers."
    mina "I'll be right back, I'll get some soap or something to slip it off."
    show bg handyinjail_15
    $ renpy.pause()
    show bg handyinjail_16
    $ renpy.pause(0.4,hard=True)
    show bg handyinjail_17
    $ renpy.pause(0.4,hard=True)
    show bg handyinjail_18
    $ renpy.pause(0.2,hard=True)
    show bg handyinjail_16
    $ renpy.pause(0.4,hard=True)
    show bg handyinjail_20
    pau "Hey! Stop doing that!"
    show bg handyinjail_19
    sis "Shut up, Paul."
    show bg handyinjail_20
    pov "Yeah, shut up... Stev-"
    show bg handyinjail_19
    sis "Paul."
    show bg handyinjail_20
    pov "Paul!"
    show bg handyinjail_21
    sis "You know you wanna watch..."
    show bg handyinjail_22
    sis "Sit there and keep quiet, I know what I'm doing."

    jump lbl_handy_in_jail_0

label lbl_handy_in_jail_0:
    #$ handy_in_jail_counter = 0
    jump lbl_handy_in_jail_1

####################
## Stage 1
label lbl_handy_in_jail_1:
    scene img_handy_in_jail_stage_1
    #$ handy_in_jail_counter += 1
    #show bg handyinjail_15
    #$ renpy.pause(0.15,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_17
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_18
    #$ renpy.pause(0.15,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.15,hard=True)
    #show bg handyinjail_15
    #$ renpy.pause(0.15,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_17
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_18
    #$ renpy.pause(0.15,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.15,hard=True)
    #if skill_sta <= 7 and handy_in_jail_counter == 4:
    #    jump lbl_handy_in_jail_cum
    #elif skill_sta <= 14 and handy_in_jail_counter == 6:
    #    jump lbl_handy_in_jail_2
    #elif skill_sta <= 20 and handy_in_jail_counter == 8:
    #    jump lbl_handy_in_jail_2
    #else:
    #    jump lbl_handy_in_jail_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_handy_in_jail_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_handy_in_jail_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_handy_in_jail_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_handy_in_jail_1

image img_handy_in_jail_stage_1:
    "bg handyinjail_15"
    pause 0.15
    "bg handyinjail_16"
    pause 0.05
    "bg handyinjail_17"
    pause 0.05
    "bg handyinjail_18"
    pause 0.15
    "bg handyinjail_16"
    pause 0.15
    "bg handyinjail_15"
    pause 0.15
    "bg handyinjail_16"
    pause 0.05
    "bg handyinjail_17"
    pause 0.05
    "bg handyinjail_18"
    pause 0.15
    "bg handyinjail_16"
    pause 0.15
    repeat

####################
## Stage 2
label lbl_handy_in_jail_2:
    scene img_handy_in_jail_stage_2
    #$ handy_in_jail_counter += 1
    #show bg handyinjail_15
    #$ renpy.pause(0.15,hard=True)
    #show bg handyinjail_17
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_18
    #$ renpy.pause(0.1,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.1,hard=True)
    #show bg handyinjail_15
    #$ renpy.pause(0.15,hard=True)
    #show bg handyinjail_17
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_18
    #$ renpy.pause(0.1,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 14 and handy_in_jail_counter == 14:
    #    jump lbl_handy_in_jail_cum
    #elif skill_sta <= 20 and handy_in_jail_counter == 16:
    #    jump lbl_handy_in_jail_3
    #else:
    #    jump lbl_handy_in_jail_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_handy_in_jail_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_handy_in_jail_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_handy_in_jail_2

image img_handy_in_jail_stage_2:
    "bg handyinjail_15"
    pause 0.15
    "bg handyinjail_17"
    pause 0.05
    "bg handyinjail_18"
    pause 0.1
    "bg handyinjail_16"
    pause 0.1
    "bg handyinjail_15"
    pause 0.15
    "bg handyinjail_17"
    pause 0.05
    "bg handyinjail_18"
    pause 0.1
    "bg handyinjail_16"
    pause 0.1
    repeat

####################
## Stage 3
label lbl_handy_in_jail_3:
    scene img_handy_in_jail_stage_3
    #$ handy_in_jail_counter += 1
    #show bg handyinjail_15
    #$ renpy.pause(0.1,hard=True)
    #show bg handyinjail_17
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.1,hard=True)
    #show bg handyinjail_15
    #$ renpy.pause(0.1,hard=True)
    #show bg handyinjail_17
    #$ renpy.pause(0.05,hard=True)
    #show bg handyinjail_16
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and handy_in_jail_counter == 24:
    #    jump lbl_handy_in_jail_cum
    #else:
    #    jump lbl_handy_in_jail_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_handy_in_jail_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_handy_in_jail_3

image img_handy_in_jail_stage_3:
    "bg handyinjail_15"
    pause 0.1
    "bg handyinjail_17"
    pause 0.05
    "bg handyinjail_16"
    pause 0.1
    "bg handyinjail_15"
    pause 0.1
    "bg handyinjail_17"
    pause 0.05
    "bg handyinjail_16"
    pause 0.1
    repeat

####################
## BJ Cum Menu

label lbl_handy_in_jail_cum:
    jump lbl_handy_in_jail_cum_menu

label lbl_handy_in_jail_cum_menu:

    #scene bg handyinjail_15
    call screen scr_handy_in_jail_cum_menu

screen scr_handy_in_jail_cum_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_handy_in_jail_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_handy_in_jail_cum_1")

label lbl_handy_in_jail_cum_1:
    scene bg handyinjail_23_0
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_1
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_2
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_3
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_4
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_5
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_6
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_7
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_8
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_9
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_10
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_11
    $ renpy.pause(0.3,hard=True)
    show bg handyinjail_23_12
    $ renpy.pause()
    show bg handyinjail_24
    sis "There we go. That should do it"
    show bg handyinjail_25
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg handyinjail_26
    with dissolve
    $ renpy.pause(0.5,hard=True)
    pov "Ahh.. that feels a ton better..."
    show bg handyinjail_27
    with hpunch
    mina "ARE-"
    mina "YOU-"
    show bg jailhouse_2
    show min angry_talk at right
    with hpunch
    mina "KIDDING ME?!"
    show bg jailhouse_3
    with hpunch
    mina "PAUL?!"
    show min angry at right
    pau "What the hell did you expect me to do from all the way over here?"
    show min angry_talk at right
    mina "This cell is a fucking mess. The floor, and those troublemakers."
    show min angry at right
    if winc == 0:
        pau "Aren't those two [sisrole]s?"
    else:
        pau "Aren't those two twins?"
    show min bored_talk at right
    mina "From their IDs, it does seem so..."
    show min bored at right
    pau "Yikes... that's... so... soo wrong..."
    show min bored_talk at right
    mina "You don't have to tell me twice. I'll give them the benefit of the doubt, they are both extremely intoxicated."
    show min shocked at right
    if winc == 0:
        pau "Are you going to tell their [mumrole] about this, Mina?"
    else:
        pau "Are you going to tell their mother about this, Mina?"
    show min bored_talk at right
    mina "{i}*Sigh*{/i} Speaking of..."
    hide min bored_talk
    show mumc angry_talk at Position(xpos=1300)
    show min shocked at right
    with hpunch
    mum "YOU TWO ARE IN SOO MUCH TROUB-"
    show mumc angry at Position(xpos=1300)
    show min angry at right
    if winc == 0:
        sis "Mom!"
        pov "Mommy!"
    else:
        sis "[missus]!"
        pov "[missus]~!"
    mum "..."
    show mumc angry_talk at Position(xpos=1300)
    mum "WHAT IS GOING ON HERE?!"
    if winc == 0:
        mum "[sister]! What are you doing to your [povsisrole]?!"
    else:
        mum "[sister]! What are you doing to your brother?!"
    show mumc angry at Position(xpos=1300)
    show min confused at right
    sis "Well, it all started when he found out that I'm a sex toy tester."
    sis "And then we got drunk at the club next door."
    if winc == 0:
        sis "Then this kind lady, who by the way, [missus]. Is not a prostitute, my mistake. She took us here."
    else:
        sis "Then this kind lady, who by the way, Mom. Is not a prostitute, my mistake. She took us here."
    sis "I stole the keys, put it on [povname]'s dick only because I thought it'd be funny and it got stuck."
    sis "And well... he made a messy."
    sis "..."
    show sis sad_talk flip at Position(xpos=600)
    with dissolve
    show pov shocked at left
    with dissolve
    sis "It's his fault, it's all [povname]'s fault! It was his idea, the whole thing!"
    show sis angry_talk flip at Position(xpos=600)
    sis "If he wasn't snooping around the adult store in the first place, this whole thing wouldn't have happened!"

    jump lbl_sibling_jail_time_4

label lbl_sibling_jail_time_3:
    show bg siblingjailtime_22
    sis "Fiiine! You're such a party pooper. Should've had another shot before we left the club."
    show bg siblingjailtime_23
    pov "You aaactually think that- tha- that prostitute would've let us have... another onnnne?"
    show bg siblingjailtime_24
    sis "You're right, it would've been rude to show off."
    show bg siblingjailtime_25
    sis "Well... I guess these are useless."
    show bg siblingjailtime_26
    with hpunch
    mina "HEY! WHAT THE HELL DO YOU THINK YOU'RE DOING?!"

    scene bg jailhouse_2
    show min angry_talk at right
    mina "WHERE DID YOU GET THOSE KEYS?!"
    mina "ARE YOU FUCKING SERIOUS, PAUL?! WHERE ARE THE SPARE KEYS?!"
    show bg jailhouse_3
    show min angry at right
    pau "Those... are the spare keys."
    show min angry_talk at right
    mina "And what the fuck were you doing? You were supposed to keep an eye on these two."
    show min shocked_talk at right
    mina "Is that a nudie mag I see through the window?!"
    show min bored_talk at right
    mina "For God's sakes, Paul."
    show min angry_talk at right
    mina "Gimme those fucking keys, you two or you'll get into extra trouble!"
    show min angry at right
    sis "Nuh-uh! Finders keepers!"
    show min angry_talk at right
    mina "You both are lucky your mother is coming to get you out of my hands."
    show min bored_talk at right
    mina "I should have just pretended I didn't notice them... I should just have pretended..."
    show min confused at right
    if winc == 0:
        pau "Excuse me, Mina? I believe their [mumrole] is here-"
    else:
        pau "Excuse me, Mina? I believe their mother is here-"
    hide min confused
    show mumc angry_talk at Position(xpos=1300)
    show min shocked at right
    mum "YOU TWO ARE IN SOO MUCH TROUBLE!"
    show mumc angry at Position(xpos=1300)
    show sis neutral_talk flip at Position(xpos=600)
    with dissolve
    show pov neutral at left
    with dissolve
    if winc == 0:
        sis "[missus]!"
        show sis neutral flip at Position(xpos=600)
        show pov neutral_talk at left
        pov "[missus]~!"
    else:
        sis "Mom!"
        show sis neutral flip at Position(xpos=600)
        show pov neutral_talk at left
        pov "Mommy!"
    show mumc angry_talk at Position(xpos=1300)
    show min bored at right
    show pov embarrassed at left
    mum "What happened here?!"
    show mumc angry at Position(xpos=1300)
    show sis embarrassed_talk flip at Position(xpos=600)
    sis "Well, it all started when he found out that I'm a sex toy tester."
    show pov smirk at left
    sis "And then we got drunk at the club next door."
    show sis sad_talk flip at Position(xpos=600)
    show pov sad at left
    if winc == 0:
        sis "Then this kind lady, who by the way, [missus]. Is not a prostitute, my mistake. She took us here."
    else:
        sis "Then this kind lady, who by the way, Mom. Is not a prostitute, my mistake. She took us here."
    show sis sad flip at Position(xpos=600)
    sis "..."
    show sis neutral_talk flip at Position(xpos=600)
    show pov neutral at left
    sis "The end!"
    show sis neutral flip at Position(xpos=600)
    sis "..."
    show sis sad_talk flip at Position(xpos=600)
    show pov shocked at left
    sis "It's his fault, it's all [povname]'s fault! It was his idea, the whole thing!"
    show sis angry_talk flip at Position(xpos=600)
    sis "If he wasn't snooping around the adult store in the first place, this whole thing wouldn't have happened!"

    jump lbl_sibling_jail_time_4

label lbl_sibling_jail_time_4:

    menu:
        "Blame [sister]":
            if sister_points >= 3:
                $ sister_points -= 3
            else:
                $ sister_points = 0
            $ renpy.notify("Your relationship with [sister] has decreased by 3")
            show sis angry flip at Position(xpos=600)
            show pov confused_talk at left
            pov "Thaaaat! Is not entirely corr-corr- uh- right!"
            show pov shocked_talk at left
            pov "It was [sister] that invited me to the bar!"
            show pov confused_talk at left
            pov "T-That guy... uh- Pau-"
            show min confused at right
            show sis bored_talk flip at Position(xpos=600)
            show pov confused at left
            sis "Steve."
            show sis angry flip at Position(xpos=600)
            show pov shocked_talk at left
            pov "Steve! He wouldn't eveeen serve me drinks!"
            show pov smirk_talk at left
            pov "But to [sister]! Nooooo worries!"
            show min confused_talk at right
            show sis shocked flip at Position(xpos=600)
            show pov bored at left
            mina "Steve, huh?"
            $ siblingjailtime_stevereveal = 1
        "Take the blame":
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has decreased by 3")
            else:
                $ renpy.notify("Your relationship with Mom has decreased by 3")
            show sis smirk flip at Position(xpos=600)
            show pov smirk_talk at left
            pov "Hehehe, woopsies. Definitely-lutely my fault."
            show pov sad_talk at left
            if winc == 0:
                pov "I shouldn't have gone into the naughty store. I'm sorry, [missus]."
            else:
                pov "I shouldn't have gone into the naughty store. I'm sorry, Mommy."
    show mumc angry_talk at Position(xpos=1300)
    show min shocked at right
    show sis sad flip at Position(xpos=600)
    show pov sad at left
    mum "That's it! You two, hand over the keys."
    show mumc sad_talk at Position(xpos=1300)
    show min bored at right
    mum "I'm so sorry about these two, ma'am. A-and the keys."
    show mumc embarrassed at Position(xpos=1300)
    show min bored_talk at right
    mina "That's... totally alright, ma'am. It happens all the time..."

    scene black
    with fade
    $ renpy.pause()
    "At home..."
    $ sister_path = 21

    jump lbl_twin_scolding
