import pathlib
import sys

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[2])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from py3d.core.base import Base


# Check input
class Example(Base):
    """ Create a text-based application to verify that the key-press modifications work as expected """
    def initialize(self):
        print("Initializing program...")

    def update(self):
        # # Debug printing
        # if len(self.input.key_down_list) > 0:
        #     print('Keys down:', self.input.key_down_list)
        # if len(self.input.key_pressed_list) > 0:
        #     print('Keys pressed:', self.input.key_pressed_list)
        # if len(self.input.key_up_list) > 0:
        #     print('Keys up:', self.input.key_up_list)
        # typical usage
        if self.input.is_key_down('space'):
            print("The 'space' key was just pressed down")
        if self.input.is_key_pressed('right'):
            print("The 'right' key is currently being pressed")


# Instantiate this class and run the program
Example().run()