## Trapped With Allaway ##
label lbl_trapped_with_allaway:

    scene black
    with fade
    "A few hours have passed..."

    scene bg trappedwithallaway_0
    with fade
    mis "We really have to try and conserve our body heat like this."
    show bg trappedwithallaway_1
    mis "We're in a room with no heater in the middle of the night."
    show bg trappedwithallaway_2
    pov "I don't mind us cuddling close to each other."
    show bg trappedwithallaway_3
    mis "Couldn't you have used another word other than ‘cuddling'."
    show bg trappedwithallaway_4
    pov "..."
    show bg trappedwithallaway_5
    pov "I don't mind us snuggling closely like this."
    show bg trappedwithallaway_6
    mis "Hehe, I should've expected that."
    show bg trappedwithallaway_7
    pov "..."
    show bg trappedwithallaway_8
    pov "I've talked a good few hours about myself. I think it's time you tell me stuff about you."
    show bg trappedwithallaway_9
    mis "Do we really?"
    show bg trappedwithallaway_5
    pov "Yes, Miss. It's only fair."
    pov "I trusted you with my story, now it's time for you to trust me with yours."
    show bg trappedwithallaway_10
    mis "Hmm... What do you want to know?"
    show bg trappedwithallaway_11
    pov "Let's start with why you wanted to become a teacher."
    show bg trappedwithallaway_12
    mis "You know the saying, ‘if you can't do, teach'. Hehehe."

    menu:
        "I don't believe that was the case.":
            show bg trappedwithallaway_13
            pov "I don't believe that was the case to begin with."
            show bg trappedwithallaway_14
            mis "I've always wanted to be a teacher when I was young."
            show bg trappedwithallaway_0
            mis "I don't know why or what triggered my interest in it."
            mis "I guess when I was a young girl, I always saw teachers to be extremely smart and that they know everything."
            mis "And to have students look up to you for knowledge and wisdom..."
            mis "Possibly a power fantasy..."
            pov "Oooh, that's actually really kinky."
            mis "Ugh, [povname]. Don't read between the lines."
            mis "It wasn't meant to come off as means for me to... y'know..."
            mis "Yeah, I'll just stop there for now."
        "English? Humanities?":
            show bg trappedwithallaway_15
            pov "English? Humanities? Literature?"
            show bg trappedwithallaway_16
            mis "Ugh, don't say literature to me again."
            show bg trappedwithallaway_0
            mis "The only reason I do it is because it is part of curriculum."
            mis "I would better off doing film analysis but those come by once in a blue moon."
            mis "I've actually always wanted to be a teacher and it just so happens that the subjects I teach is what I do best in."
            mis "Not that I drool over the thought of essays or anything."
            mis "Life just has a way with things."
        "I get it.":
            show bg trappedwithallaway_17
            pov "I totally get it."
            show bg trappedwithallaway_18
            pov "Not everyone can get paid to do what they want, so they help other achieve dreams that they hoped for."
            show bg trappedwithallaway_0
            mis "Uh- yeah... I guess. You can say that."
            mis "I actually did want to be a teacher though."
            mis "I didn't grow up wanting to be a writer, or an English... speaker..."
            mis "Or some kind of humanitarian."
            mis "Just a plain ol' teacher, teaching what I'm good at."
            mis "Something I'm comfortable with."
            mis "I don't strive for anything ambitious, at the end of the day, I come home and do what I love."
            mis "And that's to be a lazy, fat slob with no one to judge me."
    show bg trappedwithallaway_19
    pov "Alright then, moving on to something else."
    pov "What do you like to do in your spare time?"
    pov "I know I told you that I like to [allawayatthecafe_hobby]."
    if skill_int >= 5:
        if missallaway_points <= 9:
            $ missallaway_points += 1
        else:
            $ missallaway_points = 10
        $ skill_int -= 4
        $ renpy.notify("You used 3 Intelligence Points\nYour relationship with Miss Allaway has increased")
        pov "And from what I'll say is a bit of intuition, you love your Webflicks, coffee, cakes and pastries."
        pov "Is there anything else I'm missing?"
        show bg trappedwithallaway_20
        mis "We've only known each other for a short period of time and already you know me extremely well."
        mis "You can add movies onto that list but I guess it really goes under Webflicks."
    else:
        if missallaway_points >= 1:
            $ missallaway_points -= 1
        else:
            $ missallaway_points = 0
        $ renpy.notify("Your relationship with Miss Allaway has decreased")
        show bg trappedwithallaway_21
        pov "I don't know what you like."
        show bg trappedwithallaway_22
        mis "Really? I figured that that should be obvious by this point."
        mis "It's not like we're complete strangers to each other."
        mis "There's only a few things that I really like in this world."
        show bg trappedwithallaway_20
        mis "Those are coffee, cakes and pastries, and Webflicks."
        mis "I guess you can throw in movies as well but they sorta go under Webflicks."
    show bg trappedwithallaway_5
    pov "Movies, aye? Movies... movies... movies..."
    pov "We should go watch a movie together."
    if whyamiintrouble_movieask == 1:
        show bg trappedwithallaway_22
        mis "You asked me that already, didn't you? Remember when you first caught me spyin-"
        show bg trappedwithallaway_23
        mis "I mean when we ran into each other outside the university gym?"
        show bg trappedwithallaway_24
        pov "Yeah, and you said ‘no', didn't you?"
        show bg trappedwithallaway_25
        mis "I said it was inappropriate because I'm still your teacher and you're still my student."
    else:
        show bg trappedwithallaway_25
        mis "Did you just ask me out on a date?"
        show bg trappedwithallaway_24
        pov "I... guess I did."
        show bg trappedwithallaway_24
        pov "Yeah! It's not a secret that I like you, Miss."
        show bg trappedwithallaway_2
        pov "I've nearly graduated, it's not all that weird, is it?"
        show bg trappedwithallaway_25
        mis "It's inappropriate is what it is."
        mis "I'm still your teacher and you're still my student. I can't be in any sort of romantic relationship with you."
    mis "I shouldn't even have to explain it to you."

    menu:
        "Doesn't that get you excited?":
            show bg trappedwithallaway_0
            pov "Doesn't that get you excited?"
            if skill_cha >= 15:
                if missallaway_points <= 7:
                    $ missallaway_points += 3
                else:
                    $ missallaway_points = 10
                $ skill_cha -= 12
                $ renpy.notify("You used 12 Charisma Points\nYour relationship with Miss Allaway has increased by 3")
                mis "..."
                mis "It does sound... exciting."
                pov "We're not supposed to be with each other, doesn't that sound..."
                pov "Titillating."
                mis "Even just thinking about it.. If we're being open and honest with each other."
            else:
                if missallaway_points >= 1:
                    $ missallaway_points -= 1
                else:
                    $ missallaway_points = 0
                $ renpy.notify("Your relationship with Miss Allaway has decreased")
                mis "[povname]... don't-"
                mis "Don't keep trying to push this on me. I'm trying to be realistic here.:"
                mis "We're not meant to be."
                mis "Face it."
        "It can be our little secret.":
            show bg trappedwithallaway_0
            pov "It can be our little secret."
            if skill_cha >= 10:
                if missallaway_points <= 8:
                    $ missallaway_points += 2
                else:
                    $ missallaway_points = 10
                $ skill_cha -= 7
                $ renpy.notify("You used 7 Charisma Points\nYour relationship with Miss Allaway has increased by 2")
                mis "You know me... I'm not the best with secrets."
                pov "Really? It seems to me like you're doing pretty well hiding your feelings from me."
                mis "What?! No, I'm not! It's stupidly transparent how much I want you-"
                mis "Fuck!"
                mis "Whoops... don't mean to swear."
                pov "..."
                pov "No one's here, Miss. Just us."
            else:
                if missallaway_points >= 1:
                    $ missallaway_points -= 1
                else:
                    $ missallaway_points = 0
                $ renpy.notify("Your relationship with Miss Allaway has decreased")
                mis "It will be a very dangerous secret if one at all."
                mis "I'm already trying to ignore your advances towards me and play it like nothing's happening."
                mis "But it is, and you just can't stop it."
                mis "Any further with you and someone's going to find out eventually."
                mis "I have my career, my reputation, my life at stake here, [povname]."
        "It doesn't have to be romantic.":
            show bg trappedwithallaway_0
            pov "It doesn't have to be romantic."
            if skill_cha >= 5:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_cha -= 3
                $ renpy.notify("You used 3 Charisma Points\nYour relationship with Miss Allaway has increased")
                pov "Just as friends, or even still just as a formal, teacher-student course related activity thing."
                pov "Maybe call it a one-on-one film excursion."
                pov "I don't care. As long as we can have some more time together."
                mis "..."
                mis "You've really thought long and hard about me, haven't you, [povname]."
            else:
                if missallaway_points >= 1:
                    $ missallaway_points -= 1
                else:
                    $ missallaway_points = 0
                $ renpy.notify("Your relationship with Miss Allaway has decreased")
                mis "Oh, but you will make it romantic, I know you will."
                mis "I know how you boys are with your secret agendas. I'm not stupid."
                mis "Miss me with that curve ball as the kids say these days."
                pov "You're the one that said it, not me."
        "I know, I'm sorry.":
            show bg trappedwithallaway_0
            pov "I know, I'm sorry."
            if skill_luc >= 12:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_luc -= 9
                $ renpy.notify("You used 9 Luck Points\nYour relationship with Miss Allaway has increased")
                mis "It's alright, as much as I want to make bad mistakes with you."
                mis "I have to keep a clean record and clean face."
                mis "Clean face, don't wanna walk around with your cum on me, am I right-"
                mis "..."
                mis "D-did... I just say that..."
            else:
                mis "It's okay, [povname]. At this point, all I'm doing is reminding you how much it is a bad idea."
                mis "Why can't you go after girls your own age?"
                mis "Doesn't anyone in the class interest you?"
                pov "It's not that, I'm not as picky as you think when it comes to women."
                pov "There's something about you that-"
                mis "As much as I wanna hear your flattery, I also don't."
    mis "Can we just... move onto some other topic?"
    pov "You know how these deep night conversations go, the longer we talk, the more personal things get."
    mis "{i}*Sigh*{/i} Hit me with it then. It's not like I have anything better to do right now."
    show bg trappedwithallaway_2
    pov "How's the dating game going with you? Are you seeing anyone?"
    show bg trappedwithallaway_24
    pov "Maybe even a friend with benny?"
    show bg trappedwithallaway_26
    mis "Who's benny?"
    show bg trappedwithallaway_27
    pov "Benefits. Friends with benefits."
    show bg trappedwithallaway_28
    mis "Ohhh! Oh, Jesus, [povname]. You're really gonna go there?"
    show bg trappedwithallaway_29
    mis "{i}*Sigh*{/i}"
    show bg trappedwithallaway_30
    pov "Just because you're my teacher, doesn't mean I'm not going to treat you and talk to you any differently than I would with my peers."
    pov "It's a single step towards getting close with a person, wouldn't you agree."
    show bg trappedwithallaway_31
    mis "Unfortunately, I see your point."
    show bg trappedwithallaway_29
    mis "I just always wonder why me though."
    show bg trappedwithallaway_32
    mis "..."
    show bg trappedwithallaway_33
    pov "So? Anyone?"
    show bg trappedwithallaway_34
    mis "Hm? Oh... uhm.. No."
    mis "Not really."
    show bg trappedwithallaway_35
    mis "My parents are nagging me to find someone at least."
    mis "But things just hasn't been going well for me."
    show bg trappedwithallaway_34
    mis "I used Flinter but haven't had any good experience with that app."
    mis "Most of the guys I have found on there are only looking to hook up or are uninteresting."
    show bg trappedwithallaway_36
    mis "I'm kind of embarrassed that I even resorted to using that app."
    show bg trappedwithallaway_37
    mis "That was a while ago though so you won't find me on there anymore."
    if crushonallaway_time == 1:
        show bg trappedwithallaway_38
        pov "What's the deal with you and Effie?"
        show bg trappedwithallaway_39
        mis "What about us? We're good friends."
    else:
        show bg trappedwithallaway_38
        pov "How close are you with Effie?"
        show bg trappedwithallaway_39
        mis "Why do you ask?"
        show bg trappedwithallaway_40
        pov "I just ask because I see you two talking and laughing a lot before class, like waay too often."
        show bg trappedwithallaway_41
        pov "Not that that's weird or that I'm saying Effie is a loner."
        pov "But she really prefers talking to you than any of the other girls in class."
        show bg trappedwithallaway_39
        mis "We're actually quite close friends."
    mis "I was her teacher for many years and a friendship has spontaneously sparked between use."
    mis "More so last year when she's been coming to me frequently for help."
    mis "She's really determined to get into a good college."
    show bg trappedwithallaway_40
    pov "Nothing more than that?"
    show bg trappedwithallaway_0
    mis "..."
    mis "Why? Did Effie say something to you?"
    if crushonallaway_time == 1:

        menu:
            "She told me...":
                pov "She told me that she helped you get off. Her words, not mine."
                mis "..."
                mis "That weasley bitch! That was meant to be between us!"
                pov "So, it's true?!"
                mis "..."
                mis "Nooooo..."
                mis "{i}*Sigh*{/i}"
                mis "Fucking, yeah."
                mis "[povname]. Girls, experiment- with each other a lot more than guys do."
                mis "It was normal."
                pov "Sex with your student is normal?"
                mis "I- uh-!"
                pov "Don't worry, Miss. I can keep a secret."
                pov "And please don't tell Effie I told you this, she's going to freak at the both of us."
                mis "Fine..."
                mis "You're digging me into a deeper and deeper hole, [povname]."

                jump lbl_trapped_with_allaway_2
            "Nope.":
                jump lbl_trapped_with_allaway_1
    else:
        jump lbl_trapped_with_allaway_1

