label lbl_lashley_lunch_talk:
    default lashley_questions_count = 0
    default lashley_questions_asked_porn_bust = False
    default lashley_questions_asked_everything_alright = False
    default lashley_questions_asked_hows_work = False

    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    ##-Scene takes place in the cafeteria where Lashley is eating alone looking kind of sad once you approach her, the Mc can choose to talk to her or not, if he picks not to speak with her, the scene ends and the player can go back to picking who to talk to in the cafeteria-
    scene bg schoolcafeteria_day
    pov "{i}I see Director Lashley eating alone.{/i}"

    menu:
        "Talk to Lashley":
            #scene bg lashleylunchtalk_temp1
            scene bg lashleylunchtalk_eyesdown_sad
            with fade
            ## CG SCENE (PRI LASHLEY SIMILAR TO MISS ALLAWAY CAFETERIA SCENE)

        "Go on about your day":
            pov "{i}I'll just leave her be.{/i}"
            jump lbl_schoolcafeteria_day

    pov "Director Lashley?"
    scene bg lashleylunchtalk_eyesup_confused
    pri "Hmm?"
    scene bg lashleylunchtalk_eyesup_surprised_talk
    pri "Oh, good morning, [povname]."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "I trust you've been having a good day?"
    scene bg lashleylunchtalk_eyesup_neutral
    pov "Uh… Yeah."
    pov "You doing okay?"
    scene bg lashleylunchtalk_eyesup_surprised_talk
    pri "Oh, quite so!"
    scene bg lashleylunchtalk_eyesup_bored_talk
    pri "Nice early morning, some exercise along with my daily prayers and then a light breakfast before coming straight to work."
    scene bg lashleylunchtalk_eyesup_confused_talk
    pri "Why do you ask?"
    scene bg lashleylunchtalk_eyesup_confused
    pov "Oh, nothing it's just…"
    pov "I dunno, you are looking a bit down?"
    scene bg lashleylunchtalk_eyesdown_sad_talk
    pri "W-Well…"
    pri "It's nothing major, but the few times I eat in the cafeteria there is a certain tension in the air around me."
    scene bg lashleylunchtalk_eyesup_sad_talk
    pri "Kids make sure to stay at least a few tables away to avoid being heard by the administrator."
    pri "The stares and whispers are enough to make anyone uncomfortable."
    scene bg lashleylunchtalk_eyesdown_sad
    pov "Why are you eating on your own?"
    pov "Don't teachers have a teachers lounge or at least a table for them to lunch together?"
    scene bg lashleylunchtalk_eyesup_sad_talk
    pri "We do have a lounge, but most teachers would rather eat in their own classrooms while they do some work."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "I am not about to complain about good work ethic."
    scene bg lashleylunchtalk_eyesup_confused
    pov "Well, why not eat in your office, then?"
    scene bg lashleylunchtalk_eyesup_sad_talk
    pri "Normally I do, but I forgot to pack a lunch with me this morning and you are not allowed to bring a tray outside the cafeteria premises."
    pri "It's not a good look for your university, to have the director not respect the rules they enforce."
    scene bg lashleylunchtalk_eyesdown_sad
    pov "Fair enough."
    pov "Still, why the long face?"
    pov "I thought you were used to most students keeping their distance from you."
    scene bg lashleylunchtalk_eyesup_sad_talk
    pri "W-Well, that's true…"
    scene bg lashleylunchtalk_eyesup_bored_talk
    pri "It's really nothing, really."
    pri "It's just that I had a bit of a… confrontation back home, and well…"
    pri "Kind of made me realize how lonely I am sometimes…"
    scene bg lashleylunchtalk_eyesup_bored
    pov "Oh…"
    pov "Well, would it be okay for me to join you?"
    scene bg lashleylunchtalk_eyesup_surprised_talk
    pri "Y-You mean it?"
    scene bg lashleylunchtalk_eyesup_embarrassed_talk
    pri "Don’t feel obliged to do so. Really, it’s not a big deal."
    scene bg lashleylunchtalk_eyesup_confused
    pov "I insist."
    scene bg lashleylunchtalk_eyesup_sad_talk
    pri "B-But, aren’t you worried about getting a lot of attention from being seen hanging around the administrator?"
    scene bg lashleylunchtalk_eyesdown_sad
    pov "I’m already the new kid in town, Director Lashley."
    pov "There isn’t a lot I can do to draw even more attention to myself."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "That’s true…"
    scene bg lashleylunchtalk_eyesdown_neutral
    pri "…"
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "You have a kind soul, [povname]."
    pri "Please, go ahead and sit."
    scene bg lashleylunchtalk_eyesup_neutral
    pov "Don’t mind if I do."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "So, how are things going for you?"
    scene bg lashleylunchtalk_eyesup_neutral
    pov "So far so good, one can’t complain."
    pov "The town is really something and so far I’ve met a few nice people I hope to be friends with."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "That is such a relief."
    pri "I was worried you might have some trouble fitting in the first time I saw you, so I prayed you would adapt quickly."
    pri "Though, I was quite relieved when I first met you so I knew you would be fine."
    scene bg lashleylunchtalk_eyesup_neutral
    pov "Relieved? In what way?"
    scene bg lashleylunchtalk_eyesup_surprised_talk
    pri "Well, I was praying every night, for a week, that you wouldn’t be some sort of delinquent or bully or an overall troublemaker."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "I thanked the good lord for an hour once I properly spoke to you the first time."
    pri "You seem like a good person so I’m sure you won’t have any trouble at all to fit in."
    scene bg lashleylunchtalk_eyesup_neutral
    pov "Glad to hear I made a good first impression."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "Quite a good one indeed!"
    scene bg lashleylunchtalk_eyesup_neutral

    menu ask_lashley_all_questions:
        "How are the 'Porn-Bust’s' going?"if not lashley_questions_asked_porn_bust:
            $ lashley_questions_asked_porn_bust = True
            $ lashley_questions_count += 1
            pov "So, changing the subject, how is the whole “Porn-Busting” crusade going?"
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "Quite well, luckily."
            pri "The student from the other day kept his whole “I was framed” thing for a while, eventually caved under pressure when I threatened calling his parents."
            pri "Even pointed fingers at his friends when I started adding extra weeks to his punishment."
            pri "Have six people in detention because of it, so hopefully they’ll learn their lesson!"
            scene bg lashleylunchtalk_eyesup_neutral
            pov "Quite a good bust, then."
            scene bg lashleylunchtalk_eyesup_surprised_talk
            pri "Quite so!"
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "If I can give a student a chance at redemption, then I have quite a good week."
            pri "Plus, they help the university remain looking clean."
            scene bg lashleylunchtalk_eyesup_neutral
            pov "You have them do hard labor in detention?"
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "Depends on the offense."
            scene bg lashleylunchtalk_eyesup_bored_talk
            pri "Repeating offenders are tasked with painting the facilities, after hours, or help cafeteria workers or janitors clean."
            pri "First time offenders have extra assignments or help teachers with coursework grading, after hours."
            pri "Everything with approval from parents, of course."
            pri "Better than just having them hanging out in a classroom wasting time."
            scene bg lashleylunchtalk_eyesup_bored
            pov "Good point."
            pov "Bonus points for creativity."
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "The path to redemption is through hard work and the lord, for he said it best."
            pri "Ephesians 1:7"
            scene bg lashleylunchtalk_eyesup_neutral
            pov "Right, yes, of course."
            pov "Who could forget it?"
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "Glad to see a fellow verse enthusiast!"
            pri "I keep them close to mind whenever I need guidance."
            pri "I found it better to just cite the chapter and verse number rather than the whole verse itself."
            scene bg lashleylunchtalk_eyesup_sad_talk
            pri "People kind of tune me out when I do that. I get it, no one likes a long sermon."
            scene bg lashleylunchtalk_eyesup_confused_talk
            pri "So hopefully citing the chapter and its numbers will bring interest in others to look them up and provide them guidance when needed!"
            scene bg lashleylunchtalk_eyesup_neutral
            pov "Is that so? That’s kind of you."
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "I’m not about to push my beliefs onto someone else unwilling."
            pri "The lord's arms are open to anyone and everyone, but they must be the one making the choice to embrace him back."
            scene bg lashleylunchtalk_eyesup_neutral

        "Everything alright at home?"if not lashley_questions_asked_everything_alright:
            $ lashley_questions_asked_everything_alright = True
            $ lashley_questions_count += 1
            pov "And how’s everything at home?"
            scene bg lashleylunchtalk_eyesup_confused
            pov "You mentioned something happened this morning?"
            scene bg lashleylunchtalk_eyesup_confused_talk
            pri "Oh, did I?"
            scene bg lashleylunchtalk_eyesup_bored_talk
            pri "I apologize, I don’t mean to go much into detail about my personal life for obvious reasons."
            pri "Last thing I want is having the more troublemaking students know where I reside."
            scene bg lashleylunchtalk_eyesup_bored
            pov "Fair enough."
            pov "Still, I hope everything’s alright?"
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "Oh yes, thank you for your concern."
            scene bg lashleylunchtalk_eyesup_bored_talk
            pri "It’s just that having to eat breakfast alone for the hundredth time tends to get you down, you know?"
            scene bg lashleylunchtalk_eyesup_bored
            pov "Busy family?"
            scene bg lashleylunchtalk_eyesup_bored_talk
            pri "They work nearly 24 hours a day, 7 days a week and 365 days of the year. I don’t really get to see them often."
            scene bg lashleylunchtalk_eyesup_bored
            pov "Sounds really unhealthy."
            scene bg lashleylunchtalk_eyesup_sad_talk
            pri "Yeah, I really worry about them."
            pri "Sometimes I hear them late at night still working but they toss my worries aside, assuring me that they are fine."
            scene bg lashleylunchtalk_eyesdown_sad
            pov "Sounds rough."
            scene bg lashleylunchtalk_eyesup_sad_talk
            pri "It is, but that's family. I am not about to put myself between their career and life goals, but I’ll always be there if they burn themselves out or need a friend."
            scene bg lashleylunchtalk_eyesdown_sad
            pov "It’s only natural for you to worry, especially if they are working that hard."
            pov "You sound really loving and attentive of them. I’m certain that they appreciate everything you do."
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "You are so sweet, [povname]. Thank you."
            scene bg lashleylunchtalk_eyesup_neutral

            if skill_cha >= 3:
                $ skill_cha -= 3
                $ renpy.notify("You used 3 Charisma Points")
                $ renpy.pause(1.0,hard=True)

                $ add_points("principallashley_points",2)
                scene bg lashleylunchtalk_eyesup_shocked
                pov "I know for sure I would enjoy you fussing over me."
                pov "You seem so sweet and attentive, I am bound to get spoiled if you were to look after me."
                scene bg lashleylunchtalk_eyesup_embarrassed_talk
                pri "Ahahaha, you say the funniest things."
                pri "I um…"
                scene bg lashleylunchtalk_eyesup_neutral_talk
                pri "A-Again, thank you…"
                scene bg lashleylunchtalk_eyesup_neutral

        "How’s work?"if not lashley_questions_asked_hows_work:
            $ lashley_questions_asked_hows_work = True
            $ lashley_questions_count += 1
            scene bg lashleylunchtalk_eyesup_confused
            pov "And how has work been, if you don’t mind me asking?"
            pov "I’ve always wondered just how tough can be to be an administrator."
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "Oh, I don't mind at all!"
            pri "It can be productive and a handful, but it is rewarding to see young adults on the path to adulthood."
            pri "Doing my best to provide you with a safe environment to learn and then achieve your dreams is the joy of my life!"
            scene bg lashleylunchtalk_eyesup_neutral
            pov "Did you always want to become an administrator?"
            scene bg lashleylunchtalk_eyesup_bored_talk
            pri "No, not really."
            pri "All my life I’ve felt as if I simply didn’t belong anywhere I went."
            pri "I grew up sheltered by my father and the family name."
            pri "Never allowed to play with the other kids growing up, or at all."
            pri "He said I had quite a fragile immune system growing up, so I had to keep myself in a sterile area for the most part, mainly my room and the manor."
            scene bg lashleylunchtalk_eyesdown_sad
            pov "So you were quite sick, as a child?"
            scene bg lashleylunchtalk_eyesup_sad_talk
            pri "Quite so."
            pri "I suffered from high fevers constantly. My body would ache and grow hot, not to mention I would be overcomed with a feeling of anxiety and overall nervousness."
            pri "Sometimes for hours."
            scene bg lashleylunchtalk_eyesdown_sad_talk
            pri "It only got worse as I grew up."
            pri "The fevers grew more intense, sometimes my whole body would feel as if it was burning and I would lose control of my legs, not having the strength to stand up for a few minutes up to an hour."
            scene bg lashleylunchtalk_eyesdown_sad
            pov "That sounds horrible."
            pov "What did you do?"
            scene bg lashleylunchtalk_eyesup_sad_talk
            pri "My father taught me to get through it."
            pri "He would make me take cold baths, before rubbing my body with some medicine that would make me numb, for the most part."
            pri "Afterwards, he would make me fall asleep by reading the Bible to me."
            scene bg lashleylunchtalk_eyesup_bored_talk
            pri "My father taught me the word of the Lord since I was very young."
            pri "He would sit next to my bed and read me his favorite verses. Or I would sit on his lap as he read it in his office, from cover to cover."
            pri "He spent lots of time with me making sure I was safe and teaching me the verses of the Lord."
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "The majority of my most precious childhood memories were with him."
            scene bg lashleylunchtalk_eyesup_neutral
            pov "He sounds like an excellent guy."
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "The best man I’ve ever known."
            pri "He was a pastor for the town for the majority of his life."
            pri "Seeing the way he guided men and women in need was my inspiration."
            pri "Even when it went against his own faith, he would never turn his back from someone in need and he would bravely share his beliefs of free love to anyone around."
            pri "He would even hold secret weddings for gay and lesbian couples back in the day!"
            scene bg lashleylunchtalk_eyesup_neutral
            pov "Wow, seems like a man with quite the story to tell."
            scene bg lashleylunchtalk_eyesup_neutral_talk
            pri "I wish he could see how the world has turned now or if he would officiate a wedding that doesn’t have to be in the shadows anymore."
            scene bg lashleylunchtalk_eyesup_neutral
            ##-If Charisma is 8 or higher-
            if skill_cha >= 3:
                $ skill_cha -= 3
                $ renpy.notify("You used 3 Charisma Points")
                $ renpy.pause(1.0,hard=True)
                ##(+2 Lashley Rp)
                $ add_points("principallashley_points",2)
                scene bg lashleylunchtalk_eyesup_shocked
                pov "I know for a fact he would be proud of the woman you are today."
                scene bg lashleylunchtalk_eyesup_surprised_talk
                pri "Do you really think so?"
                scene bg lashleylunchtalk_eyesup_shocked
                pov "I’m quite sure."
                scene bg lashleylunchtalk_eyesup_neutral
                pov "You made a total stranger in town feel welcome, after all."
                scene bg lashleylunchtalk_eyesup_neutral_talk
                pri "That’s so sweet of you, [povname]."
                scene bg lashleylunchtalk_eyesup_embarrassed_talk
                pri "A-Anyway."
                scene bg lashleylunchtalk_eyesup_neutral_talk
                pri "He inspired me to become a pillar of my community, the same way he was."
                pri "But since his role within the church is reserved for men, I decided to become an educator, and now I’m here."
                scene bg lashleylunchtalk_eyesup_neutral
                pov "That’s quite the story."
                pov "Thank you for sharing it."
                scene bg lashleylunchtalk_eyesup_neutral_talk
                pri "You are one of the few people I’ve ever told this story to."
                pri "I should be the one thanking you for listening."
                scene bg lashleylunchtalk_eyesup_neutral
    ##-Once one of the options has been picked, the scene will follow its path until completion before returning to this menu until all the choices are picked-

    if lashley_questions_count != 3:
        jump ask_lashley_all_questions

    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "I’ve had a really good time talking to you, [povname]."
    pri "You definitely made me enjoy my off time, far more than usual."
    scene bg lashleylunchtalk_eyesup_neutral
    pov "Glad I could help!"
    pov "It was fun for me too."
    scene bg lashleylunchtalk_eyesup_bored_talk
    pri "Still, I feel like I just talked and talked here, I apologize."
    pri "Please, go ahead and tell me something about you."
    pri "It’s not often I get to know a student without consulting their permanent records or having detention or a punishment involved."
    scene bg lashleylunchtalk_eyesup_bored
    pov "Well, there isn’t much to tell, really."
    scene bg lashleylunchtalk_eyesup_bored_talk
    pri "Anything you want to tell me, I’ll listen."
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "I like talking with you, [povname], truly!"
    scene bg lashleylunchtalk_eyesup_neutral
    pov "Well, when you put it like that, I-"
    scene bg lashleylunchtalk_eyesup_shocked
    studf "Director Lashley!"
    scene bg lashleylunchtalk_eyesup_confused
    studf "There are a bunch of boys shoving one of the nerds heads into the toilet!"
    scene bg lashleylunchtalk_eyesup_angry_talk
    pri "AGAIN?!"
    scene bg lashleylunchtalk_eyesup_bored_talk
    pri "Ugh, they are going to get it this time!"
    scene bg lashleylunchtalk_eyesup_sad_talk
    pri "I’m sorry, [povname], but our conversation will have to continue some other time."
    scene bg lashleylunchtalk_eyesup_bored
    pov "It’s no problem, go ahead!"
    scene bg lashleylunchtalk_eyesup_neutral_talk
    pri "Thank you so much for today, I won’t forget it."
    scene bg lashleylunchtalk_no_lashley with fade
    pri "NOW, UNLESS YOU WANT A MONTH PAINTING THE GYM, YOU BOYS BETTER LEAVE IAN ALONE!" with hpunch

    pov "How does she immediately know who they are torturing?"
    studf "Ian is pretty much a bully magnet."
    pov "Poor guy…"
    scene black
    with fade

    $ principallashley_path = 3

    jump lbl_schoolcafeteria_day_setup
