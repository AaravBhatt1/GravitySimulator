# Gravity Simulator
This is a simple simulation of Newtonian gravity made with Pygame (the objects in space are called planets for simplicity).
## Demonstration

https://github.com/AaravBhatt1/GravitySimulator/assets/64959071/5b9e02fa-060d-4de3-bcfe-25ee2d4b0cd6

## Getting Started
### Running the Simulator
1. Create a clone of the repository using `git clone https://github.com/AaravBhatt1/GravitySimulator`.
2. Adjust the planets.json file to set starting conditions.
3. Run the file using `py main.py planets.json`.
### Using the Simulator
You can set the starting conditions by changing the `planets.json` file. In this, you can set the x and y position of the planet, the mass, and the x and y velocity. Note that the positions are relative to the cetner of the screen and positive values mean going right or going up.
Feel free to also change the constants found in the files.
When running the file, you can press space to pause and play the simulation.
## Future Updates
Updates I plan to add involve:
1. Adding error messages (custom exceptions)
2. Making the simulation keep the center of mass of the whole system at the center of the screen
3. Adding the option to set collisions such that they don't become one unified object
