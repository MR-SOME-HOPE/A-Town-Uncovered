label lbl_porn_police:

    image bg pornpolice_anim = Animation(
    "//scenes/school/hallway2/day/story/pornpolice/assets/bg_pornpolice_1.jpg", 1.2,
    "//scenes/school/hallway2/day/story/pornpolice/assets/bg_pornpolice_2.jpg", 1.2
    )##bg schoolanxiety_2_lights_on, bg schoolanxiety_2_lights_off
    ##scene bg pornpolice_temp1
    scene bg pornpolice_1
    with fade
    #"Scene starts when entering the second floor hallway in an odd day, you walk up to a scene of Lashley digging in an open locker as a crowd of students circle her."
    ##"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    #if inventory.has_item(Items.fbpwmag1):
    studm "I don’t got no nothing on me, man!"
    studm "This isn’t constitutional, it is a violation of my rights! I demand my right to a lawyer!"
    pri "The only thing you should be concerned about right now is the weeks of detention every single magazine or picture that I find will give you, young man!"
    pri "And may the lord have mercy on your immortal soul if I find any of those clearly underage japanese caricatures you young men call 'lollies'?!"
    pri "I assure you, they are not the sweet kind!"
    show bg pornpolice_anim
    pov "What’s going on?"
    studf "Director Lashley is going on one of her 'inspections'."
    pov "Oh, so the guy has weed or something in his locker?"
    studf "If he is lucky that's all there is."
    pri "Aha! Just what I was looking for!"
    show bg pornpolice_2 with dissolve

    #"Lashley comes out of the locker with a few magazines of the porn variety."

    #show bg pornpolice_temp2
    show bg pornpolice_3 with hpunch
    pri "Just like I suspected."
    show bg pornpolice_4
    studm "T-Those aren’t mine!"
    studm "I was set up!"
    show bg pornpolice_5
    pri "Sure you were... I hope you understand that all of these are going to land you at least three weeks of detention; not to mention the extra for lying directly to my face."
    show bg pornpolice_6
    studm "C-Come on, man! It ain’t like that!"
    show bg pornpolice_7
    pri "Proverbs 12:22. My child, we are going to go over what that verse means in detention - not to mention some general study to help occupy that filthy mind of yours with something productive."
    show bg pornpolice_3
    pri "Now head straight to my office!"
    show bg pornpolice_8
    pri "And all of you start heading to class before I start handing out detention to you as well!"
    show bg pornpolice_4
    pov "{i}Damn, she really is going full detective on that guy.{/i}"
    pov "{i}I think he is even about to cry in frustration or something.{/i}"
    if inventory.has_item(Items.fbpwmag1):
        pov "{i}Wait... Do I still have that porno mag I got from Hitomi with me?!{/i}"
        pov "{i}Damnit, why didn't I leave it at home?!{/i}"
        pov "{i}O-Okay, no need to panic. Just be cool and make sure she doesn't see you.{/i}"
        pov "{i}No way she is going to turn her attention on me out of the blue, right?{/i}"
    show bg pornpolice_9
    pri "Except for you, [povname]. You stay."

    ## Sprite Start
    scene bg schoolhallway2_day
    with fade
    show pov embarrassed_talk at left
    with dissolve
    show pri neutral at right
    with dissolve
    pov "Uh…"
    show pri smirk at right
    pov "Am I in trouble?"
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "Hehehe~"
    show pri neutral_talk at right
    pri "No, not at all."
    show pov confused at left
    show pri embarrassed_talk at right
    pri "I’m sorry you had to see that, but at least it lets me openly discuss with you a few more rules of the university."
    show pov confused_talk at left
    show pri neutral at right
    pov "I assume it involves the whole 'surprise inspection' thing?"
    show pov confused at left
    show pri neutral_talk at right
    pri "It’s all related to the zero tolerance policies we have. I don’t just go opening lockers at random - that would be highly unethical without a reason."
    show pov confused_talk at left
    show pri neutral at right
    pov "So the porn is one of those 'zero tolerances'?"
    show pov embarrassed at left
    show pri confused_talk at right
    pri "Do you hear yourself when you ask that? Of course it is!"
    show pri bored_talk at right
    pri "Along with drugs and weapons, the university has an absolute zero tolerance regarding any and all kinds of pornography and smut."
    show pov embarrassed_talk at left
    show pri bored at right
    pov "Sounds standard enough."
    show pov embarrassed at left
    show pri confused_talk at right
    pri "You would think so, but we actually have quite a severe problem of pornography distribution around the university."
    show pov shocked at left
    show pri bored_talk at right
    pri "Magazines, pictures, toys - even erotic PC games!"
    show pov embarrassed at left
    show pri sad_talk at right
    pri "This university has a bigger problem with pornography than most would have with Marijuana or alcohol!"
    show pri confused_talk at right
    pri "It’s gotten to the point, students are even trading with it, like back in the 90’s with those dreadful Yugi-Mon cards and whatnot."
    show pov embarrassed_talk at left
    show pri confused at right
    pov "I’m 100%% positive that’s not what they are called, but I see the problem."
    show pov shocked at left
    show pri confused_talk at right
    pri "Indeed - which is why I want you to take this as a warning."
    show pov embarrassed at left
    show pri bored_talk at right
    pri "I keep a very close eye -on this sort of stuff- around the premises."
    show pri angry_talk at right
    pri "If I see you, even looking, at a picture or video on your phone, or worse: have a magazine or toy on your person or in your locker; that will land you in detention, no questions asked."
    show pov shocked at left
    pri "'Revenge' content and any media taken and shared without consent, may even be reason for expulsion - along with any legal ramifications."
    show pov embarrassed at left
    pri "And don’t even get me started on sexual acts in my university."
    show pov embarrassed_talk at left
    show pri bored at right
    pov "Duly noted, Director Lashley. Don't worry, I will follow and obey."
    show pov embarrassed at left
    show pri bored_talk at right
    pri "Good!"
    show pri neutral_talk at right
    pri "I’m happy to see you are such a good egg, [povname]."
    show pri bored_talk at right
    pri "There is a time and place for everything. If I let hormonal teens roam around, doing whatever they want; there will be no order."
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "What do you think, [povname]?"

    menu:
        "Common practice.":
            $ add_points("principallashley_points",1)
            show pov confused_talk at left
            show pri neutral at right
            pov "Hey, nothing new to me, Director Lashley. Seems like common practice for any university."
            show pov embarrassed_talk at left
            pov "Do the crime; pay the time. And all that jazz."
            show pov neutral at left
            show pri neutral_talk at right
            pri "Thank you, [povname]."
            show pov confused at left
            show pri embarrassed_talk at right
            pri "This all shouldn't be so difficult, but it really is a problem here."
            show pov confused_talk at left
            show pri embarrassed at right
            pov "You get a hard time from all of this?"
            show pov embarrassed at left
            show pri embarrassed_talk at right
            pri "That’s an understatement."
            pri "You youngsters are always looking for something to rebel against, after all; it’s in your nature."
            pri "Since when was it wrong to have traditional values of sex until marriage?!"
            show pov shocked at left
            show pri confused_talk at right
            pri "The previous administrator was quite a slimeball. Did you know he molested a student?"
            show pov confused at left
            show pri angry_talk at right
            pri "I believe God forgives everyone but that is something not worth forgiving."
            show pov sad_talk at left
            show pri bored at right
            pov "Oh my God-"
            show pov shocked at left
            show pri bored_talk at right
            pri "Uh- please don't use his name in vain."
            show pov embarrassed_talk at left
            show pri bored at right
            pov "Sorry..."
            show pov neutral at left
            show pri bored_talk at right
            pri "When I stepped into the position, I made a lot of changes so nothing like that would ever happen again."
            show pov embarrassed_talk at left
            show pri embarrassed at right
            pov "Well, it’s nice to have someone care so much about us."
            show pov neutral_talk at left
            pov "If it eases your mind about what I think, I'm totally all for the policy and it makes all the senses."
            pov "I mean, I already came to this university with the assumption that that's already an established rule."
            show pov neutral at left
            show pri embarrassed_talk at right
            pri "That's great to hear, [povname]. I really am not emphasising how much that actually means to me to hear that."
            pri "I really appreciate it, [povname]. Thank you."

            if skill_cha >= 3:
                $ add_points("principallashley_points",1)
                $ skill_cha -= 2
                $ renpy.notify("You used 2 Charisma Points")
                show pov neutral_talk at left
                show pri embarrassed at right
                pov "Don’t mention it."
                pov "Willing to stand up for what's right is something worthy of respect."
                pov "So seeing you take measures to prevent stuff from happening in the first place, is rather admirable."
                show pov neutral at left
                show pri embarrassed_talk at right
                pri "T-Thank you!"
                pri "Wow, now that has to be the nicest thing I think anyone has ever said to me, period."
                show pov embarrassed at left
                show pri sad_talk at right
                pri "You are going to make me cry here, [povname]."
                show pov embarrassed_talk at left
                show pri embarrassed at right
                pov "I assure you, that isn’t my intention."

                if skill_cha >= 5:
                    $ add_points("principallashley_points",2)
                    $ skill_cha -= 3
                    $ renpy.notify("You used 3 Charisma Points")
                    show pov smirk_talk at left
                    show pri shocked at right
                    pov "I think you look far more beautiful when you smile."
                    show pov smirk at left
                    show pri shocked_talk at right
                    pri "O-Oh!"
                    show pri confused_talk at right
                    pri "W-Well now, I…"
                    show pri embarrassed_talk at right
                    pri "I-I, um…"
                    show pov neutral at left
                    pri "T-Thank you, [povname]..."
                    show pov smirk at left
                    pri "You are really sweet."

        "It's a little harsh…":
            $ subtract_points("principallashley_points",2)
            show pov confused_talk at left
            show pri shocked at right
            pov "I don’t know: it seems a little harsh, to be honest."
            show pov confused at left
            show pri bored_talk at right
            pri "Oh, pray tell, [povname]..?"
            show pri angry_talk at right
            pri "I find it hard to believe you're arguing that pornography shouldn't be banned on university grounds."
            pri "University. Grounds."
            pri "Pornography."
            show pov embarrassed at left
            show pri bored_talk at right
            pri "See what I'm getting at?"
            show pov embarrassed_talk at left
            show pri bored at right
            pov "I don’t know... I just feel it can be counterproductive, a little bit."
            pov "People get more of an edge of doing something forbidden than the actual porn."
            show pov smirk_talk at left
            show pri confused at right
            pov "And from the way you speak about it, it seems like these guys bring porn to the university, mainly to get a rise out of you."
            pov "I mean, internet porn exists for a reason. There really is no need for magazines these days."
            show pov smirk at left
            show pri smirk_talk at right
            pri "You know what? You bring up really good points, [povname]."
            show pov smirk_talk at left
            show pri angry at right
            pov "Really?"
            show pov shocked at left
            show pri angry_talk at right
            with hpunch
            pri "No?! Are you absolutely kidding me, [povname]?! That was the most tom-foolery I've ever heard all year."
            show pov sad at left
            pri "Someone has to draw the line where decency in concerned. And sue me for pushing the 'no porn' limit to the ultimate limit."
            pri "Don't forget the grounds in which you stand on - this isn't the jungle."
            show pov confused at left
            pri "So if I have to seem like a nosy-parker, or be accused of an invasion of privacy - so be it."
            show pov embarrassed at left
            pri "I am the principal, [povname]."
            pri "I am the rope that keeps this university together."
            show pri bored_talk at right
            pri "Sooner or later, I’m bound to find stuff out."
            show pov sad at left
            show pri sad_talk at right
            pri "{i}*Sigh*{/i}"
            show pov shocked at left
            show pri sad_talk at right
            pri "The previous administrator was quite a slimeball. Did you know he molested a student?"
            show pri bored_talk at right
            pri "I believe God forgives everyone, but that is something not worth forgiving."
            show pov shocked_talk at left
            show pri bored at right
            pov "Something like that happened?!"
            show pov shocked at left
            show pri bored_talk at right
            pri "I took over from the previous administrator after the major sex scandal, that he tried to push under the rug."
            show pov sad at left
            pri "I made it my vow since I first sat on the chair, to crack down on it. Not to mention, keep the more submissive students safe and keep the overall atmosphere of the university clean."
            show pov embarrassed at left
            pri "Extensive background checks and inspections had me getting rid of a lot of teachers. But luckily, now I have a team I trust."
            show pov embarrassed_talk at left
            show pri confused at right
            pov "Wow. Sounds like you made a lot of enemies with that."
            show pov embarrassed at left
            show pri bored_talk at right
            pri "Plenty - but I have not once wavered in my conviction."
            show pri confused_talk at right
            pri "As long as I have God on my side -to power me through the path of righteousness- he will protect me from the evil."
            show pri bored_talk at right
            pri "I am a firm believer that, if I teach you youngsters to respect public decency, I can prevent you from doing those horrible things to yourself and others."

            if skill_cha >= 3:
                $ add_points("principallashley_points",1)
                $ skill_cha -= 2
                $ renpy.notify("You used 2 Charisma Points")
                show pov embarrassed_talk at left
                show pri bored at right
                pov "Wow, Director Lashley. I don't know what to say"
                show pri embarrassed at right
                pov "I now totally understand why rules are in place and why you enforce them so heavily around here."
                pov "And nowadays, it seems educational facilities and such places make policies to protect the aggressors and blame victims."
                pov "So seeing you, willing to take measures to prevent stuff from happening in the first place, is rather admirable."
                show pov embarrassed at left
                show pri embarrassed_talk at right
                pri "Thank you, [povname]. I'm glad you came around to an understanding."

    show pov embarrassed at left
    show pri confused_talk at right
    pri "Well, I better get going."
    show pov shocked at left
    show pri bored_talk at right
    pri "I shudder to imagine what he might do if I give him too much time alone in my office."
    show pov embarrassed_talk at left
    show pri bored at right
    pov "Sounds like you speak from experience."
    show pov embarrassed at left
    show pri bored_talk at right
    pri "The girls usually just steal my lipstick or stick gum under my desk; along with other tame stuff like that."
    show pri sad_talk at right
    pri "It’s the boys around here that can be quite the hassle."
    show pov smirk at left
    show pri confused_talk at right
    pri "Digging into my drawers, trying to look for answer sheets or access to permanent records; Writing something foul in my computer or notebooks, for me to find later."
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Better not keep you anymore, then."
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Have a nice day, [povname]."
    pri "May the grace of our lord shine on you."
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Y-yeah, same for you, Director Lashley."
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "Don’t be a stranger, now!"

    $ principallashley_path = 2

    jump lbl_schoolhallway2_day_setup
