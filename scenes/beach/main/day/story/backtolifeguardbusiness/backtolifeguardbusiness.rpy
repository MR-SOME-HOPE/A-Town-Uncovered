## Back to Lifeguard Business
label lbl_back_to_lifeguard_business:
    ## Returning to the beach, Violette is there
    scene bg beachmain_day
    $ renpy.pause(0.001)


    show povn neutral_talk at left
    show vio neutral  at right
    with dissolve
    pov "Violette! Good to see you’re back at your post."
    show povn smirk_talk at left
    show vio smirk at right
    pov "Did you drink enough water today?"
    show povn smirk at left
    show vio neutral_talk at right
    vio "Yes, I did."
    show vio embarrassed_talk at right
    vio "Although it’s nowhere near as hot today, I’m making sure I’m super hydrated."
    show povn neutral_talk at left
    show vio embarrassed at right
    pov "That’s good to hear."
    show povn embarrassed at left
    show vio confused_talk at right
    vio "Man, I feel the roles have reversed with you looking out for me instead of me having to look out for you."
    show povn smirk_talk at left
    show vio confused at right
    pov "Why shouldn’t I be able to make sure you’re okay too?"
    show povn neutral_talk at left
    pov "I care about you."
    show povn shocked at left
    show vio shocked_talk at right
    vio "Don’t-"
    show vio bored_talk at right
    vio "Say that, [povname]."
    show povn bored at left
    show vio smirk_talk at right
    vio "We’re just trainer and trainee, nothing more."
    show povn neutral at left
    show vio embarrassed_talk at right
    vio "I hope you didn’t get the wrong idea about that one night."
    show povn neutral_talk at left
    show vio embarrassed at right
    pov "No, of course not-"
    show povn bored_talk at left
    show vio confused at right
    pov "But-"
    show povn bored at left
    show vio neutral_talk at right
    vio "But nothing."
    show povn neutral at left
    show vio bored_talk at right
    vio "I don’t have time to deal with this whole ‘what are we’ deal."
    show vio shocked_talk at right
    vio "It was nothing, get over it."
    show povn smirk_talk at left
    show vio shocked at right
    pov "Okay! Okay…"
    show povn smirk at left
    show vio bored_talk at right
    vio "We’re strictly sticking to business."
    show povn bored at left
    show vio neutral_talk at right
    vio "Nothing less, nothing more."
    show povn bored_talk at left
    show vio neutral at right
    pov "…"
    show povn embarrassed_talk at left
    show vio bored at right
    pov "Gotcha, understood."
    show povn embarrassed at left
    show vio bored_talk at right
    vio "Good."
    show povn neutral at left
    show vio confused_talk at right
    vio "…"
    show povn neutral_talk at left
    show vio confused at right
    pov "I’ll go get changed."
    show povn neutral at left
    show vio bored_talk at right
    vio "Good."
    show vio shocked_talk at right
    vio "Hurry."

    scene black
    with fade
    $ renpy.pause()
    "After training..."

    scene bg beachmain_day
    with fade

    show povlg neutral_talk at left
    show vio confused at right
    with dissolve
    pov "Hey, uhmm…"
    show povlg embarrassed_talk at left
    show vio neutral at right
    pov "Sorry about earlier."
    show povlg embarrassed at left
    show vio neutral_talk at right
    vio "What do you mean."
    show povlg smirk_talk at left
    show vio confused at right
    pov "About, y’know.."
    pov "Just pushing things and making it awkward between us."
    show povlg neutral_talk at left
    show vio shocked at right
    pov "I didn’t really intend for things to be the way it ende-"
    show povlg confused at left
    show vio shocked_talk at right
    vio "I’m gonna stop you right there, [povname]."
    show povlg shocked at left
    show vio smirk_talk at right
    vio "You really are thinking too much about it."
    show povlg embarrassed at left
    vio "We’re good."
    show povlg embarrassed_talk at left
    show vio confused at right
    pov "…"
    show povlg bored_talk at left
    show vio neutral at right
    pov "Right."
    pov "I’m just overthinking it all."
    show povlg bored at left
    show vio smirk_talk at right
    vio "Mhmm."
    show povlg bored_talk at left
    show vio smirk at right
    pov "*Sigh*"
    show povlg bored at left
    show vio smirk_talk at right
    vio "You really need to clear your head and focus on things that matter."
    show povlg confused_talk at left
    show vio bored at right
    pov "Don’t I matter to you?"
    show povlg smirk at left
    show vio confused at right
    vio "…"
    show povlg shocked_talk at left
    show vio bored at right
    pov "Wow- okay…"
    show povlg smirk_talk at left
    pov "The silence says a lot."
    show povlg confused_talk at left
    show vio smirk at right
    pov "Sorry for thinking we could be more than just a fling."
    show povlg shocked_talk at left
    pov "After spending all this time with you-"
    show povlg smirk_talk at left
    show vio confused at right
    pov "Y’know what, nevermind."
    pov "I’ll take my leave here."
    show povlg bored_talk at left
    show vio bored at right
    pov "Thanks for today’s lesson, Violette."
    show povlg bored at left
    show vio bored_talk at right
    vio "I want you coming back here without that mindset next time, [povname]."
    show povlg confused at left
    vio "It’s really getting in the way of your progress."
    show povlg bored_talk at left
    show vio bored at right
    pov "*Sigh*"
    show povlg embarrassed_talk at left
    pov "Understood, ma’am."
    show povlg shocked at left
    show vio shocked at right
    idk "HEEELLP!!"
    show vio confused_talk at right
    vio "Wha-?!"

    ## SCENE END

    $ violette_path = 9

    jump lbl_unexpected_crisis
