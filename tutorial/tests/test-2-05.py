import OpenGL.GL as GL

from tutorial.core.base import Base
from tutorial.core.utils import Utils
from tutorial.core.attribute import Attribute


class Test(Base):
    """ Render shapes with vertex colors """
    def initialize(self):
        print("Initializing program...")

        # initialize program #
        vs_code = """
            in vec3 position;
            in vec3 vertexColor;
            out vec3 color;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
                color = vertexColor;
            }
        """
        fs_code = """
            in vec3 color;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(color.r, color.g, color.b, 1.0);
            }
        """
        self._program_ref = Utils.initialize_program(vs_code, fs_code)
        # render settings (optional) #
        GL.glPointSize(10)
        GL.glLineWidth(4)
        # set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # set up vertex attributes #
        position_data = [[ 0.8,  0.0,  0.0],
                         [ 0.4,  0.6,  0.0],
                         [-0.4,  0.6,  0.0],
                         [-0.8,  0.0,  0.0],
                         [-0.4, -0.6,  0.0],
                         [ 0.4, -0.6,  0.0]]
        self._vertex_count = len(position_data)
        position_attribute = Attribute("vec3", position_data)
        position_attribute.associate_variable(self._program_ref, 'position')
        color_data = [[1.0, 0.0, 0.0],
                      [1.0, 0.5, 0.0],
                      [1.0, 1.0, 0.0],
                      [0.0, 1.0, 0.0],
                      [0.0, 0.0, 1.0],
                      [0.5, 0.0, 1.0]]
        color_attribute = Attribute("vec3", color_data)
        color_attribute.associate_variable(self._program_ref, 'vertexColor')

    def update(self):
        GL.glUseProgram(self._program_ref)
        # GL.glDrawArrays(GL.GL_POINTS, 0, self._vertex_count)
        # GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self._vertex_count)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self._vertex_count)


# instantiate this class and run the program
Test().run()