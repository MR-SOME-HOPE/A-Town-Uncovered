## Bump in the Night
label lbl_bump_in_the_night:
    ## CG Start
    ## bg bumpinthenight_1

    ##scene bg bumpinthenight_temp1
    scene bg bumpinthenight_1-1
    with fade
    ##"You wake up, several hours later. The fall and head slamming were enough to knock you out for a good couple of hours. The bump on the back of your head, now making itself present."

    pov "Ugh…"
    pov "God, who’s the fucker that hit me?"
    pov "Did someone get his number plate…?"

    ##show bg bumpinthenight_temp2
    scene bg bumpinthenight_1-2 with dissolve
    ##"You put your hand to your head - still groggy."

    pov "Did I?-"
    pov "Ugh…"
    scene bg bumpinthenight_1-3 with dissolve
    pov "{i}*Sigh*{/i} Fuck.. oww.. My head."
    pov "Nice moves, [povname]... Nice moves."
    pov "{i}What time is it anyway?{/i}"
    pov "..."
    pov "Fuck... the sun's already down?!"
    pov "Ow shit, my head..."
    pov "Stupid fucking chair..."

    ##show bg bumpinthenight_temp3
    ##"Once your brain stops leaking out of your ear and resets itself, you head over to the window to open the curtain, and check outside."
    scene bg bumpinthenight_2-1 with fade
    $ renpy.pause(0.3,hard=True)
    ##show bg bumpinthenight_temp4
    scene bg bumpinthenight_2-2 with dissolve
    $ renpy.pause(0.3,hard=True)
    ##show bg bumpinthenight_temp5
    #scene bg bumpinthenight_5 with dissolve
    #$ renpy.pause(2.0)
    pov "{i}The woman’s-{/i}"
    pov "{i}She’s gone…{/i}"
    pov "..."
    pov "{i}What did she want from me…?{/i}"
    pov "{i}She just stood there... stalking me.{/i}"
    pov "{i}Did she want me to willfully go with her?{/i}"
    pov "{i}It’s possible that she didn’t want to disturb the household...{/i}"
    scene bg bumpinthenight_2-3 with dissolve
    $ renpy.pause(0.3,hard=True)
    scene bg bumpinthenight_2-4 with dissolve
    $ renpy.pause(0.3,hard=True)

    #"you sit at your desk, clearly confused"
    ##bg bumpinthenight_6_angry
    ##bg bumpinthenight_6_angry_talk
    ##bg bumpinthenight_6_happy
    ##bg bumpinthenight_6_happy_talk
    ##bg bumpinthenight_6_confused_talk
    ##bg bumpinthenight_6_confused
    ##show bg bumpinthenight_temp5
    ##with dissolve
    scene bg bumpinthenight_6_confused with fade
    pov "{i}I’m not sure whether she’s just not allowed to enter my home.{/i}"
    pov "{i}But she's not a vampire... is she?{/i}"
    pov "{i}Maybe she’s waiting to pounce on me when I least expect it.{/i}"
    pov "{i}I suppose that I better keep an eye on using the main roads. And avoid the park during quiet hours.{/i}"
    pov "{i}Better to play it safe than to be sacrificed by a maniac.{/i}"
    pov "{i}That’s a saying, right?{/i}"
    pov "…"
    ##scene bg bumpinthenight_6_confused_talk
    scene bg bumpinthenight_3_hunched with dissolve
    pov "I am fucking losing it, aren’t I?"
    ##scene bg bumpinthenight_6_confused
    pov "{i}*Sigh*{/i}"
    pov "What am the hell am I supposed to do now?"
    pov "{i}What is even going on in this town?!{/i}"
    pov "{i}S-Should I talk to the police?{/i}"
    pov "{i}They are supposed to help with kind of situations, right?{/i}"
    pov "{i}Either that, or at least, I should be way harder to sacrifice in a mental institution.{/i}"
    ##scene bg bumpinthenight_6_happy
    pov "{i}Locked up in one of those comfy looking, cushion covered rooms.{/i}"
    pov "{i}At the very least, I wouldn’t have to worry about the course assignments anymore.{/i}"
    pov "…"
    pov "Yeah, that’s fucking stupid."
    ##scene bg bumpinthenight_6_confused
    pov "Someone has to know something about this, right?"
    pov "{i}There is always that one person in horror movies, who inexplicably knows all the answers and everything that's going on.{/i}"
    ##scene bg bumpinthenight_6_happy
    pov "{i}Then again, they usually get killed, right as they are about to explain everything.{/i}"
    ##scene bg bumpinthenight_6_angry
    pov "{i}Not to mention that if I go around asking people questions like this, I am likely to end in the same loony bin as the previous option.{/i}"
    pov "{i}And with my record, if I start showing the signs; Officer Mina will undoubtedly send me to the cushioned room herself.{/i}"
    pov "{i}I need to collect information. If I stay in one place, I am a fish in a barrel.{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}Who would know anything strange about the things in town?{/i}"
    pov "{i}Effie is always a safe bet, with how much she knows everyone around. Then again, who knows how she would take, me just asking random questions. And I don’t want to scare one of my only friends here, away.{/i}"
    pov "{i}For that matter, there is Jacob too. Though I doubt he knows anything at all… Or is that what they want me to think?{/i}"
    pov "…"
    ##scene bg bumpinthenight_6_happy
    pov "{i}Nah, Jacob playing the hidden traitor card?{/i}"
    pov "{i}He would shoot himself in the foot the first day on the job if he was a spy.{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}Right?{/i}"
    pov "..."

    #(Threeghans)
    pov "{i}There are the ‘Threeghans’.{/i}"
    ##scene bg bumpinthenight_6_angry_talk
    pov "The trifecta of snobs."
    ##scene bg bumpinthenight_6_confused
    pov "{i}Well, only Meghan’s the bitch. Teghan’s pretty cool, and who’s the exchange student?{/i}"
    if discussingtheincident_threeghans == 1:
        pov "It's not Chieghan. It's Lee... something - I remember Lashley saying."
    else:
        pov "{i}Chieghan? I’m pretty sure that’s a nickname.{/i}"
    pov "{i}In any case-{/i}"
    pov "{i}If anyone knows of anything regarding any strange occurrences around town and its history, it’s definitely got to be the plastics.{/i}"
    pov "{i}If anyone has the whole town in their contact list, it’s them.{/i}"
    pov "{i}I should talk to them individually though - I know how they are in a pack{/i}."
    pov "{i}At least Teghan and Chieghan are nicer when speaking, separate from Meghan’s influence.{/i}"
    pov "{i}I shouldn’t have my hopes too high, but it’s better than nothing when I have zero leads.{/i}"
    pov "{i}*Sigh*{/i} I’m just realising that anything I say to them will be turned into a meme. I just know it."
    pov "{i}News spreads like wildfire when they’re involved, but that could possibly be in my favour.{/i}"

    #(Grundle Sam)
    pov "Hmmm..."
    pov "{i}There is that crazy totem guy at the mall.{/i}"
    pov "{i}If there is anyone strange enough to know something about another world, it has to be the guy; who bases his entire business module in trading totems.{/i}"
    ##scene bg bumpinthenight_6_happy
    pov "{i}At least that’s how it works in the games and movies.{/i}"
    pov "{i}As long as I don’t let him ramble on about lizard people, I should be fine.{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "…"
    ##scene bg bumpinthenight_6_angry
    pov "{i}I’m not fucking lizard people disguised as actual humans, right?{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}There's no way!{/i}"
    pov "…"
    pov "{i}Right?{/i}"

    #(Edward)
    pov "{i}There is that nerdy dude: Edward.{/i}"
    pov "{i}He is always finnicking around with gadgets and stuff like that.{/i}"
    ##scene bg bumpinthenight_6_happy
    pov "{i}He seems to be the guy who knows a thing or two - even if that thing or two consists of supernatural beings.{/i}"
    pov "{i}Hopefully one of his ‘ghost catching’ ma-jiggies works-{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}Actually, now that I think about it, if one of them did work, either no one would believe him or he would be rich-up-the-anus.{/i}"
    pov "{i}At the very least, he should have a camera I could borrow. I can use it to capture VI on tape and use it as evidence.{/i}"
    pov "…"
    ##scene bg bumpinthenight_6_angry
    pov "{i}Or I could be seen as a massive pervert, for putting surveillance equipment everywhere.{/i}"
    pov "{i}I bet Officer Mina and Director Lashley are going to love having me explain myself, over that whole mess.{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}I doubt that I can pull the ‘scary lady following me from an alternate dimension under the lake’ card, with them.{/i}"
    pov "{i}I doubt it even has that high of a success rate with anyone, to begin with.{/i}"
    ##scene bg bumpinthenight_6_angry
    pov "{i}Much less from someone who is now known as the town’s local exhibisionist.{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}And that’s saying something, when the town has a very distinctive nudist beach.{/i}"

    #(Violette)
    ##scene bg bumpinthenight_6_happy
    pov "{i}Which reminds me: Violette - that lifeguard at the beach - may be able to help me out.{/i}"
    ##scene bg bumpinthenight_6_confused_talk
    pov "She {i}did{/i} save me at the park, after all… or did she…?"
    pov "{i}I don’t want to confuse myself, by overthinking all this.{/i}"
    ##scene bg bumpinthenight_6_happy
    pov "{i}But who better to talk to, than the person who watches over the source of my problem?{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}Things around town have been strange enough, as it is. And that means they must have at least some crazy theories of their own.{/i}"
    pov "{i}I’d likely not find anything of use from them. But they say rumors come from a bit of truth, so there is bound to be a clue scattered among the nonsense.{/i}"
    pov "{i}Plus, Violette seems to be the type to know many faces. That raises the chances of having anything to lead with.{/i}"
    ##scene bg bumpinthenight_6_happy_talk
    pov "Hopefully she doesn’t ban me from the beach."
    ##scene bg bumpinthenight_6_confused
    pov "{i}For the time being, I guess those are the best start I am going to get when it comes to leads.{/i}"
    pov "{i}I wonder how deep this whole thing goes.{/i}"
    ##scene bg bumpinthenight_6_angry
    pov "{i}I mean, I think the whole town was at that ritualistic ceremony.{/i}"
    ##scene bg bumpinthenight_6_confused
    pov "{i}But I doubt there are many on this side of the lake who actually know about the whole... other world thing.{/i}"
    pov "{i}Otherwise I think they would at least mention it; in a brochure or on their wykypydia.{/i}"

    ##if 20 <= mum_path <= 24 or 26 <= sister_path <= 36:
    ##    jump lbl_bump_in_the_night_pt3
    ##else:
    jump lbl_bump_in_the_night_pt2
