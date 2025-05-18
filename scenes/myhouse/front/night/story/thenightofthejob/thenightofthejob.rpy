## The Night of the Job ##
label lbl_the_night_of_the_job:

    scene bg suburb_night
    with fade
    $ renpy.pause(1.5)

    scene bg thenightofthejob_0
    with dissolve
    $ renpy.pause(1.5)
    show pov bored_talk at left
    with dissolve
    show jack bored at right
    with dissolve
    pov "Nice timing."
    show pov bored at left
    show jack smirk_talk at right
    jack "It pays well, to be on time."
    jack "How you feeling, golden boy?"
    show pov confused_talk at left
    show jack smirk at right
    pov "Honestly speaking, nervous."
    show pov bored at left
    show jack smirk_talk at right
    jack "Good. That means you'll stay sharp."
    show pov confused_talk at left
    show jack smirk at right
    pov "You got Allaway's truck for this?"
    pov "Wasn't the plan to destroy the delivery vehicle afterwards?!"
    show pov bored at left
    show jack bored_talk at right
    jack "Do I look like a charity case, giving away burner vehicles for free?"
    show jack confused at right
    pov "..."
    show pov angry_talk at left
    show jack smirk at right
    pov "I-I'm not going to burn Allaway's truck! I couldn't do that to her!"
    show pov angry at left
    show jack smirk_talk at right
    jack "When I asked her about it, she seemed pretty okay with it."
    show pov angry_talk at left
    show jack smirk at right
    pov "You {i}asked{/i} her to burn down her dad's old truck and she agreed?!"
    show pov angry at left
    show jack smirk_talk at right
    jack "Yeah, the piece of junk is old enough to not warrant much suspicion when it goes up in flames."
    jack "Besides, she had some terms and conditions of her own which I couldn't pass on."
    show pov angry_talk at left
    show jack smirk at right
    pov "And what was that exactly?"
    show pov shocked at left
    show misc bored_talk
    with dissolve
    mis "I get to be your driver."
    show pov shocked_talk at left
    show misc bored
    pov "Allaway?!"
    pov "What are you doing here?!"
    pov "You're supposed to be out!"
    show pov angry at left
    show misc sad
    show jack bored_talk at right
    jack "You guys can kiss and fuck, all you want, while you wait for my guy down at the hospital."
    show jack angry_talk at right
    jack "Other than that, you're wasting time. And we are in a very limited time frame, if we want this to go smoothly."
    jack "Hold onto this, big guy."
    hide jack angry_talk
    with dissolve
    show pov confused_talk at left
    show jack bored at right
    with dissolve
    pov "What's this?"
    show pov bored at left
    show jack bored_talk at right
    jack "Radio, genius. Change it to channel four; you'll be able to hear any warnings before trouble arises."
    show pov sad at left
    show misc sad_talk
    show jack smirk at right
    mis "C'mon. There's no time to waste..."
    show pov angry at left
    show misc sad
    show jack smirk_talk at right
    jack "I can see who wears the pants in the relationship."
    show pov angry_talk at left
    show misc sad
    show jack bored at right
    pov "Wait-"
    show pov angry at left
    show misc confused
    show jack bored_talk at right
    jack "{i}*Sigh*{/i} What is it now?!"
    show pov angry_talk at left
    show jack bored at right
    pov "Once the job is done..."
    show misc sad
    show jack smirk at right
    pov "The photos and dirt you have on us disappears, right?"
    show pov angry at left
    show jack smirk_talk at right
    jack "It'll be like nothing ever happened."
    show pov angry_talk at left
    show jack smirk at right
    pov "Do I have your word?"
    show pov angry at left
    show jack bored_talk at right
    jack "When you drop off the package, you will watch me delete it, in person."
    show pov angry_talk at left
    show jack bored at right
    pov "I really can't trust you or your word."
    show pov angry at left
    show jack bored_talk at right
    jack "I really think you don't have a choice."
    jack "Look, since I don't have to share our winnings with the two of you, it means there will be a substantial bonus headed my way."
    show jack smirk_talk at right
    jack "Think of it as buying the dirt I have on you from my hands."
    jack "I've been trying to do this job for a while and since all I have to do is delete some pictures to get it done."
    show jack bored_talk at right
    jack "You can be certain I will uphold my end of the bargain."
    jack "I'm a businessman; not a moronic sociopath."
    show pov angry_talk at left
    show jack bored at right
    pov "You sure about that?"
    show pov angry at left
    show jack angry_talk at right
    jack "Just get in the damn truck, ‘Golden boy'. You talk way too fucking much!"
    show misc sad_talk
    show jack bored at right
    mis "C'mon, [povname]... let's just go."

    jump lbl_blackmail_job
