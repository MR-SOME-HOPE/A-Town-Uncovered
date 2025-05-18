label lbl_lashleys_busy:
    #[Lashley’s Office Second Floor, After School– “Lashley's busy” – misslashley_path = 17]

    #-Once classes are over, the mc heads to Lashley’s office, only to be interrupted by Allaway once you get close to the door-

    show pov shocked at left
    with dissolve
    show mis embarrassed_talk at right
    with dissolve
    mis "Wait, [povname], don’t go into the director's office!"
    show pov confused_talk at left
    show mis embarrassed at right
    pov "What?"
    show pov embarrassed at left
    show mis neutral at right
    pov "Why not?"
    show pov embarrassed at left
    show mis neutral_talk at right
    mis "She requested of us to inform students and any appointment she has to not interrupt her."
    show pov shocked at left
    show mis embarrassed_talk at right
    mis "Apparently she is in the middle of some rather important business."
    show pov embarrassed at left
    show mis confused_talk at right
    mis "She didn’t really specify in the teacher group chat."
    show pov embarrassed_talk at left
    show mis shocked at right
    pov "I see, well, I’m supposed to meet her for my uh… Detention under her, did she say anything about it?"
    show pov shocked at left
    show mis embarrassed_talk at right
    mis "Actually she did."
    show pov shocked at left
    show mis neutral_talk at right
    mis "Told me to let you know you are excused for the day, so I guess you are in the clear."
    show pov confused_talk at left
    show mis neutral at right
    pov "Huh, alright then…"
    show pov neutral at left
    show mis embarrassed_talk at right
    mis "Hope you don’t mind me asking, but what exactly do you do on her sessions?"
    show pov shocked at left
    show mis bored_talk at right
    mis "She always comes up with different tasks for different students, so I can’t help but be curious and ask."
    show pov embarrassed at left
    show mis bored at right
    pov "Uhh… Well, you know-"

    #=The following dialogue changes depending if Allaway is romanced or not. The choice tree is only present if she isn’t romanced=

    #-If Allaway is not Romanced-
    if missallaway_path >= 24:
        show pov embarrassed_talk at left
        show mis shocked at right
        pov "Just the odd task she asks of me around her office."
        show pov neutral_talk at left
        show mis neutral at right
        pov "Usually with some sermon or some other thing to try and teach me a lesson."
        show pov neutral at left
        show mis embarrassed_talk at right
        mis "I can see that happening."
        show pov embarrassed at left
        show mis confused_talk at right
        mis "How are you holding up with her detention then?"
        show pov shocked at left
        show mis bored_talk at right
        mis "I sure hope it’s not interrupting your studies and homework."
        show pov embarrassed_talk at left
        show mis neutral at right
        pov "W-Well, you know me."
        show pov smirk_talk at left
        show mis smirk at right
        pov "I can handle a bit of extra work just fine!"
        show pov smirk at left
        show mis smirk_talk at right
        mis "Is that so?"
        show pov embarrassed_talk at left
        show mis confused_talk at right
        mis "And you are not getting… Distracted?"
        show pov embarrassed_talk at left
        show mis bored at right
        pov "Distracted in what way?"
        show pov confused at left
        show mis bored_talk at right
        mis "Well… It is no secret that whenever students work detention with Lashley, they tend to get… Distracted… Along with daydreaming a lot."
        show pov confused_talk at left
        show mis bored at right
        pov "About?"
        show pov confused at left
        show mis embarrassed_talk at right
        mis "Ummm… You know…"
        show pov shocked_talk at left
        show mis embarrassed at right
        pov "Do I?"
        show pov embarrassed at left
        show mis embarrassed_talk at right
        mis "Well, it is no secret that Lashley is quite an attractive woman."
        show pov confused at left
        mis "not to mention…"
        show pov confused_talk at left
        show mis embarrassed at right
        pov "What?"
        show pov confused at left
        show mis bored_talk at right
        mis "Are you really gonna make me say it?"
        show pov shocked_talk at left
        show mis bored at right
        pov "Huh? Oh!"
        show pov confused_talk at left
        show mis shocked at right
        pov "You are talking about her che-"
        show pov shocked at left
        show mis shocked_talk at right
        mis "Yes!"
        show pov embarrassed at left
        show mis bored_talk at right
        mis "Now don’t say it."
        show pov embarrassed_talk at left
        show mis bored at right
        pov "Uhhh… Well, I don’t know what you want me to tell you there…"
        show pov bored_talk at left
        show mis smirk at right
        pov "I-I mean, it’s not like I haven’t noticed them or anything but…"
        show pov embarrassed_talk at left
        show mis bored at right
        pov "Uhhh…"

        menu:
            "Feign Ignorance and lie":
                #-If “Feign ignorance and lie” was picked-

                show pov embarrassed_talk at left
                show mis confused at right
                pov "I-I’ve really been busy with her errands and tasks to really been paying attention."
                show pov bored_talk at left
                show mis shocked at right
                pov "If I mess up she shoots me back another sermon so I try to focus on what I’m doing, you see?"
                show pov smirk at left
                show mis embarrassed_talk at right
                mis "Is that so?"
                show pov smirk_talk at left
                show mis bored at right
                pov "Y-Yeah! I mean, you know her longer than I do, how often does she give you a sermon when you just have a casual conversation."
                show pov embarrassed at left
                show mis confused_talk at right
                mis "Well, that’s true, but…"
                show pov bored_talk at left
                show mis embarrassed at right
                pov "So I try to avoid it as much as possible by doing a good job."
                show pov embarrassed_talk at left
                show mis embarrassed at right
                pov "Don’t even want to imagine what she would recite me if she caught me staring at her chest or something."
                show pov bored at left
                show mis shocked_talk at right
                mis "It’s not fun, I’ll tell you that much…"
                show pov shocked_talk at left
                show mis bored at right
                pov "Wait, so that means, you-?"
                show pov confused at left
                show mis smirk_talk at right
                mis "I’m human and I get curious too, that’s enough questions out of you mister!"

            "Change the subject to her":
                #-If “Change the subject to her” was picked-
                show pov embarrassed_talk at left
                show mis shocked at right
                pov "B-But I like your figure better!"
                show pov shocked at left
                show mis shocked_talk at right
                mis "W-What?!"
                show pov embarrassed_talk at left
                show mis shocked at right
                pov "Yeah!"
                show pov embarrassed_talk at left
                show mis confused at right
                pov "I think your figure overall is way better."
                show pov smirk_talk at left
                show mis shocked at right
                pov "Consistently good and perfect proportions."
                show pov neutral_talk at left
                show mis embarrassed at right
                pov "10 out of 10!"
                show pov embarrassed at left
                show mis embarrassed_talk at right
                mis "M-May I remind you that I’m your teacher here?!"
                show pov confused at left
                show mis confused_talk at right
                mis "I would much prefer for you to be paying more attention to your books and assignments than my figure!"
                show pov embarrassed at left
                show mis confused_talk at right
                mis "Ummm…"
                show pov shocked at left
                show mis embarrassed_talk at right
                mis "But thank you… I guess?"
                show pov smirk at left
                show mis neutral at right
                mis "Nice to know I can still catch eyes with Director Lashley around..."

                #+1 Allaway Rp.
                $ add_points("missallaway_points",2)
                show pov smirk_talk at left
                show mis shocked at right
                pov "Of course you ca-"
                show pov shocked at left
                show mis angry_talk at right
                mis "Not another word out of you, mister!"
                show pov embarrassed at left
                show mis bored_talk at right
                mis "It’s still not proper for you to be staring at your teacher like that!"


        show pov confused at left
        show mis embarrassed_talk at right
        mis "I-In any case, since you are free and all,  you wouldn’t mind helping me out with some extra work?"
        show pov embarrassed_talk at left
        show mis neutral at right
        pov "U-Ummm…"
        show pov embarrassed at left
        show mis embarrassed_talk at right
        mis "Just some light stuff regarding some grading."
        show pov shocked at left
        show mis neutral_talk at right
        mis "I’ll give you extra credit for helping me out."
        show pov smirk_talk at left
        show mis smirk at right
        pov "Suffice to say that it will be detrimental to said grading for me if I refuse, huh?"
        show pov smirk at left
        show mis smirk_talk at right
        mis "Nice to see we understand each other."
        #=RESULT END (If Allaway is not romanced)=


    #-If Allaway has been Romanced=
    elif missallaway_path >= 24:
        show pov bored_talk at left
        show mis smirk at right
        pov "The random task she needs around the office."
        show pov smirk_talk at left
        show mis neutral at right
        pov "She tries to feed me a sermon in the middle of it, but she usually just gives me the code where to find it in the Bible or something alike."
        show pov bored at left
        show mis neutral_talk at right
        mis "And that's it?"
        show pov bored_talk at left
        show mis bored at right
        pov "Yeah, normally it is."
        show pov smirk_talk at left
        show mis smirk at right
        pov "She does have the odd task here and there but nothing I cannot handle."
        show pov embarrassed_talk at left
        show mis bored at right
        pov "Why do you ask?"
        show pov confused at left
        show mis bored_talk at right
        mis "Just… Curious, I guess."
        show pov embarrassed at left
        show mis smirk_talk at right
        mis "She has been keeping you rather busy, huh?"
        show pov embarrassed_talk at left
        show mis bored at right
        pov "Well, yeah."
        show pov smirk_talk at left
        show mis smirk at right
        pov "What else can you expect from detention work?"
        show pov neutral_talk at left
        pov "At least she doesn’t have me cleaning the bathrooms or painting the school or something, so I guess I can’t really complain."
        show pov embarrassed_talk at left
        show mis smirk at right
        pov "Could be worse if I do, you know?"
        show pov shocked at left
        show mis smirk_talk at right
        mis "And… I expect you to be behaving yourself while you are with her?"
        show pov confused_talk at left
        show mis smirk at right
        pov "Uhh… Yeah?"
        show mis neutral at right
        pov "Why wouldn’t I?"
        show pov bored_talk at left
        pov "I’m already in detention, so I’m not going to start acting like an idiot or talking back to her or something."
        show pov embarrassed_talk at left
        show mis smirk at right
        pov "What’s that going to get me?"
        show pov confused at left
        show mis embarrassed_talk at right
        mis "I-I don’t mean it like that, you bean!"
        show pov confused_talk at left
        show mis neutral at right
        pov "Well, what do you mean to say then?"
        show pov confused at left
        show mis embarrassed_talk at right
        mis "U-Um…"
        mis "I…"
        show pov embarrassed_talk at left
        show mis embarrassed at right
        pov "You know you can tell me anything, Allaway."
        pov "What’s in your mind?"
        show pov confused at left
        show mis embarrassed_talk at right
        mis "W-Well…"
        show pov shocked at left
        show mis confused_talk at right
        mis "Do you promise not to take this the wrong way?"
        show pov embarrassed at left
        show mis bored_talk at right
        mis "Or laugh at me?"
        show pov embarrassed_talk at left
        show mis bored at right
        pov "That tells me that I’m not gonna like what you are going to say."
        show pov confused at left
        show mis confused_talk at right
        mis "A-Are you… Um…"
        show pov shocked at left
        show mis embarrassed_talk at right
        mis "Are you… Trying to get to Lashley’s pants as well?"
        show pov shocked_talk at left
        show mis embarrassed at right
        pov "What?"
        show pov confused at left
        show mis embarrassed_talk at right
        mis "D-Don’t get me wrong!"
        show pov shocked at left
        show mis shocked_talk at right
        mis "I trust you!"
        show pov bored at left
        show mis embarrassed_talk at right
        mis "And it’s not like I am afraid you are trying to bang the whole town or anything-"
        show pov bored_talk at left
        show mis shocked at right
        pov "Oh my god."
        show pov bored at left
        show mis embarrassed at right
        mis "B-But you and I are… Well, you know…"
        show pov shocked at left
        show mis confused_talk at right
        mis "I’m a Teacher and all yet that didn’t stop you from… Courting me and I-"

        #-The Mc smiles as she continues her ramble-

        show pov smirk_talk at left
        show mis confused at right
        pov "Oh my god!"
        show pov neutral at left
        show mis embarrassed_talk at right
        mis "I-I-I can’t help but wonder if you are also aiming for doing something similar with Lashley!"
        show pov embarrassed at left
        show mis sad_talk at right
        mis "I-I mean, she is far prettier than I, not to mention she has that massive pair of ti-"
        show pov smirk_talk at left
        show mis shocked at right
        pov "Oh my god, you are jealous!"
        show pov shocked at left
        show mis angry_talk at right
        mis "Yes, I’m jealous, you dry potato!!"
        show pov embarrassed at left
        show mis bored_talk at right
        mis "MY boyfriend is hanging out with a woman ten times more attractive than me, how do you expect me to-"
        show pov neutral_talk at left
        show mis angry at right
        pov "Allaway!"
        show pov smirk_talk at left
        show mis angry_talk at right
        mis "What?!"
        show pov neutral_talk at left
        show mis angry at right
        pov "I remind you where we are?"
        show pov embarrassed_talk at left
        show mis bored at right
        pov "We are lucky no one really pays attention this time of day, but let’s not blow a fuse in school property, okay?"
        show pov embarrassed at left
        show mis embarrassed_talk at right
        mis "… You are right…"
        show pov neutral at left
        show mis bored_talk at right
        mis "I’m sorry."
        show pov embarrassed_talk at left
        show mis bored at right
        pov "What brought this all on?"
        show pov neutral at left
        show mis embarrassed_talk at right
        mis "W-Well… You were spending so much time with her, I thought…"
        show pov embarrassed_talk at left
        show mis embarrassed at right
        pov "I am serving detention, you know?"
        show pov bored_talk at left
        show mis bored at right
        pov "Not really by choice."
        show pov shocked at left
        show mis angry_talk at right
        mis "I-I know that!"
        show pov embarrassed at left
        show mis bored_talk at right
        mis "It’s just…"
        show pov neutral at left
        show mis angry_talk at right
        mis "Sigh."
        show mis bored_talk at right
        mis "I’m sorry…"
        show pov shocked at left
        show mis embarrassed_talk at right
        mis "I just miss you sometimes and saw how much time you were spending with her and…"
        show pov bored_talk at left
        show mis embarrassed at right
        pov "I understand."
        show pov embarrassed at left
        show mis bored_talk at right
        mis "I-I don't want you to think I'm needy or toxic or anything."
        show pov neutral at left
        show mis embarrassed_talk at right
        mis "I understand you have your own life and our individual positions don't let us be public often…"
        show pov embarrassed at left
        show mis angry_talk at right
        mis "But I still can't help but feel anxious when I see you spending time with another girl..."
        show pov neutral_talk at left
        show mis angry at right
        pov "I know, I know."
        show pov embarrassed_talk at left
        show mis bored at right
        pov "I'll make it up to you, I promise."
        show pov shocked_talk at left
        show mis confused at right
        pov "Actually, you said so yourself, she set me free for the day right?"
        show pov smirk at left
        show mis confused_talk at right
        mis "Right."
        show pov smirk_talk at left
        show mis bored at right
        pov "Well, let’s fix that and spend some time together and get those thoughts out of your head, okay?"
        show pov neutral_talk at left
        show mis confused at right
        pov "How about a movie?"
        show pov smirk_talk at left
        show mis shocked at right
        pov "Just you and me."
        show pov neutral_talk at left
        show mis embarrassed at right
        pov "No Lashley, no nothing."
        show pov embarrassed at left
        show mis embarrassed_talk at right
        mis "I…"
        show pov neutral at left
        mis "I would really like that."
        show pov shocked at left
        show mis sad_talk at right
        mis "But I do have some piled up work grading stuff that I need to do first."
        show pov neutral_talk at left
        show mis shocked at right
        pov "Want me to help so we can go sooner?"
        show pov neutral at left
        show mis shocked_talk at right
        mis "What, were you expecting not to help me out?"
        show pov shocked_talk at left
        show mis neutral at right
        pov "I doubt I had a choice to begin with."
        show pov smirk at left
        show mis neutral_talk at right
        mis "You see?"
        show pov neutral at left
        show mis smirk_talk at right
        mis "That’s why I love you so much!"
        show mis neutral_talk at right
        mis "We always get to understand each other."
        show mis smirk_talk at right
        mis "Communication is the key."
        hide pov neutral
        with dissolve
        hide mis smirk_talk
        with dissolve

        #=RESULT END=

        #=END=

        #-Back to main route-

    #-The Mc And Allaway move out of frame to indicate they are walking away-

    pov "Some people would call it being whipped."

    mis "Call it whatever helps you sleep at night."

    mis "You are still helping me out."

    pov "Yeah, yeah…"

    mis "What was that?"

    pov "Y-Yes, Ma’am!"

    mis "Better~"

    mis "Good boy, now march!"


    #-Allaway and Mc grow silent to indicate they have left but Lashley has a bit of dialogue with her out of frame to indicate she was listening on the other side of the door-
    pri "…"
    pri "O-Oh dear... {i}*hic*{/i}"

    #=SCENE END=
    $ principallashley_path = 13.5

    jump lbl_schoolhallway2_day_setup
