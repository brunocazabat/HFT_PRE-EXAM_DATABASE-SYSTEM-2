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
values (1, 'Royal', 'Tomato', 'Mozzarella', 'Basil', 'Olive', 'Ham', 'Spices', 'pizza_img\royal.png'),
       (2, 'Queen', 'Tomato', 'Mozzarella', 'Basil', 'Olive', 'Egg', 'Spices', 'pizza_img\queen.png'),
       (3, 'Mountain', 'Cream', 'Mozzarella', 'Blue Cheese', 'Goat Cheese', 'Tartiflette', 'Chicken', 'pizza_img\mountain.png'),
       (4, 'Veggie', 'Tomato', 'Mushroom', 'Basil Pesto', 'Olive', 'Onion', 'Spices', 'pizza_img\veggie.png'),
       (5, 'Chicken Hawaiian', 'Tomato', 'Chicken', 'Ham', 'Pineapple', 'Belle Pepper', 'Mozzarella', 'pizza_img\hawaii.png');
--Create Ingredient Table--
create table Ingredients (
    ingredient_id int PRIMARY KEY,
    ingredient_name VARCHAR(20),
    photo VARCHAR(100)
);
--Insert Ingredient Values--
insert into Ingredients (ingredient_id, ingredient_name, photo)
values (1, 'Tomato', 'ingre_img\tomato.png'),
       (2, 'Mozzarella', 'ingre_img\mozza.png'),
       (3, 'Basil', 'ingre_img\basil.png'),
       (4, 'Basil Pesto', 'ingre_img\pesto.png'),
       (5, 'Olive', 'ingre_img\olive.png'),
       (6, 'Ham', 'ingre_img\ham.png'),
       (7, 'Egg', 'ingre_img\egg.png'),
       (8, 'Mushroom', 'ingre_img\mush.png');
--Push SQL Script into PostgreSQL DB--
COMMIT;