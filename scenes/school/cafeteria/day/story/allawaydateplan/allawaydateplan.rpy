## Allaway Date Plan ##
label lbl_allaway_date_plan:
    scene bg schoolcafeteria_day
    show btn schoolcafeteria_day_missallaway_idle

    menu:
        "Ask to sit with her":
            pass
        "Go on about your day":
            pov "{i}I'll just leave her be.{/i}"
            jump lbl_schoolcafeteria_day

    scene bg sitwithmissallaway_4
    with fade
    pov "Mind if I sit?"
    show bg sitwithmissallaway_5
    mis "No, be my guest. I was actually hoping you'd come by."
    show bg sitwithmissallaway_4
    pov "Really?"
    pov "Miss Allaway was actually waiting for me? [povname]. The love-struck student who can't take a no from his teacher."
    show bg sitwithmissallaway_5
    mis "Hehehe, hey, [povname]."
    show bg sitwithmissallaway_11
    mis "I'd like to apologise for being so weird and paranoid a while ago."
    mis "With the thing that happened between us..."
    show bg sitwithmissallaway_5
    mis "Uh- while I was tutoring you..."
    show bg sitwithmissallaway_11
    mis "You know the one."
    mis "Yeah, I just felt like my spidey-senses were tingling."
    mis "My eyes were catching every student laughing as if they were gossiping about us."
    mis "My ears were on edge and reacted whenever either one of our names were called."
    mis "I- was scared to even say anything remotely close to what happened in case it gave out any clues to anyone."
    mis "I'm not... wrong to be like that, right?"

    menu:
        "Not at all.":
            if missallaway_path >= 9:
                $ missallaway_path += 1
            else:
                $ missallaway_path = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased")
            show bg sitwithmissallaway_4
            pov "Not at all, I completely understand the reason for the paranoia."
            show bg sitwithmissallaway_5
            mis "{i}*Sigh*{/i} Phew... I'm glad you do. I feel like I've been a little cuckoo in the head."
        "Maybe a little.":
            show bg sitwithmissallaway_4
            pov "Maybe that's a little strange but I can understand."
            show bg sitwithmissallaway_5
            mis "Thanks, [povname]."
        "You're overreacting.":
            if missallaway_path <= 1:
                $ missallaway_path -= 1
            else:
                $ missallaway_path = 0
            $ renpy.notify("Your relationship with Miss Allaway has decreased by 1")
            show bg sitwithmissallaway_17
            pov "You're overreacting a little."
            show bg sitwithmissallaway_11
            mis "Mhmm? So I am acting crazy. Thanks."
    show bg sitwithmissallaway_16
    pov "What about that kiss?"
    pov "You seem to be dealing with it quite well. Not feeling paranoid that someone saw?"
    show bg sitwithmissallaway_15
    mis "Do you really have to bring that up out here?!"
    show bg sitwithmissallaway_14
    pov "It's fine, Miss. I didn't say it was between u-"
    show bg sitwithmissallaway_15
    mis "Shhhh! You're terrible, y'know."
    show bg sitwithmissallaway_16
    pov "You liked it, didn't you?"
    show bg sitwithmissallaway_15
    mis "No..."
    show bg sitwithmissallaway_11
    mis "Maybe..."
    show bg sitwithmissallaway_4
    pov "I liked it, if that makes you feel any better."
    show bg sitwithmissallaway_12
    mis "I know YOU like it. I'm an excellent kisser."
    show bg sitwithmissallaway_16
    pov "What makes you such an excellent kisser? You don't date very often."
    show bg sitwithmissallaway_5
    mis "Just because I don't date, doesn't mean I've never had experience."
    show bg sitwithmissallaway_4
    pov "I don't believe that."
    mis "..."

    menu:
        "Did Effie..." if skill_int >= 6 and crushonallaway_time == 1:
            show bg sitwithmissallaway_16
            pov "Did Effie have something to do with this?"
            mis "..."
            show bg sitwithmissallaway_14
            pov "Oooh lala, Effie and Allaway sitting in a tree."
            show bg sitwithmissallaway_15
            mis "Don't take this back to the 3rd grade!"
            show bg sitwithmissallaway_14
            mis "..."
            show bg sitwithmissallaway_17
            pov "I just can't help but say how hot I think it is that she was teaching YOU how to Frenchie."
            show bg sitwithmissallaway_11
            mis "Are you done embarrassing me, [povname]?"
        "You must've been a party animal.":
            show bg sitwithmissallaway_4
            pov "You must've been a party animal in your college years."
            show bg sitwithmissallaway_6
            mis "Haha, yeah... I've had some fun."
            mis "College guys dig a girl with glasses."
            show bg sitwithmissallaway_5
            mis "I think it fulfills their librarian fantasies or something."
            show bg sitwithmissallaway_4
            pov "I think it's just the glasses."
        "Maybe I'm just jealous.":
            show bg sitwithmissallaway_4
            pov "Maybe I'm just being jealous of whoever you ‘trained' with."
            show bg sitwithmissallaway_5
            mis "Hahaha... yeah."
            mis "‘trained'..."
            mis "Definitely someone you know."
            show bg sitwithmissallaway_4
            pov "You're sounding awfully suspicious. Who is it?"
            mis "..."
            show bg sitwithmissallaway_6
            mis "Just because I have spontaneous outburst, doesn't mean I'm telling you who it is."
            show bg sitwithmissallaway_8
            mis "..."
            show bg sitwithmissallaway_11
            mis "Stop staring at me like that..."
    show bg sitwithmissallaway_10
    mis "Oh! I just remembered something sort of relevant but not really."
    show bg sitwithmissallaway_16
    pov "What is it?"
    show bg sitwithmissallaway_5
    mis "I have a date soon with this guy I met on a dating site."
    show bg sitwithmissallaway_4
    pov "You have a date?"
    show bg sitwithmissallaway_8
    pov "First off, doesn't our kiss mean anything to you?"
    show bg sitwithmissallaway_4
    pov "And second, I'm surprised you already trust me enough to tell me that."
    show bg sitwithmissallaway_5
    mis "Firstly, it was just a kiss..."
    mis "People kiss all the time..."
    mis "Europeans kiss for no reason sometimes..."
    show bg sitwithmissallaway_11
    mis "And second, I never really thought about that."
    show bg sitwithmissallaway_5
    mis "I guess I do? I didn't even think of whether it was appropriate to tell you or not."
    show bg sitwithmissallaway_11
    mis "I-"
    show bg sitwithmissallaway_4
    pov "Just did."
    pov "I think you're starting to like-like me."
    show bg sitwithmissallaway_6
    mis "... You're still as cocky as ever."
    show bg sitwithmissallaway_4
    pov "I know, and I know you like it."
    show bg sitwithmissallaway_5
    mis "No comment."
    show bg sitwithmissallaway_16
    pov "Well, then. Since we're in this gray area of our relationshi-"
    show bg sitwithmissallaway_15
    mis "Can you not say it like that, the teacher-student thing we have still stands, nothing more."
    show bg sitwithmissallaway_16
    pov "Yeah, keep telling yourself that, sugar lips."
    show bg sitwithmissallaway_18
    mis "{i}*Gasp*{/i}"
    show bg sitwithmissallaway_15
    pov "When's this date of yours?"
    show bg sitwithmissallaway_12
    mis "Why should I tell you and why do you care?"
    show bg sitwithmissallaway_2
    mis "You're not going to stalk me on my date are you?"
    show bg sitwithmissallaway_3
    pov "Psssh! No..."
    pov "You make it sound more creepy than what I had in my head."
    show bg sitwithmissallaway_2
    mis "That's because it is."
    show bg sitwithmissallaway_3
    pov "..."
    show bg sitwithmissallaway_4
    pov "I just don't want you getting hurt or.."
    pov "Or what if your date is actually a serial killer?"
    show bg sitwithmissallaway_6
    mis "What if I told you that serial killers are kind of hot?"
    show bg sitwithmissallaway_8
    pov "Then I'm both worried about you and I wanna murder you and your-"
    show bg sitwithmissallaway_12
    mis "Ah-ah- don't finish that sentence."
    show bg sitwithmissallaway_5
    mis "There's nothing to worry about, [povname]. I'll be fine."
    show bg sitwithmissallaway_2
    mis "Don't stalk me, okay?"
    mis "We're just going to meet up a few hours beforehand to chat and then watch a movi-"
    show bg sitwithmissallaway_10
    mis "Woops.. I shouldn't have said that."
    show bg sitwithmissallaway_11
    mis "{i}*Sigh*{/i} I'll be fine, [povname]."
    show bg sitwithmissallaway_4
    pov "'Fine' stands for fucked up, insecure, neurotic, and emo-"
    show bg sitwithmissallaway_12
    mis "Language, [povname]. You're still on school grounds."
    show bg sitwithmissallaway_8
    pov "Sorry."
    show bg sitwithmissallaway_9
    mis "I'll head back to class, and prepare for the next period."
    show bg sitwithmissallaway_7
    pov "Alright, Miss Allaway. Nice chatting with you."
    $ missallaway_path = 14

    jump lbl_schoolcafeteria_day_setup
