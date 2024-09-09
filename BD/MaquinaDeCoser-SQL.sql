CREATE SCHEMA `maquina`;
USE `maquina`;

CREATE TABLE`maquina`.`Puntada` (
  `Id_libro` INT NOT NULL,
  `tipoDePuntada` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id_libro`))
ENGINE = InnoDB;

CREATE TABLE `maquina`.`Hilos` (
  `idHilos` INT NOT NULL,
  `color` VARCHAR(45) NULL DEFAULT 'blanco',
  `largo_cm` INT NULL,
  PRIMARY KEY (`idHilos`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `maquina`.`Maquina` (
  `IdMaquina` INT NOT NULL,
  `Modelo` VARCHAR(45) NULL,
  `Puntada_Id_libro` INT NOT NULL,
  `Hilos_idHilos` INT NOT NULL,
  `velocidad_maxima` INT NOT NULL,
  `velocidad_minima` INT NOT NULL,
  PRIMARY KEY (`IdMaquina`, `Puntada_Id_libro`, `Hilos_idHilos`),
  CONSTRAINT `fk_Maquina_Puntada`
    FOREIGN KEY (`Puntada_Id_libro`)
    REFERENCES `maquina`.`Puntada` (`Id_libro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Maquina_Hilos1`
    FOREIGN KEY (`Hilos_idHilos`)
    REFERENCES `maquina`.`Hilos` (`idHilos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

