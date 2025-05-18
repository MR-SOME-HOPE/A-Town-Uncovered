## Why am I in trouble? ##
label lbl_why_am_i_in_trouble:
    default whyamiintrouble_leave = 0
    default whyamiintrouble_fightclub = 0
    default whyamiintrouble_movieask = 0

    scene bg schoolyard_night
    with fade
    show pov shocked at left
    with dissolve
    show mis angry_talk at right
    with dissolve
    mis "You better give me a good reason for why I shouldn't give you detention tomorrow."
    show pov shocked_talk at left
    show mis angry at right
    pov "What?! What did I do?"
    show pov shocked_talk at left
    show mis angry at right
    pov "Why am I the one in trouble?"
    show pov angry at left
    show mis sad_talk at right
    mis "B-because! You're not supposed to be here at this hour."
    show pov confused_talk at left
    show mis shocked at right
    pov "Isn't the gym available for public use?"
    show pov bored_talk at left
    show mis embarrassed at right
    pov "I'm pretty sure the gym is open for public use."
    show pov confused_talk at left
    show mis sad at right
    pov "Coach Fistem is right inside, go talk to him about ‘trespassing' at this hour."
    show pov confused at left
    show mis sad_talk at right
    mis "No, no. I rather not. I don't like him, his name turns me off."
    show pov confused_talk at left
    show mis shocked at right
    pov "Turns you off?"
    show pov bored at left
    show mis shocked_talk at right
    mis "Hmm? I didn't say that."
    show pov bored_talk at left
    show mis bored at right
    pov "Yes, yo-"
    show pov bored at left
    show mis bored_talk at right
    mis "[povname]. I'm going to give you the count of 3 to leave the premises."
    show pov confused_talk at left
    show mis angry at right
    pov "What are you even doing here at this hour? Didn't university finish hours ago?"
    show pov confused at left
    show mis angry_talk at right
    mis "1..."

    menu:
        "I'm not leaving until I get an answer.":
            show pov confused_talk at left
            show mis angry at right
            pov "I'm not leaving until I get an answer."
        "Leave":
            show pov sad_talk at left
            show mis smirk at right
            pov "Alright! I'm leaving... goodnight, Miss."
            $ whyamiintrouble_leave = 1
            $ missallaway_path = 1.5

            jump lbl_townmap_setup
    show pov confused at left
    show mis angry_talk at right
    mis "2..."

    menu:
        "I'm not afraid of you.":
            show pov confused_talk at left
            show mis angry at right
            pov "I'm not afraid of you, Miss."
        "Leave":
            show pov sad_talk at left
            show mis smirk at right
            pov "Alright! I'm leaving... goodnight, Miss."
            $ whyamiintrouble_leave = 1
            $ missallaway_path = 1.5

            jump lbl_townmap_setup
    show pov confused at left
    show mis angry_talk at right
    mis "3..."

    menu:
        "Alright! I'm leaving!":
            show pov sad_talk at left
            show mis smirk at right
            pov "Alright! I'm leaving, don't get your knickers in a twist."
            $ whyamiintrouble_leave = 1
            $ missallaway_path = 1.5

            jump lbl_townmap_setup
        "Stay silent":
            show pov bored at left
            show mis angry at right
            pov "..."
    $ whyamiintrouble_fightclub = 1
    show mis angry at right
    mis "..."
    show mis sad_talk at right
    mis "Really, [povname]?"
    show pov smirk_talk at left
    show mis bored at right
    pov "Does it look like I'm a 5 year old? That counting thing doesn't work on me."
    show pov smirk at left
    show mis sad_talk at right
    mis "Unfortunately."
    show pov confused_talk at left
    show mis sad at right
    pov "So... why are you here this late at night?"
    show mis embarrassed at right
    pov "Lots of work to mark?"
    show pov confused at left
    show mis embarrassed_talk at right
    mis "I guess you can say that. Just been checking some work.. out..."
    mis "Tough... and rough... glistening sweat..."
    show mis embarrassed at right
    mis "..."
    show mis bored_talk at right
    mis "I'm very thorough."
    show pov confused_talk at left
    pov "Uh-huh..?"
    show pov confused_talk at left
    show mis confused at right
    pov "Isn't it better to take the work with you to do in the comfort of your own home?"
    show pov confused at left
    show mis smirk_talk at right
    mis "You enjoy the home...work I give you, [povname]?"
    show mis smirk at right
    pov "..."
    show pov smirk_talk at left
    pov "Touche. Very touche."
    show pov embarrassed at left
    show mis bored_talk at right
    mis "Well, for the record. I already knew it was a fight club. I'm not oblivious to it, it's been going on for the past few years."
    show pov confused at left
    show mis sad_talk at right
    mis "Especially with the testosterone-filled... boys."
    show pov confused at left
    show mis embarrassed_talk at right
    mis "{i}*Clears throat*{/i} Besides, I love the movie. I'd say it's one of my favourites."
    show pov confused_talk at left
    show mis neutral at right
    pov "Movie?"
    show pov neutral at left
    show mis neutral_talk at right
    mis "Yeah, Fight Club."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Oh, right, right."
    if fightclub_seen == 0:

        menu:
            "Maybe we can watch it together sometime.":
                $ whyamiintrouble_movieask = 1
                show pov smirk_talk at left
                show mis bored at right
                pov "Maybe we can watch it together sometime."
                if skill_cha >= 3:
                    $ skill_cha -= 3
                    if missallaway_points <= 9:
                        $ missallaway_points += 1
                    else:
                        $ missallaway_points = 10
                    $ renpy.notify("You used 3 Charisma Points\nYour relationship with Miss Allaway has increased")
                    show pov embarrassed at left
                    show mis confused_talk at right
                    mis "Are you asking me on a date?"

                    menu:
                        "If you want to put a label on it.":
                            show pov embarrassed_talk at left
                            show mis bored at right
                            pov "If you want to put a label on it, then sure."
                            show pov sad at left
                            show mis bored_talk at right
                            mis "[povname]. That's really inappropriate. I'm your teacher."
                            mis "Look, I'm flattered you have an interest in me but dropping all formalities. I'm not willing to risk going to jail for you."
                            show pov embarrassed at left
                            mis "Nothing personal, it's all business and legal reasons."
                            show mis embarrassed_talk at right
                            mis "You know how these things are."
                            show mis sad_talk at right
                            mis "Sadly."
                            show pov embarrassed_talk at left
                            show mis sad at right
                            pov "Well, it doesn't have to be a date. Just as friends? We can be friends, right?"
                        "Not a date, just as friends.":
                            show pov smirk_talk at left
                            show mis embarrassed at right
                            pov "Not a date, that's a little farfetched. Just as friends?"
                            show pov embarrassed_talk at left
                            show mis sad at right
                            pov "Y'know, who happen to be a teacher and her student."
                            show pov sad_talk at left
                            show mis sad at right
                            pov "I totally get the whole y'know, legal aspect of things."
                            show pov shocked_talk at left
                            show mis embarrassed at right
                            pov "I don't wanna rush- I mean push!"
                            show pov embarrassed_talk at left
                            pov "I don't wanna push things."
                            show mis sad at right
                            pov "It's just a movie, right?"
                            show pov embarrassed at left
                            mis "..."
                    show pov shocked at left
                    show mis sad_talk at right
                    mis "You're friendzoning me already?"
                    show pov shocked_talk at left
                    show mis shocked at right
                    pov "What?"
                    show pov sad at left
                    show mis shocked_talk at right
                    mis "What? I- I should go. Enough of this topic, [povname]."
                    show pov sad_talk at left
                    show mis embarrassed at right
                    pov "Miss, I didn't mean... I- I don't even know what I meant."
                    show pov embarrassed at left
                    show mis embarrassed_talk at right
                    mis "It's okay."
                    mis "Be safe going home, [povname]."
                    mis "I'll see you in class."
                    show pov embarrassed_talk at left
                    show mis embarrassed at right
                    pov "See you, Miss Allaway."
                    $ missallaway_path = 1.5

                    jump lbl_townmap_setup
                else:
                    show pov embarrassed at left
                    show mis bored_talk at right
                    mis "Mmm, yeah. Not a very wise thing to suggest there, [povname]."
                    show pov sad at left
                    mis "Look, I'm flattered you have an interest in me but dropping all formalities. I'm not willing to risk going to jail for you."
                    show pov embarrassed at left
                    mis "Nothing personal, it's all business and legal reasons."
                    show mis confused_talk at right
                    mis "You know how these things are. Teacher and student relationships."
                    show pov embarrassed_talk at left
                    show mis confused at right
                    pov "Yeah, no. Of course. It was more of a joke, sorta. Haha..."
                    show pov sad at left
                    show mis confused_talk at right
                    mis "Oh... well. Just in case you actually weren't. It's never going to happen. Again, nothing personal."
                    show pov sad_talk at left
                    show mis confused at right
                    pov "Yup, I got it. Forget I even said that, Miss. Sorry, how stupid of me."
                    show pov sad at left
                    show mis bored_talk at right
                    mis "It's okay."
                    show pov embarrassed at left
                    show mis confused_talk at right
                    mis "I'll be heading home now."
                    show mis neutral_talk at right
                    mis "Be safe going home, [povname]."
                    show mis confused_talk at right
                    mis "I'll see you in class."
                    show pov embarrassed_talk at left
                    show mis neutral at right
                    pov "See you, Miss Allaway."
                    $ missallaway_path = 1.5

                    jump lbl_townmap_setup
            "I'll have to watch that myself sometime.":
                show pov neutral_talk at left
                show mis neutral at right
                pov "I'll have to get around to watching that myself sometime."
                pov "I've heard great things about it."
                show pov neutral at left
                show mis neutral_talk at right
                mis "You won't regret it. Brad Fitt is amazing in it."
                show pov smirk_talk at left
                show mis confused at right
                pov "Did you know in Japan, they call him ‘Buraffi'?"
                show pov smirk at left
                show mis neutral_talk at right
                mis "Heh... Buraffi. That's fun to say."
                show pov smirk_talk at left
                show mis neutral at right
                pov "Isn't it?"
                show pov neutral at left
                show mis embarrassed_talk at right
                mis "Anyway, I think it's time we head back home."
                show pov smirk at left
                show mis sad_talk at right
                mis "Take care on your way, okay, [povname]. I don't like the dark, it always feels like someone's watching."
                show pov smirk_talk at left
                show mis embarrassed at right
                pov "Haha, I will, you take care too, Miss."
                $ missallaway_path = 1.5

                jump lbl_townmap_setup
    else:
        show pov neutral_talk at left
        show mis neutral at right
        pov "I've seen the movie before."
        show pov neutral at left
        show mis neutral_talk at right
        mis "What do you think of it?"

        menu:
            "I love it.":
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ renpy.notify("Your relationship with Miss Allaway has increased")
                show pov neutral_talk at left
                show mis neutral at right
                pov "I love it, one of my favourite movies."
                show pov neutral at left
                show mis smirk_talk at right
                mis "You're just saying that because I said it. It can't be your favourite movie too."
                show pov neutral_talk at left
                show mis smirk at right
                pov "Oh, but it really is, at least it's up there on my list of greatest movies ever."
                show pov smirk at left
                show mis neutral_talk at right
                mis "Hmm, I guess I can believe that."
                show mis smirk_talk at right
                mis "Hehe, well look at us, [povname]. We have something in common."
                show pov embarrassed at left
                show mis smirk_talk at right
                mis "That's the first step, isn't it?"
                show pov embarrassed_talk at left
                show mis shocked at right
                pov "What are you talking about?"
                show pov confused at left
                show mis embarrassed_talk at right
                mis "Oh, uh- nothing. I- I should be going home. You should be too, it's too dark out."
                show pov confused_talk at left
                show mis embarrassed at right
                pov "Yeah, I guess. The dark doesn't really scare me."
                show pov smirk at left
                show mis sad_talk at right
                mis "It does for me, I always feel like someone's watching me..."
                show pov neutral at left
                show mis embarrassed_talk at right
                mis "Anyhoo! Take care, [povname]."
                show pov neutral_talk at left
                show mis embarrassed at right
                pov "See you, Miss."
                $ missallaway_path = 1.5

                jump lbl_townmap_setup
            "It's an alright movie.":
                show pov smirk_talk at left
                show mis confused at right
                pov "It's an alright movie. I get the appeal."
                show pov neutral at left
                show mis confused_talk at right
                mis "At least you're honest about it."
                show pov confused at left
                show mis bored_talk at right
                mis "Unless you're one of those hipster kids who just say those things to seem different."
                show pov smirk_talk at left
                show mis neutral at right
                pov "Nope, I just genuinely think it's a pretty alright movie."
                show pov smirk at left
                show mis neutral_talk at right
                mis "Maybe I can convince you one day to reconsider it."
                show pov smirk_talk at left
                show mis neutral at right
                pov "You can try."
                show pov smirk at left
                show mis smirk_talk at right
                mis "Oh, you know I will, one day."
                show pov neutral at left
                show mis neutral_talk at right
                mis "We should be going home. It's too dark out."
                show pov confused_talk at left
                show mis embarrassed at right
                pov "Yeah, I guess. It doesn't really scare me though."
                show pov smirk at left
                show mis sad_talk at right
                mis "It does for me, I always feel like someone's watching me..."
                show pov neutral at left
                show mis embarrassed_talk at right
                mis "Anyhoo! Take care, [povname]."
                show pov neutral_talk at left
                show mis embarrassed at right
                pov "See you, Miss."
                $ missallaway_path = 1.5

                jump lbl_townmap_setup
            "It was a pretty bad watching experience.":
                if missallaway_points >= 1:
                    $ missallaway_points -= 1
                else:
                    $ missallaway_points = 0
                $ renpy.notify("Your relationship with Miss Allaway has decreased")
                show pov confused_talk at left
                show mis bored at right
                pov "It was a pretty bad watching experience for me."
                show pov confused at left
                show mis bored_talk at right
                mis "How dare you say that about it! It's a film classic, and no matter what you say, it will always be a film classic."
                show mis shocked_talk at right
                mis "It has one of the most iconic lines in the history of iconic lines."
                show pov confused_talk at left
                show mis bored at right
                pov "Yeah, but that doesn't make it a great movie."
                show pov confused at left
                show mis bored_talk at right
                mis "It wasn't really my main point, [povname]."
                show pov neutral at left
                show mis confused_talk at right
                mis "Heh, well maybe there'll be another movie that we actually mutually like."
                show pov bored at left
                mis "I doubt your cinematic taste are functional though."
                show pov smirk_talk at left
                show mis confused at right
                pov "Haha, ouch. We all have our personalized interests."
                show pov embarrassed at left
                show mis smirk_talk at right
                mis "I guess. Just some better than others."
                show pov embarrassed_talk at left
                show mis embarrassed at right
                pov "Don't have to be so hostile, Miss."
                show pov neutral at left
                show mis embarrassed_talk at right
                mis "Hehe.. I'm kidding."
                show pov embarrassed at left
                show mis bored_talk at right
                mis "Not really."
                show mis neutral_talk at right
                mis "Anyway, I should get home. You should too."
                show pov embarrassed_talk at left
                show mis neutral at right
                pov "Yeah, I should"
                show pov embarrassed at left
                show mis confused_talk at right
                mis "Take care, okay, [povname]? I don't like the dark, it always feels like someone's watching."
                show pov embarrassed_talk at left
                show mis neutral at right
                pov "I will, you too."
                $ missallaway_path = 1.5

                jump lbl_townmap_setup
            "It's overrated." if skill_int >= 3:
                $ skill_int -= 3
                $ renpy.notify("You used 3 Intelligence Points")
                show pov smirk_talk at left
                show mis confused at right
                pov "I think it's overrated. There are much better Brad Fitt movies than that."
                show pov smirk at left
                show mis smirk_talk at right
                mis "Oh, Brad Fitt movies, huh? Like what?"

                menu:
                    "Ingloruious Basterds.":
                        if missallaway_points <= 8:
                            $ missallaway_points += 2
                        else:
                            $ missallaway_points = 10
                        $ renpy.notify("Your relationship with Miss Allaway has increased by 2")
                        show pov smirk_talk at left
                        show mis confused at right
                        pov "Inglourious Basterds."
                        show pov smirk at left
                        show mis smirk_talk at right
                        mis "Ohh, you know what, [povname]. I love your taste in films."
                        mis "That's actually a not-at-all bad choice."
                        mis "I'm impressed."
                    "Mr and Mrs Smith.":
                        show pov smirk_talk at left
                        show mis confused at right
                        pov "Mr and Mrs Smith."
                        show pov embarrassed at left
                        show mis smirk_talk at right
                        mis "Mr and Mrs Smith.? Seriously?"
                        show mis confused_talk at right
                        mis "Alright, on a serious note, the action, pretty meh. The romance aspect can go up a dog's butt."
                        show mis smirk_talk at right
                        mis "I can't believe you actually think that's a better movie than Fight Club."
                    "Moneyball.":
                        if missallaway_points <= 9:
                            $ missallaway_points += 1
                        else:
                            $ missallaway_points = 10
                        $ renpy.notify("Your relationship with Miss Allaway has increased")
                        show pov smirk_talk at left
                        show mis confused at right
                        pov "Moneyball."
                        show pov neutral at left
                        show mis confused_talk at right
                        mis "Ehh.. it's a good movie. It's just a little ‘overrated'."
                        show pov smirk_talk at left
                        show mis smirk at right
                        pov "Oh, c'mon. Don't pull that on me."
                        show pov neutral at left
                        show mis neutral_talk at right
                        mis "It's a good movie. Though I did fall asleep to it, so I guess it's good for that."
        show pov confused at left
        show mis neutral_talk at right
        mis "Well, I should actually be heading home, [povname]. You should too. It's dark out."
        show pov smirk_talk at left
        show mis neutral at right
        pov "Yeah, good idea."
        show pov smirk at left
        show mis confused_talk at right
        mis "Be careful going home, okay? I don't like the dark, it always feels like someone's watching."
        show pov smirk_talk at left
        show mis neutral at right
        pov "Haha, I will, Miss. You take care too."
        $ missallaway_path = 1.5

        jump lbl_townmap_setup
