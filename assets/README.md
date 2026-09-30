# Assets - Mascota Virtual de Informática

## Descripción

Esta carpeta contiene todos los assets (recursos) del proyecto:

- **sounds/** - Archivos de audio WAV
- **images/** - Imágenes SVG
- **generate_assets.py** - Script para generar assets automáticamente

## Generación automática

Si los assets no existen, el script `generate_assets.py` se ejecuta automáticamente al iniciar el juego.

Para ejecutarlo manualmente:

```bash
python assets/generate_assets.py
```

## Sonidos procedurales

Los sonidos se generan usando ondas de diferentes formas:

- **Triángulo:** Sonidos suave y orgánicos (comer, feliz)
- **Senoide:** Sonidos profundos y continuos (baño, dormir, triste)
- **Cuadrado:** Sonidos digitales y electrónicos (jugar)
- **Diente de sierra:** Sonidos complejos y robóticos (programar)

## Imágenes SVG

Las imágenes se generan en formato SVG (vectorial) escalable sin pérdida de calidad.

### Assets incluidos:

1. **shield_ipet249.svg** - Escudo institucional del IPET 249
2. **pet_idle.svg** - Pingüino en posición neutra
3. **pet_happy.svg** - Pingüino feliz
4. **pet_triste.svg** - Pingüino triste
5. **pet_sleep.svg** - Pingüino dormido

## Reemplazo de assets

Puedes reemplazar los assets generados con tus propios archivos:

1. Coloca sonidos WAV en `sounds/`
2. Coloca imágenes en `images/`
3. Actualiza las rutas en `main.py` si es necesario

## Especificaciones técnicas

### Sonidos
- **Formato:** WAV PCM 16-bit
- **Frecuencia de muestreo:** 22050 Hz
- **Canales:** Mono (1)
- **Duración:** 0.2 - 0.45 segundos
- **Volumen:** 0.38 - 0.6 (normalizado)

### Imágenes
- **Formato:** SVG (Scalable Vector Graphics)
- **Resolución:** Escalable (viewport 220x220)
- **Colores:** RGB + Gradientes
- **Bordes:** Suavizados (border-radius)

---

**IPET 249 | Especialidad en Informática | 2026**
