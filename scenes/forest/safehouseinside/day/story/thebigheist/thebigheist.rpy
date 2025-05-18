label lbl_the_big_heist:
    default big_heist_choices_jacob = 0
    default big_heist_choices_effie = 0
    default big_heist_choices_pov = 0
    #[Edward's Computer, Night - “The Big Heist”  - main_story =118]

    #-The following scene takes place from the perspective of Edward on his computer
    # where he is monitoring everything from a drone while listening in to the
    # earpieces he has on his friends. After a brief introduction, the player will
    # have a choice between Jacob, Effie and Mc where they will follow whoever they
    # chose inside the different storage unit and learn what's inside with a different
    # background for each unit-

    scene black
    with fade

    $ renpy.pause()

    scene bg thebigheist_1
    with fade

    edw "Alright guys, final testing of the earpiece, do you copy?"

    pov "Copy."

    eff "Copy."

    jac "I copy too."
    jac "Though seriously dude, you couldn’t find a better fitting earpiece for me?"
    jac "This thing is hurting my ear like crazy, man!"

    edw "Sorry, dude, but it’s what I had on hand that could support the electronics for it."
    edw "I had to rush to make an extra pair so all four of us could have one, you know?"

    jac "And why am I the one stuck with the crappy one?!"

    edw "Because you almost broke the GPS tracker I brought for this when I was setting it up!"

    jac "It’s not my fault you didn’t tell me the wiring was so delicate!"
    jac "It’s obviously going to get tangled if it’s left lying around like that!"

    edw "I didn’t have much time to secure everything properly due to the circumstances, ok?!"

    eff "Ok, enough you two!"
    eff "I swear I’ll smack the hell out of the two of you if you keep arguing!"
    eff "Can I remind you guys we are supposed to be sneaking around, now?!"

    pov "Is the GPS ready, Edward?"

    edw "Yeah, I’ve got a live feed of your locations. The system triangulates your positions based on the trackers in your earpieces."
    edw "It’s accurate enough to show me which room or hallway you’re in, so I’ll guide you based on that."
    edw "I’ve also mapped the guard patrol patterns from the warehouse’s stolen security logs."
    edw "Most of the guards are on the far ends of the warehouse, I think, so this is the best time to get inside and start moving."

    pov "Right, and we’ll know where the cameras are facing from the little display thing you gave us, right?"

    edw "Correct. I synced your trackers with the security feed data. Just remember that whenever the light on your display flashes green, you’re good to cross."
    edw "But if it flashes red, you need to get close to a wall or a corner and hide to avoid the cameras."

    eff "So we’re just playing extreme red light, green light?"

    jac "I just hope we don’t get caught in this version of it…"

    edw "As long as you move between safe zones and listen to my instructions about the guards, we should be fine."
    edw "If you can’t reach the next zone in time or are in danger of being caught, use your cards to enter the closest storage unit."
    edw "That should buy you some time until it’s safe to move again."

    jac "I’m trusting you to keep your eyes glued to that screen, Edward!"

    edw "Dude, I’m literally sitting here in a bush, surrounded by bugs, using my laptop with barely any light."
    edw "Where else would my eyes be?!"

    jac "Probably looking at that thing behind you?"

    edw "WHAT?!"

    jac "Hah! Made you look, didn’t I?!"

    eff "-SMACK-"

    jac "OW!"

    eff "Next time it’s going to be with the crowbar!"

    pov "Alright, alright. Enough messing around."
    pov "Edward, are we in the clear to get in?"

    edw "Y-Yeah, you guys are in the clear."
    edw "I’ll keep monitoring the patrol routes and let you know once you’re close to your respective targets."
    edw "I’ll keep you guys on single channels unless you find something, just to save battery."
    edw "Remember, guys, we gotta do this quickly."
    edw "You ready?"

    pov "Ready as I’ll ever be, I guess."

    jac "Just finished my stretches and I’m ready to roll!"

    eff "This has been a long time coming, and I’m ready for anything."

    edw "Alright, you guys, let’s get this crazy night over without any of us ending up in jail."

    jac "MISSION START!"

    eff "What?"

    jac "Reference, never mind, they got it."

    #-Fade to black to indicate passage of time-
    scene black with fade


    #-scene transitions once again to Edward on his laptop, perhaps a new set
    # of screens to indicate what he is seeing on his GPS monitoring software.

    edw "OK, GPS shows the guys are close to their respective targets."
    edw "The guards are still mostly out of the way, so I should start monitoring what the guys are up to."
    edw "But who should I start with?"

    menu menu_big_heist_choices:
        "Jacob" if not big_heist_choices_jacob:
            #-If “Jacob.” was picked-
            $ big_heist_choices_jacob = 1

            edw "Jacob, do you read me?"

    jac "Don't know if I can read you, but I can totally hear ya!"

    edw "You really pulling Dad jokes on me, Dude?"

    jac "Sorry."
    jac "Humor is how I deal with stressful situations."

    edw "Fair enough, I suppose."
    edw "Your GPS signal shows you’re close to Unit-B22, is that correct?"

    jac "Yep!"
    jac "I’m about to scan the access card now."

    edw "Damn, dude. You really dashed there!"

    jac "Yeah, man!"
    jac "I mean, I know I got into the cross-country club to flirt with the hot coach, but I still learned a lot about running, you know?"
    jac "Though it’s hard to keep a steady pace while also making sure I don’t make too much noise with my feet."
    jac "Not to mention the constant stops to time my moves with the camera sweeps."
    jac "My legs are gonna feel it in the morning, man…"
    jac "Can’t say I don’t envy your position sitting in a bush all comfy."

    edw "Heh, trust me, dude. It’s not as cozy as you think."
    edw "I’m glued to this screen tracking your GPS and keeping an eye on the perimeter cameras."
    edw "That, and fighting off bugs crawling under my shirt."
    edw "Not to mention watching out for any late-night dog walkers."

    jac "At least you can’t say you’re beating around the bush, huh?"

    edw "Heh, ok. I’ll give you that one."

    jac "Knew I could get a chuckle out of ya!"
    jac "Alright, I’m inside the unit."

    edw "Got it. Your GPS shows you're stationary now. What do you see?"

    jac "Not much... It’s pitch black in here."
    jac "I’m looking around for a light switch or something."

    edw "Should be by the entrance wall, according to the layout."

    jac "Yeah, give me a sec to feel around and…"
    jac "Ah, there we go!"

    edw "What’s inside? Describe it to me while I sync the info for the others."

    jac "Clothes."
    jac "Like... A lot of clothes."

    edw "Huh. Hang tight; I’m looping Effie and [povname] into the channel."

    edw "Effie, [povname]."
    edw "Do you guys copy?"

    eff "Loud and clear."

    pov "I’m listening."

    edw "Jacob’s inside Unit-B22. He says there’s a lot of clothes in there."

    eff "What kind of clothes, Jacob? Anything specific?"

    jac "Uhh..."
    jac "It’s hard to explain. They’re just... clothes. Lots of them."

    pov "Can you be more specific?"

    jac "Yeah, hang on."
    jac "They’re arranged weirdly, like complete outfits. Shirt, pants, socks, shoes, and even a set of underwear for each."

    edw "That is strange. Anything else?"

    jac "Actually, yeah."
    jac "Each outfit has a picture of someone wearing it attached to the bag."

    pov "What?"

    edw "Okay, that’s unexpected. Can you describe the layout? Are the outfits in bags or on hangers?"

    jac "They’re vacuum-sealed in bags. The whole setup looks... meticulous. Like someone cataloged them or something."

    eff "Are they running some sort of uniform program or something?"

    edw "Not that I know of. TRC handles uniforms differently, and I’ve never heard of a setup like this."

    pov "So this wasn’t a bust, then. There’s definitely something unusual here."

    jac "Should I dig around a bit more?"

    edw "Negative. I’ve got movement on the GPS logs—guards are on their way toward you."
    edw "Take a few pictures and get out. Meet us at the rendezvous point."

    jac "Alright, on it."

    edw "Effie, [povname], status?"

    eff "Waiting for the cameras to sweep."

    pov "Moving to the next checkpoint."

    edw "Copy that. Switching you both to single-channel comms. Let’s stay sharp."

    eff "Got it."

    pov "Understood."

    edw "Alright, on to the next step."

            #-BACK TO CHOICE MENU-
            #=CHOICE END=
    menu:
        "Effie" if not big_heist_choices_effie:
            $ big_heist_choices_effie = 1
            #-If “Effie.” was picked-

            edw "Effie, do you copy?"

            eff "Loud and clear, Edward."

            edw "How are you holding up?"

            eff "You want my honest answer or the sarcastic one?"

            edw "I, uh…"

            eff "Sigh."
            eff "Sorry about that, I’m just a bit on edge lately…"

            edw "Well, let’s be honest here, dude. Who could blame you after all of this?"
            edw "I mean… I know for a fact I would be like that too if I was in your shoes."

            eff "Yeah… It’s just…"
            eff "I guess I’m still struggling with the whole idea, you know?"
            eff "I mean, holy shit dude… Imagine remembering something with such vivid detail only for everyone to tell you it didn’t happen and you just made it all up or had a nightmare because of the situation…"
            eff "To the point you even come to believe it yourself."

            edw "It must be horrible…"

            eff "I spent so many years telling myself that I never saw that woman when i was a kid."
            eff "That despite my nightmares and constant flashbacks of that night, she was just a figment of my childlike brain trying to make sense with the fact my mom straight up and left."
            eff "But now that I know it actually happened, I…"
            eff "I’m finding myself with a lot of newly found feelings and emotions…"
            eff "I need to get to the bottom of all of this, especially now that I’m not a little girl who doesn’t know any better."

            edw "Hey, that’s why we are here, dude."
            edw "We all want to get to the bottom of it with you."

            eff "I know and you have no idea how much I appreciate it you guys for it."

            edw "Oh, but I’ll bet you are extra appreciative of [povname], huh?"

            eff " Well, yeah… I mean, without him and his information we wouldn’t be here at all, you know?"

            edw "Oh come on dude, you know what I mean!"
            edw "He may not get the full picture of it because he hasn’t known you as long as Jacob and I do, but we can totally call your signs!"

            eff "I-I don’t know what you are talking about!"
            eff "And this isn’t the time to be gossiping dude!"

            edw "Sorry, sorry. Just trying to keep your mind from overthinking itself to death and get you to focus."

            eff "I appreciate it but there are definitely better ways to do it!"
            eff "A-Anyway’s, I’m using the card to enter my unit now!"

            edw "Luckily you and [povname] are close by to each other and the storage garage so with any luck, We’ll be home before the change of guard shift."

            eff "Yeah, no kidding. I want to get rid of these cards as soon as possible."
            eff "Now where’s the damn light switch?"
            eff "Oh, by the way, should we come with a group alibi or something just in case?"

            edw "Probably a smart move considering the circumstances."
            edw "We could probably claim we were hanging out in one of our houses or just on the way to testing out my drone in some drills or something, right?"

            eff "…"

            edw "Right, Effie?"

            eff "…"

            edw "Effie?"

            eff "…"

            edw "Oh crap, not this shit again!"
            edw "I’m getting everyone on the channel, hang on!"
            edw "Guys?! Guys, do you copy?!"

            jac "Yeah dude, I’m here."

            pov "I can hear you, what’s up?"

            edw "Somethings wrong with Effie, she is not responding!"

            jac "Wait, what?!"

            pov "Oh shit, I’m just a few units away from her, I can rush in there and-"

            eff "N-No, No, you guys. It’s fine."
            eff "I’m alright."

            jac "Oh thank god…"

            edw "Dudes, you have to stop freaking scaring me like that, Jesus Christ!"
            edw "It’s happened two times with you guys already and both times I’ve felt like my life expectancy has been reduced by 5 years each time!"

            pov "What happened, Effie?"

            eff "I…"
            eff "I was just in shock as to what I was seeing to be honest with you…"
            eff "In fact I’m still a bit in shock…"

            pov "What do you mean, what are you seeing?"

            eff "It’s… some kind of machine?"
            eff "Or maybe a chair… I… I honestly don’t know how to describe it so I’ll just send you guys a picture."

            pov "Y-Yeah, that would probably be for the best."

            #-Scene now shows a new window pop up on Edward’s display that shows what Effie is seeing-
            #-The image depicts a large futuristic looking Tantra Chair (one of those curvy kamasutra sex couches) hooked up to several different types of tubes and wires in a similar manner to the Matrix Broadcast Chair or a H. R. Giger machine piece. The chair has arm and leg cuffs to tie up someone in a specific position and restrain their movements. A series of screens depicting random information in pie charts and the like along with monitoring things like battery levels and other information in #that regard. Finally, it comes with several dildo like attachments on the bottom aiming at where a woman’s privates would be if they were sitting on the chair of different dimensions, lengths and girths. It overall has a terrifying or roughly put together look to it-
            #-This is Vi’s charging and repair station in this world but the group hasn’t realized it yet-
            show bg thebigheist_2

            jac "…"

            edw "…"

            pov "…"

            eff "…"
            eff "Yeah, now you get my reaction…"

            jac "That’s… What the hell is that, Edward?"

            edw "I… I don’t know…"

            jac "I thought you were familiar with all the projects of this company!"

            edw "I-I mean, I am but this is definitely new!"
            edw "Definitely never seen it before in my TRC forums or heard anything about it…"
            edw "Hell, I can’t even make heads or tails of what it actually is!"

            eff "Well, Any guesses?"

            edw "If you asked me just from looking at it?"
            edw "I’d say it’s some kind of highly advance, likely illegal in most states, highly fetishistic and probably japanese fuck machine."

            pov "What makes you think it’s japanese?"

            edw "Because that shit looks straight out of a horror hentai manga or something, I mean look at it!"

            eff "What could they possibly want with a machine like this?"

            jac "Maybe some of the staff likes to party extra hard?"
            jac "I mean, I always wondered what the female equivalent of Cock and Ball Torture would be like."
            jac "Now I know it’s being strapped to that thing and letting the machine do it’s thing."

            eff "Definitely not the time for jokes, Jacob!"

            pov "Well, what else do you see in there, Effie?"

            eff "Gimme a second, I don’t want to get too close to this thing…"
            eff "Nothing guarantees me some wire won’t snap and wrap itself on my arm and pull me into the chair or something…"

            jac "At this point, that’s honestly a reasonable fear to have…"

            eff "Hang on, I found some documents here…"
            eff "Some kinds of progress reports or evaluation summaries?"
            eff "I can’t make tails or heads of it so I’ll take some pictures and send it to you so we can look them over later, Edward."

            edw "Alright, sounds like a plan."

            eff "I don’t want to be here any more than I have to, this whole place has some bad vibes to it, man…"

            edw "I’ll bet, alright. Do that and once you are out head to the meeting point"

            eff "Understood."

            edw "Jacob, [povname]. You guys are still moving, right?"

            pov "As quietly as I can, yes."

            jac "I’m making my way downtown, walking fast, faces pass and I’m dodging cameras."

            edw "What?"

            jac "Nevermind. Yes, I’m on the move."

            edw "Alright… Well, I’ll put you back on single channels and keep monitoring your progress and contact you once you are near your objectives."

            pov "Understood."

            jac "Over and out!"

            edw "OK, on to the next step."

            #-BACK TO CHOICE MENU-
            #=CHOICE END=
        "[povname]."if not big_heist_choices_pov:
            $ big_heist_choices_pov = 1
            #-If “[povname].” was picked-

            edw "[povname], do you hear me?"

            pov "I hear you, Edward."
            pov "I’m closing in on Unit R-04."

            edw "So I can see from the GPS tracking, how are you holding up, dude?"

            pov "I’m trying not to think about it too much."

            edw "You good?"

            pov "It’s just… I don’t know what we are hoping to find here but something tells me I’m not going to like it."

            edw "You are that sure of it?"

            pov "After all I’ve been through?"
            pov "I’d say it’s a very safe guess at this point."
            pov "Nothing’s ever as simple as it seems at first in my life."
            pov "Even now that I'm using the card on the door, I feel like things are just gonna get more and more complicated."

            edw "Well, you do go out of your way to help other people so it’s natural you get into all kinds of situations, right?"

            pov "I’m not sure if that's a good or bad thing anymore, all things considered."
            pov "Especially with the whole…"

            edw "The Sex World thing?"

            pov "Well.. Yeah…"

            edw "I’ll be honest dude, I’m still not a hundred percent sure I believe you on that part, but I can definitely tell you’ve been through some shit."
            edw "I mean, there’s no denying the whole lady in the lake thing after all."

            pov "I still don't know if I would have preferred the Sex World being real or her actually stalking me for God knows what…"
            pov "She made it clear she was coming for me and if the Sex World is real, then it's for nothing good…"

            edw "Well, now you are not on your own and we can figure it out, dude!"
            edw "Effie has her own personal stakes against her, Jacob isn't gonna leave you on your own, and this is the most exciting thing I've done in years and I'm definitely sticking around to see how it ends!"
            edw "So just focus on the fact that you don't have to deal with it all by yourself anymore or keep it a secret."
            edw "So just rely a little more on your friends and stop keeping everything to yourself."
            edw "I know you go around helping people and getting them what they need and all, but you can always ask for help too, you know?"

            pov "I…"
            pov "Thanks Edward, I think I really needed to hear that right now."
            pov "Anyway, I'm entering the room now."

            edw "What do you see?"
            edw "The light switch should be somewhere by the entrance."

            pov "I… don't think that's a problem…"

            edw "How so?"

            pov "The light is already on…"

            edw "What?"

            pov "I'm peeking inside but there doesn't seem to be anybody in…"

            edw "And what do you see?"

            pov "It's… some kind of office or something?"
            pov "Definitely not what I expected to find inside a storage unit, that's for sure…"
            pov "I can see several of those large pin boards, a desk with a bunch of files… Hang on, I'm gonna get a little bit closer and take some pictures."

            edw "Alright, do that while I get the others on the channel.."

            pov "Yeah, ok…"

            edw "Effie, Jacob. Come in, over."

            jac "I'm here!"

            eff "I just hid in an adjacent unit, what's up?"

            edw "[povname] just entered his unit and is about to show us what he found."

            jac "Alright, nice job, dude!"

            eff "Found anything of interest?"

            pov "I…"
            pov "You could say that, yeah…"

            eff "What's wrong?"

            pov "Well… Where do I begin?"
            pov "Guess I'll send this one first…"

            edw "Alright, let me pull up the GPS display for the others."

            #-Scene now shows a new window pop up on Edward’s display that shows
            # what the Mc is seeing- (adjusted for Edward receiving text/image data)-

            #-Scene depicts a large pin board with a bunch of papers scattered around
            # the edges, on the center of it however there is a map of the whole
            # town with some of the buildings crossed with a red cross, while areas
            # like the beach, park and police station have a red circle around.
            # Some of the roads have red lines that connect them with those areas
            # and others such as the church and the mall-

            #-The red lines indicate the underground tunnels that the Sex World
            # cult uses to move around undetected while the circles indicate the
            # location of portals to Sex World but the gang doesn't know that yet-
            show bg thebigheist_3

            eff "What the hell?"

            edw "That's a map of the whole town right?"
            edw "But all those crosses and circles…"

            jac "Please, Lord in heaven, let those be markings indicating pirate treasure and not targets for bombs or some shit like that…."
            jac "Hell, I'll even take a drug smuggling route over that shit."

            eff "I really doubt it's something like that, Jacob."
            eff "Or well… at least I hope not…"

            edw "Well, I really doubt that's the case because what would those other lines on the roads mean then?"

            jac "Maybe routes on which to take said stuff?"
            jac "Whatever it is, it's giving me the creeps like no one's business, man!"

            eff "I can definitely see why that would have you worried, [povname]."

            pov "Oh, this isn't the cork board I'm worried about though…"
            pov "Remember when I said there's multiple cork boards in this room?"

            #-The image changes, to a new picture of a different pin board, sent from the MC’s device.-

            #-This next pin board is even more chaotic than the last, with pictures
            # of several different people listed as potential targets though it
            # doesn't explicitly say they are, the pictures show people of the
            # town such as some adults in the office or in uniform, some of them
            # have a red cross over them which indicates they have been taken.
            # (this could be a good chance to put in Patreon OC's or something in
            # that nature along with the random Easter egg? Or just keep them as
            # basic silhouettes) Along the pictures however are Edward's parents
            # and Davendithas' mother who was kidnapped along with his sibling,
            # she is one of the pictures who has a red cross over them-
            show bg thebigheist_4

            eff "Oh…"

            jac "And the creep factor managed to somehow skyrocket past what I assumed was the limit once again…"
            jac "I'm honestly thinking I'm going to get desensitized to being creeped out by the time the night ends, you guys…"

            pov "Do you guys recognize anyone in these pictures?"

            eff "Well… Yeah, I mean some of them I think I've seen crossing the street or at the mall I think…"
            eff "Why do only some have that red X on them?"

            jac "Woah! One of them is of Davendithas' mom!"
            jac "She has a red X on it!"

            pov "Wait, Davendithas' Mom was one of the people that were taken in the kidnapping case, right?"

            jac "Yeah… her along with his little brother…"

            eff "You are not suggesting that maybe…"

            pov "I mean, if the glove fits…"

            jac "Oh, boy. What have we gotten ourselves into?"

            pov "I don't know anymore man, your guess is as good as mine at this point."
            pov "What about you, Edward?"
            pov "You haven't said anything yet, what do you think of all this?"

            edw "…"

            pov "Edward?"

            jac "Come on, Ed-boy. Our computer guy can't go quiet on us!"

            eff "Edward, is everything okay?"

            edw "…"
            edw "Those pictures…"

            jac "What about them, dude?"

            edw "Two of them are of my parents…"

            eff "Wait, what?!"

            jac "Oh, holy shit! I just noticed them too!"
            jac "But they don't have red X's on them!"

            edw "Does that mean they are still targeting them?"
            edw "I mean… if we go by the logic that the red cross means that they've disappeared, then that means anyone on this pin board could be next, right?"
            edw "And that means they must be coming after my parents too, like they did with Davendithas…"

            eff "Edward, listen to me."
            eff "It's too soon to make any assumptions and even sooner for us to crumble down."

            edw "Crumble down?"
            edw "Dude, I'm fucking pissed!"
            edw "Who the fuck do these people think they are trying to target my parents?!"
            edw "Oh, they messed with the wrong Gadget Man, I assure you!"

            jac "Alright, alright. I'm loving the hyped up confidence coming from anger, but remember you are still supposed to be hiding!"

            eff "Look, we can go over all our evidence and share our feelings later, we need to focus right now and for that we need you on your A game, Edward!"

            edw "Oh, you are not getting just my A game anymore, guys."
            edw "You getting full on Smokey Sexy Style up in here!"
            edw "I'll start looking over the town records and try to bring names to the pictures with a red cross in them."

            eff "Alright, that's what I'm talking about!"
            eff "[povname], if there'd nothing else of interest, you should really get out of there."

            pov "Uhh… there definitely is…"

            eff "Wait, there's actually more?"

            pov "Remember when I said I was certain I've been stalked recently and you just started to believe me?"
            pov "I'm starting to really fucking hate when I'm right and the more I prove it to you guys that I am…"

            #-Image changes one final time, to the last pin board picture, on
            # Edward’s display that shows what the MC is seeing-

            #-For this last one image, the pin board goes full Pepe Silvia levels
            # of chaos with multiple pictures of the MC taken from afar in a variety
            # of situations along with papers detailing random information, all
            # of them circulating a larger picture of him in black and white with
            # multiple red circles around his face along with similar graffiti
            # such as hearts and the like across the others in a full stalker vibe-
            eff "Oh…"

            edw "My…"

            jac "Sweet God…"

            pov "Safe to say, you guys believe me now, right?"

            eff "I… ah…"

            jac "What in the actual fuck is all this?!"

            pov "The reason I've been having constant panic attacks and been on edge as all fuck for a while now."

            edw "I mean… With good reason, holy shit…"
            edw "Dude they got everything on you…"
            edw "Usual routine with time-frames, your usual hanging out spots, the times you get back home…"

            jac "Even the times you take a shower or go to the bathroom!"

            pov "I told you guys! I freaking told you!"

            eff "I… Why are they so obsessed with you in the first place?!"

            pov "Because they wanted to gut me like a pig in some kind of weird sex ritual and I bolted the hell out of there as soon as I could!"

            edw "If they wanted you so badly then why haven't they taken you yet?"
            edw "I mean, with the amount of information they have on you here, they could have easily taken you in the middle of the day if they wanted to and no one would have been able to tell you are missing for hours!"

            pov "Gee, thanks a lot for the thought, dude!"

            edw "I'm just saying, they have everything they need. Why haven't they taken you yet?"

            jac "Maybe they are preparing to do it soon then?"
            jac "Who knows how old this information is."

            pov "You guys are not helping!"
            pov "Jesus Christ, what do I do with all of this?! Should I take it all down or something?"

            eff "NO!"
            eff "No, no, no, no, no. That is a bad idea!"
            eff "We can't leave any evidence that we were here in the first place!"
            eff "You taking down their whole stalker board is surely going to be noticed and if they find further evidence we were here then we lose the element of surprise and we end up truly fucked!"

            pov "Then what do I do with this shit?!"

            edw "I have all their information on my system now, dude. Once you guys come back we can figure out a way to break up your routine and keep them from monitoring you."
            edw "I can also give you something to defend yourself or we can group up to make sure you are always accompanied."
            edw "But unless we get to the bottom of this, then we are just delaying them."
            edw "We need to keep our heads cool and avoid panicking."

            pov "I… You are right…"
            pov "You are right, you are right…"
            pov "It's just… God, I just started working at the TRC and I don't know how involved they are in all of this shit…"

            eff "You'll need to keep an extra eye out for now, but if they are involved then they could have taken you anytime now and you wouldn't have expected it."
            eff "They are clearly waiting for something to happen or for some sort of signal before they actually try to take you…"

            edw "We can figure out what it is later but for now you need to get out of there, [povname]."
            edw "I'm seeing the heat signal of a guard approaching your location and you could lose your window to get out if they reach you."

            pov "R-Right… Right…"

            edw "Effie, Jacob. You guys are clear to keep going but remember to watch your step."
            edw "I know this whole situation just got super personal for all of us but we need to keep moving or we won't have a chance to fix it before it's too late."

            eff "Understood."

            jac "Jesus Christ, what did we truly get ourselves into…"

            pov "I don't know anymore, man…"
            pov "I don't know anymore…"

            edw "I'm putting you all back on single channel now. Keep an eye out and I'll keep in touch."
            edw "OK, on to the next step."

            #-BACK TO CHOICE MENU-
            #=CHOICE END=
            #=END=
    #=CHOICE END=

    #-Once a choice is made the scene will play out until conclusion and if there
    # are remaining options the player will be returned to the choice menu to
    # pick a different character with the exception of the character they already
    # chose. Once all options all exhausted, the scene will continue-


    if 0 in (big_heist_choices_jacob,big_heist_choices_effie,big_heist_choices_pov):
        jump menu_big_heist_choices



    #-Once all options are exhausted the scene will continue-
    scene bg thebigheist_1
    
    edw "Guys, I'm putting you back on the group channel. That's all of the single storage units done so we can move on to step two."
    edw "Meet up at the rendezvous point and we can finish up at the storage garage together and then get the hell out of here."

    eff "Copy that."

    pov "What a fucking crazy night, I can't wait for it to end…"

    edw "Jacob, you are still at the farthest point available of the whole group, how fast do you think you can get back to Effie and [povname]?"

    jac "Gonna be honest with you man, I'm having a bit of a situation right now!"

    pov "What do you mean?"

    eff "Jacob are you okay?"

    jac "Well, health wise yeah, but I'm a little bit pinned at the moment by some security guards and I can't seem to find a window out!"

    edw "Oh, crap! One of them must have been taking their break inside one of the units or something!"

    jac "With everything we have found, it wouldn't surprise me if one of these units actually has a couch or a lounge area or something."
    jac "Edward what do I do?!"

    edw "Alright, Alright. Don't panic just yet, dude!"
    edw "Effie, [povname]. Where are you guys at?"

    eff "I just met up with him at the rendezvous point next to the Storage Garage."

    pov "Should we wait for Jacob?"

    edw "No, it's too risky to keep you guys in the open and if a guard patrol comes around you guys then we could very well lose our chance!"
    edw "The two of you should go ahead and start looking around the storage garage."
    edw "You'll be on your own for a bit while I focus on Jacob and guide him out of the guards path and back towards you guys."

    pov "I don't feel that comfortable leaving Jacob behind like that, dude…"

    jac "It's alright, man! I got Edward watching my back."
    jac "Worse case scenario we can buy you guys some time or cause a distraction or something if you need it."

    eff "You sure about this, Jacob?"

    jac "Dudes, we have no time to argue about this!"
    jac "After all we found, we know we are in some deep shit and who knows what they are storing in such a large garage."
    jac "Now the three of you have stakes on all of this with Effie's Mom going missing, Edward's parents apparently being on the target list and the whole stalker board they have on [povname]."
    jac "I ain't about to drag the team down so make the most of it while I get over there and let me know if I can help from this side!"

    eff "Jacob…"
    eff "You are the best."
    eff "Alright you heard him, [povname]. Let 's get going!"

    pov "Right, we are heading into the storage garage now."

    edw "Setting you to single channel between the two of you."
    edw "You guys are on your own now, be careful and remember to collect any evidence of what you see."

    eff "Right, you guys be careful too."
    eff "Especially you, Jacob!"

    jac "I'll be fine, let's just hurry and get out of here as soon as possible, alright?"


    edw "Over and out."

    $ main_story = 119

    scene black with fade

    jump lbl_the_pods
