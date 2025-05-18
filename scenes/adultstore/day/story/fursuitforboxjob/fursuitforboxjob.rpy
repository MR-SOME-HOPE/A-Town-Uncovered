## Fursuit for Box Job ##
label lbl_fursuit_for_box_job:
    default fursuitforboxjob_attended = 0
    default fursuitforboxjob_times = 0
    default fursuitforboxjob_effort = 0
    default fursuitforboxjob_boxes = 0
    if fursuitforboxjob_attended == 1:
        pov "{i}I've already done my job for today. I'll come back another time.{/i}"

        jump lbl_adultstore_day_setup
    if fursuitforboxjob_times == 0:
        jump lbl_fursuit_for_box_job_pre
    elif fursuitforboxjob_times >= 1:
        jump lbl_fursuit_for_box_job_menu

label lbl_fursuit_for_box_job_menu:
    "How much effort should I put into today?"

    menu:
        "Give a casual performance":
            $ fursuitforboxjob_effort = 0
        "Give a good performance":
            $ fursuitforboxjob_effort = 1
        "Give it your all":
            $ fursuitforboxjob_effort = 2
        #"Get 50 boxes":
        #    $ fursuitforboxjob_boxes = 50
    if fursuitforboxjob_times == 2:
        jump lbl_fursuit_for_box_job_event_1
    elif fursuitforboxjob_times == 4:
        jump lbl_fursuit_for_box_job_event_2
    elif fursuitforboxjob_times == 6:
        jump lbl_fursuit_for_box_job_event_3
    else:
        jump lbl_fursuit_for_box_job_0

## Hazel

label lbl_fursuit_for_box_job_pre:

    scene black
    with fade
    $ renpy.pause()
    "After changing..."

    scene bg adultstore_day
    with fade
    show povfur neutral at left
    with dissolve
    show haz smirk at right
    with dissolve
    pov "This is beyond degrading."
    show haz smirk_talk at right
    haz "All jobs regarding any kind of costume usually are."
    haz "Now, you remember how the suit works, right?"
    show haz smirk at right
    pov "Yeah, just press one of my fingertips to my palm."
    pov "I still don't get how they managed to build into the suit a complex system of audio and add the controller of it to its hands yet they still managed to fuck up the tail."
    show haz smirk_talk at right
    haz "Well, that's the miracle of human stupidity for you."
    haz "Give one of those buttons a whirl."
    show haz neutral at right

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
    show haz embarrassed_talk at right
    haz "The sound of an angel."
    show haz smirk at right
    pov "It sounds like voice box is dying."
    show haz smirk_talk at right
    haz "And so is your soul. Are you ready?"
    show haz smirk at right

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
            show haz smirk_talk at right
            haz "Great spirit, call-to-action. I love it."
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
            show haz smirk_talk at right
            haz "I love it, convince them with a cliffhanging statement."
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
            show haz smirk_talk at right
            haz "Everyone loves to have a sexy-ass. That's the attitude to have."
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
            show haz smirk_talk at right
            haz "Exactly! If all goes wrong, bring out the big guns."
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
            show haz embarrassed_talk at right
            haz "A little creepy and stalkerish but you said 'hot ass' so that's fine..."

    jump lbl_fursuit_for_box_job_menu

## Roleplayers

