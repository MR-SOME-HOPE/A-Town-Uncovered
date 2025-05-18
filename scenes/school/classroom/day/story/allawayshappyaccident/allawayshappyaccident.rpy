label lbl_allaways_happy_accident:
    #[Classroom, After School– “Allaway’s Happy Accident” – misslashley_path = 27]

    #-Scene takes place on Thursday-

    #-After the class of the day you are called by Allaway to stay behind to help her with something, the reason changes depending on whether or not you have romanced her at this point or not-
    ## SPRITE START
    scene bg chalkboard_day
    with fade
    show mis bored_talk_forward_1
    with dissolve
    mis "Alright class, that’s all for today."
    show mis angry_talk_forward_1
    mis "Make sure to hand in your assignments for grading and be sure that it has a name on it!"
    mis "You guys aren’t in kindergarten anymore and the next paper I see without a name on it is going straight into the trash!"
    show mis shocked_talk
    mis "Oh and I also need one of the guys to stay behind and help me move some stuff into the classroom for an activity I have in mind for you guys tomorrow."
    show mis confused_talk_forward_1
    mis "Any volunteers?"
    show mis smirk_forward_1
    "Class" "…"
    show mis bored_talk_forward_1
    mis "… Anyone at all?"
    show mis bored_forward_1
    "Class" "-Silent muttering-"
    show mis shocked_talk_forward_1
    mis "Alrighty, first random pick of the list it seems!"
    show mis smirk_talk
    mis "Let’s see now…"
    show mis bored_talk
    mis "Eenie, Meenie, Minie, Moe…"
    show mis shocked_talk_forward_1
    mis "Ah, [povname]!"
    show mis smirk_talk_forward_1
    mis "Well, look just how lucky you are!"
    show mis smirk_forward_1
    pov "Aww man…"
    show mis bored_talk_forward_1
    mis "Oh, don’t be such a baby."
    show mis neutral_talk_forward_1
    mis "Everyone else is free to go now, see you all tomorrow!"
    show mis neutral
    "Class" "{i}*relieved muttering*{/i}"

    #-The rest of class leaves the room leaving the Mc and Allaway alone-

    #-The following Dialogue changes depending on whether Allaway has been romanced or not-

    #-If Allaway has been Romanced-
    if missallaway_path >= 24:
        scene bg classroom_dayempty
        with fade
        show pov confused_talk at left
        with dissolve
        show mis smirk at right
        with dissolve
        pov "Alright, when are the supplies coming then?"
        show pov confused at left
        show mis smirk_talk at right
        mis "Oh, first things first, [povname]!"
        show pov confused_talk at left
        show mis smirk at right
        pov "What do you-"

        ## CG START
        #-Mc is interrupted by Allaway who rushes to embrace him tightly-"
        scene bg lasthourofclass_1
        with hpunch
        pov "...!"
        mis "Sigh… That’s much better…"

        pov "Woah, you are quite eager today, aren’t you?"

        mis "Shhhh…"
        mis "Shush that lovely mouth of yours for a second."
        mis "I’m recharging~"

        pov "Had a hard day today?"

        ## SPRITE START
        scene bg classroom_dayempty
        with fade

        show pov embarrassed at left
        show mis sad_talk at right
        mis "More like I’m having a hard week."
        show pov confused at left
        show mis embarrassed_talk at right
        mis "Lashley has been working me like a slave lately!"
        show mis shocked_talk at right
        mis "Seriously, there hasn’t been a day this week so far that I haven’t been flooded with paperwork and other random stuff."
        mis "It’s like she’s funneling all paperwork everyone else doesn’t wanna do into my desk and expects me to have it all done by the next morning!"
        show pov embarrassed at left
        show mis sad_talk at right
        mis "I’m so freaking tired…"
        mis "It’s the reason I haven’t really been available this week to go out with you."
        show pov smirk_talk at left
        show mis sad at right
        pov "Need me to lend a hand?"
        show pov sad_talk at left
        show mis embarrassed at right
        pov "I know it’s not really appropriate for me to help you out with paperwork but still…"
        show pov sad at left
        show mis embarrassed_talk at right
        mis "You are sweet to ask, love."
        show pov embarrassed at left
        show mis neutral_talk at right
        mis "But right now, all I need you to worry about is to wrap those strong arms of yours around me and give me a big tight squeeze, ok?"
        show pov smirk at left
        mis "I just need a boost to help me through the rest of the week."
        show pov smirk_talk at left
        show mis shocked at right
        pov "Well, how about a little extra motivation then?"
        show pov smirk at left
        show mis smirk_talk at right
        mis "As much as I want you to give me a striptease right now, it’s not really the time or the place, honey."
        show pov neutral_talk at left
        show mis smirk at right
        pov "Not what I meant, but I like where your head's at."
        show pov neutral at left
        show mis smirk_talk at right
        mis "You are going to have to rock my world hard once this horrible week is over."
        show pov embarrassed at left
        mis "I’m not even expecting a date here, just come to my place and pamper me till I’m spoiled rotten."
        show pov embarrassed_talk at left
        show mis smirk at right
        pov "You say that as if I don’t already spoil you as much as I can."
        show pov smirk at left
        show mis shocked_talk at right
        mis "And you say that as if you weren’t expecting me to want more."
        show pov neutral at left
        show mis neutral_talk at right
        mis "I’m talking massages, cuddling, kisses, you feeding me stuff and the occassional round or two of hardcore sex."
        show pov shocked at left
        show mis smirk_talk at right
        mis "Also is it too much to ask to do it all with your shirt off and with a little bowtie on?"
        show pov shocked_talk at left
        show mis bored at right
        pov "Wow, you are that stressed out, huh?"
        show pov embarrassed at left
        show mis bored_talk at right
        mis "My back is aching already at the thought of having to sit down and write some more."
        mis "That’s why I called in a few favours and on Friday you guys are gonna watch some documentaries on business and some random stuff in topic with the class I downloaded."
        show pov smirk at left
        show mis embarrassed_talk at right
        mis "I plan on just sitting my pretty little ass down and have you do all the work and learning while I try to relax a bit before I hand over all this paperwork to Lashley."
        mis "Along with a piece of my mind on all this extra work and perhaps a request for a day off next week."
        show pov smirk at left
        show mis shocked_talk at right
        mis "Say, think you can be sly enough to sneak under my desk once the lights are out?"
        show pov smirk_talk at left
        show mis smirk at right
        pov "As tempting as that sounds, you know you can’t keep quiet enough for that to work."
        show mis shocked at right
        pov "Not to mention that face you make when you are close is going to give a dead giveaway."
        show pov shocked at left
        show mis embarrassed_talk at right
        mis "I-I don’t make a face!"
        show pov smirk_talk at left
        show mis embarrassed at right
        pov "Let’s agree to disagree then."
        show pov smirk at left
        show mis embarrassed_talk at right
        mis "Smartass…"
        show pov smirk_talk at left
        show mis embarrassed at right
        pov "I have no problem with your first idea of having me pamper you at your place!"
        show pov neutral_talk at left
        pov "The whole bow tie thing is a little extra, but you deserve it after working so hard."
        show pov neutral at left
        show mis smirk_talk at right
        mis "God, I love you."
        show pov smirk_talk at left
        show mis smirk at right
        pov "I know, I’m quite loveable."
        show pov shocked_talk at left
        show mis confused at right
        pov "Oh, but I’m not available this weekend though."
        show pov embarrassed_talk at left
        pov "Kinda got roped into going to check out Zariah’s new EP and I kinda can’t cancel it."
        show pov embarrassed at left
        show mis shocked_talk at right
        mis "Oh, you are going to Zariah’s party?"
        show pov embarrassed_talk at left
        show mis embarrassed at right
        pov "Yeah, I kinda got in the position where I can’t afford to not go now."
        pov "You know about it?"
        show pov shocked at left
        show mis embarrassed_talk at right
        mis "She invited me but I had to decline since it wouldn’t be appropriate for a teacher to be at a party with her students."
        show pov embarrassed at left
        show mis bored_talk at right
        mis "And besides I was planning on just passing out on my bed naked and watch some old sitcoms for a day or two after I’m done with all this fucking paperwork."
        mis "But besides that, it’s pretty hard not to know about the whole thing seeing as how much it upsets Lashley."
        show pov confused_talk at left
        show mis bored at right
        pov "It upsets her?"
        show pov confused at left
        show mis bored_talk at right
        mis "Ugh, yes…"
        show mis shocked_talk at right
        mis "She has been going on and on about how this sort of “get togethers” only poison the youth and how they should be focused on far more important things like school and their significant others."
        show pov bored at left
        show mis angry_talk at right
        mis "I swear to god, that woman needs to chill the hell out for once."
        mis "What’s so wrong with a party once in a while anyway?"
        show mis confused_talk at right
        mis "It’s not like you guys are snorting cocaine or trying to summon satan or something."
        show pov embarrassed at left
        show mis bored_talk at right
        mis "… Right?"
        show pov shocked_talk at left
        show mis bored at right
        pov "Of course not!"
        show pov shocked at left
        show mis shocked_talk at right
        mis "Good!"
        mis "Because after everything we’ve been through, if I ever find you even remotely close to drugs outside the legal spectrum, I’m not only breaking up with you, I’m also shoving them up your ass."
        show pov shocked_talk at left
        show mis confused at right
        pov "You know what? That’s more than fair enough."
        pov "So, is it okay for me to go?"
        show pov neutral at left
        show mis neutral_talk at right
        mis "Of course, babe!"
        mis "You go and have some fun with your friends and tell me if something fun happened."
        show mis bored_talk at right
        mis "I trust you enough to know the consequences of you having too much fun out there."
        show pov embarrassed at left
        show mis smirk_talk at right
        mis "Be sure to let me know if something funny happens though! I love hearing embarrassing stories of my students."
        show pov embarrassed_talk at left
        show mis neutral at right
        pov "Now you have an inside man to give you all the details."
        show pov neutral at left
        show mis smirk_talk at right
        mis "One of the perks of our kind of relationship, I suppose."
        show pov confused at left
        show mis shocked_talk at right
        mis "Alright, changing topic though, I don’t plan on letting you go anytime soon, so how about you stop talking and pucker up for me?"
        show pov embarrassed at left
        show mis sad_talk at right
        mis "My lips feel rather lonely you know?"
        show pov smirk at left
        show mis smirk_talk at right
        mis "If you are a good boy, I may just let you do some of our type of… “overtime”"
        show pov smirk_talk at left
        show mis smirk at right
        pov "I like the sound of that."
        show pov smirk at left
        show mis neutral_talk at right
        mis "I love you, you know?"
        show pov neutral_talk at left
        show mis neutral at right
        pov "Of course I do, I love you too."
        show pov smirk at left
        show mis neutral_talk at right
        mis "Sigh. You’ll never know how much I enjoy hearing you say that."
        show pov smirk_talk at left
        show mis neutral at right
        pov "I get a good idea from the goosebumps you get when you hear it."
        show pov embarrassed at left
        show mis neutral_talk at right
        mis "Always going for that one final line."
        show pov smirk at left
        show mis smirk_talk at Position(xpos=1300)
        with dissolve
        mis "Alright, no more talking, lip time!"

        #-As Allaway says this, Lashley enters the room-

        show pov neutral at left
        show mis smirk at Position(xpos=1200)
        show pri confused_talk at right
        with dissolve
        pri "Miss Allaway?"
        show pov shocked at left
        show mis shocked at Position(xpos=1200)
        show pri embarrassed_talk at right
        pri "The projector and supplies you wanted are ready for-"

        #-Lashley stops as she looks on at the two of them in jealous shock as Allaway and Mc let go of each other-

        show mis shocked_talk at Position(xpos=1300)
        show pri shocked at right
        mis "D-Director Lashley!"
        mis "I- Um, I-"
        show pov confused at left
        show mis angry_talk at Position(xpos=1500)
        with dissolve
        mis "C-Cockroach!"
        mis "There was a big nasty cockroach!"
        show pov shocked at left
        show mis shocked_talk at Position(xpos=1500)
        mis "Thankfully [povname], managed to kill it."
        mis "Y-You know how bad I am with those kinds of creatures, I kind of panicked and jumped into his arms!"
        show pov shocked_talk at left
        show mis shocked at Position(xpos=1500)
        show pri bored at right
        pov "Y-Yeah!"
        pov "It totally caught me off guard!"
        show pov embarrassed_talk at left
        show mis embarrassed at Position(xpos=1500)
        pov "I couldn’t even see what I was doing but I managed a lucky stomp on it!"
        show pov embarrassed at left
        show mis embarrassed_talk at Position(xpos=1500)
        mis "O-Oh, what a huge relief!"

        #=RESULT END=



    #-If Allaway is Not Romanced-
    elif missallaway_path < 24:
        scene bg classroom_dayempty
        with fade

        show pov confused_talk at left
        show mis bored at right
        pov "Alright, so when are the supplies coming?"
        show pov confused at left
        show mis bored_talk at right
        mis "Should be any time now."
        mis "I asked to borrow the old projector so it takes a bit of setting up to get it working properly, so it’s best to just do it the day before you need it and save time."
        show pov confused_talk at left
        show mis bored at right
        pov "Doesn’t the school have access for newer projectors?"
        show pov smirk at left
        show mis bored_talk at right
        mis "Oh, we definitely have modern projectors but the other teachers have them reserved months in advance for their subjects so the old projector is mainly for out of the blue presentations and stuff."
        mis "It’s a bit of a dinosaur but nothing too terrible."
        show pov smirk_talk at left
        show mis neutral at right
        pov "So this whole thing for friday is just an out of the blue thing?"
        show pov smirk at left
        show mis embarrassed_talk at right
        mis "Sigh. kind of, yeah…"
        mis "You promise not to say anything? I’m only considering telling you since you seem trustworthy enough for it to not come back to bite me in the ass later."
        show pov smirk_talk at left
        show mis smirk at right
        pov "Of course, my lips are sealed. Honest."
        show pov smirk at left
        show mis confused_talk at right
        mis "Well, the truth is that I had other stuff planned for Friday this week and even have my days where I’m going to need one of the good projectors already scheduled ahead."
        show pov confused at left
        show mis shocked_talk at right
        mis "But lately it seems all the paperwork that Director Lashley or other teachers don’t want to do has come to fall on me for some reason!"
        mis "Seriously, it’s like I have a mountain of work just dropped into my lap the moment I finish another stupid report!"
        show pov smirk_talk at left
        show mis smirk at right
        pov "Must be bad if it has you this stressed."
        show pov embarrassed at left
        show mis bored_talk at right
        mis "My back is aching already at the thought of having to sit down and write some more..."
        mis "That’s why I called in a few favours and on Friday you guys are gonna watch some documentaries on business and some random stuff in topic with the class I downloaded."
        show mis embarrassed_talk at right
        mis "Just something for me to take some rest and keep you guys occupied for the duration of the class."
        show pov neutral at left
        show mis sad_talk at right
        mis "I have to deliver the rest of the paperwork on friday as well so I think I earned a bit of a chill day after all that work before turning it all in for Lashley."
        mis "As well as some question as to why my pile of work seemed to increase so much lately."
        show pov neutral_talk at left
        show mis embarrassed at right
        pov "I think that’s more than fair."
        show pov shocked at left
        show mis shocked_talk at right
        mis "Seriously, I haven’t had this much paperwork since my thesis work!"
        mis "I’m even considering finding the help of a student just to help me organize all the papers that need to be delivered on friday!"
        show pov confused_talk at left
        show mis shocked at right
        pov "D-Do you now?"
        show pov confused at left
        show mis neutral_talk at right
        mis "Don’t worry [povname]. You are already helping me out with the setting up of the projector and the supplies for the class, so you are safe from helping me with the paperwork."
        show pov shocked_talk at left
        show mis confused at right
        pov "That’s a relief and all but that only makes me more nervous for this whole thing."
        show pov shocked at left
        show mis smirk_talk at right
        mis "You are going to see more finicky dongles in an electronic device than you have ever thought was possible for a device to even function with it."
        show pov confused at left
        show mis shocked_talk at right
        mis "Not to mention the fact that they each need to be in a specific combination for it to work properly."
        show mis smirk_talk at right
        mis "Otherwise the sound is off or the colors are wrong or the thing doesn’t even work."
        show pov bored_talk at left
        show mis smirk at right
        pov "Fun."
        pov "Can’t wait..."
        show pov embarrassed at left
        show mis smirk_talk at right
        mis "I hope you haven’t made any plans for right after school today."
        show pov embarrassed_talk at left
        show mis smirk at right
        pov "I have no real plans until the weekend, I believe."
        show pov embarrassed at left
        show mis shocked_talk at right
        mis "Oh, I suppose you are going to Zariah’s party then?"
        show pov embarrassed_talk at left
        show mis smirk at right
        pov "Yeah, that’s the plan at least."
        show pov confused_talk at left
        pov "You know about it?"
        show pov confused at left
        show mis embarrassed_talk at right
        mis "She actually invited me to go but I had to decline since I don’t think it would be appropriate for a teacher to be at a party with her students."
        show mis shocked_talk at right
        mis "And besides I was already planning on resting at home with a good book and some sweet tea to let go of all that paperwork related stress."
        show pov shocked at left
        show mis bored_talk at right
        mis "But besides that, it’s pretty hard not to know about the whole thing seeing as how much it upsets Lashley."
        show pov confused_talk at left
        show mis bored at right
        pov "It upsets her?"
        show pov confused at left
        show mis smirk_talk at right
        mis "Oh, quite so I’m afraid."
        show mis confused_talk at right
        mis "She has been going frequent tangents in the teachers lounge about how this sort of “get togethers” only poison the minds of the youth and how they should be focused on far more important things like school and their significant others."
        show mis angry_talk at right
        mis "I swear, she really needs to learn how to relax sometimes."
        mis "What’s so wrong with a party once in a while anyway?"
        show pov embarrassed at left
        show mis shocked_talk at right
        mis "You are young and in the prime age for this sort of thing after all."
        mis "Besides it's not like you guys are snorting cocaine or trying to summon satan or something."
        show pov shocked at left
        show mis confused_talk at right
        mis "… Right?"
        show pov embarrassed_talk at left
        show mis confused at right
        pov "Of course not, Miss."
        pov "Zariah just wants our opinion over her new EP and for us to hang out for a while."
        show pov embarrassed at left
        show mis bored_talk at right
        mis "OK, good."
        mis "Just making sure."
        show pov smirk at left
        show mis smirk_talk at right
        mis "Again, I trust you all to know the consequences of having too much fun, so try not going overboard."
        show pov smirk_talk at left
        show mis neutral at right
        pov "Of course."
        show pov neutral_talk at left
        show mis confused at right
        pov "Hey, not to cut you off or anything but when are those supplies and projector coming in anyway?"
        show pov confused at left
        show mis shocked_talk at right
        mis "Oh, they shouldn’t take long now."
        mis "Help me some space on the back of the classroom for when they arrive."
        show pov neutral_talk at left
        show mis embarrassed at right
        pov "You got it."
        show pov neutral at left
        show mis confused_talk at right
        mis "Do be mindful though, the students in the back tend to be quite messy since they think I don’t see them eating candy mid class, so there is always a chance to find a-"

        #-As Allaway says this, she sees on the floor what she was afraid of seeing-

        show pov shocked at left
        show mis shocked_talk at right
        mis "C-C-C-COCKROACH!"

        #-Allaway jumps into the Mc’s arms and hugs him tight trying to escape the nasty bug-

        show mis angry_talk at Position(xpos=1300)
        with dissolve
        mis "KILL IT!"
        mis "KILL IT! KILL IT! KILL IT! KILL IT! KILL IT! KILL IT!"
        show mis embarrassed_talk at Position(xpos=1300)
        mis "Oh sweet and merciful god, [povname], kill it!"
        mis "I swear to god if that disgusting thing starts flying, I’ll either faint or jump out the damn window!"
        show pov shocked_talk at left
        show mis angry at right
        pov "A-Allaway hang on, I can’t move if you don’t let me-!"
        show pov shocked at left
        show mis angry_talk at Position(xpos=1300)
        mis "Just kill it already, I’ll freaking fail your grade in my class if you let it get on me!"
        show pov angry_talk at left
        show mis shocked at Position(xpos=1300)
        pov "I got it, I got it!"

        #-The mc proceeds to stomp on the wild cockroach after a moment of silence-

        #(perhaps add a “Crunch” sound effect to indicate the Mc stepped on the bug?)

        show pov shocked_talk at left
        with hpunch
        show mis confused at Position(xpos=1300)
        pov "There, got it!"
        show pov shocked at left
        show mis shocked_talk at Position(xpos=1300)
        mis "Oh my god, thank you!"
        show pov embarrassed at left
        show mis angry_talk at Position(xpos=1300)
        mis "I hate those disgusting things!"
        show pov embarrassed_talk at left
        show mis confused at Position(xpos=1300)
        pov "Do you? Never would have guessed with how you just jumped into my arms."
        show pov smirk at left
        show mis shocked_talk at Position(xpos=1300)
        mis "They are gross and icky and I want to see you not panicking if they started to fly at you out of nowhere!"
        show pov smirk_talk at left
        show mis shocked at Position(xpos=1300)
        pov "Ok, fair enough point."
        show pov confused_talk at left
        show mis confused at Position(xpos=1300)
        pov "Think you can let me go now?"
        show pov embarrassed_talk at left
        pov "Anyone could walk in and get the wrong-"

        #-As Mc says this, Lashley enters the room-

        show pov confused at left
        show pri neutral_talk at right
        with dissolve
        pri "Miss Allaway?"
        show pov shocked at left
        show pri smirk_talk at right
        pri "The projector and supplies you wanted are ready for-"

        #-Lashley stops as she looks on at the two of them in jealous shock as Allaway and Mc let go of eachother-

        show mis shocked_talk at Position(xpos=1300)
        show pri shocked at right
        mis "D-Director Lashley!"
        mis "O-Oh my goodness, please don’t get the wrong idea!"
        show pov embarrassed at left
        show mis embarrassed_talk at Position(xpos=1500)
        with dissolve
        show pri confused at right
        mis "T-There was a cockroach!"
        mis "A big nasty cockroach that came out from the back of the classroom!"
        show pov shocked at left
        show mis neutral_talk at Position(xpos=1500)
        mis "Thankfully [povname], managed to kill it."
        show mis embarrassed_talk at Position(xpos=1500)
        show pri bored at right
        mis "You know how bad I am with those kinds of creatures, I kind of panicked and jumped into his arms!"
        show pov embarrassed_talk at left
        show mis embarrassed at Position(xpos=1500)
        pov "Y-Yeah!"
        pov "It totally caught me off guard!"
        pov "I couldn’t even see what I was doing but I managed a lucky stomp on it!"
        show pov embarrassed at left
        show mis shocked_talk at Position(xpos=1500)
        show pri confused at right
        mis "God I hate those nasty things!"

        #=RESULT END=

    #-Back to regular dialogue-

    show mis embarrassed at Position(xpos=1500)
    show pri confused_talk at right
    pri "A… Cockroach, huh?"
    show mis embarrassed_talk at Position(xpos=1500)
    show pri confused at right
    mis "Y-Yes!"
    mis "I almost had a panic attack for a second."
    show mis embarrassed at Position(xpos=1500)
    show pri bored_talk at right
    pri "I see…"
    show pov shocked_talk at left
    show pri bored at right
    pov "Y-Yeah, you should probably call an exterminator or something on the next long weekend we have."
    show pov confused_talk at left
    pov "Isn’t it the season where they start to come out of every corner they are hiding on?"
    show pov confused at left
    show mis angry_talk at Position(xpos=1500)
    show pri confused at right
    mis "Ugh, don’t remind me of that!"
    mis "I’m going to be panicked looking all over the place for them!"
    show pov embarrassed at left
    show mis embarrassed_talk at Position(xpos=1500)
    show pri smirk at right
    mis "I get all jittery and anxious when I think of those things…"
    show mis embarrassed at Position(xpos=1500)
    show pri smirk_talk at right
    pri "Yes… They are quite the pests that need exterminating…"
    show mis embarrassed_talk at Position(xpos=1500)
    show pri bored at right
    mis "Sigh. Anyway, were you saying that the projector and supplies I requested are here already?"
    show pov confused at left
    show mis embarrassed at Position(xpos=1500)
    show pri bored_talk at right
    pri "Yes… The janitor brought them over from storage."
    pri "I’ll let the janitor know you are good for bringing them here."
    show mis embarrassed_talk at Position(xpos=1500)
    show pri confused at right
    mis "U-Um, actually I was hoping if we could get some help from the janitor?"
    mis "You know how the wheels on that old thing no longer budge so it would be easier if-"
    show mis shocked at Position(xpos=1500)
    show pri bored_talk at right
    pri "Oh, I’m terribly sorry."
    pri "The janitor has some more urgent work to do for me on the second floor."
    show pri shocked_talk at right
    pri "We’ll be having an inspection soon by the board of education so we need to start with waxing the floors."
    show pri bored_talk at right
    pri "Plus, now that you tell me we have a cockroach problem, I got to have him contact the exterminator right away to come fix the problem."
    show mis embarrassed_talk at Position(xpos=1500)
    show pri smirk at right
    mis "I-I see, but you know how heavy that thing is and-"
    show pov shocked at left
    show mis shocked at Position(xpos=1500)
    show pri smirk_talk at right
    pri "I’m so sorry, Allaway, but this takes priority."
    show pri embarrassed_talk at right
    pri "We wouldn’t want for the amount of paperwork falling into our desks to triple out of nowhere, now would we?"
    show pov confused at left
    show mis embarrassed_talk at Position(xpos=1500)
    show pri embarrassed at right
    mis "Gulp."
    mis "N-No ma’am!"
    show mis shocked_talk at Position(xpos=1500)
    show pri bored at right
    mis "It’s alright, [povname] and I are more than capable of bringing the projector and supplies along with setting everything up by ourselves!"
    show pov embarrassed at left
    show mis embarrassed at Position(xpos=1500)
    show pri bored_talk at right
    pri "Yes… You and [povname]..."
    pri "I love to hear that…"
    show pov confused at left
    show pri confused_talk at right
    pri "Carry on then, Allaway."
    show pov shocked at left
    show mis confused at Position(xpos=1500)
    show pri bored_talk at right
    pri "And I hope to see you tomorrow morning in my office, Mr. [povname]."
    show pov confused at left
    pri "Something troubling came up that I must speak to you about as soon as possible..."
    show pov confused_talk at left
    show pri bored at right
    pov "Y-Yes, Director Lashley…"

    #-Lashley leaves the room still looking quite pissed-

    show pov confused at left
    show mis embarrassed_talk at Position(xpos=1500)
    hide pri angry at right
    with dissolve
    mis "Sigh."
    mis "Well, our time with this thing just suddenly doubled..."
    show pov confused_talk at left
    show mis sad at right
    with dissolve
    pov "Is it that bad? We just gotta move it back here."
    show pov embarrassed at left
    show mis bored_talk at right
    mis "It’s an old as hell projector from the eighties, [povname]."
    show mis shocked_talk at right
    mis "It weighs probably more than the two of us combined!"
    mis "Plus, the wheels on it haven’t moved since I was a student here, so it’s all just deadweight waiting to fall over."
    show pov bored_talk at left
    show mis bored at right
    pov "Oh boy…"
    show pov bored at left
    show mis embarrassed_talk at right
    mis "Well, let’s try getting it over as soon as possible to start working our heads on the dongle thing, which will likely also take another good chunk of the day…"
    show pov bored_talk at left
    show mis  at right
    pov "Delightful…"
    show pov shocked_talk at left
    show mis confused at right
    pov "Say, before we go though…"
    show pov confused_talk at left
    pov "Did Director Lashley seem odd to you just now?"
    show pov confused at left
    show mis shocked_talk at right
    mis "Definitely, but I guess I can’t really blame her."
    mis "She is probably just stressed out with everything."
    show mis smirk_talk at right
    mis "I mean, there is the whole thing with Zariah’s van and the paperwork I’ve been sending only for her to receive more bad news about the sudden inspection she just mentioned and now the cockroach problem?"
    show mis shocked_talk at right
    mis "let’s just be thankful that she didn’t add in a sermon to all of this and get on our way."
    show pov embarrassed_talk at left
    show mis confused at right
    pov "I guess you are right…"
    show pov embarrassed at left
    show mis shocked_talk at right
    mis "Come on, this is going to take longer the more we stay here."
    show pov smirk at left
    show mis embarrassed_talk at right
    mis "Hopefully there are some other students around to lend us a hand moving it back here."
    show mis smirk_talk at right
    mis "At this point, I’m willing to give extra credit just for helping us move this thing..."
    show pov smirk_talk at left
    show mis embarrassed at right
    pov "Coming!"
    $ principallashley_path = 21.5
    jump lbl_classroom_day_setup
    #=SCENE END=
