## Allaway's Call
label lbl_allaways_call:
    ###scene bg allawaycall_temp1
    ##scene bg allawaycall_1
    scene bg allawaycall_1_confused_talk
    with fade
    pov "{i}What a mess has this whole place turned into...{/i}"
    scene bg allawaycall_1_shocked
    "{i}*Riiiiingggtoneeee*{/i}"
    scene bg allawaycall_1_angry_talk
    pov "...Who the heck-?"
    scene bg allawaycall_1_bored
    pov "..."
    ###show bg allawaycall_temp2
    ##show bg allawaycall_2
    scene bg allawaycall_2_sad_talk with dissolve
    pov "H-Hello?"
    ##$ missallaway_path = 17#TEMP TEST
    if missallaway_path >= 24:
        scene bg allawaycall_2_shocked with hpunch
        mis "{i}YOU ABSOLUTE FUCKING BASTARD!{/i}" with vpunch
        scene bg allawaycall_2_shocked_talk
        pov "Sweet Jesus!"
        scene bg allawaycall_2_embarrassed
        mis "{i}YOU HAVE FIVE SECONDS TO EXPLAIN WHERE THE HELL HAVE YOU BEEN ALL DAY BEFORE I FREAKING LOSE IT!{/i}" with vpunch
        scene bg allawaycall_2_confused_talk
        pov "M-Miss Allaway?"
        pov "I-I am at home, what's wrong?"
        pov "Why are you yelling at me?"
        scene bg allawaycall_2_confused
        mis "{i}WHAT’S WRONG? WHAT’S WRONG?! I’LL TELL YOU WHAT THE FUCK IS WRONG!{/i}" with vpunch
        mis "{i}I HAVE SPENT ALL DAY WORRIEDLY CALLING AND TEXTING YOU EVER SINCE I FOUND OUT TWO PEOPLE GOT FUCKING KIDNAPPED AND AFTER BEING IGNORED ALL DAY-{/i}" with vpunch
        mis "{i}THE SON OF A BITCH DARES TO ASK WHAT THE HELL IS WRONG WITH ME!{/i}" with vpunch
        mis "{i}SO, I DON’T KNOW, WHY THE FUCK DO YOU THINK I AM YELLING AT YOU?!{/i}" with vpunch
        scene bg allawaycall_2_sad_talk
        pov "Jeez, I did not expect to see this side of you for a very long time."
        pov "I get your point. I am sorry I made you worry."
        scene bg allawaycall_2_confused
        mis "{i}SORRY ISN’T GOING TO CUT IT FOR HAVING ME PANICKING FOR THE WHOLE DAY!{/i}" with vpunch
        mis "{i}WHERE THE HELL HAVE YOU BEEN AND WHY HAVEN’T YOU CALLED ME?!{/i}" with vpunch
        scene bg allawaycall_2_embarrassed_talk
        pov "Okay, I’ll explain everything to you. But please calm down!"
        scene bg allawaycall_2_embarrassed
        mis "{i}DON’T YOU KNOW YOU NEVER TELL A WOMAN TO CALM DOWN AFTER YOU MESS UP THIS BAD?!{/i}" with vpunch
        scene bg allawaycall_2_embarrassed_talk
        if winc == 1:
            pov "Right!"
            pov "I am sorry."
            pov "Look, I was walking to uni, when I stumbled upon the rest of the guys and we kept walking until we saw all the commotion."
            pov "A few minutes later and my mom is blasting my phone telling me to come home and once I get there she almost fainted from stress."
            scene bg allawaycall_2_sad_talk
            pov "My sister and I have spent the entire day helping her rest and calming each other out."
            pov "I just got to my room after my sister fell asleep as well and I just now checked my phone."
            scene bg allawaycall_2_sad
            mis "{i}And it didn’t occur to you to call your girlfriend the second you got home?!{/i}"
            scene bg allawaycall_2_shocked_talk
            pov "My Mom almost put me in a choke hold with how hard she was hugging me. Not to mention how bad she got once the stress got to her."
            scene bg allawaycall_2_sad_talk
            pov "As much as I wanted to call you, I couldn’t just ask for five minutes and leave my mom alone."
            scene bg allawaycall_2_confused
            mis "{i}W-Well, what about your sister?!{/i}"
            mis "{i}I am sure she could have bought you some time for you to tell me you were alright!{/i}"
            scene bg allawaycall_2_embarrassed_talk
            pov "She is just as stressed as my mom is, Allaway."
            pov "The only reason she didn’t collapsed as well was because mom beat her to the punch and her focus went to her well being."
            pov "I couldn’t just leave her alone with her thoughts, and let her panic as well."
        else:
            pov "Right!"
            pov "I am sorry."
            pov "Look, I was walking to uni, when I stumbled upon the rest of the guys and we kept walking until we saw all the commotion."
            pov "A few minutes later and my [povmumrole] is blasting my phone telling me to come home and once I get there she almost fainted from stress."
            scene bg allawaycall_2_sad_talk
            pov "[sister] and I have spent the entire day helping her rest and calming each other out."
            pov "I just got to my room after my [sisrole] fell asleep as well and I just now checked my phone."
            scene bg allawaycall_2_sad
            mis "{i}And it didn’t occur to you to call your girlfriend the second you got home?!{/i}"
            scene bg allawaycall_2_shocked_talk
            pov "My [povmumrole] almost put me in a choke hold with how hard she was hugging me. Not to mention how bad she got once the stress got to her."
            scene bg allawaycall_2_sad_talk
            pov "As much as I wanted to call you, I couldn’t just ask for five minutes and leave my [povmumrole] alone."
            scene bg allawaycall_2_confused
            mis "{i}W-Well, what about your [sisrole]?!{/i}"
            mis "{i}I am sure she could have bought you some time for you to tell me you were alright!{/i}"
            scene bg allawaycall_2_embarrassed_talk
            pov "She is just as stressed as my [povmumrole] is, Allaway."
            pov "The only reason she didn’t collapsed as well was because my [povmumrole] beat her to the punch and her focus went to her well being."
            pov "I couldn’t just leave her alone with her thoughts, and let her panic as well."
        scene bg allawaycall_2_sad
        mis "{i}W-Well.{/i}"
        mis "{i}B-But I-{/i}"
        mis "{i}Ugh, it’s so unfair!{/i}"
        mis "{i}I was ready to rip you open a new asshole and yell at you for about three hours!{/i}"
        scene bg allawaycall_2_smirk
        mis "{i}I had even made a script with everything I wanted to say!{/i}"
        mis "{i}Why is it so hard for me to stay mad at you?!{/i}"
        scene bg allawaycall_2_smirk_talk
        pov "Hehe, I guess that’s one of my charms."
        scene bg allawaycall_2_smirk
        mis "{i}Oh, quite the modest one, aren’t you?{/i}"
        scene bg allawaycall_2_smirk_talk
        pov "You knew what you were getting into when we started dating, too late to back off now, cause I am never letting you go."
        scene bg allawaycall_2_neutral
        mis "{i}As sweet as that is, don’t think for a second I am still not angry with you.{/i}"
        scene bg allawaycall_2_neutral_talk
        pov "I assumed as much."
        pov "Don’t worry, I am alright."
        scene bg allawaycall_2_smirk
        mis "{i}You know I can’t not worry about you.{/i}"
        mis "{i}I am in love with you, it’s my job to watch your back.{/i}"
        scene bg allawaycall_2_neutral_talk
        pov "And I thank you for that but I remind you it goes both ways."
        scene bg allawaycall_2_bored_talk with dissolve
        pov "How are you holding up? Are you alright?"
        scene bg allawaycall_2_bored
        mis "{i}Got an appointment to have all my locks changed; bought online, some pepper spray meant to be used in case of wild brown bear attacks - that may or may not be illegal to use on humans; signed up for a self defense class.{/i}"
        mis "{i}You know, the usual scared-shitless behaviour one has, after one of these things happens in your neighborhood.{/i}"
        scene bg allawaycall_2_sad_talk
        pov "You have my number on speed dial, right?"
        pov "Anything happens, and I’ll come running to save you."
        scene bg allawaycall_2_sad
        mis "{i}I know.{/i}"
        mis "{i}But do try to keep yourself out of trouble.{/i}"
        mis "{i}It almost seems to gravitate around you.{/i}"
        scene bg allawaycall_2_sad_talk
        pov "I’ll try."
        scene bg allawaycall_2_neutral_talk
        pov "What else did you do today?"
        scene bg allawaycall_2_neutral
        mis "{i}Ugh, we had a stupidly long meeting, where Lashley was basically mid religious breakdown. While the police gave us information to keep you guys from panicking.{/i}"
        mis "{i}I swear, as much as I appreciate the sentiment, if I hear one more prayer today I am going to lose it!{/i}"
        scene bg allawaycall_2_confused_talk
        pov "Was it really that bad?"
        scene bg allawaycall_2_embarrassed
        mis "{i}Well, the fact that I was also dying to find out if my boyfriend was okay; only for him to ignore me for three hours didn’t exactly helped my mood, you know?!{/i}"
        scene bg allawaycall_2_embarrassed_talk
        pov "Ehehe…"
        scene bg allawaycall_2_sad_talk
        pov "I’ll make it up to you, I promise."
        scene bg allawaycall_2_neutral
        mis "{i}Yeah, you better!{/i}"
        scene bg allawaycall_2_sad
        mis "{i}…{/i}"
        mis "{i}I don’t know what I would do if something happened to you.{/i}"
        mis "{i}Please be safe.{/i}"
        mis "{i}I know you don’t need a chaperon and I am supposed to act like your girlfriend, not your mother but…{/i}"
        mis "{i}Could you keep me posted of how you are doing from time to time?{/i}"
        mis "{i}I just need to know you are safe and I know you can’t come over, despite how much I want you to.{/i}"
        scene bg allawaycall_2_sad_talk
        pov "You got it, I understand."
        pov "It’s the least I could do."
        scene bg allawaycall_2_neutral
        mis "{i}Thank you, [povname].{/i}"
        mis "{i}Just knowing you are doing okay, lifts a huge weight off my shoulders.{/i}"
        scene bg allawaycall_2_neutral_talk
        pov "It’s alright. I do it out of love, after all."
        scene bg allawaycall_2_confused_talk
        pov "So what was the meeting about?"
        scene bg allawaycall_2_confused
        mis "{i}Mostly the police calming us down so we can calm you guys down if you are afraid.{/i}"
        mis "{i}The university is going to have an assembly tomorrow meant to give you vague information of what’s going on and keep you safe.{/i}"
        mis "{i}It is mandatory, so please make sure to not miss it, alright?{/i}"
        scene bg allawaycall_2_sad_talk
        pov "I don’t know…"
        pov "Sounds like a drag."
        scene bg allawaycall_2_shocked
        mis "{i}I will slap you.{/i}"
        scene bg allawaycall_2_shocked_talk
        pov "Hehehe, alright, alright."
        pov "I’ll be there, I promise."
        scene bg allawaycall_2_shocked
        mis "{i}Good boy.{/i}"
        scene bg allawaycall_2_smirk_talk
        pov "Do I get a reward from my girl?"
        scene bg allawaycall_2_shocked
        mis "{i}Yes, you get to walk away, still breathing, after scaring me half to death!{/i}"
        scene bg allawaycall_2_smirk_talk
        pov "I’ll take what I can get."
        scene bg allawaycall_2_smirk
        mis "{i}Good.{/i}"
        scene bg allawaycall_2_confused
        mis "{i}Now, as much as I want to stay and keep talking, I am afraid I’m going to have to hang up now.{/i}"
        scene bg allawaycall_2_confused_talk
        pov "That’s new."
        scene bg allawaycall_2_sad_talk
        pov "Usually we speak for way longer. Everything okay?"
        scene bg allawaycall_2_sad
        mis "{i}Yeah, but I should have been contacting everyone else in the classroom to check how they were doing, and inform them of the mandatory assembly tomorrow.{/i}"
        scene bg allawaycall_2_sad_talk
        pov "And you haven’t been doing it?"
        scene bg allawaycall_2_sad
        mis "{i}I was really worried, okay?!{/i}"
        mis "{i}I spent hours trying to reach you so now I have to call everyone else, don’t judge me for having my priorities!{/i}"
        scene bg allawaycall_2_smirk_talk
        pov "Hehehe, it flatters me that I am so high on the list."
        scene bg allawaycall_2_neutral_talk
        pov "But do get to work, Allaway."
        scene bg allawaycall_2_neutral
        mis "{i}Yeah, yeah…{/i}"
        mis "{i}…{/i}"
        mis "{i}Can I call you once I am finished?{/i}"
        scene bg allawaycall_2_neutral_talk
        pov "I’ll stay up all night if I have to."
        scene bg allawaycall_2_neutral
        mis "{i}I love you so damn much.{/i}"
        mis "{i}I’ll try to finish as soon as I can.{/i}"
        mis "{i}I love you!{/i}"
        scene bg allawaycall_2_neutral_talk
        pov "I love you too."
        pov "See you later, Allaway."
        scene bg allawaycall_2_neutral
        mis "{i}See you later, [povname].{/i}"

    elif missallaway_path >= 18:
        scene bg allawaycall_2_shocked
        mis "[povname]!"
        mis "A-Are you alright?!"
        mis "Did you get home safe?!"
        mis "Where are you right now?!"
        scene bg allawaycall_2_shocked_talk
        pov "W-Woah there!"
        pov "Miss Allaway, hi!"
        scene bg allawaycall_2_confused_talk
        pov "Yeah, I got home safe, after seeing the whole thing. "
        pov "I am currently in my room right now."
        pov "Is everything okay?"
        scene bg allawaycall_2_confused
        mis "Y-Yeah, sorry about that."
        mis "I’ve just really been on edge lately thanks to the whole kidnapping thing."
        scene bg allawaycall_2_sad_talk
        pov "I can’t blame you. The whole town is in a panic, after all."
        pov "But what about you?"
        pov "Are you safe?"
        scene bg allawaycall_2_sad
        mis "Yeah. I just got home after Director Lashley had all the teachers over for an emergency meeting regarding the recent kidnapping."
        mis "She was going wild with worry."
        mis "I swear, had officer Mina not been there to give us the rundown of the events and calm her down; Lashley would have forced us all to convert in that room, with how much she was praying for everyone’s safety."
        scene bg allawaycall_2_confused_talk
        pov "Well, everyone has their own way to deal with stress, I guess."
        scene bg allawaycall_2_confused
        mis "By the time she reached her sixth or seventh prayer, I was wondering if she was praying for us or performing an exorcism."
        mis "Still, I appreciate the sentiment."
        mis "You can never go with too much protection after something like this happens. So if whatever higher-being is willing to keep an eye on me -as long as Lashley gives them prayers- I am all for it."
        scene bg allawaycall_2_neutral_talk
        pov "You never know when you might need some divine intervention to save your ass."
        scene bg allawaycall_2_neutral
        mis "Speaking of saving your ass."
        mis "Tomorrow we are going to have the first hour booked by an assembly in the gymnasium."
        mis "You’ll leave your things in the classroom and we’ll head to the gym, once everyone arrives."
        scene bg allawaycall_2_confused_talk
        pov "What’s the assembly about?"
        scene bg allawaycall_2_confused
        mis "From what I understand, the main event will be the police addressing the whole thing and preventing you kids from panicking."
        mis "Along that they may give out some safety pamphlets and other stuff like that."
        mis "Run-of-the-mill stuff to make it seem like they have everything under control."
        scene bg allawaycall_2_confused_talk
        pov "Do they have everything under control?"
        scene bg allawaycall_2_confused
        mis "I don’t know, [povname]."
        mis "Regardless if they do or not, you can bet I’ll keep my doors and windows locked at all times and 911 on speed dial."
        scene bg allawaycall_2_neutral_talk
        pov "Smartest thing I’ve heard all day."
        scene bg allawaycall_2_neutral
        mis "At least this whole thing has given me free time away from Jack."
        scene bg allawaycall_2_angry with dissolve
        mis "The guy is laying low, with all the police snooping over the whole town."
        mis "He gets caught “working” and he’ll find himself in the top suspect list."
        mis "And I doubt Officer Mina wouldn’t take a shot at handcuffing him for good, given the chance."
        scene bg allawaycall_2_angry_talk
        pov "Maybe if we are lucky, they catch him with something by the time they figure out who is behind the kidnapping - and we kill two birds with one stone."
        scene bg allawaycall_2_smirk
        mis "One can only hope…"
        scene bg allawaycall_2_neutral
        mis "Anyway, I am so glad you are safe, and just hearing your voice helped me calmed down a whole lot."
        scene bg allawaycall_2_confused_talk
        pov "Sounds like you are about to say goodbye."
        mis "Ugh, I have to."
        scene bg allawaycall_2_shocked
        mis "I am sorry. As much as I want to talk to you, I have to call the rest of the class to let them know of the assembly -since its mandatory- and missing it will come with a sizeable punishment."
        mis "Director Lashley doesn’t take safety lightly."
        scene bg allawaycall_2_shocked_talk
        pov "I understand."
        scene bg allawaycall_2_neutral_talk
        pov "Thanks for calling, Allaway."
        scene bg allawaycall_2_neutral
        mis "I am just so glad you are safe, [povname]."
        mis "Maybe if I manage to finish early, I could call you again?"
        mis "I honestly just need a friendly voice right now, or else I may not sleep tonight."
        scene bg allawaycall_2_neutral_talk
        pov "I would like that, sure!"
        pov "Send me a text once you are finished, just in case I fell asleep."
        scene bg allawaycall_2_neutral
        mis "Sounds good. "
        mis "Thanks again, [povname]."
        scene bg allawaycall_2_neutral_talk
        pov "For you, anything."
        pov "See you later!"
        scene bg allawaycall_2_neutral
        mis "See ya!"

    else:
        scene bg allawaycall_2_confused
        mis "Hello, [povname], this is your teacher Miss Allaway. Do you have some time to talk?"
        scene bg allawaycall_2_confused_talk
        pov "Uh, yeah…"
        pov "Sure. I am sorry, I just wasn’t expecting my teacher to call."
        scene bg allawaycall_2_confused
        mis "I hope I\'m not disturbing you or anything."
        mis "I can call later, if you need?"
        scene bg allawaycall_2_embarrassed_talk
        pov "N-No, it’s alright."
        pov "I was just getting to my room after uh… working out."
        pov "It’s been a crazy day, so I was hoping to have some rest - but I can spare a few minutes."
        scene bg allawaycall_2_confused
        mis "I completely understand."
        mis "Things have been hectic, and you kids need to rest before you are all panicking."
        mis "Don’t worry, I’ll be quick about this."
        mis "I am basically tasked with informing all students in my class that there will be an assembly at the first hour tomorrow so all students should head to the gym once they arrive at university."
        mis "The assembly is about the recent events in town. This assembly is mandatory, so missing it will come with repercussions. So make sure not to be late!"
        mis "After that we will let you go an hour later, to get home safer and in order for you to inform your parents or legal guardians about the current safety precautions that you were told about during the assembly."
        mis "As well as inviting them to participate in the parent-teacher conference that will be taking place later during the week, meant to solve any remaining doubts."
        scene bg allawaycall_2_neutral_talk
        pov "Alright, sounds like the standard run-of-the-mill stuff for these sort of situations."
        scene bg allawaycall_2_neutral
        mis "Yeah, they even gave me a whole script to say that has the most frequently asked questions in this sort of situations, so if you have any doubts feel free to ask!"
        scene bg allawaycall_2_neutral_talk
        pov "Can you explain again how I am supposed to divide the quadratic equations using the formula?"
        scene bg allawaycall_2_confused_talk
        pov "I can’t make heads or tails of the coursework assignment."
        scene bg allawaycall_2_confused
        mis "As much as I would love to explain you an entire topic of Algebra over the phone, I have to call the rest of your classmates to inform them about the assembly."
        scene bg allawaycall_2_neutral
        mis "I have gone through the first third of the class so I still have plenty of nervous student’s left to talk to."
        scene bg allawaycall_2_neutral_talk
        pov "Fair enough."
        pov "I won’t take more of your time, then."
        scene bg allawaycall_2_neutral
        mis "Alright!"
        mis "If that is all, have a good night, [povname]."
        scene bg allawaycall_2_neutral_talk
        pov "Same to you, Miss Allaway."

    #"You put down the phone once you are done talking and stare at the ceiling lost in thought."
    ###show bg allawaycall_temp1
    scene bg allawaycall_1_angry with fade
    pov "{i}It had to be them, right?{/i}"
    pov "{i}This can’t be just be a coincidence…{/i}"
    pov "{i}They took them to the other world, there’s no doubt about that.{/i}"
    scene bg allawaycall_1_confused
    pov "{i}The only question is why would they target Davendithas and his family?{/i}"
    pov "{i}Why would they want them in the first place?{/i}"
    pov "…"
    scene bg allawaycall_1_shocked
    pov "…"
    show bg allawaycall_2-5 with vpunch#ADDITION
    pov "{i}W-Wait, don’t tell me that-!{/i}"

    #"You shoot up to sit on the bed with a horrified look on your face."
    ###show bg allawaycall_temp3
    show bg allawaycall_3 with dissolve

    pov "{i}I-Is this my fault?!{/i}"
    pov "{i}Did they take them to sacrifice them instead of me?!{/i}"
    pov "{i}T-That can’t be right?!{/i}"
    pov "{i}That woman said I was the one who produced the best cum in town, but what if they are running out of time and just took whoever they found?{/i}"
    pov "{i}No…{/i}"
    pov "{i}No, that can’t be it, right?{/i}"

    #"You look straight out the window from your bed."
    ###show bg allawaycall_temp4
    show bg allawaycall_4
    pov "{i}She is still out there…{/i}"
    pov "{i}No, this whole kidnapping thing is for something else…{/i}"
    pov "{i}Otherwise they would have taken Davendithas or his father.{/i}"
    pov "{i}Why would they need his mother?{/i}"

    #"You go back to the bed and go back to staring at the ceiling."
    ###show bg allawaycall_temp1
    scene bg allawaycall_1_confused with fade
    pov "{i}Are they gonna stop with them?{/i}"
    pov "{i}Are they going to take the entire town?{/i}"
    pov "…"
    scene bg allawaycall_1_shocked
    pov "{i}Have they been replaced, like in a horror movie?{/i}"
    pov "…"
    scene bg allawaycall_1_sad
    pov "{i}*Sigh*{/i}"
    pov "{i}What the fuck am I supposed to do now?{/i}"
    scene bg allawaycall_1_angry
    pov "{i}I have to stop them.{/i}"
    pov "{i}I have to stop HER before they take someone I care about…{/i}"
    pov "…"
    pov "{i}I have to stop a sex cult from kidnapping the people in my new town and prevent them from sacrificing me - and for whatever fucking reason they have to want me dead, as well…{/i}"
    pov "..."
    pov "{i}I didn’t sign up for this shit!{/i}"
    scene bg allawaycall_1_bored_talk
    pov "Ughh.."
    scene bg allawaycall_1_sad
    pov "{i}I can’t waste anymore time on fucking around.{/i}"
    pov "{i}I’ll start gathering information tomorrow.{/i}"
    pov "{i}Someone has to know something…{/i}"
    pov "…"
    pov "{i}Please don’t let anyone else be kidnapped tonight…{/i}"

    $ main_story = 58
    $ townmap_enabled = 1

    scene black
    with fade

    jump lbl_mybedroom_day_sleep_1
