## Allaway is Cold ##
label lbl_allaway_is_cold:

    scene bg classroom_day
    with fade
    show pov neutral_talk at left
    with dissolve
    show mis bored at right
    with dissolve
    pov "Hey, Miss."
    show pov confused at left
    show mis bored_talk at right
    mis "Go away, [povname]."
    show pov confused_talk at left
    show mis bored at right
    pov "What? What's going on with you?"
    show pov shocked at left
    show mis angry_talk at right
    mis "I said go away, I don't want to talk to you."
    show pov sad_talk at left
    show mis angry at right
    pov "Did I do something wrong...?"
    show pov sad at left
    pov "..."
    show pov confused_talk at left
    show mis bored at right
    pov "Miss?"
    show pov confused at left
    show mis bored_talk at right
    mis "Don't make me say it again, don't bother me."
    show pov shocked at left
    show mis angry_talk at right
    mis "Don't even look at me."
    show pov sad_talk at left
    show mis bored at right
    pov "But M-"
    show pov sad at left
    show mis bored_talk at right
    mis "[povname]... please. Just go."
    hide mis bored_talk
    pov "..."
    pov "{i}What is her problem? I thought everything was fine and dandy?!{/i}"
    pov "..."
    show pov confused at left
    pov "{i}Does she think different of me now?{/i}"
    pov "{i}Is it ‘cause I've been pursuing her too much?{/i}"
    show pov sad at left
    pov "{i}She likes bad boys, right?{/i}"
    show pov confused at left
    pov "{i}I can be bad.{/i}"
    show pov sad at left
    pov "{i}But... she's a teacher, so she must like someone smart...{/i}"
    pov "{i}She really likes Effie and Effie's mad intellect.{/i}"
    if skill_int <= 18:
        pov "{i}But... I've been studying, I think. I'm not that stupid, am I?{/i}"
        pov "{i}Ugh, now's not the time to be so ignorant, [povname].{/i}"
        show pov confused at left
        pov "{i}I'm sure there's plenty of room for me to improve academically.{/i}"
        pov "{i}I have to show her that I'm not just an idiotic one-trick-pony.{/i}"
        show pov angry at left
        pov "{i}I gotta prove to her that I take my education seriously; and I respect her as a teacher.{/i}"
        show pov sad at left
        pov "{i}Because hell am I gonna win a woman like her if I don't give her any actual reasons to go any further.{/i}"
        pov "{i}She's not some dumb, gullible 18 year old anymore.{/i}"
    else:
        pov "{i}But... I'm gettin straight A's in class?{/i}"
        pov "{i}Every coursework and test I've done is all top tier.{/i}"
        pov "{i}Where have I gone wrong?{/i}"
        show pov confused at left
        pov "{i}Am I... too smart for her? Is she intimidated?{/i}"
        show pov bored at left
        pov "{i}No, [povname]. That's stupid.{/i}"
        show pov confused at left
        pov "{i}Maybe she's just not feeling it today. There's definitely something fishy going on.{/i}"
        show pov sad at left
        pov "{i}She's not herself.{/i}"
    $ missallaway_path = 16

    jump lbl_classroom_day_setup
