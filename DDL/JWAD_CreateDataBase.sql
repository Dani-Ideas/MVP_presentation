CREATE BATABASE DBJW_Angel_Daniel;
USE DBJW_Angel_Daniel;

DROP TABLE IF EXISTS clients;
CREATE TABLE clients(
id_client int AUTO_INCREMENT PRIMARY KEY,
registration_date datetime NOT NULL,
name_client varchar(45),
cel_number int(10) UNIQUE NOT NULL,
contact_method varchar(150), -- email, perfil de red social, etc ...
ip_adress varchar(16)
);

DROP TABLE IF EXISTS processes;
CREATE TABLE processes(
id_process int AUTO_INCREMENT PRIMARY KEY, -- llave primaria
name_process varchar(50) NOT NULL,
description_process text,
need_monitoring boolean,
standar_time_minuts int,
process_simultan boolean
);

DROP TABLE IF EXISTS dificults;
CREATE TABLE dificults(
id_dificult int AUTO_INCREMENT PRIMARY KEY, -- llave primaria
name_dificult varchar(30) NOT NULL,
estimate_minuts float -- multiplicador de el tiempo por defecto
);

DROP TABLE IF EXISTS supplies;
CREATE TABLE supplies(
	id_supplies int AUTO_INCREMENT PRIMARY KEY,
    name_type varchar(50) NOT NULL,
    description_insume text
);

DROP TABLE IF EXISTS machines_tools;
CREATE TABLE machines_tools(
	id_machine_tool int AUTO_INCREMENT PRIMARY KEY, 
    name_machine_tool varchar(45),
    cost_machime_tool float
    );
    
    CREATE TABLE machine_supplies (
    machine_id INT,
    supply_id INT,
    quantity INT NOT NULL,
    PRIMARY KEY (machine_id, supply_id)
    -- FOREIGN KEY (machine_id) REFERENCES machines(id) ON DELETE CASCADE ON UPDATE CASCADE,
    -- FOREIGN KEY (supply_id) REFERENCES supplies(id) ON DELETE CASCADE ON UPDATE CASCADE
);
    
    
-- ******
DROP TABLE IF EXISTS models;
CREATE TABLE models(
	id_model int AUTO_INCREMENT PRIMARY KEY, -- llave primaria
	name_model varchar(25),
	description_model text,
	type_model int NOT NULL, -- FK pieces_type
	volum_model_metal float8 NOT NULL,
    quantity_stones int NOT NULL,
    image_model text, -- pasar a binario la imagen
	number_mold int
);

DROP TABLE IF EXISTS metals_types;
CREATE TABLE metals_types(
	id_metal_type int AUTO_INCREMENT PRIMARY KEY,
    name_metal varchar(25) NOT NULL
);

DROP TABLE IF EXISTS pieces_type;
CREATE TABLE pieces_type(
	id_piece_type int AUTO_INCREMENT PRIMARY KEY,
	name_type varchar(25)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
	id_order int AUTO_INCREMENT PRIMARY KEY, -- llave primaria
    -- los datos de fecha son así para la bitacora
    order_date datetime NOT NULL, -- el dia que se registro el pedido
    start_date DATE,-- cuando se empezo a fabricar
    end_date DATE, -- cuando es se termino
    dead_line DATE, -- fecha limite de entrega
    id_client INT NOT NULL,-- FK clients
    cost_order DECIMAL(10, 2) NOT NULL, -- posible llave foranea
	id_model int NOT NULL, -- FK models encaso de ya ser un modelo existente, de lo contrario, registrar modelo
    id_type_piece int NOT NULL,-- FK models,pieces_type
    quantity_stones int NOT NULL, -- FK models,quantity_stones, falta llevar cotrol del origen de las piedras, corte y el tipo
    id_metal_type int NOT NULL, -- FK metals_types
    all_process varchar(50) NOT NULL, -- posible cambio de numero de digitos, procesos '1,2,3,4,5,... ' '6, 7, 8, 10'
    all_dificults varchar(50) NOT NULL,
    status_order_general ENUM('pendiente', 'pausado', 'en proceso', 'completado') NOT NULL,-- agregar la logica de completado en proceso actual
    status_actual_process ENUM('pendiente', 'pausado', 'en proceso', 'completado') NOT NULL
);
DROP TABLE IF EXISTS providers;
CREATE TABLE providers(
	id_provider int AUTO_INCREMENT PRIMARY KEY,
	name_provider varchar(50) NOT NULL,
	-- aqui podria ser el nombre del contacto (comuniqueme con el director X de la empresa Y)
	cel_number int(10) UNIQUE NOT NULL,
	insume_type int -- llave foranea
);

DROP TABLE IF EXISTS purchase;
CREATE TABLE purchases(
	id_purchase int AUTO_INCREMENT PRIMARY KEY,
    date_purchase datetime,
	price DECIMAL(10, 2) NOT NULL,
    quantity int NOT NULL, -- llave foranea
    insume int NOT NULL, -- llave foranea
    provider int NOT NULL -- llave foranea
);