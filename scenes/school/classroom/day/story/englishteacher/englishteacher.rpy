## English Teacher ##
label lbl_english_teacher:

    scene bg chalkboard_day
    with fade
    show mis neutral_talk_forward_1
    with dissolve
    mis "Alright class, settle down, settle down. You can catch up and talk about your holidays with your friends after class."
    mis "Welcome to a new year of university."
    show mis bored_talk_forward_1
    mis "It's not gonna be easy for most of you, it's the last leg of the marathon, so you better work your butts off if you want to get into a good career."
    show mis neutral_talk_forward_1
    mis "If you haven't had me before or you don't know who I am, I'm Miss Allaway and I'll be your English teacher for this year."
    mis "Any questions before we get started?"
    mis "Yes, Effie."
    show mis neutral_forward_1
    eff "He's probably gonna hate me for pointing him out but we've got a new student here."
    show mis neutral_talk_forward_1
    mis "Ooh, a new student? Welcome!"

    menu:
        "Hi, my name is [povname].":
            jump lbl_english_teacher_1
        "Stay silent":
            jump lbl_english_teacher_2

label lbl_english_teacher_1:
    show mis neutral_forward_1
    pov "Hi, my name is [povname]. I just moved into town not too long ago so I'm pretty new to pretty much everything."
    show mis neutral_talk_forward_1
    mis "[povname]. Gotcha, mentally noted down. On behalf of the class and our beautiful town, we welcome you to the university."
    mis "If you need any help, you can always talk to Effie, I'm sure she'll be more than happy to help."
    show mis neutral_forward_1
    eff "Definitely! Always happy to."
    show mis neutral_talk_forward_1
    mis "Otherwise you can always come to me if you need help with absolutely anything you need."
    show mis bored_talk_forward_1
    mis "Literally anything."

    jump lbl_english_teacher_3

label lbl_english_teacher_2:
    show mis neutral_talk_forward_1
    mis "If you need any help, you can always talk to Effie, I'm sure she'll be more than happy to help."
    show mis neutral_forward_1
    eff "Of course! [povname] and I introduced each other earlier."
    show mis neutral_talk_forward_1
    mis "Oh, [povname], there we go. Talk to her, otherwise you can always come to me if you need help with absolutely anything you need.."
    show mis bored_talk_forward_1
    mis "..or want."

    jump lbl_english_teacher_3

label lbl_english_teacher_3:
    show mis neutral_talk_forward_1
    mis "Anyway! Assignments!"
    show mis bored_forward_1
    clas "{i}*Groaaaan*{/i}"
    show mis bored_talk_forward_1
    mis "Now now, I can hear your groaning but I'm doing you a favour here. This assignment isn't due till the end of the year."
    mis "To which if you are able to comprehend English, means that you have the whole year to do it."
    mis "And that also means that I'll accept absolutely no excuses for not getting it done in time."
    show mis neutral_talk_forward_1
    mis "Each of you will need to write an in-depth 2,500 word piece on a current event that occurs anytime between the beginning of this month and the submission day."
    show mis bored_talk_forward_1
    mis "Here comes the groaning and moaning again. I know some of you are going to literally write it up the day before it's due, so just a pro-tip:"
    show mis angry_talk_forward_1
    mis "Don't."
    mis "This is going to be worth 50 percent of your overall mark, so don't half-arse it."
    show mis neutral_talk_forward_1
    mis "Well, good luck with that. If you have any questions or you need assistance, come see me whenever I'm free."
    scene bg skills_int_1
    with fade
    scene bg skills_int_4
    with fade
    "You successfully increased your INT Max Limit."
    $ skill_intmax += 1
    $ skill_int_times = 1
    $ main_story = 7

    jump lbl_the_assignment
