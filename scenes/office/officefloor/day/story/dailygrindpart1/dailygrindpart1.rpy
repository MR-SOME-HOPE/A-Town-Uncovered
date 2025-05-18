label lbl_daily_grind_part1:
    default officejobs_complete = 0
    default officejobs_copymachine = 0
    default officejobs_coffeerun = 0
    default officejobs_emailproofread = 0
    default received_eloise_text = 0
    #[Office, afternoon - “Daily Grind Part 1”  - main_story =102]

    #-During the “Daily Grind” Scenes in the main story, the player and Mc will
    # have a short scene with some of the characters around the office before
    # playing the respective minigames of the day-

############################################################################################
    #-Mc enters the office only for his phone to vibrate indicating a text message.
    # Pulling up his phone, it shows it’s from Eloise-

    $ officejobs_complete = 0

    scene bg dailygrindpart1_1
    with fade
    $ renpy.pause()
    show bg dailygrindpart1_2
    $ renpy.pause()
    show bg dailygrindpart1_3
    $ renpy.pause()
    show bg dailygrindpart1_4
    $ renpy.pause()
    show bg dailygrindpart1_5
    $ renpy.pause()
    show bg dailygrindpart1_6
    $ renpy.pause()
    show bg dailygrindpart1_7
    $ renpy.pause()
    show bg dailygrindpart1_8
    $ renpy.pause()
    show bg dailygrindpart1_9
    $ renpy.pause()

    $ received_eloise_text = 1
    # elo "Hi, [povname]!"
    # elo "Looking good today!"
    # elo "I can see you via the cctv."
    # elo "I'm always watching"
    # elo "Remember that if you think about causing trouble~"
    # elo "Anyway, I got a lot on my agenda today"
    # elo "Busy busy"
    # elo "Next part of our tour will be on Thursday after work."
    # elo "See you then~"

    #-Mc puts his phone down-
############################################################################################

    scene bg officefloor_day
    with fade
    show pov smirk_talk at left
    with dissolve
    pov "Huh, guess the boss has to keep an eye on everything…"

    #-Manager appears behind the MC-
    show pov shocked at left
    show mrf bored_talk at right
    with dissolve
    mrf "Damn straight, kid."
    mrf "I have to do the occasional round of the floor to make sure all of you are working optimally and have everything you need to get you through the day."
    show pov bored at left
    mrf "Still, I’m impressed you managed to notice me with your back turned."
    show pov embarrassed_talk at left
    show mrf bored at right
    pov "O-Oh, Uh… I wasn’t actually talking to…"
    pov "N-Nevermind."
    show pov neutral_talk at left
    pov "Sorry if I’m late, I came here as soon as I could."
    show pov neutral at left
    show mrf neutral_talk at right
    mrf "It’s alright, [povname], I’ve been informed you attend the town’s community college and education is always important."
    show mrf smirk_talk at right
    mrf "The important thing is that you are here now and ready to work, right?"
    show pov neutral_talk at left
    show mrf smirk at right
    pov "Yes, sir!"
    show pov neutral at left
    show mrf smirk_talk at right
    mrf "Good! Talk to Corrine about what needs to be done today."
    mrf "I’m going to need you to come all week while we continue setting up the department."
    mrf "Things should slow down a little by next week and you’ll have a bit more freedom of schedule but the more you are here and showing interest and passion in your work, the better you’ll be rewarded."
    show pov embarrassed at left
    show mrf bored_talk at right
    mrf "Understood?"
    show pov neutral_talk at left
    show mrf bored at right
    pov "Crystal clear, Mr.Fistem, sir."
    show pov embarrassed at left
    show mrf neutral_talk at right
    mrf "At'ta boy!"
    hide mrf with dissolve

label lbl_daily_grind_part1_jobs_menu:
    menu:
        "Copy Machine" if not officejobs_copymachine:
            jump lbl_officejobs_copymachine

        "Coffee Run" if not officejobs_coffeerun:
            jump lbl_officejobs_coffeerun

        #"Email Proofreading" if not officejobs_emailproofread:
        #    jump lbl_officejobs_emailproofread


    #-Manager leaves the scene and player is free to interact with the office,
    # upon clicking on Corrine, a Menu of the available tasks will pop up. Player
    # only needs to do 2 of the available minigames in order to finish a work shift,
    # during the events of the main story, the player will be able to see a scene
    # in between the two minigames that showcases the office characters-

    #-MID MINIGAME SCENE-

