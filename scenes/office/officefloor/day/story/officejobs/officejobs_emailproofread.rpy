#########################################################################################
## TYPING EMAILS
label lbl_office_jobs_tutorial_email_proofread:
    default email_word_1 = "motherfuckers"#fine people
    default email_word_2 = "shit for brains"#unprofessionalism
    default email_word_3 = "head-fuckwad"#management
    default email_word_4 = "dumbass"#busy_hands
    default email_word_5 = "assholes"#gentlemen
    default email_word_6 = "assholes"#gentlemen
    default email_word_7 = "assholes"#gentlemen

    default cntdwn_number_of_correcting_tries = 8
    default cntdwn_number_of_swears_to_fix = 5
    default grind_stage = 0
    #$ renpy.checkpoint(hard=True)
    #$ renpy.suspend_rollback(True)


##########################################
## INSTRUCTIONS
    mrf "This task requires you to proofread emails made by Eloise."
    mrf "She prefers using voice to text so her language may sound a little-"
    mrf "Straightforward and colorful at times."
    mrf "Your job is to straigten things out and have it ready to be sent out."
    mrf "Look for all the innaproriate wordings and replace it with something more professional."
    mrf "Don't waste time trying to change things that don't need changing."



    #jump lbl_officejobs_emailproofread
    jump lbl_email_proofread_tutorial

##########################################
## OFFICE JOB
label lbl_officejobs_emailproofread:
    #$ renpy.checkpoint(hard=True)
    $ grind_stage += 1
    if grind_stage == 1:
        $ email_word_1 = "perverted cumrags"#rowdy employees
        $ email_word_2 = "fucking"#enormous
        $ email_word_3 = "saggy-ass titties"#inappropriate imagery
        $ email_word_4 = "downright fucking"#extreme flirting
        $ email_word_5 = "fuckery"#prank
        $ cntdwn_number_of_swears_to_fix = 5
    elif grind_stage == 2:
        $ email_word_1 = "actual fuck"#world
        $ email_word_2 = "fucking degenerates"#sexually proactive minds
        $ email_word_3 = "goddamned"#uncalled for
        $ email_word_4 = "shitty"#amateur
        $ email_word_5 = "pathetic virgin perverts"#members of society
        $ email_word_6 = "ejaculate"#say a prayer
        $ cntdwn_number_of_swears_to_fix = 6
    elif grind_stage == 3:
        $ email_word_1 = "dumbass pieces of shit"#unprofessional bullies
        $ email_word_2 = "fucking"#immature
        $ email_word_3 = "unloved bastards"#young-blood
        $ email_word_4 = "shitty"#confusing
        $ email_word_5 = "basic bitch"#inexpensive
        $ email_word_6 = "fucking"#proper
        $ email_word_7 = "miniature dicks"#coffee breaks
        $ cntdwn_number_of_swears_to_fix = 7

    $ cntdwn_number_of_correcting_tries = 8

    #show screen scr_email_proofread
    #with fade

    #$ Function('turn_on_email_correcting_hyperlink_functions')
    #$ renpy.pause(1.0)
    #$ renpy.suspend_rollback(True)

    #call screen scr_email_proofread
    jump lbl_email_proofread_tutorial

##########################################
## SCREENS
screen scr_blocker():
    modal True

