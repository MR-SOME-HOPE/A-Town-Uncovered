## The Aftermath ##
label lbl_the_aftermath:

    scene bg chalkboard_day
    with fade
    show mis neutral_talk_forward_1
    with dissolve
    pov "{i}Life is good. Life is alright.{/i}"
    pov "{i}The job is done, the evidence is gone.{/i}"
    show mis confused_talk_forward_1
    pov "{i}She is safe, and she is mine.{/i}"
    show mis bored_talk_forward_1
    pov "{i}I can't believe we actually did it.{/i}"
    show mis bored_forward_1
    pov "{i}All kinds of ‘it', getting away with... all of it.{/i}"
    show mis confused_talk_forward_1
    pov "{i}All of our secrets.{/i}"
    show mis confused_forward_1
    if skill_luc >= 15:
        pov "{i}It's like... as if my luck is really high.{/i}"
    elif 6 <= skill_luc <= 14:
        pov "{i}It's like... not as if my luck is that special.{/i}"
    else:
        pov "{i}It's like... weird since my luck hasn't been that great as of late.{/i}"
    show mis confused_talk_forward_1
    mis "[povname]?"

    menu:
        "47.":
            show mis confused_forward_1
            pov "47."
            show mis bored_talk_forward_1
            mis "Um... that is incorrect."
            show mis confused_talk_forward_1
            mis "Class? What is one of the themes in Shakespeare's play?"
        "Sorry, I wasn't listening.":
            show mis bored_forward_1
            pov "Sorry, I wasn't listening."
            show mis confused_talk_forward_1
            mis "I asked, ‘what is one of the themes in Shakespeare's play?'"
        "Stay silent":
            pov "..."
            mis "[povname]? Earth to [povname]?"
            mis "What is- one of the themes- in Shakespeare's play?"
    jac "Revenge, Miss. Jeez, [povname]. You may as well name the play 'Revenge'."
    eff "Cut him some slack, he's thinking about his girlfriend."
    jac "Tch- teenagers."
    mis "Jacob. Effie. Quiet please."

    scene bg classroom_day
    with fade
    $ missallaway_path = 25
    $ gtime = 1
    $ renpy.pause(0.1)
    jump lbl_classroom_day_setup
