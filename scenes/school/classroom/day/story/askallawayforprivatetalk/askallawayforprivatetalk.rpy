## Ask Allaway for Private Talk ##
label lbl_ask_allaway_for_private_talk:

    scene bg classroom_day
    with fade
    show pov embarrassed_talk at left
    with dissolve
    show mis sad at right
    with dissolve
    pov "Hey, Miss?"
    show pov embarrassed at left
    show mis sad at right
    mis "Hmmm?"
    show pov embarrassed at left
    show mis embarrassed_talk at right
    mis "Oh, hey [povname]. Do you need something?"
    show pov sad_talk at left
    show mis embarrassed at right
    pov "Well..."
    show mis sad at right
    pov "Yes and no..."
    show mis sad at right
    pov "We need to have a talk."
    show pov sad at left
    show mis embarrassed_talk at right
    mis "Sure, [povname], just bring up a chair and I can help you out with-"
    show pov sad_talk at left
    show mis confused at right
    pov "No, it's..."
    show mis shocked at right
    pov "It's something about 'that'..."
    show pov sad at left
    show mis sad at right
    mis "..."
    show mis sad_talk at right
    mis "Oh..."
    mis "Well, [povname] I-"
    show mis shocked at right
    "{i}Riiiiiiiingtooooneee{/i}"
    show mis embarrassed_talk at right
    mis "Oh- that's my phone... hold on- um.."
    show mis embarrassed_talk at right
    mis "M-Meet me at the park tonight... I am... free then..."
    show mis sad_talk at right
    mis "{i}*Sigh*{/i} I'm sorry, [povname], I have to go..."
    show pov sad_talk at left
    show mis sad at right
    pov "O-kay..."
    show pov sad at left
    hide mis sad
    $ renpy.pause()
    show jac confused_talk at right
    jac "Hey, is it me or does the teach' look different to you?"
    jac "A bad type of different, I mean."
    jac "Like she hasn't been eating or sleeping well?"
    show jac confused at right
    pov "..."
    show jac confused_talk at right
    jac "Dude?"
    jac "You alright?"
    show pov sad_talk at left
    show jac confused at right
    pov "Y-Yeah... Just something I ate..."
    show pov sad at left
    show jac confused_talk at right
    jac "Are you constipated for real now? We can go to the nurse's office to see if they have any pills for that."
    show pov embarrassed_talk at left
    show jac confused at right
    pov "Heh... nah, I'll be alright..."
    pov "Say... What did the fortune cookie you read me the other day say again?"
    show pov embarrassed at left
    show jac neutral_talk at right
    jac "Something about standing tall to your problems or something like that, right?"
    show jac confused_talk at right
    jac "I don't really remember, that's a weird thing to ask about out of the blue, you know?"
    show pov embarrassed_talk at left
    show jac confused at right
    pov "Yeah..."
    pov "I have to go, man. I'll see you around."
    hide pov embarrassed_talk
    $ renpy.pause()
    show eff confused_talk
    show jac confused at right
    eff "Whoa, he left in a hurry. Is he okay?"
    show eff bored
    show jac smirk_talk at right
    jac "Yeah, he is just really constipated and hasn't pooped in a few days."
    show eff bored_talk
    show jac neutral at right
    eff "Alright, didn't need to know all of that."
    show eff bored
    show jac neutral_talk at right
    jac "Ask and you shall receive."
    $ missallaway_path = 21

    jump lbl_schoolhallway1_day_setup
