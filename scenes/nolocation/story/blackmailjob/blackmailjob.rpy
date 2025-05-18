## Blackmail Job ##
label lbl_blackmail_job:

    scene bg allawaytruck_3
    with fade
    $ renpy.pause(1,hard=True)
    show bg allawaytruck_4
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawaytruck_5
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawaytruck_3
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawaytruck_4
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawaytruck_5
    with dissolve
    pov "{i}The silence is killing me!{/i}"
    pov "{i}Should I say something?!{/i}"
    show bg allawaytruck_3
    pov "{i}Should I wait for her to say something?!{/i}"
    if allawayprivatetalk_telltruth == 0:
        pov "{i}She knows I hid the truth last night!{/i}"
        pov "{i}She should be trying to tear my head off!{/i}"
        show bg allawaytruck_4
        pov "{i}At least having her yell or scold me would be better than absolute silence!{/i}"
        pov "{i}She won't even look at me!{/i}"
        pov "{i}Ok, maybe I'm overthinking this...{/i}"
        show bg allawaytruck_5
        pov "{i}Maybe she is just waiting to hear my explanation?{/i}"
        pov "{i}Then again, she could also be composing in her head, the longest rant I have ever received...{/i}"
        pov "{i}Either Way, I need to carefully think what I'm about to say.{/i}"
    else:
        pov "{i}What is she even doing here on the first place?!{/i}"
        pov "{i}I told her, I would take care of things in her place!{/i}"
        show bg allawaytruck_4
        pov "{i}I should have seen this coming.{/i}"
        pov "{i}There was no way she wouldn't try to come after hearing I was involved with all of this.{/i}"
        pov "{i}She must be so scared...{/i}"
        show bg allawaytruck_5
        pov "{i}Alright, let's just get this silence over with.{/i}"
    pov "What are you doing here, Allaway?"
    mis "..."
    show bg allawaytruck_3
    mis "I..."
    mis "I just couldn't sit idle while you're out there risking your neck for me..."
    mis "You should know by now that I'm not that type of woman."
    mis "I've done this a couple of times, so at least I have some experience to help you out."
    show bg allawaytruck_4
    pov "You understand we will have to burn this truck once we are done, right?"
    mis "I-I know that."
    mis "But it's just a truck, [povname]."
    show bg allawaytruck_5
    mis "I want to have you in my life more than I want to keep driving this rusted can with wheels."
    pov "So you're not angry with me, then?"
    mis "Angry? Oh, no..."
    if allawayprivatetalk_telltruth == 0:
        if missallaway_points >= 3:
            $ missallaway_points -= 3
        else:
            $ missallaway_points = 0
        $ renpy.notify("Your relationship with Miss Allaway has decreased by 3")
        show bg allawaytruck_6
        with hpunch
        mis "I am FUCKING FURIOUS!"
        pov "Oh, boy."
        mis "How could you keep this hidden from me?!"
        show bg allawaytruck_7
        mis "Did you think I wouldn't find out?!"
        mis "Do you think I'm that stupid, to never find out?! Is that it?!"
        mis "I thought we were a team, [povname]!"
        show bg allawaytruck_6
        mis "We aren't supposed to keep secrets from each other!"
        pov "I-I know that!"
        pov "But I had to make a choice on the spot, and I didn't want you getting caught in the crossfire!"
        show bg allawaytruck_7
        pov "Much less suffer the fallout, if things went wrong!"
        mis "You didn't want to involve me?! "
        mis "In case you haven't noticed, I was involved in all of this from the very start!"
        show bg allawaytruck_6
        mis "I appear in those pictures, just as much as you do!"
        mis "Hell, if anything, I should be the one to have volunteered to do this, solo. Considering I have the most to lose!"
        pov "It was my fault all of this started, in the first place!"
        show bg allawaytruck_7
        pov "I'm taking responsibility for my actions!"
        mis "I'm as guilty as you are, don't you dare try and make yourself a martyr now!"
        pov "I couldn't let you lose everything you have worked so hard to get!"
        show bg allawaytruck_6
        mis "I- I would've agreed with you, back then- but now..."
        mis "Now everything is different. I would give up so much for you."
        mis "At least that's what I would've done. I don't really know anymore. I'm caught in a loop."
        show bg allawaytruck_7
        pov "..."
        mis "..."
    else:
        if missallaway_points <= 7:
            $ missallaway_points += 3
        else:
            $ missallaway_points = 10
        $ renpy.notify("Your relationship with Miss Allaway has increased by 3")
        show bg allawaytruck_6
        mis "No, I don't think I was ever angry at you..."
        mis "I-I guess I was more... afraid, than anything else."
        mis "Afraid to lose you to this whole thing..."
        show bg allawaytruck_7
        pov "You know very well that you're never going to lose me, Allaway."
        mis "I-I know that!"
        show bg allawaytruck_6
        mis "The possibility of this whole thing being a set up, scares me too much to just let you do this on your own..."
        pov "You know I can defend myself."
        mis "Can you, really?"
        show bg allawaytruck_7
        mis "Even if this was a trap?"
        mis "What if this was all just a set up to get you to be alone with a bunch of Jack's thugs. And then they gang up on you, as payback for what you did at the fight club?"
        mis "That thought alone kept me up all night..."
        show bg allawaytruck_6
        pov "..."
        pov "That's- a possibility..."
        pov "But just in case this is legit..."
        pov "Well, I couldn't pass up the opportunity to free you from all of this..."
        show bg allawaytruck_7
        mis "I just wish there was another way of doing this..."
        pov "Me too..."
        pov "But we'll pull through, as long as we do it together."
        show bg allawaytruck_6
        mis "No matter what happens."
    pov "So, did Jack give you a description on this guy we are picking up?"
    show bg allawaytruck_7
    pov "I don't want to just pick up the first random guy we see looking suspicious."
    mis "According to his instructions, we just have to park at the hospital and he will show up with the stuff."
    show bg allawaytruck_6
    mis "Honestly, the less we see of him the better."
    mis "God, this makes me feel so dirty."
    mis "To know we are basically allowing some junkie to get his or her fix."
    show bg allawaytruck_7
    mis "We are basically helping them kill themselves!"
    pov "I know what you mean."
    pov "I don't get how people like Jack can do this for a living."
    show bg allawaytruck_6
    pov "To care so little about human life, just to make money."
    pov "I'm really going to start watching my back around him."
    mis "You and me both."

    jump lbl_the_getaway_0
