INSERT INTO `maquina`.`Maquina` (`IdMaquina`, `Modelo`, `Puntada_Id_libro`, `Hilos_idHilos`, `velocidad_maxima`, `velocidad_minima`) VALUES
(1, 'Modelo0', 1, 1, 2000, 100),
(2, 'Modelo1', 2, 2, 1800, 150),
(3, 'Modelo2', 3, 3, 1600, 120),
(4, 'Modelo3', 4, 4, 2200, 130),
(5, 'Modelo4', 5, 5, 2000, 100),
(6, 'Modelo5', 1, 2, 1900, 110),
(7, 'Modelo6', 2, 3, 2100, 140),
(8, 'Modelo7', 3, 4, 1700, 125),
(9, 'Modelo8', 4, 5, 2000, 120),
(10, 'Modelo9', 5, 1, 1800, 130);


INSERT INTO `maquina`.`Hilos` (`idHilos`, `color`, `largo_cm`) VALUES
(1, 'Rojo', 100),
(2, 'Azul', 150),
(3, 'Verde', 200),
(4, 'Negro', 50),
(5, 'Blanco', 75);


INSERT INTO `maquina`.`Puntada` (`Id_libro`, `tipoDePuntada`) VALUES
(1, 'Recta'),
(2, 'Zigzag'),
(3, 'Overlock'),
(4, 'Punto de satén'),
(5, 'Punto de cadeneta');

