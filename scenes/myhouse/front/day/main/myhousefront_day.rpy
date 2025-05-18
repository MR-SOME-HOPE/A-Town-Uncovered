###############
## Setup
label lbl_myhousefront_day_setup:
    ## Getting a Job
    if 18 <= main_story <= 20:
        if nextday_ajob == 0:
            if winc == 0:
                pov "{i}I should get a job before I show my face to [missus]. I'll go check the mall.{/i}"
            else:
                pov "{i}I should get a job before I show my face to Mom. I'll go check the mall.{/i}"
            jump lbl_townmap_setup
        elif nextday_ajob == 1:
            if main_story < 20:
                pov "{i}I found a job but I know [missus] will make a big deal about it. I'll go back later.{/i}"

                jump lbl_townmap_setup
            else:
                $ main_story = 21
                $ townmap_enabled = 0 ## DISABLE ONLY TOWNMAP
                jump lbl_myhousefront_day

    ## The Town is Crazy
    elif main_story == 33.5 and (sexaroundtowncafe and sexaroundtownbeach and sexaroundtownstreet and sexaroundtownpark and sexaroundtownretailstore) == 1:
        $ main_story = 34
        $ townmap_enabled = 0  ## DISABLE ONLY TOWNMAP
        jump lbl_myhousefront_day

    # ## A Note At The Front Door
    # elif main_story == 156:
    #     jump lbl_a_note_at_the_front_door



    ## Meet Allaway for Sex in your Bedroom
    if allawaybedroomsex_sneakherin == 1:
        if gtime != 0:
            $ allawaybedroomsex_sneakherin = 2
            if gtime == 1:
                scene bg myhousefront_day
            else:
                scene bg myhousefront_night
            show pov neutral
            pov "I guess I missed Allaway. Damn."
            if gtime == 1:
                jump lbl_myhousefront_day_setup
            else:
                jump lbl_myhousefront_night_setup
        $ gtime = 1
        jump lbl_allaway_bedroom_sex_sneakin

    ## NO EVENT
    else:
        jump lbl_myhousefront_day

###############
## Room Navigation
label lbl_myhousefront_day:

    scene bg myhousefront_day
    call screen scr_myhousefront_day

screen scr_myhousefront_day():
    imagebutton auto "btn myhousefront_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_day_setup")#If( main_story == 21, SetVariable("townmap_enabled",0) ),
    imagebutton auto "btn myhousefront_day_gate_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_day_setup")
    if newspaper <= 0:
        imagebutton auto "btn myhousefront_day_mailboxnews_%s" xpos 0 ypos 0 focus_mask True action [SetVariable("newspaper",1),Jump("lbl_newspaper_day")]
    else:
        if violette_path == 1 and main_story >= 22:
            imagebutton auto "btn myhousefront_day_mailbox_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lifeguard_training")
        else:
            imagebutton auto "btn myhousefront_day_mailbox_%s" xpos 0 ypos 0 focus_mask True action Notify("I should check this tomorrow morning.")

    use hud_overlay
