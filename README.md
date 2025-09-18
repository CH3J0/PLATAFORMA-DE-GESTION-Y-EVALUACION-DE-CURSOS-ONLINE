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