screen scr_email_proofread():
    #$ renpy.fix_rollback()
    #on "show" action Function('turn_on_email_correcting_hyperlink_functions')
    #on "hide" action Function('turn_off_email_correcting_hyperlink_functions')

    add "bg emailproofread_1"

    ## WRONG
    imagebutton:
        idle "btn emailproofread_idle"
        focus_mask True
        action Jump('lbl_correction_turn_used')

    ## EMAIL
    vbox:
        xalign 0.4 yalign 0.68
        xmaximum 1400
        spacing 32
        if grind_stage == 0:
            text "This email is to be forwarded to the offices of shipment and transport of “C.B.T. Manufacturer” and it’s ceo." size 25 style "correction_text"
            text "I do not know how many times I need to keep contacting you {a=email_word_1}[email_word_1]{/a} before you’re finally able to fix our problem." size 25 style "correction_text"
            text "This is the fourth time this year where we’ve ordered new equipment in bulk from you only for it to be delayed in delivery if not downright lost within your warehouse's backlog." size 25style "correction_text"
            text "“The Robotics Company” is one of your main business partners so it pains me that this puts a strain on our business relationship due to your {a=email_word_2}[email_word_2]{/a}." size 25style "correction_text"
            text "I’ve tried to be patient and understanding of your situation considering the years we have worked together, but it’s clear to me that the new {a=email_word_3}[email_word_3]{/a} has no other interest than twiddling their thumbs and messing with MY business!" size 25 style "correction_text"
            text "If this is all too much for your {a=email_word_4}[email_word_4]{/a} to handle then perhaps it’s time I look for a new provider of equipment!" size 25 style "correction_text"
            text "Either you send the equipment we’ve requested by the end of the week, or you can expect to see us in court under breach of contract charges, {a=email_word_5}[email_word_5]{/a}." size 25 style "correction_text"
        elif grind_stage == 1:
            text "This is an email to be forwarded to all employees and interns in charge of copying and distribution of files regarding a certain incident with the copying machine." size 25 style "correction_text"
            text "I do not know which of you {a=email_word_1}[email_word_1]{/a} did this but in case you are not aware, some of you seem to have decided to slip in a little surprise with our latest monthly performance report." size 25 style "correction_text"
            text "Imagine my {a=email_word_2}[email_word_2]{/a} surprise when during a routine review of paperwork, I see a picture of {a=email_word_3}[email_word_3]{/a} stapled in the middle of the report!" size 25style "correction_text"
            text "I don’t think I need to remind all of you of the consequences of misuse of company property. But it seems I need to remind you of the consequences of {a=email_word_4}[email_word_4]{/a} in the office!" size 25style "correction_text"
            text "Had this picture been added to a report to be submitted outside of the company to a potential client or business partner, our professional reputation would be in shambles!" size 25 style "correction_text"
            text "An Investigation has already been started to determine the source of this {a=email_word_5}[email_word_5]{/a}, I recommend the people responsible to come forward and submit themselves to the appropriate termination." size 25 style "correction_text"
            text "Failure to do so and being discovered by the investigation team will result in even harsher consequences!" size 25 style "correction_text"
        elif grind_stage == 2:
            text "I send this email in response to the solicitation of “HotAssRoboBabes.com” for an interview about the possible advantages that “The Robotics Company” could bring to the Sex-Bot Industry." size 25 style "correction_text"
            text "I want to open up by asking, How in the {a=email_word_1}[email_word_1]{/a} do you dare send me one of your website’s fruit flavored condom baskets as a way to try to convince me to agree to it?!" size 25 style "correction_text"
            text "“The Robotics Company” Has never and will NEVER be involve in the production or distribution of machines designed for the entertainment of {a=email_word_2}[email_word_2]{/a} like yourself!" size 25 style "correction_text"
            text "Try to pull this {a=email_word_3}[email_word_3]{/a} stunt again and I’ll have your whole {a=email_word_4}[email_word_4]{/a} website down and all of you {a=email_word_5}[email_word_5]{/a} out of a job faster than the half a minute it takes you to {a=email_word_6}[email_word_6]{/a}!" size 25 style "correction_text"
        elif grind_stage == 3:
            text "I direct this email to the Chief Executive Officer of the up-and-coming “Cybernet Robotics” and his executive associates." size 25 style "correction_text"
            text "Let me start by saying that I hope you {a=email_word_1}[email_word_1]{/a} are having a laugh and had your {a=email_word_2}[email_word_2]{/a} fun at my expense over the rumors you started during the last robotics convention." size 25 style "correction_text"
            text "You neanderthals had the audacity to shake my hand and show your yellow and crooked smiles before going behind my back and making all sorts of accusations of my company to potential clients." size 25 style "correction_text"
            text "I want you all to know that this behavior WILL NOT go unpunished and I shall remind you I have been in this business far longer than you {a=email_word_3}[email_word_3]{/a} have had your {a=email_word_4}[email_word_4]{/a} company name!" size 25 style "correction_text"
            text "Do you really think you can just start up your company, get yourself some {a=email_word_5}[email_word_5]{/a} suits and suddenly come at the big dogs like you are the next Asimov?!" size 25 style "correction_text"
            text "We at “The Robotics Company” have a zero tolerance policy for this kind of behavior from competitors, especially the ones trying to do {a=email_word_6}[email_word_6]{/a} business with us!" size 25 style "correction_text"
            text "I hope you enjoyed your time in the robotics industry, because it’s about to be cut shorter than your {a=email_word_7}[email_word_7]{/a}!" size 25 style "correction_text"
    ## STOPWATCH
    imagebutton:
        if cntdwn_number_of_correcting_tries == 0:
            idle "img stopwatch_8"
        else:
            idle "img stopwatch_[cntdwn_number_of_correcting_tries]"
        focus_mask True
    #$ renpy.checkpoint()#hard=True
    #$ renpy.checkpoint(hard=True)
    #$ renpy.block_rollback()
    #$ renpy.fix_rollback()
    #$ renpy.suspend_rollback(True)

        # vbox:
        #
        #     # fixed xmaximum 1400:
        #         #spacing 100
        #         #xalign 0.5
        #
        #         #spacing 500
        #         #if email_word_1== 'motherfuckers':
        # vbox:
        #     ysize 7# NOTE for paragraphs that will always be double lined
        #     fixed xmaximum 1400:
        #         #spacing 100
        #         text "I do not know how many times I need to keep contacting you {a=email_word_1}[email_word_1]{/a} before you’re finally able to fix our problem." size 25 style "correction_text"
        #         #else:
        #         #    text "I do not know how many times I need to keep contacting you {a=email_word_1}[email_word_1]{/a} before you’re finally able to fix our problem." style "correction_text"
        # vbox:
        #     ysize 32
        #     fixed xmaximum 1400:
        #         #spacing 100
        #         text "This is the fourth time this year where we’ve ordered new equipment in bulk from you only for it to be delayed in delivery if not downright lost within your warehouse's backlog."  size 25style "correction_text"
        #         #else:
        #         #    text "I do not know how many times I need to keep contacting you {a=email_word_1}[email_word_1]{/a} before you’re finally able to fix our problem." style "correction_text"
        # vbox:
        #     ysize 32
        #     fixed xmaximum 1400:
        #         #spacing 100
        #         text "“The Robotics Company” is one of your main business partners so it pains me that this puts a strain on our business relationship due to your {a=email_word_2}[email_word_2]{/a}."  size 25style "correction_text"
        #         #else:
        #         #    text "I do not know how many times I need to keep contacting you {a=email_word_2}[email_word_2]{/a} before you’re finally able to fix our problem." style "correction_text"
        # vbox:
        #     ysize 32 # NOTE ysize 57 for paragraphs that will always be triple lined
        #     fixed xmaximum 1400:
        #         #spacing 100
        #         text "I’ve tried to be patient and understanding of your situation considering the years we have worked together, but it’s clear to me that the new {a=email_word_3}[email_word_3]{/a} has no other interest than twiddling their thumbs and messing with MY business!" size 25 style "correction_text"
        #         #else:
        #         #    text "I do not know how many times I need to keep contacting you {a=email_word_2}[email_word_2]{/a} before you’re finally able to fix our problem." style "correction_text"
        # vbox:
        #     ysize 7
        #     fixed xmaximum 1400:
        #         #spacing 100
        #         text "If this is all too much for your {a=email_word_4}[email_word_4]{/a} to handle then perhaps it’s time I look for a new provider of equipment!" size 25 style "correction_text"
        #         #else:
        #         #    text "I do not know how many times I need to keep contacting you {a=email_word_2}[email_word_2]{/a} before you’re finally able to fix our problem." style "correction_text"
        # vbox:
        #     ysize 7
        #     fixed xmaximum 1400:
        #         #spacing 100
        #         text "Either you send the equipment we’ve requested by the end of the week, or you can expect to see us in court under breach of contract charges, {a=email_word_5}[email_word_5]{/a}." size 25 style "correction_text"
        #         #else:
        #         #    text "I do not know how many times I need to keep contacting you {a=email_word_2}[email_word_2]{/a} before you’re finally able to fix our problem." style "correction_text"