label lbl_daily_grind_part1_jobs_midscene:
    #-Scene takes place as Mc is bringing a large pile of paperwork over to Jacob’s
    # Dad/Isaac-
    scene bg officefloor_day with fade
    show pov embarrassed_talk at left
    with dissolve
    pov "Uh, sir, I have some of the introductory reports that need a few notes from the floor supervisor before being submitted to the floor manager for review?"
    show pov embarrassed at left
    show jacdad confused_talk at right with dissolve
    jacdad "Ah, yes! Those must be the evaluative performance reports for our test group calls. I need to give them a final review and add in my thoughts."
    show pov embarrassed_talk at left
    show jacdad embarrassed at right
    pov "So you are passing out grades then, sir?"
    show pov embarrassed at left
    show jacdad embarrassed_talk at right
    isac "Please, [povname]. Just call me Isaac."
    show pov neutral at left
    show jacdad neutral_talk at right
    isac "We are coworkers now and you already make me feel old enough by just being my son’s friend working with me."
    isac "So feel free to just call me by my name when we are over here."
    show pov embarrassed_talk at left
    show jacdad neutral at right
    pov "Oh, well…"
    show pov neutral_talk at left
    pov "You got it, Isaac."
    show pov neutral at left
    show jacdad neutral_talk at right
    isac "Much better!"
    show pov confused at left
    show jacdad confused_talk at right
    isac "But more than grades, it’s mainly an evaluation of their customer service in simulated situations."
    show jacdad embarrassed_talk at right
    isac "Scenarios with angry callers, people who struggle with understanding technology and similar situations where the agent has to deescalate the situation and reach a satisfactory conclusion."
    show pov confused_talk at left
    show jacdad embarrassed at right
    pov "I thought you guys weren’t ready to accept calls yet. Who are you practicing with?"
    show pov shocked at left
    show jacdad embarrassed_talk at right
    isac "Oh, Corrine is giving us a hand and playing a few characters via a few scripts."
    isac "She is quite the actress and can get really into character."
    show pov embarrassed_talk at left
    show jacdad neutral at right
    pov "You don’t say?"

    #-Howie appears on the scene coming back from his break-

    show pov shocked at left
    show jacdad confused at Position(xpos=1600) with dissolve
    show how embarrassed_talk at Position(xpos=1800) with dissolve
    how "A-Afternoon, Sir… Afternoon, [povname]..."
    show pov embarrassed at left
    show jacdad neutral_talk at Position(xpos=1600)
    show how embarrassed at Position(xpos=1800)
    isac "Ah, Mr.Howard!"
    isac "Back from your break, then? Hope everything was good!"
    show pov confused at left
    show jacdad confused at Position(xpos=1600)
    show how embarrassed_talk at Position(xpos=1800)
    how "Y-Yeah, just um…"
    how "T-T-Took some air…"
    show jacdad embarrassed_talk at Position(xpos=1600)
    show how embarrassed at Position(xpos=1800)
    isac "Good, good!"
    isac "Say, [povname] just got me the evaluations from our last test group calls. How about we go over yours now?"
    show jacdad neutral at Position(xpos=1600)
    show how embarrassed_talk at Position(xpos=1800)
    how "U-U_um, I-I-I don’t think t-that’s-"
    show pov embarrassed at left
    show jacdad neutral_talk at Position(xpos=1600)
    show how embarrassed at Position(xpos=1800)
    isac "It’s alright, Mr. Howard, the evaluation is to help you improve so it’s natural if things are still not perfect."
    isac "Let’s see your results now."
    show jacdad neutral at Position(xpos=1600)
    show how embarrassed_talk at Position(xpos=1800)
    how "I-I’d r-r-rather not-"
    show jacdad confused_talk at Position(xpos=1600)
    show how embarrassed at Position(xpos=1800)
    isac "Hmm… outstanding on ticket filing…"
    isac "Outstanding follow-up of problem and issue solving skill…"
    show pov confused at left
    show jacdad bored_talk at Position(xpos=1600)
    isac "…"
    show jacdad neutral_talk at Position(xpos=1600)
    isac "Well, everything looks great except for your “communication with client” grade…"
    show jacdad bored_talk at Position(xpos=1600)
    isac "In which you somehow managed to get a score below even your already low average."
    show jacdad confused_talk at Position(xpos=1600)
    show how sad at Position(xpos=1800)
    isac "Did you happen to get the angry customer script?"
    show jacdad embarrassed_talk at Position(xpos=1600)
    isac "That can be a difficult call for anyone. Don’t feel too bad if it was too much for you."
    show pov embarrassed at left
    show jacdad embarrassed at Position(xpos=1600)
    show how embarrassed_talk at Position(xpos=1800)
    how "I-I… I um…"
    how "I-I didn’t g-g-get… The a-angry one…"
    show pov confused at left
    show jacdad embarrassed_talk at Position(xpos=1600)
    show how embarrassed at Position(xpos=1800)
    isac "Oh? Which one did you get, then?"
    show pov shocked at left
    show jacdad confused at Position(xpos=1600)
    show how embarrassed_talk at Position(xpos=1800)
    how "F-F-Flirty…"
    show jacdad shocked_talk at Position(xpos=1600)
    show how embarrassed at Position(xpos=1800)
    isac "Oh…"
    show jacdad embarrassed_talk at Position(xpos=1600)
    isac "You got the “Flirty looking for a deal or free maintenance work” one, eh?"
    isac "Yeah, you guys specifically seem to keep having issues with that one…"

    #-Bradley also shows up in the scene also coming back from his break-
    show pov shocked at left
    show bra neutral_talk at Position(xpos=1000) with dissolve
    show jacdad embarrassed at Position(xpos=1700) with dissolve
    show how  at Position(xpos=1800)
    bra "Good Afternoon, sir!"
    show bra smirk_talk at Position(xpos=1000)
    bra "Howie… Intern…"
    bra "Say, I couldn’t help but notice those files with you, sir."
    show pov confused at left
    show bra bored_talk at Position(xpos=1000)
    bra "Would they happen to be our recent evaluations? I’m more than ready to be graded, and I assure you that you’ll find nothing but an outstanding performance."
    show bra neutral_talk at Position(xpos=1000)
    bra "I even got the non-tech savvy customer call and handled it quite well, if I do say so myself."
    show bra bored at Position(xpos=1000)
    show jacdad bored_talk at Position(xpos=1700)
    isac "Oh, hello Mr. Bradley."
    isac "Yes, these are the latest evaluations. I was just going over Mr. Howard’s before you arrived."
    show bra smirk_talk at Position(xpos=1000)
    bra "Heh, did he faint during the communication test again?"
    show bra neutral at Position(xpos=1000)
    bra "Must be bad luck if he got the angry customer call again."
    show bra shocked at Position(xpos=1000)
    show jacdad bored_talk at Position(xpos=1700)
    isac "No, he got the “Flirty” one this time."
    show bra shocked_talk at Position(xpos=1000)
    show jacdad neutral at Position(xpos=1700)
    bra "Ah…"
    show bra smirk_talk at Position(xpos=1000)
    bra "No worries, man. It happens to the best of us, it’s alright…"
    show pov confused_talk at left
    show bra confused at Position(xpos=1000)
    pov "Well, that’s a complete change of attitude in just five seconds."
    pov "What gives?"
    show pov confused at left
    show bra smirk_talk at Position(xpos=1000)
    bra "That’s because you don’t understand the whole context, Intern. Which is not surprising."
    show pov shocked at left
    show bra smirk at Position(xpos=1000)
    show jacdad angry_talk at Position(xpos=1700)
    show how shocked at Position(xpos=1800)
    isac "No need for the added comment, Mr. Bradley!"
    show pov confused at left
    show jacdad embarrassed_talk at Position(xpos=1700)
    isac "But yes, [povname], Corrine is…"
    isac "Well… Let’s just say she is exceptionally good at playing the role of the flirty customer."
    show jacdad confused_talk at Position(xpos=1700)
    isac "Like… Really really good…"
    show bra smirk_talk at Position(xpos=1000)
    show jacdad confused at Position(xpos=1700)
    bra "Really damn good, you mean…"
    show pov shocked at left
    show bra neutral at Position(xpos=1000)
    show jacdad shocked at Position(xpos=1700)
    show how shocked_talk at Position(xpos=1800)
    how "A-A S-Succubus…"
    show jacdad embarrassed_talk at Position(xpos=1700)
    show how shocked at Position(xpos=1800)
    isac "And so the guys have a bit of trouble when dealing with that particular script."
    show pov confused_talk at left
    show jacdad embarrassed at Position(xpos=1700)
    pov "You as well, Isaac?"
    show bra smirk at Position(xpos=1000)
    show jacdad shocked_talk at Position(xpos=1700)
    show how embarrassed at Position(xpos=1800)
    isac "Mr. Bradley!"
    isac "Let’s evaluate you by your cubicle next!"
    show bra smirk_talk at Position(xpos=1000)
    show jacdad bored at Position(xpos=1700)
    bra "Yes, sir!"

    #-Isaac and Bradley leave the scene-
    show pov shocked_talk at left
    hide bra
    hide jacdad
    with dissolve
    show how  at Position(xpos=1800)
    pov "I guess that’s my answer…"

    #-Corrine enters the scene with a friendly look-
    show pov shocked at left
    show how shocked at Position(xpos=1800)
    show cor neutral_talk at Position(xpos=1400) with dissolve
    cor "Hey [povname], hey Howie!"
    cor "Working hard or hardly wor-"
    show cor confused at Position(xpos=1400)
    show how shocked_talk at Position(xpos=1800)
    how "EEEK!"

    #-Howie speeds out and leaves the scene-
    show pov embarrassed at left
    show cor shocked_talk at Position(xpos=1400)
    hide how with dissolve
    cor "-king…"
    cor "Geez, I know it’s a corny office joke but I didn’t think it was that bad…"
    show pov embarrassed_talk at left
    show cor embarrassed at Position(xpos=1400)
    pov "Ahahaha…"
    hide cor
    with dissolve

    jump lbl_daily_grind_part1_jobs_menu

