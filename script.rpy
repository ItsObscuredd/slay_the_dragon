# The script of the game goes in this file. Nothing here should be taken as
# canon. This was mostly an early-stage test for display and GUI and what
# not. The following code was developed by ObscuredMedal219 using Ren'Py.
# This includes, script.rpy, gui.rpy, options.rpy, and screens.rpy. Please
# do not claim this code as your own, and credit me if it is used.
# Otherwise, have fun!

# Transforms

## Characters

transform chi_staircase:
    xalign 0.43 yalign 0.5 zoom 0.5
transform chi_midway:
    xalign 0.33 yalign 0.6 zoom 0.75
transform at_princess:
    xalign 0.5 yalign 1.0 zoom 1.0

# Variables

define vessel_count = 0

# Used in several chapters

define quiet_nice = 0
define attempted_escape = False
define asked_for_help = False

# Chapter I: The Hero and the Princess
default ci_entry_choice_1_cache = set()

# Chapter II: The Stranger
default cii_stranger_entry_choice_1_cache = set()
default cii_stranger_quiet_call_cache = set()
define attempts_to_reach_quiet = 0

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# White text for Dragon
#define n = Character("", who_color="#ffffff", what_size=25, what_xalign=0.5, what_ypos=75, what_xmaximum=1116)
define w_l = Character("", who_color="#ffffff", what_font="gui/fonts/AmaticSC-Regular.ttf", what_size=55, what_xalign=0.1, what_ypos=-700, what_xmaximum=600) # The Dragon XAlign L
define w_c = Character("", who_color="#ffffff", what_font="gui/fonts/AmaticSC-Regular.ttf", what_size=55, what_xalign=0.5, what_ypos=-700, what_xmaximum=600) # The Dragon XAlign Center
define w_r = Character("", who_color="#ffffff", what_font="gui/fonts/AmaticSC-Regular.ttf", what_size=55, what_xalign=0.9, what_ypos=-700, what_xmaximum=600) # The Dragon XAlign R

# The game starts here.


###############
## Splashscreen
###############


label splashscreen:
    scene black
    with Pause(1)

    show text "{font=gui/fonts/EastSeaDokdo-Regular.ttf}{size=50}Original game by{/size}{/font}\n{size=100}{font=gui/fonts/AmaticSC-Regular.ttf}BLACK TABBY GAMES" with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)

    show text "{font=gui/fonts/EastSeaDokdo-Regular.ttf}{size=50}Team Acheron presents" with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)

    show text "{font=gui/fonts/EastSeaDokdo-Regular.ttf}{size=50}This game is not suitable for children, or those who are easily disturbed." with dissolve
    " "
    hide text with dissolve
    with Pause(1)

    return


#################
## The Long Quiet
#################


label start:

    play music ambience fadein 3.0 loop if_changed

    scene bg quiet

    "You are torn away from something. Or something was torn away from you. Either way, something was torn away, and that something was important."
    "A feathery void is all you know. It is quiet here."
    jump quiet_count_vessels

label quiet_count_vessels:

    play music ambience fadein 3.0 loop if_changed

    scene bg quiet

    menu:
        "\[Gaze at yourself.\]":
            if vessel_count == 0:
                "You are nothing at all."
            elif vessel_count == 1:
                "You are unravelled."
            elif vessel_count == 2:
                "You are withered."
            elif vessel_count == 3:
                "You are rotting."
            elif vessel_count == 4:
                "It is you."
            play sound "sfx glass_shatter.mp3"
            jump ci_entry


#######################################
## Chapter I: The Hero and the Princess
#######################################


label ci_entry:

    play music the_dragon fadein 3.0 loop if_changed

    scene bg basement_main with None

    $ ci_entry_choice_1_cache = []

    "You are alone in a basement. It is dark, starlight vaguely illuminating the shape of a staircase on the opposite side of the room. Your wrist is chained to the wall behind you. {cps=30}This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve."
    "The air is stale and dusty, a hint of rot filtering from the wooden planks of the staircase. This is an oppressive place."
    jump ci_entry_choice_1

label ci_entry_choice_1:

    play music the_dragon fadein 3.0 loop if_changed

    scene bg basement_main

    menu:
        set ci_entry_choice_1_cache
        "\(Explore\) \"Hello? Is anyone there?\"":
            "You receive no response. No one will help you."
            $ asked_for_help = True
            jump ci_entry_choice_1
        "\(Explore\) \[Gaze at yourself.\]":
            scene bg chi_basement_floor
            show ovrly princess_hands
            with dissolve

            "It's you."

            scene bg basement_main
            with dissolve
            jump ci_entry_choice_1
        "\[Try to escape.\]":
            "You tug with all of your might on the heavy chains that bind your arm, but they do not yield."
            $ attempted_escape = True
            jump ci_quiet_arrival_1
        "\[Do nothing.\]":

            if asked_for_help == True:
                jump ci_stranger_transition

            $ attempted_escape = False
            jump ci_quiet_arrival_1

