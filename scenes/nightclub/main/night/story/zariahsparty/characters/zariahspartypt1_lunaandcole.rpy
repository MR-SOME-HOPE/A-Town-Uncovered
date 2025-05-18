## LUNA AND COLE
label lbl_zariahs_party_luna_and_cole:
    #-Luna and Cole are in the middle of a conversation or rather Luna is mid-talking about some pretty gruesome topics as the Mc joins in, she is happy to see him and happily strikes a conversation with him. Cole on the other hand looks absolutely traumatized as if he has acquired Eldritch knowledge and his mind can’t truly wrap itself around the fact. He is definitely regretting trying the “Cole Charm” on Luna-
    if zariahs_party_talking_luna_and_cole == 0:
        show lun bored_talk at Position(xpos=1200)
        show col bored at Position(xpos=1700)
        with dissolve
        lun "-And that’s only one of the many beneficial treatments used to this day that contain the use of live maggots."
        show lun smirk_talk at Position(xpos=1200)
        lun "They can be quite the beneficial little things."
        show lun bored_talk at Position(xpos=1200)
        lun "Moving on in the list of fun party facts, in number 47we have the rather interesting method of ancient Persian execution known as “Scaphism” which used the fascinating combination of milk, honey and two boats that trap the victim all with the objective in mind to-"

        #-Luna notices the Mc and stops her conversation-
        show pov neutral at left
        with dissolve
        show lun smirk_talk at Position(xpos=1200)
        lun "Oh Greetings, [povname]."
        show pov embarrassed at left
        show lun smirk_talk at Position(xpos=1200)
        lun "Do you also wish to join us in my sharing of fun party facts?"
        show pov embarrassed_talk at left
        show lun smirk at Position(xpos=1200)
        pov "Hey, Luna."
        pov "And uhh… fun party facts?"
        show pov embarrassed at left
        show lun neutral_talk at Position(xpos=1200)
        lun "Just an accumulation of interesting trivia of some topics of my preference."
        show lun confused_talk at Position(xpos=1200)
        lun "Why I had just started with number 47 when you showed up and snapped me out of it."
        lun "I usually try to keep things to around number 23 or so."
        show lun bored_talk at Position(xpos=1200)
        lun "It tends to be a lot for people but he’s taken it well."
        show pov embarrassed_talk at left
        show lun confused at Position(xpos=1200)
        pov "How are you feeling, Cole?"
        show pov confused at left
        show col shocked_talk at Position(xpos=1700)
        col "…"
        show pov confused_talk at left
        show col shocked at Position(xpos=1700)
        pov "Cole?"
        pov "Dude, are you okay?"
        show pov confused at left
        show lun bored at Position(xpos=1200)
        show col shocked_talk at Position(xpos=1700)
        col "…"

        #-Upon closer inspection, you can see that the horrified look on his eyes also reveals a lack of focus in his surroundings, he’s passed out from terror with his eyes open-
        show pov shocked_talk at left
        show lun embarrassed at Position(xpos=1200)
        show col shocked at Position(xpos=1700)
        pov "Oh damn, I think he’s out cold…"
        show pov shocked at left
        show lun bored_talk at Position(xpos=1200)
        lun "Oh dear, it happened again…"
        show pov shocked_talk at left
        show lun confused at Position(xpos=1200)
        pov "Is he going to be okay?!"
        show pov confused at left
        show lun embarrassed_talk at Position(xpos=1200)
        lun "Y-Yes, it seems that the topic of conversation was a bit too much for him."
        lun "People have different levels of tolerance when it comes to my fun facts."
        show pov shocked at left
        show lun confused_talk at Position(xpos=1200)
        lun "Just give him some time for him to readjust himself."
        show pov bored_talk at left
        show lun confused at Position(xpos=1200)
        pov "Uhh… Perhaps you should practice more small talk over your fun facts…"
        show pov bored at left
        show lun embarrassed_talk at Position(xpos=1200)
        lun "Oh, but he seemed so interested in the beginning!"
        lun "Why, with the way that he approached me and seemed so dedicated to holding a conversation with me, I was certain he could last a little bit longer than that."
        lun "The last time it got too much for someone they fainted, after all."
        show pov bored_talk at left
        show lun confused at Position(xpos=1200)
        pov "Luna, I think he passed out with his eyes open…"
        show pov bored at left
        show lun shocked_talk at Position(xpos=1200)
        lun "Oh my, no wonder he was stuck in the same pose for 30 minutes now…"
        show pov confused_talk at left
        show lun shocked at Position(xpos=1200)
        pov "How long ago did you two start talking, again?"
        show pov shocked_talk at left
        show lun embarrassed_talk at Position(xpos=1200)
        lun "Around 35 minutes or so?"
        lun "And now that I say that outloud, I realize how I’ve been talking to myself for a while now and I rather do that when people are not around."
        show pov embarrassed_talk at left
        show lun embarrassed at Position(xpos=1200)
        pov "I-I’m sure it wasn’t his intention."
        show pov embarrassed at left
        show lun bored_talk at Position(xpos=1200)
        lun "It doesn’t matter, the information was stored in his brain even in his half-conscious state, so my indepth ramblings about different methods of torture and other fun facts shall lurk within the deep corners of his subconcious and come back into his active thoughts during moments of great stress."
        lun "I shall take that as the appropriate comeuppance for making me talk by myself."
        show pov shocked_talk at left
        show lun confused at Position(xpos=1200)
        pov "Good god, Luna…"
        show pov shocked at left
        show lun embarrassed_talk at Position(xpos=1200)
        lun "But now that I think about it, isn’t it kind of cool that I now know I can have this effect on people?"
        show lun smirk_talk at Position(xpos=1200)
        lun "Sharing my eldritch knowledge to forever mark the curious victims who try to tempt fate…"
        show pov bored at left
        show lun embarrassed_talk at Position(xpos=1200)
        lun "It has a lovecraftian vibe to it, doesn’t it?"
        show pov bored_talk at left
        show lun smirk at Position(xpos=1200)
        pov "Okay, we need to change the subject right now before you turn into a supervillain."
        show pov confused at left
        show lun smirk_talk at Position(xpos=1200)
        lun "Why?"
        lun "Does the idea of that scare you?~"
        show pov bored_talk at left
        show lun smirk at Position(xpos=1200)
        pov "Considering the fact you can seemingly disappear at will and no one knows how you do it, then yes, it absolutely does."
        show pov bored at left
        show lun smirk_talk at Position(xpos=1200)
        lun "{i}*giggle*{/i} Well, at least you are honest about it."
        lun "Sorry, I really don’t know how you are supposed to behave at big events like this."
        show pov bored_talk at left
        show lun embarrassed at Position(xpos=1200)
        pov "..."
        show pov bored at left
        show lun neutral_talk at Position(xpos=1200)
        lun "Zariah asked me to take pictures during the event to upload on her site."
        show pov confused at left
        show lun bored_talk at Position(xpos=1200)
        lun "Kind of hard to look for spots to take all the action without being spotted when you are also worrying about conversation topics with people."
        lun "That's why I always default to my fun party facts for any social interaction outside of my party plans."
        show pov confused_talk at left
        show lun confused at Position(xpos=1200)
        pov "How often do you go to parties, again?"
        show pov smirk at left
        show lun bored_talk at Position(xpos=1200)
        lun "Just to the ones Zariah invites me and I usually try to stick around with her most of the time."
        lun "Large crowds can make me nervous so I either cling to her or find a place to hide for a while."
        show pov smirk_talk at left
        show lun shocked at Position(xpos=1200)
        pov "And are you gonna be okay taking pictures when you are going to be within the crowd to get them?"
        show pov smirk at left
        show lun bored_talk at Position(xpos=1200)
        lun "I’ll have the camera to keep my mind off it, so please try not to remind me."
        lun "Besides, I’ll make sure people don’t even notice me, so there won’t be any eyes on me to make me feel nervous!"
        show pov shocked_talk at left
        show lun bored at Position(xpos=1200)
        pov "Just promise you’ll be careful enough not to get trampled if it turns into a mosh pit or something."
        show pov confused at left
        show lun bored_talk at Position(xpos=1200)
        lun "That’s why I asked Zariah for her playlist ahead of time, I know which songs to be careful at and which to look for a safer angle entirely."
        lun "It’s gonna be a fun challenge."
        show pov smirk at left
        show lun neutral_talk at Position(xpos=1200)
        lun "Stick around and I’ll even take your picture."
        show pov smirk_talk at left
        show lun smirk at Position(xpos=1200)
        pov "Sure thing!"
        show pov embarrassed_talk at left
        show lun shocked at Position(xpos=1200)
        pov "So uh… should we do something with Cole?"
        show pov embarrassed at left
        show lun smirk_talk at Position(xpos=1200)
        lun "Oh, he’ll be fine, don’t worry too much about it."
        show pov confused at left
        show lun neutral_talk at Position(xpos=1200)
        lun "I have to start preparing my stuff so, I’ll see you later, [povname]."
        show pov embarrassed at left
        show lun smirk_talk at Position(xpos=1200)
        lun "Though I make no promises that you’ll be able to see me~"

        #-Luna quickly flees away from the the scene-
        show pov confused_talk at left
        hide lun smirk at Position(xpos=1200)
        with dissolve
        pov "And she is gone into the shadows again…"

        #-The Mc turns back to the still frozen Cole-
        show pov embarrassed_talk at left
        show col shocked at right
        with dissolve
        pov "Alright, big guy, let’s find you a booth to sit in."
        show pov embarrassed at left
        show col bored_talk at right
        col "The horror…"
        show pov shocked_talk at left
        show col bored at right
        pov "Wait, you are awake?!"
        show pov shocked at left
        show col confused_talk at right
        col "Why?"
        col "Why would someone invent a device design to take the nuts off a bro?"
        col "Why did people want other people’s nuts in the first place?"
        show pov confused_talk at left
        show col bored at right
        pov "So you did hear all of her facts…"
        show pov confused at left
        show col bored_talk at right
        col "I lost a part of myself today, dude…"
        col "Is there something in the bro code that allows a bro to request a hug from another bro after his mind is soiled beyond belief?"
        show pov embarrassed_talk at left
        show col embarrassed at right
        pov "Okay, let’s get you something to drink at the bar, perhaps you can convince Steven to give you something to kill off the brain cells with your memories of the whole thing."
        show pov embarrassed at left
        show col sad_talk at right
        col "I would like that very much, thank you…"

        #-The Mc and Cole leave the scene-
        hide pov embarrassed at left
        hide col sad at right
        with dissolve
        #=RESULT END=

        $ zariahs_party_talking_luna_and_cole = 1

    else:
        pov "I'll let them enjoy the party."
    jump lbl_nightclubdancefloor_zariahs_party_setup
