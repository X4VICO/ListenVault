# Resume-Podcasts
Herramienta para pasar videos a textos para su futuro procesado con IA

---

# Objetivo
- Descargar audio de un video/podcast con **yt-dpl**
- Transcribir el audio a texto con **Wisper(Open AI)**
- Guardar el texto en un archivo *.txt* o *.md*
- Ahora mismo, de forma manual, copiar el contenido del archivo de texto y pasarlo por IA para hacer el resumen. (a futuro se puede implementar mediante API o un modelo local).
# Dependencias
Para que el script funcione correctamente tenemos que tener instalados los siguientes paquetes:
``pip install yt-dlp openai-whisper``

También tendremos que instalar **ffmpeg**
``sudo apt install ffmpeg`` o [[Instalar Fmpeg en Windows|guía para instalar en Windows]]

# Funcionamiento
1. Ejecutar script
2. Introducir URL
3. Esperar a que acabe
4. Subir el archivo a IA para procesar datos
5. Guardar resultado según formato pedido

> [!NOTE]
> - **Formato `.md`** (Markdown) es mejor si luego quieres leerlo más bonito (títulos, listas, citas...).
> 
> - **`medium`** es un modelo de Whisper bastante equilibrado entre precisión y velocidad. Si ves que tarda mucho, puedes cambiar `"medium"` por `"small"` o `"tiny"`
> 
> - **Archivos**: después tendrás el audio (`audio.mp3`) y la transcripción (`transcripcion.md`) en la misma carpeta del script.

---
# Tabla de Modelos de Whisper

| Modelo   | Tamaño Aprox. | Velocidad de transcripción | Precisión | RAM Recomend. | Uso general     |
|----------|----------------|-----------------------------|-----------|----------------|------------------|
| `tiny`   | ~75 MB         | Muy rápida                  | Baja      | ≥ 1 GB         | Tests rápidos    |
| `base`   | ~140 MB        | Rápida                      | Baja-Media| ≥ 1 GB         | Casos básicos    |
| `small`  | ~460 MB        | Moderada                    | Media     | ≥ 2 GB         | Equilibrado      |
| `medium` | ~1.5 GB        | Lenta                       | Alta      | ≥ 5 GB         | Buena calidad    |
| `large`  | ~2.9 GB        | Más lenta                   | Muy alta  | ≥ 10 GB        | Máxima fidelidad |
## ¿Cuándo usar cada modelo?

| Situación / Necesidad                         | Modelo recomendado |
|----------------------------------------------|--------------------|
| Pruebas rápidas o scripts desechables        | `tiny`             |
| Transcripciones simples sin ruido            | `base` o `small`   |
| Podcast con calidad de audio razonable       | `small`            |
| Audios con varios hablantes o ruido leve     | `medium`           |
| Uso profesional, publicación o archivado     | `medium` o `large` |
| Alta precisión + audio difícil o con ruido   | `large`            |
| PC con poca RAM o sin GPU dedicada           | `tiny` o `base`    |

[🟣 Script en python](ResumePodcast.py)
