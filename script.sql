CREATE TABLE tarea( 
  id SERIAL PRIMARY KEY, 
  titulo VARCHAR(30), 
  contenido VARCHAR(300), 
  fecha_fin DATE DEFAULT NOW(), 
  terminado BOOLEAN DEFAULT false
);