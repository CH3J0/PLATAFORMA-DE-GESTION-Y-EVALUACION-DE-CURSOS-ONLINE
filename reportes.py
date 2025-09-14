def reporte_promedio_bajo(curso, umbral=60):
    """
    Genera un reporte de estudiantes con promedio bajo en un curso.
    """
    print(f"\n--- REPORTE: Estudiantes con promedio menor a {umbral} ---")
    for estudiante in curso.estudiantes_inscritos:
        notas = [
            eval.notas.get(estudiante, 0)
            for eval in curso.evaluaciones
            if estudiante in eval.notas
        ]
        if notas:
            promedio = sum(notas) / len(notas)
            if promedio < umbral:
                print(f"\nEstudiante: {estudiante.nombre} | ID: {estudiante.id_usuario} | Email: {estudiante.email}")
                print(f"Promedio: {promedio:.2f}")