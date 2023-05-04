import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    n1 = 45
    n2 = 50
    
    output = methods.addition(n1,n2)
    assert output == 95
    
def test_subtracao():
    n1 = 70
    n2 = 50
    
    output = methods.subtraction(n1,n2)
    assert output == 20
    
def test_multiplicacao():
    n1 = 5
    n2 = 4
    
    output = methods.multiplication(n1,n2)
    assert output == 20
    
def test_divisao():
    n1 = 50
    n2 = 10
    
    output = methods.division(n1,n2)
    assert output == 5
    
    