label lbl_fursuit_for_box_job_event_1:

    scene bg adultstoreoutside_day
    with fade
    show povfur neutral at left
    with dissolve
    show cru shocked_talk at Position(xpos=1300)
    with dissolve
    show lor confused at right
    with dissolve
    show dav neutral at Position(xpos=1900)
    with dissolve
    cru "By the all nine rings orbiting the the third moon of the planet Osaria!"
    show cru neutral at Position(xpos=1300)
    show lor confused_talk at right
    lor "What do you speak of, Crugeon?"
    show cru neutral_talk at Position(xpos=1300)
    show lor shocked at right
    cru "Look! It's a perfect representation of Lady Crystal from the Chronicle of Crystal web games and comics!"
    show cru neutral at Position(xpos=1300)
    pov "..."

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
            show cru embarrassed at Position(xpos=1300)
            show lor angry_talk at right
            lor "I'm not to be told what to do, beast."
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
            show cru embarrassed at Position(xpos=1300)
            show lor smirk_talk at right
            lor "Fun? I doubt anything's as fun as the DnD game we'll be having tonight."
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
            show cru embarrassed at Position(xpos=1300)
            show lor bored_talk at right
            lor "Pfft. I guess whoever's under there lacks the meaning of 'being humble'."
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
            show cru embarrassed at Position(xpos=1300)
            show lor confused_talk at right
            lor "Dildos don't make for good LARPing swords, I've tried. Video games do tend to deceive you."
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
            show cru embarrassed at Position(xpos=1300)
            show lor smirk_talk at right
            lor "Now hold on a second, your face has 'available quest' written all over it."
    show cru neutral_talk at Position(xpos=1300)
    show lor confused at right
    cru "Major props on basing the costume on the “Trails of the Space-Enchantress” arc where she was cursed by her arch nemesis Milatrix by cursing her with a futanius curse!"
    show cru embarrassed_talk at Position(xpos=1300)
    cru "Not many people liked it but I think it's one of the high points of the series."
    show cru confused at Position(xpos=1300)
    show lor smirk_talk at right
    lor "Nice try, Crugeon."
    lor "But I'm afraid that you are mistaken here."
    lor "Can you not see the lack of her golden decor on her battle suit?"
    show cru bored at Position(xpos=1300)
    lor "This is obviously a costume based on the “Colosseum of the Orc-Bangers” arc."
    lor "Where she used her black sneaking suit to try and assassinate the Orc Warlock, Helisantrius the Great, before getting captured and experimented on by Dr. Conundrum."
    show cru confused_talk at Position(xpos=1300)
    show lor angry at right
    cru "I would be mistaken if I was talking of Gregory Matthews run of the comics which totally ruined her character."
    cru "Yet of course as my friend here and I know, I'm talking of the original and vastly superior run of the series by the real, true master Dave Young!"
    show cru confused at Position(xpos=1300)

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
    show cru shocked at Position(xpos=1300)
    show lor angry_talk at right
    show dav bored at Position(xpos=1900)
    lor "Hey, silence for a second you scandalous piece of meat."
    lor "Gregory Matthews brought much needed fresh air into the series by-"
    show haz smirk_talk flip at Position(xpos=650)
    show cru shocked at Position(xpos=1300)
    show lor shocked at right
    show dav neutral at Position(xpos=1900)
    haz "Fellas!"
    haz "Please bring this oh-so-interesting debate inside!"
    haz "We can discuss it together and maybe purchase a thing or two? It'll definitely help Lady Crystal out and make her day?"
    show haz smirk flip at Position(xpos=650)
    dav ".."
    hide dav neutral
    cru "..."
    hide cru shocked
    lor "...."
    show lor embarrassed_talk at right
    lor "Gladly, m'lady."
    hide lor embarrassed_talk
    pov "..."
    show haz smirk_talk flip at Position(xpos=650)
    haz "One tends to know these things when you're located next to a comic book store, you know?"

    jump lbl_fursuit_for_box_job_0

## Nightclubbers

