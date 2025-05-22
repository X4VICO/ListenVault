---
tags:
  - tutorial
  - software
  - herramienta
aliases:
  - fmpeg
---
---

**Descarga FFmpeg para Windows** desde la página oficial:
Web: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
Pulsa en **"Release builds"** y baja un `.zip`.

**Extrae el `.zip`** en una carpeta, por ejemplo: ``C:\ffmpeg``

**Agrega FFmpeg al PATH del sistema** (importante):
- Abre el menú de inicio → escribe "Editar las variables de entorno del sistema" → entra en "Variables de Entorno".
- En “Variables del sistema” busca la que dice **Path** → **Editar** → **Nuevo**.
- Añade la ruta: ``C:\ffmpeg\bin``
- Guarda y cierra todo.

**Comprueba que esté bien instalado**:

Abre una consola (cmd o Powershell) y escribe: ``ffmpeg -version``
Si sale la versión, ¡ya está funcionando!