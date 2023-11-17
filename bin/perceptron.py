
"""
    This module is used to create, train and predict using perceptron
    """

class Perceptron:
    """
        This class represent a small model of perceptron
        """
    def __init__(self):
        """
            Create empty perceptron, set original weight to None
            """
        self._weights = None

    def train(self, inputs, labels):
        """
            Train the model by taking inputs and corresponding labels, adjust the weights
            """
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for dummy_input, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(dummy_input)
                for index, item in enumerate(dummy_input):
                    self._weights[index] += .1 * item * label_delta

    def predict(self, inputs):
        """
            Make predictions by taking new inputs and adjusted (trained) weights
            """
        if len(inputs) == 0:
            return None
        inputs = inputs + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, inputs)])) #pylint: disable=R1728