label lbl_fursuit_for_box_job_event_2:

    scene bg adultstoreoutside_day
    with fade
    show povfur neutral at left
    with dissolve
    show zar smirk at Position(xpos=1250)
    with dissolve
    show ste confused_talk at right
    with dissolve
    ste "What t'e heck are you supposed to be?"
    show ste confused at right

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
    show ste shocked_talk at right
    ste "Ohhhh no. No, no, no, no, no."
    ste "Nuh-uh. I don't like t'at."
    show ste confused_talk at right
    ste "Sorry, I know you're just doing your job or what not but please do not do t'at around me again."
    ste "It p'reaks me out."
    show zar smirk_talk at Position(xpos=1250)
    show ste bored at right
    zar "Huh, a small stereo speaker tied to the head and connected to a voice box and controlled via the buttons inside the glove?"
    show zar confused_talk at Position(xpos=1250)
    zar "Not bad, sister! Although, I don't get the whole tail on the front thing."

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
            show zar neutral at Position(xpos=1250)
            show ste angry_talk at right
            ste "Can you shut up? I don't want to go inside!"
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
            show zar neutral at Position(xpos=1250)
            show ste angry_talk at right
            ste "Can you shut up? I just got off work and I'm too tired for t'is shit!"
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
            show zar neutral at Position(xpos=1250)
            show ste angry_talk at right
            ste "Can you shut up? I p'eel so p'rikkin uncomfortable right now!"
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
            show zar neutral at Position(xpos=1250)
            show ste angry_talk at right
            ste "No, I don't want a p'rikkin dildo-cock-ring bullshit!"
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
            show zar neutral at Position(xpos=1250)
            show ste angry_talk at right
            ste "Don't p'ollow me home you p'reak!"
    show zar smirk at Position(xpos=1250)
    show ste confused at right
    ste "..."
    show ste confused_talk at right
    ste "I guarantee that tail was not intentional..."
    show zar smirk_talk at Position(xpos=1250)
    show ste confused at right
    zar "Still, I should totally add something like this to my own DJ rig!"
    zar "It would add a ton to the effect and make my performance a whole lot more extravagant."
    zar "Imagine me finger tutting."
    show zar neutral at Position(xpos=1250)
    show ste confused_talk at right
    ste "And have you dress like one of t'ese weirdos?"
    show zar confused at Position(xpos=1250)
    show ste bored_talk at right
    ste "No way, Josie!"
    show zar bored at Position(xpos=1250)
    ste "I don't want you attracting more of these costumed p'olk dancing around drunk and groping each ot'er on the dance p'loor.."
    show zar bored_talk at Position(xpos=1250)
    show ste bored at right
    zar "People already dance drunk. Rubbing each other on the dance floor, though..."
    show zar angry_talk at Position(xpos=1250)
    zar "And who even says that I want to dress up as this, I'm talking about the mechanics behind it."
    show zar bored at Position(xpos=1250)
    show ste bored_talk at right
    ste "Look, we just came out of work. I'm too tired to argue about t'is."
    show ste bored at right

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
    show zar neutral at Position(xpos=1250)
    show ste bored_talk at right
    ste "P'uck this I'm out."
    show zar sad_talk at Position(xpos=1250)
    hide ste bored_talk
    zar "At least let me ask what controller she is using!"
    hide zar sad_talk
    pov "..."

    jump lbl_fursuit_for_box_job_0

## LUNA

