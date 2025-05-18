##-In this scene the player talks to the characters located in the School entrance, this characters are Edward, Cole, Luna and Zariah-


##[School’s Entrance, afternoon - “Investigations_Cole”  - main_story =84-I]

##-Mc approaches Cole who is mid conversation in his phone looking upset-
label lbl_investigations_cole:
    if investigations_cole != 0:
        pov "{i}I'll leave him alone for now.{/i}"
    else:
        default investigations_cole = 0
        show col embarrassed_talk at right
        with dissolve
        col "N-No, no."
        show col angry_talk at right
        col "I told you this already in the morning man, just put the new merchandise with the newer looking boxes and take the damaged looking ones out."
        show pov shocked at left
        show col shocked_talk at right
        with dissolve
        col "The ones that are leaking some sort of fuzzy green goop."
        show pov confused_talk at left
        show col shocked at right
        pov "Uh, hey Cole?"
        show pov confused at left
        show col embarrassed_talk at right
        col "Just a sec, dude."
        show pov embarrassed at left
        show col shocked_talk at right
        col "No, it's nothing radioactive or anything like that!"
        show pov confused at left
        show col angry_talk at right
        col "Why would I keep anything radioactive in a storage unit?!"
        show col bored_talk at right
        col "And if I did, you would be the last person I consider for getting rid of it!"
        show pov embarrassed at left
        col "Look, just get it out of the unit and clean any excess goop on the floor. I'll come over there in a bit to get rid of the boxes and help you get the new stuff in, okay?"
        show col smirk_talk at right
        col "Cool, see you later."

        ##-Cole hangs up and looks back to the mc-
        show col embarrassed_talk at right
        col "Sigh. This is the sort of headaches I get for hiring cheap labor."
        show col bored_talk at right
        col "It seems downright impossible to find someone around who is at least capable of running errands without blasting my phone every five minutes."
        show pov confused at left
        show col neutral_talk at right
        col "Speaking of, are you free today by any chance, [povname]?"
        show pov embarrassed_talk at left
        show col sad at right
        pov "Uh, sadly I have my hands full at the moment, man."
        show pov sad_talk at left
        show col neutral at right
        pov "I'll take a raincheck on that."
        show pov embarrassed at left
        show col neutral_talk at right
        col "No worries man, I can't expect you to be available 24/7."
        show pov neutral at left
        show col confused_talk at right
        col "So, what's up? Is there something you need?"
        show pov embarrassed_talk at left
        show col confused at right
        pov "Actually, I could use a bit of help myself right now."
        show pov embarrassed at left
        show col neutral_talk at right
        col "If it's in my power, sure!"
        show col smirk_talk at right
        col "But I do need to go sort some business out by my storage unit soon."
        show pov embarrassed_talk at left
        show col smirk at right
        pov "That's ok, I was actually in the hunt for some information."
        show pov neutral at left
        show col shocked_talk at right
        col "Oh, of that I have plenty!"
        show pov embarrassed at left
        show col smirk_talk at right
        col "What do you wanna know?"
        show pov embarrassed_talk at left
        show col smirk at right
        pov "Well, I was hoping you could tell me anything about strange events around town."
        show pov neutral at left
        show col smirk_talk at right
        col "Is that a trick question or something?"
        show pov smirk_talk at left
        show col smirk at right
        pov "I mean before all of this mess."
        show pov embarrassed at left
        show col smirk_talk at right
        col "Trying to get to know more about the town, huh?"
        show col embarrassed_talk at right
        col "Well, sorry to disappoint you dude, but small towns like this one tend to be rather stale in terms of what happens around town."
        show col confused_talk at right
        col "Why do you think the news of you getting naked and arrested traveled around so fast?"
        show pov embarrassed_talk at left
        show col confused at right
        pov "Yeah, I figured that was the case, so I’m more interested in the history of the town and some interesting legends or rumors about it."
        show pov neutral_talk at left
        show col neutral at right
        pov "Figured I could get to know this sort of thing and get more familiar with the town at the same time."
        show pov embarrassed at left
        show col neutral_talk at right
        col "I get ya man, must be hard being the new kid in lands you don’t know."
        col "Well, let me think here…"
        show col bored_talk at right
        col "Hmmm…"
        show pov embarrassed_talk at left
        show col confused at right
        pov "It’s cool if you can’t think of anything, I’m asking a few people so don’t feel pressured."
        show pov embarrassed at left
        show col embarrassed_talk at right
        col "No, no. I wanna help you and it would be a bit embarrassing if an outsider becomes more familiar with the town than a local boy, you know?"
        show pov confused at left
        show col smirk_talk at right
        col "Hmmm, well. What first comes to mind is an old horror story they used to tell us about the town."
        show col confused_talk at right
        col "Is that something you would be interested in?"
        show pov neutral_talk at left
        show col embarrassed at right
        pov "That sounds interesting enough."
        show pov smirk_talk at left
        show col neutral at right
        pov "Sure, let me hear it."
        show pov neutral at left
        show col embarrassed at right
        col "Well, before anything, you should know that early during its founding, the town used to be a mining town."
        show pov shocked_talk at left
        show col embarrassed at right
        pov "Really?"
        show pov confused at left
        show col embarrassed_talk at right
        col "Yeah, it was quite the lucrative early century business that every fat cat back then seemed to be into."
        show col bored_talk at right
        col "All across the valley back in the old days had a lot of ore deposits one could take benefit from and the town was chosen as the main hub to settle the companies in since it was pretty much in the middle of everything."
        show col confused_talk at right
        col "But as the town grew and demand increased, the founding families in charge of the mining operations became more and more greedy."
        show pov embarrassed at left
        show col embarrassed_talk at right
        col "Tale as old as time, the times are good, prosperous and everyone is happy but the fat cats all want to be top dog and feel like they have the biggest dick in the room."
        show pov embarrassed_talk at left
        show col embarrassed at right
        pov "The usual standard in businesses."
        show pov bored at left
        show col embarrassed_talk at right
        col "Sadly the case."
        show col bored_talk at right
        col "Anyway, with the rising competition and without laws to really prevent rich dudes from trying to fuck each other over."
        col "The two main mining families in town pretty much went in an all out war."
        show pov confused at left
        show col shocked_talk at right
        col "Stealing the other’s equipment, wrecking the other’s work space, going behind their backs and stealing their clients."
        show col bored_talk at right
        col "Overall annoying stuff to make the other’s life more difficult, but nothing too over the line."
        show pov shocked at left
        show col smirk_talk at right
        col "Mining jobs were dangerous and the workers weren’t about to mess with each other inside the mine."
        show pov confused at left
        show col bored_talk at right
        col "But even so, the hatred between the two families' heads was reaching its boiling point."
        show col smirk_talk at right
        col "Legend is that they always hated each other until it boiled over by something that hasn’t really been specified and the other retaliated even worse."
        show pov smirk_talk at left
        show col smirk at right
        pov "People back then really got butt hurt easily and held over grudges for life over dumb shit."
        show pov smirk at left
        show col smirk_talk at right
        col "I like to think one of them made a rude “Yo mama” joke and the other retaliated by sleeping with the other’s wife or something."
        show col bored_talk at right
        col "Anyway, point is, that this rivalry of theirs eventually reached a breaking point, so they started some sort of competition."
        show col confused at right
        col "Whoever mined the deepest into the soil and found the biggest treasure by the end of some length of time they agreed on would be the winner and the loser had to leave town."
        show pov confused_talk at left
        show col confused at right
        pov "How many things were resolved by a contest of some sort back in the day?"
        show pov smirk at left
        show col bored_talk at right
        col "Isn’t that the plot of “Around the world in 80 days”?"
        show col smirk_talk at right
        col "Love that book, but my point is, if you have the money and are bored enough to make big contests out of anything, why not?"
        show pov neutral at left
        show col smirk_talk at right
        col "There was jack shit to do back in the day after all."
        show pov smirk_talk at left
        show col neutral at right
        pov "Fair enough."
        show pov shocked at left
        show col bored_talk at right
        col "Anyway, the contest started and the two men went a bit crazy over it."
        show col shocked_talk at right
        col "Started hiring people in mass, to the point even women had to join the mining efforts, mostly to tend to the wounded down the mines since the need to dig fast meant to also overlook safety standards."
        show col smirk_talk at right
        col "If you can call the lack of human empathy back then a safety standard."
        show pov smirk at left
        show col bored_talk at right
        col "Accidents were common but that didn’t stop the family heads from forcing their workers to work under ever more dangerous conditions."
        show pov confused at left
        show col smirk_talk at right
        col "Not that they could complain since the more they digged, the better their pay."
        show col bored_talk at right
        col "The family heads were out for the other’s blood and if that meant paying their workers double or triple the amount so that they would work faster, they would be willing to pay it."
        show col smirk_talk at right
        col "Even if it meant cutting corners to the point it wasn’t humane to send people down there."
        show pov embarrassed_talk at left
        show col smirk at right
        pov "I assume all authorities were turning a blind eye to it."
        show pov embarrassed at left
        show col smirk_talk at right
        col "That's the beauty about the law system back then."
        show col bored_talk at right
        col "As long as the officers and judges' wallets were constantly full, everyone turns a blind eye."
        show pov shocked_talk at left
        show col smirk at right
        pov "Fits today's bill quite often as well."
        show pov smirk at left
        show col smirk_talk at right
        col "Cash is king dude."
        show col neutral_talk at right
        col "And all men obey the king's command."
        show pov smirk_talk at left
        show col neutral at right
        pov "Quite poetic of you."
        show pov smirk at left
        show col neutral_talk at right
        col "Thank you!"
        show pov confused at left
        show col bored_talk at right
        col "Anyway, with time, the tunnels down the mines grew longer and longer, to the point it allegedly took a whole day's travel on foot to get in and out of it."
        show col neutral_talk at right
        col "Camps were set up in several places in order to look for fortune and treat the injured and people were getting fed up with the families heads."
        show pov shocked at left
        col "It all came to a stop however when the two main tunnels collided."
        show col smirk_talk at right
        col "They had digged down so much that eventually they reached a cavern where their tunnels met."
        show pov neutral at left
        col "And according to the records, they also found exactly what they were looking for."
        show col smirk_talk at right
        col "A treasure that would force one of the companies to leave as agreed."
        show pov confused_talk at left
        show col smirk at right
        pov "What kind of treasure was it?"
        show pov confused at left
        show col embarrassed_talk at right
        col "Nobody really knows, especially after what happened next."
        show pov confused_talk at left
        show col embarrassed at right
        pov "What do you mean?"
        show pov confused at left
        show col embarrassed_talk at right
        col "Well, it’s not clear if it was the exhaustion and stress from being overworked, the influence of their bosses to hate each other or the threat of getting out of a job if their company wasn’t the one to bring back the treasure, but a full on brawl started."
        col "I’m talking a full on “Killer Kombat” style fight between the two groups."
        show pov shocked at left
        show col sad_talk at right
        col "Countless people injured and several dead all."
        show pov confused at left
        show col bored_talk at right
        col "The men were tired and not about to hand over the treasure, so while some continued to fight, others tried messing with the competitors tunnels."
        show pov shocked at left
        show col embarrassed_talk at right
        col "It all ended up as you can imagine."
        show pov sad at left
        show col sad_talk at right
        col "A huge collapse that buried people alive and trapped everyone else."
        show pov sad_talk at left
        show col embarrassed at right
        pov "My god…"
        show pov sad at left
        show col embarrassed at right
        col "both of the families lost around 70%% of their workers in the collapse and due to their need to cut corners to pay their employees, there was no other way down the mines."
        show pov shocked at left
        show col bored_talk at right
        col "No emergency exit or second tunnel, nothing that could save the workers in time."
        show pov sad at left
        show col sad_talk at right
        col "The family heads had pretty much ran out of money, so the law stopped turning a blind eye and the two family heads were sentenced to death, their families were left in ruins and had to flee town before the angry mob crucified them and the mines were closed for good."
        show pov sad_talk at left
        show col sad at right
        pov "That is a haunting story, man."
        show pov sad at left
        show col shocked_talk at right
        col "Oh, but there is more!"
        show pov confused_talk at left
        show col shocked at right
        pov "There is?"
        show pov confused at left
        show col embarrassed_talk at right
        col "Yeah, dude!"
        show col smirk_talk at right
        col "Here is where the actual horror story starts man!"
        show pov confused_talk at left
        show col smirk at right
        pov "Oh boy."
        show pov confused at left
        show col shocked_talk at right
        col "Some people say that some of the tunnels stood intact and that some people survived."
        show col angry_talk at right
        col "Staying alive on water that came from underground canals and rocks and by feeding themselves on the corpses of the death miners. Waiting for a rescue that would never come."
        show pov shocked at left
        show col shocked_talk at right
        col "Slowly losing their minds and digging trying to find their way outside with their own bare hands."
        show pov confused at left
        show col smirk_talk at right
        col "The legend says that if they were to ever get out, they would be mutated cannibal mutants ready to enact their revenge on the town that forgot about them."
        show pov confused_talk at left
        show col smirk at right
        pov "Ok, that’s a bit of a stretch isn’t it?"
        show pov confused at left
        show col smirk_talk at right
        col "Is it?"
        show col bored_talk at right
        col "Back in the 70’s a few teenagers disappeared when they apparently found a secret exit that led into one of the tunnels of the mine."
        show pov shocked at left
        show col smirk_talk at right
        col "The only thing that was found of them?"
        show col shocked_talk at right
        col "Clothes that seemed to have been clawed off their bodies and left in rags."
        show pov confused at left
        col "Likely so the cannibals could feast upon their naked bodies!"
        show pov confused_talk at left
        show col smirk at right
        pov "Creepy."
        show pov confused at left
        show col smirk_talk at right
        col "I heard that story a few summers ago, back then it kept me awake for two nights straight."
        show col bored_talk at right
        col "doesn’t help that I’m claustrophobic, so I had many nightmares of being trapped in the mines with the cannibals after me."
        show pov embarrassed_talk at left
        show col bored at right
        pov "It’s a cool story, Cole."
        show pov neutral_talk at left
        show col smirk at right
        pov "Thanks for telling me."
        show pov neutral at left
        show col smirk_talk at right
        col "No problem dude!"
        show col embarrassed_talk at right
        col "Hope it satisfies your curiosity a bit."
        show pov embarrassed_talk at left
        show col neutral at right
        pov "It does, but I feel like I should find some more stories like that before I call it a day you know?"
        show pov neutral at left
        show col shocked_talk at right
        col "Oh, in that case you should go chat with Violette at the beach."
        show pov confused_talk at left
        show col neutral at right
        pov "With Violette?"
        show pov confused at left
        show col smirk_talk at right
        col "Yeah, she says she has been witnessing some weird shit happening at the beach."
        show pov smirk at left
        show col embarrassed_talk at right
        col "I don’t really recall what it was, but it had her pretty freaked out one day."
        show pov smirk_talk at left
        show col embarrassed at right
        pov "I’ll ask her next time I see her."
        show pov neutral_talk at left
        show col neutral at right
        pov "Thanks again man, you’ve been a big help!"
        show pov neutral at left
        show col neutral_talk at right
        col "It’s nothing dude, that’s what friends are for."
        show pov confused at left
        show col embarrassed_talk at right
        col "Anyway, if you excuse me, I gotta go clean some green goop boxes."
        show col bored_talk at right
        col "Something I’m NOT looking forward to as you can imagine."
        show pov confused_talk at left
        show col embarrassed at right
        pov "What’s up with that, by the way?"
        show pov embarrassed at left
        show col embarrassed_talk at right
        col "I ordered some lava lamps I was planning to sell around town, but the idiots at the post office pretty much smashed every single one of them when they left them at my storage unit so they are now leaking that floating liquid."
        show pov confused at left
        show col bored_talk at right
        col "Been procrastinating about getting them out but now that I have a shipment of scented candles coming up, I need the space."
        show pov confused_talk at left
        show col embarrassed at right
        pov "Scented candles?"
        show pov confused at left
        show col bored_talk at right
        col "You would not believe how easy it is to sell them when they are in season."
        show col smirk_talk at right
        col "Right now, at home yoga and meditation is very popular so they sell like hot bread since they help set the mood when you try it!"
        show pov embarrassed at left
        show col bored_talk at right
        col "For that and you never know when you could use some extra mood lighting, you know?"
        show pov neutral_talk at left
        show col embarrassed at right
        pov "I get ya."
        show pov smirk_talk at left
        show col smirk at right
        pov "Well, don’t let me stop you."
        show pov neutral at left
        show col smirk_talk at right
        col "Nice talking to you man, glad I was of any help."
        show pov neutral_talk at left
        show col neutral at right
        pov "You sure were, Cole. Thanks again!"
        show col smirk at right
        pov "See you later."
        show pov neutral at left
        show col smirk_talk at right
        col "Don’t be a stranger, dude!"

        ##=SCENE END=

        $ investigations_cole = 1

    jump lbl_schoolyard_day_setup
