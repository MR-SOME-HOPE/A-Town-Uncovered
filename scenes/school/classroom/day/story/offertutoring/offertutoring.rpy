## Offer Tutoring ##
label lbl_offer_tutoring:

    scene bg classroom_dayempty
    with fade
    if allawaypickingonyou_int == 3:
        show pov neutral at left
        with dissolve
        show mis smirk_talk at right
        with dissolve
        mis "[povname]. You did remarkably in class, today."
        show pov neutral_talk at left
        show mis neutral at right
        pov "Thanks, I just, put in the work is all."
    elif allawaypickingonyou_luc == 3:
        show pov embarrassed at left
        with dissolve
        show mis confused_talk at right
        with dissolve
        mis "[povname]. You did surprisingly well in class today."
        mis "I'm sure you've read the book and done the coursework, but you sounded really unsure about what you're talking about."
        show pov embarrassed_talk at left
        show mis confused at right
        pov "I'm... just a little worried about getting it wrong in front of the class."
    elif allawaypickingonyou_int == 0 and allawaypickingonyou_luc == 0:
        show pov embarrassed at left
        with dissolve
        show mis embarrassed_talk at right
        with dissolve
        mis "[povname], you can tell me if you didn't understand the book at all."
        show mis neutral_talk at right
        mis "You know I'm here for you, to help you."
        show mis embarrassed at right
        pov "..."
        show pov embarrassed_talk at left
        pov "Thanks, Miss Allaway. I may have rushed through it and went into a day dream while reading it. That's totally my fault, I admit."
    else:
        show pov neutral at left
        with dissolve
        show mis neutral_talk at right
        with dissolve
        mis "[povname]. Good job in class today, seems like you knew most of the main themes and characters in the text."
        show pov embarrassed_talk at left
        show mis neutral at right
        pov "I did my best."
        show pov neutral at left
        show mis neutral_talk at right
        mis "And that's all I can ever ask from you. I don't expect you to know this book front to back at this point."
        show pov neutral_talk at left
    show mis shocked at right
    pov "Alright, see you, Miss Allaway."
    show pov confused at left
    show mis shocked_talk at right
    mis "Wait wait wait! Not so fast there, [povname]."
    show mis smirk_talk at right
    mis "That's not why I pulled you aside for."
    show mis embarrassed_talk at right
    mis "At least, not entirely."
    mis "I wanted- to..."
    mis "I was wondering..."
    mis "If you..."
    show pov bored at left
    mis "Y'know, would consider if we..."
    mis "Uh- how do I put this..?"
    mis "I wanted to know if you would consider us..."
    mis "Do you mind if we..."
    mis "Can I..."
    show pov embarrassed_talk at left
    show mis shocked at right
    pov "Miss? Take a deep breath... and try one more time."
    show pov embarrassed at left
    show mis embarrassed_talk at right
    mis "{i}*Inhale*{/i}"
    show mis bored_talk at right
    mis "Alright...."
    show mis embarrassed_talk at right
    mis "I was wondering if you would allow me to offer a one-on-one after class tutoring session to you."
    show pov smirk_talk at left
    show mis confused at right
    pov "A one-on-one tutor session? After class."
    show pov bored at left
    show mis confused_talk at right
    mis "Uh- did I stutter, [povname]?"
    show mis sad_talk at right
    mis "Yes, that's what I said. Gosh, why are you making such a big deal out of it! It's just tut-"
    show pov confused_talk at left
    show mis bored at right
    pov "Okay, okay. Don't get your knickers in a twist, Miss."
    show pov smirk_talk at left
    show mis shocked at right
    pov "I'll consider it a second date."
    show pov smirk at left
    show mis shocked_talk at right
    mis "Second dat-"
    show pov smirk_talk at left
    show mis shocked at right
    pov "Shhh, not so loud. You don't want people hearing."
    show pov smirk at left
    show mis bored_talk at right
    mis "You know, I'm starting to regret offering you this."
    show pov smirk_talk at left
    show mis bored at right
    pov "You told me when we first met that I can come to you for anything... and literally anything."
    show pov smirk at left
    show mis bored_talk at right
    mis "...Gosh darnit..."
    show mis angry_talk at right
    mis "It's not because I favour you or like you... or like-like you..."
    show mis shocked_talk at right
    mis "Which I don't!"
    show mis embarrassed_talk at right
    mis "Ahem... I- just want you to excel further in your studies. I know you can do a lot better."
    mis "What do you say?"
    show pov smirk_talk at left
    show mis bored at right
    pov "Alright, I wouldn't mind the extra help if that means we can have some personal time together."
    show pov smirk at left
    show mis bored_talk at right
    mis "[povname]? Stay in your lane, boy."
    show mis sad_talk at right
    mis "{i}*Sigh*{/i}"
    show mis embarrassed_talk at right
    mis "Come see me after class, whenever you're ready. I'll be free."
    $ missallaway_path = 8
    $ gtime = 1

    jump lbl_classroom_day_setup
