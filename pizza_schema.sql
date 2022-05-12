BEGIN;
--Create Student Table--
create table Pizzas (pizza_name VARCHAR(20),
  first_ingredient VARCHAR(20),
  second_ingredient VARCHAR(20),
  third_ingredient VARCHAR(20),
  fourth_ingredient VARCHAR(20),
  fifth_ingredient VARCHAR(20),
  sixth_ingredient VARCHAR(20),
  photo VARCHAR(100)
);
create table Ingredients (ingredient_name VARCHAR(20),
  photo VARCHAR(100)
);
COMMIT;