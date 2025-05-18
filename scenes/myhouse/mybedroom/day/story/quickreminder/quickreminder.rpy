## Quick Reminder
label lbl_quick_reminder:
    #[MC’s bedroom, morning- “Quick reminder”  - main_story =107]

    #-Once the Mc heads to bed after the previous scene, they will wake up in
    # their room all groggy to the sound of their phone ringing, they are beyond
    # tired from all the had work they put in yesterday-

    "{i}*Riiiiiiiing*{/i}" with hpunch
    pov "Mnnn…"

    "{i}*Riiiiiiiiiiiiing*{/i}"
    pov "Mmnnn… noo…"
    pov "…"
    pov "Ugh… Who’s even calling at this hour?"
    "{i}*Click*{/i}"

    ## CG SCENE ##
    scene bg quickreminder
    show body quickreminder_withphone
    show povexpression quickreminder_bored_talk
    with fade
    $ renpy.pause(1.0)
    pov "Hello?"
    show povexpression quickreminder_shocked
    jac "MORNING, DUDE!" with hpunch
    show povexpression quickreminder_shocked_talk
    pov "Jacob?!"
    show povexpression quickreminder_bored_talk
    pov "Dude, what the hell are you doing calling me so early just to yell into my ear?"
    show povexpression quickreminder_bored
    jac "Oh, nothing much. I assumed you would still be asleep, considering how exhausting my dad told us yesterday was."
    show povexpression quickreminder_bored_talk
    pov "It was brutal…"
    show povexpression quickreminder_bored
    jac "Sorry to hear that and for waking you up."
    show povexpression quickreminder_confused_talk
    pov "{i}*Sigh*{/i} It’s fine, Jacob."
    pov "What did you need?"
    show povexpression quickreminder_confused
    jac "Well, I’m just calling you to remind you that you agreed to meet up with me and Effie at the beach today so we could sort out this whole situation."
    jac "You didn’t forget, did you?"
    show povexpression quickreminder_confused_talk
    pov "What…?"
    show povexpression quickreminder_shocked_talk
    pov "Oh… Shit!"
    pov "Oh man. It totally slipped my mind, after yesterday!"
    show povexpression quickreminder_confused_talk
    pov "Shit, shit, shit. Don’t tell me I’ve kept you guys waiting!"
    show povexpression quickreminder_angry_talk
    pov "Don’t move from there, I’m on my way!"
    show povexpression quickreminder_shocked
    jac "Woah, woah, woah. Hold your horses, dude."
    jac "You are fine."
    show povexpression quickreminder_embarrassed
    jac "Effie still hasn’t contacted me and I’m only just making my way to the beach now."
    jac "I just figured I should call in case you were still sleeping."
    show povexpression quickreminder_smirk
    jac "Especially after seeing how dead my dad is after his shift yesterday."
    show povexpression quickreminder_smirk_talk
    pov "Oh, well…"
    pov "Thanks man, you totally just saved me there."
    show povexpression quickreminder_smirk
    jac "No problem, dude!"
    show povexpression quickreminder_shocked
    jac "Still, you should probably make your way over here."
    show povexpression quickreminder_embarrassed
    jac "Knowing Effie, she won’t take long to get here and best if we meet up before too many people start showing up at the beach."
    show povexpression quickreminder_embarrassed_talk
    pov "Y-Yeah, you are probably right."
    show povexpression quickreminder_neutral_talk
    pov "Alright, I’m on my way."
    show povexpression quickreminder_neutral
    jac "See you soon!"

    #-Jacob hangs up and Mc puts his phone away-
    show body quickreminder_nophone with dissolve
    show povexpression quickreminder_neutral_talk
    pov "Alright, not the best way to wake up, but at least I didn’t oversleep and miss the two of them."
    show povexpression quickreminder_confused_talk
    pov "Hmmm… Edward still hasn’t sent a text or anything about the footage though…"
    show povexpression quickreminder_embarrassed_talk
    pov "Let’s hope that’s because he is still checking over the footage and not because he hasn’t found anything…"

    #-Mc takes a pause before letting out a sigh-
    show povexpression quickreminder_bored_talk
    pov "{i}*Sigh*{/i}"
    show povexpression quickreminder_neutral_talk
    pov "Alright…"
    show povexpression quickreminder_bored_talk
    pov "Go to the beach behind the rocks, explain your piece to Effie and hope for the best."
    show povexpression quickreminder_confused_talk
    pov "Jacob is gonna be there and things won't be as bad as they could be."
    show povexpression quickreminder_smirk_talk
    pov "What’s the worst that could happen, right?"
    show povexpression quickreminder_confused_talk
    pov "…"
    show povexpression quickreminder_embarrassed_talk
    pov "I just had to say that, didn’t I?"

    #-Fade to black-

    #=SCENE END=

    scene bg mybedroom_day #TEMP
    with fade

    $ main_story = 108

    jump lbl_mybedroom_day
