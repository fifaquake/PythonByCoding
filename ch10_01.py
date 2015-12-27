import simplemodule
import simpleadvmodule

num1 = simplemodule.perform(10, 5)
print(num1)

num1 = simplemodule.calculate(4, 3)
print(num1)

city_a = simpleadvmodule.City('Hamburg', 8, 12)
city_b = simpleadvmodule.City('Berlin', 5, 7)
print(city_a)
print(city_b)

city_a.move_to(4, 2)
city_b.move_to(7, 12)

print(city_a)
print(city_b)