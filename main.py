
# Button A represents the feeding action.
# It decreases hunger and ensures the value does not drop below 0.

def on_button_pressed_a():
    global Hunger
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(200)
    Hunger += -20
    if Hunger < 0:
        Hunger = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

# Buttons A and B - Physical Examination Panel

def on_button_pressed_ab():
    basic.show_string("H")
    basic.show_number(Happiness)
    basic.show_string("E")
    basic.show_number(Energy)
    basic.show_string("U")
    basic.show_number(Hunger)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Button B represets the playing action.
# It increases happiness while reducing energy and increasing hunger with 0-100 limits.

def on_button_pressed_b():
    global Happiness, Energy, Hunger
    basic.show_icon(IconNames.HEART)
    basic.pause(200)
    Happiness += 15
    if Happiness > 100:
        Happiness = 100
    Energy += -10
    if Energy < 0:
        Energy = 0
    Hunger += 5
    if Hunger > 100:
        Hunger = 100
input.on_button_pressed(Button.B, on_button_pressed_b)

# The shake gesture acts as an active physical interaction.
# It boosts happiness, drains energy and slightly increases hunger.

def on_gesture_shake():
    global Happiness, Energy, Hunger
    basic.show_icon(IconNames.HAPPY)
    Happiness += 10
    if Happiness > 100:
        Happiness = 100
    Energy += -5
    if Energy < 0:
        Energy = 0
    Hunger += 2
    if Hunger > 100:
        Hunger = 100
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Energy = 0
Hunger = 0
Happiness = 0
# Initialise the pet's internal states (Happiness, Energy, Hunger).
# And display the initial dog icon before entering the main loop.
Happiness = 50
Hunger = 20
Energy = 80
# Display the startup welcome icon (puppy/cute face) and pause for 2 seconds.
basic.show_leds("""
    # . . . #
    # # # # #
    # . # . #
    . # . # .
    . # # # .
    """)
basic.pause(2000)
# The main loop continuously checks the pet's internal states.
# And uses conditional logic with strict priority to display the corresponding emotion LED.

def on_forever():
    global Hunger, Energy, Happiness
    if Hunger > 60:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . # # .
            """)
        basic.pause(200)
        basic.clear_screen()
        basic.pause(200)
    elif Energy < 30:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            """)
    elif Happiness < 30:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
    # Over time, the pet's stats change automatically so that the pet gets hungerier, more tired and less happy even without user input.
    basic.pause(1000)
    Hunger += 3
    if Hunger > 100:
        Hunger = 100
    Energy += -2
    if Energy < 0:
        Energy = 0
    Happiness += -3
    if Happiness < 0:
        Happiness = 0
basic.forever(on_forever)

energy: number
Type a name for your project
A2
