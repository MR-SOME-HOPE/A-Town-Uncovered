## Keeping it Consistent
default violette_keepingitconsistent = 0

label lbl_keeping_it_consistent:
    show povn neutral_talk at left
    show vio neutral at right
    with dissolve
    pov "Hey, Violette. I’m here for training."
    show povn neutral at left
    show vio neutral_talk at right
    vio "Alright, go get changed and meet me here in 1 minute!"
    show povn embarrassed at left
    vio "Go go go! Like your life depends on it!"
    show povn smirk at left
    show vio bored_talk at right
    vio "55 seconds!"
    show povn smirk_talk at left
    show vio neutral at right
    pov "Ahhh!"

    scene black
    with fade
    $ renpy.pause()
    "After your training session..."

    $ violette_keepingitconsistent += 1

    if violette_keepingitconsistent == 1:
        jump lbl_keeping_it_consistent_day1
    elif violette_keepingitconsistent == 2:
        jump lbl_keeping_it_consistent_day2
    elif violette_keepingitconsistent == 3:
        jump lbl_keeping_it_consistent_day3

label lbl_keeping_it_consistent_day1:
    scene bg beachmain_day
    with fade

    show povlg bored_talk at left
    show vio neutral at right
    with dissolve
    pov "*Huff huff huff*"
    show povlg sad_talk at left
    pov "Fin-ally…"
    show povlg embarrassed at left
    show vio neutral_talk at right
    vio "Good job reciting the rules of the beach."
    show povlg smirk at left
    show vio smirk_talk at right
    vio "Took you a few tries but stay in the planking position long enough and you’ll want to get it correct as quickly as possible."
    show povlg neutral at left
    show vio neutral_talk at right
    vio "That is all for today, [povname]."
    vio "Good job."
    show povlg neutral_talk at left
    show vio neutral at right
    pov "Thanks, the beach laps were a lot easier today it felt like."
    show povlg neutral at left
    show vio smirk_talk at right
    vio "You’ve got the cool breeze on your side today, the cool air helped you feel less sweaty and in turn less tired."
    show povlg embarrassed at left
    show vio neutral at right
    pov "Let’s hope it’s like that next time too."
    show povlg confused at left
    show vio neutral_talk at right
    vio "Run enough laps and it’ll be nothing but a piece of cake."
    show povlg smirk at left
    show vio embarrassed_talk at right
    vio "Now, run along and get plenty of rest and drink plenty of water."
    show povlg neutral at left
    show vio neutral_talk at right
    vio "I’ve got a beach to survey."

    $ violette_path = 3.1
    #$ violette_keepingitconsistent = 1

    $ gtime = 2

    scene bg townmap_day
    with fade

    jump lbl_townmap_setup

label lbl_keeping_it_consistent_day2:
    scene bg beachmain_day
    with fade

    show povlg confused_talk at left
    show vio confused at right
    pov "So- does that mean I’m CPR and first aid certified?"
    show povlg confused at left
    show vio embarrassed_talk at right
    vio "Not officially. You’ll need to do the official CPR certification test which is part of the official lifeguard exam to be an official lifeguard."
    show vio confused_talk at right
    vio "But as a trainee and hopefully as a volunteer lifeguard in the future, knowing how to do it is all you need in the real world."
    show povlg confused at left
    show vio neutral_talk at right
    vio "As long as you do it properly."
    show povlg shocked at left
    vio "That being said, you really SHOULD get a certification eventually, just because it helps you with life and employment."
    show povlg shocked_talk at left
    show vio neutral at right
    pov "Noted, I’ll get around to it eventually."
    show povlg confused at left
    show vio shocked_talk at right
    vio "Oh- and also, try not to get hard when you give CPR, I could feel you stabbing me earlier today."
    show povlg embarrassed_talk at left
    show vio shocked at right
    pov "Sorry… it’s all the nudity and mouth to mouth and feeling your chest."
    show povlg embarrassed at left
    show vio neutral_talk at right
    vio "I understand, that’s why I said ‘try’."
    show povlg neutral_talk at left
    show vio neutral at right
    pov "I’ll do my best but I can’t always guarantee it, you know how boners are."
    show povlg neutral at left
    show vio confused_talk at right
    vio "How about we make that homework, practice CPR on a pillow or something and practice thinking of un-arousing subjects."
    show povlg bored at left
    show vio smirk_talk at right
    vio "Like the person you’re giving CPR to dying in your hands."
    show povlg bored_talk at left
    show vio smirk at right
    pov "Right- right…"
    show povlg neutral at left
    show vio neutral_talk at right
    vio "That’s all for today, hand over the sash and I’ll see you next time."

    $ violette_path = 3.1
    #$ violette_keepingitconsistent = 2

    $ gtime = 2

    scene bg townmap_day
    with fade

    jump lbl_townmap_setup

