SELECT * from `Hilos`;

SELECT * FROM `maquina`.`Puntada`;

SELECT * FROM `maquina`.`Hilos` WHERE `color` = 'Azul';

SELECT * FROM `maquina`.`Maquina` WHERE `IdMaquina` = 3;

SELECT m.`IdMaquina`, m.`Modelo`, h.`color`, h.`largo_cm`
FROM `maquina`.`Maquina` m
JOIN `maquina`.`Hilos` h ON m.`Hilos_idHilos` = h.`idHilos`
WHERE h.`largo_cm` > 100;