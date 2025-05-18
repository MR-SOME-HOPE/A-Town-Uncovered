## Quite the Town
label lbl_quite_the_town:
    #scene bg quitethetown_day ## myparentsbedroom_day with mom sleeping in bed
    scene bg quitethetown_0
    with fade
    show pov embarrassed at left
    with dissolve
    show sis sad_talk at right
    with dissolve
    sis "{i}*Sigh*{/i}"
    show sis embarrassed_talk at right
    sis "She finally fell asleep."
    show pov sad_talk at left
    show sis confused at right
    pov "I swear to god, this town never lets us catch a breath."
    show pov shocked at left
    show sis bored_talk at right
    sis "Well, you don’t really help, with all the shit you pull!"
    show pov sad at left
    show sis sad_talk at right
    sis "Mom was staring out the window for hours, waiting for you."
    show pov angry at left
    show sis confused_talk at right
    sis "Why did it take you so long to get home?!"
    show pov angry_talk at left
    show sis angry at right
    pov "Oh, come on. Not you too!"
    show pov embarrassed_talk at left
    show sis confused at right
    pov "I told you, I started walking home, the moment you guys called me!"
    show pov confused_talk at left
    pov "It’s not like I went to get a coffee or something."
    show pov sad at left
    show sis angry_talk at right
    sis "We can’t take our sweet time when Mom is worrying her way into a heart attack!"
    show sis sad_talk at right
    sis "If we aren’t careful, she won’t let us out of the house anymore!"
    show pov confused_talk at left
    show sis bored at right
    pov "Do you have that much of an urge to get out when there's a kidnapper on the loose?!"
    show pov shocked_talk at left
    pov "For all we know, they have a bunch of people locked in a basement and used as meat for their canabalistic lifestyle."
    show pov shocked at left
    show sis confused at right
    sis "…"
    show pov sad at left
    show sis sad at right
    pov "…"
    show pov embarrassed at left
    show sis embarrassed_talk at right
    sis "Quite the place we moved into, huh?"
    show pov embarrassed_talk at left
    show sis sad at right
    pov "So much for quiet beach-side town paradise."
    show pov embarrassed at left
    show sis sad_talk at right
    sis "I’m sorry, [povname]."
    show pov sad at left
    sis "It’s just that the moment we saw the whole thing on the news, [missus] went into mama bear mode and started panicking about our safety."
    show pov embarrassed at left
    show sis embarrassed_talk at right
    sis "She almost thrashed the house looking for her phone to call you back home; and she had it in her hand the whole time!"
    show sis shocked_talk at right
    sis "I was so close to literally slapping her back into reality."
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "I am sorry too."
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "I should have hurried home quicker."
    show pov sad_talk at left
    show sis confused at right
    pov "It’s just that we split in pairs to get home safe, and it just lead to me talking with Effie for a while."
    show pov embarrassed_talk at left
    pov "Guess we were too freaked out to notice how slow we were walking."
    show pov embarrassed at left
    show sis embarrassed_talk at right
    sis "Just try to keep us posted about where you are, whenever you are out."
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "I’ll definitely do that from now on."
    show pov sad at left
    show sis sad_talk at right
    sis "[missus]'s worried and paranoid. And I'm worried and paranoid for her, y'know?"
    scene black
    with fade

    ## After Mom Date but Before Twin Fortress Rebuild
    if mum_path >= 28 and sister_path <= 25:
        ###scene bg quitethetown_temp1
        scene bg quitethetown_1
        with fade
        sis "I mean, seriously."
        if winc == 1:
            sis "Mom right now wouldn’t let go of you when we were putting her in bed!"
        else:
            sis "[missus] right now wouldn’t let go of you when we were putting her in bed!"
        sis "And the way she was asking you to not leave her and stuff?"
        sis "I mean, I get she is worried and all, but I feel a little bit left out!"
        pov "Ehehehe…"
        pov "W-Well, I am the one who has to get out of the house more often."
        pov "It’s only natural she gets worried like that, right?"
        sis "I mean, I guess so."
        sis "I don’t know, doesn’t it seem like she is way too attached to you lately?"
        pov "W-What do you mean?"
        sis "Just some things that I’ve noticed lately."
        sis "How she seems to cook your favorites more often and how happy she gets when you too meetup to watch TV."
        sis "Also the way she seems to wear her pretty clothes around the house."
        sis "I think I’ve even been seeing her wearing a little bit of makeup too!"
        pov "Hehe… He."
        pov "W-Well, we have been spending a lot of time together."
        pov "A-And you know how she gets with her dramas and all."
        pov "Maybe she is trying to look more like the people there and all?"
        pov "You know how they fill the commercial breaks with makeup things and all."
        sis "..."
        sis "Right…"
        pov "I um…"
        pov "I should probably stay with her to make sure she can sleep comfortably."
        pov "J-Just in case she needs anything or starts to freak out again."
        sis "And that’s all you plan on doing?"
        pov "W-Well yeah."
        pov "What else would I be doing? "
        sis "I don’t know, why don’t you tell me?"
        if winc == 1:
            pov "I am just feeling guilty about worrying Mom."
        else:
            pov "I am just feeling guilty about worrying [missus]."
        pov "I don’t want to be a bigger pain in the neck than what I have to be."
        sis "Such a gentleman, eh?"
        if winc == 1:
            pov "W-Well, she is my mom after all."
        else:
            pov "W-Well, she is my [mumrole] after all."
        sis "Exactly."
        pov "Huh?"
        sis "Nothing, just don’t stay there too long, she needs to rest too, you know?"
        pov "R-Right…"

    ## After Mom Date and After Twin Fortress Rebuild
    elif mum_path >= 28 and sister_path >= 35:
        ###scene bg quitethetown_temp1
        scene bg quitethetown_1
        with fade
        sis "She won’t be sleeping for weeks if the people who kidnapped that family are still at large…"
        pov "Even now she still looks worried…"
        sis "What are we supposed to do, [povname]?"
        sis "It’s not like we can just barricade ourselves in the house and wait for things to pass."
        sis "The whole town is going to be in a panic because of this!"
        pov "I doubt whoever did this will strike again soon."
        pov "They would have to be ridiculously dumb if they were to try it again now that the whole town is on high alert."
        pov "As long as we don’t go looking for trouble, I am sure we’ll be fine."
        sis "That’s the problem with you though, isn’t it?"
        pov "What do you mean?"
        sis "You are always looking for trouble!"
        pov "I do not!"
        sis "You have been like a magnet for problems ever since we were little!"
        sis "It’s like you have a giant neon target over your head or something."
        pov "It’s not like I want it to happen to me!"
        pov "My life is crazy enough as it is."
        sis "Which is why you have to be more careful from now on!"
        if winc == 1:
            sis "What are Mom and I supposed to do if something happened to you?"
        else:
            sis "What are [missus] and I supposed to do if something happened to you?"
        mum "Mnnnn… [povname]..."
        pov "I…"
        sis "You have us to look after, [povname]."
        sis "You can’t just go missing…"
        sis "I think I would have a heart attack if you disappeared like that and Mom would likely lose it completely."
        sis "I am absolutely in love with you, so I know you are trustworthy, but..."
        sis "You have to promise me that you are going to be careful."
        if winc == 1:
            sis "For my and Mom’s sake."
        else:
            sis "For my and [missus]’s sake."
        pov "[sister], I-"
        sis "If you meant everything that you told me that night at the beach…"
        sis "You have to promise…"
        sis "Please…"
        pov "…"
        pov "I will…"
        pov "I promise."
        sis "…"
        sis "Good…"
        sis "Now, hold me…"

        ###show bg quitethetown_temp2
        show bg quitethetown_2

        pov "{i}She won’t stop shaking…{/i}"
        pov "{i}And Mom... she's still got some tears left on her face.{/i}"
        pov "{i}I have to find a way to keep them safe...{/i}"

    ## Before Mom Date and After Twin Fortress Rebuild
    elif sister_path >= 35 and mum_path <= 27:
        ###scene bg quitethetown_temp1
        scene bg quitethetown_1
        with fade
        sis "S-Seriously, dude, keep me posted about this."
        if winc == 1:
            sis "It’s kind of hard to keep Mom from freaking out about you when I am worried sick as well."
        else:
            sis "It’s kind of hard to keep [missus] from freaking out about you when I am worried sick as well."
        sis "I’ve told you not to scare me like that, jackass…"

        ###show bg quitethetown_temp2
        show bg quitethetown_2

        sis "I am really scared enough as it is."
        sis "Don’t scare me even more, you big doofus."
        pov "[sister]..."
        sis "What am I supposed to do if something happens to you?"
        sis "Y-You can’t make me fall for you like this..."
        sis "Change my entire world like this…"
        sis "Only for something to happen to you or for you to disappear on me!"
        sis "I’ve told you before!"
        sis "I-I am not about to be one of those girls in dramas who lose the love of their life when she is the happiest she has ever been!"
        sis "I completely refuse that idea!"
        pov "H-Hey, it’s alright…"
        sis "You can’t leave me, [povname]!"
        sis "Take responsibility over everything you have done!"
        sis "Y-You {i}*sniff*{/i} you can’t-!"
        sis "{i}*Sniff*{/i}"
        pov "H-Hey!"
        pov "[sister], please, it’s ok!"
        pov "I am never going to leave you. I promised you before and I plan to keep that promise."
        pov "Come on, please don’t cry…"
        sis "{i}*Sniff*{/i} I-I can’t help it!"
        sis "Just don’t leave me! {i}*sobbing*{/i}"
        pov "I won’t…"
        pov "I’ll keep you safe. I promise."

    else:#sister_path >= 35 and mum_path >= 28
        ###scene bg quitethetown_temp1
        scene bg quitethetown_1
        with fade
        sis "Someone has to look after your scrawny ass; to get you out of trouble, after all."
        sis "Who better to do that, other than your family?"
        pov "Yeah."
        pov "I know that."
        sis "H-Hey-"
        sis "I know this is going to sound real lame from me but…"
        sis "Um…"
        pov "What is it, [sister]?"
        sis "D-Do you think you can keep me company for a while?"
        sis "I-I kind of just don’t want to be alone in my room right now…"
        pov "…"
        pov "Of course, [sister]."
        pov "You don’t even need to ask."

    $ main_story = 57

    jump lbl_allaways_call