label lbl_daily_grind_part1_jobs_end:
    #-MID MINIGAME SCENE END-

    #-Once the player has done the second minigame his shift is over and he has
    # a few closing words with the manager-
    scene bg officefloor_day with fade
    show pov neutral at left
    show mrf smirk_talk at right
    with dissolve
    mrf "Alright kid, all done and ready to clock out?"
    show pov neutral_talk at left
    show mrf smirk at right
    pov "Ready as I’ll ever be, I guess."
    show pov neutral at left
    show mrf neutral_talk at right
    mrf "Nothing sweeter than getting out of the office after a long day of work."
    mrf "Keep it up, kid. You’ll get the hang of everything there is to this whole office thing eventually."
    show pov embarrassed at left
    show mrf smirk_talk at right
    mrf "Get home safe, and see you tomorrow."
    show pov neutral_talk at left
    show mrf smirk at right
    pov "See you tomorrow, sir!"
    show pov shocked at left
    show mrf bored_talk at right
    mrf "Oh, and if you see Corrine on the way down…"
    show pov embarrassed_talk at left
    show mrf bored at right
    pov "I’ll tell her you want to see her in your office."
    show pov embarrassed at left
    show mrf smirk_talk at right
    mrf "At'ta boy, already getting a hang of how things work here!"
    mrf "Alright, now get out here and take it easy the rest of the night."
    show pov neutral_talk at left
    show mrf smirk at right
    pov "Will do!"

    $ officejobs_complete = 0
    $ officejobs_copymachine = 0
    $ officejobs_coffeerun = 0
    $ officejobs_emailproofread = 0

    $ gtime = 2
    $ main_story = 101.9

    scene black with fade
    jump lbl_elevator_night

    #=SCENE ENDS=
