#que que
def cuantas_personas_saben_el_secreto(dias_totales, dias_espera, dias_olvido):
    # Esta lista será nuestra fila de personas. 
    # Cada persona guardará: [día_en_que_empieza_a_hablar, día_en_que_olvida]
    fila_de_gente = []
    
    # El primer día, la persona que sabe el secreto entra a la fila
    # Empieza a hablar en (1 + espera), y olvida en (1 + olvido)
    fila_de_gente.append([1 + dias_espera, 1 + dias_olvido])
    
    # Empezamos a contar desde el día 2 hasta el último día
    for hoy in range(2, dias_totales + 1):
        
        # 1. Primero, los que ya olvidaron el secreto se van de la fila
        nueva_fila = []
        for persona in fila_de_gente:
            if persona[1] > hoy:
                nueva_fila.append(persona)
        fila_de_gente = nueva_fila
            
        # 2. Ahora, contamos cuántos ya pueden contar el secreto
        cuantos_pueden_hablar = 0
        for persona in fila_de_gente:
            if persona[0] <= hoy:
                cuantos_pueden_hablar += 1
        
        # 3. Cada uno de los que puede hablar, le cuenta a alguien nuevo hoy
        for _ in range(cuantos_pueden_hablar):
            fila_de_gente.append([hoy + dias_espera, hoy + dias_olvido])
                
    # Al final, el tamaño de la fila es la cantidad de personas que saben el secreto
    return len(fila_de_gente)

print(cuantas_personas_saben_el_secreto(6, 2, 4)) # Salida esperada: 5