label lbl_keeping_it_consistent_day3:
    scene bg beachmain_day
    with fade

    show povlg shocked_talk at left
    show vio confused at right
    pov "Man…"
    show povlg shocked at left
    show vio neutral_talk at right
    vio "Don’t be discouraged, water rescues are terribly difficult for people who didn’t grow up at the beach."
    show vio confused_talk at right
    vio "The waves are something you need to learn the flow of as well as handling the rescue board."
    show povlg embarrassed_talk at left
    show vio confused at right
    pov "I nearly hit someone head on."
    show povlg embarrassed at left
    show vio neutral_talk at right
    vio "I know, I saw that."
    show povlg confused at left
    vio "But you did your very best to prevent that from happening and that’s what matters."
    show vio smirk_talk at right
    vio "You really wrangled that board to the best of your ability, even though it was out of your control and you looked like a soggy cucumber on it."
    show povlg confused_talk at left
    show vio smirk at right
    pov "How long does it take to get used to it?"
    show povlg confused at left
    show vio neutral_talk at right
    vio "The more you’re in there getting used to it, the faster the progress."
    show povlg shocked at left
    show vio smirk_talk at right
    vio "Just like anything."
    show povlg neutral_talk at left
    show vio smirk at right
    pov "You’re right. I’ll keep at it…"
    show povlg neutral at left
    show vio neutral_talk at right
    vio "I’m really glad you’re still coming to the training sessions and really proving that you’re here to learn and give it your all."
    show povlg neutral_talk at left
    show vio shocked at right
    pov "I’m starting to like being here and that sense of accomplishment that I feel when I’ve felt like I’m growing and becoming closer to being an actual lifeguard."
    show povlg confused at left
    show vio smirk_talk at right
    vio "Would you consider actually being one?"
    show povlg embarrassed_talk at left
    show vio smirk at right
    pov "To be honest, not in this lifetime though I wouldn’t mind volunteering every once in a while."
    show vio confused at right
    pov "And even if I’m not volunteering, I can help anyone in danger if no other help is around."
    show povlg neutral_talk at left
    show vio neutral at right
    pov "That’s what I’m getting out of this experience."
    show povlg neutral at left
    show vio neutral_talk at right
    vio "I’m glad you’re honest with me, and I’m happy to help you achieve that goal."
    show povlg confused at left
    show vio shocked_talk at right
    vio "It gives ME a sense of pride knowing that I’m making beaches just a little more safer whenever you’re around."
    show povlg neutral at left
    show vio smirk_talk at right
    vio "Are you busy? Would you mind sticking around and helping me pack the beach up for the night?"
    show povlg neutral_talk at left
    show vio neutral at right
    pov "Sure. I may as well, don’t wanna leave you to do everything yourself."
    show povlg neutral at left
    show vio neutral_talk at right
    vio "Thanks, I appreciate it."

    stop music fadeout 2.0
    play ambience 'audio/ambience/quietexteriornight_ambience.ogg' fadein 2.0

    $ violette_path = 4

    jump lbl_beach_sparks_after_dark