label ci_stranger_transition:

    play music ambience fadein 3.0 loop if_changed

    scene bg basement_main

    "You wait, and you wait. You do not know how long you wait in this basement."
    play sound "sfx glass_shatter.mp3"
    "Suddenly, you feel yourself split."
    play sound "sfx glass_shatter.mp3"
    "Suddenly, you feel yourself split.\nAnd then again, and again, and again."
    play sound "sfx glass_shatter.mp3"
    "Suddenly, you feel yourself split.\nAnd then again, and again, and again.\nYou split until there are endless basements and endless yous, an endless fractal of cabins and Princesses."
    "And then the world ends."

    jump cii_stranger_entry

label ci_quiet_arrival_1:

    play music the_dragon fadein 3.0 loop if_changed

    scene bg basement_main

    play sound "sfx cabin_door.mp3"
    "You hear the muffled sound of a door opening upstairs. Something is here."
    play sound ["sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3", "sfx blade_scrape.mp3"]
    pause(4.5)
    play music face_of_the_earth fadein 3.0 loop if_changed
    "You hear the {i}thump, thump, thump{/i} of heavy footsteps. Then, something sharp scraping off of wood."
    play sound ["sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3", "sfx cabin_door.mp3"]
    "{i}Thump, thump, thump.{/i} The sound of a door opening. Closer. It is on the stairs."
    "It halts."

    menu:
        "\"H-hello? Is anyone there?\"":
            $ quiet_nice = True
            jump c1_quiet_arrival_2
        "\"Who's there?\"":
            $ quiet_nice = False
            jump c1_quiet_arrival_2

label c1_quiet_arrival_2:

    play music face_of_the_earth fadein 3.0 loop if_changed

    if quiet_nice == True:
        if attempted_escape == True:
            w_l "Hi!"
        else:
            w_l "Just checking in on you."
    else:
        if attempted_escape == True:
            w_l "Hey, I think I'm here to kill you?"
    
    play sound ["sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3"]
    "It continues down the stairs."
    show dragon stare at chi_staircase
    with dissolve
    "It finally comes into view, a pristine blade gripped tightly in its hand, the world trailing behind it. This is a monster."
    "It stares at you quietly."

    menu:
        "\"And there you are. Are you really here to kill me?\"":
            show dragon tilt_l at chi_staircase
            with dissolve
            "It pauses, its face blank. Is it confused? Inquisitive? Hostile?"
            if quiet_nice == True:
                if attempted_escape == True:
                    show dragon hero at chi_staircase
                    with dissolve
                    "Silence still as soft eyes glance at you."
                    show dragon hero_talk at chi_staircase
                    with dissolve
                    w_l "What? No, of course not! What makes you say that?"
                else:
                    show dragon cold at chi_staircase
                    with dissolve
                    "Silence still as cold eyes regard you."
                    show dragon cold_talk at chi_staircase
                    with dissolve
                    w_l "No, I just want to talk."
            else:
                if attempted_escape == True:
                    show dragon cold at chi_staircase
                    with dissolve
                    "Silence still as cold eyes regard you."
                    show dragon cold_talk at chi_staircase
                    with dissolve
                    w_l "I just want to talk."
                else:
                    show dragon opportunist at chi_staircase
                    with dissolve
                    "Silence still as its eyes search for an opportunity."
                    play sound "sfx tlq_footstep.mp3"
                    show dragon opportunist_b at chi_midway
                    with dissolve
                    "Still silent, it takes a step closer."
                    jump chi_princess_warning_1

label chi_princess_warning_1:

    play music face_of_the_earth fadein 3.0 loop if_changed

    menu:
        "\"Oh? Do you really want to do that? If you want to kill me, you'll have to get close enough to use that blade. Best not to risk finding out what I can do.":
            "It ignores your threat."
            jump slay_the_princess
        "\[Say nothing.\]":
            jump slay_the_princess

label slay_the_princess:
    scene bg dragon_opportunist_prestab
    with fade
    "You feel small as it rushes forward, pristine blade raised."
    scene bg dragon_opportunist_stab
    with dissolve
    "It sends the blade deep into your heart."

    menu:
        "\"O-oh.\"":
            jump chi_princess_dying_1
        "\[Die.\]":
            jump chi_princess_dying_1

label chi_princess_dying_1:
    return


###########################
## Chapter II: The Stranger
###########################


label cii_stranger_entry:

    play music metamorphosis fadein 3.0 loop if_changed
    
    scene bg basement_stranger

    "You are alone in a basement. It is dark, starlight vaguely illuminating the shape of a blank staircase on the opposite side of the blank room. Your wrist is chained to the blank wall behind you. {cps=30}This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve."
    "The air is empty. The scent of the room is a scent that can only be described as the blending of everything at once, all culminating into a nauseating nothing."
    jump cii_stranger_entry_choice_1

