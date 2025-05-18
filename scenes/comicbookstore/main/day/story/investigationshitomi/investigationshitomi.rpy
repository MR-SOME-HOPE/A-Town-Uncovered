#Comic Book Shop
#-In this scene the player talks to the characters located in the Comic Book Shop, This character are Jacob, Hitomi, Lord Kevlamin and Crugeon-

#-Jacob will not be available to talk unless the player has interacted with Effie first-

#[Comic Book Shop, afternoon - “Investigations_Hitomi”  - main_story =84-M]

#-Mc approaches Hitomi at the counter as she works writing on a notepad-
label lbl_investigations_hitomi:
    show btn_comicbookstore_day_hitomi_idle2
    if gtime == 1:
        show btn_comicbookstore_day_jacob_idle2
    $ renpy.pause(0.001)

    if investigations_hitomi != 0:
        pov "{i}She's already told me everything she knows.{/i}"
    else:
        default investigations_hitomi = 0
        show pov neutral_talk at left
        with dissolve
        show hit neutral at right
        hide btn_comicbookstore_day_hitomi_idle2
        with dissolve
        pov "Hi, Hitomi."
        show pov neutral at left
        show hit neutral_talk at right
        hit "Hey, [povname]."
        show pov embarrassed at left
        show hit smirk_talk at right
        hit "Gimme a sec, I’m trying to run some numbers over here."
        show pov embarrassed_talk at left
        show hit smirk at right
        pov "Working hard or hardly working?"
        show pov neutral at left
        show hit smirk_talk at right
        hit "Sometimes I’m not even sure myself."
        hit "But if numbers keep getting closer to the red mark, then I may not be working at all…"
        show pov confused_talk at left
        show hit smirk at right
        pov "Are things that bad?"
        show pov confused at left
        show hit smirk_talk at right
        hit "It is sadly one of the things that are common with comic book shops nowadays."
        show pov embarrassed at left
        show hit bored_talk at right
        hit "Mostly because most people read their comics online or even buy their merch online."
        hit "We mainly sell the experience of location based geekness."
        show pov bored at left
        show hit shocked_talk at right
        hit "It’s why the manager allows the guys to read some of the comic books and the like."
        show hit bored_talk at right
        hit "Prompts people to stay which makes them more likely to buy or something."
        show pov confused_talk at left
        show hit bored at right
        pov "How's that working for you all so far?"
        show pov confused at left
        show hit bored_talk at right
        hit "Well, as you know by now, we have a bunch of nerds sorta living in the back of the store and they made a card game club."
        show hit angry_talk at right
        hit "Problem is that their leader is a bit elitist on who gets to play and scares newcomers away."
        show pov confused_talk at left
        show hit bored at right
        pov "Not to mention the whole “Lord” roleplay thing going on."
        show pov confused at left
        show hit smirk_talk at right
        hit "That too."
        show hit shocked_talk at right
        hit "Good thing is that they pretty much pay half the rent for the place, so the manager isn’t about to kick them out anytime soon."
        show pov embarrassed at left
        show hit bored_talk at right
        hit "So, what can I do for you?"
        show pov embarrassed_talk at left
        show hit bored at right
        pov "Well, I figured I’d get more familiar with the town so I’m just asking around for interesting facts or stories about it."
        show pov neutral_talk at left
        show hit confused at right
        pov "Was hoping you would know anything interesting, actually."
        show pov neutral at left
        show hit confused_talk at right
        hit "Asking the girl who hangs out with weirdos all day if she knows anything strange?"
        show pov embarrassed at left
        show hit smirk_talk at right
        hit "I could write my own comic book series at this point with everything ive seen and heard coming out of the guys' mouths over my years here."
        hit "“Hitomi’s tales of the weeb and strange!”"
        show hit bored_talk at right
        hit "Too bad I don’t have a bod like Alvira to help sell it."
        show pov smirk at left
        show hit smirk_talk at right
        hit "I’m more like the gravekeeper from Tales from the Grave if anything."
        show pov smirk_talk at left
        show hit smirk at right
        pov "Oh come on, don’t say that."
        show pov embarrassed at left
        show hit bored_talk at right
        hit "Sorry, force of habit."
        show hit neutral_talk at right
        hit "Anyway, what would you like to hear?"
        show pov embarrassed_talk at left
        show hit neutral at right
        pov "Well, So far I’ve been a bit all over the place trying to get more familiar with the town history and interesting events around it."
        show pov embarrassed at left
        show hit confused_talk at right
        hit "What, did you finish binge watching your favorite show and have nothing left to do now?"
        show pov neutral at left
        show hit smirk_talk at right
        hit "I can recommend a few good shows on Cadabra Prime if you are that desperate for things to do."
        show pov neutral_talk at left
        show hit smirk at right
        pov "No, no. Trust me, this is not the kind of thing I would like to spend my free time on."
        show pov embarrassed_talk at left
        show hit confused at right
        pov "No, it’s for school work."
        pov "I guess it’s natural to assign the new kid on the block an essay about the town’s history."
        show pov embarrassed at left
        show hit smirk_talk at right
        hit "I can see the logic in it. Alright, I’ll help you out."
        show pov neutral at left
        show hit confused_talk at right
        hit "Anything specific you want to know about?"
        show pov neutral_talk at left
        show hit neutral at right
        pov "Well, things are strange enough nowadays so I was wondering more about stuff in the past."
        show pov confused_talk at left
        show hit bored at right
        pov "Does any of that ring a bell?"
        show pov confused at left
        show hit bored_talk at right
        hit "Well, a lot of guys make stuff up to try and make conversation with me or to just scare each other out."
        show pov embarrassed at left
        show hit angry_talk at right
        hit "You have any idea how many times they have told me either Mexican, Korean, or even Australian cryptids and ghosts just so happen to also be haunting our town now?"
        show pov embarrassed_talk at left
        show hit angry at right
        pov "Not even gonna take a guess."
        show pov smirk_talk at left
        show hit smirk at right
        pov "I already have enough problems as it is to also worry about foreign haunts. Plus, thing’s can’t haunt you if you don’t know they exist, right?"
        show pov smirk at left
        show hit smirk_talk at right
        hit "Hey, that’s not a bad way to think about it!"
        show pov neutral at left
        hit "May just use that line to save myself from another half hour narration."
        show pov shocked at left
        show hit smirk_talk at right
        hit "Anyway, ghosts aside, I think I do have something that might interest you."
        show pov neutral_talk at left
        show hit smirk at right
        pov "You do?"
        show pov neutral at left
        show hit neutral_talk at right
        hit "It’s not something people like to talk about around the town, so I recommend you be careful who you tell this too."
        show pov confused at left
        show hit bored_talk at right
        hit "Specially old people or adults who were around at the time."
        show pov confused_talk at left
        show hit smirk at right
        pov "Okay, you definitely have hooked into it now, what’s this about?"
        show pov neutral at left
        show hit smirk_talk at right
        hit "Well, rumor has it that years ago in this town, people would disappear all the time under mysterious circumstances."
        show pov confused_talk at left
        show hit smirk at right
        pov "You mean something similar to the one that recently happened?"
        show pov confused at left
        show hit smirk_talk at right
        hit "Oh no, not at all from what I know."
        show hit embarrassed_talk at right
        hit "What I mean is that people actually vanished without a trace only to return later in a daze, acting strange for a few days before vanishing again and reappearing a few days later in even more of a daze, having no recollection of being missing in the first place."
        show pov shocked_talk at left
        show hit embarrassed at right
        pov "That is pretty spooky."
        show pov smirk_talk at left
        show hit neutral at right
        pov "How do you know about all of this?"
        show pov shocked at left
        show hit smirk_talk at right
        hit "My father actually."
        show pov confused at left
        show hit shocked_talk at right
        hit "He is very superstitious so when this kidnapping happened, he went a bit psycho and had a panic attack."
        show pov shocked at left
        show hit embarrassed_talk at right
        hit "Once we managed to calm him down and stabilize him, he told me the story."
        hit "Apparently my grandparents disappeared for a whole month in this phenomenon."
        show pov confused at left
        show hit shocked_talk at right
        hit "When they came back, they were completely different people according to him."
        show hit confused_talk at right
        hit "They were once very strict and sometimes cruel to my dad, to the point of forbidding him from seeing my mother."
        show pov shocked at left
        show hit shocked_talk at right
        hit "But once they reappeared, they were completely changed!"
        show hit smirk_talk at right
        hit "Suddenly they were all loving and supportive, even invited my mom over for dinner and helped set them up on their first big date and all!"
        show pov shocked_talk at left
        show hit confused at right
        pov "Well, isn’t all of that a good thing?"
        show pov confused_talk at left
        show hit shocked at right
        pov "What about all of that could have your father in such a panic later on?"
        show pov confused at left
        show hit confused_talk at right
        hit "It’s not what happened then that had him scarred for life."
        show hit shocked_talk at right
        hit "It’s what happened after."
        show pov shocked at left
        show hit bored_talk at right
        hit "Once they disappeared again, they never came back."
        show pov shocked_talk at left
        show hit bored at right
        pov "Oh god…"
        show pov shocked at left
        show hit bored_talk at right
        hit "He waited and waited, they told him they would be back soon and how much they loved him."
        hit "He remembers how they seemed really sad when saying it, like it would be their last chance to say it or something…"
        show pov confused at left
        show hit shocked_talk at right
        hit "Turns out it was…"
        show pov shocked_talk at left
        show hit bored at right
        pov "Damn… I’m so sorry…"
        show pov sad at left
        show hit bored_talk at right
        hit "It’s alright."
        show hit embarrassed_talk at right
        hit "Despite the whole panic attack and trauma, it was quite nice to spend some time with my family like that."
        show hit sad_talk at right
        hit "He held me and my mom with an iron grip hug and just kept muttering how much he loved us."
        show hit confused_talk at right
        hit "I think he was afraid it meant it was his turn to leave as well or something."
        show pov shocked at left
        show hit sad_talk at right
        hit "He kept saying stuff like how he was s-sad he wouldn’t get to see me down the altar… O-Or how he was sorry he was so strict with me at times a-and-"

        ##-At this point Hitomi is visibly shaken up-
        show pov sad_talk at left
        show hit sad at right
        pov "Hey…"
        show pov embarrassed_talk at left
        show hit embarrassed at right
        pov "It’s alright… Do you need a minute, can I get you anything?"
        show pov embarrassed at left
        show hit embarrassed_talk at right
        hit "N-No, I’m sorry… I’m okay; it's just that I’m still a bit shaken up about all of it."
        show pov embarrassed_talk at left
        show hit embarrassed at right
        pov "I’m so sorry I even brought it up in the first place."
        show pov sad_talk at left
        pov "I shouldn’t have said anything."
        show pov sad at left
        show hit neutral_talk at right
        hit "It’s ok, really."
        show pov embarrassed at left
        show hit embarrassed_talk at right
        hit "You didn’t know and I made it more personal than it needed to be."
        show pov sad at left
        show hit sad_talk at right
        hit "J-Just give me a moment…"
        show pov embarrassed_talk at left
        show hit embarrassed at right
        pov "As many as you need."

        #-If Charisma is 10 or higher-
        if skill_cha >= 4:
            $ renpy.notify("You Used 4 Charisma Points")
            $ skill_cha -= 4
            show pov confused_talk at left
            show hit embarrassed at right
            pov "Isn’t there anything I can get you? Some water or…"
            show pov embarrassed_talk at left
            pov "Do you want a hug?"
            show pov embarrassed at left
            show hit embarrassed_talk at right
            hit "I-I…"
            show pov neutral at left
            show hit neutral_talk at right
            hit "I could use a hug, thank you…"

            #+1 Hitomi Rp
            if hitomi_points < 10:
                $ hitomi_points += 1
                $ renpy.notify("Your relationship with Hitomi has increased")
        #-Hitomi and the Mc embrace for a moment, her smiling as she finds comfort in his arms-
        #		=RESULT END=
        show pov embarrassed at left
        show hit embarrassed_talk at right
        hit "Sorry about that."
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "Hey, I completely understand."
        show hit neutral at right
        pov "I wouldn’t be any different if that had happened with my family instead."
        show pov neutral at left
        show hit neutral_talk at right
        hit "You are so nice, [povname]."
        show pov embarrassed at left
        hit "I appreciate it, truly."
        show pov shocked at left
        show hit embarrassed_talk at right
        hit "A-Anyway, back to the story."
        show pov embarrassed_talk at left
        show hit embarrassed at right
        pov "Only if you are sure."
        show pov neutral at left
        show hit neutral_talk at right
        hit "I am, thank you again."
        show hit embarrassed_talk at right
        hit "So, once we managed to get my dad to calm down, my mom sat me down and told me more about the whole thing."
        show pov confused at left
        show hit confused_talk at right
        hit "What happened to my parents was the first time people who vanished didn’t return."
        hit "People were used to others disappearing in a more innocent manner."
        show pov shocked at left
        show hit smirk_talk at right
        hit "Getting lost in the outskirts of town or just wandering in the night after a fight with the spouse or something like that."
        show hit shocked_talk at right
        hit "Nothing that wouldn’t get fixed after a few days with people wandering back into town in a bit of a daze."
        show pov shocked_talk at left
        show hit smirk at right
        pov "Because that’s not concerning…"
        show pov confused at left
        show hit smirk_talk at right
        hit "Oh, it was!"
        show hit shocked_talk at right
        hit "People were thinking something was in the water or gas was leaking out and making people dumb or something."
        show pov shocked at left
        show hit smirk_talk at right
        hit "There were even a bunch of old people who thought punks were hypnotizing the population with their loud music and grunge attitude."
        show hit bored_talk at right
        hit "But regardless, people always came back eventually and there wasn’t much of a mess made."
        show pov confused at left
        show hit shocked_talk at right
        hit "Just people walking out one night and coming back in a few days."
        show pov confused_talk at left
        show hit shocked at right
        pov "But then things got worse didn’t it?"
        show pov confused at left
        show hit shocked_talk at right
        hit "What happened with my grandparents was only the beginning."
        show hit confused_talk at right
        hit "People were already scared and cautious because of it. But then one day, someone returned in a panicked state."
        show pov shocked at left
        show hit angry_talk at right
        hit "Spouting off nonsense and beyond paranoid. Claiming about something about “The Other Side” and about a “Harvester of men”"
        show hit confused_talk at right
        hit "No one could make sense of them and they were quickly taken into custody somewhere secure until they could calm them down enough to be talked some sense into."
        show pov confused at left
        show hit smirk_talk at right
        hit "But that's when the real trouble started."
        show pov confused_talk at left
        show hit smirk at right
        pov "What do you mean?"
        show pov confused at left
        show hit smirk_talk at right
        hit "Soon after they were taken into custody, the disappearances turned violent and even more mysterious."
        show pov shocked at left
        show hit shocked_talk at right
        hit "Homes were getting ransacked and broken into, traces of a struggle often left behind, No clues or fingerprints either."
        show hit bored_talk at right
        hit "Almost as if some ghost or force rushed in and left without a trace."
        show pov smirk_talk at left
        show hit smirk at right
        pov "That sounds way too familiar…"
        show pov embarrassed at left
        show hit smirk_talk at right
        hit "No kidding."
        show pov confused at left
        show hit bored_talk at right
        hit "The worst part was when the messages started to appear."
        show pov shocked_talk at left
        show hit smirk at right
        pov "Messages?"
        show pov shocked at left
        show hit smirk_talk at right
        hit "The more people vanished, odd messages started to appear in town."
        show hit bored_talk at right
        hit "Ramblings and random notes left by the assailants as if they were taunting the police."
        show pov confused at left
        show hit confused_talk at right
        hit "What was concerning though, is that those ramblings were similar to the ramblings that the person in custody made."
        show pov angry_talk at left
        show hit confused at right
        pov "Who was this person?"
        show pov angry at left
        show hit angry_talk at right
        hit "That’s the weirdest part!"
        show pov shocked at left
        show hit shocked_talk at right
        hit "No one outside of the main investigation team and the victim’s family knew their identity."
        show hit smirk_talk at right
        hit "The fact someone returned to begin with, was the only thing that was leaked to the press, but the police kept a tight lip regarding their identity."
        show pov confused_talk at left
        show hit smirk at right
        pov "Sounds a little hard to believe that it wasn’t leaked out."
        show pov confused at left
        show hit bored_talk at right
        hit "I told my mom the same thing."
        show pov embarrassed at left
        show hit shocked_talk at right
        hit "She just emphasized how back then things were not as convenient in terms of leaks and the internet wasn’t the near orwellian nonsense it’s shaping up to be now."
        show hit embarrassed_talk at right
        hit "What she told me are mostly low coffee break conversations and pieces mashed together after multiple interviews from different interviewers."
        show pov confused_talk at left
        show hit embarrassed at right
        pov "How did she come to know all of this then?"
        show pov confused at left
        show hit embarrassed_talk at right
        hit "My dad never stopped searching."
        show hit bored_talk at right
        hit "He did his own investigation once the police gave up on the case and with the help of my mom, they tried to get answers from anyone they could."
        show pov shocked at left
        show hit sad_talk at right
        hit "They were forced to stop once my dad became obsessive after reaching a dead end."
        show hit embarrassed_talk at right
        hit "Nearly drove him insane and almost tore their relationship apart."
        show pov embarrassed at left
        hit "It wasn’t until I was born that my dad decided to put all the work aside to take care of me and my mom."
        show hit confused_talk at right
        hit "According to my mom, he still keeps all his notes and documents on the case in his desk drawer in his office just in case."
        show pov shocked_talk at left
        show hit confused at right
        pov "What happened next with the town?"
        show pov confused at left
        show hit smirk_talk at right
        hit "What you can expect."
        show hit bored_talk at right
        hit "Once things got out of control, people became more and more paranoid the more people disappeared."
        show pov shocked at left
        show hit angry_talk at right
        hit "Blamed the cops, blamed the youth, blamed tv. The usual small town folk nonsense."
        show hit bored_talk at right
        hit "Soon enough, people started moving away in mass."
        show pov sad at left
        show hit shocked_talk at right
        hit "A lot of families left and a ton of businesses went under because of it, to the point it really put the town’s future in trouble."
        show hit sad_talk at right
        hit "All the expansion the town had seen in the nineties pretty much caved in on itself and the mayor was pretty much begging on his knees for businesses and people to stay."
        show pov sad_talk at left
        show hit bored at right
        pov "Sounds like a worse case scenario."
        show pov confused at left
        show hit embarrassed_talk at right
        hit "Here is where it gets weird though."
        show pov confused at left
        show hit smirk_talk at right
        hit "Suddenly, everything came to an end as if nothing ever happened."
        show pov confused_talk at left
        show hit smirk at right
        pov "What do you mean?"
        show pov confused at left
        show hit bored_talk at right
        hit "The kidnappings, the ransacking, the messages, everything just stopped as if nothing ever happened."
        show pov shocked at left
        show hit shocked_talk at right
        hit "All quiet on the western front out of the sudden."
        show hit smirk_talk at right
        hit "At first it was a huge shit show since the more paranoid people got it into everyone’s heads that the sudden silence meant that something worse was coming."
        show pov confused_talk at left
        show hit smirk at right
        pov "And nothing happened?"
        show pov confused at left
        show hit smirk_talk at right
        hit "Nothing that day, or the next or the next after that."
        show pov shocked at left
        show hit bored_talk at right
        hit "Just peace and quiet after so long."
        show pov embarrassed_talk at left
        show hit bored at right
        pov "Do you have any idea what stopped it?"
        show pov embarrassed at left
        show hit bored_talk at right
        hit "No one knows for sure."
        hit "They were just blown with the wind and no one heard anything about it again."
        show hit embarrassed_talk at right
        hit "But while people were relieved about how the kidnappings and even the disappearances in general were coming to an end, there was still the pressing issue of the low businesses in town."
        show pov confused at left
        show hit bored_talk at right
        hit "And that’s when The Robotics Company came in."
        show pov shocked at left
        show hit smirk_talk at right
        hit "Bought as much land as they could, be it for their offices or warehouse space and set up a small branch of their conglomerate right here in town."
        show hit confused_talk at right
        hit "And just like that, the town was saved and The Robotics Company managed to get a ton of property here for real cheap."
        show pov confused at left
        show hit smirk_talk at right
        hit "My mom went on a tangent for an hour about it."
        hit "Going into detail about all the property whose original owners could never return to after leaving, so a lot of the businesses that were once privately owned were replaced or co-owned for ones approved by The Robotics Company."
        show pov confused_talk at left
        show hit smirk at right
        pov "Sounds like she has a lot of animosity against them."
        show pov confused at left
        show hit smirk_talk at right
        hit "My grandpops on my mother’s side used to own a bakery, but since it was in an area The Robotics Company needed during their expansion, they eventually got buyed out."
        show hit bored_talk at right
        hit "She and many others were affected by the sudden change and still have yet to entirely forgive The Robotics Company for taking advantage of the situation."
        show pov embarrassed at left
        show hit sad_talk at right
        hit "Losing your own business only for someone else to expand their own, and even being offered to keep working on it’s replacement as their employee can be quite the slap to the face for some people."
        hit "Some more than others of course and some don’t let go of their grudges easily."
        show pov sad_talk at left
        show hit sad at right
        pov "I see…"
        show pov sad at left
        show hit sad_talk at right
        hit "After that, it was all soon forgotten and everyone moved on with their lives but…"
        show pov confused_talk at left
        show hit sad at right
        pov "But?"
        show pov confused at left
        show hit embarrassed_talk at right
        hit "Well, my mom and dad have no real evidence backing this up since no one really knows who they were."
        show pov shocked at left
        show hit bored_talk at right
        hit "But some rumors say that the paranoid person who was held in custody, also disappeared the very same night everything came to an end."
        show pov shocked_talk at left
        show hit embarrassed at right
        pov "What?"
        show pov shocked at left
        show hit embarrassed_talk at right
        hit "It’s just a rumor for the people who know the full picture about it."
        show pov angry at left
        show hit bored_talk at right
        hit "But no reports ever confirmed the identity of whoever was the one who was taken back then and far too many people disappeared back then to be sure of a single suspect."
        show hit confused_talk at right
        hit "But think about it. Someone with that level of a damaged mind would stand out even after a few years, don’t you think?"
        show pov shocked at left
        show hit shocked_talk at right
        hit "And the fact no one has ever come forward about it makes it even more suspicious."
        show pov confused_talk at left
        show hit bored at right
        pov "C-Couldn’t they have just left town afterwards?"
        show pov confused at left
        show hit bored_talk at right
        hit "I mean, maybe?"
        show hit embarrassed_talk at right
        hit "But doesn’t it seem convenient?"
        show hit confused_talk at right
        hit "The ransacking and kidnappings just end out of the sudden without any explanation?"
        show pov bored at left
        show hit bored_talk at right
        hit "Wouldn’t it make sense for it to cease once they managed to get what they were looking for to begin with?"
        show pov embarrassed_talk at left
        show hit bored at right
        pov "It could just be a coincidence, right?"
        show pov embarrassed at left
        show hit bored_talk at right
        hit "Maybe, but my parents sure as hell don’t believe that."
        show pov confused at left
        show hit sad_talk at right
        hit "And once you are the level of desperation for answers that my dad reached..."
        show pov shocked at left
        show hit embarrassed_talk at right
        hit "Well, let’s just say that there are no such things as coincidences."
        show pov shocked_talk at left
        show hit embarrassed at right
        pov "Wow…"
        show pov bored_talk at left
        pov "W-Well, thanks Hitomi. This was really…"
        show pov embarrassed_talk at left
        show hit embarrassed at right
        pov "Quite eye opening in many ways…"
        show pov embarrassed at left
        show hit embarrassed_talk at right
        hit "I hope it proves useful on your essay."
        show hit smirk_talk at right
        hit "I wouldn’t share a story like this with just anyone you know?"
        show pov shocked at left
        show hit embarrassed_talk at right
        hit "B-but you have been really nice to me, so I feel comfortable enough telling it to you."
        show pov embarrassed_talk at left
        show hit neutral at right
        pov "I really appreciate it."
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "I’ll pay you back for it someway, I promise."
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "J-Just make sure you keep my family’s name out of it, okay?"
        show hit smirk_talk at right
        hit "I really don’t want people to give me sympathy about it or much less try to play the nice guy card on me to try and comfort me."
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "I give you my word, no one will know you are even involved with it."
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "Thanks [povname]."
        show pov embarrassed at left
        show hit neutral_talk at right
        hit "Well, I better get back to work."
        hit "I’ll see you later, okay?"
        show pov neutral_talk at left
        show hit neutral at right
        pov "Sure thing!"
        pov "Thanks again for your help."

        $ investigations_hitomi = 1

    jump lbl_comicbookstore_day_setup
