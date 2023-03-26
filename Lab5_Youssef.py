'''
Jack Youssef
2/28/2023

Lab 5, Option 2: Adding the ^ operator to reverse polish notation evaluator.

Includes the main function, which tests the PFEvaluatorModel for calculating reverse polish notations.
The files are from Chapter 7 Student Files, with the model and token files updated to include the ^ operator.
'''


from model import PFEvaluatorModel


def main():
    # Testing: 4 5 ^ , expected output: 1024
    print("4 5 ^  ==  ", end="")
    print(PFEvaluatorModel().evaluate("4 5 ^"))
    
    # Testing: 2 4 3 * ^ , expected output: 4096
    print("2 4 3 * ^  ==  ", end="")
    print(PFEvaluatorModel().evaluate("2 4 3 * ^"))

    
if __name__ == '__main__': 
    main()
    
    