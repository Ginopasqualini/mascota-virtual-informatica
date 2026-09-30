# 📋 GDD - Mascota Virtual de Informática

## 1. Concepto General

La mascota virtual es un **pingüino azul marino con barriga blanca**, estilo "Pou" (tamagotchi), pero con una identidad totalmente institucional y representativa de la especialidad de Informática del IPET 249.

Representa a la Especialidad en Informática, mezclando elementos lúdicos, tecnológicos y educativos en una experiencia interactiva de cuidado y progresión emocional.

---

## 2. Personaje Base

### Identidad visual:
- **Tipo de criatura:** Pingüino
- **Estilo artístico:** Caricaturesco y adorable
- **Tamaño relativo:** Mediano (ocupa ~25% de la pantalla)

### Paleta de colores:
- **Azul marino (#122850):** Cuerpo principal
- **Blanco (#F5F5F5):** Barriga y detalles
- **Amarillo (#FFCD32):** Pico, patas y accesorios
- **Negro (#0F0F0F):** Ojos, anteojos
- **Bordó (#6E141E):** Detalles institucionales

### Atributos personalizados:
- 👓 **Anteojos:** Representan el análisis y la lógica de programación
- 🎧 **Auriculares gamer:** Conectan con la cultura tecnológica
- ⌨️ **Teclado/Pantalla:** Símbolo de código y desarrollo
- 🛡️ **Escudo del IPET 249:** Identidad institucional presente en el entorno
- 💙 **Expresiones emocionales:** Cambian según estados de ánimo

---

## 3. Objetivo del Juego

Mantener a la mascota sana, feliz, productiva y descansada a través de interacciones constantes. El jugador actúa como "cuidador" del pingüino, equilibrando sus necesidades físicas y emocionales durante el tiempo de juego.

### Objetivos secundarios:
- Aprender sobre gestión de recursos y balance
- Experimentar feedback visual y emocional inmediato
- Disfrutar de interacciones lúdicas y creativas

---

## 4. Variables de Estado (Estadísticas)

Se implementarán **5 barras de estado principales** (0-100%) que representan las necesidades de la mascota:

### 4.1 Energía / Batería
- **Rango:** 0-100%
- **Decrecimiento natural:** -0.7 puntos/segundo
- **Aumento:** Dormir (+26), Comer (+10), Descanso pasivo
- **Impacto visual:** Afecta velocidad de animación
- **Estado crítico:** <20% → Parpadeo lento, movimiento pesado

### 4.2 Hambre / Alimentación
- **Rango:** 0-100%
- **Decrecimiento natural:** -0.8 puntos/segundo
- **Aumento:** Alimentar (+20), Programar (+5)
- **Impacto visual:** Expresión de tristeza si <30%
- **Nota:** La mascota necesita comer regularmente

### 4.3 Higiene / Limpieza
- **Rango:** 0-100%
- **Decrecimiento natural:** -0.6 puntos/segundo
- **Aumento:** Bañar (+24)
- **Impacto visual:** Cambio de brillo y claridad del sprite
- **Estado crítico:** <20% → Colores apagados, expresión de disgusto

### 4.4 Felicidad / Ánimo
- **Rango:** 0-100%
- **Decrecimiento natural:** -0.5 puntos/segundo
- **Aumento:** Jugar (+22), Programar (+7), Alimentar (+8), Bañar (+6), Dormir (+5)
- **Impacto visual:** Sonrisa vs ceño fruncido
- **Más importante para el mood general**

### 4.5 Programación / Productividad
- **Rango:** 0-100%
- **Decrecimiento natural:** -0.45 puntos/segundo
- **Aumento:** Programar (+22)
- **Aumento negativo:** Jugar (-5)
- **Impacto visual:** Pantalla/código visible en pechera
- **Concepto:** Representa compromiso con la especialidad

### Fórmula de Promedio General:
```
Promedio = (Energía + Hambre + Higiene + Felicidad + Programación) / 5
```

---

## 5. Sistema de Emociones

El **mood** se calcula en base al promedio de todas las estadísticas y determina la expresión visual:

| Mood | Promedio | Expresión | Color aura | Animación |
|------|----------|-----------|-----------|----------|
| 🥰 **Feliz** | >75% | Sonrisa amplia, ojos brillantes | Verde/Dorado | Saltitos, energía |
| 😊 **Tranquilo** | 45-75% | Expresión neutral | Azul | Movimiento normal |
| 😢 **Triste** | 25-45% | Ojos caídos, boca hacia abajo | Gris | Movimiento lento |
| 😴 **Cansado** | <25% | Parpadeo lento, ojos cerrándose | Púrpura | Apenas se mueve |

---

## 6. Interacciones del Usuario (Acciones)

El jugador puede realizar 5 acciones principales mediante **teclado (1-5)** o **clicks en botones**:

### 6.1 Alimentar (Tecla 1)
**Descripción:** Dar comida (café/código) al pingüino

**Efectos:**
- Hambre: +20
- Energía: +10
- Felicidad: +8

**Animación:** Mascota abre boca, pequeño sprite de café aparece

**Icono:** 🍜 / ☕

---

### 6.2 Bañar (Tecla 2)
**Descripción:** Limpiar y refrescar al pingüino

**Efectos:**
- Higiene: +24 (mayor aumento)
- Felicidad: +6

**Animación:** Burbujas, splash, cambio de brillo del sprite

**Icono:** 🚿 / 💦

---

### 6.3 Jugar (Tecla 3)
**Descripción:** Interacción con minijuegos arcade

**Efectos:**
- Felicidad: +22 (aumento importante)
- Energía: -8 (costo energético)
- Programación: -5 (distracción)

**Minijuegos disponibles:**
1. **Space Invaders (A):** Evitar/disparar enemigos
2. **Voley (B):** Botar pelota contra IA
3. **Autos (C):** Carrera simple tipo Pac-Man

**Animación:** Transición a pantalla de minijuego, mascota se anima

**Icono:** 🎮

---

### 6.4 Programar (Tecla 4)
**Descripción:** Trabajar en tareas de código

**Efectos:**
- Programación: +22 (aumento importante)
- Felicidad: +7
- Energía: -6 (costo intelectual)

**Animación:** Código aparece en pantalla, mascota se concentra (ojos más serios)

**Icono:** 💻 / ⌨️

---

### 6.5 Dormir (Tecla 5)
**Descripción:** Descanso y recarga de energía

**Efectos:**
- Energía: +26 (aumento importante)
- Felicidad: +5

**Animación:** Mascota cierra ojos, pequeña burbuja Zzz aparece

**Icono:** 😴 / 🛏️

---

### Tecla especial:
- **R:** Reinicia todas las estadísticas a valores iniciales

---

## 7. Evolución y Expresiones Visuales

### Estados del sprite principal:

#### Feliz 🥰
```
- Sonrisa: Arco hacia arriba (curvado positivo)
- Ojos: Grandes, brillantes, cejas hacia arriba
- Cuerpo: Postura erguida
- Pechera: Muestra líneas de código en amarillo
- Auriculares: Levantados, activos
```

#### Tranquilo 😊
```
- Sonrisa: Línea recta, neutra
- Ojos: Normales, mirando al frente
- Cuerpo: Postura relajada
- Pechera: Línea neutral
- Movimiento: Suave bobbing (arriba/abajo)
```

#### Triste 😢
```
- Sonrisa: Arco hacia abajo (curvado negativo)
- Ojos: Caídos, cejas hacia abajo
- Cuerpo: Postura encorvada
- Pechera: Línea diagonal inclinada
- Movimiento: Lento, pesado
```

#### Cansado 😴
```
- Ojos: Casi cerrados, parpadeo lento
- Boca: Línea recta, sin expresión
- Cuerpo: Inclinado, apoyado
- Aura: Colores oscurecidos
- Movimiento: Mínimo, casi estático
```

### Animaciones dinámicas:

**Bobbing (flotación):**
```
y_offset = sin(tiempo * velocidad) * amplitud
```
La mascota sube y baja sutilmente para dar sensación de vida.

**Parpadeo:**
- Intervalo: cada 3-5 segundos
- Duración: 200ms
- Más frecuente cuando está cansada

**Cambio de escala:**
- Al saltar: 1.0 → 1.1 → 1.0 (feliz)
- Al deprimirse: 1.0 → 0.95 (triste)

---

## 8. Ciclo Principal del Juego (Game Loop)

```
while juego_activo:
    dt = delta_time / 1000  # Diferencia de tiempo en segundos
    
    # Eventos
    procesar_inputs()
    
    # Lógica
    mascota.update(dt)
      - Decrementar estadísticas
      - Calcular mood
      - Actualizar animaciones
    
    # Renderizado
    limpiar_pantalla()
    dibujar_fondo()
    dibujar_panel_estadísticas()
    dibujar_mascota()
    dibujar_botones()
    actualizar_pantalla()
    
    # Control de FPS
    clock.tick(60)  # 60 FPS
```

---

## 9. Interfaz de Usuario

### Elementos principales:

**Encabezado:**
- Logo/Escudo del IPET 249 (pequeño, 80x80px)
- Título: "IPET 249 | Especialidad en Informática"
- Subtítulo: "Laboratorio de Aplicaciones II - 2026"

**Panel de Estadísticas (izquierda):**
- 5 barras de progreso horizontales
- Etiqueta + porcentaje por cada barra
- Colores diferenciados (azul, naranja, celeste, rojo, amarillo)

**Área central:**
- Mascota (pingüino, ~200x250px)
- Fondo de laboratorio
- Sombra bajo los pies

**Panel de Minijuegos (derecha):**
- 3 botones de juegos disponibles
- Indicador de juego activo

**Botones de acción (abajo):**
- 5 botones grandes en fila
- Textos con números de tecla (1, 2, 3, 4, 5)
- Colores diferenciados por acción

---

## 10. Entorno Visual

### Fondo principal:
- Fondo superior (encabezado): Gradiente bordó/negro
- Fondo inferior (juego): Gris oscuro con grid leve (laboratorio)

### Paleta de colores institucional:
```
- Bordó (#6E141E): Encabezado, líneas decorativas
- Amarillo (#FFCD32): Acentos, escudo, líneas de énfasis
- Rojo (#B92323): Botones de acción, alertas
- Blanco (#F5F5F5): Texto, contraste
- Azul marino (#122850): Pingüino, detalles técnicos
- Azul oscuro (#091228): Sombras, profundidad
```

### Elementos decorativos:
- Escudo del IPET 249 en la esquina superior izquierda
- Grid sutil de fondo (representa laboratorio)
- Pequeños símbolos de código (llaves, paréntesis) dispersos

---

## 11. Mecánicas de Balance y Desafío

### Balance de dificultad:
- Al inicio: Barras bajan lentamente, acción fácil
- Con el tiempo: Jugador debe ser más activo/responsable
- No hay "Game Over", la mascota simplemente se pone triste

### Desafíos emergentes:
1. **Multitarea:** Gestionar 5 necesidades simultáneamente
2. **Timing:** Saber cuándo actuar para mantener balance
3. **Trade-offs:** Jugar reduce productividad, pero aumenta felicidad

---

## 12. Progresión y Logros (Futuro)

### Sistema de logros (v2):
- Mantener felicidad >80% por 5 minutos
- Alcanzar programación 100%
- Jugar todos los minijuegos
- Pasar 10 minutos sin que baje una barra

---

## 13. Especificaciones técnicas

### Resolución:
- **Pantalla:** 1000x700px
- **Escalable:** Sí, con viewport responsivo

### FPS:
- Objetivo: 60 FPS
- Motor: Pygame 2.5.0+
- Lenguaje: Python 3.10+

### Estructura de código:
```
main.py
├── Clase Mascota
│   ├── __init__()
│   ├── update(dt)
│   └── action(tipo)
├── Clase Button
│   ├── draw()
│   └── is_clicked()
├── Funciones de dibujo
│   ├── draw_pet()
│   ├── draw_bar()
│   ├── draw_shield()
│   └── draw_minigame_panel()
└── Función main()
    └── Game loop
```

---

## 14. Consideraciones futuras

- Sonidos y música de fondo
- Implementación completa de minijuegos
- Sistema de guardado/persistencia
- Personalizaciones visuales (sombreros, accesorios)
- Múltiples mascotas / mascota del usuario
- Logros y estadísticas globales

---

## 15. Conclusión

Este GDD define una mascota virtual completa, interactiva y representativa de la especialidad de Informática. La combinación de mecánicas de cuidado (Tamagotchi), elementos lúdicos (minijuegos) y identidad institucional crea una experiencia educativa y entretenida que refleja los valores del IPET 249.

---

**Versión:** 1.0  
**Fecha:** Septiembre 2026  
**Autor:** Gino Pasqualini  
**Estado:** Completado ✅
