# 🐧 Mascota Virtual de Informática

## IPET 249 - Nicolás Copérnico
### Especialidad: Informática
### Laboratorio de Aplicaciones II - Año 2026

---

## 🎨 Concepto de la mascota

La mascota virtual de la especialidad es un **pingüino azul marino con barriga blanca**, estilo "Pou" pero completamente adaptado al IPET 249. Su identidad combina elementos de la programación, la cultura gamer y la identidad institucional del colegio.

### Características visuales:
- **Color principal:** Azul marino
- **Color secundario:** Blanco cálido para el abdomen
- **Accesorios:** Anteojos, auriculares gamer, teclado y pantalla con código
- **Escudo institucional:** Presente en el entorno y elementos visuales
- **Estilo:** Mascota tamagotchi / vida virtual con necesidades y estado emocional

---

## 🎯 Objetivo del proyecto

Crear una mascota virtual interactiva que represente a la especialidad de Informática, con mecánicas de cuidado, progresión emocional y juegos rápidos inspirados en arcade.

---

## ✨ Funcionalidades principales

- ✅ **Alimentación** - Aumenta energía y ánimo
- ✅ **Higiene / Baño** - Mejora limpieza y bienestar
- ✅ **Recreación** - Minijuegos tipo arcade
- ✅ **Programación** - Atención de tareas técnicas
- ✅ **Descanso** - Recarga de energía y batería
- ✅ **Sistema emocional** - Evolución de estados (feliz, triste, cansado)
- ✅ **Barras de estado** - Energía, hambre, higiene, felicidad, programación

---

## 🎮 Controles

| Tecla | Acción | Efecto |
|-------|--------|--------|
| **1** | Alimentar | +Hambre, +Energía, +Felicidad |
| **2** | Bañar | +Higiene, +Felicidad |
| **3** | Jugar | +Felicidad, -Energía, Activa minijuego |
| **4** | Programar | +Código/Productividad, +Felicidad, -Energía |
| **5** | Dormir | +Energía, +Felicidad |
| **Mouse** | Clic en botones | Ejecuta la acción del botón |
| **R** | Reiniciar | Vuelve a los valores iniciales |

---

## 📋 Requisitos

- Python 3.10+
- Pygame 2.5.0+
- Sistema operativo: Windows, macOS o Linux

---

## 🚀 Instalación y ejecución

### Opción 1: Con entorno virtual (RECOMENDADO)

```bash
# Clonar o descargar el repositorio
git clone https://github.com/Ginopasqualini/mascota-virtual-informatica.git
cd mascota-virtual-informatica

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# En Windows:
.venv\Scripts\activate

# En macOS/Linux:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el juego
python main.py
```

### Opción 2: Instalación directa

```bash
pip install pygame
python main.py
```

---

## 📖 Manual de uso

La mascota necesita mantenerse en equilibrio emocional y físico:

### Sistema de estadísticas:

**Energía / Batería:**
- Disminuye naturalmente con el tiempo
- Se recarga al dormir
- Necesaria para cualquier actividad

**Hambre:**
- La mascota requiere alimentación regular
- Alimentarla mejora su ánimo
- Si baja demasiado, se pone triste

**Higiene:**
- Bañar al pingüino mantiene su higiene
- Mejora su bienestar general
- Afecta su expresión visual

**Felicidad:**
- Jugar es la forma principal de aumentarla
- Se reduce con la monotonía
- Refleja el estado emocional general

**Programación / Código:**
- Aumenta al programar
- Representa productividad
- Mejora el bienestar intelectual

### Estados emocionales:

- 🥰 **Feliz** (promedio >75%): Sonrisa amplia, ojos abiertos, movimiento energético
- 😊 **Tranquilo** (promedio 45-75%): Estado neutral, movimiento normal
- 😢 **Triste** (promedio 25-45%): Ojos caídos, movimiento lento
- 😴 **Cansado** (promedio <25%): Parpadeo lento, bordes apagados

---

## 🎮 Minijuegos disponibles

Al presionar **3 (Jugar)**, la mascota accede a minijuegos inspirados en arcade:

- **Space Invaders (A):** Defensa clásica
- **Voley (B):** Deporte de reflejos
- **Autos (C):** Carrera estilo Pac-Man

*Nota: La versión actual muestra el selector de minijuegos. Las implementaciones completas están en desarrollo.*

---

## 📁 Estructura del proyecto

```
mascota-virtual-informatica/
├── README.md                 # Este archivo
├── GDD.md                    # Game Design Document completo
├── IA_LOG.md                 # Registro de uso de IA
├── requirements.txt          # Dependencias Python
├── main.py                   # Código principal del juego
├── assets/                   # Carpeta para imágenes y sonidos (futura)
│   └── .gitkeep
└── .gitignore               # Archivos a ignorar en Git
```

---

## 🎨 Diseño visual

La escena principal usa la **paleta institucional del IPET 249**:

- 🔴 **Bordó** (#6E141E) - Color principal institucional
- 🟨 **Amarillo** (#FFCD32) - Acento principal
- 🔴 **Rojo** (#B92323) - Secundario
- ⚪ **Blanco** (#F5F5F5) - Contraste y limpieza
- 🔵 **Azul marino** (#122850) - Color del pingüino

El fondo recrea un **entorno de laboratorio**, con:
- Escudo del IPET 249 en la parte superior
- Elementos informáticos sugeridos mediante formas geométricas
- Panel de estadísticas con barras de progreso
- Botones interactivos claros y accesibles
- Panel de minijuegos lateral

---

## 🔧 Desarrollo técnico

### Tecnologías utilizadas:
- **Pygame 2.5.0+:** Motor gráfico y gestión de eventos
- **Python 3.10+:** Lenguaje de programación
- **Git/GitHub:** Control de versiones

### Características de código:
- Clase `Mascota` para gestionar estado y lógica
- Clase `Button` para interfaz de usuario reutilizable
- Sistema de actualización con delta time (dt)
- Game loop a 60 FPS
- Decrecimiento progresivo de estadísticas
- Sistema de estados emocionales dinámico

---

## 📚 Créditos

**Proyecto desarrollado como:** Trabajo Práctico de Recuperación de la Especialidad de Informática  
**Institución:** IPET 249 "Nicolás Copérnico"  
**Asignatura:** Laboratorio de Aplicaciones II  
**Año:** 2026  
**Autor:** Gino Pasqualini  

---

## 📝 Licencia

MIT License - Ver LICENSE para más detalles

---

## 🤝 Contribuciones y feedback

Este proyecto es parte de la propuesta educativa del IPET 249. Para sugerencias o mejoras, contactar al desarrollador.

---

**¡Gracias por usar la Mascota Virtual de Informática del IPET 249! 🐧💻**
