## Breaking in Fort Rebuild ##
label lbl_breaking_in_fort_rebuild:

    scene bg breakinginfortrebuild_1
    with fade
    $ renpy.pause()
    show bg breakinginfortrebuild_4
    pov "Calmed down a bit?"
    show bg breakinginfortrebuild_2
    sis "Y-Yeah... My heart's just racing. I have no idea why."
    show bg breakinginfortrebuild_4
    pov "Do you like how it turned out?"
    show bg breakinginfortrebuild_3
    pov "I know it's not as good as the other fort but-"
    show bg breakinginfortrebuild_5
    with hpunch
    $ renpy.pause(1,hard=True)
    show bg breakinginfortrebuild_6
    sis "Shut up."
    show bg breakinginfortrebuild_7
    sis "It's perfect. You did an amazing job with it. All of it."
    show bg breakinginfortrebuild_8
    pov "I tried to get it as close to what it originally was."
    pov "Something that felt familiar."
    show bg breakinginfortrebuild_9
    sis "I love it."
    sis "I absolutely freakin' love it, [povname]."
    show bg breakinginfortrebuild_8
    pov "It was a hassle getting all these boxes together so I'm happy to know you like it."
    show bg breakinginfortrebuild_10
    sis "Why? Can't imagine it being that hard. Stores have plenty of boxes in the back."
    show bg breakinginfortrebuild_11
    pov "That's what I thought as well."
    show bg breakinginfortrebuild_12
    sis "Hehehe."
    show bg breakinginfortrebuild_13
    pov "You're blushing, [sister]."
    show bg breakinginfortrebuild_14
    sis "N-No, I'm not."
    sis "I can't blush..."
    show bg breakinginfortrebuild_15
    pov "I got you to blush!"
    show bg breakinginfortrebuild_14
    sis "W-Way to ruin the mood, you jackass!"
    show bg breakinginfortrebuild_15
    pov "I'm never letting this go, Oh my God!"
    pov "I made [sister] blush, like a schoolgirl with a crush!"
    pov "Hahahaha! You're just one adorable little lady, aren't cha?"
    show bg breakinginfortrebuild_14
    sis "Shut up, shut up, shut up!"
    sis "It's your fault for saying such sweet shit like that and doing such sweet shit like this, okay?!"
    show bg breakinginfortrebuild_16
    sis "Any girl would be as red as a tomato if you did this for them!"
    show bg breakinginfortrebuild_3
    pov "Hehehehe, well..."
    show bg breakinginfortrebuild_17
    pov "{i}*Clears throat*{/i}"
    show bg breakinginfortrebuild_18
    pov "W-Well, you should know that I wouldn't do something like this for just any girl, you know?"
    show bg breakinginfortrebuild_19
    pov "None of them deserve it as much as you, either way."
    show bg breakinginfortrebuild_20
    sis "Oh! Shut up! You're so damn corny."
    show bg breakinginfortrebuild_21
    sis "You... You...!"
    show bg breakinginfortrebuild_22
    pov "Oh my God, you're too flustered to even come up with something!"
    show bg breakinginfortrebuild_14
    sis "Ugh.. whatever... dick."
    show bg breakinginfortrebuild_23
    pov "Hehehe."
    show bg breakinginfortrebuild_24
    pov "I might be making fun of you, but I meant what I say."
    show bg breakinginfortrebuild_25
    sis "..."
    show bg breakinginfortrebuild_24
    pov "Also..."
    pov "You're pretty cute when you blush, you know?"
    show bg breakinginfortrebuild_25
    sis "..."
    show bg breakinginfortrebuild_26
    if winc == 1:
        sis "Mom's not home... right?"
    else:
        sis "[missus]'s not home... right?"
    show bg breakinginfortrebuild_27
    pov "She- uh.. went to drop Effie off-"
    show bg breakinginfortrebuild_28
    sis "Awesome."
    show bg breakinginfortrebuild_5
    with hpunch
    $ renpy.pause()
    show bg breakinginfortrebuild_29
    $ renpy.pause()
    show bg breakinginfortrebuild_30
    $ renpy.pause(2,hard=True)
    show bg breakinginfortrebuild_31
    $ renpy.pause(1,hard=True)
    show bg breakinginfortrebuild_32
    $ renpy.pause(1,hard=True)
    show bg breakinginfortrebuild_33
    pov "H-Hey!"
    pov "[sister], what are you doing?"
    show bg breakinginfortrebuild_34
    sis "D-Do you not want to?"

    menu:
        "Come back up here.":
            show bg breakinginfortrebuild_35
            pov "Come back up here."
            show bg breakinginfortrebuild_36
            if winc == 1:
                sis "Are you sure, baby-bro?"
            else:
                sis "Are you sure, [povname]?"
            show bg breakinginfortrebuild_37
            pov "Y'know, you don't have t-"
            show bg breakinginfortrebuild_38
            sis "I... I want to be close to you right now..."
            sis "Perhaps not the whole way yet, but..."
            sis "I want to at least do this right now."
            ###################################################################
        "I'll keep quiet.":
            pass
    show bg breakinginfortrebuild_39
    pov "I'll keep quiet."
    jump lbl_breakinginfortrebuild_bj_pre

