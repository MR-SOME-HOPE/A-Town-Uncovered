## Sit With Miss Allaway ##
label lbl_sit_with_miss_allaway:
    default sitwithmissallaway_introvert = 0

    scene bg schoolcafeteria_day
    show btn schoolcafeteria_day_missallaway_idle

    menu:
        "Ask to sit with her":
            show pov neutral_talk at left
            with dissolve
            pov "Hey, Miss Allaway. Mind if I take a seat here with you?"
            show pov neutral at left
            show mis confused at right
            hide btn schoolcafeteria_day_missallaway_idle
            with dissolve
            mis "Uh... are you lost, [povname]?"
            show pov smirk_talk at left
            show mis confused at right
            pov "No?"
            show pov confused at left
            show mis confused at right
            mis "It's just-"
            show mis neutral at right
            show pov neutral at left
            mis "Sure."
        "Go on about your day":
            pov "{i}I'll just leave her be.{/i}"

            jump lbl_schoolcafeteria_day

    scene bg sitwithmissallaway_1
    with fade
    mis "..."
    pov "..."
    mis "..."
    pov "So... What's up?"
    show bg sitwithmissallaway_2
    mis "Are you doing alright, [povname]?"
    mis "Is uh... Jacob and Effie treating you well?"
    show bg sitwithmissallaway_3
    pov "Yeah, definitely. They're great. Why'd you ask?"
    show bg sitwithmissallaway_2
    mis "Well, it's actually quite unusual for um... students to sit with teachers during lunch."
    show bg sitwithmissallaway_4
    pov "I just saw that you were quite lonely eating by yourself."
    show bg sitwithmissallaway_5
    mis "Hehe, I actually like being by myself."
    show bg sitwithmissallaway_6
    mis "I'm what you kids call, introverted."
    show bg sitwithmissallaway_2
    mis "'Hip term' yet I don't believe in categorizing myself in either one side of the spectrum."

    menu:
        "I'd classify myself as an introvert.":
            $ sitwithmissallaway_introvert = 1
            show bg sitwithmissallaway_7
            pov "I'd classify myself as an introvert."
            pov "Don't really like going out much. More of an indoor cat."
            show bg sitwithmissallaway_5
            mis "Really? That's what I find myself doing most weekends but I'm trying to push myself out of the house more."
            mis "I'm way too pale."
            show bg sitwithmissallaway_8
            pov "Haha, ironically, I'm the most tanned one in my family."
            pov "It came from playing a lot of outdoor sports when I was younger."
            show bg sitwithmissallaway_6
            mis "That seems to be very common thing with boys."
            show bg sitwithmissallaway_2
            mis "Especially Japanese boys."
            mis "...Like in those videos... why is it always dark skinned guys with milky-skinned girls."
            show bg sitwithmissallaway_1
            pov "You're not talking about... that..."
        "I'd classify myself as an extrovert.":
            show bg sitwithmissallaway_7
            pov "I'd classify myself as an extrovert."
            pov "I'm always out of the house, give me any reason to leave the house and I will."
            show bg sitwithmissallaway_5
            mis "Really? I've got to REALLY need a strong reason to leave my place. Otherwise I'm literally just walking around aimlessly."
            show bg sitwithmissallaway_4
            pov "Sounds like you're really far along one side of the spectrum."
            show bg sitwithmissallaway_5
            mis "Well, I'm trying to break that habit really. I usually go to the park or the local cafe for a drink and to read."
            show bg sitwithmissallaway_7
            pov "I've never seen you at the Cafe before."
            show bg sitwithmissallaway_9
            mis "I usually go in the morning."
            show bg sitwithmissallaway_6
            mis "The shot of caffeine really makes me feel... tingly all day."
            show bg sitwithmissallaway_3
            pov "Heh.. tingly?"
            mis "Hmm?"
            pov "Like a buzz right."
            show bg sitwithmissallaway_6
            mis "In my panties."
            show bg sitwithmissallaway_1
            pov "Uh-"
        "I don't like labelling myself as one of the other either.":
            show bg sitwithmissallaway_7
            pov "I'm with you, I don't like labelling myself as one of the other."
            show bg sitwithmissallaway_8
            pov "We're all different, neither black or white."
            show bg sitwithmissallaway_6
            mis "Preach it, sister."
            show bg sitwithmissallaway_8
            pov "We can go out and have a good time, but we can also stay in for as long as we want!"
            pov "We deserve the freedom to be who we are and not conform to a mere label."
            show bg sitwithmissallaway_6
            mis "You take the words right out of my mouth."
            show bg sitwithmissallaway_5
            mis "Though if it give you a better insight to me, I like sitting at home, all snugged up in a blanket, reading a book or watching a movie."
            mis "I'm kind of trying to push myself out more often."
            show bg sitwithmissallaway_4
            pov "A balanced lifestyle is probably the healthiest."
            show bg sitwithmissallaway_2
            mis "Yeah, I just find going out during my leisure time a waste."
            mis "Other than the delicious pasties at the cafe and the calming scenery in the park. There's not much for me to do."
            show bg sitwithmissallaway_6
            mis "Plus being naked at home is the best."
            show bg sitwithmissallaway_1
            pov "What did you say?"
    show bg sitwithmissallaway_10
    mis "What?"
    show bg sitwithmissallaway_1
    mis "..."
    show bg sitwithmissallaway_10
    mis "I have no idea what you're talking about."
    show bg sitwithmissallaway_1
    pov "..."
    pov "You do that a lot, don't you?"
    show bg sitwithmissallaway_2
    mis "Hm? Do what? You're really confusing me."
    show bg sitwithmissallaway_3
    pov "Like, you say something really quietly under your breath and you avoid admitting that you just said it."
    show bg sitwithmissallaway_5
    mis "Oh.. really... I-"
    mis "Sorry..."
    show bg sitwithmissallaway_4
    pov "No, no need to be sorry."
    show bg sitwithmissallaway_5
    mis "A few people have mentioned that about me, it's actually quite embarrassing."
    show bg sitwithmissallaway_11
    mis "My brain's thoughts seems to be one step ahead of my mouth."
    show bg sitwithmissallaway_4
    pov "Must be world war 3 going on in that mind of yours."
    show bg sitwithmissallaway_11
    mis "You have no idea how late I sleep because of it."
    show bg sitwithmissallaway_5
    mis "I guess it's another reason for me to have my regular morning expresso."

    menu:
        "We should go out to the cafe together.":
            show bg sitwithmissallaway_3
            pov "We should go out to the cafe together sometime."
        "We should go to the park.":
            show bg sitwithmissallaway_3
            pov "We should go out to the park sometime."
        "We should go watch a movie sometime.":
            show bg sitwithmissallaway_3
            pov "We should go out and watch a movie sometime."
    show bg sitwithmissallaway_2
    mis "You didn't just ask me out, did you?"
    show bg sitwithmissallaway_3
    pov "I mean, just to hang out?"
    show bg sitwithmissallaway_1
    pov "I've nearly graduated, so it wouldn't be THAT weird... would it?"
    show bg sitwithmissallaway_12
    mis "Right now, it's still a little inappropriate."
    show bg sitwithmissallaway_13
    pov "Only a little though, right?"
    show bg sitwithmissallaway_12
    mis "[povname]."
    if whyamiintrouble_leave == 0:
        mis "I told you before, as long as I'm your teacher and you are my student, we will never be more than that."
    else:
        mis "For as long as I'm your teacher and you are my student, we will never be more than that."
    show bg sitwithmissallaway_2
    mis "I don't want to get you in trouble."
    mis "And I most certainly don't want to get myself into trouble."
    mis "I'm the so-called ‘grown-up' here."
    show bg sitwithmissallaway_11
    mis "Do you know how much more trouble I'll get into?"
    show bg sitwithmissallaway_14
    pov "Miss- It- It's just as y'know, friends. Start things pretty casually."
    show bg sitwithmissallaway_15
    mis "Casually?! [povname]. You can't just suggest friends with benefits here."
    show bg sitwithmissallaway_14
    pov "I didn-"
    show bg sitwithmissallaway_12
    mis "Again, I'm flattered, [povname] but it's a straight 'no' from me."
    mis "Don't even try and pursue me or else I'm going to have to make decisions and actions that I don't want to do."
    mis "I know you boys and your games. I've read plenty of teacher-student eroti-"
    show bg sitwithmissallaway_14
    mis "..."
    show bg sitwithmissallaway_12
    mis "Don't. Pursue. Me."
    show bg sitwithmissallaway_13
    pov "..."
    pov "Alright."

    menu:
        "Reverse psychology. I get you.":
            show bg sitwithmissallaway_16
            pov "Reverse psychology. I get you."
            if skill_int >= 3 and skill_cha >= 3:
                if missallaway_points <= 8:
                    $ missallaway_points += 2
                else:
                    $ missallaway_points = 10
                $ skill_int -= 3
                $ skill_cha -= 3
                $ renpy.notify("You used 3 Charisma Points\nYou used 3 Intelligence Points\nYour relationship with Miss Allaway has increased by 2")
                show bg sitwithmissallaway_11
                mis "[povname]... just shush about your psychodelic theories."
                show bg sitwithmissallaway_1
                pov "So you do like me."
                show bg sitwithmissallaway_11
                mis "I-"
                show bg sitwithmissallaway_14
                pov "I knew it."
                pov "Welp, I better leave you to your lunch and let you think about me for the rest of the day."
                show bg sitwithmissallaway_13
                pov "You know what they say, ‘You always want, what you can't have.'"
                show bg sitwithmissallaway_16
                pov "You can have me anytime."
                show bg sitwithmissallaway_15
                mis "[povname]! Get out of here before I give you a month's detention."
            elif skill_int >= 3 or skill_cha >= 3:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                if skill_int >= 3:
                    $ skill_int -= 3
                    $ renpy.notify("You used 3 Intelligence Points\nYour relationship with Miss Allaway has increased")
                elif skill_int >= 3:
                    $ skill_cha -= 3
                    $ renpy.notify("You used 3 Charisma Points\nYour relationship with Miss Allaway has increased")
                show bg sitwithmissallaway_12
                mis "[povname]. You're not listening..."
                show bg sitwithmissallaway_16
                pov "All I heard was that you have a secret crush on me."
                show bg sitwithmissallaway_14
                mis "..."
                show bg sitwithmissallaway_16
                pov "Aha! I knew it."
                show bg sitwithmissallaway_11
                mis "What?! No! I- just... can't even believe what you're saying."
                show bg sitwithmissallaway_10
                mis "Do you hear how silly you sound right now?"
                show bg sitwithmissallaway_3
                pov "Oh, I do. I hear it loud and clear, Miss Allaway. Maybe you should listen to your heart."
                show bg sitwithmissallaway_12
                mis "Ughh.. that was actual gross to hear."
                show bg sitwithmissallaway_13
                pov "Hahaha, I'll be off now. Don't be a stranger, Miss."
                mis "..."
            else:
                if missallaway_points >= 1:
                    $ missallaway_points -= 1
                else:
                    $ missallaway_points = 0
                $ renpy.notify("Your relationship with Miss Allaway has decreased")
                show bg sitwithmissallaway_12
                mis "[povname]. You're really pushing it."
                show bg sitwithmissallaway_13
                pov "Am I tugging on your heart strings."
                show bg sitwithmissallaway_15
                mis "[povname]!"
                show bg sitwithmissallaway_12
                mis "I'm going to be nice and tell you to leave me be or there will be consequences."
                show bg sitwithmissallaway_13
                pov "..."
                pov "Okay, okay... I'm going."
                pov "Sorry. I was just playing around."
                show bg sitwithmissallaway_12
                mis "Don't be an idiot. Have some manners and respect for your teachers."
                show bg sitwithmissallaway_13
                pov "I'm sorry..."
                mis "..."
        "Sorry for trying to connect with you.":
            show bg sitwithmissallaway_1
            pov "Sorry for trying to connect with you, Miss Allaway."
            pov "I didn't mean for you to think that I'm trying to be anything more than..."
            pov "Nevermind."
            pov "I guess I should go, leave you to the rest of your lunch. Sorry."
            mis "..."
    $ missallaway_path = 4

    jump lbl_schoolcafeteria_day_setup
