# Tarea 2 — RISC vs CISC

Este repositorio contiene la solución a la **Tarea 2** del curso *CE-4301 Arquitectura de Computadores I*.  
La **Pregunta 1** está desarrollada en `Tarea_2_Arqui.pdf` e incluye una figura con los resultados del programa.

## Ejecución (Pregunta 2)
Para correr el programa y generar los resultados:
```bash
python3 main.py
```
O simplemente ejecutar el archivo `main.py` en el editor de preferencia. 

Al finalizar, se creará un archivo de texto en `./results/` (la carpeta se crea automáticamente si no existe), por ejemplo:
```
results/
├── results_run_YYYYMMDD-HHMMSS.txt
```

### ¿Qué se guarda?
En el **.txt** se encontrará:
- Vector resultado en CISC (rango de direcciones en memoria).
- Vector resultado en RISC.
- **Instrucciones ejecutadas** y **ciclos** por arquitectura.
- Verificación final: Si los vectores resultado de CISC y RISC coinciden.
