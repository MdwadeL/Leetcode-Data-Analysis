# 595 Big Countries
World(name, continent, area, population, gdp)
PK = {name}

| name        | continent | area    | population | gdp          |
| ----------- | --------- | ------- | ---------- | ------------ |
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |

<br>

A country is big if one of the following conditions is met:
- area > 3,000,000 km2
- population > 25,000,000
Write a solution to find the name, population, and area of the big countries.

## Skills
- Multi Conditional Filtering
- Filtering rows
- Boolean OR
- Numeric comparisons
  
# Solution 

  return world[
        (world['area'] >= 3000000) |
        (world['population'] >= 25000000)
    ][['name', 'population', 'area']]

| name        | population | area    |
| ----------- | ---------- | ------- |
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
