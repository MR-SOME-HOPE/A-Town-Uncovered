label lbl_down_to_his_level:

    scene bg schoolyard_night
    with fade
    pov "Let me go, man!"
    pov "I wasn't done with that piece of shit!"
    show pov angry at left
    with dissolve
    show bro confused_talk at right
    with dissolve
    bro "For God's sake, man! Calm the fuck down!"
    bro "It's over, you won! You knocked him out! Congratu-fucking-lations!"
    show bro bored_talk at right
    bro "Seriously dude, back off. Any more, and you'll come up off the bigger jackass."
    show pov angry_talk at left
    show bro bored at right
    pov "That walking piece of human garbage has been tormenting us for long enough! This has been a long time coming!"
    show pov angry at left
    show bro confused_talk at right
    bro "Hey, I don't wanna be that guy; but I think you should be the better man, and just walk away - metaphorically."
    show pov angry_talk at left
    show bro bored at right
    pov "He doesn't deserve to be let off that easy!"
    show pov angry at left
    show bro sad_talk at right
    bro "I know, dude. But why are you going down to his level, man?"
    show pov angry_talk at left
    show bro confused at right
    pov "What else am I supposed to do?!"
    show pov angry at left
    show bro confused_talk at right
    bro "I don't know, man, but this ain't that!"
    show bro confused at right
    bro "..."
    show pov confused at left
    show bro embarrassed_talk at right
    bro "Look, I'm-a be real with you for a sec."
    bro "I can't say I know what you're going through. I don't."
    bro "I've only heard a snippet of your quarrel earlier, and I still don't know what's going on."
    bro "But do you really think she is going to like, seeing you like this?"
    show pov confused_talk at left
    show bro embarrassed at right
    pov "You do..? Uh-"
    show bro confused at right
    pov "Who...?"
    show pov sad at left
    show bro confused_talk at right
    bro "Okay, that part is none of my business. I'm just saying, 'would she be proud of your actions tonight'?"

    menu:
        "Yes.":
            show pov angry_talk at left
            show bro confused at right
            pov "Yes, I thi-"
        "No.":
            show pov sad_talk at left
            show bro smirk at right
            pov "No, but I-"
        "I don't know.":
            show pov sad_talk at left
            show bro confused at right
            pov "I don't kn-"
    show pov sad at left
    show bro embarrassed_talk at right
    bro "Do you really think this is going to change anything?"
    show bro confused_talk at right
    bro "If anything, you just pissed Jack off."
    show pov shocked at left
    bro "What are you going to do if he decides to take it out on your girl?"
    show pov sad_talk at left
    show bro confused at right
    pov "I..."
    pov "I don't know..."
    show pov angry_talk at left
    pov "One side of me wants to kill him but the realistic scenario..?"
    show pov sad_talk at left
    pov "I just don't know..."
    show pov sad at left
    show bro bored_talk at right
    bro "Exactly."
    show bro embarrassed_talk at right
    bro "Head home for tonight."
    bro "Talk to her."
    show pov embarrassed at left
    bro "Try to come up with a solution with her instead of pretending to be the big man and fix her problems for her."
    bro "It's the 21st century: the whole 'damsel in distress' trope doesn't run that well anymore."
    show bro smirk_talk at right
    bro "But either way, I know what I'm talking about."
    show bro confused_talk at right
    bro "Now go, little bro. If Coach sees you lurking around here, he'll surely suspend you for a while."
    show pov confused_talk at left
    show bro neutral at right
    pov "I thought he said he would ban me for a month if things got out of hand?"
    show pov embarrassed at left
    show bro smirk_talk at right
    bro "Well, you're lucky that you put up a good show."
    show bro neutral_talk at right
    bro "Go home and rest, man. You deserve a winner's night sleep."
    show pov embarrassed_talk at left
    show bro neutral at right
    pov "Thanks, Brock. I appreciate- this."
    show pov embarrassed at left
    show bro neutral_talk at right
    bro "Don't mention it."
    show pov neutral_talk at left
    show bro neutral at right
    pov "See you later, Brock."
    show pov neutral at left
    show bro neutral_talk at right
    bro "Be safe, little dude!"

    scene black
    with fade
    $ renpy.pause()
    "Later... after walking back home..."
    $ gtime = 3

    jump lbl_i_own_you
