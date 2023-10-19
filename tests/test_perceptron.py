import sys
sys.path.append(".")

#import bin.clockdeco_param as cp
from bin.perceptron import Perceptron # TODO: import the perceptron directly

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  1, "assert comment"
    assert the_perceptron.predict([1,0]) ==  1, "assert comment"
    assert the_perceptron.predict([0,1]) ==  1, "assert comment"
    assert the_perceptron.predict([0,0]) ==  0, "assert comment"

# TODO: make them fail, use "f strings" for comments

# TODO: negative test, create a new test, then purposely replace the four assertion with one failing assertion
# This should show up 'red' on your test output for now, since it is of course, failing.
# TODO: add the proper pytest decorator, so that it is obvious it is expected to fail, XFAIL



# TODO: write a test that is conditionally skipped, skipif the OS is not linux ubuntu (???)





# TODO: Write another test, put a bogus reason in your decorator like This test is not yet ready for prime time and add the decorator so the test is always skipped.



# TODO: parametarization, say you wanted to run 3 or 5 or 10. The inputs should be "trainingset, labels, expected". Have at least 5 or 6 different datasets and make the test run. 




# TODO fixtures. instead of training a Perceptron with the same data set for 3 tests, have the Perceptron trained once in a function, and use a fixture to provide that to each of the 3 tests.
