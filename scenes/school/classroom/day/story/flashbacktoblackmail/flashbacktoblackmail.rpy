## Flashback to Blackmail ##
label lbl_flashback_to_blackmail:
    default flashbacktoblackmail_leave = 0

    scene bg classroom_day
    with fade
    show pov confused at left
    with dissolve
    show mis sad_talk at right
    with dissolve
    mis "{i}*Sniff*{/i} I'm sorry, [povname]. I'm so sorry..."
    show pov sad_talk at left
    show mis sad at right
    pov "Why are you sorry..."
    show pov sad at left
    show mis sad_talk at right
    mis "I'm- sorry for being so.. distant."
    mis "And cold... to you."
    mis "I- I'm just so... exhausted... and paranoid."

    menu:
        "Exhausted?":
            show pov sad_talk at left
            show mis sad at right
            pov "Exhausted, from doing what?"
        "Paranoid?":
            show pov sad_talk at left
            show mis sad at right
            pov "Paranoid, from what..?"
        "You don't have to apologize.":
            show pov embarrassed_talk at left
            show mis sad at right
            pov "You don't have to apologize for that."
    show pov sad at left
    show mis sad_talk at right
    mis "I-"
    show mis sad at right
    mis "{i}*sniff*{/i}"
    show mis sad_talk at right
    mis "I can't..."
    mis "I hate myself."
    show pov sad at left
    mis "I hate that I can't talk to you about it!"
    show mis sad at right
    mis "{i}*sniff*{/i}"
    show pov sad_talk at left
    show mis sad at right
    pov "Miss, slow down. Take a deep breath and take as much time as you need."
    show pov embarrassed_talk at left
    pov "I'm here to listen."
    show pov embarrassed at left
    show mis sad_talk at right
    mis "{i}*Inhale*{/i}"
    mis "{i}*Exhale*{/i}"
    mis "Y-you-"
    show mis sad_talk at right
    mis "-are the only student that I've ever fallen this deeply in love with."
    show mis sad_talk at right
    mis "Y-you're so straightforward, it's scary."
    show mis embarrassed_talk at right
    mis "But it's scary-good."
    mis "It actually makes my heart race in a good way."
    show mis sad_talk at right
    mis "And I will do anything to save us."
    mis "T-the thing with..."
    pov "Wait- 'save us'?"
    pov "What do you mean 'save us'...?"
    show pov confused at left
    show mis sad_talk at right
    mis "Mm.. Jack."
    mis "He-"
    show pov shocked at left
    mis "He's blackmailing us."
    show pov shocked_talk at left
    show mis sad at right
    with hpunch
    pov "He's WHAT?!"
    pov "H-how?!"
    pov "How does he know that..."
    pov "Did we... say or something that made it obvious?"
    pov "Did he see us?"
    show pov shocked at left
    show mis sad_talk at right
    mis "He saw us."
    mis "That night."
    mis "Outside your house."
    show pov shocked_talk at left
    show mis sad at right
    pov "He fuckin' WHAT?!"
    pov "Y-yeah but he only just saw us parked there right...?"
    pov "Oh, God.."
    show pov shocked at left
    show mis sad_talk at right
    mis "He has videos and pictures of us on his phone."
    if parkingwithallaway_action == 0:
        show pov sad at left
        show mis embarrassed_talk at right
        mis "I mean- it's not like we did anything, right?"
        mis "We just talked and then you left-"
        mis "A-and..."
        show mis sad_talk at right
        mis "Fuck, [povname]. It still doesn't look good for me."
        mis "Just by us being in the same vehicle is enough to make assumptions."
    elif parkingwithallaway_action == 1:
        show pov sad at left
        mis "He-"
        show pov shocked at left
        mis "He caught us locking lips."
        mis "That's fucking evidence enough to put me in prison and ruin my entire life, [povname]!"
        show pov sad at left
        mis "Do you understand how fucking scared I am?!"
    else:
        show pov shocked at left
        mis "He caught me sucking you off, [povname]."
        mis "Sucking. You. Off."
        show pov sad at left
        mis "I'm fucking done, [povname]."
        mis "There's no going back for me now. My entire life is in his hands."
    show pov sad at left
    show mis sad_talk at right
    mis "I'm so fucking fucked."
    mis "I'm fucked so fucking.. I'm going to fucking jail if I don't-."
    mis "A-and I can't tell anyone because anything I do, I'm fucking dead."
    mis "My career is dead."
    show pov sad_talk at left
    show mis shocked at right
    pov "Is he... asking you for sexual favour..?"
    show pov embarrassed at left
    show mis shocked_talk at right
    mis "N-no! No, he's not. I swear to God he's not."
    show pov sad at left
    show mis angry_talk at right
    mis "But he is a fuckin' monster."
    show pov angry at left
    mis "A manipulative son-of-a-bitch!"
    show pov angry at left
    mis "He's gotten me involved in-"
    show mis sad_talk at right
    mis "I-"
    mis "I can't even say it... I don't want to say it. I don't want you dragged into all this."
    pov "..."
    mis "My life is dead. I have no future if this gets out."
    show pov angry_talk at left
    show mis sad at right
    pov "Jack is fucking scumbag."
    pov "I'll help you get out of this mess, Miss Allaway."
    pov "Even if it kills me."
    show pov confused at left
    show mis sad_talk at right
    mis "I don't want you involved anymore than you are."
    show pov angry_talk at left
    show mis sad at right
    pov "He has video of {i}us{/i}, as far as I know, I'm involved whether I want to or not."
    pov "I'm going to settle things once and for all."
    show pov angry at left
    show mis sad_talk at right
    mis "Don't do anything stupid, [povname]."
    show pov confused at left
    mis "I know you want to save us and be the hero of the day but Jack isn't your average guy."
    show pov angry at left
    show mis sad_talk at right
    mis "There's something sinister about him."
    show pov confused_talk at left
    show mis embarrassed at right
    pov "I'm not normal either, Miss."
    show pov smirk_talk at left
    pov "Trust me on this one."
    show pov smirk at left
    mis "..."
    show pov confused at left
    show mis embarrassed_talk at right
    mis "Fuck..."
    mis "I don't know why that turned me on."
    mis "Uhm..."
    mis "[povname]?"
    show pov confused_talk at left
    show mis embarrassed at right
    pov "Yes? What is it?"
    show pov confused at left
    show mis embarrassed_talk at right
    mis "I- I'll be under the table if you need me."
    show mis embarrassed at right
    pov "..."
    show pov confused_talk at left
    pov "You say what?"
    show pov confused at left
    show mis confused_talk at right
    mis "Under my desk."
    show mis confused at right
    mis "..."
    show pov shocked at left
    show mis smirk_talk at right
    mis "If you need me."
    show pov smirk at left
    show mis embarrassed at right
    mis "{i}*Clears throat*{/i}"
    show mis smirk_talk at right
    mis "Lock the classroom door first."

    menu:
        "Lock the door":
            show pov smirk_talk at left
            show mis smirk at right
            pov "Right on it."

            jump lbl_allaway_under_the_desk
        "Leave the room":
            show pov embarrassed_talk at left
            show mis confused at right
            pov "Um, Miss..."
            pov "I don't think we should-."
            show pov sad_talk at left
            show mis sad at right
            pov "There are still people on university grounds.. and based on what you said."
            pov "I think- we should play it safe, y'know?"
            show pov embarrassed at left
            show mis sad_talk at right
            mis "Oh- oh, okay... sure. Smart thinking.."
            mis "I guess I'll see you.. when I see you."
            if missallaway_points >= 1:
                $ missallaway_points -= 1
            else:
                $ missallaway_points = 0
            $ flashbacktoblackmail_leave = 1
            $ missallaway_path = 17.5
            $ gtime = 1

            jump lbl_schoolhallway1_day_setup