label lbl_trapped_with_allaway_1:
    pov "Nope."
    pov "Didn't say a single thing, I was just curious, is all. I don't have a clue about you two."
    mis "Oh- good. We're just friends."

label lbl_trapped_with_allaway_2:
    mis "Is that all the questions you want to ask me, [povname]. I'm afraid to go any deeper into my personal life than what I've already shared."
    mis "Mind you that I don't usually and voluntarily share things like this to anyone."
    mis "It's just- because... you... are..."
    mis "..."
    show bg trappedwithallaway_14
    mis "We're trapped here alone with nothing to do."
    mis "And I'm not one to be the biggest fan of small talks."
    show bg trappedwithallaway_19
    pov "Don't worry, me neither. And I think I'm pretty much done with interrogating you."
    show bg trappedwithallaway_42
    pov "..."
    show bg trappedwithallaway_8
    pov "Thank you for being open with me."
    show bg trappedwithallaway_10
    mis "Whatever happens in class between you and me, stays with us to our graves. Got it?"
    show bg trappedwithallaway_43
    pov "..."
    show bg trappedwithallaway_44
    pov "You sure about that?"
    show bg trappedwithallaway_39
    mis "I'm serious, [povname]. Whatever we did and shared today remains between us and only us."

    jump lbl_trapped_and_teased
