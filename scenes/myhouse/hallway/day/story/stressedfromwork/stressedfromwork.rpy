## Stressed From Work
default mumsis_stressedfromwork = 0

label lbl_stressed_from_work:
    scene bg myhallway_day
    with fade
    show pov neutral_talk at left
    with dissolve
    show sis confused at right
    with dissolve
    pov "Hey, you feeling alright?"
    show pov neutral at left
    show sis confused_talk at right
    sis "Yeah, why?"
    show pov confused_talk at left
    show sis confused at right
    pov "It was unusual for you to fall asleep on the couch, you usually crawl your way to bed before passing out."
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "Oh- yeah. Mom started massaging me and it felt to good to leave."
    show pov neutral_talk at left
    show sis embarrassed at right
    pov "Hahaha, yeah okay. I totally understand."
    show pov embarrassed at left
    show sis embarrassed_talk at right
    sis "Work’s been a pain in the ass and just needed someone to relieve the stress in my head."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "I hope things ease up soon with work, I guess."
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "Thanks."
    show sis sad_talk at right
    sis "It really takes a toll on my body but I can’t really quit."
    show pov confused_talk at left
    show sis bored at right
    pov "Why not?"
    show pov confused at left
    show sis confused_talk at right
    sis "The pay’s pretty decent no qualifications."
    show pov confused_talk at left
    show sis shocked at right
    pov "What is it that you do again?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Oh- well..."
    sis "Uhm.."
    sis "This and that."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "Uh-huh."
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Just retail."
    show pov confused_talk at left
    show sis bored at right
    pov "Where though?"
    show pov confused at left
    show sis bored_talk at right
    sis "Look, man. I don’t really feel like talking about work, I just wanna not think about it when I can."
    show pov confused_talk at left
    show sis sad at right
    pov "Hmm.. alright."
    show pov confused at left
    show sis embarrassed_talk at right
    sis "I’ll catch ya later."

    $ mumsis_stressedfromwork = 1
    $ mumsis_path = 3
    $ townmap_enabled = 1

    jump lbl_myhallway_day