label lbl_fursuit_for_box_job_event_3:

    scene bg adultstoreoutside_day
    with fade
    show povfur neutral at left
    with dissolve
    show lun confused at right
    with dissolve
    lun ".."
    lun "..."
    lun "...."
    show lun shocked_talk at right
    lun "O-Oh!"
    show lun embarrassed_talk at right
    lun "I'm sorry, I didn't mean to stare..."
    show lun confused_talk at right
    lun "I-I'm sorry but what exactly are you?"
    show lun confused at right

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
            show lun smirk_talk at right
            lun "No, thanks. I'm a little intrigued by what's out here at the moment."
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
            show lun smirk_talk at right
            lun "Haha, I bet you do."
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
            show lun confused_talk at right
            lun "That wasn't a yes or no question."
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
            show lun confused_talk at right
            lun "Not really in the market for some new ones at the moment. Sorry, honey."
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
            show lun bored_talk at right
            lun "Hold on a second, I'm not done with you."
    show lun confused_talk at right
    lun "They just have you out like that in this heat?"
    show lun sad_talk at right
    lun "You poor baby."
    show lun embarrassed_talk at right
    lun "I know this is a bit of a weird request but... May I touch you?"
    lun "I'm very into fur-like materials and plushies so I'm just curious what your costume is made of."
    show lun embarrassed at right

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
            show lun confused_talk at right
            lun "I'll take a pass on that offer, I just wanna feel you."
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
            show lun neutral_talk at right
            lun "I'll take that as a 'yes'!"
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
            show lun neutral_talk at right
            lun "Wicked awesome!"
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
            show lun bored_talk at right
            lun "Let me touch you and maybe I'll consider that offer!"
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
            show lun angry_talk at right
            lun "Nuh-uh you ain't leaving me hanging there, sweet-cheeks!"

    scene black
    with fade

    scene bg adultstoreoutside_day
    with fade
    show povfur neutral at left
    with dissolve
    show lun confused_talk at right
    with dissolve
    lun "Huh, I see..."
    show lun neutral_talk at right
    lun "This is definitely some quality material they put into your costume."
    show lun confused_talk at right
    lun "Makes it even weirder for them to put the tail in the crotch region then, don't you think?"
    show lun confused at right

    menu:
        "Press button number 1":
            pov "{i}WE-WE-WELCOME WELCOME! PLEASE COME INTO TH-THE STORE!{/i}"
            show lun confused_talk at right
            lun "I think you pressed the wrong button there, ma'am!"
        "Press button number 2":
            pov "{i}LO-LO-LOOKING FOR SOME FUN? WE'VE G-G-GOT THE REAL DEAL!{/i}"
            show lun smirk_talk at right
            lun "Oooh, naughty-naughty, aren't you? You're making me blush."
        "Press button number 3":
            pov "{i}Y-Y-YES, HONEY. YOU CAN BET YOUR SEXY ASS!{/i}"
            show lun neutral_talk at right
            lun "At least you're well-aware and embracing it loud and proud."
        "Press button number 4":
            pov "{i}I-I-I'M SORRY, HONEY. BUT WE DO HAVE PREMIUM DILDOS AND COCK RINGS!{/i}"
            show lun smirk_talk at right
            lun "I'm guessing you use them both at the same time?"
        "Press button number 5":
            pov "{i}T-T-THANK YOU FOR STOPPING BY! HOPE TO CATCH YOUR HOT ASS LATER TONIGHT!{/i}"
            show lun confused_talk at right
            lun "Tch- avoiding the question. It's not something to be embarrassed about y'know..."
    show lun confused_talk at right
    lun "You're pretty lucky. I've always wondered what it's like to skin something and climb inside."
    show lun smirk_talk at right
    lun "I bet it smells the same in there as it would with the real thing."
    show lun smirk at right
    lun "..."
    lun "...."
    show lun shocked at right
    "{i}*RIIIIINGTOOONEEE*{/i}"
    show lun confused at right
    lun "Hmm?"
    show lun shocked_talk at right
    lun "Oh, darn! I was supposed to be home half an hour ago!"
    show lun embarrassed_talk at right
    lun "I'm so sorry for taking your time."
    hide lun embarrassed_talk
    pov "..."
    pov "...."

    jump lbl_fursuit_for_box_job_0

####################################
label lbl_fursuit_for_box_job_0:

    scene bg fursuitforbox_1
    with fade
    $ renpy.pause(3,hard=True)

