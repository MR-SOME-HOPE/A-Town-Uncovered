## Effie Calling
label lbl_effie_calling:

    #-Scene takes place five whole days after the previous scene where as soon as the MC wakes up, he receives a call from Effie-
    #-Mc’s phone rings-
    # Use assets from /mybedroom/day/story/quickreminder

    scene bg quickreminder
    show body quickreminder_nophone
    show povexpression quickreminder_confused
    with fade
    "{i}*Phooooneeee riiiiiiinnnnnng*"
    "{i}*Rrrrrriiiiiinggggg riiiiiiinnnnnng*"

    ## CG
    show body quickreminder_withphone
    show povexpression quickreminder_confused_talk
    with dissolve
    pov "Hello?"
    show povexpression quickreminder_confused
    eff "H-Hey there…"
    show povexpression quickreminder_surprised_talk
    pov "Oh… Hey, Effie."
    show povexpression quickreminder_confused_talk
    pov "What’s up?"
    show povexpression quickreminder_confused
    eff "Not much…"
    show povexpression quickreminder_embarrassed
    eff "I’m sorry, I didn’t wake you up or sonething, did I?"
    eff "I probably should have called a bit later..."
    show povexpression quickreminder_embarrassed_talk
    pov "Nah, you are good. I was just getting ready to get out actually."
    show povexpression quickreminder_confused
    eff "Big plans for today?"
    show povexpression quickreminder_neutral_talk
    pov "No, not really."
    show povexpression quickreminder_smirk_talk
    pov "Mainly going out to see what troubles I can get into."
    show povexpression quickreminder_smirk
    eff "Not even noon yet and you are already looking to get into trouble?"
    show povexpression quickreminder_shocked_talk
    pov "Well, I’ve come to learn it finds me either way so I may as well go look for it myself."
    show povexpression quickreminder_neutral_talk
    pov "Trying to be proactive rather than reactive and all that jazz, you know?"
    show povexpression quickreminder_confused
    eff "Heh, well that’s certainly an interesting way of looking at it."
    show povexpression quickreminder_bored_talk
    pov "You get used to it."
    show povexpression quickreminder_surprised_talk
    pov "So, what’s up? Is everything ok with your old man after…"
    show povexpression quickreminder_confused
    eff "Y-Yeah, that’s actually the reason why I called you."
    show povexpression quickreminder_embarrassed
    eff "You said you aren’t busy today, right? T-Think we could meet up in the park like last time?"
    show povexpression quickreminder_embarrassed_talk
    pov "You mean on that bench we chatted on?"
    show povexpression quickreminder_neutral_talk
    pov "Sure, should I head out there now?"
    show povexpression quickreminder_neutral
    eff "I still need to finish my shift. See you there afterwards?"
    show povexpression quickreminder_embarrassed_talk
    pov "Sure thing, is everything ok though?"
    show povexpression quickreminder_confused
    eff "I’d rather chat about this in person if that’s alright with you…"
    show povexpression quickreminder_embarrassed_talk
    pov "Yes, of course! But you ARE ok, right? Just so I can calm my nerves a little after the whole thing."
    show povexpression quickreminder_embarrassed
    eff "Y-Yeah! Yeah, all’s good but thank you for being worried about me."
    show povexpression quickreminder_neutral
    eff "I appreciate the sentiment and promise to tell you the whole thing once we meet ok?"
    show povexpression quickreminder_neutral_talk
    pov "Alright, sounds good, I’ll see you there."
    show povexpression quickreminder_neutral
    eff "See you then!"

    #-Phone call ends and Mc returns to regular gameplay with the objective to meet with Effie in the afternoon at the park-

    $ effie_path = 12

    jump lbl_mybedroom_day_setup
