# INPUTS
dy = lambda x,y: 4*x + y**2
x0, y0 = 0, -1
h = 0.3
end = 1.5

# CALCULATIONS
steps = int((end-x0)/h)
x_past = x0
y_past = y0
print(f"x0 = {x_past}, y0 = {y_past}")
for step in range(steps):
    y_next = y_past + h*(dy(x_past, y_past))
    x_next = x_past+h
    print(f"x{step+1} = {x_next}, y{step+1} = {y_next}")
    x_past, y_past = x_next, y_next


