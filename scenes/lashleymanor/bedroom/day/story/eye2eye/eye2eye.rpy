label lbl_eye_2_eye:
    default choice_asked_eye2eye_donow =  False
    default choice_asked_eye2eye_doaboutsister =  False
    default choice_asked_eye2eye_doabouteverything =  False
    default eye2eye_lashleys_lover_chosen = False
    #[Lashley’s Bedroom, Day– “Eye-2-Eye” – misslashley_path = 34]

    #-Scene fades in with Lashley and the Mc fully dressed and her room cleaned,
    # there is still an air of awkwardness between them, but Lashley has at least calmed down-
    scene bg lashleybedroom_day
    with fade

    show pov bored at left
    show pri embarrassed_talk at right
    with dissolve
    pri "Thank you so much for helping me clean up."
    show pri sad_talk at right
    pri "You really didn’t have to…"
    show pov bored_talk at left
    show pri shocked at right
    pov "Don’t sweat it."
    pov "It’s not that big of a deal - and I was a key factor in getting it dirty in the first place."
    show pov bored at left
    show pri embarrassed_talk at right
    pri "R-Right…"
    pri "Umm…"
    pri "A-Are you still in pain… You know…"
    show pri confused_talk at right
    pri "Down there?"
    show pov bored_talk at left
    show pri confused at right
    pov "Feels a lot better by now, though I’m going to need some time before I can do something like that again. I think I may have pulled a few muscles there."
    show pri shocked at right
    pov "But to be honest with you, it’s the scratches and bite marks what makes it a bit uncomfortable to move now."

    #-Lashley grows embarrassed upon hearing that-
    show pov bored at left
    show pri confused_talk at right
    pri "T-The ointment I applied on you should take care of it soon!"
    show pov shocked at left
    show pri embarrassed_talk at right
    pri "Let me know if you need some more…"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "Looking for an excuse for me to take my shirt off again, eh?"
    pov "You really are insatiable."

    #-Lashley grows even more embarrassed-
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "T-That’s not what I meant; and you know it!"
    pri "G-Good heavens, why do you take so much joy in teasing me?"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "Cuz you are cute when you are embarrassed."
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "S-Stop it!"
    pri "Gosh, silver tongue devils are the enemy of all women out there."
    show pov shocked at left
    show pri neutral_talk at right
    pri "Maybe I do need to keep you to myself…"
    show pri shocked_talk at right
    pri "…!"
    pri "I… I shouldn’t have said that…"
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "Sorry…"
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "… It’s okay."
    pov "I guess we can’t postpone going back to that subject with cleaning, anymore."
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "W-Well, I’ve been meaning to clean the attic, so…"
    show pov smirk at left
    show pri shocked at right
    pov "Don’t push your luck."
    pov "We have to talk about it, Lashley."
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "{i}*sigh*{/i}…"
    pri "I know…"
    pri "I’m just… Scared about what you have to say…"
    show pov bored_talk at left
    show pri confused at right
    pov "I just have a couple of questions, Lashley."
    show pov confused_talk at left
    pov "After that… Well, we can figure out what to do after that."
    show pov embarrassed_talk at left
    pov "I haven’t planned that far ahead myself."
    show pov confused at left
    show pri embarrassed_talk at right
    pri "A-Alright…"
    pri "It seems only fair."
    show pov bored at left
    show pri confused at right
    pri "What are your questions, then?"

    menu eye2eye_question_loop:
        "What will you do now?"if not choice_asked_eye2eye_donow:

            #-If "What will you do now?" Was picked-
            show pov confused_talk at left
            show pri shocked_talk at right
            pov "What are you going to do now?"
            show pov bored_talk at left
            pov "I mean, what are you going to do now that you are thinking straight and aren’t going all Yandere on me?"
            show pov confused at left
            show pri embarrassed_talk at right
            pri "I… I don’t know…"
            show pri confused_talk at right
            pri "I no longer feel like I'm constantly fighting with my own urges."
            pri "It’s like my body is finally at ease from a phantom pain that it’s been struggling with for years now."
            show pri embarrassed_talk at right
            pri "I feel so at ease that…"
            show pov embarrassed at left
            show pri confused_talk at right
            pri "That I’m not really sure what to do now…"
            pri "It's such a strange feeling."
            show pov embarrassed_talk at left
            show pri embarrassed at right
            pov "I think you finally relaxed for real for once."
            pov "All those years of bottling everything up and it finally bursting on you."
            show pov neutral_talk at left
            pov "Just give yourself some time to adjust to it and you’ll be fine."
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "You know, I think you are right…"
            pri "I-I’m just worried I don’t know what to do with myself now that I feel like this."
            show pri confused_talk at right
            pri "It was that same feeling of dread that I used as fuel to push me forward, you know?"
            pri "I would always keep my schedule full and always trying to find something to do so I could distract myself from my urges."
            show pri neutral_talk at right
            pri "Now that I’m not feeling them…"
            show pov confused_talk at left
            show pri embarrassed_talk at right
            pov "You are feeling lost."
            show pov smirk at left
            show pri embarrassed_talk at right
            pri "Y-Yeah…"
            pri "The fact that we just cleaned ourselves up and why I asked you to help clean the room up was to avoid another deep conversation…"
            show pov confused_talk at left
            show pri smirk at right
            pov "I guess I can’t blame you for that."
            pov "I’d do it too if I could get away with it."
            show pov neutral at left
            show pri smirk_talk at right
            pri "Thanks for being lenient with me, then."
            show pov confused at left
            show pri shocked_talk at right
            pri "… But."
            pri "It just occurred to me that a lot of the things I thought I love to do I only really do when I want to keep myself from thinking about my urges…"
            show pov embarrassed at left
            show pri embarrassed_talk at right
            pri "so, does that mean all of my hobbies just so happen to be related to me escaping from my problems?"
            show pov smirk_talk at left
            show pri embarrassed at right
            pov "I think you are overthinking things too much."
            pov "I mean, they managed to distract you because you found them fun, right?"
            show pov smirk at left
            show pri embarrassed_talk at right
            pri "Well… Yeah…"
            show pov neutral_talk at left
            show pri shocked at right
            pov "Then try them out now and see how you feel or try and experiment with something new!"
            pov "Don’t overthink things too much."
            show pov neutral at left
            show pri confused_talk at right
            pri "I… I shall, then."
            show pri embarrassed_talk at right
            pri "Thank you, [povname]."
            show pov neutral_talk at left
            show pri neutral at right
            pov "Don’t mention it."
            $ choice_asked_eye2eye_donow = True
            #=RESULT END=

            #-Back to choice tree-

        "What will you do about your sister?"if not choice_asked_eye2eye_doaboutsister:
            #-If “What will you do about your sister?” was picked-
            show pov confused_talk at left
            show pri shocked at right
            pov "What will you do about your sister?"
            pov "I doubt you want to just bottle your feelings up again and pretend everything is going to be ok."
            show pov confused at left
            show pri embarrassed_talk at right
            pri "I… I’m not sure…"
            pri "I have so many things to say to her, but it’s not like me having an outburst of my emotions is gonna make her suddenly start listening to me."
            show pov bored_talk at left
            show pri embarrassed at right
            pov "It couldn’t be that easy after all."
            show pov bored at left
            show pri embarrassed_talk at right
            pri "I… I want to keep trying."
            pri "Getting close with my sister has been a dream of mine for so long…"
            show pov confused at left
            show pri sad_talk at right
            pri "I just can't imagine myself giving up on it just like that…"
            show pov confused_talk at left
            show pri sad at right
            pov "Are you sure it's a smart thing to do?"
            pov "Healthy even?"
            show pov confused at left
            show pri bored_talk at right
            pri "Maybe… Maybe not…"
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "I mean… I don't want to give up on her… Even after all I've said…"
            show pov embarrassed_talk at left
            show pri bored at right
            pov "She's still your sister…"
            show pov embarrassed at left
            show pri bored_talk at right
            pri "And because of that, she gets a pass…"
            show pov neutral at left
            show pri confused_talk at right
            pri "I have to keep trying…"
            show pov neutral_talk at left
            show pri confused at right
            pov "Please tell me you’ll at least look after yourself more."
            show pov embarrassed at left
            show pri embarrassed_talk at right
            pri "That is indeed a priority."
            show pri bored_talk at right
            pri "I may still be adamant about reconnecting with my sister one day."
            show pri neutral_talk at right
            pri "But now I know not to let it become the only thing pushing me forward or letting me bother me to the point of a breakdown."
            show pri embarrassed_talk at right
            pri "I’ll always be ready to receive my sister with my arms open, but until then…"
            show pov neutral at left
            show pri neutral_talk at right
            pri "I’m going to take better care of myself."
            show pov embarrassed at left
            show pri confused_talk at right
            pri "I-I don’t know how yet, but…"
            pri "I’ll figure something out."
            show pov embarrassed_talk at left
            show pri confused at right
            pov "That’s probably for the best."
            pov "You need to reconnect with other people before you try and reconnect with her."
            show pov neutral_talk at left
            show pri confused at right
            pov "That way you’ll at least have a safety net to fall back on if she gives you a cold shoulder again."
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "That does sound lovely."
            $ choice_asked_eye2eye_doaboutsister = True
                #=RESULT END=

        "What will you do about everything you did?"if not choice_asked_eye2eye_doabouteverything:
            #-If “What will you do about everything you did” was picked-
            show pov confused_talk at left
            show pri shocked at right
            pov "What will you do about everything you did while you were on this little crusade of yours?"
            show pov bored_talk at left
            show pri confused at right
            pov "I mean, luckily nobody was hurt aside from the bump on the back of my head and the destruction of property you caused."
            show pov smirk_talk at left
            pov "Plus Allaway being overworked as all hell."
            show pov confused at left
            show pri embarrassed_talk at right
            pri "I-I’ll take care of everything, I promise you!"
            show pov shocked at left
            show pri confused_talk at right
            pri "How’s your head by the way?"
            show pov embarrassed at left
            show pri embarrassed_talk at right
            pri "Oh, I hope I didn't hit you too hard…"
            show pov neutral_talk at left
            show pri embarrassed at right
            pov "It’s fine, don’t worry about it."
            show pov embarrassed_talk at left
            show pri  at right
            pov "I don’t think any permanent damage was made and I don’t notice any pain either."
            show pov bored_talk at left
            pov "Though… I was far more distracted with what we were doing to really pay any attention to it."

            #-Lashley goes red-
            show pov bored at left
            show pri shocked_talk at right
            pri "D-Don’t bring that up while we are being serious here!"
            show pov smirk_talk at left
            show pri embarrassed at right
            pov "Hehehe."
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "{i}*sigh*{/i}…"
            pri "I… I’ll be sure to compensate everyone I may have crossed while I was out of control."
            show pov embarrassed at left
            show pri neutral_talk at right
            pri "I’ll own up to my mistakes and take care of them."
            pri "That’s how I’ve been raised, after all."
            show pov shocked_talk at left
            show pri embarrassed at right
            pov "So you are planning on turning yourself in?"
            show pri embarrassed_talk at right
            pri "W-Well, I’m planning something else at the moment, but I assure you I’ll take care of everything."
            pri "Just have some faith in me that I’ll be able to handle things."
            show pov smirk_talk at left
            show pri neutral at right
            pov "So that’s a no on being honest with the law?"
            show pov shocked at left
            show pri neutral_talk at right
            pri "I’ll make up for everything and more."
            show pov embarrassed at left
            show pri smirk_talk at right
            pri "Can’t do that while facing charges as well right?"
            show pov neutral_talk at left
            show pri smirk at right
            pov "Fair enough, I suppose."
            show pov embarrassed_talk at left
            show pri embarrassed at right
            pov "Just… Don’t ever do something like this again."
            pov "It’s fine if I’m the only one affected but don’t drag others as well."
            show pov embarrassed at left
            show pri sad_talk at right
            pri "Y-Yes, of course…"
            $ choice_asked_eye2eye_doabouteverything = True
            #=RESULT END=

            #-Back to choice tree-
                #=CHOICE END=

    #-during this segment, the player will be returned to the choice tree until every question has been asked once-
    if False in (choice_asked_eye2eye_donow, choice_asked_eye2eye_doaboutsister, choice_asked_eye2eye_doabouteverything):
        jump eye2eye_question_loop




    #-Back to choice tree-



    #-Once all choices have been selected, the scene continues-
    show pov confused at left
    show pri embarrassed_talk at right
    pri "Alright, was that everything you wanted to ask?"
    show pov bored_talk at left
    show pri embarrassed at right
    pov "At the moment, yes."
    show pov confused at left
    show pri confused_talk at right
    pri "Is it alright if I ask you one thing in return?"
    show pov bored_talk at left
    show pri embarrassed at right
    pov "What exactly?"
    show pov confused at left
    show pri embarrassed_talk at right
    pri "It’s just… Something that’s been in the back of my mind for a while and I want an honest answer before we proceed with the topic about…"
    show pov confused_talk at left
    show pri embarrassed at right
    pov "Your confession and the whole wedding thing?"
    show pov bored at left
    show pri embarrassed_talk at right
    pri "Y-Yeah…"
    show pov bored_talk at left
    show pri embarrassed at right
    pov "Alright, what is it you wanted to ask?"

    #-This part of the dialogue has 2 variants depending on whether or not Allaway
    # was romanced before Lashley-

    #-If Allaway has been romanced-
    if missallaway_path >= 24:
        show pov shocked at left
        show pri confused_talk at right
        pri "Allaway…"
        pri "You two are together, right?"
        show pov bored_talk at left
        show pri bored at right
        pov "…"
        show pov smirk_talk at left
        show pri bored at right
        pov "You do remember everything, huh?"
        show pov smirk at left
        show pri confused_talk at right
        pri "Y-Yeah…"
        pri "And I… I don’t know how to feel about this fact…"
        show pov bored at left
        show pri bored_talk at right
        pri "Or what to do about it."
        show pov bored_talk at left
        show pri confused at right
        pov "Lashley, please don’t punish Allaway for this."
        show pov confused_talk at left
        show pri shocked at right
        pov "I take full responsibility for this, I pushed her into this and convinced her it was a good idea to-"
        show pov shocked at left
        show pri bored_talk at right
        pri "I don’t mind."
        show pov shocked_talk at left
        show pri bored at right
        pov "…"
        show pov confused_talk at left
        pov "What?"
        show pov confused at left
        show pri bored_talk at right
        pri "W-Well, I do mind a little but for other reasons."
        show pov shocked at left
        show pri embarrassed_talk at right
        pri "What I mean to say is that I won’t be punishing her or doing anything about it."
        show pov shocked_talk at left
        show pri embarrassed at right
        pov "Uhh… I know it’s a  good thing, but I gotta ask."
        pov "How come?"
        show pov confused at left
        show pri bored_talk at right
        pri "Well, after the wild night we shared together, it would be pretty hypocritical of me to reprimand Allaway for having a similar relationship with you, right?"
        pri "I’m not exactly in the moral high ground to be judging others and I already used my position for my own gain far too much lately."
        show pov shocked at left
        show pri embarrassed_talk at right
        pri "S-so I’ll keep your secret."
        show pov shocked_talk at left
        show pri embarrassed at right
        pov "You don’t… mind?"
        show pov shocked at left
        show pri embarrassed_talk at right
        pri "W-Well, I do, but for different reasons."
        pri "Reasons related to the huge elephant in the room here…"
        show pov confused_talk at left
        show pri embarrassed at right
        pov "I suppose we have to talk about that."
        show pov confused at left
        show pri embarrassed_talk at right
        pri "Y-Yeah… We do…"
        pri "B-But, just so you know…"
        pri "I… I wouldn’t mind… You know..."
        show pov confused_talk at left
        show pri sad at right
        pov "What?"
        show pov confused at left
        show pri sad_talk at right
        pri "I-I mean, I’m the homewrecker here, so I can’t just ask you to leave everything and run off with me."
        pri "B-But that’s an option too, I suppose…"
        show pov bored_talk at left
        show pri sad at right
        pov "Okay, let’s go back on topic, for now."
        show pov bored at left
        show pri sad_talk at right
        pri "R-Right!"
        #=RESULT END=

        #-Back to regular dialogue-


    #-If Allaway hasn’t been romanced-
    else:
        show pov shocked at left
        show pri bored_talk at right
        pri "It’s about the other girls you hang out with."
        pri "The ones you went to the party with specifically..."
        show pov confused_talk at left
        show pri bored at right
        pov "What about them?"
        show pov confused at left
        show pri bored_talk at right
        pri "Well… Are you going out with any of them?"
        show pov bored_talk at left
        show pri confused at right
        pov "Didn’t you ask this question before?"
        show pov bored at left
        show pri confused_talk at right
        pri "Y-Yeah, but I wasn’t really myself when I did."
        pri "And after everything that we have been through and all that I’ve done, I can’t help but want to ask again about it."
        show pov smirk_talk at left
        show pri confused at right
        pov "W-Well…"
        show pov smirk at left
        show pri confused_talk at right
        pri "B-But then again, perhaps it’s better if I don’t know."
        show pov confused at left
        show pri bored_talk at right
        pri "I-I mean, I already dug myself into a hole with everything that happened and I feel terrible for all the things I did."
        pri "I don’t think it would help or make me feel any better knowing if you have a sweetheart I also forced you to cheat on along with everything else."
        show pov smirk at left
        show pri embarrassed_talk at right
        pri "S-So let’s keep it a mystery."
        show pov smirk_talk at left
        show pri bored at right
        pov "Alright then, if you are sure…"
        show pov neutral at left
        show pri bored_talk at right
        pri "Was the party fun?"
        show pov neutral_talk at left
        show pri bored at right
        pov "Well, I couldn’t really stick around to really have fun."
        pov "I got roped into a whole thing with being one of my friend’s wingman and that took a whole bunch of time."
        show pov embarrassed at left
        show pri confused_talk at right
        pri "What’s a wingman?"
        show pov embarrassed_talk at left
        show pri shocked at right
        pov "Eh, basically a friend who helps you with hooking up."
        pov "I pretty much just talked to this girl’s friend and kept her busy while he talked to her."
        show pov embarrassed at left
        show pri bored_talk at right
        pri "Oh…"
        pri "And… Was this friend pretty or-?"
        show pov embarrassed_talk at left
        show pri bored at right
        pov "Nothing happened between us, if that’s what you actually want to know."
        show pov neutral_talk at left
        pov "I ended up bouncing out of there before things went either way and ended up having Ian take my place talking to her."
        pov "Last I saw them, they seemed to be hitting it off well!"
        show pov neutral at left
        show pri bored_talk at right
        pri "O-Oh, I see."
        pri "Well, it’s nice to hear Ian is out and trying to socialize."
        show pov neutral_talk at left
        show pri bored at right
        pov "Yeah, hopefully it goes well for him."
        show pov neutral at left
        show pri bored_talk at right
        pri "And did anything else happen at the party?"
        show pov confused_talk at left
        show pri bored at right
        pov "Well, I couldn't really stick around, I got your message asking to meet me outside and after that, I’m pretty sure you can recall everything that happened by yourself."
        show pov smirk at left
        show pri shocked_talk at right
        pri "R-Right."
        show pov smirk_talk at left
        show pri embarrassed at right
        pov "Which brings us back to the main topic, doesn’t it?"
        show pov smirk at left
        show pri embarrassed_talk at right
        pri "I-It sure does…"


        #=RESULT END=

        #-Back to regular dialogue-

    #-Scene continues-
    show pov bored_talk at left
    show pri confused at right
    pov "Lashley…"
    pov "Be completely honest here…"
    show pov confused at left
    show pri sad at right
    pov "Do you really love me?"
    show pov confused at left
    show pri sad_talk at right
    pri "I-I…"
    pri "…"
    show pov shocked at left
    show pri embarrassed_talk at right
    pri "Yes…"
    pri "A-At least I believe I do."
    pri "What I feel for you pushed me to do all of these crazy things…"
    show pov embarrassed at left
    show pri confused_talk at right
    pri "If that’s not love, then what is it?"
    show pov embarrassed_talk at left
    show pri confused at right
    pov "It could be many things, Lashley."
    pov "You said it yourself, your urges got out of control."
    show pov smirk_talk at left
    show pri bored at right
    pov "Are you sure it wasn’t just your repressed lust messing with your head?"
    show pov smirk at left
    show pri bored_talk at right
    pri "W-Well… I don’t know…"
    pri "I’ve never felt something like this before."
    show pri shocked_talk at right
    pri "I mean, sure I’ve gotten plenty of crushes before but I have always kept the idea off my head of actually exploring those feelings."
    show pov embarrassed at left
    show pri confused_talk at right
    pri "So, I don’t really know what actually loving someone really means…"
    show pov confused_talk at left
    show pri confused at right
    pov "Well… Have your feelings for me changed in any way now that you can think straight?"
    show pov confused at left
    show pri bored_talk at right
    pri "…"
    show pov bored_talk at left
    show pri bored at right
    pov "Be honest with me."
    show pov confused_talk at left
    pov "What are you feeling right now?"
    show pov bored at left
    show pri bored_talk at right
    pri "I…"
    pri "I’m feeling worried beyond belief at what could happen if anyone found out about what I did while I was losing it."
    show pov embarrassed at left
    pri "Angry and disgusted of myself for allowing my own body to lose control like I did."
    show pri angry_talk at right
    pri "Horrified at the lengths I was willing to go and went to get you."
    pri "And beyond regretful over the damage I may and have caused to you and others…"
    show pri sad_talk at right
    pri "I’m feeling all of that and so many more things that make me think I’m close to having an anxiety attack!"
    pri "B-But even so…"
    show pov bored_talk at left
    show pri sad at right
    pov "Even so?"
    show pov confused at left
    show pri embarrassed_talk at right
    pri "…"
    pri "Even so…"
    show pov embarrassed at left
    pri "I don’t regret in the slightest what I said to you."
    show pri embarrassed_talk at right
    pri "I-I mean, at least when it comes to telling you how I felt for you."
    show pov shocked at left
    show pri neutral_talk at right
    pri "I certainly regret the way I revealed it to you along with the whole wedding thing."
    show pov confused at left
    show pri shocked_talk at right
    pri "N-not that I wouldn’t want to marry you, I absolutely would but-!"
    pri "W-Wait, that’s not what I meant either!"

    # (Perhaps make the following Lashley lines move automatically at an increased
    # speed to indicate she is babbling? Mc would then interrupt her to snap her out of it)
    show pov shocked at left
    show pri embarrassed_talk at right
    pri "I-I mean, marrying you would be lovely, sure b-but there are many things to do before that!"
    pri "G-Granted, that we have definitely skipped over a few parts of how usual courtship goes."
    pri "I-I mean, we haven’t even gone on a first date and yet we already explored each others bodies thoroughly, something that should normally be reserved until marriage but-"
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "Alright, let’s take it easy now!"
    pov "You are babbling, Lashley."
    show pov embarrassed at left
    show pri shocked_talk at right
    pri "S-Sorry about that…"
    pri "Still though."
    show pri embarrassed_talk at right
    pri "I’m also feeling… Incredibly sad…"
    show pov confused_talk at left
    show pri embarrassed at right
    pov "Sad?"
    show pov confused at left
    show pri embarrassed_talk at right
    pri "Y-Yeah."
    pri "I mean… Maybe it’s because I can think clearly now, but I’m realizing that…"
    pri "Despite how I feel for you and us talking like this…"
    pri "I realize now that no matter how much I may want you…"
    show pov sad at left
    show pri sad_talk at right
    pri "I… Can’t have you..."
    show pov embarrassed_talk at left
    show pri sad at right
    pov "What are you talking about?"
    show pov shocked at left
    show pri sad_talk at right
    pri "I’m your Headmistress, [povname]..."
    pri "Forget the age difference, the fact I'm an adult with a position such as myself over you will never let us have a normal relationship…"
    show pov confused at left
    show pri embarrassed_talk at right
    pri "Even after you graduate, it will continue to be a problem…"
    show pov confused_talk at left
    show pri embarrassed at right
    pov "How so?"
    pov "I mean, you didn’t seem to really care for the consequences regarding your public image a few moments ago."
    show pov confused at left
    show pri confused_talk at right
    pri "I-It’s not my image what I’m worried about, here!"
    pri "[povname], I have sacrificed so many things for my career."
    show pri embarrassed_talk at right
    pri "And right now I’d be willing to throw them all to the trash if it means being with you…"
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "But I realize that I can not ask you to make the same sacrifice..."
    pri "Because so far I have only been leading you around to what I wanted… Yet neer once ask what you want…"
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "…"
    show pov sad at left
    show pri confused_talk at right
    pri "S-So…"
    show pov confused at left
    show pri bored_talk at right
    pri "Before I ask and… You must likely reject me after everything that I’ve done so far…"
    show pov shocked at left
    show pri confused_talk at right
    pri "Can I be selfish one more time and ask one final thing from you?"
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Of course."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Thank you…"
    pri "[povname]... As much as I hate to say it, you and I know that one of these days my urges are going to rise up again."
    show pri shocked_talk at right
    pri "I mean, I doubt it will ever get as bad as it did again!"
    pri "T-That was me releasing years of pent up frustration on you."
    show pov shocked at left
    show pri embarrassed_talk at right
    pri "B-But…"
    pri "W-Well, right now I’m feeling the best I’ve ever felt in years and I know for sure no other method is gonna work on me anymore…"
    show pri confused_talk at right
    pri "S-So…"
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "Are you getting what I’m trying to ask of you?"
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "I have an idea."
    show pov confused at left
    show pri embarrassed_talk at right
    pri "O-OK, good..."
    show pov smirk_talk at left
    show pri shocked at right
    pov "But I want to hear you say it regardless."
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "R-Right…"
    pri "[povname], I-If I ever feel my urges start to become a bother…"
    show pri confused_talk at right
    pri "C-Can I count on you to please come and help me take care of them?"
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "E-Even if you don’t want to have anything to do with me aside from that…"
    show pov neutral_talk at left
    show pri embarrassed at right
    pov "You’d still want me to come help you even if I cut you off like that?"
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "W-Well, yeah…"
    pri "You are the one person in my life who I am completely open to."
    show pri confused_talk at right
    pri "The one who knows all the aspects of me, even the terrible things I try to keep hidden…"
    show pov  at left
    show pri embarrassed_talk at right
    pri "You know me in a way no other person on this earth does and..."
    pri "Well I wouldn’t feel comfortable doing this with anyone else."
    show pov confused at left
    show pri confused_talk at right
    pri "S-So… Even if you want to cut me off from your life for what I did, I still want to ask- no, I want to beg you to let me be selfish this one final time..."
    show pov bored_talk at left
    show pri shocked at right
    pov "No one else but me will work?"
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "N-Not one man or woman on this earth will."
    pri "Not if I want to at least enjoy the whole thing a bit and not feel ashamed of myself afterwards."
    show pov bored_talk at left
    show pri embarrassed at right
    pov "Hmmm, is that so?"
    show pov bored at left
    show pri embarrassed_talk at right
    pri "I swear to God it’s the honest and complete truth."
    show pov bored_talk at left
    show pri embarrassed at right
    pov "I see…"
    show pov bored at left
    show pri confused_talk at right
    pri "..."
    pri "S-So…?"
    show pri embarrassed_talk at right
    pri "What do you say?"
    show pov neutral_talk at left
    show pri shocked at right
    pov "Oh, I’m in."
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "I know this is a difficult thing to ask of you."
    pri "But I promise you that no one else but you will-"
    show pov smirk at left
    show pri shocked_talk at right
    pri "…"
    show pri confused_talk at right
    pri "Wait, what did you say?"
    show pov neutral_talk at left
    show pri confused at right
    pov "I said I’ll do it."
    show pov neutral at left
    show pri shocked_talk at right
    pri "A-Are you sure?"
    pri "I understand this is quite a lot for me to ask from someone that doesn’t want to see me again and-"
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "Lashley, calm down."
    show pov neutral_talk at left
    show pri confused at right
    pov "I’m more than sure."
    pov "I’ll help you out whenever you need it."
    show pov neutral at left
    show pri confused_talk at right
    pri "D-do you mean it?"
    show pov smirk_talk at left
    show pri confused at right
    pov "I’ll say it as many times as you need."
    pov "I’ll do it, Lashley."
    show pov neutral at left
    show pri shocked_talk at right
    pri "O-Oh, [povname]. I don’t know how to begin to thank you!"
    pri "You have no idea how much this means to me!"
    show pov neutral_talk at left
    show pri embarrassed at right
    pov "I probably don’t, but you got something wrong out of all of this."
    show pov smirk at left
    show pri confused_talk at right
    pri "I did?"
    show pov smirk_talk at left
    show pri confused at right
    pov "Of course you did."
    show pov embarrassed_talk at left
    pov "I don’t know where you got the idea that I never want to see you again or want to cut you out of my life."
    show pov smirk_talk at left
    show pri sad at right
    pov "I don’t feel that way at all!"
    show pov shocked_talk at left
    show pri confused at right
    pov "Neither do I hate you!"
    show pov embarrassed at left
    show pri confused_talk at right
    pri "You don’t?"
    pri "Even after all I did?"
    show pov neutral_talk at left
    show pri confused at right
    pov "Of course not!"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "I mean, sure, I’m upset over the things you did, but I don’t hate you at all!"
    pov "Besides, you weren’t really acting with your whole brain and rather were letting your horny side take over."
    show pov neutral_talk at left
    pov "Happens to the best of us."
    pov "Can’t even tell you how many times I’ve made a stupid decision because I was turned on."
    show pov smirk_talk at left
    show pri sad at right
    pov "That’s why they say you never make decisions when you are angry, depressed or horny!"
    show pov shocked at left
    show pri sad_talk at right
    pri "B-but… I lied to you!"
    pri "I abused your trust and did so many horrible things!"
    show pov bored_talk at left
    show pri sad at right
    pov "Which I’m claiming you did in a lapse of judgment and expecting you to make up for them with time."
    show pov neutral_talk at left
    show pri embarrassed at right
    pov "Come on Lashley, I know plenty of people who had a lapse in judgment themselves when they were horny only to regret it once the bill hits them after they had their orgasm and the post nut daze fades away."
    pov "How do you think recovering simps feel when their goddess no longer satisfies their needs or changes in a way they don’t approve?"
    show pov neutral at left
    show pri confused_talk at right
    pri "O-Okay that’s a fair point, but still-"
    show pov bored_talk at left
    show pri embarrassed at right
    pov "Lashley."
    pov "I’m seriously not angry and I definitely don’t hate you."
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "You… You really, really don’t?"
    show pov neutral_talk at left
    show pri confused at right
    pov "I really, really don’t..."
    show pov confused at left
    show pri confused_talk at right
    pri "Then… What do you feel about me?"
    show pov bored_talk at left
    show pri confused at right
    pov "Well…"

    #-The following dialogue occurs in the Mc’s head-
    show pov embarrassed at left
    pov "{i}What do I feel about Lashley?{/i}"
    pov "{i}I definitely don’t hate her and can’t blame her much for what she did after I had a hand on getting her like this.{/i}"
    show pov sad at left
    pov "{i}I have to make a choice about how I feel.{/i}"
    show pov shocked at left
    pov "{i}What I say right now is definitely important and will affect my relationship with Lashley forever.{/i}"
    show pov embarrassed at left
    pov "{i}There is no turning back from this…{/i}"

    menu:
        "Become her lover.":
            #-If “Become her lover” was picked-
            $ eye2eye_lashleys_lover_chosen = True
            show pov smirk_talk at left
            show pri embarrassed at right
            pov "Lashley do you even need me to say it?"
            show pov bored_talk at left
            show pri shocked at right
            pov "Ever since I laid eyes on you for the first time, I knew I wanted you."
            show pov embarrassed_talk at left
            pov "Sure, back then it was just a fantasy that I never thought could go beyond just that."
            show pov neutral_talk at left
            pov "But as I got to know you, I couldn’t help but to find myself wanting more of you."
            show pov embarrassed_talk at left
            pov "I mean, how could I not?"
            pov "You are hot as all hell and yet you are still an adorable, quirky little goober who I love to tease."
            show pov embarrassed at left
            show pri shocked_talk at right
            pri "W-Wait..."
            pri "D-Does that mean that you…?"
            show pov embarrassed_talk at left
            show pri shocked at right
            pov "Yes, Lashley."
            show pov neutral_talk at left
            show pri confused at right
            pov "I feel the same way for you."
            show pov neutral at left
            show pri shocked_talk at right
            pri "…!"
            show pov neutral_talk at left
            show pri shocked at right
            pov "I’ve felt the way for you way before things got out of control."
            show pov embarrassed_talk at left
            pov "And I don’t want us to just remain as friends with benefits."
            show pri embarrassed at right
            pov "I want you to explore and find out exactly what romance is."
            show pov neutral_talk at left
            show pri sad at right
            pov "And I want you to keep experiencing all of your firsts with me"
            show pov neutral at left
            show pri sad_talk at right
            pri "Y-You…"
            show pov neutral_talk at left
            show pri sad at right
            pov "I want to be there for you when you need me."
            pov "I want to share all those moments you missed out on."
            show pov smirk_talk at left
            show pri embarrassed at right
            pov "I want to be everything you have always dreamed of having one day and to fill that need you have for actual affection."
            show pov smirk at left
            show pri embarrassed_talk at right
            pri "You… You actually love…?"
            show pov neutral_talk at left
            show pri embarrassed at right
            pov "Yes Lashley."
            show pov confused_talk at left
            pov "Despite everything that happened and how difficult things might be for us in the future, having to hide our relationship from everybody else…"
            show pov bored_talk at left
            show pri smirk at right
            pov "Despite all of that, I still feel the same way you do."
            show pov neutral_talk at left
            show pri neutral at right
            pov "I love you too."

            # -Lashley pounces at the Mc, kissing him passionately while starting
            # to cry once again, the two make out for a couple seconds before Lashley
            # breaks the kiss and hugs him for dear life, still crying her eyes out-

            scene bg eye2eye_1
            with hpunch
            $ renpy.pause(1,hard=True)
            show bg eye2eye_2
            $ renpy.pause(0.8,hard=True)
            show bg eye2eye_1
            $ renpy.pause(0.8,hard=True)
            show bg eye2eye_2
            $ renpy.pause(1,hard=True)

            scene bg lashleybedroom_day
            with fade
            show pov neutral at left
            show pri embarrassed_talk at right
            with dissolve
            pri "Thank you…"
            show pov embarrassed at left
            show pri neutral_talk at right
            pri "Oh sweet and merciful God, thank you…"
            pri "This… This is all I’ve ever wanted…"
            show pov neutral at left
            show pri shocked_talk at right
            pri "I love you, [povname]."
            show pov embarrassed at left
            show pri neutral_talk at right
            pri "I love you, I love you, I love you, I love you, I love you."
            show pri smirk_talk at right
            pri "I’ll say it a million times if I have to."
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "I love you with every fiber of my being!"
            show pov smirk_talk at left
            show pri neutral at right
            pov "I know you do."
            show pov neutral at left
            show pri smirk at right
            pov "I love you too…"
            show pov confused at left
            show pri embarrassed_talk at right
            pri "Don’t ever leave me…"
            pri "Please, don’t you ever leave me!"
            show pov embarrassed at left
            show pri sad_talk at right
            pri "I can’t… I can’t go on without you…"
            show pov neutral at left
            show pri bored_talk at right
            pri "Not after I spent so long trying to find you…"
            show pov neutral_talk at left
            show pri embarrassed at right
            pov "I’m not going anywhere, Lashley…"
            pov "You finally found me…"

            #-Lashley continues to cry and the scene fades to black-

                #=RESULT END=
                #=OR=
        "Remain her friend.":
            #-If “Remain her friend” was picked-
            show pov bored_talk at left
            show pri sad at right
            pov "Lashley, nothing has changed between us."
            pov "You were and have always been my friend."
            show pov embarrassed at left
            show pri sad_talk at right
            pri "E-Even after everything I did?"
            show pov sad_talk at left
            show pri sad at right
            pov "Yes, Lashley."
            pov "Even after all of that."
            show pov embarrassed at left
            show pri sad_talk at right
            pri "…"
            pri "But it doesn’t go beyond that, does it?"
            show pov confused_talk at left
            show pri confused at right
            pov "…"
            pov "Not right now."
            show pov confused at left
            show pri confused_talk at right
            pri "Right now?"
            show pov smirk_talk at left
            show pri sad at right
            pov "Yeah."
            show pov bored_talk at left
            show pri confused at right
            pov "Look, Lashley. I care about you a lot."
            pov "I genuinely don’t know what I would do without you at this point."
            show pov smirk_talk at left
            show pri sad at right
            pov "I love spending time with you and our conversations about anything and everything."
            show pov confused_talk at left
            pov "But I don’t think that what you need right now is a boyfriend or a lover."
            show pov confused at left
            show pri bored_talk at right
            pri "Then what do I need?"
            show pov embarrassed at left
            show pri shocked_talk at right
            pri "What am I missing, [povname]?"
            show pov embarrassed_talk at left
            show pri shocked at right
            pov "How about a good friend?"
            show pov embarrassed at left
            show pri confused_talk at right
            pri "A… Good friend?"
            show pov neutral_talk at left
            show pri sad at right
            pov "Yeah!"
            pov "Lashley, you don’t know the first thing there is about a healthy relationship."
            show pov embarrassed_talk at left
            show pri embarrassed at right
            pov "I’m really sorry for saying it like this, but you are downright starved for affection."
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "That… May have some merit to it…"
            show pov neutral_talk at left
            show pri embarrassed at right
            pov "Right?"
            pov "Lashley, I understand and accept your feelings."
            show pov embarrassed_talk at left
            pov "But it’s because I love you that I can’t be more than your friend right now."
            show pov confused at left
            show pri sad_talk at right
            pri "I… I don’t understand…"
            show pov confused_talk at left
            show pri sad at right
            pov "I want your first real relationship to be one where you can be yourself and learn what a healthy relationship is actually like."
            show pov embarrassed_talk at left
            pov "So… I’m not saying no and shooting you down."
            pov "I’m just saying not now while you learn what being actual  friends is like."
            show pov shocked at left
            show pri confused_talk at right
            pri "So you're saying there's a chance later on?"
            show pov bored_talk at left
            show pri confused at right
            pov "Maybe."
            pov "Who knows what the future might bring us?"
            show pov embarrassed_talk at left
            show pri sad at right
            pov "But right now, let’s start off as friends."
            show pov confused_talk at left
            show pri embarrassed at right
            pov "Weird, unexpected and with a very weird arrangement of having sex from time to time, but still friends."
            show pov confused at left
            show pri smirk_talk at right
            pri "Real… Actual friends?"
            show pov embarrassed_talk at left
            show pri bored at right
            pov "I know that… Maybe it wasn’t what you wanted or were expecting but…"
            pov "It’s because I want to make you happy that I want to make sure you learn all the aspects there is to know about a relationship before jumping to something serious right away."
            show pov neutral_talk at left
            pov "We can go to the movies, talk for hours in your office or just meet up somewhere to have dinner and talk!"
            pov "We can still do all the things you want to experience, Lashley."
            show pov embarrassed_talk at left
            show pri confused at right
            pov "Nothing has changed between us."
            show pov neutral_talk at left
            show pri shocked at right
            pov "I’m not going to leave you alone."
            show pov neutral at left
            show pri shocked_talk at right
            pri "…!"
            show pov neutral_talk at left
            show pri confused at right
            pov "I’ll be there for all the important moments you want someone to support you."
            pov "I’ll be there when you feel the need to vent and have someone listen."
            show pov embarrassed_talk at left
            pov "I’ll be there if you are bored in the middle of night and just want to text someone until you fall asleep."
            pov "I’ll do all of that and more."
            show pov neutral_talk at left
            show pri sad at right
            pov "I won’t let you be alone again."
            #-Lashley pounces at the Mc, this time only hugging him while starting to cry once again, the two continue to hug as Lashley keeps crying her eyes out-"
            show pov neutral at left
            show pri sad_talk at right
            pri "Thank you…"
            pri "[povname], thank you… I..."
            show pov confused at left
            pri "This… This is all I’ve ever wanted…"
            show pov embarrassed at left
            show pri embarrassed_talk at right
            pri "To hear someone say…"
            pri "For them to promise to be there..."
            show pov embarrassed_talk at left
            show pri embarrassed at right
            pov "I know you did…"
            show pov neutral at left
            show pri sad at right
            pov "I’m here now, Lashley."
            show pri neutral at right
            pov "I’ll always be."
            show pov embarrassed at left
            show pri neutral_talk at right
            pri "Don’t ever leave me…"
            show pov shocked at left
            show pri shocked_talk at right
            pri "Please, don’t you ever leave me!"
            show pov embarrassed at left
            show pri sad_talk at right
            pri "I can’t… I can’t go on without you…"
            pri "Not after everything…"
            show pov neutral at left
            show pri confused_talk at right
            pri "Please promise me you’ll stay!"
            show pov neutral_talk at left
            show pri sad at right
            pov "I’m not going anywhere, Lashley…"
            pov "I swear it…"

            #-Lashley continues to cry and the scene fades to black-

            #    =RESULT END=

            #-End of result leads to a fade to black as the scene then ends-

            #=SCENE END=
            #	=CHOICE END=

    $ principallashley_path = 27

    scene black with fade
    jump lbl_uptownmap_setup
