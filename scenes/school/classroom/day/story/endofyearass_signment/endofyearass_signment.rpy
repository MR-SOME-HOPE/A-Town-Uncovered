## End of Year Ass Signment ##
label lbl_end_of_year_ass_signment:
    show mis bored_talk_forward_1
    with dissolve
    mis "Alright kids, I would just like to go over one thing for today before we start class."
    mis "I got quite a lot of questions about the end-of-year assignment and I might as well answer the most frequent one."
    pov "{i}Oh, it's about the end-of-year assignment. I guess that's still going, huh?{/i}"
    mis "A lot of you were wondering about who's going to be assessing your final assignment."
    show mis confused_talk_forward_1
    mis "Rumour has it that there are multiple teachers assessing it but from the meeting we just had, that is completely false information."
    show mis bored_talk_forward_1
    mis "The only person that is assessing your performance is your own teacher, not someone else's."
    show mis angry_talk_forward_1
    mis "So when I say you're going to have sex with me, it does not mean you're going to have sex with other teachers."

    menu:
        "Spit out non-existent water":
            show mis confused_talk_forward_1
            mis "[povname]? Are you okay? Was there a bug in your mouth?"
            show mis confused_forward_1
            pov "No, miss-"

            jump lbl_end_of_year_ass_signment_2
        "Did you just say..":
            show mis confused_forward_1
            pov "Did you just say that we're going to be fucking you?"
            show mis confused_talk_forward_1
            mis "Excuse your language, [povname]. And yes, you are. I thought we made this clear on the first day?"
            mis "You were here then, weren't you?"
            show mis confused_forward_1
            pov "I was..."
            show mis bored_talk_forward_1
            mis "If you're still unclear about something, it's better to just come talk to me about it after class, alright?"
            show mis neutral_forward_1
            pov "Alright."

            jump lbl_end_of_year_ass_signment_2
        "Seriously?":
            show mis bored_forward_1
            pov "Wait- Seriously?"
            show mis bored_talk_forward_1
            mis "Sorry to burst your bubble, but yes. And don't go on a tangent about another teaching facility, having to get their final assignment assessed by multiple teachers."
            show mis sad_talk_forward_1
            mis "It'll be a very busy time period for us, with final report writing and such."

            jump lbl_end_of_year_ass_signment_2

label lbl_end_of_year_ass_signment_2:
    show mis confused_talk_forward_1
    mis "Any questions? No? Good."
    show mis bored_talk_forward_1
    mis "Get your workbook out and turn your pages to 394."

    scene bg classroom_daysexworld
    with fade
    $ townmap_enabled = 1
    $ main_story = 33
    $ gtime = 1

    #default sexaroundtownbeach = 0
    #default sexaroundtownpark = 0
    #default sexaroundtownstreet = 0
    #default sexaroundtowncomicbookstore = 0
    #default sexaroundtowncafe = 0
    #default sexaroundtownretailstore = 0

    $ renpy.notify("New Objective: Find Answers Around Town")

    jump lbl_classroom_day_setup
