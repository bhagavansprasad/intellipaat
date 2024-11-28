x1 := 7; x2 := 2; x3 := 25
w1 := 0.1; w2 := 0.16; w3 := 0.1; w4 := 0.5
w5 := 0.1; w6 := 0.6; w7 := 7; w8 := 3
b1 := -4; b2 := -4; b3 := 12
y_act := 85

# x1 := 6; x2 := 1; x3 := 32
# w1 := 0.1; w2 := 0.16; w3 := 0.1; w4 := 0.5
# w5 := 0.1; w6 := 0.6; w7 := 7; w8 := 3
# b1 := -4; b2 := -4; b3 := 12
# y_act := 65

# x1 := 8; x2 := 2; x3 := 17
# w1 := 0.1; w2 := 0.16; w3 := 0.1; w4 := 0.5
# w5 := 0.1; w6 := 0.6; w7 := 7; w8 := 3
# b1 := -4; b2 := -4; b3 := 12
# y_act := 92

# x1 := 8; x2 := 3; x3 := 19
# w1 := 0.1; w2 := 0.16; w3 := 0.1; w4 := 0.5
# w5 := 0.1; w6 := 0.6; w7 := 7; w8 := 3
# b1 := -4; b2 := -4; b3 := 12
# y_act := 95

Error: y_act y_pre
    Error = (y_act - y_pred) ** 2
    Error = (85 - 17.473) ** 2
    Error = (67.522) ** 2

y_act: Input -> Actual output 
    y_act = 85

y_pred: w7 w8 b3
    y_pred = (w7*g1) + (w8*g2) + b3
    y_pred = (7*0.354) + (3*1) + 12
    y_pred = 17.473

w7: Input-Random weight
    w7 = 7

w8: Input-Random weight
    w8 = 3

b3: random Bios
    b3 = 12
    
g1: Z1
    g1 = 1 / (1 + (e ** -Z1))
    g1 = 1 / (1 + (e ** -(-0.6))
    g1 = 0.354

Z1: w1 x1 w3 x2 w5 x3 b1
    Z1 = (w1*x1) + (w3*x2) + (w5*x3) + b1
    Z1 = (0.1*7) + (0.1*2) + (0.1*25) + (-4)
    Z1 = -0.6

w1: Input-Random weight
    w1 = 0.1

w3: Input-Random weight
    w3 = 0.1

w5: Input-Random weight
    w5 = 0.1

x1: Input - Hours of sleep
    x1 = 7

x2: Input - Count of coffee
    x2 = 2

x3: Input - Minutes of Travel
    x3 = 25

b1: random Bios
    b1 = -4
    
g2: Z2
    g2 = 1 / (1 + (e ** -Z2))
    g2 = 1 / (1 + (e ** -(13.12))
    g2 = 0.999
    g2 = 1

Z2: w2 x1 w4 x2 w6 x3 b2
    Z2 = (w2*x1) + (w4*x2) + (w6*x3) + b2
    Z2 = (0.16*7) + (0.5*2) + (0.6*25) + (-4)
    Z2 = 13.12

w2: Input-Random weight
    w2 = 0.16
    
w4: Input-Random weight
    w4 = 0.5
    
w6: Input-Random weight
    w6 = 0.6
    
x1: Input - Hours of sleep
    x1 = 7
    
x2: Input - Count of coffee
    x2 = 2

x3: Input - Minutes of Travel
    x3 = 25

b2: random Bios
    b2 = -4