label lbl_correction_turn_used:
    #"screen"
    $ cntdwn_number_of_correcting_tries -= 1

label lbl_email_proofread_hyperlink_return:
    #$ renpy.checkpoint(hard=True)
    pass

label lbl_email_proofread_tutorial:

    #$ renpy.block_rollback()
    #$ renpy.fix_rollback()
    #$ renpy.checkpoint(hard=True)

    #if word != None:
    #"here"
    #$ email_word_4 = "busy hands"

    #$ cntdwn_number_of_swears_to_fix -= 1
    #"[cntdwn_number_of_swears_to_fix], [cntdwn_number_of_correcting_tries]"
    #$ renpy.checkpoint()#hard=True
    #$ renpy.fix_rollback()

    if 0 in (cntdwn_number_of_correcting_tries,cntdwn_number_of_swears_to_fix):
        #if cntdwn_number_of_swears_to_fix == 0:
        show screen scr_email_proofread
        show screen scr_blocker
        $ renpy.pause(0.5,hard=True)
        hide screen scr_email_proofread
        hide screen scr_blocker
        #$ renpy.suspend_rollback(True)
        #$ renpy.checkpoint()
        #$ renpy.checkpoint(hard=True)
        #$ renpy.suspend_rollback(True)

        $ renpy.jump('lbl_after_corrections_pass_or_fail')

    call screen scr_email_proofread

