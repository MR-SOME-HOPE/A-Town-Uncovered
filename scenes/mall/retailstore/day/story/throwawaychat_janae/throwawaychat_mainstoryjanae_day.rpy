## Janae Main Story Throwaway Conversations Retail Store ##
default retailstore_ajob = 0

## A Job
label lbl_retailstore_day_janae_job:
    show pov neutral_talk at left
    with dissolve
    show jan neutral at right
    call lbl_retailstore_counter_check
    with dissolve

    pov "I was wondering if you have job opening here."
    show pov sad at left
    show jan neutral_talk at right
    jan "We have an application form you can fill out and my boss may or may not get back to you in a few weeks."
    show pov sad_talk at left
    show jan embarrassed at right
    pov "{i}*Sigh*{/i} I'll pass. I sorta need something guaranteed and stat."
    show pov confused at left
    show jan neutral_talk at right
    jan "Have you tried the ice cream parlour just across from here?"
    show pov embarrassed_talk at left
    show jan neutral at right
    pov "If I hadn't considered yet, I'm considering it now."
    show pov neutral_talk at left
    pov "Thanks, Janae."
    show pov neutral at left
    show jan neutral_talk at right
    jan "Good luck!"

    $ retailstore_ajob = 1

    jump lbl_retailstore_day_setup
