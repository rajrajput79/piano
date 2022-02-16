from rainbow_controller import RainbowController
from piano_lights import LightsFromPiano
from simple_controller import ParentClass1

lights_controller = RainbowController(50)
piano_input = LightsFromPiano()
piano_input.run(lights_controller)
