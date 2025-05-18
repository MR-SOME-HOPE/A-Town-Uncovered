##[School’s Entrance, afternoon - “Investigations_Luna”  - main_story =84-J]

##-The Player approaches Luna as she is sitting in the steps of the school, reading a black book by herself-
label lbl_investigations_luna:
    if investigations_luna != 0:
        pov "{i}I don't think I'll do that again right now.{/i}"
    else:
        default investigations_luna = 0

        if gtime == 1:
            #scene bg schoolhallway2_day
        #else:
            #scene bg classroom_day
            show btn_classroom_day_missallaway_idle2
            $ renpy.pause(0.001)


        show lun smirk_talk at right
        if gtime == 0:
            hide btn_schoolhallway2_day_luna_idle2
        elif gtime == 1:
            hide btn_classroom_day_luna_idle2
        with dissolve
        lun "Greetings, [povname]. I’ve been expecting you."
        show pov embarrassed_talk at left
        with dissolve
        show lun smirk at right
        pov "Uhhh, hi Luna."
        pov "Were you actually expecting me?"
        show pov confused at left
        show lun bored_talk at right
        lun "Of course, you are in seek of aid, are you not?"
        show pov shocked_talk at left
        show lun bored at right
        pov "How did you-?"
        show pov confused at left
        show lun bored_talk at right
        lun "I know many things, [povname]."
        show lun smirk_talk at right
        lun "The shadows tend to guide me to places where you lurk."
        show lun bored_talk
        lun "One can’t help but overhear things sometimes, especially things that pike at my curiosity."
        show pov embarrassed at left
        show lun smirk_talk at right
        lun "Like your call for aid regarding this town’s mysteries."
        show pov angry_talk at left
        show lun bored at right
        pov "Wait, have you been following me?!"
        show pov confused at left
        show lun bored_talk at right
        lun "Semantics are of no importance right now."
        show lun smirk_talk at right
        lun "Especially now that you are looking for aid regarding the mysteries in the town."
        show pov bored_talk at left
        show lun smirk at right
        pov "Dodging the question, just like that?"
        show pov bored at left
        show lun confused_talk at right
        lun "Do you want help or not?!"
        show pov bored_talk at left
        show lun confused at right
        pov "Alright, alright!"
        show pov confused_talk at left
        pov "Sorry, does that mean that you can help me on this?"
        show pov embarrassed at left
        show lun bored_talk at right
        lun "Perhaps…"
        show lun embarrassed_talk at right
        lun "You get to see plenty of strange phenomena from the shadows of the town."
        show pov confused at left
        show lun smirk_talk at right
        lun "And if you know where to look."
        show pov bored_talk at left
        show lun smirk at right
        pov "Luna, I already deal with enough cryptic shit as it is, can you give me a break?"
        show pov confused at left
        show lun smirk_talk at right
        lun "Where’s the fun in that~?"
        show pov bored_talk at left
        show lun bored at right
        pov "In helping out a friend who will REALLY appreciate it if you help him out on this?"
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I dunno, seeing you jump at the shadows is kinda cute."
        show pov embarrassed_talk at left
        show lun embarrassed at right
        pov "It ain’t gonna be so cute when something actually jumps me from the shadows though."
        show pov bored at left
        show lun embarrassed_talk at right
        lun "Hey, I am told my surprise hugs are quite nice!"
        show lun bored_talk at right
        lun "At least Zariah tends to say so."
        show pov embarrassed_talk at left
        show lun bored at right
        pov "I-I’m sure they are, but I really doubt it’s gonna be you who jumps out at me from the shadows first…"
        show pov embarrassed at left
        show lun bored_talk at right
        lun "Hmm, we shall see about that."
        show pov sad_talk at left
        show lun bored at right
        pov "Will you please help me out here?"
        show pov bored_talk at left
        pov "You haven’t even told me what you intend to do or what you know that could possibly help me out here."
        show pov embarrassed at left
        show lun smirk_talk at right
        lun "Alright, fair enough."
        show lun shocked_talk at right
        lun "I happen to know some weird stuff tends to happen in the lake late at night on certain days."
        show pov confused_talk at left
        show lun shocked at right
        pov "What exactly?"
        show pov shocked at left
        show lun bored_talk at right
        lun "I don’t know."
        show lun smirk_talk at right
        lun "I never stay around long enough to really catch a good look."
        show pov smirk_talk at left
        lun "Even from the shadows, something is always on the hunt to make sure unwanted eyes are kept away."
        show pov smirk_talk at left
        show lun smirk at right
        pov "If you’ve never seen what’s going on, then how are you so sure something is keeping you away?"
        show pov shocked at left
        show lun smirk_talk at right
        lun "I’ve run away from it before."
        show pov confused at left
        show lun bored_talk at right
        lun "You need to understand that the way I move around town, from within the shadows, it’s a way that makes me practically invisible."
        lun "I’ve pretty much been using it my whole life and I know it like the back of my hand."
        show pov bored at left
        show lun confused_talk at right
        lun "For something to be aware of my presence and even chase after me…"
        lun "I have never experienced what it is like to be the hunted running away from the hunter in the shadows like I did that time."
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I had to use every trick I know to escape, it's a good thing that whatever chased after me wasn’t as familiar with my ways and passageways as I am."
        show pov confused_talk at left
        show lun embarrassed at right
        pov "And you didn’t report this to anyone?"
        show pov bored at left
        show lun bored_talk at right
        lun "I wasn’t about to risk people knowing my secrets."
        show lun smirk_talk at right
        lun "Besides, I just stay clear from the lake at night ever since then."
        show pov confused at left
        show lun neutral_talk at right
        lun "Haven’t had any troubles with whatever chased me ever since."
        show pov confused_talk at left
        show lun bored at right
        pov "Yeah, but what if that’s not always the case?"
        show pov smirk_talk at left
        pov "Whatever chased after you may try again and next time you wouldn’t even see it coming."
        show pov confused at left
        show lun bored_talk at right
        lun "It’s sweet you are trying to worry about me, but I assure you I’ll be fine."
        show pov bored at left
        show lun smirk_talk at right
        lun "I am the mistress of my shadowy domains and I just so happen to know whenever uninvited forces enter my domain."
        show pov bored_talk at left
        show lun bored at right
        pov "Alright, back to cryptic talk again."
        show pov confused_talk at left
        show lun confused at right
        pov "Still, I would be more at ease if you had a backup plan in case something happens."
        show pov embarrassed_talk at left
        show lun shocked at right
        pov "Let me give you my number so you can call me if anything happens."

        ##-Luna is now visibly embarrassed at this-
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I-I appreciate it but I assure you it’s not-"
        show pov bored_talk at left
        show lun embarrassed at right
        pov "Please Luna, I insist on this."
        show pov embarrassed_talk at left
        pov "I wouldn’t be able to live with myself if something happened to you too."
        show pov embarrassed at left
        show lun embarrassed_talk at right
        lun "E-eep…"
        show pov embarrassed_talk at left
        show lun embarrassed at right
        pov "You do have a cell phone right?"
        show pov confused_talk at left
        pov "Can you use it from wherever your shadows are?"
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I-I do and I can…"
        show pov neutral_talk at left
        show lun shocked at right
        pov "Great! Let me pass you my number and-"
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I-It won’t be necessary..."
        show pov bored_talk at left
        show lun shocked at right
        pov "Luna, please. Let me-"
        show pov shocked at left
        show lun embarrassed_talk at right
        lun "N-No, you don’t understand, I…"
        lun "-quiet mumbling-"
        show pov confused_talk at left
        show lun embarrassed at right
        pov "What's that?"
        pov "I couldn’t hear you."
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I…"
        lun "I-I already have your number…"
        show pov shocked_talk at left
        show lun embarrassed at right
        pov "Oh, sorry did I give to you already?"
        show pov confused at left
        show lun embarrassed at right
        lun "N-Not exactly…"
        show pov confused_talk at left
        show lun confused at right
        pov "What do you mean?"
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I-I may have taken it when you weren’t looking and copied your number onto mine…"
        show pov shocked_talk at left
        show lun embarrassed at right
        pov "Oh…"
        show pov bored_talk at left
        pov "Uhhhhm…"
        show pov confused_talk at left
        show lun shocked at right
        pov "I’m not sure what to respond to that…"
        show pov embarrassed_talk at left
        pov "You could have just asked for it, you know?"
        pov "I wouldn’t have said no or anything."
        show pov embarrassed at left
        show lun embarrassed_talk at right
        lun "I-I know that but…"
        lun "I was really shy about asking and…"
        show pov bored_talk at left
        show lun sad at right
        pov "And?"
        show pov confused at left
        show lun embarrassed_talk at right
        lun "I-I thought it would be fun to scare you with a message or call out of nowhere…"
        show pov bored_talk at left
        show lun embarrassed at right
        pov "Ah, I see."
        show pov smirk_talk at left
        pov "Yeah, that makes way more sense for your character."
        show pov neutral at left
        show lun embarrassed_talk at right
        lun "I’m so sorry…"
        show pov neutral_talk at left
        show lun embarrassed at right
        pov "Well, it's alright I guess since you haven’t done it."
        show pov bored_talk at left
        pov "Still, be sure to call me if you ever need help alright?"
        show pov bored at left
        show lun embarrassed_talk at right
        lun "I will…"
        lun "L-Let me actually help you out for the trouble."
        show pov neutral_talk at left
        show lun neutral at right
        pov "I would appreciate it."
        show pov confused at left
        show lun neutral_talk at right
        lun "You should talk to Edward."
        show lun bored_talk at right
        lun "He thinks no one knows but I’ve seen him place cameras around town way before this all started."
        show lun smirk_talk at right
        lun "I’m sure you can convince him to let you borrow one to set up in the park at night."
        show pov bored_talk at left
        show lun smirk at right
        pov "Huh, I’ll be sure to ask then."
        show pov smirk_talk at left
        pov "He’s been looking rather busy lately so I didn’t want to interrupt him."
        show pov smirk at left
        show lun smirk_talk at right
        lun "Don’t worry about it, he mainly tinkers outside hoping to be approached to begin with."
        show lun bored_talk at right
        lun "Just pretend some interest into whatever he is doing and he will be eating from the palm of your hand in no time."
        show pov smirk_talk at left
        show lun smirk at right
        pov "Huh, I see…"
        show pov neutral_talk at left
        pov "Well, thanks a lot Luna, you were a huge help."
        show pov embarrassed_talk at left
        pov "Actually feels like I’m getting somewhere now."
        show pov embarrassed at left
        show lun embarrassed_talk at right
        lun "M-My pleasure."
        lun "A-And sorry again about the phone thing."
        show pov neutral_talk at left
        show lun embarrassed at right
        pov "Don’t worry about it. It’s already off my mind."
        show pov embarrassed_talk at left
        pov "But for the record, do feel free to call me anytime."
        show pov neutral_talk at left
        show lun shocked at right
        pov "I wouldn’t mind chatting or hanging out for a while if you are that interested to sneak my number into your phone."
        show pov neutral at left
        show lun embarrassed_talk at right
        lun "E-Eeep."
        lun "T-Thank you, I’ll be sure to do that…"
        show pov neutral_talk at left
        show lun embarrassed at right
        pov "See you later, then."
        show pov confused at left
        show lun smirk_talk at right
        lun "I’ll see you sooner than you’ll see me though."

        ##-Luna disappears from the scene after saying that-
        show pov shocked_talk at left
        hide lun
        with dissolve
        pov "…"
        show pov bored_talk at left
        pov "Yep, she is still creepy."
        show pov smirk at left
        lun "Thank you~"

        $ investigations_luna = 1
    if gtime == 0:
        jump lbl_schoolhallway2_day_setup
    elif gtime == 1:
        jump lbl_classroom_day
    ##=SCENE END=
