label lbl_pre_mission_briefing:
    ##-This scene serves as a final reminder for the player of who are the people that may be of use to him to find further info about the town-

    ##-The key people to ask are “Violette” “Effie” “Edward” and “Grundle Sam”, but some of the other characters may also have things to say. Keep it short in general with exception of those 4-

    ##-The Mc comes out of the house and has a moment to think, but looks apologetic over lying to Missus yet again-
    scene bg myhousefront_day
    with fade
    show pov bored_talk at left
    with dissolve
    pov "That little lie is going to buy me some time…"
    show pov sad at left
    if winc == 0:
        pov "{i}I’m sorry, [missus]. But I can’t involve you or [sister] into all of this. And the last thing I need: is you constantly keeping an eye on me.{/i}"
    else:
        pov "{i}I’m sorry, mom. But I can’t involve you or [sister] into all of this. And the last thing I need: is you constantly keeping an eye on me.{/i}"
    show pov confused at left
    pov "{i}I don’t have time to wonder about that weird call either…{/i}"
    pov "{i}Whoever it was, they did make us pay attention to the news, so that’s bound to be a hint…{/i}"
    show pov sad_talk at left
    pov "One problem at a time…"
    show pov confused_talk at left
    pov "I now gotta talk to people who may be able to tell me more about the town…"
    show pov confused at left
    pov "{i}People who either would know a lot of what goes on around town or people weird enough to care about stuff like this…{/i}"
    show pov embarrassed at left
    pov "{i}Shouldn’t be too hard… Right?{/i}"
    show pov bored_talk at left
    pov "Let’s start by the Mall and see what I can learn."

    jump lbl_myhousefront_day_setup
