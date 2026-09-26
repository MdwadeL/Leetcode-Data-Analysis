# 595 Big Countries

A big country fits one of the parameters:
        area >= 3,000,000 km^2
        population >= 25,000,000

## Skills
- multi conditional filtering
  
# Solution 1
    solution = world[
        (world['area'] >= 3000000) |
        (world['population'] >= 25000000)
    ][['name', 'population', 'area']]

    return solution
## runtime: 255 ms


# Solution 2
    return world[
        (world['area'] >= 3000000) |
        (world['population'] >= 25000000)
    ][['name', 'population', 'area']]

## runtime: 232 ms