##########################################
## RESULTS
label lbl_after_corrections_pass_or_fail:

    #$ style.default.hyperlink_functions = (None, None, None)
    scene bg emailproofread_2
    with fade
    #$ renpy.fix_rollback()
    #$ renpy.suspend_rollback(True)
    #$ renpy.checkpoint(hard=True)
    if cntdwn_number_of_swears_to_fix == 0:
        mrf "Good job on fixing that email. I already sent it out."
        pov "No problem, sir."
        if cntdwn_number_of_correcting_tries > 2:
            mrf "You got it done pretty quick too. I like that."
            pov "Thank you, sir."
        elif cntdwn_number_of_correcting_tries > 0:
            mrf "Try to improve on your speed for next time."
            pov "Will do, sir."
        elif cntdwn_number_of_correcting_tries == 0:
            mrf "I was just about to come check on the progress when you sent it in. Try to do it a little quicker next time."
            pov "Yes, sir."
        #TODO reward or like by mr fistem
    else:
        mrf "Are you still working on that email? Nevermind. Forward what you have over to me."
        pov "Yes sir."

    scene black
    with fade
    #$ renpy.fix_rollback()
    ## FIRST SHIFT / TUTORIAL
    if main_story <= 100:
        $ internship_job_tutorial_completed_email_proofread = True
        if internship_job_tutorial_completed_coffee_runs and internship_job_tutorial_completed_copy_machine:
            jump lbl_completed_all_office_training
        else:
            jump lbl_office_jobs_tutorials
    ## DAILY GRIND
    else:
        $ officejobs_complete += 1
        $ officejobs_emailproofread = 1

        if main_story == 101:
            if officejobs_complete == 1:
                jump lbl_daily_grind_part1_jobs_midscene
            else:
                jump lbl_daily_grind_part1_jobs_end
        elif main_story == 102:
            if officejobs_complete == 1:
                jump lbl_daily_grind_part2_jobs_midscene
            else:
                jump lbl_daily_grind_part2_jobs_end
        elif main_story == 103:
            if officejobs_complete == 1:
                jump lbl_daily_grind_part3_jobs_menu
            else:
                jump lbl_daily_grind_part3_jobs_end
        ## NON-MAIN STORY
        else:
            jump lbl_officefloor_day_setup
