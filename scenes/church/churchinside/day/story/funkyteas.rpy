label lbl_funky_teas:
    default funky_teas_choice = 0
    #-Following scene takes place the next time that the player interacts with the door to Lashley’s office.
    # They will have a prompt to meet up with Lashley at the church and if they accept,
    # they will transition to the inside of the church where the Mc is waiting-


    scene bg church_night
    show pov confused
    with fade
    pov "{i}Hmmm- looks like no one's here.{/i}"
    show pov bored
    pov "{i}Wonder where she is.{/i}"
    show pov embarrassed
    pov "{i}Guess I'll wait around.{/i}"

    scene black
    with fade
    $ renpy.pause()
    "Half an hour later..."

    scene bg church_night
    show pov confused_talk at left
    with fade
    pov "…"
    pov "She sure is taking her sweet time…"
    show pov smirk_talk at left
    pov "She isn’t replying to any of my texts either."
    show pov bored_talk at left
    pov "Did she get flooded with last minute paperwork or something?"
    pov "Perhaps I should go and check she is okay or-"

    #-Mc’s thoughts are interrupted by Lashley hurriedly appearing on to the scene-

    show pov shocked at left
    show pri embarrassed_talk at right
    with dissolve
    pri "{i}*huff* *huff*{/i} I-I’m here!"
    pri "Oh good heavens, I made it!"
    show pov confused_talk at left
    show pri embarrassed at right
    pov "There you are, I was worried something happened to you or you were going to cancel on me last minute."
    show pov confused at left
    show pri embarrassed_talk at right
    pri "I am so, so sorry, [povname]!"
    pri "I promise it wasn’t intentional or anything!"
    show pov smirk at left
    show pri bored_talk at right
    pri "Ugh, everyone suddenly needed me for all kinds of silly things and not to mention this one person was late in delivering me something I requested days ago and just, ugh!"
    pri "Just wait until I get my hands on them later!"
    show pov embarrassed_talk at left
    show pri angry at right
    pov "Woah, never seen you this worked up about something before."
    show pov embarrassed at left
    show pri bored_talk at right
    pri "Well, I felt terrible keeping you of all people waiting for me for so long!"
    pri "I was hoping to just finish with today’s paperwork and having that stuff delivered to me by the end of it and just head over here right away."
    show pri bored_talk at right
    pri "But this one person decided that whatever they were doing was more important so I had to wait for them to arrive."
    pri "And since people saw I was staying a bit later than usual, a ton of people decided to just barge into my office and add themselves to the work pile."
    show pov neutral at left
    show pri sad_talk at right
    pri "Students needing help about this and that, Teachers needing me to reorganize schedules due to them needing a day off, the janitor complaining about gross white stuff in the bathrooms."
    pri "Just the whole nine yards that I just didn’t have time for today."
    show pov neutral_talk at left
    show pri bored at right
    pov "That’s new, I thought you lived to be able to help and take care of everybody like that."
    show pov embarrassed at left
    show pri angry_talk at right
    pri "Well, yes. But why did it have to be today?!"
    pri "Every other day my door is open for everybody to just come in and complain, but the one day I have reserved for both of us just happens to be the day everybody needs something from me!"
    pri "It’s just so frustrating that I could just… UGH!!!"
    pri "I swear, once I have the chance, I’m going to force them to understand the importance of punctuality!"
    show pov neutral at left
    show pri bored_talk at right
    pri "I’m really, really sorry, [povname]."
    show pov neutral_talk at left
    show pri sad at right
    pov "It’s cool, Lashley, really."
    pov "No harm done."
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "But thanks to all of this, we now lost a whole hour together and I had planned for so much to say and do and-"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "Complaining is just gonna take more time from that."
    pov "Let’s just forget about it and you can begin showing me what you wanted me to see, sounds good?"
    show pov embarrassed at left
    show pri embarrassed_talk at right
    pri "{i}*sigh*{/i}... I guess it’ll have to do…"
    pri "Let me just sit down and take a breather, I have been standing up for a while dealing with all that last minute work."
    show pov smirk_talk at left
    show pri neutral at right
    pov "Sounds good to me, don’t let me stop you."

    #-Lashley takes a seat next to the Mc-

    ## CG SCENE STARTS
    hide pov smirk at left
    hide pri neutral at right
    with dissolve
    show bg funkyteas_1
    with dissolve
    pri "{i}*sigh*{/i} I had so much planned to show you…"
    show bg funkyteas_2
    pov "Did you have a whole tour guide or something?"
    pov "Does it really take much time to take a look at this whole place?"
    show bg funkyteas_3
    pri "Oh, it certainly does!"
    pri "You may have assumed this already but I’m deeply involved in the management and conservation of this church along with the cemetery adjacent to it."
    show bg funkyteas_2
    pri "It’s been around since the founding years of the town, it was one of the first buildings to be built in fact!"
    pri "My family has been in charge of it ever since then, with the eldest male always taking the role as the designated preacher all the way until my father’s generation."
    show bg funkyteas_4
    pri "I would spend countless hours here listening to sermons, singing in the choir, attending all kinds of events during the happiests and most terrible moments where the lord’s guidance was most needed."
    pri "I saw children being presented to the lord, charity events where we would help those in need, tremendous barbeques where the whole community got together, heart wrenching funerals where we said goodbye to beloved members of the town…"
    show bg funkyteas_3
    pri "And the most wonderful of weddings where we could see a man and a woman declare their eternal love for one another in the face of our lord and savior."
    pri "Tying their immortal souls together for the rest of eternity while they took the first step towards everlasting happiness."
    show bg funkyteas_2
    pri "And every single wedding was even more and more beautiful than the last."

    pov "Quite a lot of memories for a place this old, huh?"
    show bg funkyteas_3
    pov "Aren’t you afraid the foundation may be shoddy or moldy or something?"
    show bg funkyteas_4
    pri "Oh, don’t be silly, [povname]."
    show bg funkyteas_1
    pri "I told you, my family has been taking care of the church since its founding years."
    pri "Whatever damage or wear that may show with time has been properly taken care of or replaced."
    pri "I estimate that by now there is very little left still up from the original church."
    pri "But it’s message, memories and values are still here as fresh and intact as it’s always been."
    pri "It’s the sort of thing you can only really get when a building has seen as much history as this one has."
    show bg funkyteas_3
    pov "And you were planning on giving me a tour of the whole place?"

    pri "Precisely!"
    pri "I wanted to take you all across the church and show you all of these wonderful places and tell you all about what they meant for me."
    pri "I wanted to share this whole part of me that no one really gets to know much about."
    show bg funkyteas_2
    pov "Not that I don’t appreciate it or anything, but don’t you think that's a bit too personal to share with your student?"
    show bg funkyteas_4
    pri "Don’t sell yourself short, [povname]."
    show bg funkyteas_1
    pri "You should know by now since you get to call me by my first name that you are more than that at this point."
    pri "So, so much more…"
    show bg funkyteas_2
    pov "I-Is that so?"
    show bg funkyteas_3
    pri "Mhm! It feels so liberating to be able to share this with someone who really listens and understands."
    show bg funkyteas_1
    pri "I feel like I can really just open up to you and show this sort of sight of myself that is begging to be shared with somebody."
    pri "It just… Feels right, you know?"
    show bg funkyteas_4
    pri "To open up like this to you..."
    pri "Oh, I wish I could introduce you to my father."
    pri "You two would have so much to talk about and get along so well, I’m sure of it!"
    show bg funkyteas_1
    pov "H-He sounds like quite the guy…"
    pov "Listen, Lashley, I-"
    show bg funkyteas_3
    pri "Would you like some tea?"

    pov "Uh… What?"

    pri "Tea! It’s what I was waiting so long for it to be delivered."
    pri "I have a thermus filled to the brim with some."
    pri "I have recently gotten into the whole fascinating world of herbal infusions and I really wanted to make a special tea for today."
    show bg funkyteas_2
    pri "So I joined this online group and have been trying out some different recipes they recommend and teach me."
    pri "I wanted to make something special for today."
    pri "Just something for us to share while we take in the moment and all."
    show bg funkyteas_3
    pov "That’s nice, but I don’t really drink-"
    show bg funkyteas_1
    pri "It took a lot of time to get everything ready and I was really worried it wouldn’t arrive in time."
    pri "It’s a blend I learned to make specifically for us two alone to share."
    pri "And it would really mean a lot to me if you tried it out too."

    pov "I-I, um…"
    show bg funkyteas_3
    pri "Pretty please?"

    pov "…"
    show bg funkyteas_2
    pov "Alright…"

    pri "Oh, you are the best, [povname]!"
    show bg funkyteas_3
    pri "It’s really good, I can assure you that I worked hard to get it just right!"
    show bg funkyteas_5
    pov "Sounds good…"

    #-Lashley serves the mc a cup from her thermos, the liquid has pink color to it-

    show bg funkyteas_6
    pov "Oh wow, this actually smells really good!"

    pri "Right?!"
    show bg funkyteas_7
    pri "It’s quite the popular recipe with the group."
    pri "It helps with increasing your overall circulation and your blood flow along with helping you relax while giving your body a warm feeling."

    pov "We won’t have any trouble drinking this here?"
    pov "I had the idea you couldn’t bring food or drinks inside a church. Won’t the preacher or a nun get mad?"
    show bg funkyteas_8
    pri "Oh, don’t you worry about that."
    pri "The acting preacher is currently in a seminar in the next town and the nuns of the congregation are out as well, though they didn’t really say where they were going."
    show bg funkyteas_9
    pri "I made sure that we had the church for just the two of us. I didn’t want anyone to come in and just give you a sermon out of the blue, you know?"
    pri "Plus, it lets us have an open conversation without having to keep impressions."
    pri "I want to just relax for once with my friend without having to hide the fact to people and pretend you are serving detention."
    show bg funkyteas_4
    pov "That’s fair enough."
    pov "Still though, I’m kinda surprised you are ok with breaking the rules a little here."
    show bg funkyteas_3
    pri "No harm, no foul and all that, right?"
    pri "They won’t disapprove of what they don’t know and I’m sure the lord won’t mind either."
    show bg funkyteas_2
    pri "It’s a special occasion after all."
    show bg funkyteas_3
    pri "Well, how about you give a try?"
    pri "Careful though, it’s hot."
    show bg funkyteas_2
    pov "Don’t mind if I do."

    #-The Mc takes a sip of the tea-

    show bg funkyteas_10
    pov "Damn, it’s really good!"
    show bg funkyteas_2
    pov "Mind if I ask what’s on it?"
    show bg funkyteas_10
    pri "Not at all!"
    pri "It’s actually a bit of a floral mixture with something special added to it."
    pri "It’s based on things like ginger, roses, hibiscus, sarsaparilla and… Damiana with a little extra to it."
    show bg funkyteas_3
    pov "A little extra?"

    pri "Oh, nothing to be concerned with, I assure you."
    pri "I’m not really supposed to talk about it since it’s a bit of the group’s secret."
    show bg funkyteas_2
    pri "Their herbs for the infusions, especially those like the Damiana are genetically modified."
    pri "It normally scares people off when they hear that, but I assure you that it’s only so that their fragrances and their natural properties are stronger when infused into tea."
    pri "Nothing dangerous."
    show bg funkyteas_4
    pov "Oh, alright then."
    pov "So the Damiana on this has been enhanced then?"
    pov "What are its properties?"
    show bg funkyteas_3
    pri "Oh, you know. This and that."
    pri "Iit’s properties mainly work on helping stimulate your body, help strengthen your nervous system, it’s supposed to help elevate your mood, calm nerves and mainly help with relieving tension."
    pri "You’ll feel more relaxed and you are going to feel a little heat for a second but that’s supposed to happen, don’t worry."
    show bg funkyteas_2
    pov "Now that you mention it, I do feel a bit more relaxed."

    pri "That’s great! Be sure to finish your cup, I’ll serve you some more once you are done."
    show bg funkyteas_3
    pov "Aren’t you having some too?"
    show bg funkyteas_10
    pri "In a second, [povname]."
    pri "I came rushing here so I’m a bit out of breath."
    pri "Let me cool my body a bit, it’s not healthy to drink hot beverages when you are all heated up, you know?"
    show bg funkyteas_2
    pov "I guess that’s fair enough."
    show bg funkyteas_1
    pri "For now, lets just take in the moment, okay?"

    pov "Sounds fine by me."

    #-The Mc and Lashley take a moment in silence, Lashley is looking a bit smug though since the tea is basically an aphrodisiac she enhanced just for the Mc and is waiting for it to start taking effect. Perhaps have her looking at his crotch as if anticipating him getting hard soon before making her next move?-

    #-The following dialogue happens in the Mc’s thoughts-

    pov "{i}Huh, this tea stuff is really hitting the spot!{/i}"
    pov "{i}Haven’t felt this relaxed in a while…{/i}"
    pov "{i}And I think I’m starting to feel that heat Lashley was talking about.{/i}"
    pov "{i}Though… Why do my pants feel tighter all of a sudden?{/i}"

    #-Back to regular dialogue-

    show bg funkyteas_2
    pri "This is nice, isn’t it?"
    pri "Churches and buildings like that just have this sort of… effect on them."
    pri "Like being protected by a warm blanket or something…"
    pri "Like whatever may be going on outside, you’ll be safe inside of them."
    pri "You know what I mean?"
    show bg funkyteas_1
    pov "Yeah, I think I do."

    pri "But they can also have such a foreboding feeling to them as well."
    pri "Like, something is constantly watching you and making sure you behave and all that."
    pri "But that can also add to the excitement when you are doing something you are not supposed to, right?"

    pov "Uh… Y-Yeah, I suppose so."
    show bg funkyteas_3
    pri "I remember on weddings when my father acted as the priest, I was always picked as the flower girl."
    pri "I always found it fun to make faces in photographs, but only every so often so that the couple could have pictures without me making a face at them."
    pri "My father never found out, but I was the bane of the photographers existence since I tended to ruin shots."
    pri "I know I wasn’t supposed to, but it was just fun after such a hectic day, you know?"

    pov "I can’t imagine you ever making faces in a picture."

    pri "I think I have some on the old album back in my abode, I’ll be sure to show them to you sometime."
    show bg funkyteas_4
    pri "But since I brought the whole subject, I can’t help but be curious about…"
    pri "Well..."
    show bg funkyteas_2
    pov "What is it?"

    pri "[povname], do you ever want to get married?"
    pri "Have you ever considered it?"

    menu:
        "Yes":
            $ funky_teas_choice = 1
            #-If “pov "Yes” was picked-

            #+1 Lashley RP.
            $ add_points("principallashley_points",1)

            show bg funkyteas_2
            pov "Well, the question comes out of nowhere, but yeah. I think I do."
            show bg funkyteas_1
            pri "That’s wonderful to hear!"
            pri "Oh I’m so relieved!"
            show bg funkyteas_3
            pov "You are?"
            show bg funkyteas_4
            pri "U-Uhm, I mean-"
            pri "Of course!"
            show bg funkyteas_3
            pri "You are my student after all and I think it’s important for you to have a semblance of an idea of what you want your future to be like."
            pri "And call me old fashioned if you want, but I believe marriage is one of those stepping stones one must reach in their lives once they find that special someone to share with."

            pov "That’s a more than respectable view to have."

            pri "Thank you and I’m sure you’ll excel as a husband once the time is right."
        "No":
            $ funky_teas_choice = 2
            #-If “pov "No” was picked-
            #-1 Lashley RP.
            $ subtract_points("principallashley_points",1)

            show bg funkyteas_1
            pov "Well… If I can be honest with you, it’s not something I have really considered for me."
            show bg funkyteas_2
            pri "W-WHAT?!"
            pri "WHY THE FRICK NOT?!"
            show bg funkyteas_3
            pov "Woah, easy there Lashley!"
            pov "Jeez, I didn’t think it was such a big issue."

            pri "Oh, but it is, [povname]!"
            pri "Don’t you know that marriage is one of the pillars to build a stable future?!"
            pri "Not to mention it is also an important step to then proceed to procreating the next generation and ensure your bloodline continues!"
            show bg funkyteas_2
            pov "W-Well, I’ve just never thought it was something really fit for me, you know?"
            pov "You don’t have to yell about it though..."

            pri "I-I’m sorry, [povname], I swear I didn’t mean to."
            pri "I-It’s just that as your Director, I find it worrying that you haven’t considered it."
            pri "It is quite an important step of life, you know?"
            show bg funkyteas_4
            pov "Well, I’m still young so I haven’t really paid attention to that whole aspect of it."
            pov "Plus, I haven’t been dating long enough to say a woman has changed my mind about the whole thing, you know?"
            show bg funkyteas_1
            pri "Oh, don’t you worry about that."
            show bg funkyteas_2
            pri "I’m sure soon enough the right woman will change your mind about it all in no time."
            pri "And once you do, you’ll be a great husband to her too!"

        "That’s a secret":
            $ funky_teas_choice = 3
            #-If “pov "That’s a secret” was picked-
            show bg funkyteas_1
            pov "Well, that’s actually a secret."
            show bg funkyteas_2
            pri "Oh, come on now!"
            pri "It’s alright, you can tell me."

            pov "I’ll take a raincheck on it."
            pov "I mean, I’m not saying yes or no, but I have to think about other stuff first."
            show bg funkyteas_3
            pov "Finishing school, finding a job."
            pov "Important things I have to do first before the idea of the big day, you know?"
            show bg funkyteas_2
            pov "So I rather keep it to myself until I feel like the time is right and all."
            show bg funkyteas_1
            pri "I see…"
            pri "Well, I can see the logic behind it all, but I still don’t like how you won’t tell me."
            show bg funkyteas_2
            pri "I guess as an educator, I should be happy that you are taking school seriously, so let’s leave it at that."
            pri "Well, still. There are some things in life that don’t wait until you are “ready” for them, you know?"
            pri "The right woman for you just may find you when you least expect it and put a ring on your finger before you know it."
            pri "And when she does, I’m sure you’ll step up to the plate and be an amazing husband."


    #########
    show bg funkyteas_3
    pov "Thanks, but what brought this on?"
    show bg funkyteas_4
    pri "Oh, just me reminiscing about all those weddings in my childhood, sorry about that."
    pri "I just get all dreamy about it when I come here and remember all the weddings that I attended through the years and all."
    show bg funkyteas_3
    pri "Every girl dreams of their wedding day, you know?"
    pri "But I guess you boys are more interested on what happens on the wedding night huh?~"

    #-By now, Lashley is full on smug, knowing the effect of the tea is kicking in-

    #-Mc’s Thoughts-
    show bg funkyteas_1
    pov "{i}Why do I… Keep feeling hot?{/i}"
    pov "{i}My pants too, they…{/i}"
    show bg funkyteas_2
    pov "{i}Oh no… Now’s not the time for that!{/i}"

    #-Back to regular dialogue-
    show bg funkyteas_3
    pov "I-I don’t know what you mean?"

    pri "Really? I was under the impression all men had the same thing in mind when it came to this sort of thing."
    pri "I mean, seeing the woman of your dreams willing to give herself to you in mind, body and soul?"
    pri "Taking off that giant dress to reveal the lingerie underneath…"
    pri "Her opening herself up to you as she begs you to connect yourself to her most intimate part to then embrace…"
    show bg funkyteas_2
    pov "I-I…"

    pri "And don’t you get me started on the honeymoon~"

    #-By now the Mc is at full mast and hiding himself-
    show bg funkyteas_3
    pov "Oh boy…"

    pri "Hmm?"
    pri "Is something wrong, [povname]?"

    pov "N-No, nothing at all!"

    pri "Are you sure? You seemed oddly tense…"
    pri "Did the tea not sit well with you?"
    show bg funkyteas_2
    pov "I-I’m telling you, I’m fine!"
    pov "Just a bit of a cramp is all!"

    pri "It’s not good to lie, [povname]."
    pri "I can tell something’s wrong, you are real easy to read."
    show bg funkyteas_3
    pov "I-I don’t know what you are talking about…"
    show bg funkyteas_12
    with dissolve
    pri "Is it perhaps…"
    show bg funkyteas_13
    with dissolve
    pov "W-Wait, Lashley. Don’t-!"

    #-Lashley uncovers the Mc to reveal the bulge in his pants with fake surprise-

    show bg funkyteas_14
    with dissolve
    pri "{i}*Gasp*{/i} O-Oh my..."

    pov "I-I’m so sorry!"
    pov "It just came up out of nowhere and I didn’t want you to-"
    show bg funkyteas_11
    with dissolve
    pri "Shhhh… It’s okay, [povname], I’m not mad at you or anything."
    pri "It’s likely my fault anyway, so don’t be embarrassed."
    show bg funkyteas_3
    with dissolve
    pov "What do you mean it’s your fault?"

    pri "Well, like I told you, the tea helps with blood circulation, right?"
    pri "It’s only natural for blood to rush there when you hear something naughty, don’t you think?"
    show bg funkyteas_4
    with dissolve
    pov "Well, but still…"

    pri "I didn’t realize my wording and made it far raunchier than it needed to be, I’m sorry."
    pri "Don’t you worry though, I’ll take care of it."
    show bg funkyteas_12
    with dissolve
    pov "W-What do you mean?"

    pri "W-Well, the nuns may be here any second and who knows when it will get soft again, so I can’t just let you walk home with it bulging out of your pants, right?"
    pri "That would only bring you bigger problems if someone saw you. Officer Mina has a zero tolerance on Perverts and creeps after all."
    show bg funkyteas_13
    pri "Besides, since it’s all swollen like that, it must feel pretty uncomfortable."
    pri "S-So, let me take care of it since it’s my fault you have it in the first place..."

    pov "B-But Lashley, I-"
    show bg funkyteas_14
    with dissolve
    pri "Shhh, you don’t have to say anything…"
    pri "Accident or not, I caused this so it’s my responsibility."
    show bg funkyteas_11
    with dissolve
    pri "This is just me going the extra mile for you, so don’t think about it too much."
    pri "Besides with the tea still in your system it could take a bit to get flacid on it’s own."
    pri "This is just the quickest way to get rid of it."

    pov "I…"
    show bg funkyteas_13
    with dissolve
    pri "Follow me, we can’t do this here."

    pov "R-Right.."

    jump lbl_lashleys_hunger
    #=SCENE END=
