## Discussing Stolen Evidence
label lbl_discussing_stolen_evidence:
    "Attend detention?"
    menu:
        "Yes":
            pass
        "No":
            jump lbl_classroom_day

    scene black
    with fade
    $ renpy.pause()
    "After class..."

    ## SPRITEWORK
    ## In detention

    scene bg classroom_dayempty
    with fade

    show pov embarrassed at left
    show edw neutral_talk at Position(xpos=1000)
    with dissolve
    edw "Alright, we’re all here."
    show edw neutral at Position(xpos=1000)
    show jac bored_talk at Position(xpos=1300)
    jac "Dude, what are we gonna do?"
    jac "Everything we worked so hard for."
    show pov confused at left
    show jac confused_talk at Position(xpos=1300)
    jac "Was it Xina? Do you know?"
    show jac smirk_talk at Position(xpos=1300)
    jac "I think it was Xina."
    show jac smirk at Position(xpos=1300)
    show eff bored_talk at Position(xpos=1600)
    with dissolve
    eff "No, it was definitely the police."
    show col smirk_talk at Position(xpos=1900)
    show eff bored at Position(xpos=1600)
    col "Maybe it’s both, maybe they’re working together."
    show edw angry_talk at Position(xpos=1000)
    show col smirk at Position(xpos=1900)
    edw "My prototypes! {i}*Wailing sounds*{/i}"
    show pov smirk_talk at left
    show edw angry at Position(xpos=1000)
    pov "Hey, hey. Edward, get a hold of yourself."
    show pov smirk at left
    show jac shocked_talk at Position(xpos=1300)
    show eff confused at Position(xpos=1600)
    jac "Fuck, I think they’re watching us."
    jac "They’re spying on us."
    show jac confused_talk at Position(xpos=1300)
    show col confused at Position(xpos=1900)
    jac "Listening to our every move."
    show jac shocked_talk at Position(xpos=1300)
    jac "I can’t, man."
    jac "This is too much."
    show jac smirk_talk at Position(xpos=1300)
    jac "This is not very cool at all."
    show pov embarrassed at left
    show jac embarrassed at Position(xpos=1300)
    show col smirk_talk at Position(xpos=1900)
    col "Yo, little dude, calm your farm."
    col "There’s only room for one panicked little dude in this group and I vote for Edward."
    show edw shocked_talk at Position(xpos=1000)
    show col smirk at Position(xpos=1900)
    show eff  at Position(xpos=1600)
    edw "No, no- Jacob’s right."
    show edw smirk_talk at Position(xpos=1000)
    edw "We are screwed."
    show pov embarrassed_talk at left
    show edw shocked at Position(xpos=1000)
    pov "Why and how could this have happened?"
    show pov embarrassed at left
    show eff smirk_talk at Position(xpos=1600)
    eff "I guess having our hideout in an unsecured area in the forest wasn’t the best move."
    show edw shocked_talk at Position(xpos=1000)
    edw "I swear it was off the grid and hard to find."
    show pov confused at left
    show edw bored_talk at Position(xpos=1000)
    edw "I definitely made sure of it."
    show edw embarrassed_talk at Position(xpos=1000)
    show col bored at Position(xpos=1900)
    edw "T-t-t-t-t-there’s no way they could’ve known it was all there."
    show pov confused_talk at left
    show edw sad at Position(xpos=1000)
    show col neutral at Position(xpos=1900)
    pov "Okay! Okay. One step at a time."
    show pov embarrassed_talk at left
    show jac embarrassed at Position(xpos=1300)
    show eff neutral at Position(xpos=1600)
    pov "Let’s just go through this together, okay?"
    show pov neutral_talk at left
    pov "We’ll take it one question at a time."

    ## CG SCENE
    scene bg detentionmainstory_1
    with fade

    pov "First thing’s first; who could’ve possibly done it."

    eff "It was either Xina or the feds."

    col "I say they’re both in on it."

    pov "Okay, so what would be their motive?"

    edw "I think whoever did it thinks we know too much."

    pov "We know too much."
    pov "And if we know too much, why haven’t they taken us instead?"
    pov "If it were the police or the government, wouldn’t they have taken us as well as the evidence?"

    col "Man’s got a point."

    pov "I can conclude that it’s Xina."
    pov "This whole things seems too- abnormally done if it were the pigs."

    edw "*Hyperventilating* Okay okay okay-"
    edw "I see what you mean."
    edw "Okay, at least we’re not in trouble by the actual law."

    pov "For now…"
    pov "We still need to lay low enough."

    jac "Our enemy is still Xina."

    pov "This is a good sign."

    eff "How the fuck is it a good sign, [povname]?"

    pov "If they had to take everything away from us, it means it’s because we were on the right track."
    pov "Let’s assume we were on a completely different course and nowhere near solving the meaning of this sexworld’s existence as well as Xina’s motive."
    pov "Wouldn’t they see us as a low threat?"
    pov "This-"
    pov "This is good."

    jac "That fucking sucks but at the same time, it does make sense, strategy wise."
    jac "They would WANT us to be circling around, chasing our own stupid tails."
    jac "But because we were on THEIRS’, it became serious enough to get dirty."

    edw "I just want my inventions back, man…"

    col "Okay, so let’s assume we’re 90%% sure that Xina did this and because we were on the right track of unmasking her motives."
    col "Now what?"
    col "As Edward said, we don’t got shit on them now."

    eff "We do, we don’t need the physical evidence to know what we know."
    eff "It’s not like we intend to take them to court."
    eff "That’s stupid."

    jac "Hahahaha- yeah… stupid."
    jac "Who would think we’d do that- ahaha…"

    eff "Anyway, I’m sorry Edward, I know your precious machines have been taken as well but risking to get them back is not worth it."

    edw "Huhu- huhuhuhuu- even my blueprints, I have to start from scratch all over again-"
    edw "FUUUUUUUCCCCKKKKKKK!!!!"
    edw "Sorry."
    edw "Sorry, I just had to let it out."

    col "It’s all good, dude. Coach Fistem is a heavy sleeper."
    col "The only thing that can wake him up is the smell of sweat and pussy."

    eff "Ew…"

    jac "Okay but really, what are we gonna do next though?"
    jac "What’s our jumping off point?"

    pov "Well-"
    pov "Did everyone bring the flyers that Edward told you to bring?"

    eff "The Followers of Master Buukakki?"
    eff "Got it right here."

    jac "Yeah, did anyone figure out what the fuck that map was?"
    jac "I think it’s out of town because I don’t recognize that place at all."

    col "It looked hella sus to me so of course I took one for myself."
    col "Hopefully it contains a clue."

    pov "Okay, everyone hand them to me. Let me try som-"

    pri "Excuse me, did I overhear what I thought I overheard?"
    pri "COACH FISTEM, WAKE UP!"

    ## Transition straight to the next scene


    $ main_story = 150

    jump lbl_confiscated_flyers
