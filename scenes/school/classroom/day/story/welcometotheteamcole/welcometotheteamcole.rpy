## Welcome To The Team Cole
label lbl_welcome_to_the_team_cole:
    "Attend detention?"
    menu:
        "Yes":
            $ gtime = 1
            pass
        "No":
            jump lbl_classroom_day

    scene black
    with fade
    $ renpy.pause()
    "After class and in your seats..."

    ## CG
    scene bg detentionmainstory_1
    with fade

    pov "Alright, gang."
    pov "Did we manage to get our hands on some flyers?"
    pov "I- unfortunately got some but none of them has the map at the back."
    pov "Which is incredibly odd, don’t you think?"
    pov "Why would you have a map originally but then take it off?"

    jac "Mine doesn’t have the map either."

    eff "Neither does mine."

    col "Same. I even asked around and everyone I asked has either thrown them away or doesn’t have the older ones."

    edw "What the fuck is going on? That is extremely suspicious."

    col "We NEED to get those flyers back from Lashley."

    eff "What makes you think she has them?"

    col "What makes you think she doesn’t?"

    eff "She probably thinks its trash and in the trash it went."

    col "I beg to differ."
    col "I have been in her office many times and I have seen her confiscation drawer."
    col "She is not the type to take something from someone just to trash."

    jac "Are you sure about that?"
    jac "What about my-"

    col "Your hentai book is still in there, yes, Jacob."

    jac "Phew! That was a pre-order."

    edw "We need to sneak into her office and take back what’s ours."

    jac "We should probably grab the flyers too."

    eff "…"
    eff "Assuming it isn’t trashed."

    col "Assuming it isn’t trashed."
    col "It won’t be, trust me."
    col "Do you wanna bet on it?"
    col "Seriously, do you wanna make a bet?"

    edw "Dude, you have a gambling problem."

    col "I’m high risk, high reward, baby."

    eff "No, bets."
    eff "But I don’t know- is it worth trying?"

    pov "Yes, it is very much worth trying. We need those maps because we need to know where this location is."

    jac "Why don’t we all just sign up to it?"

    eff "It’s too dangerous, Jacob."

    jac "More dangerous than what? Sneaking into said location?"
    jac "We can blend in more if we sign up, just because we do, doesn’t mean we actually wanna be in the cult, right?"
    jac "I think that’ll be way easier."

    edw "I’m with Eff, there’s no knowing what kind of initiation ritual they have in store for the new recruits."
    edw "They could drug us in so many ways and mask it as an initiation."
    edw "If we sneak in and blend in as established members, we can bypass any dangerous newcomer ritual."

    jac "Okay…"
    jac "But what if-"

    pov "I agree with everyone else. These cults tend to target the greenies and we don’t want to have the spotlight on us."
    pov "I vote for sneaking into said location and blending in as established members."

    jac "Fine."
    jac "We just gotta figure out how to-"

    coa "{i}*Grumble*{/i}"
    coa "H-"
    coa "Hey!"
    coa "What’rya’ll tal’mbout there?"
    coa "*Gulp*"
    coa "Your yapping is too loud!"

    col "Sorry, coach!"
    col "*Whisper* Maybe we should talk about this somewhere else."

    eff "The hideout?"

    col "Ooh- wait- where’s that? Can I come?"

    edw "Uhmm-"
    edw "[povname]?"

    pov "Yeah, Cole’s in."

    col "Yeesssssssssssss~"

    jac "Welcome aboard, bud."

    edw "I’ll send you the details later, it’s kinda off the gr-"

    coa "YO!"
    coa "Shut it!"
    coa "Detention. Remember?"

    jac "Sorry, coach!"

    scene black
    with fade
    $ renpy.pause()
    "After detention…"

    scene bg schoolyard_day
    with fade

    $ main_story = 153

    jump lbl_schoolyard_day_setup
