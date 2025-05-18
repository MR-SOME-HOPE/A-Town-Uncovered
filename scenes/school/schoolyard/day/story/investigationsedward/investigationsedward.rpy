##[School’s Entrance, afternoon - “Investigations_Edward”  - main_story =84-K]

##=This scene has 2 variants, if the Player hasn’t talked to Luna before approaching Edward, the Mc will note that he looks busy and he shouldn’t bother him. If the Player has talked to Luna before, Then the Mc will approach Edward and talk to him=
label lbl_investigations_edward:
    default investigations_edward = 0

    show btn schoolyard_day_edward_idle
    #-If Player has not talked to Luna before talking to Edward-
    if investigations_luna == 0:
        ##-The following dialogue happens within the Mc’s thoughts-

        pov "Edward seems to be hard at work on one of his gadgets."
        pov "Don’t want to interrupt his flow."
        pov "I should check back with him later when he is not looking so busy."
        pov "Let’s check with others nearby."

    ##-If Player has talked to Luna before talking to Edward-
    elif investigations_luna == 1:
        ##-The following dialogue happens within the Mc’s thoughts-
        if investigations_edward != 0:
            pov "I already spoke to him."
        else:

            pov "{i}Luna said Edward is just waiting for someone to ask about his work.{/i}"
            pov "{i}I guess he must have trouble starting conversations so he waits for other people to take interest and start them.{/i}"
            pov "{i}Well, no harm giving him some attention now.{/i}"

            ##-Back to regular talking-
            show pov neutral_talk at left
            with dissolve
            pov "Hey, Edward. Are you busy?"
            show pov neutral at left
            $ renpy.pause(0.001)

            show edw neutral_talk at right
            hide btn schoolyard_day_edward_idle
            with dissolve
            edw "Oh, hey, [povname]."
            show pov neutral at left
            show edw embarrassed_talk at right
            edw "Not at all! I was just doing some adjustments to one of my side projects."
            show pov confused_talk at left
            show edw embarrassed at right
            pov "Shouldn’t you be doing this somewhere inside to avoid dust or other stuff crawling in?"
            show pov confused at left
            show edw embarrassed_talk at right
            edw "Maybe if you are a novice or something."
            show pov neutral at left
            show edw neutral_talk at right
            edw "Being outside helps my brain think."
            show pov embarrassed at left
            show edw smirk_talk at right
            edw "Plus, some of my projects require being tested in an outdoor environment, you know?"
            show pov embarrassed_talk at left
            show edw smirk at right
            pov "I see."
            show pov neutral_talk at left
            show edw neutral at right
            pov "Actually, I was hoping to ask you more about some of your side projects?"
            show pov neutral at left
            show edw smirk_talk at right
            edw "Taking an interest in the craft?"
            show pov embarrassed at left
            show edw shocked_talk at right
            edw "It’s quite exciting to know just how many things you can make with some electronics and the right know-how."
            show edw smirk_talk at right
            edw "What caught your interest?"
            edw "Was it some of my drone prototypes? Or the safety backpack perhaps?"
            show pov confused at left
            show edw embarrassed_talk at right
            edw "It’s still missing the taser bits, but that’s on me for going through legal sources to obtain them."
            show pov shocked at left
            show edw bored_talk at right
            edw "Then again, it’s worth it to not suffer an accidental shock again like it happened when I got those cheap Taiwanese tasers from Cole."
            show edw sad_talk at right
            edw "The lesson of that whole mess is that you can’t afford to go cheap when it comes to your own safety, [povname]."
            show pov embarrassed at left
            show edw sad at right
            edw "Always remember that."
            show pov embarrassed_talk at left
            show edw embarrassed at right
            pov "Yeah…"
            show pov neutral_talk at left
            pov "All of those sound like really interesting projects and all, but I actually wanted to ask you about something else."
            show pov embarrassed at left
            show edw neutral_talk at right
            edw "Sure, ask me anything."
            show pov embarrassed_talk at left
            show edw shocked at right
            pov "Well, I was hoping to confirm if it’s true that you actually have installed cameras hidden around tow-"
            show pov shocked at left
            show edw angry_talk at right
            edw "SHHHHHHH!!"
            edw "Shut your mouth right now, dude!"
            show pov confused at left
            edw "Are you trying to get me arrested or something?!"
            show pov confused_talk at left
            show edw angry at right
            pov "So it is true, then?"
            show pov smirk at left
            show edw bored_talk at right
            edw "I’ll reject everything without the presence of a lawyer!"
            show pov smirk_talk at left
            show edw bored at right
            pov "Dude, it’s cool. I’m not accusing you of anything."
            show pov neutral at left
            show edw bored_talk at right
            edw "That’s good, because there is nothing worth accusing me for to begin with because I don’t know anything of what you are talking about right now."
            show pov bored_talk at left
            show edw confused at right
            pov "Edward, you are not helping your case here."
            show pov shocked at left
            show edw angry_talk at right
            edw "I know nothing!"
            show pov shocked_talk at left
            show edw angry at right
            pov "Calm down!"
            pov "Look, I’m gonna assume some of those cameras are on places that you clearly shouldn’t be on, so I won’t ask about those-"
            show pov angry at left
            show edw angry_talk at right
            edw "If you are accusing me of perving around, I assure you that is not the case sir!"
            show pov confused_talk at left
            show edw angry at right
            pov "So you admit to having them?"
            show pov confused at left
            show edw bored_talk at right
            edw "Depends on why you are asking for them in the first place."
            show pov bored at left
            show edw shocked_talk at right
            edw "But if I did, I wouldn’t be using them for anything other than honest to god research!"
            show pov smirk at left
            show edw smirk_talk at right
            edw "I’m not so scummy to try to put them in ladies bathrooms or the beach!"
            show pov bored at left
            show edw angry_talk at right
            edw "You are jumping to conclusions real fast there, sir!"
            show pov bored_talk at left
            show edw angry at right
            pov "What you do with them is your business, Edward."
            show pov smirk_talk at left
            show edw confused at right
            pov "I’m just trying to gather evidence about something."
            show pov bored at left
            show edw smirk_talk at right
            edw "If it is about what happened to you during your disappearance, you are out of luck."
            show pov confused at left
            show edw embarrassed_talk at right
            edw "None of the cameras caught any sight of you."
            show pov confused_talk at left
            show edw embarrassed at right
            pov "You checked?"
            show pov confused at left
            show edw bored_talk at right
            edw "Maybe, I still haven’t confirmed knowing anything."
            show pov angry_talk at left
            show edw bored at right
            pov "Dude, I’m not with the police or anything."
            show pov bored_talk at left
            show edw bored at right
            pov "Look, think I can borrow some of those cameras?"
            show pov bored at left
            show edw bored_talk at right
            edw "What cameras?"
            show pov angry_talk at left
            show edw bored at right
            pov "Edward!"
            show pov angry at left
            show edw bored_talk at right
            edw "{i}*sigh*{/i} Alright, alright."
            show pov angry at left
            show edw smirk_talk at right
            edw "I know you wouldn’t rat me out, but one can never be too safe when it comes to these things."
            show pov confused at left
            show edw embarrassed_talk at right
            edw "I already have 2 strikes with Officer Mina due to previous incidents, if she knew I also had a surveillance system in town, she would kill me before sending me to juvie."
            show pov confused_talk at left
            show edw embarrassed at right
            pov "Alright, that’s a fair enough fear."
            show pov confused at left
            show edw bored_talk at right
            edw "Look, I’ll tell you about them but this doesn’t leave this conversation and any further attempts to talk about them in public will be met with total ignorance and avoidance."
            show pov smirk_talk at left
            show edw bored at right
            pov "I can agree to those terms."
            show pov smirk at left
            show edw bored_talk at right
            edw "Good."
            show pov bored at left
            edw "Yes, I do have cameras around town, but again, it’s not for pervy purposes."
            show pov bored_talk at left
            show edw embarrassed at right
            pov "What are they for then?"
            show pov bored at left
            show edw bored_talk at right
            edw "Research."
            show pov bored_talk at left
            show edw confused at right
            pov "On what exactly?"
            show pov confused at left
            show edw embarrassed_talk at right
            edw "Are you familiar with “The Robotics Company”?"
            show pov confused_talk at left
            show edw neutral at right
            pov "At this point, I kinda have to. They are the ones installing the alarm and home safety system for free all over town, right?"
            show pov confused at left
            show edw embarrassed_talk at right
            edw "Well, it is my dream to work there one day."
            show pov bored at left
            show edw neutral_talk at right
            edw "I’ve made several projects and inventions in the hopes of one day presenting them to the board and CEO."
            edw "They have a scholarship program for young engineers and inventors who manage to surprise them and show promise, so I have been working my ass off on some of my projects."
            show pov bored_talk at left
            show edw smirk at right
            pov "What kind of projects."
            show pov confused at left
            show edw smirk_talk at right
            edw "Sorry, that bit is actually classified."
            show pov smirk at left
            show edw bored_talk at right
            edw "I trust you dude, but I tend to have bad luck with projects if I reveal them too early."
            show pov smirk_talk at left
            show edw bored at right
            pov "Fair enough."
            show pov bored_talk at left
            show edw embarrassed at right
            pov "So is the whole camera rig around town one of your projects?"
            show pov smirk_talk at left
            show edw smirk at right
            pov "Don’t tell me you plan on making Big Brother or something."
            show pov smirk at left
            show edw neutral_talk at right
            edw "I wish!"
            show edw embarrassed_talk at right
            edw "Can you imagine what some countries would pay me for a system capable of that kind of monitoring?"
            show pov embarrassed at left
            show edw shocked_talk at right
            edw "I would be a decadrillionare in whatever foreign currency they decided to pay me for sure!"
            show edw bored_talk at right
            edw "But no, I rather build robots, drones and things that don’t necessarily violate basic human rights."
            show edw smirk_talk at right
            edw "Besides, I just know there would be an ironic twist at the end where I’m brought to my demise by the very same system I created."
            show pov smirk_talk at left
            show edw shocked at right
            pov "Well, glad to know that at least you are up to date with your “Crazy Evil Genius 101” rule book."
            show pov smirk at left
            show edw smirk_talk at right
            edw "I’ll take the “Genius” part as a compliment, thank you very much."
            show pov bored_talk at left
            show edw smirk at right
            pov "Right."
            show pov confused_talk at left
            pov "So, if it’s not one of your projects, what is it then?"
            show pov confused at left
            show edw smirk_talk at right
            edw "I told you dude, research."
            show edw embarrassed_talk at right
            edw "I have my cameras installed on specific places I go to test the variety of gadgets and projects I make."
            edw "They are there so I can have multiple angles of whatever experiment or test drive I make."
            show pov smirk_talk at left
            show edw neutral_talk at right
            edw "It helps to determine the cause of issues if things went wrong or helps if I need to make a presentation if they do go right!"
            show pov confused_talk at left
            show edw neutral at right
            pov "Why not just set them up and take them down when you are done?"
            show pov smirk_talk at left
            show edw embarrassed at right
            pov "Why keep them there hidden away?"
            show pov smirk at left
            show edw bored_talk at right
            edw "I get a lot of my good ideas on a whim or in a sudden flash of brilliance."
            show pov bored at left
            show edw embarrassed_talk at right
            edw "Whenever I get those flashes I don’t have the time to waste setting up a filming gear in the angles I need."
            show edw neutral_talk at right
            edw "So I keep the cameras up in the exact angle and range I need and just shoot whenever I’m ready."
            show pov smirk at left
            edw "It saves a lot of valuable time of inspiration I could be using for further improvements to the devices."
            show pov smirk_talk at left
            show edw neutral at right
            pov "I guess I can see the logic to that."
            show pov bored at left
            show edw bored_talk at right
            edw "Besides, they are all looking away from the town or any private property for the most part and I delete any useless footage after analyzing the mistakes of my tests from their different angles."
            show pov confused_talk at left
            show edw bored at right
            pov "But then, why have so many test spots around town?"
            show pov confused at left
            show edw bored_talk at right
            edw "So that I can test different gadgets in optimal conditions depending on the gadget in question, duh."
            show edw smirk_talk at right
            edw "Some of my gadgets need to be tested in places away from the public and some have to be tested in areas closer to town."
            show edw bored_talk at right
            edw "So I need different test sites to monitor how they perform."
            show pov bored_talk at left
            show edw bored at right
            pov "I see."
            show pov confused at left
            show edw bored_talk at right
            edw "And they all remain off until I need to use them and they all mostly are set up in public property, so even if they were found and somehow linked back to me, they have no case against me whatsoever."
            show pov smirk_talk at left
            show edw bored at right
            pov "The fact you so adamantly refused to even admit about the cameras at first tells me there is a loophole you are afraid of somewhere in that logic."
            show pov bored_talk at left
            show edw shocked at right
            pov "Anyway, do you think I can borrow some of those cameras?"
            show pov bored at left
            show edw confused_talk at right
            edw "What for?"
            show pov bored_talk at left
            show edw confused at right
            pov "Look, it’s a long story but something weird is going on in this town and those cameras could be the tool I need to at the very least prove to myself I’m not going crazy."
            show pov shocked_talk at left
            show edw shocked at right
            pov "And perhaps even save my life if what I fear is happening is actually real."
            show pov bored at left
            show edw embarrassed_talk at right
            edw "Not the explanation I was expecting, not gonna lie."
            show edw smirk_talk at right
            edw "I was kinda expecting you to creep on some girls or something."
            show pov angry_talk at left
            show edw neutral at right
            pov "Now who’s jumping to conclusions?!"
            show pov angry at left
            show edw neutral_talk at right
            edw "I kid, I kid."
            show edw embarrassed_talk at right
            edw "Still it’s kind of a tall order, [povname]."
            show pov bored at left
            edw "I’m sorta running out of them."
            show pov confused_talk at left
            show edw embarrassed at right
            pov "Running out?"
            pov "Are you putting up more test sites?"
            show pov confused at left
            show edw embarrassed_talk at right
            edw "No, I’m replacing old ones actually."
            show edw sad_talk at right
            edw "This past few days I tried using some of my cameras on some tests only to find them either missing or wrecked."
            show pov shocked at left
            show edw angry_talk at right
            edw "Somebody has been messing with my whole setup and I haven’t been able to find any traces of who."
            show pov confused_talk at left
            show edw embarrassed at right
            pov "And you keep 'em off so no way to see who wrecked them in the footage, huh?"
            show pov confused at left
            show edw embarrassed_talk at right
            edw "Exactly."
            show pov bored at left
            show edw bored_talk at right
            edw "So just giving you a few cameras kind of puts me at a bad position here dude."
            show pov angry_talk at left
            show edw shocked at right
            pov "Come on, Edward. This is really important!"
            show pov angry at left
            show edw shocked_talk at right
            edw "Hey, my stuff is important too, you know?"
            show pov shocked at left
            show edw angry_talk at right
            edw "I’m out here busting my ass trying to make a device that could set me and my family up for life!"
            show pov shocked_talk at left
            show edw angry at right
            pov "I didn’t mean it like that, dude."
            show pov embarrassed_talk at left
            show edw bored at right
            pov "Look, is there something I could do for you to consider it?"
            show pov embarrassed at left
            show edw embarrassed_talk at right
            edw "Well, I guess if you agree to owe me a favour and test some gadgets I’m not willing to test on myself that would call us even…"
            show pov confused_talk at left
            show edw bored at right
            pov "That someone doesn’t seem even the least bit even for me seeing the possibility of serious injury..."
            show pov embarrassed_talk at left
            pov "Look, how about I get you something else?"
            show pov shocked_talk at left
            show edw confused at right
            pov "My dad works at “The Robotics Company” and-"
            show pov confused at left
            show edw shocked_talk at right
            edw "YOUR DAD WORKS AT “THE ROBOTICS COMPANY”?!"
            show pov shocked_talk at left
            show edw shocked at right
            pov "Well, yeah…"
            show pov confused_talk at left
            pov "His job was the reason we moved here."
            show pov confused at left
            show edw smirk_talk at right
            edw "Dude, why didn’t you say anything about it before?!"
            show pov bored_talk at left
            show edw shocked at right
            pov "Well, there was never a good time to bring it out and-"
            show pov shocked at left
            show edw shocked_talk at right
            edw "Do you think he could get me the interview with the board and CEO?!"
            show pov bored at left
            show edw smirk at right
            edw "I have so many ideas and inventions that could impress them, I just need some more time to develop them and-"
            show pov bored_talk at left
            show edw shocked at right
            pov "Alright, alright, calm down before you start hyperventilating or something!"
            show pov embarrassed_talk at left
            show edw neutral at right
            pov "Look, my dad is not an easy man to convince of things, but if I promise to try, will you help me set up the cameras I need?"
            show pov shocked at left
            show edw neutral_talk at right
            edw "DEFINITELY!"
            show pov shocked_talk at left
            show edw neutral at right
            pov "Edward, calm down!"
            show pov embarrassed at left
            show edw neutral_talk at right
            edw "Sorry, sorry!"
            show edw embarrassed_talk at right
            edw "It’s just that this is the closest I have ever gotten to actually getting to meet the board."
            show pov embarrassed_talk at left
            show edw embarrassed at right
            pov "I thought you had already planned it out though?"
            show pov embarrassed at left
            show edw neutral_talk at right
            edw "Well yeah, but you know how it is with these large corporations."
            show edw confused_talk at right
            edw "All the times I tried to make an appointment to introduce my ideas, the system of secretaries and machines only threw me for a loop to make me go away."
            show edw embarrassed_talk at right
            edw "I have been trying hard to get their attention in other ways, but even now I haven’t really gotten anywhere..."
            show pov shocked at left
            show edw shocked_talk at right
            edw "But with you it changes!"
            show edw smirk_talk at right
            edw "You actually have someone on the inside that is above the automated system that us people outside the company have to access through!"
            show pov embarrassed_talk at left
            show edw smirk at right
            pov "Dude, don’t get your hopes up, he is really mainly an office worker here."
            show pov bored_talk at left
            pov "Plus he is a difficult man to talk to these days he’s done some…"
            show pov smirk_talk at left
            show edw embarrassed at right
            pov "Rather hurtful things to the family lately so we aren’t in the best of terms."
            show pov bored_talk at left
            show edw shocked at right
            pov "Besides, I don’t even really know what he does."
            show pov confused at left
            show edw shocked_talk at right
            edw "Maybe not, but it could be a chance I won’t get otherwise!"
            show pov shocked at left
            show edw embarrassed_talk at right
            edw "Please promise me you’ll try and that’s gonna be enough for me to help set up the cameras!"
            show pov embarrassed_talk at left
            show edw embarrassed at right
            pov "I…"
            pov "I guess I don’t have any other choice at this point."
            show pov bored_talk at left
            show edw shocked at right
            pov "Fine, I’ll give it a shot."
            show pov bored at left
            show edw shocked_talk at right
            edw "Thank you! Oh, thank you [povname]!"
            edw "I won’t ever forget this favour, ever!"
            show pov bored_talk at left
            show edw shocked at right
            pov "Can we start discussing the cameras proper now?"
            show pov smirk at left
            show edw neutral_talk at right
            edw "Sure! Where do you need them and what do you expect to find?"
            show pov embarrassed_talk at left
            show edw neutral at right
            pov "I need them in the lake in the park."
            show pov confused_talk at left
            show edw confused at right
            pov "It’s likely going to be in the night, so do you have any camera with night vision?"
            show pov confused at left
            show edw confused_talk at right
            edw "Dude, who do you think you are talking to?"
            show edw smirk_talk at right
            edw "Of course they do! Even have the ability to stream directly into my network with a high definition degree!"
            show pov smirk_talk at left
            show edw smirk at right
            pov "Sweet, well, We’ll definitely need those covering the whole lake."
            show pov shocked at left
            show edw confused_talk at right
            edw "Why the lake though?"
            show pov smirk_talk at left
            show edw confused at right
            pov "Trust me, it’s a long story."
            show pov neutral_talk at left
            pov "They need to be hidden because no one else can know about this."
            show pov smirk_talk at left
            show edw smirk at right
            pov "Do you think you can do it?"
            show pov smirk at left
            show edw smirk_talk at right
            edw "Again, who do you think you are talking to?"
            show pov neutral at left
            show edw embarrassed_talk at right
            edw "I’ll need a few days, but I’ll have the whole thing ready soon enough."
            show edw neutral_talk at right
            edw "Once I have them up, I’ll send you a text to show you the set up and will let you know if I find anything."
            show pov neutral_talk at left
            show edw neutral at right
            pov "We only need to record at night when the park is empty."
            show pov neutral at left
            show edw neutral_talk at right
            edw "That saves on battery life and will make them easier to hide then!"
            show edw smirk_talk at right
            edw "Keep your part of the barging and I’ll keep mine."
            show pov smirk_talk at left
            show edw smirk at right
            pov "Sounds like we have a deal then."
            show pov neutral at left
            show edw smirk_talk at right
            edw "A deal it is!"
            show pov shocked at left
            show edw neutral_talk at right
            edw "Now, I better get going to start setting them up then."
            show pov confused_talk at left
            show edw smirk at right
            pov "Wait, you are going to start now?"
            show pov confused at left
            show edw smirk_talk at right
            edw "Well duh, no way in hell am I doing it at night after you told me we have to keep surveillance for something there!"
            show edw shocked_talk at right
            edw "The fact you won’t even tell me what it is only makes it scarier!"
            show pov bored at left
            show edw bored_talk at right
            edw "It will be a bit more difficult to set them up during the day so that’s why I’ll need a few days to set up a perimeter to be sure I catch everything."
            edw "Have to make sure I’m not seen while installing and test them so I’ll have to do it at the crack of dawn and in the afternoon when there are less people."
            show pov shocked at left
            show edw smirk_talk at right
            edw "Installing military grade surveillance equipment is a timely task, you know?"
            show pov shocked_talk at left
            show edw confused at right
            pov "Wait, we didn’t say anything about military grade."
            show pov confused at left
            show edw smirk_talk at right
            edw "You only get the best when you are helping me achieve my dreams bro."
            show pov shocked_talk at left
            show edw smirk at right
            pov "Well, thanks then!"
            show pov smirk at left
            show edw bored_talk at right
            edw "The only thanks I need is for you to keep your part of the barging."
            show pov embarrassed_talk at left
            show edw smirk at right
            pov "I know, I know."
            show pov neutral_talk at left
            show edw neutral at right
            pov "I’ll figure something out."
            show pov neutral at left
            show edw shocked_talk at right
            edw "Good!"
            show edw neutral_talk at right
            edw "I better get to work then, see you [povname]!"
            show pov neutral_talk at left
            hide edw
            with dissolve
            pov "Yeah, thanks again!"

            ##-Edward now leaves the frame leaving the Mc alone with his thoughts-
            show pov shocked_talk at left
            pov "Well, that went well."
            show pov bored_talk at left
            pov "Now I just need to somehow convince my dad to agree to talk to someone in his work that could help Edward and I on this…"
            pov "Oh shit…"
            $ investigations_edward = 1

    jump lbl_schoolyard_day_setup
