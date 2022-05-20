--Start SQL Script--
BEGIN;
--Create Pizza Table--
create table Pizzas (
    pizza_id int PRIMARY KEY,
    pizza_name VARCHAR(20),
    first_ingredient VARCHAR(20),
    second_ingredient VARCHAR(20),
    third_ingredient VARCHAR(20),
    fourth_ingredient VARCHAR(20),
    fifth_ingredient VARCHAR(20),
    sixth_ingredient VARCHAR(20),
    photo VARCHAR(100)
);
--Insert Pizza Values--
insert into Pizzas (pizza_id, pizza_name, first_ingredient, second_ingredient, third_ingredient, fourth_ingredient, fifth_ingredient, sixth_ingredient, photo)
values (1, 'Royal', 'Tomato', 'Mozzarella', 'Basil', 'Olive', 'Ham', 'Spices', 'img\pizzas\royal.png'),
       (2, 'Queen', 'Tomato', 'Mozzarella', 'Basil', 'Olive', 'Egg', 'Spices', 'img\pizzas\queen.png'),
       (3, 'Mountain', 'Cream', 'Mozzarella', 'Blue Cheese', 'Goat Cheese', 'Tartiflette', 'Chicken', 'img\pizzas\mountain.png'),
       (4, 'Veggie', 'Tomato', 'Mushroom', 'Basil Pesto', 'Olive', 'Onion', 'Spices', 'img\pizzas\veggie.png'),
       (5, 'Chicken Hawaiian', 'Tomato', 'Chicken', 'Ham', 'Pineapple', 'Belle Pepper', 'Mozzarella', 'img\pizzas\hawaii.png');
--Create Ingredient Table--
create table Ingredients (
    ingredient_id int PRIMARY KEY,
    ingredient_name VARCHAR(20),
    photo VARCHAR(100)
);
--Insert Ingredient Values--
insert into Ingredients (ingredient_id, ingredient_name, photo)
values (1, 'Tomato', 'img\ingredients\tomato.png'),
       (2, 'Mozzarella', 'img\ingredients\mozza.png'),
       (3, 'Basil', 'img\ingredients\basil.png'),
       (4, 'Basil Pesto', 'img\ingredients\pesto.png'),
       (5, 'Olive', 'img\ingredients\olive.png'),
       (6, 'Ham', 'img\ingredients\ham.png'),
       (7, 'Egg', 'img\ingredients\egg.png'),
       (8, 'Mushroom', 'img\ingredients\mush.png');
--Push SQL Script into PostgreSQL DB--
COMMIT;