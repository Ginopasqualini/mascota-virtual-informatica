# 🦔 GDD actualizado: Erizo Virtual de Informática

## 1. Concepto
La mascota virtual es un erizo marrón tierno de diseño propio. El jugador debe cuidar sus necesidades, jugar minijuegos, conseguir puntos y comprar accesorios.

El erizo representa Informática porque combina una interfaz de estados, lógica condicional, game loop, minijuegos, economía virtual y personalización.

## 2. Estados visuales con imágenes
El juego utiliza cuatro imágenes entregadas por el estudiante dentro de `img/`:

- `normal.png`: expresión sonriente cuando la mascota está estable.
- `feliz.png`: brazos arriba cuando la felicidad y el promedio general son altos.
- `llorando.png`: lágrimas cuando el hambre es menor a 30%.
- `bostezando.png`: sueño cuando la energía es menor a 25%.

Prioridad de estados:
1. Hambre baja → llorando.
2. Energía baja → bostezando.
3. Felicidad alta y buen promedio → brazos arriba.
4. Caso contrario → sonriendo.

## 3. Variables
- **Energía:** baja con el tiempo; aumenta al dormir.
- **Hambre:** baja con el tiempo; aumenta al alimentar.
- **Higiene:** baja con el tiempo; aumenta al bañar.
- **Felicidad:** baja lentamente; aumenta al jugar y realizar cuidados.
- **Código:** representa la productividad; aumenta al programar.
- **Puntos:** se obtienen en los minijuegos.
- **Dinero:** se obtiene al convertir puntos y se utiliza en la tienda.

## 4. Minijuegos
### Space Invaders
El jugador mueve el personaje con las flechas y dispara con espacio. Cada enemigo destruido otorga puntos.

### Vóley
El jugador mueve la plataforma con las flechas para devolver la pelota. Cada devolución suma puntos y aumenta el combo.

### Autos
El jugador mueve el auto horizontalmente y evita obstáculos. Cada obstáculo superado suma puntos.

## 5. Tienda
La tienda se abre con `T`. Los puntos se convierten en dinero y permiten comprar:
- sombrero rojo;
- sombrero amarillo;
- lentes;
- corona;
- pañuelo bordó.

## 6. Game loop
En cada ciclo se procesan eventos, se actualizan las estadísticas, se determina el estado visual, se actualiza el minijuego activo y se dibuja la pantalla a 60 FPS.

## 7. Objetivo
Mantener al erizo cuidado, conseguir la mayor cantidad de puntos y personalizarlo con accesorios institucionales.
