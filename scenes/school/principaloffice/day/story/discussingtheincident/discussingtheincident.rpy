## Discussing the Incident ##
label lbl_discussing_the_incident:
    default discussingtheincident_monitored = 0
    default discussingtheincident_threeghans = 0

    scene bg discussingtheincident_19
    with fade
    pov "Director Lashley?"
    show bg discussingtheincident_7
    with vpunch
    pri "Hmm...?"
    show bg discussingtheincident_8
    pri "O-Oh! [povname]!"
    show bg discussingtheincident_6
    pri "P-Please, come in, come in!"
    show bg discussingtheincident_7
    pov "Are you okay, Director Lashley?"
    pov "You seem... on edge?"
    show bg discussingtheincident_6
    pri "N-No, I- mean.. Yes! Hehe, never better! Hehehe."
    show bg discussingtheincident_5
    pri "{i}*Clears throat*{/i}"
    show bg discussingtheincident_10
    pri "Do you know why I called you here?"

    menu:
        "Not for my good grades.":
            if skill_cha >= 3:
                if skill_int >= 14:
                    $ skill_cha -= 3
                    if principallashley_points <= 9:
                        $ principallashley_points += 1
                    else:
                        $ principallashley_points = 10
                    $ renpy.notify("You used 3 Charisma Points\nYour relationship with Ms. Lashley has increased")
            else:
                pass
            show bg discussingtheincident_11
            pov "I assume it's not for my good grades."
            show bg discussingtheincident_6
            pri "Sadly, no."
            show bg discussingtheincident_2
            pri "I am however glad to hear that you're taking your studies seriously."
            pri "Keep it up and next time you're here, it will be to receive an award for academic excellence!"
            show bg discussingtheincident_6
            pri "But your grades aside, this is about you and what's been circling around recently."
        "My joyous company.":
            show bg discussingtheincident_11
            pov "You missed me and my joyous company?"
            show bg discussingtheincident_6
            pri "Well, I'm happy to see this whole situation hasn't bothered you too much at all."
            pri "It's such a relief to see you still smiling and cracking jokes despite what you went through."
            show bg discussingtheincident_13
            pri "I suppose I have to admit that seeing the news of your disappearance did fill me with worry."
            show bg discussingtheincident_10
            pri "I would appreciate it if you refrain from vanishing out of the blue like that in the future."
            show bg discussingtheincident_9
            pov "I can hope that I won't, Director Lashley"
            show bg discussingtheincident_6
            pri "I will pray for it not to happen, [povname]. Don't you worry."
        "The incident recently.":
            show bg discussingtheincident_5
            pov "If my detective senses are right, I'm guessing it's about the incident regarding me recently."
            show bg discussingtheincident_14
            pri "That really comes to no surprise."
            pri "I'm sure you're going through a rough time right now."
            pri "I can't imagine the things you hear and the pain you feel."
    show bg discussingtheincident_5
    pri "..."
    show bg discussingtheincident_14
    pri "You caused quite a commotion yesterday."
    show bg discussingtheincident_10
    pri "This is a small town so news spread like wildfire."
    if winc == 0:
        pri "Not to mention the fact your [mumrole] called the other night asking if we had seen you."
    else:
        pri "Not to mention the fact your mother called the other night asking if we had seen you."
    show bg discussingtheincident_9
    pov "In my defense, I didn't plan for all this to happen. I may have just been in a bad place at a bad time."
    show bg discussingtheincident_6
    pri "I believe you had no control over what you were doing."
    pri "I'm with you and I will back you up 120 percent."
    pri "I'm just glad to know you're safe and sound in the grand scheme of things."
    show bg discussingtheincident_10
    pri "The police are still investigating into the matter, but know that the staff of this university will be keeping a close eye on you to prevent this from happening again."
    show bg discussingtheincident_9
    pov "Close eye? Like, what do you mean?"
    show bg discussingtheincident_6
    pri "Oh! It's nothing drastic. No rigging of cameras and mics or anything like that."
    pri "Just, literally a close eye."
    show bg discussingtheincident_10
    pri "I hope you understand, it's just standard procedure."

    menu:
        "Is that a good or bad thing?":
            $ discussingtheincident_monitored = 1
            show bg discussingtheincident_9
            pov "Is that a good or bad thing?"
            show bg discussingtheincident_10
            pri "Depends on how you look at it."
            show bg discussingtheincident_8
            pri "We as an institution care for the safety of all of our students."
            show bg discussingtheincident_4
            pri "It is my job as the administrator to provide measures to ensure that safety."
            show bg discussingtheincident_6
            pri "I care about my students and therefore, I care about you, [povname]."
        "I don't like the idea of being monitored.":
            show bg discussingtheincident_5
            pov "I'm not too fond of the idea of being monitored."
            pov "It's not that comforting of a thought."
            show bg discussingtheincident_6
            pri "I don't blame you."
            show bg discussingtheincident_14
            pri "But sadly that's how things are."
            show bg discussingtheincident_10
            pri "You worried a lot of people with this little stunt."
            show bg discussingtheincident_4
            pri "And even if it wasn't entirely your fault, it's my duty as an educator to keep you from straying down a bad path."
            show bg discussingtheincident_8
            pri "I made an oath when I became administrator, that I would take all means necessary to keep my students safe."
            show bg discussingtheincident_4
            pri "Whether they like it or not."
            show bg discussingtheincident_3
            pov "So you're all going to be looking over me like a bunch of security cameras?"
            show bg discussingtheincident_4
            pri "Just until we know you're safe and you have proven that you can take care of yourself."
        "I can take care of myself.":
            show bg discussingtheincident_5
            pov "That is really not needed. I can take care of myself."
            show bg discussingtheincident_6
            pri "You're very brave, [povname]."
            pri "I don't doubt that, not for a single minute."
            show bg discussingtheincident_14
            pri "But it would let all of us who care for you sleep easier at night knowing one of us is looking after you."
            show bg discussingtheincident_6
            pri "I'm happy to know that you're confident in your own strength."
            show bg discussingtheincident_14
            pri "But until we are sure things are back to normal, please just let us help."
            show bg discussingtheincident_7
            pov "With all due respect, Director Lashley; I'm not a baby. This is violating my privacy and my rights."
            show bg discussingtheincident_6
            pri "I know that."
            pri "I promise this will only be temporary."
            show bg discussingtheincident_2
            pri "If you let us help and don't fight it, I guarantee it will all be over before you know it."
    show bg discussingtheincident_6
    pri "Sounds like a deal?"

    menu:
        "Absolutely.":
            show bg discussingtheincident_1
            pov "Absolutely. I completely understand why this needs to be done."
            show bg discussingtheincident_2
            pri "Good!"
            pri "I'm glad to see you understand."
            show bg discussingtheincident_6
            pri "Normally people in your situation try their hardest to object."
            show bg discussingtheincident_2
            pri "I'm so happy you're willing to give us a chance!"
        "I guess I can give it a shot.":
            show bg discussingtheincident_1
            pov "I guess I can give it a shot."
            pov "If it's for my safety and what not."
            show bg discussingtheincident_6
            pri "That's all I'm asking, [povname]."
            pri "I know this is hard for you, but we'll get through this together."
            if discussingtheincident_monitored == 1:
                show bg discussingtheincident_2
                pri "Knowing you're still willing to give me a chance; despite not liking the idea, means the world to me."
                show bg discussingtheincident_6
                pri "Thank you for trusting me, [povname]."
                show bg discussingtheincident_2
                pri "I promise, I'm only doing this with your best interests in mind."
        "It sounds like a terrible deal.":
            show bg discussingtheincident_7
            pov "I sounds like a terrible, horrible deal."
            pov "I don't want to constantly be on everyone's radar."
            pov "I have the right to feel comfortable in my own personal bubble."
            show bg discussingtheincident_13
            pri "..."
            pov "Sorry, not sorry. I do not want green eggs and ham."
            show bg discussingtheincident_3
            pov "I don't want to be monitored, Sam I am."
            show bg discussingtheincident_4
            pri "Well, I'm sorry to hear that, [povname]."
            pri "But, I'm afraid you don't have much of a choice on the matter."
            pri "This was an agreement reached with your parents and Officer Mina to prevent this incident from appearing in your permanent record."
            pri "It's sad to know we are going to have to force this on you, but you're not giving me much of a choice."
    show bg discussingtheincident_10
    pri "Now, keep in mind that since this is your first misdeed, I'm not going to punish you."
    show bg discussingtheincident_3
    pov "I still don't really understand why you're acting like {i}I'm{/i} the one in troubl-"
    show bg discussingtheincident_4
    pri "But, shall this behaviour continue, I will be forced to come up with some sort of punishment."
    pri "Do you understand?"
    show bg discussingtheincident_3
    pov "..."
    show bg discussingtheincident_11
    pov "Crystal."
    show bg discussingtheincident_12
    pri "Good."
    pri "Now, let's address the second thing on the agenda."
    show bg discussingtheincident_11
    pov "There's a second thing?"
    show bg discussingtheincident_10
    pri "Well, more of a part ‘B'."
    pri "While the previous issue was regarding the actual event and your behaviour, this is a matter of a more..."
    show bg discussingtheincident_6
    pri "Private... type..."
    show bg discussingtheincident_14
    pri "It has come to my attention that a series of pictures of yourself has been leaked online."
    show bg discussingtheincident_4
    pri "We take cyberbullying as a very serious issue."
    show bg discussingtheincident_14
    pri "I want you to know that we are doing our best to find whoever took these pictures and I'll be sure they face a..."
    show bg discussingtheincident_6
    pri "Very long..."
    show bg discussingtheincident_14
    pri "...and hard..."
    show bg discussingtheincident_15
    pri "..."
    show bg discussingtheincident_16
    pri "...punishment."
    show bg discussingtheincident_15
    pri ".."
    pri "..."
    pri "...."
    pov "..."
    pov "Um..."

    menu:
        "Stay silent":
            pass
        "Are you okay?":
            pass
        "Are you thinking about a penis?":
            pass
    pri "..."
    show bg discussingtheincident_7
    pri "Hmm..."
    show bg discussingtheincident_8
    pri "Uhm.. where am I?"
    show bg discussingtheincident_6
    pri "Excuse me, [povname]. I must've lost my train of thought for a second."
    show bg discussingtheincident_5
    pov "T-Thats okay, you must be tired from all the work you do."
    show bg discussingtheincident_6
    pri "Um..."
    show bg discussingtheincident_10
    pri "I'm sorry, what was I going on about?"

    menu:
        "Something long and hard?":
            show bg discussingtheincident_7
            pov "You were talking about something long and hard?"
            show bg discussingtheincident_8
            pri "W-W-Was I?!"
            show bg discussingtheincident_14
            pri "I-It's not what you think!"
            show bg discussingtheincident_8
            pri "I-I didn't-"
            show bg discussingtheincident_14
            pri "Oh my, Lord, please for-"
            show bg discussingtheincident_7
            pov "Woah! Director Lashley, calm down!"
            pov "I was talking about the punishment you were describing!"
            show bg discussingtheincident_6
            pri "A punishment?"
            show bg discussingtheincident_8
            pri "O-Oh, right!"
            show bg discussingtheincident_6
            pri "I remember now!"
        "About to let me go?":
            show bg discussingtheincident_7
            pov "You were about to let me go?"
            show bg discussingtheincident_10
            pri "W-Was I?"
            pri "I could have sworn I still had to tell you about-"
            show bg discussingtheincident_8
            pri "Oh, right!"
            pri "I wanted to let you know that we will be looking into this leak and we'll punish whoever did this."
        "About my naked pictures?":
            show bg discussingtheincident_7
            pov "You were talking about my naked pictures?"
            show bg discussingtheincident_8
            pri "Right! The-"
            show bg discussingtheincident_6
            pri "Pictures..."
            pri "T-Thank you, [povname]."
            show bg discussingtheincident_14
            pri "I don't know what came over me."
    show bg discussingtheincident_6
    pri "You can rest assured that we will do everything in our power to punish whoever did this to you."
    show bg discussingtheincident_10
    pri "Do you have any idea who could have done this to you?"

    menu:
        "Mention 'The Threeghans'":
            $ discussingtheincident_threeghans = 1
            show bg discussingtheincident_9
            pov "Well, actually..."
            pov "According to some classmates of mine, it was one of the Threegan's who found me."
            show bg discussingtheincident_10
            pri "The Threeghans?"
            show bg discussingtheincident_9
            pov "Yeah, y'know them, don't you?."
            show bg discussingtheincident_10
            pri "You mean Meghan, Teghan, and who?"
            show bg discussingtheincident_9
            pov "Chieghan? I believe. I'm told that's more of a nickname than her actual name."
            show bg discussingtheincident_8
            pri "Lee Soon-yi, the new exchange student."
            show bg discussingtheincident_4
            pri "I prefer to call my student by the name their parents gave them."
            pri "No 'Threeghans'."
            show bg discussingtheincident_7
            pov "Well, anyway, they took the pictures and sent it to the others before calling the police."
            show bg discussingtheincident_13
            pov "By the time I woke up, everybody had already seen them."
            show bg discussingtheincident_10
            pri "You're certain about this?"
            show bg discussingtheincident_9
            pov "I trust their words."
            show bg discussingtheincident_4
            pri "Thank you, [povname]. This is some very new information."
            pri "I will.. definitely look into the matter at hand."
            pri "We'll handle the rest after that."
        "Say nothing":
            show bg discussingtheincident_9
            pov "I'm not really sure, but you shouldn't trouble yourself about it."
            show bg discussingtheincident_13
            pov "It's really not that big of a deal."
            show bg discussingtheincident_5
            pov "I've actually been receiving a few compliments for them here and there."
            show bg discussingtheincident_6
            pri "I can see why..."
            show bg discussingtheincident_7
            pov "What was that?"
            show bg discussingtheincident_8
            pri "N-Nothing!"
            show bg discussingtheincident_16
            pri "Still.."
            show bg discussingtheincident_7
            pov "..."
    show bg discussingtheincident_18
    pri "We must not allow this sort of thing to go unpunished."
    pri "If we don't do something about it, other students may start doing it."
    show bg discussingtheincident_10
    pri "And I don't mean to assume but you seem to taking this quite positively and maturely."
    show bg discussingtheincident_4
    pri "Other students may not be so lucky."
    pri "Think of it as extinguishing an ember before it creates a fire."
    show bg discussingtheincident_3
    pov "Yeah, you're right."
    show bg discussingtheincident_9
    pov "Anyway, would that be all?"
    show bg discussingtheincident_14
    pri "Yes, [povname]."
    show bg discussingtheincident_6
    pri "Keep in mind what we talked about."
    show bg discussingtheincident_8
    pri "Oh! Before I forget-"
    show bg discussingtheincident_10
    if winc == 0:
        pri "Your [mumrole] requested me to inform you that you should head straight home after university."
    else:
        pri "Your mother requested me to inform you that you should head straight home after university."
    show bg discussingtheincident_9
    pov "She actually called y- {i}*sigh*{/i} Of course, Director Lashley."
    show bg discussingtheincident_8
    pri "And [povname]?"
    show bg discussingtheincident_5
    pov "Yes?"
    show bg discussingtheincident_6
    pri "I'm really am glad you're safe. Thank the Lord that you are."

    menu:
        "Yeah, me too.":
            show bg discussingtheincident_5
            pov "Yeah, me too, Ms. Lashley. Safe and sound."
            show bg discussingtheincident_2
            pri "Without a single scratch on your body."
            show bg discussingtheincident_1
            pov "Yeah... uh- Have a nice day, Director Lashley."
        "I'm happy to see you again.":
            show bg discussingtheincident_1
            pov "I'm happy to see you again."
            pov "Have a nice day, Director Lashley."
        "Thanks.":
            show bg discussingtheincident_1
            pov "Thanks, Director Lashley."
            pov "Have a nice day!"
    show bg discussingtheincident_2
    pri "God bless, [povname]! If you're in any trouble, remember that he's always there for you."

    scene bg schoolhallway2_day
    with fade
    show pov confused
    with dissolve
    $ renpy.pause(1,hard=True)

    scene bg discussingtheincident_13
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg discussingtheincident_15
    $ renpy.pause()
    show bg discussingtheincident_22
    with dissolve
    $ renpy.pause()
    pri "Oh, sweet Lord, forgive me for I will have sinned..."
    show bg discussingtheincident_20
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_21
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_20
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_21
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_20
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_21
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_20
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_21
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_20
    $ renpy.pause(0.5,hard=True)
    show bg discussingtheincident_21
    $ renpy.pause(0.5,hard=True)
    pri "{i}W-What am I doing?!{/i}"
    pri "..."
    pri "{i}Oh my Go- g- goodness...{/i}"
    pri "{i}I can't- I must not be thinking straight.{/i}"
    pri "Forgive me, Lord for I am a sinner..."

    scene bg schoolhallway2_day
    with dissolve
    show pov confused
    with dissolve
    pov "{i}That was strange...{/i}"
    pov "{i}Something is definitely up with Lashley.{/i}"
    if discussingtheincident_monitored == 1:
        pov "{i}I didn't realized how much I mattered to people here.{/i}"
        show pov embarrassed
        pov "{i}This is nothing like it was back home.{/i}"
        pov "{i}But...{/i}"
        pov "{i}I guess this is my home now.{/i}"
        show pov confused
        pov "{i}What I saw last night...{/i}"
        pov "{i}It couldn't have been a dream right?{/i}"
        pov "{i}That other world at the bottom of the lake...{/i}"
        show pov sad
        pov "{i}Was I really just drugged?{/i}"
        pov "{i}Am I losing my mind?{/i}"
        show pov shocked
        pov "{i}And that woman...{/i}"
        show pov confused
        pov "{i}What was her name?{/i}"
        pov "{i}Xina?{/i}"
        pov "..."
    else:
        show pov angry
        pov "{i}So I'm under her surveillance now...{/i}"
        pov "..."
        show pov bored
        pov "{i}Great, just perfect!{/i}"
        pov "{i}Not a month here and I'm already up to my neck in shit!{/i}"
        show pov angry
        pov "{i}Just what the fuck is wrong with this place?!{/i}"
        pov "..."
        show pov confused
        pov "{i}That woman...{/i}"
        pov "{i}What was her name?{/i}"
        pov "{i}Xina?{/i}"
        pov "{i}...{/i}"
        show pov sad
        pov "{i}I couldn't have imagined her...{/i}"
        pov "{i}They say you can't create new faces from imagination...{/i}"
        show pov confused
        pov "{i}That whole place... That...{/i}"
        pov "{i}Sex World.{/i}"
        pov "{i}No amount of drugs could get you to hallucinate like that...{/i}"
        pov "{i}I don't think they can...{/i}"
        show pov sad
        pov "{i}I mean- She wanted to kill me!{/i}"
        pov "..."
    show pov confused
    pov "{i}What cryptic hellhole did I just fall into?{/i}"
    pov "{i}I should just try to get home before more people spot me.{/i}"
    $ main_story = 45
    $ townmap_enabled = 1
    $ gtime = 1
    scene black with fade
    #jump lbl_schoolhallway2_day_setup
    ## Something is Following You

    jump lbl_something_is_following_you
