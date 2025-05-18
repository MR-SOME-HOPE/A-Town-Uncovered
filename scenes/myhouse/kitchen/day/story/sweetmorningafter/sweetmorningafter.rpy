label lbl_sweet_morning_after:
    scene bg mykitchen_day
    with fade

    if parentsbedroommovie_threesome == 3:
        jump lbl_spicy_morning_after
    ##-This version of the scene only takes place if the player did not see one of the threesome scenes last night-

    ##-The Mc comes down the stairs and into the kitchen to meet with Sister and Missus who are also serving breakfast-

    show mum neutral at right
    show sis neutral at Position(xpos=1300)
    with dissolve

    $ renpy.pause(1.0)

    show pov neutral at left
    with dissolve
    $ renpy.pause(0.5)
    show pov neutral_talk at left

    pov "Good morning."
    show pov neutral at left
    show mum neutral at right
    show sis neutral_talk at Position(xpos=1300)
    sis "Finally, there he is!"
    sis "Can we please eat now, [missus]?"
    show pov neutral at left
    show mum angry_talk at right
    show sis neutral at Position(xpos=1300)
    mum "Let him sit down and join us, geez!"
    mum "You are acting like I never feed you, or something!"

    if parentsbedroommovie_threesome == 0:
        show pov neutral at left
        show mum neutral_talk at right
        show sis neutral at Position(xpos=1300)
        mum "Good morning, sweetie. Did you sleep okay?"
        show pov neutral_talk at left
        show mum neutral at right
        show sis neutral at Position(xpos=1300)
        pov "Y-Yeah, it’s been a while since we all slept together, hasn’t it?"
        show pov neutral at left
        show mum neutral_talk at right
        show sis neutral at Position(xpos=1300)
        mum "Oh, I think it’s been years since we did!"
        mum "At least on the same bed."
        show pov neutral at left
        show mum neutral at right
        show sis neutral_talk at Position(xpos=1300)
        sis "Yeah, even on our camping trips we rarely shared the tent rather than having [povname] and I shared one while you and dad shared the bigger one."
        show pov neutral at left
        show mum neutral_talk at right
        show sis neutral at Position(xpos=1300)
        mum "Well, as you two got bigger we simply couldn’t fit all together anymore."
        show mum smirk_talk at right
        mum "Plus, you were going on that whole “Rebellious Independence” phase in our last camping trip, [sister]."
        mum "So we figured it best to just get you and [povname] your own tent before you tore each other’s eyes out in a silly fight."
        show pov neutral_talk at left
        show mum neutral at right
        show sis neutral at Position(xpos=1300)
        pov "Back then, it was quite the possibility with how hostile you were, [sister]."
        show pov neutral at left
        show mum confused_talk at right
        show sis neutral at Position(xpos=1300)
        sis "Okay, what’s with you two putting me in the spotlight today?!"
        sis "Geez!"
        sis "We all have our phases growing up, alright?"
        show pov neutral at left
        show mum smirk_talk at right
        show sis neutral at Position(xpos=1300)
        mum "Oh? but you used to swear to me how it wasn’t a phase and how you were “Revealing your true rebellious nature” against the grown ups that could never understand you."
        mum "And let's not forget how you would also tell us how that boyfriend vocalist of yours would take you away one day whenever you got upset at us."
        show pov shocked_talk at left
        show mum neutral at right
        show sis neutral at Position(xpos=1300)
        pov "Oh God, is this her phase when she had her wall covered in “Chemicals at the Disco” and “My Panicked Romance” Posters?"
        pov "I remember how you could shine a flashlight at them and get practically flashbanged back from the amount of face grease that got stuck on them from all the times she would rub her face on them and kiss em too."
        pov "No wonder you had all those zits that summer."
        show pov shocked at left
        show mum neutral at right
        show sis angry_talk at Position(xpos=1300)
        sis "Keep talking shit about my then husband and I will cut you."
        show pov shocked at left
        show mum shocked_talk at right
        show sis angry at Position(xpos=1300)
        mum "Language!"
        mum "Also, it’s not good to threaten your [sisrole]!"
        show pov shocked at left
        show mum shocked at right
        show sis angry_talk at Position(xpos=1300)
        sis "Oh, don’t act as if you wouldn’t do the same if we talked bad about one of those korean drama actors you swoon over!"
        sis "What was his name?"
        sis "Lee Min-Something and Ahn Something-else Ki?"
        show pov shocked at left
        show mum angry_talk at right
        show sis angry at Position(xpos=1300)
        mum "Young lady, I will actually starve you if you don’t stop right now."
        mum "You keep those names in the same level of respect as you do the lord."
        show pov shocked at left
        show mum angry at right
        show sis angry_talk at Position(xpos=1300)
        sis "How is that any better than me threatening to cut him though?!"
        show pov smirk_talk at left
        show mum angry at right
        show sis angry at Position(xpos=1300)
        pov "Pfft-"
        pov "Ahahahaha!"

        ##-You take a moment to laugh at the random conversation and soon enough Mom and Sister join in as well-
        show pov neutral at left
        show mum sad_talk at right
        show sis neutral at Position(xpos=1300)
        mum "W-Well, it’s nice to know we can still kick back and laugh like this again."
        mum "I’m still really grateful that I got you kids back."
        show pov confused_talk at left
        show mum sad at right
        show sis confused at Position(xpos=1300)
        pov "What are you talking about?"
        show pov confused at left
        show mum sad at right
        show sis confused_talk at Position(xpos=1300)
        sis "Yeah, [missus], we never left!"
        sis "We’ve always been here and we’ll always be."

        ##-Missus gains a large smile and is clearly touched by that statement."
        show pov confused at left
        show mum neutral_talk at right
        show sis confused at Position(xpos=1300)
        mum "Yeah…"
        mum "You will, won’t you?"
        show pov neutral at left
        show mum neutral_talk at right
        show sis neutral at Position(xpos=1300)
        mum "I love you both…"
        mum "With all I have."
        show pov neutral_talk at left
        show mum neutral at right
        show sis neutral_talk at Position(xpos=1300)
        pov "We love you too."
        sis "Yeah."

    ##-Just then, the a phone starts going off, whoever the player didn’t fool around with last night will go and answer it, if the player didn’t fool around with anybody, then he will go and answer it-
    ##TO DO phone ring sound

    #-If you fooled around with Mom last night-
    if parentsbedroommovie_threesome == 1:
        show pov neutral at left
        show mum neutral_talk at right
        show sis neutral at Position(xpos=1300)
        mum "[sister], sweetie, can you take that while your [povsisrole] and I finish setting the table?"
        show pov neutral at left
        show mum neutral at right
        show sis neutral_talk at Position(xpos=1300)
        sis "Of course, [missus]!"
        sis "I’ll be right back."

        ##-Sister then heads off to the living room to answer the phone-
        show pov neutral_talk at left
        show mum neutral at right
        show sis neutral at Position(xpos=1300)
        pov "Weird time to call so early in the morning..."
        pov "I wonder who it is?"
        pov "Well, where should I star-"

        ##-You are suddenly silenced when Missus pulls you into her chest and smashes her lips against yours-
        show pov neutral_talk at left
        show mum neutral at right
        hide sis neutral
        pov "Mphh-!"

        ##-The two of you share a passionate kiss that Missus is clearly holding dominance over until the need to breath becomes far too strong-

        ##-When you pull apart, a string of saliva still connects your mouths together as Missus looks lovingly into your eyes-
        show pov neutral at left
        show mum smirk_talk at right
        mum "And of course, I love you most of all…"
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Before my mornings were never complete until I said good morning to you and your sister."
        show mum smirk_talk at right
        mum "Now I can just feel myself getting grumpy and bitter until I get my morning kiss from my man."
        mum "More energizing than any cup of coffee, too!"
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "G-glad you like it, [missus]."
        pov "I love you too."
        pov "B-But still do you think it's wise to be this clingy, with [sister] just out of the room?"
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Are you doubting how much I love and desire you, young man?"
        mum "Because I’ll do stuff to your dick that will have you begging for me to write my name on it and claim it for myself so you don’t do it again."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "W-what?"
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Hey, you may have been the bolder one with you going ahead and conquering me and all, But I have years of experience on the field you still yet to have."
        mum "So, how about I reach down your pants and we have some fun before your sister comes ba-"

        ##-She is interrupted out of a sudden by sister yelling at them from the other room-
        show pov embarrassed at left
        show mum smirk at right
        sis "[missus], [povname]!"
        sis "Come quick! You have to see this!"
        show pov embarrassed at left
        show mum angry_talk at right
        mum "Tch!… And it was just getting good…"
        mum "What is it pumpkin?"
        show pov embarrassed at left
        show mum neutral at right
        pov "Saved by the bell…"
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Oh, we are going to continue this later young man, don’t test me when I get my engine running."
        mum "Now come on, let’s see what she wants."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Y-Yes Ma’am!"

        ##-This causes the scene to end and move to the next one as the two of them head to the living room-
        jump lbl_alarming_news

    ##=RESULT END=




    #-If you fooled around with Sister last night-
    elif parentsbedroommovie_threesome == 2:
        show pov neutral at left
        show mum sad_talk at right
        show sis neutral at Position(xpos=1300)
        if winc == 0:
            mum "Why must we always get interrupted by something when we finally get a nice household moment to share?"
        else:
            mum "Why must we always get interrupted by something when we finally get a nice family moment to share?"
        mum "{i}*Sigh*{/i}"
        mum "I’ll go get it, kids, can you please finish arranging the table for us to have breakfast?"
        show pov neutral_talk at left
        show mum neutral at right
        show sis neutral at Position(xpos=1300)
        pov "Sure thing!"
        show pov neutral at left
        show mum neutral at right
        show sis neutral_talk at Position(xpos=1300)
        sis "We are right on it, [missus]!"
        show pov neutral at left
        show mum neutral_talk at right
        show sis neutral at Position(xpos=1300)
        mum "Thank you kids, I’ll be right back."

        ##-Mom then heads off to the living room to answer the phone-
        show pov neutral_talk at left
        hide mum neutral
        show sis neutral at Position(xpos=1300)
        pov "Weird time to call so early in the morning..."
        pov "I wonder who it is?"
        pov "Well, where should I star-"

        ##-You are suddenly stopped when Sister suddenly moves closer to you and stars covering your face in a multitude of kisses-
        show pov shocked_talk at left
        show sis smirk at Position(xpos=1300)
        pov "H-Hey, there, what are you-!"

        ##-You are then silenced when her lips collide with yours and the two of you share a gentle yet passionate kiss that Sister is clearly pouring a ton of love into it until the need to breath becomes far too strong and you separate-

        ##-When you pull apart, a string of saliva still connects your mouths together before Sister hugs you tight and rests upon your shoulder-
        show pov shocked at left
        show sis smirk_talk at Position(xpos=1300)
        sis "{i}*Sigh*{/i}"
        sis "God, I needed that as soon as I woke up."
        sis "Ten- no, twenty times better than getting a cup of coffee~"
        sis "Why did you take so long to get down?"
        sis "I was starting to get antsy without my morning kiss!"
        show pov embarrassed_talk at left
        show sis neutral at Position(xpos=1300)
        pov "W-Well, I had a rather good night yesterday so I slept in a bit."
        if winc == 0:
            pov "Still, do you think it’s wise for you to be throwing yourself at me when [missus] is right in the next room?"
        else:
            pov "Still, do you think it’s wise for you to be throwing yourself at me when mom is right in the next room?"
        show pov embarrassed at left
        show sis smirk_talk at Position(xpos=1300)
        sis "I-I know that!"
        sis "But, well…"
        sis "I still feel a bit… tingly after last night and it was kinda fun doing that sort of thing with the extra spice of almost getting caught, you know?"
        sis "I guess I’m coming to understand your fondness for public nudity a bit more now."
        show pov embarrassed at left
        show sis neutral at Position(xpos=1300)
        pov "Must you really bring that up every chance you get?"
        show pov embarrassed at left
        show sis smirk_talk at Position(xpos=1300)
        sis "Yep!"
        sis "Call it a punishment for worrying me so much."
        sis "Still though, do you think we could…"
        sis "You know…"
        sis "Fool around a little more before she comes back?"
        show pov embarrassed_talk at left
        show sis smirk at Position(xpos=1300)
        pov "Your really think we have enough ti-"

        ##-You are suddenly interrupted out of a sudden by Missus yelling at you two from the other room-
        show pov shocked at left
        show sis smirk at Position(xpos=1300)
        mum "Kids!"
        mum "Kids come quick, you have to see this!"
        show pov embarrassed at left
        show sis sad_talk at Position(xpos=1300)
        sis "{i}*Sigh*{/i}"
        sis "I guess not…"
        sis "We’re coming, [missus]!"
        show pov embarrassed_talk at left
        show sis sad at Position(xpos=1300)
        pov "Saved by the bell…"
        show pov embarrassed at left
        show sis smirk_talk at Position(xpos=1300)
        sis "Oh, we are going to continue this later, you smart ass."
        sis "Just you wait till I get my hands on you when you are least expecting me!"
        sis "Now come on, big guy, let’s see what she wants."
        show pov neutral_talk at left
        show sis smirk at Position(xpos=1300)
        pov "Right behind ya."

        jump lbl_alarming_news

        ##-This causes the scene to end and move to the next one as the two of them head to the living room-


        #=RESULT END=



    ##-If you didn’t fool around with anybody last night-
    elif parentsbedroommovie_threesome == 0:
        show pov neutral_talk at left
        show mum neutral at right
        show sis neutral at Position(xpos=1300)
        pov "Weird time to call so early in the morning..."
        pov "Any of you expecting a call?"
        show pov neutral at left
        show mum neutral_talk at right
        show sis neutral at Position(xpos=1300)
        mum "Not that I know of."
        show pov neutral at left
        show mum neutral at right
        show sis neutral_talk at Position(xpos=1300)
        sis "All my calls would go directly to my phone if someone was looking for me."
        show pov neutral at left
        show mum confused_talk at right
        show sis neutral at Position(xpos=1300)
        mum "Maybe it’s for your [povdadrole]?"
        show pov neutral_talk at left
        show mum neutral at right
        show sis neutral at Position(xpos=1300)
        pov "I’ll go get it, you can go ahead and start eating if you want."
        show pov neutral at left
        show mum neutral at right
        show sis neutral_talk at Position(xpos=1300)
        sis "Sounds like a pla-!"
        show pov neutral at left
        show mum neutral at right
        show sis neutral_talk at Position(xpos=1300)
        if winc == 0:
            mum "Don’t be silly darling, we’ll wait for you and have a nice household breakfast."
        else:
            mum "Don’t be silly darling, we’ll wait for you and have a nice family breakfast."
        show pov neutral at left
        show mum neutral at right
        show sis sad_talk at Position(xpos=1300)
        sis "But, [missus]!"
        show pov neutral at left
        show mum neutral_talk at right
        show sis sad at Position(xpos=1300)
        mum "And your [sisrole] is going to wash the dishes if she keeps complaining about it."
        show pov neutral at left
        show mum neutral at right
        show sis sad_talk at Position(xpos=1300)
        sis "Lips are sealed!"
        show pov neutral_talk at left
        show mum neutral at right
        show sis sad at Position(xpos=1300)
        pov "I’ll make it quick, don’t worry about it."

        ##-Mc then heads to the living room to grab the phone and answer the call, looking on at the kitchen as Missus and Sister seem to be having a conversation-


        jump lbl_sweet_morning_after_phone_call
