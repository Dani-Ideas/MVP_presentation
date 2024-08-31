USE DBJW_Angel_Daniel;


insert into processes (name_process, need_monitoring, standar_time_minuts, process_simultan)
VALUES 
("Cotizar", true, 60, false),
("Modelar3D", true, 120, false),
("Modelar3D_ajuste", true, 30, false),
("Imprimir3D_envio_archivo", true, 5, true),
("Imprimir3D_prepar_impresora", true, 5, true),
("Imprimir3D_imprimiendo", false, 120, true),
("Imprimir3D_quitar_soportes", true, 5, true),
("Molde_fabricado", true, 120, true),
("Inyeccion_calentamiento_inyector", false, 30, true),
("Inyeccion_inyeccion_molde", true, 1, false),
("Inyeccion_inyeccion_molde_enfriamieto_cera", true, 3, true),
("Inyeccion_liberacion_cera_fria", true, 1, false),
("Vaciado_enarbolado", true, 20, true),
("Vaciado_preparacion_cubilete", true, 10, true),
("Vaciado_mescla", true, 10, true),
("Vaciado_mescla_secado", false, 45, true),
("Vaciado_introduccion_HornoRecosido", true, 10, true),
("Vaciado_HornoRecosido",false, 300, true),
("Relimado_pulido",true, 100, false),
("Montado", true, 60, false)
-- trasportar mercansia
-- matenimieto y limpieza
;