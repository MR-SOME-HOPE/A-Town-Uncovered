## Dateish Night (Room)
label lbl_dateish_night_room:
    ## CG
    #-Scene has Mc and Effie sitting on her bed next to each other while looking at the laptop-

    scene bg dateishnight_1
    with fade
    pov "You know, when [sister] said you had a horror movie series you wanted to binge, I was expecting something like Tuesday the 10th or maybe The Massacre on 34th Street."

    show bg dateishnight_2
    eff "Classics in their very deserved right but they've been seen to death by now."

    show bg dateishnight_3
    pov "Still, gotta say that these Downward films ain't bad at all."

    show bg dateishnight_4
    eff "Nothing like girl power while running away from hideous cave cannibals because of one very shitty friend to set the mood, am I right?"

    show bg dateishnight_3
    pov "I ain't sure what kind of mood you are trying to make here but I can't say I'm complaining."

    show bg dateishnight_2
    eff "Heh, you just watch and you'll see."
    eff "Still, don't you think it's nice?"

    show bg dateishnight_6
    pov "Watching women get trapped in super claustrophobic environments only to get eaten alive by blind cannibal monsters?"
    pov "Not exactly my idea of nice to be real honest with ya."

    show bg dateishnight_7
    eff "Not that, doofus!"
    show bg dateishnight_8
    eff "I'm talking about our little movie night and all!"
    eff "I mean, I think this must be the longest we've been together at my place, right?"
    eff "Usually I'm either crashing at yours or we are hanging out somewhere else outside with Jacob tagging along."
    eff "And when we are here on our own we usually are… Busy with other stuff, so we don't really hang out in the traditional sense."

    show bg dateishnight_9
    pov "That's true but I do still enjoy your company regardless of the place and who we are with, you know?"

    show bg dateishnight_10
    eff "Heh, Thanks. I think I needed to hear that tonight."

    show bg dateishnight_11
    pov "How come?"

    show bg dateishnight_10
    eff "Girls like compliments, [povname]. In case you weren't aware."
    eff "That and…"
    eff "I don't know, I guess I'm still shaken up about a few things."
    eff "Mind's been pretty much all over the place lately."

    show bg dateishnight_11
    pov "Penny for your thoughts?"

    show bg dateishnight_12
    eff "Just… Some things I'm trying to wrap my head around lately…"

    show bg dateishnight_11
    pov "Been a bit of a crazy week, huh?"

    show bg dateishnight_10
    eff "Heh, you can say that again."
    eff "Still, for as sudden as it was, I'm quite happy we can spend some time like this."
    eff "Though, I'm sure you likely were expecting to be out of your pants by now~"

    show bg dateishnight_11
    pov "Didn't even cross my mind."

    show bg dateishnight_4
    eff "Is that so? Perhaps I should try harder then~"

    show bg dateishnight_3
    pov "Always the tease with a comeback for everything, huh?"

    show bg dateishnight_4
    eff "Patented Effie vibes. If I'm not like that, you are authorized to assume I've been replaced by an evil clone."

    show bg dateishnight_9
    pov "I shudder just imagining what an evil you must be like."

    show bg dateishnight_5
    eff "Meanwhile I'm wondering whether my evil clone would be a top or a bottom and if it would be considered incest to bang your own clone."

    show bg dateishnight_3
    pov "The real questions all scientists must be asking when they discuss the possibility of cloning."

    show bg dateishnight_4
    eff "Heh, you say that I’m always teasing you, but you are always ready to quip me right back and follow along with my banter."

    show bg dateishnight_9
    pov "Well, I can’t just leave you hanging like that, can I?"

    show bg dateishnight_10
    eff "I really appreciate it, you know?"
    eff "It’s really comforting to have someone I can just be myself to the fullest and not have to explain my jokes or tame my reactions and all."
    eff "I quite like that about you."

    show bg dateishnight_9
    pov "Well, I’m glad to hear that."

    show bg dateishnight_10
    eff "I mean what I’m saying."

    show bg dateishnight_9
    pov "I know."

    show bg dateishnight_12
    eff "Do you really?"

    show bg dateishnight_9
    pov "Well… At least I want to think that I do."
    pov "I’ve learned it’s better to not go around guessing when it comes to this sorts of things."

    show bg dateishnight_4
    eff "Hmm, smart decision."
    eff "Though you should know that girls like a man who knows what we are thinking and can take charge of the situation."

    show bg dateishnight_3
    pov "And guys love a woman who can speak her mind and doesn’t keep us guessing."

    show bg dateishnight_4
    eff "Heh, I guess you got me there yet again."

    show bg dateishnight_9
    pov "So, how about you tell me for once how you feel rather than keeping me guessing?"

    show bg dateishnight_4
    eff "Ooooh~ Look at you now trying to take charge~"

    show bg dateishnight_11
    pov "I’ve been told that girls like that in a man~"

    show bg dateishnight_8
    eff "Oh zip it already, you tease!"

    show bg dateishnight_9
    pov "I’m still waiting for an answer."

    show bg dateishnight_12
    eff "...I don’t know."

    show bg dateishnight_13
    pov "Not the answer I was expecting here."

    show bg dateishnight_12
    eff "I know."
    eff "I really wish I could give you a clear answer, but..."
    eff "Well, this is all new to me as well."
    eff "On one hand, I won’t deny that I have some feelings and you make me feel a certain way and I’m interested to see how much deeper this could go."
    eff "But on the other hand, I don’t want to mess with what we have just cause I’m feeling a certain way..."
    eff "I just need some time to process things."

    show bg dateishnight_11
    pov "Hey, I ain’t in no rush."
    pov "At the very least, I’m happy to know you like me that way, even if you are still not sure what to do about it."
    pov "Take your time to sort things out, I’ll still feel the same way about you as I do now."

    show bg dateishnight_4
    eff "Oh?"
    eff "And just how exactly do you feel about me right now, handsome?"

    show bg dateishnight_3
    pov "How about you come find out?"

    show bg dateishnight_4
    eff "I’d thought you’d never ask~"

    jump lbl_dateish_night_room_sex

    ## HSCENES
    #-Effie pushes the MC down on the bed and gets on top of him before proceeding to make out before the sex scene begins-