####################
## BJ
label lbl_breakinginfortrebuild_bj_revisit:
    scene black
    with fade
    $ renpy.pause()
    "Down in Twin Fortress..."
    scene bg breakinginfortrebuild_bj_5
    with fade

    jump lbl_breakinginfortrebuild_bj_0

label lbl_breakinginfortrebuild_bj_pre:
    show bg breakinginfortrebuild_40
    if winc == 1:
        sis "Mhmm, that's what I thought, baby-bro."
    else:
        sis "Mhmm, that's what I thought, [povname]."

    scene bg breakinginfortrebuild_bj_1
    with fade
    sis "W-Woah... It's-"
    sis "It's actually bigger than I remembered."
    sis "Like it feels really thick."
    pov "Sorry, I'm a grower, not a shower."
    show bg breakinginfortrebuild_bj_23
    sis "Tch- hashtag humble brag."
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_4
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_4
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    sis "It's not fair, you know?"
    show bg breakinginfortrebuild_bj_1
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_2
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_4
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_3
    $ renpy.pause(0.4,hard=True)
    show bg breakinginfortrebuild_bj_23
    sis "When did you become this charming?"
    sis "How is a girl not supposed to..."
    show bg breakinginfortrebuild_bj_24
    sis "To-"

label lbl_breakinginfortrebuild_bj_0:
    #$ breakinginfortrebuild_counter = 0
    jump lbl_breakinginfortrebuild_bj_1

####################
## BJ Stage 1
label lbl_breakinginfortrebuild_bj_1:
    scene img_breakinginfortrebuild_bj_stage_1
    #$ breakinginfortrebuild_counter += 1
    #show bg breakinginfortrebuild_bj_5
    #$ renpy.pause(0.3,hard=True)
    #show bg breakinginfortrebuild_bj_6
    #$ renpy.pause(0.1,hard=True)
    #show bg breakinginfortrebuild_bj_8
    #$ renpy.pause(0.1,hard=True)
    #show bg breakinginfortrebuild_bj_7
    #$ renpy.pause(0.3,hard=True)
    #show bg breakinginfortrebuild_bj_6
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and breakinginfortrebuild_counter == 4:
    #    jump lbl_breakinginfortrebuild_bj_cum
    #elif skill_sta <= 14 and breakinginfortrebuild_counter == 6:
    #    jump lbl_breakinginfortrebuild_bj_2
    #elif skill_sta <= 20 and breakinginfortrebuild_counter == 8:
    #    jump lbl_breakinginfortrebuild_bj_2
    #else:
    #    jump lbl_breakinginfortrebuild_bj_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_breakinginfortrebuild_bj_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_breakinginfortrebuild_bj_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_breakinginfortrebuild_bj_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_breakinginfortrebuild_bj_1

image img_breakinginfortrebuild_bj_stage_1:
    "bg breakinginfortrebuild_bj_5"
    pause 0.3
    "bg breakinginfortrebuild_bj_6"
    pause 0.1
    "bg breakinginfortrebuild_bj_8"
    pause 0.1
    "bg breakinginfortrebuild_bj_7"
    pause 0.3
    "bg breakinginfortrebuild_bj_6"
    pause 0.3
    repeat

