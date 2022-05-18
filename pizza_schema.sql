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
       (4, 'Veggie', 'Tomato', 'Mushroom', 'Basil Pesto', 'Olive', 'Onion', 'Spices', 'pizza_img\veggie.png');
--Create Ingredient Table--
create table Ingredients (
    ingredient_id int PRIMARY KEY,
    ingredient_name VARCHAR(20),
    photo VARCHAR(100)
);
--Insert Ingredient Values--
insert into Ingredients (ingredient_id, ingredient_name, photo)
values (1, 'Tomato', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (2, 'Mozzarella', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (3, 'Basil', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (4, 'Basil Pesto', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (5, 'Olive', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (6, 'Ham', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (7, 'Egg', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (8, 'Mushroom', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (9, 'Cream', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (10, 'Blue Cheese', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (11, 'Goat Cheese', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (12, 'Tartiflette', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (13, 'Chicken', 'C:/Users/bruno/Desktop/IMG_3014.JPG'),
       (14, 'Onion', 'C:/Users/bruno/Desktop/IMG_3014.JPG');
--Push SQL Script into PostgreSQL DB--
COMMIT;