label lbl_dateish_night_room_sex:
    $ dateishnight_sex = 1

    scene bg dateishnight_sex_1
    with fade

label lbl_dateish_night_room_sex_0:
    jump lbl_dateish_night_room_sex_1

label lbl_dateish_night_room_sex_1:
    scene img_dateish_night_room_sex_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_dateish_night_room_sex_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_dateish_night_room_sex_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_1

image img_dateish_night_room_sex_1:
    "bg dateishnight_sex_1"
    pause 0.3
    "bg dateishnight_sex_2"
    pause 0.1
    "bg dateishnight_sex_3"
    pause 0.1
    "bg dateishnight_sex_4"
    pause 0.2
    "bg dateishnight_sex_2"
    pause 0.2
    repeat

label lbl_dateish_night_room_sex_2:
    scene img_dateish_night_room_sex_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_dateish_night_room_sex_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_dateish_night_room_sex_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_2

image img_dateish_night_room_sex_2:
    "bg dateishnight_sex_1"
    pause 0.3
    "bg dateishnight_sex_2"
    pause 0.1
    "bg dateishnight_sex_4"
    pause 0.2
    "bg dateishnight_sex_2"
    pause 0.2
    repeat

label lbl_dateish_night_room_sex_3:
    scene img_dateish_night_room_sex_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_dateish_night_room_sex_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_dateish_night_room_sex_3

image img_dateish_night_room_sex_3:
    "bg dateishnight_sex_1"
    pause 0.2
    "bg dateishnight_sex_4"
    pause 0.1
    "bg dateishnight_sex_2"
    pause 0.2
    repeat

label lbl_dateish_night_room_sex_cum:
    call screen scr_dateish_night_room_sex_cum

screen scr_dateish_night_room_sex_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_dateish_night_room_sex_0")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_dateish_night_room_sex_cumming")
    else:
        pass

label lbl_dateish_night_room_sex_cumming:
    scene bg dateishnight_sex_5
    $ renpy.pause(3,hard=True)

    #-Once the scene ends we fade to black to transition immediately to the next scene-

    $ effie_path = 10

    call lbl_next_date
    call lbl_next_day

    $ gtime = 0

    scene black
    with fade
    $ renpy.pause()
    "The next morning..."

    jump lbl_meeting_your_inlaw
