# 🦔 Mascota Virtual de Informática

## IPET 249 “Nicolás Copérnico”
**Especialidad:** Informática  
**Asignatura:** Laboratorio de Aplicaciones II  
**Curso:** 6° G  
**Año:** 2026

## Concepto actualizado
La mascota es un **erizo marrón tierno**, inspirado en una mascota virtual de cuidado, pero con diseño propio. El personaje representa la orientación en Informática mediante sus estados, minijuegos, sistema de puntos y tienda de accesorios.

Las cuatro imágenes entregadas representan sus estados principales:

- `normal.png`: erizo sonriendo.
- `feliz.png`: erizo con los brazos arriba.
- `llorando.png`: erizo llorando cuando tiene hambre.
- `bostezando.png`: erizo bostezando cuando tiene poca energía.

## Estados de la mascota

| Estado | Condición | Imagen |
|---|---|---|
| Sonriendo | Estado normal | `img/normal.png` |
| Brazos arriba | Felicidad alta y promedio general alto | `img/feliz.png` |
| Llorando | Hambre menor a 30% | `img/llorando.png` |
| Bostezando | Energía menor a 25% | `img/bostezando.png` |

## Funciones
- Alimentar, bañar, jugar, programar y dormir.
- Barras de energía, hambre, higiene, felicidad y código.
- Minijuegos con puntos: Space Invaders, Vóley y Autos.
- Conversión de puntos a dinero.
- Tienda para comprar ropa y accesorios.
- Sonidos WAV y tecla `M` para activar/desactivar audio.

## Controles
- `1`: alimentar.
- `2`: bañar.
- `3`: abrir minijuegos.
- `4`: programar.
- `5`: dormir.
- `T`: abrir tienda.
- `M`: activar/desactivar sonidos.
- `R`: reiniciar estadísticas.
- `ESC`: volver desde la tienda.
- En los minijuegos: flechas izquierda/derecha; espacio para disparar en Space Invaders.

## Instalación en Visual Studio Code
```powershell
python -m pip install -r requirements.txt
python main.py
```

Si usás entorno virtual:
```powershell
.venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
```

## Estructura
```text
mascota-virtual-informatica/
├── main.py
├── README.md
├── GDD.md
├── IA_LOG.md
├── requirements.txt
├── img/
│   ├── normal.png
│   ├── feliz.png
│   ├── llorando.png
│   ├── bostezando.png
│   └── README.md
└── assets/
    └── sounds/
```

## Importante al actualizar el proyecto
Si GitHub ya muestra los cambios pero el juego sigue mostrando el pingüino, estás ejecutando otra carpeta. Desde la carpeta correcta ejecutá:
```powershell
git pull origin main
python main.py
```
También podés abrir la carpeta correcta con:
```powershell
code C:\ruta\a\mascota-virtual-informatica
```
