default lashleyribbonmatingpress_call = 0

## Lashley Ribbon Mating Press Call
label lbl_lashley_ribbon_mating_press_call:
    "{i}*Riiiiiiiingggggg*{/i}"
    pov "{i}Hmm? Oh, Director Lashley's calling me?{/i}"

    $ lashleyribbonmatingpress_call = 1

    menu:
        "Answer":
            pass
        "Decline":
            jump lbl_mykitchen_day_setup

    scene bg sweetmorningafter_phonecall_body
    show charexpression sweetmorningafter_phonecall_confused_talk
    with fade
    pov "Hello?"
    show charexpression sweetmorningafter_phonecall_confused
    pri "[povname]! Sorry to be calling you on a Sunday."
    pri "I was actually wondering if you're free today, for a quick-."
    pri "Uhm- bible study session."
    show charexpression sweetmorningafter_phonecall_confused_talk
    pov "I'm at home at the moment-"
    show charexpression sweetmorningafter_phonecall_confused
    pri "Alone?"
    show charexpression sweetmorningafter_phonecall_confused_talk
    pov "Uh- yeah. As far as I know."
    show charexpression sweetmorningafter_phonecall_embarrassed_talk
    pov "Everyone's out doing something, I guess."
    show charexpression sweetmorningafter_phonecall_confused_talk
    pov "Don't you usually go to church?"
    show charexpression sweetmorningafter_phonecall_confused
    pri "That is true but today, I felt a pull towards you and I think it's a sign from God."
    pri "He wanted me to check in on you and hopefully work out your internal struggles."
    show charexpression sweetmorningafter_phonecall_embarrassed_talk
    pov "Oh- well..."
    show charexpression sweetmorningafter_phonecall_shocked
    pri "Mind letting me in? We can discuss things further face-to-face."
    show charexpression sweetmorningafter_phonecall_embarrassed_talk
    pov "Oh- kay."

    jump lbl_lashley_ribbon_mating_press
