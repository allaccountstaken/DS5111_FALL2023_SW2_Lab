import sys
sys.path.append(".")
import pytest
import os
from sys import platform
from bin.perceptron import Perceptron # TODO: import the perceptron directly

def test_perceptron():
    # Given properly initialized perceptron
    the_perceptron = Perceptron()
    # When inputs and labels are provided
    the_perceptron.train([[1,1],[1,0],[0,1],[0,0],], # inputs
                         [1,1,1,0]) # labels
    # Then labels should be produced in predictions
    assert the_perceptron.predict([1,1]) ==  1, "test [1,1] result in 1"
    assert the_perceptron.predict([1,0]) ==  1, "test [1,0] result in 1"
    assert the_perceptron.predict([0,1]) ==  1, "test [0,1] result in 1"
    assert the_perceptron.predict([0,0]) ==  0, "test [0,0] result in 0"

# TODO: add the proper pytest decorator, so that it is obvious it is expected to fail, XFAIL
@pytest.mark.xfail(reason="expected to fail", strict=False)
def test_tofail():
    # Given properly initialized perceptron
    the_perceptron = Perceptron()
    # When inputs and labels are provided
    the_perceptron.train([[1,1],[1,0],[0,1],[0,0],], # inputs
                         [1,1,1,0]) # true labels
    # Then label 10 should not be produced in predictions
    assert the_perceptron.predict([1,1]) ==  10, "failing assertion"


# TODO: write a test that is conditionally skipped, skipif the OS is not linux ubuntu and vs
@pytest.mark.skipif(platform != 'darwin', reason="this test for Mac OS only")
def test_forMacOSonly():
    print("This test should only run on Mac OS and the current platform is", platform)


@pytest.mark.skipif(platform != 'Linux', reason="this test for Ubuntu only")
def test_forUbuntuOSonly():
    print("This test should only run on Ubuntu OS and the current platform is", platform)
    # Given os.popen is available, run Linux bash command
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    # Then assert memory usage
    assert total_memory > 0, 'Linux total memory is greater than 0'
    assert used_memory > 0, 'Linux used memory is greater than 0'
    assert free_memory > 0, 'Linux free memory is greater than 0'

# TODO: Write another test, put a bogus reason in your decorator like This test is not yet ready for 
# prime time and add the decorator so the test is always skipped.
@pytest.mark.skip(reason="Not ready for prime time")
def test_primetime():
    print("This test should be alsways skipped")


# TODO: parametarization, say you wanted to run 3 or 5 or 10. The inputs should be "trainingset, labels, expected". Have at least 5 or 6 different datasets and make the test run. 

@pytest.mark.parametrize("trainingset, labels, expected", #three type of things used in test
                         [
                          ([[1,1], [1,0], [0,1], [0,0]], [1,1,1,0], [1,1,1,0]), # this row is true data
                          ([[0,0], [0,0], [0,0], [0,0]], [0,0,0,0], [0,0,0,0]), # default all 0 case
                          ([[1,1], [1,1], [1,1], [1,1]], [1,1,1,1], [1,1,1,1]), # default all 1s case
                          ([[1,1], [1,0], [0,1], [0,0]], [1,1,1,1], [1,1,1,1]), # wrong lables
                          ([[1,1], [1,0], [1,1], [0,0]], [1,1,1,0], [1,1,1,0]) # different traing 
                         ])
def test_papametrized(trainingset, labels, expected):
    # Given properly initialized perceptron
    the_perceptron = Perceptron()
    # When inputs and labels are provided
    the_perceptron.train(trainingset, labels)
    # Then check if predictions match expected
    for n, true_labels in zip(trainingset, expected):
        assert the_perceptron.predict(n) == true_labels, f"testing for row number {n}"

# TODO fixtures. instead of training a Perceptron with the same data set for 3 tests,
#  have the Perceptron trained once in a function, and use a fixture to provide that to each of the 3 tests.
