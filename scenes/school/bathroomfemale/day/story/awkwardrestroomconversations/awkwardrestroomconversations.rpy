label lbl_awkward_restroom_conversations:
    ## continued from lbl_trapped_in_the_stalls ##
    ##-Once the Eghans leave the bathroom, Lashley is the first out of the stall to make sure the coast is clear-
    ##-Cut back to inside the stalls with MC and Lashley

    default awkward_restroom_conversation_choice = 0
    scene bg schoolbathroomfemale_day
    with fade
    show pri confused_talk at right
    with dissolve
    pri "…"
    pri "Okay, they are gone."
    show pov embarrassed at left
    with dissolve
    pri "Quickly, let's get out of here!"
    show pov confused_talk at left
    show pri shocked_talk at right
    pov "Get out?"
    pov "I thought you wanted to catch this girl on the act."
    show pov confused at left
    show pri bored_talk at right
    pri "I do, but I know she isn't coming."
    pri "Not after the -Eghans used the restroom."
    show pov shocked_talk at left
    show pri smirk at right
    pov "Wait, what?"
    pov "Why not?"
    show pov confused at left
    show pri smirk_talk at right
    pri "If Meghan and her friends are still around that means other students are still here as well."
    pri "Likely taking remedial classes or something."
    show pri bored_talk at right
    pri "It's like they said, she is known for how well she keeps her secret so she is not about to let anyone accidentally catch her in the act."
    pri "Not unless she intends to do so."
    show pov confused_talk at left
    show pri bored at right
    pov "I still don't-"
    show pov shocked at left
    show pri bored_talk at right
    pri "She is not going to risk coming into the ladies restroom after the -Eghans used it because there are bound to be some… Unique students trying to smell the seats."

    hide pri bored_talk
    with dissolve
    show pov confused at left
    pri "To my office, young man!"

    studm "…"
    studm "…"
    studm "Yes, Director Lashley…"

    scene bg bathroomstakeout_1
    show pri angry at right
    with fade
    show pov bored_talk at left
    with dissolve
    pov "..."
    pov "Oh..."
    show pov confused_talk at left
    pov "Yeah, I really didn't need to know or see that…"
    show pov confused at left
    show pri bored at right
    pri "Hey, it's your generation."
    show pov bored_talk at left
    show pri confused at right
    pov "Don’t remind me..."
    pov "We are really going to go extinct a few generations from now…"
    show pov bored at left
    show pri smirk_talk at right
    pri "Look, what's important right now is that we get out of here before people notice you here."
    show pov smirk at left
    show pri bored_talk at right
    pri "There is no way she is going to come today, so no point in trying to stand guard any longer."
    pri "I'll have to try again some other time."
    show pov embarrassed_talk at left
    show pri smirk at right
    pov "I'm sorry your stake out didn't go as planned."
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "Oh, don't worry about it, [povname]."
    show pri bored_talk at right
    pri "That's the nature of the Stake Out, sometimes you win and get the information you need and sometimes you go back home empty handed."
    show pov confused at left
    show pri neutral_talk at right
    pri "What's important is your perseverance for the cause you believe in!"
    show pri shocked_talk at right
    pri "Also, giving proper attention to all the small victories along the way help to keep you motivated."
    pri "You heard what the -Eghans said, right?"
    show pov shocked at left
    show pri smirk_talk at right
    pri "She is blackmailing her clients into silence, so I can at least rest assured that she is not being taken advantage of or is being forced to do something she doesn't want to."
    show pov embarrassed_talk at left
    show pri confused at right
    pov "I guess that’s comforting to know?"
    pov "You are looking for a dominatrix rather than a girl in trouble."
    show pov confused at left
    show pri smirk_talk at right
    pri "Give credit to small victories, [povname]. Always give proper credit to small victories."

    ##-If Lashley RP is 3 or lower-
    if principallashley_points <= 3:
        show pov smirk at left
        show pri bored_talk at right
        pri "Anyway, we best get moving."
        pri "You are still a man in the ladies restroom, you know?"
        pri "Best for you to head home."
        show pov neutral_talk at left
        show pri smirk at right
        pov "Right behind you, Director Lashley."
        pov "What are you going to do now that this girl won’t come?"
        show pov shocked at left
        show pri smirk_talk at right
        pri "Wait for the next opportunity, of course!"
        pri "All in a day's work."
        show pov embarrassed_talk at left
        show pri smirk at right
        pov "Fair enough. See you later, then, Director Lashley."
        show pov neutral at left
        show pri neutral_talk at right
        pri "Careful on your way home, [povname]!"

        $ gtime = 2
        $ renpy.notify("My Relationship with Director Lashley is too low")

        jump lbl_schoolyard_night_setup
       ##=SCENE END=
    ##-If Lashley RP is 4 or higher-
    ##elif principallashley_points >= 4:

    show pov neutral at left
    show pri embarrassed_talk at right
    pri "Um… [povname]?"
    show pov neutral_talk at left
    show pri confused at right
    pov "Yes, Director Lashley?"
    show pov shocked at left
    show pri confused_talk at right
    pri "Are you… Um…"
    pri "Close… With Miss Teghan?"
    show pov embarrassed_talk at left
    show pri embarrassed at right
    pov "Oh, you mean because of what she said?"
    show pov embarrassed at left
    show pri embarrassed_talk at right
    pri "Y-Yeah…"
    show pov smirk_talk at left
    show pri confused at right
    pov "Well, I’m not sure close is the right word for it."
    show pov smirk at left
    show pri confused_talk at right
    pri "But she shows interest for you, right?"
    show pov embarrassed_talk at left
    show pri confused at right
    pov "W-Well, I mean…"
    pov "Yeah, of course."
    show pov bored_talk at left
    show pri smirk at right
    pov "But I really haven’t interacted with her too much."
    pov "Nice to know she at least isn’t just being polite for the hell of it."
    show pov confused at left
    show pri bored_talk at right
    pri "So… You do plan on having something with her?"
    show pov neutral_talk at left
    show pri shocked at right
    pov "Well, I don’t know."
    pov "I haven’t really gotten to know her too well but she does seem really nice."
    show pov embarrassed_talk at left
    show pri bored at right
    pov "Quite pretty too."
    show pov embarrassed at left
    show pri bored at right
    pri "Pretty, huh…"
    pri "So you have a preference for girls like her?"
    show pov confused at left
    show pri smirk_talk at right
    pri "Is that your type?"
    show pov shocked_talk at left
    show pri bored at right
    pov "Well, I’m not sure what you mean by girls like her but she is nice enough to say hello from time to time and she doesn’t immediately look at me like I’m some odd bug or disgusting trash like Meghan does depending on her mood."
    pov "So at the very least she has that going for her in my book."
    show pov confused at left
    show pri bored_talk at right
    pri "Does she now…?"
    show pov bored_talk at left
    show pri shocked at right
    pov "Why do you ask?"
    show pov confused at left
    show pri shocked_talk at right
    pri "N-Nothing in particular!"
    show pov smirk at left
    pri "Just curiosity!"
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "U-Um…"
    show pov neutral_talk at left
    show pri embarrassed at right
    pov "Something wrong?"
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "N-No! Not at all…"
    show pov neutral at left
    pri "But after this are you, um… A-Are you going to…"
    pri "Pursue… Something with her by any chance?"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "Are you asking if I plan on asking her out?"
    show pov smirk at left
    show pri confused_talk at right
    pri "W-Well, are you?"
    show pov neutral_talk at left
    show pri embarrassed at right
    pov "I-"

    ##=CHOICE=
    menu:
    ##pov "I don’t think so."
        "I don't think so":
            ##-If “I don’t think so” was picked-
            $ awkward_restroom_conversation_choice = 1
            show pri shocked at right
            pov "I don’t think so."
            show pov embarrassed_talk at left
            pov "I mean, I haven't had much of a chance to talk to her and I don't want to tie myself up in a relationship right after I just arrived."
            show pri confused at right
            pov "I mean, I'm still the new kid in town, right?"
            show pov neutral_talk at left
            pov "Why rush things, you know?"
            show pov neutral at left
            show pri shocked_talk at right
            pri "R-Right!"
            show pov confused at left
            show pri embarrassed_talk at right
            pri "That's a relief…"
            show pri shocked_talk at right
            pri "I-I mean, It's a relief you aren't taking things such as who you date lightly!"
            show pov embarrassed at left
            show pri embarrassed_talk at right
            pri "I wouldn't want you to be distracted from your class work."
            show pov neutral_talk at left
            show pri embarrassed at right
            pov "Yeah, of course."
            pov "So, shall we go?"
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "R-Right! Yes."
            show pri neutral_talk at right
            pri "Until next time, [povname]."
            pri "Be safe going home."
            show pov neutral_talk at left
            show pri neutral at right
            pov "Likewise, Director Lashley."

            ##=RESULT END=
    ##=OR=
        "I do plan to":
            ##-If "I do plan to" was picked-
            $ awkward_restroom_conversation_choice = 2
            show pov neutral_talk at left
            show pri shocked at right
            pov "I do plan on asking her out, yeah."
            show pov embarrassed_talk at left
            pov "I mean, she has always been clear about how she has the hots for me and everything. But I thought at first she was just being polite or flirty or something."
            pov "Since she hangs around someone like Meghan, I was sort of expecting to be rejected the moment I tried asking her out because I read a signal wrong or something."
            show pov smirk_talk at left
            show pri embarrassed at right
            pov "We men aren't the best at reading women's signals, you know?"
            show pov neutral_talk at left
            pov "But I mean, I pretty much got confirmation from her just now that she does see potential in me."
            show pov embarrassed_talk at left
            show pri bored at right
            pov "May as well strike while the iron is hot, you know?"
            show pov embarrassed at left
            show pri bored_talk at right
            pri "I-I see…"
            pri "…"
            show pov confused at left
            show pri embarrassed_talk at right
            pri "I-Is that really the best idea?"
            pri "I-I mean, you just arrived in town and you haven't really gotten to know her well and… Uh…"
            show pov confused_talk at left
            show pri embarrassed at right
            pov "Everything alright, Director Lashley?"
            show pov confused  at left
            show pri shocked_talk at right
            pri "Y-Yeah… I just…"
            show pov embarrassed at left
            show pri confused_talk at right
            pri "… Um…"
            show pri embarrassed_talk at right
            pri "I-I'm sorry [povname], I just…"
            show pov shocked at left
            show pri embarrassed_talk at right
            pri "I really just need to go-!"

            ##-Lashley quickly turns and runs out of the restroom without another word-

            show pov shocked_talk at left
            hide pri embarrassed_talk at right
            with dissolve
            pov "H-Hey wait!"
            pov "…"
            show pov confused_talk at left
            pov "See you later, I guess?"
            pov "What was that all about?"

        "What should I do":
            ##-If "What should I do?" Was picked-
            $ awkward_restroom_conversation_choice = 3
            show pov bored_talk at left
            show pri confused at right
            pov "Well, to be completely honest with you, I'm not sure."
            show pov smirk at left
            show pri confused_talk at right
            pri "Y-You are not?"
            show pov neutral_talk at left
            show pri shocked at right
            pov "No, not at all."
            show pov embarrassed_talk at left
            pov "I mean, on one hand its obvious she is interested in me, but I'm not sure if I want to just dive into a relationship with someone I don't know."
            show pov shocked_talk at left
            show pri confused at right
            pov "Plus the fact she is tied by the hip to Meghan certainly doesn't help with things."
            show pov embarrassed_talk at left
            show pri smirk at right
            pov "She doesn't really seem like a person I want to hang around too much."
            show pov embarrassed at left
            show pri smirk_talk at right
            pri "Those are very good points."
            show pov neutral_talk at left
            show pri confused at right
            pov "I know, but on the other hand, Teghan is quite attractive and she seems really cool to be around in general."
            show pov embarrassed_talk at left
            pov "Besides, she is even talking about me to her friends when I'm not around."
            pov "That's certainly a good sign. Specially when she is the one bringing up the topic and everything."
            show pov smirk_talk at left
            show pri embarrassed at right
            pov "And unlike Meghan she is definitely the type of person I wouldn't mind hanging out or going out on dates with."
            show pov neutral at left
            show pri bored_talk at right
            pri "I-I see…"
            show pov neutral_talk at left
            show pri shocked at right
            pov "I'm definitely still on the fence about it, what do you think I should do?"
            show pov embarrassed at left
            show pri shocked_talk at right
            pri "Y-You want my opinion on this?!"
            show pov neutral_talk at left
            show pri shocked at right
            pov "Well, yeah."
            pov "I mean. You did ask me about it."
            show pov smirk_talk at left
            show pri bored at right
            pov "Surely you have your own opinion about the whole subject."
            show pov smirk at left
            show pri bored_talk at right
            pri "I-I…"
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "S-She is nice but…"
            pri "I really don’t think you should…"
            pri "Um…"
            show pov confused_talk at left
            show pri embarrassed at right
            pov "Yes?"
            pov "You really think I should what?"
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "Uh…"
            show pov confused at left
            show pri shocked_talk at right
            pri "Oh, right!"
            pri "I have a student alone in my office unattended!"
            show pov shocked at left
            show pri embarrassed_talk at right
            pri "Silly me, who knows what he could be doing there without supervision!"
            pri "I-I’m sorry, [povname], but I really have to get out of here!"
            show pov confused at left
            show pri neutral_talk at right
            pri "I’ll talk to you later!"

            ##-Lashley quickly dashes out of the restroom-
            show pov shocked_talk at left
            pov "H-Hey!"
            hide pri embarrassed at right
            with dissolve
            pov "Hang on a sec- and she’s gone…"
            show pov confused_talk at left
            pov "…"
            pov "What the hell was that all about?"

    show pov smirk_talk at left
    pov "Well, might as well get out of here before somebody sees me…"

    $ principallashley_path = 7.9
    $ gtime = 2
    jump lbl_schoolyard_night_setup
    ##=SCENE END=
