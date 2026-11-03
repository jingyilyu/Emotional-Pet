# Emotional-Pet
# Emotional Pet

## Project Overview

Emotional Pet is a Micro:bit-based interactive digital pet.  The pet uses three internal states: Happiness, Hunger and Energy.  These values change through user interaction and over time, and the Micro:bit LED display shows different emotional expressions based on the pet’s current state.

## Controls

- **Button A:** Feed the pet and reduce Hunger.
- **Button B:** Play with the pet, increase Happiness, reduce Energy and increase Hunger.
- **Shake:** Interact with the pet by increasing Happiness while reducing Energy and slightly increasing Hunger.
- **Button A + B:** Display the current Happiness, Energy and Hunger values.

## Emotional States

The pet can display different emotions on the Micro:bit LED screen, including:

- Happy
- Hungry
- Tired
- Sad

The displayed emotion is determined by the pet’s internal state and conditional logic.

## Files

- **main.py** – Source code for the project.
- **microbit-A2. hex** – Micro:bit project file that can be transferred directly to a Micro:bit.
- **The LED displays the picture of emotion.png** – Screenshot showing the LED emotion display.

## How to Run the Project

1.  Download `microbit-A2.hex`.
2.  Connect a Micro:bit to the computer using a USB cable.
3.  Copy the `. hex` file onto the Micro:bit.
4.  Wait for the file to finish transferring.
5.  Use Button A, Button B, the Shake gesture, or Button A+B to interact with the emotional pet.

## Development Environment

The project was developed using Microsoft MakeCode for Micro:bit.
