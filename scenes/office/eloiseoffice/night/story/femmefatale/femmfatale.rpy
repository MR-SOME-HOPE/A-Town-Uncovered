label lbl_femme_fatale:
    default asked_eloise_question_ceo = False
    default asked_eloise_question_lashley = False
    default asked_eloise_question_office = False
    #[Eloise’s office, Main Office - “Femme Fatale”  - main_story =99]

    #-Scene follows up the last one with Eloise barging into her office in a now grumpy mood-
    scene bg eloiseoffice_night with fade
    show pov embarrassed at left
    show elo bored_talk at right
    with dissolve
    elo "God, she can be so annoying for a glorified smartphone assistant."
    show elo embarrassed at right
    elo "Sorry about that."
    show pov embarrassed_talk at left
    show elo confused at right
    pov "I have so many questions."
    show pov embarrassed at left
    show elo embarrassed_talk at right
    elo "Which I’ll be happy to answer but let's sit down first, alright?"
    elo "We have been walking for a while."

    #-Eloise and the Mc move to her desk and leans in front of it while the Mc takes the chair closest to her-
    show pov confused at left
    show elo neutral_talk at right
    elo "Alright, fire away."
    elo "What do you want to know about?"

    menu mnu_eloise_questions:
        "You are the CEO?!"if not asked_eloise_question_ceo:
            #-If “You are the CEO?!” was picked-
            show pov shocked_talk at left
            show elo embarrassed at right
            pov "You are the CEO?!"
            show pov shocked at left
            show elo embarrassed_talk at right
            elo "Ah, so you finally figured out what my job in the company is then?"
            show pov smirk_talk at left
            show elo neutral at right
            pov "Well, you are clearly not with HR."
            show pov smirk at left
            show elo smirk_talk at right
            elo "Smart boy~"
            show pov confused_talk at left
            show elo smirk at right
            pov "Why did you tell me you were then?"
            show pov confused at left
            show elo neutral_talk at right
            elo "Oh, but I never say I was or wasn’t with HR now, did I?"
            elo "Although, technically I am a part of it considering the whole department runs under me, don’t you think?"
            show pov smirk_talk at left
            show elo smirk at right
            pov "Isn’t that a technicality?"
            show pov neutral_talk at left
            show elo confused at right
            elo "The corporate world is built upon technicalities, [povname]."
            elo "So, how does it feel to meet the CEO of a large scale company?"
            show pov neutral_talk at left
            show elo confused at right
            pov "Weirdly enough, not the strangest thing that has happened to me recently."
            show pov neutral at left
            show elo smirk_talk at right
            elo "Is that so?"
            show pov smirk_talk at left
            show elo smirk at right
            pov "Long story."
            show pov neutral at left
            show elo smirk_talk at right
            elo "Now you got me all curious though!"
            show pov embarrassed at left
            show elo neutral_talk at right
            elo "But seeing as I’ve been leading you on all night, I’ll answer your questions first."
            elo "Alright, next question!"

            #=RESULT END=

            #=BACK TO CHOICE MENU=
            $ asked_eloise_question_ceo = True


        "You and Lashley."if not asked_eloise_question_lashley:
            #-If “You and Lashley” was picked-
            show pov confused_talk at left
            show elo neutral at right
            pov "So, you and Lashley are…?"
            show pov confused at left
            show elo neutral_talk at right
            elo "She is my sister, yes."
            show pov smirk_talk at left
            show elo embarrassed at right
            pov "Huh, so running things goes in the family then?"
            show pov smirk at left
            show elo embarrassed_talk at right
            elo "Well, considering how my father was a priest and he was a leader in the community, I suppose so."
            show pov neutral at left
            show elo neutral_talk at right
            elo "That’s all I really want to say regarding that."
            show pov confused at left
            show elo bored_talk at right
            elo "I don't like to go into detail about my sister."
            show pov confused_talk at left
            show elo bored at right
            pov "Is there a reason for that or…?"
            show pov confused at left
            show elo embarrassed_talk at right
            elo "She and I… Don't have the best relationship, okay?"
            show elo confused_talk at right
            elo "And that’s saying something considering we have similar relationships with our fathers."
            show pov embarrassed at left
            show elo neutral_talk at right
            elo "So let’s leave it at that for now, okay?"
            elo "I didn’t bring you here to talk about my sister you know?"
            show elo smirk_talk at right
            elo "Truth be told, I was hoping you didn’t find out about it until much later."
            show pov embarrassed_talk at left
            show elo confused at right
            pov "I’m sorry I brought it up then."
            show pov embarrassed at left
            show elo neutral_talk at right
            elo "It’s okay. I guess it’s natural for you to ask immediately after figuring it out."

            #=RESULT END=

            #=BACK TO CHOICE MENU=
            $ asked_eloise_question_lashley = True


        "Why are you letting me into your office?"if not asked_eloise_question_office:
            #-If “Why are you letting me into your office” was picked-
            show pov embarrassed_talk at left
            show elo neutral at right
            pov "Why did you bring me into your office?"
            pov "I mean, you said it yourself that the tour usually ends just outside of your office."
            show pov confused_talk at left
            pov "So why are we here then?"
            show pov confused at left
            show elo neutral_talk at right
            elo "Ah, there is the question of the million bucks!"
            show pov bored at left
            show elo smirk_talk at right
            elo "Why indeed?"
            elo "Why am I going out of the way to get to know you?"
            show elo confused_talk at right
            elo "Why am I taking the trouble to personally take you all over the place and even show you the office no intern has ever seen before?"
            elo "Why am I asking so many questions all of a sudden?"
            show pov confused at left
            show elo neutral_talk at right
            elo "Any guesses, [povname]?"
            show pov bored_talk at left
            show elo embarrassed at right
            pov "Well, you suddenly decided to be cryptic all of a sudden."
            show pov bored at left
            show elo smirk_talk at right
            elo "Maybe I've always been and you just never noticed, who knows?"
            show pov bored_talk at left
            show elo smirk at right
            pov "Well, now I feel uneasy."
            show pov bored at left
            show elo embarrassed_talk at right
            elo "Hehe, don't be."
            elo "I'll reveal everything in just a bit but let's tackle your questions first."

            #=RESULT END=

            #=BACK TO CHOICE MENU=
            $ asked_eloise_question_office = True

    if False in (asked_eloise_question_ceo, asked_eloise_question_lashley, asked_eloise_question_office):
        jump mnu_eloise_questions


    #-Once all options have been exhausted, the scene continues-
    show pov confused_talk at left
    show elo neutral at right
    pov "Well, I think that’s it actually."
    show pov confused at left
    show elo smirk_talk at right
    elo "That’s really all you want to ask after coming this far with me?"
    show pov smirk_talk at left
    show elo shocked at right
    pov "Were you expecting something more?"
    show pov smirk at left
    show elo embarrassed_talk at right
    elo "Maybe, but this will do nicely."
    elo "At least you didn’t ask to go into detail about my father."
    show pov neutral_talk at left
    show elo embarrassed at right
    pov "You said we have similar situations right now regarding father figures and I’ve had enough of old asshat men for the day."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "No offense of course."
    show pov shocked  at left
    show elo smirk_talk at right
    elo "Hah!"
    elo "None taken!"
    show pov confused at left
    show elo neutral_talk at right
    elo "I suppose I can’t blame you for it."
    elo "Alright, I promised to answer what this is all about and I will."
    show pov bored_talk at left
    show elo neutral at right
    pov "Had enough of the mystery woman play then?"
    show pov bored at left
    show elo smirk_talk at right
    elo "Oh hush, let me have my fun."
    elo "But truth be told, I’ve been interested in meeting you for a while, [povname]."
    show pov confused_talk at left
    show elo smirk at right
    pov "In meeting me?"
    show pov confused at left
    show elo neutral_talk at right
    elo "Considering how you are all my sister talks about lately, I can’t help but get a little curious."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "Only good things, I hope."
    show pov confused at left
    show elo smirk_talk at right
    elo "Oh quite so, actually."
    elo "Perhaps… Too much even..."

    #-Eloise stands up from her desk and starts walking back and forth behind the mc while he sits on his chair unsure where to look-
    show elo neutral_talk at right
    elo "Your records, your personality, who you hang out with."
    show pov embarrassed at left
    show elo bored_talk at right
    elo "I mean, she’s had plenty of problem students that she has taken an interest in and I’m sure that your little “disappearing act” must have scared her but sheesh!"
    elo "If I didn’t know better…"

    #-Eloise Leans on his shoulder with a sly smile-
    show pov shocked at left
    show elo smirk_talk at right
    elo "I’d say she has a crush on you~."

    #-If Lashley hasn’t been romanced-
    if not eye2eye_lashleys_lover_chosen:
        show pov embarrassed_talk at left
        show elo smirk at right
        pov "I’m sure that’s not the case."
        pov "Dating a student doesn’t really seem like something she would do just like that, you know?"
        pov "Especially considering the whole relationship with the big man upstairs and her beliefs and all."


    #-If Lashley has been romanced-
    elif eye2eye_lashleys_lover_chosen:
        show pov embarrassed_talk at left
        show elo neutral at right
        pov "I-I’m sure you have read the signals wrong!"
        show pov shocked_talk at left
        show elo smirk at right
        pov "Lashle- "
        pov "I-I mean, Principal Lashley!"
        show pov embarrassed at left
        pov "She is just really attentive towards me due to my situation, you know?"


    show pov embarrassed at left
    show elo smirk_talk at right
    elo "Oh, is that what you think?"

    #-Eloise goes back to walking back and forth behind the Mc-
    show pov confused at left
    show elo neutral_talk at right
    elo "Even if you say that, [povname].  There is nobody in this world who knows my sister better than I do."
    elo "Despite my own wishes to the contrary."
    show elo bored_talk at right
    elo "She tells me everything that goes on in that little head of hers whenever she has a chance and I’ve come to recognize certain signals of hers."
    show pov confused at left
    show elo smirk_talk at right
    elo "For as pure of faith as she claims to be, she has the tendency of letting some very dirty thoughts in her head."
    show elo neutral_talk at right
    elo "I wasn’t planning on doing anything about it since I never thought I would see you face to face and yet here you are."
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "A lost little lamb on the corporate world."
    elo "Who also just so happens to now work on the biggest thorn on my side right now."
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "OK, we are back to the mystery woman act then."
    pov "I assume you are going somewhere with this?"
    show pov bored_talk at left
    pov "And what was that part about you planning to do something?"
    show pov bored at left
    show elo smirk_talk at right
    elo "I’m getting there, [povname]. No reason to get nervous~"

    #-Eloise goes back to leaning against her desk in front of the Mc-
    show pov confused at left
    show elo smirk_talk at right
    elo "You see, [povname]. I have a bit of an issue right now."
    elo "An issue regarding the department you are working at and I need someone I can trust to take care of it."
    show pov smirk_talk at left
    show elo smirk at right
    pov "You are not gonna ask me to mess them up are you?"
    show pov embarrassed_talk at left
    pov "Listen, I like you and all but I’m not gonna go around and mess with people’s lives like that."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "Glad to see you have your priorities straight then."
    show pov confused at left
    elo "But you are in luck, my task for you is the exact opposite, [povname]. I need someone to keep me informed on how I can help them."
    show pov confused_talk at left
    show elo neutral at right
    pov "You want to help them?"
    show pov smirk at left
    show elo neutral_talk at right
    elo "Of course!"
    elo "After all, I’m directly responsible for the creation of the whole department in the first place."
    elo "So it is now my responsibility to make sure they can function optimally."
    show pov confused_talk at left
    show elo neutral at right
    pov "And you need a random intern to help you out with this?"
    show pov smirk_talk at left
    pov "I mean, you are the CEO of the whole place, can’t you just…"
    show pov confused_talk at left
    show elo smirk at right
    pov "I don’t know, do something about it directly or something?"
    show pov confused at left
    show elo smirk_talk at right
    elo "Normally, you’d have a point there."
    elo "I have enough power in this company to do whatever I damn please."
    elo "But I’m afraid things aren’t as simple as that in this particular situation."
    show pov confused_talk at left
    show elo neutral at right
    pov "How come?"
    show pov confused at left
    show elo neutral_talk at right
    elo "Well, long story short. Seeing how our move to the public security market was greatly rushed by the panicking mayor and our board members."
    elo "I knew we would be having a plethora of issues from the customer base as the security system we are installing is still pretty much a prototype."
    show pov bored at left
    show elo smirk_talk at right
    elo "I mean, you guys are pretty much going to be acting as our test subjects for the equipment as we work out the software for a later widespread release."
    show pov bored_talk at left
    show elo smirk at right
    pov "So that’s why it’s a free installation and maintenance…"
    show pov bored at left
    show elo neutral_talk at right
    elo "Yep. Mayor basically wants to run with the narrative that he is doing such a great job with the budget of his campaign that there is enough for him to splurge in improving the town's safety."
    elo "While the surveillance system on the public street does run on us, the trade off to add the 24/7 monitored alarm system for homes came at the cost of you all helping us test the hardware."
    show elo smirk_talk at right
    elo "Along with a few other things the mayor is giving us on the sidelines that I’m not in liberty to say."
    show pov bored_talk at left
    show elo smirk at right
    pov "Huh… Can’t say I’m surprised by all this."
    show pov bored at left
    show elo smirk_talk at right
    elo "Greed is the basis of all business, [povname]."
    elo "The sooner you learn how to make others' greed work in your favor, the sooner you can rise up in the corporate world."
    show pov bored at left
    show elo neutral_talk at right
    elo "Politics and business do tend to go hand in hand after all."
    show pov smirk_talk at left
    show elo neutral at right
    pov "All of this is still legal, right?"
    show pov smirk at left
    show elo neutral_talk at right
    elo "Let’s focus on the topic at hand for now."
    elo "I realized that our own technical support department for our industrial and high end consumers is far too specialized on their respective corners of the market."
    show pov confused at left
    show elo bored_talk at right
    elo "Logistically, it made no sense in both a professional and moral level to allow their respective departments to be flooded with inquiries from this new venture."
    elo "Especially considering how specialized each department is and how new the product is."
    show elo neutral at right
    elo "There's bound to be a lot of calls while we test and improve the system. So the need for a specialized department was more than obvious."
    show pov smirk_talk at left
    show elo neutral at right
    pov "You make the department sound super important yet you guys aren't doing the best job at helping them set up shop."
    show pov smirk at left
    show elo bored_talk at right
    elo "Because someone is making sure that’s the case."
    show pov confused_talk at left
    show elo bored at right
    pov "What do you mean?"
    show pov confused at left
    show elo bored_talk at right
    elo "I’ve been noticing things…"
    show pov shocked at left
    show elo confused_talk  at right
    elo "Things that have been raising a lot of red flags with me that I can no longer afford to ignore."
    show elo angry_talk at right
    elo "Inventory goes missing, certain employees take long breaks during work hours, meetings are held that I’m not aware of…"
    show elo confused_talk at right
    elo "And a certain project I was very much clear over being against it was greenlighted right under my own nose…"
    show elo bored_talk at right
    elo "And now this."
    show pov shocked at left
    show elo confused_talk at right
    elo "Members of the board approving to rush a prototype of an alarm system to be installed all over the town without a more rigorous testing period."
    elo "Only for them to then push all the responsibility of not only getting it working optimally, but also tricking me into making an entire department out of the blue to deal with the issues it's without a doubt going to have."
    show pov embarrassed at left
    show elo sad_talk at right
    elo "Having it fail after landing such a prolific deal for us with the mayor would cause me a lot of problems with the shareholders and board of directors seeing as they were pretty clear they wanted me to keep a close eye on this."
    show pov confused at left
    show elo confused_talk at right
    elo "Do you get what I’m trying to say here, [povname]?"
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "You are being set up…"
    show pov shocked at left
    show elo neutral_talk at right
    elo "Good! Very good!"
    show pov embarrassed at left
    elo "Glad to know there is a brain behind that cute little face of yours."
    elo "Yes, I’m being set up. Quite brazenly too."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "Do you know who it is then?"
    show pov confused at left
    show elo smirk_talk at right
    elo "Nope."
    elo "Whoever’s doing this has done a pretty remarkable job covering their tracks."
    show pov shocked at left
    show elo neutral_talk at right
    elo "But it’s clear to me that the board of directors is somehow supporting it."
    elo "They have been really pushy regarding some projects they want developed that I’m…"
    show pov confused at left
    show elo bored_talk at right
    elo "Not really in favour of."
    elo "Until now, I’ve had a final say on what projects the company as a whole decides to research and develop."
    show elo confused_talk at right
    elo "The particular projects some of the members of the board want to push would not only tarnish our reputation as a company, but it's also such a niche product that there is no way we could see a profit from it."
    show pov confused_talk at left
    show elo bored at right
    pov "What kind of project is it?"
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "Don’t worry about that for now."
    elo "Just know that it is something I am absolutely against for a multitude of reasons."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "Alright… but you still haven’t really told me what you expect me to do about it."
    show pov smirk_talk at left
    pov "I’m just an intern, remember?"
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "Right now, I need someone I can trust."
    show pov confused at left
    show elo bored_talk at right
    elo "I’m not sure if whoever is setting me up is making some sort of power play within the company or just trying to get me fired or demoted or trying to mess with the entire company to make us lose our contracts."
    elo "All I know is that whoever is doing it has several people working for them, so I can’t trust just anyone."
    show pov embarrassed at left
    show elo shocked_talk at right
    elo "Especially anyone with power within the company or who’s been with it a long time."
    elo "And if I’m going to figure out who is trying to get me out of the way, I need to make sure I can still present myself in complete control of everything."
    show elo embarrassed_talk at right
    elo "But in order to do that, I need to make sure I know what’s actually happening within my own company."
    show pov confused_talk at left
    show elo neutral at right
    pov "Which is where I come in?"
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "Exactly."

    #-Eloise gets closer to the Mc, making him lean back into the chair as she invades his personal space-
    show pov confused at left
    show elo smirk_talk at right
    elo "You, [povname], are going to be my little spy~"
    elo "You are going to report to me absolutely everything that happens within your department."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "Conversations, progress reports, status of their equipment."
    elo "Anything and everything you see, you are going to remember to then tell back to me."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "W-Why?"
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "Reconnaissance."
    show pov bored at left
    show elo confused_talk at right
    elo "I need to figure out exactly where it is that the misleading reports I receive from your department are coming from."
    elo "So you are going to work your way up while I work my way down."
    show elo neutral at right
    elo "And once I find the sad piece of human garbage that is lying to me, I can work my way from there to figure out just how many people are involved."
    elo "All with the purpose of finding the people behind all of this and making them regret being born…"

    #-Eloise goes back to leaning against her desk-
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "Simple, isn’t it?"
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "I guess…"
    show pov confused_talk at left
    show elo neutral at right
    pov "But I still don’t get why you decided to trust me with all of this."
    show pov bored at left
    show elo smirk_talk at right
    elo "Oh come on, [povname], it should be obvious by now."
    elo "You just started your first day here and so far you’ve only had contact with people within your own department and me."
    show elo bored_talk at right
    elo "You are a clean slate who hasn’t been corrupted to think any sort of way about me and who wouldn’t catch the attention of those plotting against me."
    show pov confused at left
    show elo smirk_talk at right
    elo "And to top it all off, my sister won’t shut up about you."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "You are the perfect man for the job!"
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "How does that last one fit on all of this?"
    show pov confused at left
    show elo bored_talk at right
    elo "If my sister is vouching for you, that means you have a good enough head on your shoulders that I won’t have to worry about you stabbing me in the back."
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "And it's also is gonna make our little arrangement here all the more sweeter for me~"
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "I-I don’t know…"
    pov "Spying on people isn’t really my style, you know?"
    show pov shocked at left
    show elo smirk_talk at right
    elo "Oh, [povname], please don’t tell me I’ll have to pull the “you don’t really have a choice” card on you."
    show elo neutral_talk at right
    elo "Not when I’m just starting to like you!"
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "U-Um…"
    show pov embarrassed at left
    show elo bored_talk at right
    elo "Look, I need you to understand something here, hun."

    #-Eloise proceeds to straddle the Mc on the chair with a sultry smile in her face-
    show pov confused at left
    show elo smirk_talk at right
    elo "Anything that I want…"
    show pov shocked at left
    elo "I get…"
    show pov confused at left
    show elo neutral_talk at right
    elo "And right now, I want you."
    show pov shocked at left
    show elo bored_talk at right
    elo "I have no qualms of taking what isn’t mine, nor am I asking what it is you want."
    show pov bored at left
    show elo smirk_talk at right
    elo "All that I care about is getting what I want."
    show pov confused at left
    show elo neutral_talk at right
    elo "And I want you to help me."
    elo "Because some people are trying to take the company… MY company… Away from me."
    show pov bored at left
    show elo smirk_talk at right
    elo "And I’m going to make sure those people suffer in as many ways that money can provide me…"
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "E-Eloise, what does that-?"
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "Shhhh~"
    elo "I’m not done talking yet, sweetie~"
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "..."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "I’m giving you the opportunity to help me out of your own volition."
    elo "Something that I can promise you will be very handsomely rewarded."
    elo "And I’m doing it because I like you, [povname]."
    show pov smirk at left
    show elo smirk_talk at right
    elo "I enjoy our time together and I enjoy your company."
    show elo neutral_talk at right
    elo "I want it to continue being a thing for as long as I can."
    elo "But I need you to understand the value of a position you currently are in…"
    show pov shocked at left
    show elo embarrassed_talk at right
    elo "Because I don’t just like you… I also need you."
    show elo neutral_talk at right
    elo "You are currently a piece on the chessboard I’m going to need in order to win this little game I’ve been thrust into right now..."
    show pov embarrassed at left
    show elo confused_talk at right
    elo "And that means that as of right now, I can’t afford to lose you."
    show elo shocked_talk at right
    elo "Could I replace you?"
    show pov sad at left
    show elo bored_talk at right
    elo "Sure, with time. Time that I do not have."
    elo "Do I want to have to do such a thing?"
    show elo neutral_talk at right
    elo "No, I really really don’t. And I know it won’t have to come to that."
    show pov embarrassed_talk at left
    show elo shocked at right
    pov "H-How are you so sure?"
    show pov confused at left
    show elo smirk_talk at right
    elo "Because I know you are a smart boy, [povname]."
    elo "One who knows best when to take an opportunity handed to you on a silver platter."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "One who I plan to make sure that he knows how much I appreciate his help~"
    elo "One who understands that I’m not in the position to accept a no for an answer..."

    #-Eloise leans closer to the Mc-
    show pov shocked at left
    show elo smirk_talk at Position(xpos=1200) with dissolve
    elo "I can make your life very easy if you just let me, [povname]~"
    elo "What’s it going to be?"
    show pov shocked_talk at left
    show elo smirk at Position(xpos=1200)
    pov "I…"
    show pov embarrassed_talk at left
    pov "I don’t really have a choice here, do I?"
    show pov embarrassed at left
    show elo embarrassed_talk at Position(xpos=1200)
    elo "There is always a choice, [povname]."
    show elo smirk_talk at Position(xpos=1200)
    elo "But in this case, can you afford to make the wrong one?"
    show pov embarrassed_talk at left
    show elo confused at Position(xpos=1200)
    pov "…"
    pov "If…"
    pov "If whoever is trying to mess with you gets their way…"
    show pov confused_talk at left
    show elo smirk at Position(xpos=1200)
    pov "What would happen to the people in the department?"
    show pov smirk at left
    show elo neutral_talk at Position(xpos=1200)
    elo "Well, seeing as HR deliberately chose people who were underperforming in their respective departments…"
    elo "it’s a 50/50 on whether they would be integrated to another department or…"
    show pov embarrassed at left
    show elo bored_talk at Position(xpos=1200)
    elo "Downright fired…"
    show pov confused_talk at left
    show elo neutral at Position(xpos=1200)
    pov "And what would happen to you?"
    show pov confused at left
    show elo bored_talk at Position(xpos=1200)
    elo "I would pretty much lose a lot of power within the company and likely continue to be made the person to keep taking the fall whenever projects don’t go according to plan by the board of directors."
    elo "At least, that would be the case if they were smart."
    show pov shocked at left
    show elo embarrassed_talk at Position(xpos=1200)
    elo "Most likely they would immediately vote to get rid of me as soon as they feel they have the leverage with the shareholders."
    show pov embarrassed_talk at left
    show elo embarrassed at Position(xpos=1200)
    pov "They really don’t like you, huh?"
    show pov embarrassed at left
    show elo bored_talk at Position(xpos=1200)
    elo "Some men just can’t handle seeing a woman being on top of things."
    show pov shocked at left
    show elo neutral_talk at Position(xpos=1200)
    elo "You are handling rather well though, I like that~"
    elo "So, what do you say?"
    show pov embarrassed at left
    show elo neutral at Position(xpos=1200)
    pov ".."
    show pov bored_talk at left
    show elo shocked at Position(xpos=1200)
    pov "I’ll do it."
    show pov embarrassed_talk at left
    pov "But know that it was the last few things that I asked what really sold it to me."
    show pov bored_talk at left
    pov "I don’t want anyone losing their jobs and it’s clear this whole place is important to you."
    show pov neutral_talk at left
    pov "So I’ll do it because of that."

    #-Eloise’s smile grows-
    show elo smirk_talk at Position(xpos=1200)
    elo "You keep making a better and better impression on me."
    show pov embarrassed at left
    show elo neutral_talk at Position(xpos=1200)
    elo "That was the smart choice."

    #-Eloise proceeds to stand back up and lean back against her desk-
    show elo confused_talk at right with dissolve
    elo "And I’ll keep in mind I don’t need to do the whole “I Own You” routine with you."
    show pov smirk at left
    show elo embarrassed_talk at right
    elo "Sorry about that, I just needed to make sure you understood how serious I am regarding this."
    show pov neutral_talk at left
    show elo embarrassed at right
    pov "That’s okay, though I certainly didn’t expect it."
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "Though I can tell you aren’t that much against it seeing how I could clearly feel something going hard against my thigh~"
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "O-Oh, I..."
    pov "W-Well, that was…"
    show pov confused_talk at left
    pov "U-Umm..."
    show pov confused at left
    show elo smirk_talk at right
    elo "Hehehe, relax perv, I’m just messing with you."
    show pov shocked at left
    show elo neutral_talk at right
    elo "Besides, I already know what you are packing down there, remember?"
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "Maybe if you play your cards right I can do something about it~"
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "I’ll… Hold you up on that one…"
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "At least you know now I like to be on top~"
    show pov smirk_talk at left
    show elo smirk at right
    pov "That much is obvious now, yeah."
    show pov shocked at left
    show elo smirk_talk at right
    elo "Well, then let’s shake on it."
    show pov embarrassed at left
    elo "I’m very much looking forward to working with you, [povname]."
    show pov neutral_talk at left
    show elo smirk at right
    pov "So am I, Eloise."

    #-The Mc and Eloise shake hands with smiles on their faces-
    show pov neutral at left
    show elo neutral_talk at right
    elo "Good!"
    show pov embarrassed at left
    show elo shocked_talk at right
    elo "Now, it’s very late so let’s get you home."
    show elo neutral_talk at right
    elo "You could probably use a cold shower after all of this."
    show pov embarrassed_talk at left
    show elo embarrassed at right
    pov "I just hope I get there before you know who does."
    show pov neutral at left
    show elo smirk_talk at right
    elo "Trust me, with the amount of work he has yet to do, you have nothing to worry about."
    elo "Now come on, I’ll drive you."
    show pov smirk_talk at left
    show elo shocked at right
    pov "Gonna assume you don’t usually let interns near your car?"
    show pov shocked at left
    show elo smirk_talk at right
    elo "Well, you just became my favorite intern so you get a pass."
    show pov confused at left
    show elo shocked_talk at right
    elo "Oh, by the way give me your phone number."
    show pov smirk at left
    show elo embarrassed_talk at right
    elo "I’m going to need a way to stay in touch with you off the record after all."
    show pov neutral_talk at left
    show elo embarrassed at right
    pov "Sure thing, I assumed you already had it though, considering you have my file."
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "I do, but it feels less stalkery if I at least pretend not to have it and just ask for it."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "Heh, fair enough."

    #-Fade to black to indicate passage of time-
    scene black with fade
    $ renpy.pause()
    "Outside..."

    $ townmap_enabled = 1
    $ gtime = 3
    $ main_story = 99

    scene bg officeoutside_night
    with fade
    
    jump lbl_officeoutside_night
    #=SCENE END=
    #$ renpy.pause()
    #"Game will end here for now."

    #$ MainMenu(confirm=False)() #TEMP
