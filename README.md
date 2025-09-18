---
# Plataforma de Gestión y Evaluación de Cursos Online

---
## Autores
- CHOLOTÍO MENDOZA CARLOS ANDRÉS 1517925  
- DE LEÓN GONZÁLEZ ALEJANDRO DANIEL 1502425
---

## Descripción

Esta plataforma permite gestionar cursos, usuarios (estudiantes e instructores) y evaluaciones de forma automatizada.
El sistema soporta **registro de usuarios**, **inscripción en cursos**, **creación de evaluaciones** (exámenes, tareas, proyectos), **registro de calificaciones** y **reportes de estudiantes con bajo rendimiento**.

Está desarrollada en **Python** utilizando **programación orientada a objetos (POO)**, estructuras de datos adecuadas, manejo de errores, y control de versiones con Git.

---

## Funcionalidades

### Gestión de Usuarios

* Registro de **estudiantes** e **instructores**.
* Almacenamiento de usuarios en archivo `usuarios.txt`.
* Visualización de perfiles y cursos asociados.

### Gestión de Cursos

* Crear cursos con código, nombre, instructor y datos opcionales.
* Inscribir estudiantes en cursos.
* Almacenar información de cursos en `cursos.txt`.
* Visualización completa de información del curso (estudiantes, evaluaciones, información extra).

### Gestión de Evaluaciones

* Crear **Examenes**, **Tareas** y **Proyectos**.
* Asignar calificaciones a estudiantes.
* Registro de notas en `notas.txt`.
* Reportes de estudiantes con promedio menor a un umbral definido.

### Menús Interactivos

* Menú principal con opciones para registrar usuario o acceder al sistema.
* Menú de estudiante: ver cursos, calificaciones y perfil.
* Menú de instructor: crear cursos y evaluaciones, asignar notas, generar reportes, y ver historial de notas.

---

## Estructura de Clases

* **Usuario:** Clase base para todos los usuarios.
* **Estudiante:** Hereda de `Usuario`. Tiene cursos inscritos y calificaciones.
* **Instructor:** Hereda de `Usuario`. Tiene cursos impartidos.
* **Curso:** Contiene información de código, nombre, instructor, estudiantes inscritos, evaluaciones y datos opcionales.
* **Evaluacion:** Clase base para evaluaciones; heredan `Examen`, `Tarea` y `Proyecto`.
* **Plataforma:** Maneja usuarios y cursos, controla inscripciones, creación de cursos y evaluaciones.

---

---

## Uso

1. Ejecutar el programa.
2. En el **menú principal**, elegir entre registrar usuario, acceder como existente o salir.
3. Dependiendo del tipo de usuario:

   * **Estudiante:** ver cursos inscritos, calificaciones y perfil.
   * **Instructor:** crear cursos, crear evaluaciones, asignar notas, inscribir estudiantes, ver historial y generar reportes.

---

## Archivos Guardados

* `usuarios.txt`: almacena todos los usuarios registrados.
* `cursos.txt`: almacena todos los cursos con estudiantes y evaluaciones.
* `cursos.txt`: almacena todas las notas en orden dependiendo el curso y estudiante.

---

## Manejo de Errores

* Verificación de carnet único para usuarios.
* Control de inscripciones duplicadas en cursos.
* Validación de tipos y rangos de notas.
* Verificación de permisos del instructor para acciones sobre cursos y evaluaciones.

---

## Reportes

* Generación de reportes de estudiantes con **promedio bajo** por curso.
* Se muestran calificaciones por evaluación, promedio y datos del estudiante.

---

## Control de Versiones

* Repositorio en GitHub con **commits frecuentes y descriptivos**.
* Uso de **ramas** para desarrollo de módulos: `main`, `evaluaciones`, `Generacion-de-reportes`.

---


---

## Posibles Mejoras

* Interfaz gráfica (GUI) para facilidad de uso.
* Exportación de reportes a PDF/Excel.
* Autenticación y permisos más avanzados para usuarios.
* Integración con bases de datos como SQLite para mayor escalabilidad.

