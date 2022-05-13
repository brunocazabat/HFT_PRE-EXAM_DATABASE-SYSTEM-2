--Start SQL Script--
BEGIN;
--Create Pizza Table--
create table Pizzas (pizza_name VARCHAR(20),
  first_ingredient VARCHAR(20),
  second_ingredient VARCHAR(20),
  third_ingredient VARCHAR(20),
  fourth_ingredient VARCHAR(20),
  fifth_ingredient VARCHAR(20),
  sixth_ingredient VARCHAR(20),
  photo VARCHAR(100)
);
--Insert Pizza Values--
insert into Pizzas (pizza_name, first_ingredient, second_ingredient, third_ingredient, fourth_ingredient, fifth_ingredient, sixth_ingredient, photo)
values ('Royal', 'Tomato', 'Mozzarella', 'Basil', 'Olive', 'Ham', Null, Null),
       ('Queen', 'Tomato', 'Mozzarella', 'Basil', 'Olive', 'Egg', Null, Null),
       ('Mountain', 'Cream', 'Mozzarella', 'Blue Cheese', 'Goat Cheese', 'Tartiflette', 'Chicken', Null),
       ('Veggie', 'Tomato', 'Mushroom', 'Basil Pesto', 'Olive', 'Onion', Null, Null);
--Create Ingredient Table--
create table Ingredients (ingredient_name VARCHAR(20),
  photo VARCHAR(100)
);
--Insert Ingredient Values--
insert into Ingredients (ingredient_name, photo)
values ('Tomato', Null),
       ('Mozzarella', Null),
       ('Basil', Null),
       ('Basil Pesto', Null),
       ('Olive', Null),
       ('Ham', Null),
       ('Egg', Null),
       ('Mushroom', Null),
       ('Cream', Null),
       ('Blue Cheese', Null),
       ('Goat Cheese', Null),
       ('Tartiflette', Null),
       ('Chicken', Null),
       ('Onion', Null);
--Push SQL Script into PostgreSQL DB--
COMMIT;