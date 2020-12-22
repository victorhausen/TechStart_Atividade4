drop table categorie;
drop table marketplace;

CREATE TABLE marketplace(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, description text);
CREATE TABLE categorie(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, description text, parent_id integer, foreign key(parent_id) references marketplace(id));

insert into marketplace (name, description) values ("mercado livre", "é o meli");
insert into marketplace (name, description) values ("bw2", "é a bw2");

insert into categorie (name, description, parent_id) values ("alimentos", "são gostosos", 1);
insert into categorie (name, description, parent_id) values ("eletronicos", "são uteis", 1);

insert into categorie (name, description, parent_id) values ("joias", "são caras, servem pra demostrar afeto se você for muito rico", 1);
insert into categorie (name, description, parent_id) values ("suplementos", "são pra você ficar gostose", 2);