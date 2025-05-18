## Sister's Nightmare ##
label lbl_sisters_nightmare:

    scene black
    with fade
    idk "[povname]..."
    idk "[povname], come on."
    idk "Please, get up..."
    pov "Mmmmn..."
    idk "Please, [povname]."
    pov "Mmm..."

    scene bg sistersnightmare_1
    with fade
    show bg sistersnightmare_2
    pov "Wha?"
    pov "[sister]?"
    show bg sistersnightmare_3
    sis "Ummm... hey..."
    show bg sistersnightmare_4
    pov "Jesus, what time is it?"
    show bg sistersnightmare_5
    sis "Around 3 am..."
    show bg sistersnightmare_6
    pov "Ugh..."
    pov "Why did you wake me up?"
    show bg sistersnightmare_5
    sis "I..."
    sis "I um..."
    sis "Can I sleep here tonight?"
    show bg sistersnightmare_7
    pov "Say what again?"
    show bg sistersnightmare_8
    sis "Ugh!"
    sis "Just make some room!"
    show bg sistersnightmare_9
    pov "Woah, easy there!"

    scene bg sistersnightmare_10
    with dissolve
    pov "You do realize I'm completely naked under here, right?"
    show bg sistersnightmare_11
    sis "It's nothing I haven't seen before."
    show bg sistersnightmare_10
    pov "..."
    pov "{i}*Sigh*{/i} Why are you here in my bed, [sister]?"
    show bg sistersnightmare_11
    sis "... Promise you won't laugh?"
    pov "Are you really in the position to negotiate?"
    show bg sistersnightmare_10
    pov "You pretty much raided your way into my bed."
    sis "Don't be an ass now."
    pov "Alright, alright!"
    show bg sistersnightmare_11
    pov "Geez."
    pov "Must be something pretty big if it has you so worked up out of nowhere..."
    show bg sistersnightmare_10
    sis "I had a nightmare..."
    pov "Is that it? Usually I just fall asleep after realizing that it's not actually real. Y'know, like a grown up should."
    sis "Shut up..."
    show bg sistersnightmare_11
    sis "I know it's stupid, but I really don't want to sleep alone tonight!"
    sis "I need to know you're alright..."

    menu:
        "What was the dream about?":
            show bg sistersnightmare_10
            pov "I'm curious as to what that dream is about."
            sis "I don't really want to talk about it."
            pov "What? Come on."
            pov "You pretty much barge into my bed without asking and now you won't even tell me why?"
            pov "I deserve that at least."
            show bg sistersnightmare_11
            sis "Look, I know it's not fair but I really don't want to remember the details."
            sis "Nor do I think I can. Y'know how dreams are."
            sis "One minute it seems like they're real and next minute you can't even remember what you were afraid of."
            show bg sistersnightmare_10
            pov "Tsk- you're a real tease, you do realise that, right?"
            sis "Ugh!"
            show bg sistersnightmare_11
            sis "Fine! Just..."
            sis "Just promise you won't bring it after I tell you, ok?"
            pov "It's just a nightmare, how bad can it b-?"
            show bg sistersnightmare_12
            with dissolve
            $ renpy.pause(1,hard=True)
            show bg sistersnightmare_13
            with dissolve
            $ renpy.pause(0.6,hard=True)
            show bg sistersnightmare_14
            with dissolve
            $ renpy.pause(1,hard=True)
            show bg sistersnightmare_15
            with dissolve
            sis "There! Now we are both naked, happy?!"
            pov "Not what I meant, but okay..."
            sis "I- thought that you wanted me to-"
            sis "Because I'm a tease-"
            sis "..."
            sis "Shut up and be grateful already, you little pervert."
        "I can take care of myself.":
            show bg sistersnightmare_10
            pov "You know, I can take care of myself. You don't have to worry about me."
            if skill_str <= 7:
                sis "Yeah, right, I could crawl inside you for warmth with how flubby you are."
                show bg sistersnightmare_12
                with dissolve
                $ renpy.pause(1,hard=True)
                show bg sistersnightmare_13
                with dissolve
                $ renpy.pause(0.6,hard=True)
                show bg sistersnightmare_14
                with dissolve
                pov "What are you doing?"
                show bg sistersnightmare_15
                with dissolve
                sis "Well, I'm cold so I'm levelling the playing field and using your chubbiness to keep me warm."
                sis "Survival strategy, skin to skin contact is more effective than if you had clothes on."
                pov "I'm glad to be of service."
                sis "Hehehe, don't take it the wrong way, you're not THAT chubby. It's mostly your muffin top."
            elif skill_str <= 14:
                sis "Look, I'm sure you're confident in your own strength but you're no Hulkman either!"
                pov "Wow, thanks for the vote of confidence."
                if winc == 0:
                    sis "Thats what [sisrole]s are for, isn't it?"
                    show bg sistersnightmare_11
                    sis "Reminding our [povsisrole]s of their faults."
                else:
                    sis "Thats what sisters are for, isn't it?"
                    show bg sistersnightmare_11
                    sis "Reminding our brothers of their faults."
                pov "What would I ever do without you?"
                sis "Have a more boring existence, that's for sure."
                pov "I suppose you're right."
                show bg sistersnightmare_12
                with dissolve
                $ renpy.pause(1,hard=True)
                show bg sistersnightmare_13
                with dissolve
                $ renpy.pause(0.6,hard=True)
                show bg sistersnightmare_14
                with dissolve
                pov "What are you doing?"
                sis "Well, since you're naked underneath the covers I might as well undress too."
                show bg sistersnightmare_15
                with dissolve
                sis "I mean, I sleep nude just like you do."
            else:
                sis "I-I know that!"
                sis "Don't think I haven't noticed how much you've been working out lately."
                sis "You..."
                show bg sistersnightmare_11
                sis "You look really good..."
                pov "Hehe, appreciate it, [sister]."
                pov "What do you think? Movie star body?"
                sis "Well, you're no Chris Hemmingsworth or Ebans, but you make a nice enough substitute."
                show bg sistersnightmare_10
                pov "Wow, that was somehow both an insult and the compliment at the same time."
                pov "I'm impressed."
                sis "I saved the best pickup lines for the best."
                show bg sistersnightmare_12
                with dissolve
                $ renpy.pause(1,hard=True)
                show bg sistersnightmare_13
                with dissolve
                $ renpy.pause(0.6,hard=True)
                show bg sistersnightmare_14
                with dissolve
                pov "What are you doing now?"
                sis "It suddenly got hot in here and I wanted to take off my clothes, ok?!"
                show bg sistersnightmare_15
                with dissolve
                sis "I sleep nude anyway so I was gonna do it sooner or later."
    show bg sistersnightmare_16
    pov "...!"
    show bg sistersnightmare_17
    sis "Hm?"
    show bg sistersnightmare_16
    pov "Your-"
    sis "Shh.. just loosen up, dude."
    show bg sistersnightmare_17
    sis "A little massage doesn't hurt anyone."
    show bg sistersnightmare_16
    pov "..Wh-"
    show bg sistersnightmare_17
    pov "Why did you even bother to come in here with clothes if you were planning on taking them off anyway?"
    if winc == 0:
        sis "Just in case [missus] or [dadname] heard me sneaked out to your room."
        show bg sistersnightmare_16
        pov "Our rooms are literally 2 steps away from each other. I don't think they would have jumped out of bed and made it to the hallway fast enough to catch you."
        sis "I mean like, just in case they were already out or something or just bad timing."
        show bg sistersnightmare_17
        sis "With [missus] I would have just lied about going to the bathroom, but with [dadname]..."
    else:
        sis "Just in case Mom or Dad heard me sneaking out to your room."
        show bg sistersnightmare_16
        pov "Our rooms are literally 2 steps away from each other. I don't think they would have jumped out of bed and made it to the hallway fast enough to catch you."
        sis "I mean like, just in case they were already out or something or just bad timing."
        show bg sistersnightmare_17
        sis "With Mom I would have just lied about going to the bathroom, but with Dad..."
    sis "Well, I'm nowhere near comfortable enough to be in the same room as him."
    show bg sistersnightmare_16
    sis "I'm sure I would have a panic attack if he caught me naked in the middle of the night."
    sis "Not to mention I'm also afraid of what he might do if he saw me like that..."
    show bg sistersnightmare_17
    pov "You don't think he would- you know... Do you?"
    pov "I know he's been an asshole and a jerk lately, but I really don't think he'd go that far... right?"
    show bg sistersnightmare_16
    sis "I don't know, [povname]..."
    sis "As a woman I'm more sensitive to these sorts of things."
    show bg sistersnightmare_17
    sis "I have felt the way he looks at me lately."
    sis "Perhaps I'm overthinking it, maybe he is just pissed at me after all that's happened."
    show bg sistersnightmare_16
    sis "But I really don't like the way he stares at me."
    sis "I just don't want to risk it."
    show bg sistersnightmare_17
    pov "If he tries to even lay a finger on you, he'll end up in a whole body cast."
    pov "Just yell and I'll come running to save you."
    show bg sistersnightmare_16
    sis "You really would come for me, wouldn't you?"
    sis "No matter in how much trouble I get myself into?"
    show bg sistersnightmare_17
    pov "Of course!"
    pov "You and me against the world, right?"
    pov "I'll always come save you."
    show bg sistersnightmare_16
    sis "..."
    show bg sistersnightmare_18
    with dissolve
    sis "{i}*Chu- chu chuuu~*{/i}"
    sis "..."
    show bg sistersnightmare_19
    sis "You were in a maze running from something."
    pov "What?"
    show bg sistersnightmare_18
    sis "In my nightmare."
    sis "You seemed to be running for your life."
    show bg sistersnightmare_19
    sis "Something was after you, like a blur of black and white. I'm not sure what it was."
    sis "I want to say that it may have been a ghost...?"
    show bg sistersnightmare_18
    pov "You recall anything else?"
    sis "I was watching over it... Like on a tv or something."
    show bg sistersnightmare_19
    sis "Someone was next to me but I don't recall how they looked like."
    sis "..."
    show bg sistersnightmare_18
    sis "I know I had the option to save you but I don't know why I was so scared to do so."
    sis "I couldn't move my body as that thing got closer and closer to you."
    show bg sistersnightmare_19
    sis "It's like I was having a double sleep paralysis, one that I can't wake up from, and one in the dream I'm having."
    sis "I couldn't do anything as it kept closing in on you and eventually..."
    show bg sistersnightmare_18
    sis "..."
    sis "It lunged at you and you screamed..."
    sis "I almost jumped out of my bed and screamed myself."
    show bg sistersnightmare_19
    pov "It was just a dream, [sister]. It wasn't real."
    sis "It felt abnormally real, [povname]."
    show bg sistersnightmare_18
    sis "..."
    sis "I can't lose you, [povname]."
    sis "Not after I finally found you. The real you."
    show bg sistersnightmare_19
    pov "I'm not going anywhere."
    pov "I promise you're not going to lose me that easily."
    show bg sistersnightmare_18
    if winc == 0:
        pov "No monster can stop your [povsisrole]."
    else:
        pov "No monster can stop your bro-bro."
    sis "You don't understand, [povname]!"
    show bg sistersnightmare_19
    sis "That... That thing scared me half to death!"
    pov "And it was also just in your head."
    show bg sistersnightmare_18
    pov "I'm not just going to disappear on you like that."
    sis "Promise?"
    show bg sistersnightmare_19
    pov "Yeah, promise."
    sis "Will you help me keep the nightmares away for tonight then?"
    show bg sistersnightmare_18
    pov "Tonight and any other night you need to, my door is always open."
    sis "Technically it's always closed. Like it's actually a little stuffy in here now that I mention it."
    show bg sistersnightmare_19
    pov "Hahaha- come into my room, raid my bed, and then insult my room."
    if winc == 0:
        sis "How to be a great [sisrole] 101."
    else:
        sis "How to be a great sibling 101."
    show bg sistersnightmare_18
    sis "Hehehe~ {i}*Inhale*{/i}"
    sis "{i}*Exhale*{/i}"
    show bg sistersnightmare_19
    sis "Thank you."
    pov "Don't mention it."
    show bg sistersnightmare_18
    pov "Good night, [sister]."
    sis "Good night..."
    show bg sistersnightmare_19
    sis "I love you, [povname]."
    pov "I love you too."
    
    $ sister_path = 34.5

    scene black
    with fade
    $ renpy.pause()
    "The next morning..."

    jump lbl_mybedroom_night_sleep_1