####################
## BJ Stage 2
label lbl_breakinginfortrebuild_bj_2:
    scene img_breakinginfortrebuild_bj_stage_2
    #$ breakinginfortrebuild_counter += 1
    #show bg breakinginfortrebuild_bj_9
    #$ renpy.pause(0.3,hard=True)
    #show bg breakinginfortrebuild_bj_11
    #$ renpy.pause(0.1,hard=True)
    #show bg breakinginfortrebuild_bj_10
    #$ renpy.pause(0.2,hard=True)
    #show bg breakinginfortrebuild_bj_12
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and breakinginfortrebuild_counter == 14:
    #    jump lbl_breakinginfortrebuild_bj_cum
    #elif skill_sta <= 20 and breakinginfortrebuild_counter == 16:
    #    jump lbl_breakinginfortrebuild_bj_3
    #else:
    #    jump lbl_breakinginfortrebuild_bj_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_breakinginfortrebuild_bj_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_breakinginfortrebuild_bj_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_breakinginfortrebuild_bj_2

image img_breakinginfortrebuild_bj_stage_2:
    "bg breakinginfortrebuild_bj_9"
    pause 0.3
    "bg breakinginfortrebuild_bj_11"
    pause 0.1
    "bg breakinginfortrebuild_bj_10"
    pause 0.2
    "bg breakinginfortrebuild_bj_12"
    pause 0.2
    repeat
####################
## BJ Stage 3
label lbl_breakinginfortrebuild_bj_3:
    scene img_breakinginfortrebuild_bj_stage_3
    #$ breakinginfortrebuild_counter += 1
    #show bg breakinginfortrebuild_bj_13
    #$ renpy.pause(0.2,hard=True)
    #show bg breakinginfortrebuild_bj_14
    #$ renpy.pause(0.1,hard=True)
    #show bg breakinginfortrebuild_bj_15
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and breakinginfortrebuild_counter == 24:
    #    jump lbl_breakinginfortrebuild_bj_cum
    #else:
    #    jump lbl_breakinginfortrebuild_bj_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_breakinginfortrebuild_bj_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_breakinginfortrebuild_bj_3

image img_breakinginfortrebuild_bj_stage_3:
    "bg breakinginfortrebuild_bj_13"
    pause 0.2
    "bg breakinginfortrebuild_bj_14"
    pause 0.1
    "bg breakinginfortrebuild_bj_15"
    pause 0.2
    repeat
####################
## BJ Cum
label lbl_breakinginfortrebuild_bj_cum:
    if sister_points <= 6:
        jump lbl_breakinginfortrebuild_bj_cum_2
    else:
        jump lbl_breakinginfortrebuild_bj_cum_3

label lbl_breakinginfortrebuild_bj_cum_2:

    #scene bg breakinginfortrebuild_bj_14
    call screen scr_breakinginfortrebuild_bj_cum_2

screen scr_breakinginfortrebuild_bj_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_breakinginfortrebuild_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_breakinginfortrebuild_bj_cumchoice")

label lbl_breakinginfortrebuild_bj_cum_3:

    #scene bg breakinginfortrebuild_bj_14
    call screen scr_breakinginfortrebuild_bj_cum_3

screen scr_breakinginfortrebuild_bj_cum_3():
    #imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_breakinginfortrebuild_bj_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_breakinginfortrebuild_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_breakinginfortrebuild_bj_cumchoice")

label lbl_breakinginfortrebuild_bj_cumchoice:

    menu:
        "Cum inside mouth":
            jump lbl_breakinginfortrebuild_bj_cumin
        "Cum outside on face":
            jump lbl_breakinginfortrebuild_bj_cumout

####################
## BJ Cum in

label lbl_breakinginfortrebuild_bj_cumin:
    scene bg breakinginfortrebuild_bj_14
    $ renpy.pause(0.3,hard=True)
    show bg breakinginfortrebuild_bj_14_1
    $ renpy.pause(1,hard=True)
    show bg breakinginfortrebuild_bj_14_2
    $ renpy.pause(0.5,hard=True)
    show bg breakinginfortrebuild_bj_14_3
    $ renpy.pause()
    show bg breakinginfortrebuild_bj_16
    $ renpy.pause(0.7,hard=True)
    show bg breakinginfortrebuild_bj_17
    $ renpy.pause(0.7,hard=True)
    show bg breakinginfortrebuild_bj_18
    $ renpy.pause(0.7,hard=True)
    show bg breakinginfortrebuild_bj_19
    $ renpy.pause()
    sis "Well..."
    sis "I ain't having lunch today..."
    show bg breakinginfortrebuild_bj_20
    sis "Fuck-"
    show bg breakinginfortrebuild_bj_21
    sis "Seriously dude, it's way too much cum for a single guy."
    pov "It's a gift."
    show bg breakinginfortrebuild_bj_22
    sis "No kidding."
    sis "What's the secret? Vitamin tablets? Iron?"
    sis "Are you always on... edge?"
    pov "It keeps you on edge, doesn't it?"
    sis "..."
    show bg breakinginfortrebuild_bj_21
    sis "Fuck... that actually turns me on."
    sis "Mmmm... Can you pass me a towel or something to clean up?"

    if sister_hscenerevisit == 1:
        $ sister_hscenerevisit = 0
        scene black
        with fade
        "Shortly after..."
        $ gtime += 1
        if gtime <= 1:
            jump lbl_mybasement_day_setup
        else:
            jump lbl_mybasement_night_setup
    else:
        pass

    jump lbl_breakinginfortrebuild_2