---

## Reflexión sobre el diseño del sistema

### Explicar las decisiones de diseño tomadas
El sistema se diseñó siguiendo principios de programación orientada a objetos, buscando modularidad, claridad y escalabilidad. Se definieron clases específicas para cada entidad del dominio académico (`Usuario`, `Estudiante`, `Instructor`, `Curso`, `Evaluacion`, etc.), lo que permitió encapsular comportamientos y facilitar la extensión del sistema. Se implementaron menús diferenciados por rol, validaciones robustas para entradas de usuario, y persistencia de datos mediante archivos `.txt`.

---

### ¿Cómo manejaron la herencia y el polimorfismo en su diseño? ¿Qué ventajas les brindó?
Se utilizó herencia para evitar duplicación de atributos comunes:
- `Estudiante` e `Instructor` heredan de `Usuario`.
- `Examen`, `Tarea` y `Proyecto` heredan de `Evaluacion`.

El polimorfismo se aplicó al identificar dinámicamente el tipo de evaluación mediante funciones como `tipo_de_evaluacion()`. Esto permitió tratar diferentes evaluaciones de forma uniforme, simplificando la lógica de reportes y visualización.

**Ventajas:**
- Reutilización de código.
- Facilidad para extender el sistema con nuevos tipos de evaluación.
- Mayor claridad en la estructura del programa.

---

### ¿Qué estructuras de datos fueron más útiles y por qué?
- **Diccionarios (`dict`)**: se usaron para mapear usuarios por Carné y cursos por código, permitiendo acceso rápido y validación de unicidad.
- **Listas (`list`)**: para almacenar cursos impartidos, estudiantes inscritos, evaluaciones y notas. Su flexibilidad permitió agregar, recorrer y filtrar elementos fácilmente.
- **Diccionarios internos**: como `notas` en cada evaluación, permitieron asociar estudiantes con sus calificaciones de forma directa.

Estas estructuras fueron elegidas por su eficiencia, simplicidad y compatibilidad con las operaciones requeridas.

---

### ¿Qué errores comunes anticiparon y cómo los controlaron en el código?
- **Duplicación de usuarios o cursos**: se controló validando si el Carné o código ya existía antes de registrar.
- **Asignación de notas a estudiantes no inscritos**: se verificó la inscripción antes de permitir la calificación.
- **Evaluaciones duplicadas**: se evitó mediante comparación de nombres antes de agregar una nueva.
- **Entradas inválidas**: se manejaron con funciones específicas (`pedir_Carné()`, `pedir_email()`, `validar_nota()`) que aseguran formato correcto y rango válido.
- **Errores inesperados**: se capturaron con bloques `try-except` para mantener la estabilidad del sistema.

---

### ¿Cómo organizaron su trabajo usando Git y GitHub?
El proyecto se gestionó mediante Git y GitHub, utilizando:
- Ramas separadas
- Commits descriptivos para documentar cada cambio.
- GitHub como repositorio central para control de versiones, respaldo y colaboración.

Esta organización permitió mantener trazabilidad, evitar conflictos y facilitar el trabajo en equipo.

---

### ¿Qué mejoras harían si tuvieran más tiempo?
- Implementar carga de cursos y evaluaciones desde archivos `.txt`.
- Agregar autenticación básica por contraseña.
- Exportar reportes en formato `.csv` o `.pdf`.
- Crear una interfaz gráfica .
- Integrar una base de datos como SQLite para mayor escalabilidad.
- Mejorar la modularidad del menú y separar la lógica de presentación.

---

### Reflejar las dificultades encontradas y cómo las resolvieron
- **Persistencia incompleta**: inicialmente las notas no se guardaban. Se resolvió creando la función `guardar_notas_txt()` y estructurando el historial.
- **Validación de entradas**: se presentaron errores por formatos incorrectos. Se solucionó con funciones específicas para cada tipo de dato.
- **Manejo de excepciones**: se incorporaron bloques `try-except` para evitar que errores detuvieran el programa.