## Casual Effort
    if fursuitforboxjob_effort == 0:
        ## STAMINA REQUIREMENT
        if date == 9 or date == 18 or date == 26 or date == 5 or date == 0 or date == 7 or date == 13 or date == 29 or date == 2 or date == 16 or date == 23:
            if skill_sta <= 5:
                if skill_sta >= 3:
                    $ skill_sta -= 3
                else:
                    $ skill_sta = 0
                $ renpy.notify("You used 3 Stamina Points")
                scene black
                with fade
                "The inside of the suit was too hot and you passed out due to heatstroke."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif skill_sta >= 6:
                $ skill_sta -= 4
                $ renpy.notify("You used 4 Stamina Points")
                scene black
                with fade
                "You danced a bit to some music and convinced a few people to go in the store."
                $ fursuitforboxjob_boxes += 4
                scene bg fursuitforbox_3
                with fade
                "You gained 4 boxes for your effort today."
        ## CHARISMA REQUIREMENT
        elif date == 10 or date == 19 or date == 27 or date == 12 or date == 8 or date == 14 or date == 30 or date == 3 or date == 17 or date == 24:
            if skill_cha <= 5:
                if skill_cha >= 3:
                    $ skill_cha -= 3
                else:
                    $ skill_cha = 0
                $ renpy.notify("You used 3 Charisma Points")
                scene black
                with fade
                "Your moves are awkward and robotic, people were grossed out around you."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif skill_cha >= 6:
                $ skill_cha -= 4
                $ renpy.notify("You used 4 Charisma Points")
                scene black
                with fade
                "You waved at people and took some pictures, they enjoyed the voice lines of the suit and went in to browse the store."
                $ fursuitforboxjob_boxes += 4
                scene bg fursuitforbox_3
                with fade
                "You gained 4 boxes for your effort today."
        ## LUCK REQUIREMENT
        elif date == 6 or date == 20 or date == 28 or date == 21 or date == 1 or date == 15 or date == 22 or date == 4 or date == 11 or date == 25:
            if skill_luc <= 5:
                if skill_luc >= 3:
                    $ skill_luc -= 3
                else:
                    $ skill_luc = 0
                $ renpy.notify("You used 3 Luck Points")
                scene black
                with fade
                "A pack of dogs round the corner and now wouldn't stop chasing you."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif skill_luc >= 6:
                $ skill_luc -= 4
                $ renpy.notify("You used 4 Luck Points")
                scene black
                with fade
                "A small MeTuber meet ‘n' greet was taking place at the comic shop, a few people approached you to take pictures and some went in the store to look at the merch."
                $ fursuitforboxjob_boxes += 4
                scene bg fursuitforbox_3
                with fade
                "You gained 4 boxes for your effort today."

## Good Effort
    elif fursuitforboxjob_effort == 1:
        ## STAMINA REQUIREMENT
        if date == 5 or date == 18 or date == 26 or date == 0 or date == 2 or date == 14 or date == 28 or date == 7 or date == 11 or date == 22 or date == 9:
            if skill_sta <= 8:
                if skill_sta >= 5:
                    $ skill_sta -= 5
                else:
                    $ skill_sta = 0
                $ renpy.notify("You used 5 Stamina Points")
                scene black
                with fade
                "The air conditioning in the suit malfunctioned and performing in the hot sun had you sweating like a pig, driving away any potential customers."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif 9 <= skill_sta <= 13:
                $ skill_sta -= 7
                $ renpy.notify("You used 7 Stamina Points")
                scene black
                with fade
                "You have somewhat gotten a hang of the dance routine Hazel had you learn, it took the interest of a few customers to make the work worth it."
                $ fursuitforboxjob_boxes += 5
                scene bg fursuitforbox_3
                with fade
                "You gained 5 boxes for your effort today."
            elif skill_sta >= 14:
                $ skill_sta -= 9
                $ renpy.notify("You used 9 Stamina Points")
                scene black
                with fade
                "The choreography you've been practicing was a hit! As you questioned what you were doing with your life, customers begun taking interest in the store!"
                $ fursuitforboxjob_boxes += 7
                scene bg fursuitforbox_4
                with fade
                "You gained 7 boxes for your effort today."
        ## CHARISMA REQUIREMENT
        elif date == 4 or date == 19 or date == 29 or date == 1 or date == 13 or date == 27 or date == 6 or date == 17 or date == 21 or date == 15:
            if skill_cha <= 8:
                if skill_cha >= 5:
                    $ skill_cha -= 5
                else:
                    $ skill_cha = 0
                $ renpy.notify("You used 5 Charisma Points")
                scene black
                with fade
                "Your body language was terrible and people mistook you for a furry simpleton craving for attention so they ignored you."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif 9 <= skill_cha <= 13:
                $ skill_cha -= 7
                $ renpy.notify("You used 7 Charisma Points")
                scene black
                with fade
                "You were familiar enough with the voice box to engage others in conversation. Some were amused by it and were convinced to peruse the store."
                $ fursuitforboxjob_boxes += 5
                scene bg fursuitforbox_3
                with fade
                "You gained 5 boxes for your effort today."
            elif skill_cha >= 14:
                $ skill_cha -= 9
                $ renpy.notify("You used 9 Charisma Points")
                scene black
                with fade
                "You posed for pictures and a few videos for potential customers, they loved your enthusiasm and got in the store to help you out."
                $ fursuitforboxjob_boxes += 7
                scene bg fursuitforbox_4
                with fade
                "You gained 7 boxes for your effort today."
        ## LUCK REQUIREMENT
        elif date == 3 or date == 20 or date == 30 or date == 8 or date == 12 or date == 23 or date == 10 or date == 16 or date == 25 or date == 24:
            if skill_luc <= 8:
                if skill_luc >= 5:
                    $ skill_luc -= 5
                else:
                    $ skill_luc = 0
                $ renpy.notify("You used 5 Luck Points")
                scene black
                with fade
                "While you were dancing around, you tripped and the head landed on something disgusting, Hazel forced you to clean it for the rest of the day."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif 9 <= skill_luc <= 13:
                $ skill_luc -= 7
                $ renpy.notify("You used 7 Luck Points")
                scene black
                with fade
                "A celebrity pornstar spontaneously visited the store today! You were simply tasked to help display the products so you took it easy."
                $ fursuitforboxjob_boxes += 5
                scene bg fursuitforbox_3
                with fade
                "You gained 5 boxes for your effort today."
            elif skill_luc >= 14:
                $ skill_luc -= 9
                $ renpy.notify("You used 9 Luck Points")
                scene black
                with fade
                "A new product launched at the store, the line to get it made even more people curious so all you had to do was give out fliers, lucky break!"
                $ fursuitforboxjob_boxes += 7
                scene bg fursuitforbox_4
                with fade
                "You gained 7 boxes for your effort today."