####################
## BJ Cum out

label lbl_breakinginfortrebuild_bj_cumout:
    scene bg breakinginfortrebuild_bj_25_0
    $ renpy.pause(0.5,hard=True)
    show bg breakinginfortrebuild_bj_25_1
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_2
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_3
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_4
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_5
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_6
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_7
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_8
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_9
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_10
    $ renpy.pause(0.2,hard=True)
    show bg breakinginfortrebuild_bj_25_11
    $ renpy.pause(0.5,hard=True)
    sis "Ah!"
    sis "Crappers!"
    show bg breakinginfortrebuild_bj_25_12
    sis "Damn, dude-!"
    sis "My fuckin' nose!"
    show bg breakinginfortrebuild_bj_25_11
    sis "I accidentally snorted your crack cum!"
    pov "Sounds like Squideward is blowing me down there."
    show bg breakinginfortrebuild_bj_25_12
    sis "Fuck off."
    show bg breakinginfortrebuild_bj_25_11
    sis "How does one guy cum so much?!"
    sis "I should have swallowed."
    pov "Maybe we should retry it."
    show bg breakinginfortrebuild_bj_25_12
    sis "Again, fuck off."
    show bg breakinginfortrebuild_bj_25_11
    sis "Gaaghh... Can you pass me a towel or something to clean up?"

    if sister_hscenerevisit == 1:
        $ sister_hscenerevisit = 0
        scene black
        with fade
        "Shortly after..."
        $ gtime += 1
        if gtime <= 1:
            jump lbl_mybasement_day_setup
        else:
            jump lbl_mybasement_night_setup
    else:
        pass

    jump lbl_breakinginfortrebuild_2

##################################################################################
## BOOB JOB
    pov "H-holy shit, [sister]..."
    "she pulls the shaft out her mouth."
    sis "Hehehe~ You like that?"
    pov "Fuck- your mouth feels so fucking good."
    sis "Mmm.. Moan for me, [povname]."
    sis "I want to hear how much you like it."
    "She continues sucking for a while"
    pov "Mmmm.. oh, shit.."
    pov "H- How..."
    pov "How are you so good at this?"
    "She then takes it out of her mouth."
    sis "Tons of practice with toys."
    "She takes off her top but not her bra."
    sis "Want to see what else I can do?"
    "She unhooks her bra and wraps her breasts around the shaft moving them up and down with a proud smile on her face."
    pov "I've said it once... a-and I'll say it again."
    pov "Your boobs are amazing."
    pov "O-Oh, man..."
    sis "You may be able to make me blush like a schoolgirl..."
    sis "But I can make you moan and cum like a bitch."
    "She starts to lick and kiss the head, going faster and faster, bobbing her head back and forth to suck on the head as her breasts massage the shaf"
    pov "Oh... Oh God, [sister]."
    pov "I- I'm-"

    menu:
        "Cum in her mouth":
            "You cum in her mouth and she swallows all of it but some drips out."
        "Cum on her face":
            "You cum all over her face."
            sis "Ah!"
            sis "Crappers!"
            sis "Damn, dude-!"
            sis "My fuckin' nose!"
            sis "I accidentally snorted your crack cum!"
            pov "Sounds like Squideward is blowing me down there."
            sis "Fuck off."
            sis "How does one guy cum so much?!"
            sis "I should have swallowed."
            pov "Maybe we should retry it."
            sis "Again, fuck off."
            sis "Gaaghh... Can you pass me a towel or something to clean up?"

