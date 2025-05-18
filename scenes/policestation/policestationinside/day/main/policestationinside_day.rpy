###############
## Setup
## Story Path
label lbl_policestationinside_day_setup:
    jump lbl_policestationinside_day

###############
## Room Navigation
## This is the map for Police Station inside during the day
label lbl_policestationinside_day:
    scene bg policestationinside_daynight
    call screen scr_policestationinside_day

screen scr_policestationinside_day():
    imagebutton auto "btn policestationinside_daynight_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationoutside_day_setup")
    imagebutton auto "btn policestationinside_daynight_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationinside_day_door")
    imagebutton auto "btn policestationinside_daynight_frontdesk_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationinside_day_frontdesk")

    use hud_overlay

###############
## Labels
label lbl_policestationinside_day_door:
    pov "{i}I am not authorized to go in there at this moment.{/i}"

    jump lbl_policestationinside_day

label lbl_policestationinside_day_frontdesk:
    if main_story >= 60:
        menu:
            "Ask to speak with Officer Mina":
                pov "Hi there."
                pol "Yes, what can I help you with?"
                pov "I was wondering if I could talk to Officer Mina."

                ## Investigations
                if main_story >= 83 and investigations_complete == 0:
                    pol "Sorry, she's very busy right now. You'll have to come back later."
                    jump lbl_policestationinside_day
                elif main_story >= 85:
                    pass

                pol "May I ask for your name and reason for your visit."
                pov "Uhm.. [povname]. It's kind of an urgent, private matter."
                pol "Sir-"
                pov "Please, just mention me, she'll know."
                pol "{i}*Sigh*{/i} I'll see if she's in. Please wait over there."

                scene black
                with fade
                $ renpy.pause()
                "After some time and some weird looks from the police..."

                scene bg policestationinside_daynight
                with dissolve
                show pov neutral at left
                with dissolve
                show min confused_talk at right
                with dissolve
                mina "[povname]? What was so important that you had to call me for?"

                menu:
                    "Have some fun in the back room":
                        show pov smirk_talk at left
                        show min confused at right
                        pov "Well, seeing this is usually when you have your break."
                        show min smirk at right
                        pov "Wondering if you wanted to take a break with me."
                        show pov smirk at left
                        show min smirk_talk at right
                        mina "Ahh~ You know what? Let's make it quick though."
                        show min confused_talk at right
                        mina "I'm pretty damn busy today."

                        jump lbl_mina_standing_legup

                    "Nevermind":
                        show pov confused_talk at left
                        show min bored at right
                        pov "Nevermind, it looks like you aren't in a mood."
                        show pov confused at left
                        show min bored_talk at right
                        mina "Stop wasting my time, [povname]. Go take your trouble somewhere else."

                        jump lbl_policestationinside_day

            "Nevermind":
                pass
    else:
        pov "{i}I don't have any inquiries at the moment.{/i}"
        #"Developer Note: If you're looking for the sex scene with Officer Mina, you have to have reached Chapter 60 of the Main Story first."

    jump lbl_policestationinside_day
