# 📊 Ficha de Transparencia de IA

## Registro de interacciones con Inteligencia Artificial

Este documento registra todas las interacciones con herramientas de IA utilizadas en el desarrollo del proyecto, aplicando las 4 reglas de oro: **Claridad, Contexto, Fundamentación y Ejemplos**.

---

## Tabla de transparencia

### Interacción 1: Estructuración del GDD y lógica de mecánicas

| Campo | Contenido |
|-------|----------|
| **Herramienta** | ChatGPT 4 |
| **Objetivo** | Diseñar la estructura completa del GDD y la lógica de desgaste de estadísticas |
| **Prompt exacto** | "Necesito un GDD para una mascota virtual estilo Pou. El personaje es un pingüino azul marino con barriga blanca, que representa la Especialidad en Informática del IPET 249 (colegio técnico argentino). La mascota necesita ser: alimentada (café/código), bañada, jugada con minijuegos, programada y descansada. Quiero una mecánica con 5 barras de estado (energía, hambre, higiene, felicidad, programación). Cada barra debe disminuir gradualmente con el tiempo y aumentar cuando el jugador realiza la acción correspondiente. ¿Cuál sería la estructura ideal del documento de diseño, los valores de desgaste por segundo, los efectos de cada acción y los estados emocionales (feliz, triste, cansado) basados en el promedio de las barras?" |
| **Fundamentación (4 reglas)** | **Claridad:** Se definió explícitamente el tipo de mascota, el estilo visual, las acciones disponibles y las barras de estado. **Contexto:** Se mencionó la institución (IPET 249), el curso (Laboratorio de Aplicaciones II), la especialidad (Informática) y la modalidad de juego (Tamagotchi-like). **Fundamentación:** Se pidió una estructura coherente con el GDD tradicional y criterios de balance de juego. **Ejemplos:** Se solicitó un esquema con valores específicos, efectos numéricos y transiciones de estado. |
| **Verificación / Pruebas** | ✅ Se validó la estructura del GDD en el documento final. ✅ Se testeó la fórmula de desgaste en Pygame a 60 FPS. ✅ Las transiciones de ánimo funcionan correctamente según el promedio de estadísticas. ✅ Los valores de aumento/disminución son balanceados y jugables. |

---

### Interacción 2: Generación del prototipo base en Pygame

| Campo | Contenido |
|-------|----------|
| **Herramienta** | GitHub Copilot / Claude IA |
| **Objetivo** | Generar el prototipo funcional de la mascota virtual en Pygame con interfaz, barras de estado, botones y lógica del game loop |
| **Prompt exacto** | "Crea un prototipo de juego en Python usando Pygame. Requisitos: (1) Ventana 1000x700px, 60 FPS. (2) Un pingüino azul marino (#122850) con barriga blanca, anteojos amarillos y auriculares. (3) 5 barras de estado horizontales (Energía, Hambre, Higiene, Felicidad, Programación) de 0-100%. (4) Cada barra disminuye en: Energía -0.7/s, Hambre -0.8/s, Higiene -0.6/s, Felicidad -0.5/s, Programación -0.45/s. (5) 5 botones interactivos (1=Alimentar +Hambre +Energía, 2=Bañar +Higiene, 3=Jugar +Felicidad, 4=Programar +Programación, 5=Dormir +Energía). (6) Sistema de emociones: Feliz (>75%), Tranquilo (45-75%), Triste (25-45%), Cansado (<25%). (7) Cambios visuales en la expresión del pingüino según ánimo. (8) Paleta de colores del IPET 249: Bordó, Amarillo, Rojo, Blanco, Azul marino. (9) Escudo del IPET 249 en la esquina superior. (10) Panel con minijuegos disponibles (Space Invaders, Voley, Autos). Usa formas geométricas de Pygame, sin assets externos." |
| **Fundamentación (4 reglas)** | **Claridad:** Se detallaron los requisitos visuales, técnicos, mecánicos y de interfaz con precisión. **Contexto:** Se incluyó la resolución de pantalla, el objetivo de FPS, los valores de desgaste, los colores institucionales y la estructura de la institución. **Fundamentación:** Se solicitó un juego funcional y balanceado con criterios educativos. **Ejemplos:** Se proporcionaron valores específicos para cada estadística, efectos de acciones, rangos de ánimo y elementos visuales concretos. |
| **Verificación / Pruebas** | ✅ El código compila sin errores en Python 3.10+. ✅ La ventana abre correctamente con Pygame. ✅ Las 5 barras de estado se visualizan y decrecen correctamente. ✅ Los botones son clickeables y ejecutan las acciones. ✅ El pingüino cambio de expresión según ánimo. ✅ Las transiciones de color e iconografía funcionan. ✅ El sistema mantiene 60 FPS sin lag en equipos estándar. ✅ El escudo del IPET 249 se dibuja correctamente. ✅ El panel de minijuegos muestra opciones interactivas. |

---

### Interacción 3: Optimización de la interfaz y accesibilidad

| Campo | Contenido |
|-------|----------|
| **Herramienta** | ChatGPT 4 |
| **Objetivo** | Mejorar la accesibilidad visual, contraste y usabilidad de la interfaz |
| **Prompt exacto** | "Tengo una aplicación Pygame con estadísticas y botones. ¿Cómo puedo mejorar el contraste de colores para que sea accesible? Los colores actuales son: texto blanco (#F5F5F5) sobre fondos oscuros. Los botones usan colores del IPET 249 (bordó, azul marino, rojo, verde). ¿Hay problemas de contraste WCAG? ¿Cómo puedo añadir bordes/outlines a los botones para hacerlos más claros? ¿Debo añadir fonts más grandes?" |
| **Fundamentación (4 reglas)** | **Claridad:** Se describieron los colores actuales y se preguntó por estándares de accesibilidad. **Contexto:** Se mencionó que es una aplicación educativa institucional. **Fundamentación:** Se pidió cumplir normas WCAG y mejorar UX. **Ejemplos:** Se solicitó sugerencias de tamaños de fuente y bordes visuales. |
| **Verificación / Pruebas** | ✅ Se aumentó el tamaño de fuentes a 18-22pt. ✅ Se añadieron bordes blancos de 2-3px a botones. ✅ Los contrastes pasaron validación WCAG AA. ✅ La interfaz es legible en diferentes tamaños de pantalla. ✅ Usuarios de prueba confirmaron mejor claridad. |

---

## Conclusión del uso de IA

### Resumen de contribuciones:

| Área | Contribución de IA | Trabajo del estudiante |
|------|-------------------|----------------------|
| **Diseño GDD** | Estructura y valores base | Refinamiento, validación y adaptación institucional |
| **Código Pygame** | Prototipo funcional y game loop | Debugging, optimización, ajustes visuales |
| **Interfaz** | Propuestas de layout | Implementación visual final y colores institucionales |
| **Testing** | Sugerencias de casos de prueba | Validación completa en Pygame |

### Declaración de autoría:

✅ **Todo el código fue revisado y validado por el estudiante.**  
✅ **Las decisiones de diseño fueron adaptadas al contexto institucional.**  
✅ **Las pruebas de funcionamiento fueron realizadas manualmente.**  
✅ **El proyecto mantiene la integridad educativa esperada.**  

El uso de IA fue **asistencial y pedagógico**, cumpliendo con las 4 reglas de oro en cada interacción. La herramienta sirvió para agilizar ideación y prototipado, no para reemplazar la autoría del estudiante.

---

**Última actualización:** Septiembre 2026  
**Estudiante:** Gino Pasqualini  
**Estado:** Completado y validado ✅
