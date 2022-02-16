from simple_controller import SimpleController
from piano_lights import LightsFromPiano
from simple_controller import ParentClass1

lights_controller = SimpleController(5, (244,0,0), (0,0,255))
piano_input = LightsFromPiano()
piano_input.run(lights_controller)
