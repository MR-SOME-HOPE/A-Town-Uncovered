label lbl_a_weight_off_my_chest:
    #[MC's bedroom, Night - “A Weight Off My Chest”  - main_story =114]

    #-Scene takes place in the MC's bedroom after the previous scene-

    #-Missus enters the MC's room with him in tow in order to help him sit down
    # after the guys explain a lie where he took a fall and injured his head when
    # hanging out-
    show bg mybedroom_night_lightson
    with fade

    show pov embarrassed at left
    show mum confused_talk at right
    with dissolve
    mum "Easy there, honey. Don't make any sudden movements, here. And try not to move too much."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "You really don't have to worry so much. I keep telling you, I'm fine."
    show pov neutral_talk at left
    pov "Head doesn't hurt or anything, anymore."
    show pov confused at left
    show mum bored_talk at right
    mum "Honey, blows to the head aren't anything to take lightly!"
    mum "A bad enough blow could end up with you bleeding your brain out of your ears!"
    show pov smirk_talk at left
    show mum shocked at right
    pov "Well, considering I still have my brain goop inside my head, I'd say we are fine on that front, left?"
    show pov shocked at left
    show mum angry_talk at right
    mum "Don't get snarky with me!" with hpunch
    show mum shocked at right
    mum "I still can't believe you didn't come straight back home after it happened. It could have been really serious!"
    show pov confused_talk at left
    pov "I told you, the guys were there and they patched me up the best that they could, and I was fine after a couple of minutes. I was in good hands."
    show mum confused_talk at right
    mum "I-I know that, and I'm not saying you weren't."
    show pov embarrassed at left
    show mum shocked at right
    mum "But you shouldn't be so casual about injuries like this!"
    show mum embarrassed_talk at right
    mum "As you get older, those kinds of things won't heal as easily, you know?!"
    show pov confused_talk at left
    show mum embarrassed at right
    pov "I know, I know…"
    show pov embarrassed_talk at left
    pov "I'll rush straight home if it ever happens again, I promise."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "Well… I think the wisest move would be to call an ambulance - if it was bad enough for it to knock you out. But I appreciate your words, nonetheless."
    mum "Still… Talk about unlucky…"
    show mum shocked_talk at right
    mum "To think you would be crossing the street with your friends, and just slip on a random ice cube from a poorly discarded drink."
    show mum angry_talk at right
    mum "People should really be more mindful of where they throw their trash!"
    show pov confused_talk at left
    show mum confused at right
    pov "Ehehehe… Y-Yeah… littering can be quite the problem nowadays…"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "S-Still, the whole thing led to Effie and I mending our bridges, and we are friends again. So I'd consider that whole thing to be the universe balancing itself out with karma and all that."
    show pov confused at left
    show mum embarrassed_talk at right
    mum "I'm really glad to hear you managed to patch things up with Effie."
    mum "She is such a nice girl, and I can see she's had a really good impact on you since you joined their little friend group."
    show mum neutral_talk at right
    mum "Plus, it was really nice of them to bring you all the way home, just to make sure you were okay!"
    show pov bored_talk at left
    show mum neutral at right
    pov "Yeah… They are the best…"


    #=RESULT BRANCH=


    #=RESULT=
    #-If Missus has been romanced-
    if mum_path >= 31:
        show pov confused at left
        show mum smirk_talk at right
        mum "Though I hope you aren't getting too friendly with her behind my back, now."
        mum "You don't want me to have to remind you who should be your top priority here, left?"
        show pov embarrassed at left
        show mum bored_talk at right
        mum "You should know by now that seeing me jealous is a quick way to end up sleeping outside the comforts of my roof."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "I-I know, I know…"
        pov "I wouldn't dream of it. You know how special you are to me."
        show pov embarrassed at left
        show mum bored_talk at right
        mum "I'm well aware - though, as a woman, I need to make sure to claim my territory."
        show pov confused at left
        show mum smirk_talk at right
        mum "Only reason I'm not reminding you, and [povname] Jr, who owns the both of you left now, is the fact that I don't want to do anything until I'm sure your bump has healed up entirely."
        show pov smirk_talk at left
        show mum smirk at right
        pov "Dang, universe must really have had it against me, then."
        show pov neutral_talk at left
        show mum confused at right
        pov "You know I could never say no to you~"
        show pov neutral at left
        show mum confused_talk at right
        mum "Yes, Yes. You are very sweet, but you don't have to worry."
        show pov embarrassed at left
        show mum shocked_talk at right
        mum "I plan to give you two a reminder - once I feel like you are better."
        mum "And as such, that means these legs are closed until I feel like you are good to go."
        show mum smirk_talk at right
        mum "And from the looks of it, I'd say it's gonna take a while~"
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Oh, come on!"
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Hmmm, maybe your karma hasn't been entirely balanced out yet?"
        show mum neutral_talk at right
        mum "I'm so sorry, baby~"
        show pov smirk_talk at left
        show mum embarrassed at right
        pov "Guess I should have seen that coming…"
        show pov smirk at left
        show mum bored_talk at right
        mum "You totally should have."
        show mum shocked_talk at right
        mum "Relax, though - I'm just messing with you~"
        show pov embarrassed at left
        mum "I couldn't never hold back from making love with you without a good reason, just like that."
        show pov confused at left
        show mum smirk_talk at right
        mum "Trust me, you are not the only one who enjoys our little rendezvous and our type of a good time~"
        show pov shocked at left
        show mum bored_talk at right
        mum "But you are still not getting any tonight."
        show pov sad at left
        show mum embarrassed_talk at right
        mum "I want you to sleep in early and rest as much as you can, just to be safe."
        show pov smirk_talk at left
        show mum neutral at right
        pov "You never stop taking care of me, do you?"
        show pov embarrassed at left
        show mum neutral_talk at right
        mum "Never once have stopped and never plan on ever stopping."
        mum "That's how much I love you~"
        show pov neutral_talk at left
        show mum neutral at right
        pov "And I love you just as much, if not more."
        show pov neutral at left
        show mum smirk_talk at right
        mum "I know~"

    #=RESULT END=

    #=RESULT=

    #-If Missus hasn't been romanced-
    else:
        show pov embarrassed at left
        show mum neutral_talk at right
        mum "Soooo, what's the deal with you and Effie?~"
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "Really?"
        pov "You are asking that now?"
        show pov confused at left
        show mum embarrassed_talk at right
        mum "Well, I can't help but feel a little curious!"
        show pov smirk at left
        mum "I mean, considering how close you two seem to be and how often her name comes up, you can't blame a woman for starting to form ideas in her head."
        show pov smirk_talk at left
        show mum embarrassed at right
        pov "You've been watching way too many dramas."
        show pov smirk at left
        show mum shocked_talk at right
        mum "Don't you bring them up on this."
        show mum neutral_talk at right
        mum "But really, what's the actual deal between you two?"
        show pov confused_talk at left
        show mum neutral at right
        pov "Well… considering what happened, and the fact we just patched up, I'd say we are at least back to being friends again."
        show pov embarrassed_talk at left
        pov "Which is a massive improvement from where we were, after I screwed things up - so I can't really complain, can I?"
        show pov embarrassed at left
        show mum shocked_talk at right
        mum "No, I suppose you can't…"
        show pov confused at left
        show mum bored_talk at right
        mum "Still, you don't get into those kinds of fights and grandeur displays of apology for just any kind of friend."
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Which proves to me that she is at least quite special, for you to go through all that for her to forgive you~"
        show pov bored_talk at left
        show mum confused at right
        pov "I… don't really have a defense for that…"
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Hehehe, you simply can't hide anything from a housewife with too much time in her hands and a subscription to all the detective and mystery dramas she could ask~"
        show pov embarrassed_talk at left
        show mum confused at right
        pov "We really need to get you a new hobby and get you out of the house more… "
        show pov smirk_talk at left
        show mum embarrassed at right
        pov "The old man certainly ain't gonna help with that."
        show pov smirk at left
        show mum embarrassed_talk at right
        mum "Ain't that the truth…"

        #=RESULT END=

    #=END=

    #-BACK TO REGULAR DIALOGUE-
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Still, I'm really happy you managed to patch things up with your friends!"
    show mum embarrassed_talk at right
    mum "I was certain you would - but I was still really worried for a second there!"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Trust me when I say, so was I."
    show pov confused at left
    show mum shocked_talk at right
    mum "Well, what's important is that everything turned out well in the end. I assume you were able to be open with them?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Yeah…"
    show pov shocked_talk at left
    show mum confused at right
    pov "Wasn't sure how they would react, but I'm happy they reacted the way they did."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "I feel like a huge weight on my chest has been lifted and that I can finally relax a little, if just for a moment."
    show pov confused at left
    show mum embarrassed_talk at right
    mum "That's great to hear, Honey."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Now, I don't want to pressure you or anything…"
    show mum embarrassed_talk at right
    mum "But just remember, I'm here and I'm more than willing to listen if you ever feel the need to share what happens, with me."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I…"
    pov "I will, soon. I just need to get some stuff in order and follow a lead that I have, in the whole thing."
    show pov neutral_talk at left
    show mum embarrassed at right
    pov "If anything, just to achieve some peace of mind or something to back up my claims and make it sound less crazy."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "I'm more than willing to wait for that."
    show mum neutral_talk at right
    mum "Remember, I always have and can make time for you whenever you need me."
    show pov neutral_talk at left
    show mum neutral at right
    pov "I know."
    pov "You are the best."
    show pov smirk_talk at left
    show mum smirk at right
    mum "You know it~"
    show pov shocked at left
    show mum bored_talk at right
    mum "Just promise me you won't end up in trouble because of it."
    show pov embarrassed_talk at left
    show mum bored at right
    pov "I…"
    pov "I'll try my best…"
    show pov confused at left
    show mum smirk_talk at right
    mum "Well, that doesn't fill me with confidence…"
    show pov embarrassed_talk at left
    show mum bored at right
    pov "I know, it's just…"
    show pov bored_talk at left
    show mum confused_talk at right
    pov "I don't really know what I'm gonna end up finding out. Or what it's gonna mean, in the end."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "You make it sound so dramatic. It really doesn't help me on trying to keep out of your business until you are ready to talk about things, you know?"
    show pov confused_talk at left
    show mum confused at right
    pov "R-left… My bad…"
    show pov bored at left
    show mum embarrassed_talk at right
    mum "Still, I shall not pressure you."
    mum "Just know, I'm always here for you for when you feel ready to talk."
    show pov confused_talk at left
    show mum neutral at right
    pov "I know… Thank you, truly…"
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "It's been my pleasure, Honey. No need to thank me."
    show pov neutral at left
    mum "Now, get some rest. And let me know if that bump starts to hurt again, OK?"
    show pov shocked at left
    show mum smirk_talk at right
    mum "Luckily, you don't need to go to work on Monday, so you can rest up for two days straight, left?"
    show pov shocked_talk at left
    show mum smirk at right
    pov "Actually, HR decided to give me the final tour of the place tomorrow, seeing as I have the day off and the whole team is going to be dealing with an inspection."
    show mum confused at right
    pov "I'm sure the old man has mentioned that by now?"
    show pov embarrassed at left
    show mum shocked_talk at right
    mum "Oh right, I remember he did mention something regarding that."
    show mum embarrassed_talk at right
    mum "Still, can't they postpone it? It is your day off, after all…"
    show pov neutral_talk at left
    show mum shocked at right
    pov "Hey, you wanted me to experience the opportunity of working for such a company, right?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Having to work on your day off {b}is{/b} just a part of the whole corporate lifestyle, left? For better or worse."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "Well, that is true… It's not like I haven't ever worked on my day off, but still…"
    show pov smirk_talk at left
    show mum neutral at right
    pov "Quirks of the trade, right? At least this way I won't miss an actual work day."
    show pov smirk at left
    show mum smirk_talk at right
    mum "Well, I'm happy you are taking it so well, then."
    show pov shocked at left
    show mum shocked_talk at right
    mum "Even I would be all grumpy and unmotivated if I was forced to work on my day off."
    show pov neutral_talk at left
    show mum smirk at right
    pov "Just trying to prove I'm doing my best here."
    show pov neutral at left
    show mum smirk_talk at right
    mum "I know you are, Honey. And I'm damn proud of you for it."
    show pov confused at left
    show mum neutral_talk at right
    mum "Well, in that case, I'll make your favorite tomorrow morning for taking this so seriously. I'd say you earned it."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Sweet!"
    show pov neutral at left
    show mum neutral_talk at right
    mum "For now, just rest up and tell me if you need anything, OK?"
    show mum smirk_talk at right
    mum "Goodnight, darling."
    show pov neutral_talk at left
    show mum smirk at right
    pov "You are the best!"

    #-Missus leaves the scene leaving the MC alone-

    $ renpy.pause(2.0)
    show pov bored at left
    hide mum with dissolve
    pov "…"
    show pov embarrassed at left
    pov "{i}I'm sorry I can't tell you anything; but I'm going to get to the bottom of this.{/i}"
    show pov sad at left
    pov "{i}I promise I'll tell you everything after that…{/i}"

    #=SCENE END=
    $ gtime = 3
    $ main_story = 115

    jump lbl_mybedroom_night_setup