#############################################################################
label lbl_breakinginfortrebuild_2:

    scene black
    with fade
    $ renpy.pause()
    "After cleaning yourselves up..."

    scene bg breakinginfortrebuild_41
    with fade
    $ renpy.pause()
    pov "{i}*Inhale*{/i}"
    sis "{i}*Exhale*{/i}"
    show bg breakinginfortrebuild_42
    pov "Wow..."
    show bg breakinginfortrebuild_43
    sis "Hehehe, still got it."
    show bg breakinginfortrebuild_44
    pov "No argument there. You're still a little sticky though, I can smell it."
    show bg breakinginfortrebuild_45
    sis "I know you love it. It's like a trophy for your big-big ego."
    show bg breakinginfortrebuild_41
    pov "..."
    show bg breakinginfortrebuild_42
    pov "I can't believe we just did that."
    if siblingjailtime_hj == 1:
        show bg breakinginfortrebuild_43
        sis "And sober."
        show bg breakinginfortrebuild_44
        pov "I vaguely remember that night..."
        show bg breakinginfortrebuild_45
        sis "You came- a- lot."
        show bg breakinginfortrebuild_46
        pov "W-why... did you give me a handjob again?"
        show bg breakinginfortrebuild_47
        sis "..."
        show bg breakinginfortrebuild_48
        sis "That's... not important."
        show bg breakinginfortrebuild_49
        sis "Huh- you really must've been out of it."
    show bg breakinginfortrebuild_41
    sis "..."
    show bg breakinginfortrebuild_50
    sis "Are we- bad?"
    sis "Like... messed up?"

    menu:
        "Very.":
            show bg breakinginfortrebuild_51
            pov "Very messed up."
            pov "Very fucked up."
            pov "But..."
            pov "I- don't care."
            show bg breakinginfortrebuild_52
            sis "You don't?"
            show bg breakinginfortrebuild_53
            pov "It actually- turns me on more than ever."
            show bg breakinginfortrebuild_54
            pov "Because I see you as like-"
            pov "Forgive me for being cheesy but I feel like you're my bestest, closest friend."
            pov "I've literally known you since... even before birth."
            pov "That's actually frikkin weird to think about."
            show bg breakinginfortrebuild_55
            sis "Can I tell you a secret?"
            sis "I've thought about you... like so much."
            show bg breakinginfortrebuild_56
            sis "In... all ways."
            show bg breakinginfortrebuild_57
            sis "..."
            show bg breakinginfortrebuild_56
            sis "There's definitely something wrong with us but I don't care, [povname]."
            show bg breakinginfortrebuild_55
            sis "I love you and that's all that matters."
            show bg breakinginfortrebuild_54
            pov "I love you too, [sister]. So, so, much."
        "I don't think so.":
            show bg breakinginfortrebuild_51
            pov "I don't think so."
            pov "We're both consenting adults who know what we're doing.. right?"
            show bg breakinginfortrebuild_54
            pov "We just... happen to be siblings..."
            show bg breakinginfortrebuild_57
            pov "..."
            show bg breakinginfortrebuild_55
            sis "Uh- yeah.."
            sis "It's just some... unusual coincidence with the universe."
            if winc == 1:
                sis "If we weren't related. We'd still be fucking each other."
            show bg breakinginfortrebuild_56
            sis "Right?"
            show bg breakinginfortrebuild_53
            pov "I'd fuck you to the moon."
            show bg breakinginfortrebuild_58
            sis "That's the sweetest thing I've ever heard."
            show bg breakinginfortrebuild_53
            pov "Wanna fuck now?"
            show bg breakinginfortrebuild_58
            if winc == 1:
                sis "I like teasing you, bro-bro."
            else:
                sis "I like teasing you, [povname]."
            show bg breakinginfortrebuild_45
            sis "Let me have my fun."
            sis "Hehehe, I love you."
            show bg breakinginfortrebuild_44
            pov "I love you too, [sister]."
    show bg breakinginfortrebuild_41
    pov "..."
    show bg breakinginfortrebuild_46
    pov "Will you be coming back home?"
    show bg breakinginfortrebuild_47
    sis "..."
    show bg breakinginfortrebuild_48
    sis "I feel safe with you."
    sis "I think it's time to come home."
    sis "I have a home to come back to after all."
    show bg breakinginfortrebuild_55
    sis "The one you built for me."
    show bg breakinginfortrebuild_53
    pov "Welcome home, you cry baby."
    show bg breakinginfortrebuild_43
    sis "Thank you, you thick-dicked-meanie."

    scene black
    with fade
    $ renpy.pause()
    $ sister_path = 34

    jump lbl_mybasement_day_setup