label cii_stranger_entry_choice_1:

    play music metamorphosis fadein 3.0 loop if_changed

    scene bg basement_stranger

    menu:
        set cii_stranger_entry_choice_1_cache

        "\(Explore\) \"Hello? Is anyone there?\"":
            "You receive no response."
            $ asked_for_help = True
            jump cii_stranger_entry_choice_1
        "\(Explore\) \[Gaze at yourself.\]":
            scene black
            with dissolve

            show ovrly princess_hands
            with dissolve

            "It's you."

            scene bg basement_stranger
            with dissolve
            jump cii_stranger_entry_choice_1
        "\[Try to escape.\]":
            "You tug with all of your might on the heavy chains that bind your arm, but they do not yield."
            $ attempted_escape = True
            jump cii_stranger_quiet_arrival_1
        "\[Do nothing.\]":
            $ attempted_escape = False
            jump cii_stranger_quiet_arrival_1

label cii_stranger_quiet_arrival_1:

    play music metamorphosis fadein 3.0 loop if_changed
    
    scene bg basement_stranger

    "You feel the approach of a consciousness other than your own."
    "You wait."

    play music stranger_compound_eyes fadein 3.0 loop if_changed

    show dragon stare at chi_staircase
    with None
    "It is here."
    "It does not move, or speak, or even have a readable expression."
    jump cii_stranger_quiet_call

label cii_stranger_quiet_call:

    #scene bg basement_stranger

    #show dragon stare at chi_staircase
    #with None

    if attempts_to_reach_quiet == 7:
        jump cii_stranger_quiet_questioning

    menu:
        set cii_stranger_quiet_call_cache
        "\(Explore\) \"Hello?\"":
            pass
        "\(Explore\) \"Are you there?\"":
            pass
        "\(Explore\) \"What are you?\"":
            pass
        "\(Explore\) \"Can you tell me your name?\"":
            pass
        "\(Explore\) \"Are you okay?\"":
            pass
        "\(Explore\) \"Why are you staring?\"":
            pass
        "\(Explore\) \[Rattle your chains to get his attention.\]":
            pass
    
    if attempts_to_reach_quiet < 6:
        "It does not respond."
    else:
        "You wait. All you can do is wait."
    
    $ attempts_to_reach_quiet += 1
    
    jump cii_stranger_quiet_call

label cii_stranger_quiet_questioning:

    show dragon tilt_l at chi_staircase
    with dissolve

    "It tilts its head, as if it finally realized it existed."

    show dragon hero at chi_staircase
    with dissolve

    "It looks around for a moment. Then it looks back at you."

    show dragon hero_talk at chi_staircase
    with dissolve

    w_l "How long have I been here?"

    show dragon hero at chi_staircase
    with dissolve

    menu:
        
        "\"Oh, you're finally awake.\"":
            show dragon tilt_l at chi_staircase
            with dissolve
            "It tilts its head. Is it inquisitive? Hostile? Confused?"
        "\"Hello.\"":
            show dragon cold_talk at chi_staircase
            with dissolve
            w_l "Hello."
        "\"You've been here a few minutes at most.\"":
            show dragon stare at chi_staircase
            with dissolve
            "Silence as the consciousness in front of you falls back into itself."
    
    jump cii_stranger_quiet_talk_1

label cii_stranger_quiet_talk_1:

    play sound ["sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3", "sfx tlq_footstep.mp3"]

    scene bg basement_stranger

    show dragon stare_a at chi_midway
    with dissolve

    pause(2)
    show dragon stare at at_princess
    with dissolve

    n "It comes closer to speak with you."
    w_l "How long have you been here?"

    menu:
        "\"Too long.\"":
            pass
        "\"Longer than I'd like to be.\"":
            pass
        "\"Long enough.\"":
            pass

    "You feel yourself fracture, your personality, and very consciousness split."

    show dragon tilt_l at at_princess
    with dissolve

    n "The Dragon tilts its head at you, and remains silent. After a bit, it speaks."
    w_l "What's your name?"

    show dragon stare at at_princess
    with dissolve

    menu:
        "\"Call me Princess.\"\n\n• \"You can refer to me as 'Your Royal Highness.'\"":
            pass
        "\"Princess.\"\n\n• \"That's 'Your Royal Highness' to you.\"":
            pass
        "\[Say nothing.\]\n\n• \"I don't need to tell you, and I won't.\"":
            pass
    
    "You fracture another time. You are neutral, but you are harsh. Harsh, but you are gentle."

    show dragon hero
    with dissolve

    "Concern. The Dragon stares at you for a long moment."

    show dragon hero_talk
    with dissolve

    w_l "Do you know {i}why{/i} you're here?"

    show dragon hero
    with dissolve

    menu:
        "\"No.\"\n\n• \"I don't know.\"\n\n• \"Umm... I don't.\"":
            pass
        "\"No. Do you?\"\n\n• \"I was hoping you'd tell me.\"\n\n• \"I was thinking maybe you do?\"":
            pass
        "\[Shake your head.\]\n\n• \"Nope.\"\n\n• \"I wish I did, but I don't.\"":
            pass

# Gordon Freeman died at the end of All Dogs Go to Heaven 2.