## All in Effort
    elif fursuitforboxjob_effort == 2:
        ## STAMINA REQUIREMENT
        if date == 1 or date == 11 or date == 28 or date == 0 or date == 10 or date == 13 or date == 26 or date == 4 or date == 15 or date == 30 or date == 6:
            if skill_sta <= 10:
                if skill_sta >= 7:
                    $ skill_sta -= 7
                else:
                    $ skill_sta = 0
                $ renpy.notify("You used 7 Stamina Points")
                scene black
                with fade
                "The excessive dance you pulled off not only drove away customers with the biggest cringe on their faces, you also managed to pull a muscle, great job!"
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif 11 <= skill_sta <= 14:
                $ skill_sta -= 9
                $ renpy.notify("You used 9 Stamina Points")
                scene black
                with fade
                "You worked out quite the sweat with your routine, however it only brought it a few customers."
                $ fursuitforboxjob_boxes += 6
                scene bg fursuitforbox_4
                with fade
                "You gained 6 boxes for your effort today."
            elif 15 <= skill_sta <= 18:
                $ skill_sta -= 11
                $ renpy.notify("You used 11 Stamina Points")
                scene black
                with fade
                "You dance a complex routine that had many in awe! It created enough buzz around the store for more potential customers."
                $ fursuitforboxjob_boxes += 9
                scene bg fursuitforbox_5
                with fade
                "You gained 9 boxes for your effort today."
            elif skill_sta >= 19:
                $ skill_sta -= 13
                $ renpy.notify("You used 13 Stamina Points")
                scene black
                with fade
                "An overly complicated dance show had the public stunned as they crowd around you to see you dance. Many had to enter the store to get a good view of you."
                $ fursuitforboxjob_boxes += 12
                scene bg fursuitforbox_5
                with fade
                "You gained 12 boxes for your effort today."
        ## CHARISMA REQUIREMENT
        elif date == 9 or date == 12 or date == 27 or date == 3 or date == 14 or date == 25 or date == 7 or date == 16 or date == 23 or date == 17:
            if skill_cha <= 10:
                if skill_cha >= 7:
                    $ skill_cha -= 7
                else:
                    $ skill_cha = 0
                $ renpy.notify("You used 7 Charisma Points")
                scene black
                with fade
                "Your creepy mannerisms had gotten people to throw drinks and trash at you, a woman even called the police on you."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif 11 <= skill_cha <= 14:
                $ skill_cha -= 9
                $ renpy.notify("You used 9 Charisma Points")
                scene black
                with fade
                "You somehow managed to pull off flirting while wearing a fursuit, some went into the store but nothing extravagant."
                $ fursuitforboxjob_boxes += 6
                scene bg fursuitforbox_4
                with fade
                "You gained 6 boxes for your effort today."
            elif 15 <= skill_cha <= 18:
                $ skill_cha -= 11
                $ renpy.notify("You used 11 Charisma Points")
                scene black
                with fade
                "Your dominance over the voicebox has you practically transforming into the character, you're a total hit!"
                $ fursuitforboxjob_boxes += 9
                scene bg fursuitforbox_5
                with fade
                "You gained 9 boxes for your effort today."
            elif skill_cha >= 19:
                $ skill_cha -= 13
                $ renpy.notify("You used 13 Charisma Points")
                scene black
                with fade
                "The number of guys who approached you to give you their numbers or ask when you were getting out has you concerned for the survival of the human race."
                "At least a large majority of them entered the store in search for play things for a hopeful night with you."
                $ fursuitforboxjob_boxes += 12
                scene bg fursuitforbox_5
                with fade
                "You gained 12 boxes for your effort today."
        ## LUCK REQUIREMENT
        elif date == 2 or date == 18 or date == 29 or date == 8 or date == 19 or date == 24 or date == 5 or date == 20 or date == 22 or date == 21:
            if skill_luc <= 10:
                if skill_luc >= 7:
                    $ skill_luc -= 7
                else:
                    $ skill_luc = 0
                $ renpy.notify("You used 7 Luck Points")
                scene black
                with fade
                "The things you have experienced today were too horrific to be told without you having a panic attack, you now wonder if there is an actual curse on this suit."
                $ fursuitforboxjob_boxes += 2
                scene bg fursuitforbox_2
                with fade
                "You gained 2 boxes for your effort today."
            elif 11 <= skill_luc <= 14:
                $ skill_luc -= 9
                $ renpy.notify("You used 9 Luck Points")
                scene black
                with fade
                "For once you have quite the peaceful day, Hazel let's you off early and gives you a bonus seeing as there is very few people around."
                $ fursuitforboxjob_boxes += 6
                scene bg fursuitforbox_4
                with fade
                "You gained 6 boxes for your effort today."
            elif 15 <= skill_luc <= 18:
                $ skill_luc -= 11
                $ renpy.notify("You used 11 Luck Points")
                scene black
                with fade
                "A van of other fursuiters managed to drive by you. After seeing your costume they head into the store to support an assuming furry-positive business!"
                $ fursuitforboxjob_boxes += 9
                scene bg fursuitforbox_5
                with fade
                "You gained 9 boxes for your effort today."
            elif skill_luc >= 19:
                $ skill_luc -= 13
                $ renpy.notify("You used 13 Luck Points")
                scene black
                with fade
                "You somehow become an overnight social media star when you make a strange move trying to hold back a sneeze."
                "You were bombarded with people wanting pictures and many converted into customers."
                $ fursuitforboxjob_boxes += 12
                scene bg fursuitforbox_5
                with fade
                "You gained 12 boxes for your effort today."
    "You have a total of [fursuitforboxjob_boxes] boxes and need a total of 50 to rebuild the fort."
    if 1 <= fursuitforboxjob_boxes <= 14 and not inventory.has_item(Items.boxes1):
        $ inventory.add(Items.boxes1)
    elif 15 <= fursuitforboxjob_boxes <= 33 and not inventory.has_item(Items.boxes2):
        $ inventory.drop(Items.boxes1)
        $ inventory.add(Items.boxes2)
    elif 34 <= fursuitforboxjob_boxes <= 49 and not inventory.has_item(Items.boxes3):
        $ inventory.drop(Items.boxes2)
        $ inventory.add(Items.boxes3)
    elif fursuitforboxjob_boxes >= 50 and not inventory.has_item(Items.boxes4):
        $ inventory.drop(Items.boxes3)
        $ inventory.add(Items.boxes4)
    $ fursuitforboxjob_attended = 1
    $ fursuitforboxjob_times += 1
    $ gtime += 1
    if gtime == 1:
        jump lbl_adultstore_day_setup
    else:
        jump lbl_street_night_setup
