import numpy as np  # to perform matrix operations like square and transpose
from manim import *  # to draw all our fancy animations

# Hi Professor Short. This is my submission for Question 9.A, a proof by exhaustion showing that
# SxS is an equivalence relation. I used Numpy (as shown above) to preform the matrix operations,
# and manim to draw all the animations. And yes, I know there were easier ways of doing this than
# a thorough proof by exhaustion.


class QuestionNinePartA(Scene):
    def construct(self):

        # This builds our adjacency matrix. I've never done something like this before,
        # so please excuse the messiness.
        set_s = [1, 2, 3, 4, 5]
        matrix = []
        for a in set_s:
            for b in set_s:
                row = []
                for c in set_s:
                    for d in set_s:
                        if a + b == c + d:  # evaluates the relation
                            row.append(1)  # if true, pop a one in there
                        else:
                            row.append(0)  # if not true, pop a zero in there
                matrix.append(row)  # once a row is done, put it into the matrix

        # I'm very new to Manim, and there's definitely a more elegant way of doing this rather than tearing
        # down scenes and rewriting them from scratch, but I couldn't find it on the cursory Google searches,
        # so we're stuck with some rather inelegant (and repeated) code. Sorry about that.

        m = IntegerMatrix(matrix)
        text = Tex(
            r"This matrix is the adjacency matrix composed of the relation defined on $S \times S$ "
            r"(where $S={1, 2, 3, 4, 5}$) as follows: $\newline$ $(a,b)R(c,d)$ if and only if $a+b=c+d$"
        )
        group = VGroup(m, text)
        group.arrange(DOWN)
        group.width = config["frame_width"] - 2 * LARGE_BUFF
        group.height = config["frame_height"] - 2 * LARGE_BUFF

        self.play(Create(m), run_time=8)
        self.play(Write(text))
        self.wait(10)
        self.play(Unwrite(text))
        self.play(Uncreate(m))

        # Check next comment for why this is so messy. Anyway, we're converting our Matrix into a Numpy array,
        # then taking the transpose of it. I did not just redraw the matrix. Also, I tried to animate the transpose
        # but because the matrix was so big, it was far more difficult than originally planned.

        m_transpose = IntegerMatrix(np.transpose(np.array(matrix)))
        text = Tex(
            r"This is the transpose of that matrix. Notice how it is identical, proving symmetry. Ones across "
            r"the diagonal proves reflexivity."
        )

        group = VGroup(m_transpose, text)
        group.arrange(DOWN)
        group.width = config["frame_width"] - 2 * LARGE_BUFF
        group.height = config["frame_height"] - 2 * LARGE_BUFF

        self.play(Create(m_transpose), run_time=8)
        self.play(Write(text))
        self.wait(10)
        self.play(Unwrite(text))
        self.play(Uncreate(m_transpose))

        # This is a really messy bit of code, necessary because Numpy doesn't like lists.
        # So we convert our matrix into an array, then square it, then feed it back into Manim.
        # To clean this up, we could probably just declare it as a Numpy array at the very beginning.

        m_array = np.array(matrix)
        np_square = np.square(m_array)
        m_square = IntegerMatrix(np_square)

        text = Tex(
            r"Now, we square the matrix, so we can prove transitivity. If there are non-zero entries in the "
            r"square of the matrix that were not there in the original, it is not transitive. Given that this "
            r"is not the case, we can thus safely conclude that this relation is an equivalence relation, as it "
            r"is reflexive, symmetric, and transitive."
        )

        group = VGroup(m_square, text)
        group.arrange(DOWN)
        group.width = config["frame_width"] - 2 * LARGE_BUFF
        group.height = config["frame_height"] - 2 * LARGE_BUFF

        self.play(Create(m_square), run_time=8)
        self.play(Write(text))
        self.wait(10)
        self.play(Unwrite(text))
        self.play(Uncreate(m_square))
