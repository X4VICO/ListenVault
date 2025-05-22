import os
import subprocess
import whisper
import sys
import re
import glob

# Función para limpiar nombres de archivo
def limpiar_nombre(nombre):
    nombre = re.sub(r'\W+', '_', nombre)
    return nombre.strip('_')

# Pedir URL
url = input("🎧 Introduce la URL del podcast o video: ").strip()

if not url:
    print("❌ No se ha introducido ninguna URL. Saliendo...")
    sys.exit(1)

# Crear carpeta de resultados
output_folder = "resultados"
os.makedirs(output_folder, exist_ok=True)

# Nombre base del archivo
nombre_base = limpiar_nombre(url)

# Archivo de salida SIN extensión
audio_output_no_ext = os.path.join(output_folder, nombre_base)

# 1. Descargar solo el audio en MP3 usando yt-dlp
print("\n⬇️ Descargando el audio...")
subprocess.run([
    "python", "-m", "yt_dlp",
    "-x", "--audio-format", "mp3",
    "-o", f"{audio_output_no_ext}.%(ext)s",  # Nota el .%(ext)s
    url
])

# Buscar el archivo .mp3 generado
mp3_files = glob.glob(f"{output_folder}/{nombre_base}*.mp3")
if not mp3_files:
    print("❌ No se encontró el archivo de audio descargado.")
    sys.exit(1)

audio_file = mp3_files[0]  # usamos el primero que aparezca

# 2. Transcribir el audio con Whisper
print("\n📝 Transcribiendo el audio... (esto puede tardar un poco)")
model = whisper.load_model("small")
result = model.transcribe(audio_file, language="Spanish")

# 3. Guardar la transcripción
transcription_output = os.path.join(output_folder, f"{nombre_base}_transcripcion.md")
print("\n💾 Guardando la transcripción...")
with open(transcription_output, "w", encoding="utf-8") as f:
    f.write(f"# Transcripción de {url}\n\n")
    f.write(result["text"])

print(f"\n✅ ¡Todo listo! Archivo de transcripción guardado en: {transcription_output}")
