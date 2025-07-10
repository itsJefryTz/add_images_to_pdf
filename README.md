# PDF Image Processor

Script de Python para automatizar la adición de imágenes a PDFs de manera consistente.

## 📋 Estado Actual del Proyecto

### ✅ Implementado
- **Estructura de carpetas organizada**
- **Script principal** (`pdf_processor.py`) que procesa PDFs
- **Agregado de imagen de header** (header.jpg) en la esquina superior derecha
- **Coordenadas hardcodeadas** para el header: 3.46" x 0.781" 
- **Procesamiento automático** de todos los PDFs en la carpeta `input_pdfs/`
- **Manejo de errores** y verificaciones de archivos
- **Entorno virtual** configurado

### ❌ Pendiente por Implementar
- **Agregado de watermark** (watermark.png) - No implementado
- **Agregado de footer** (footer.jpg) - No implementado
- **Ajuste de coordenadas** para footer y watermark

## 🗂️ Estructura del Proyecto

```
add_images_to_pdf/
├── images/
│   ├── header.jpg      # Imagen del header (implementada)
│   ├── footer.jpg      # Imagen del footer (pendiente)
│   └── watermark.png   # Imagen del watermark (pendiente)
├── input_pdfs/
│   └── template.pdf    # PDFs originales a procesar
├── output_pdfs/
│   └── template.pdf    # PDFs procesados
├── myvenv/             # Entorno virtual de Python
├── pdf_processor.py    # Script principal
├── requirements.txt    # Dependencias
└── README.md          # Este archivo
```

## 🚀 Instalación

1. **Clonar o descargar el proyecto**
2. **Activar el entorno virtual:**
   ```bash
   source myvenv/bin/activate  # En macOS/Linux
   # o
   myvenv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Uso

### Procesamiento Básico
```bash
python pdf_processor.py
```

### Qué hace actualmente:
1. Lee todos los PDFs de la carpeta `input_pdfs/`
2. Agrega la imagen `header.jpg` en la esquina superior derecha
3. Guarda los PDFs procesados en `output_pdfs/`

### Coordenadas Actuales del Header:
- **Posición:** Esquina superior derecha
- **Tamaño:** 3.46" x 0.781"
- **Margen derecho:** 0.082"
- **Margen superior:** 0.20"

## 🔧 Dependencias

- **PyPDF2**: Manipulación de PDFs
- **reportlab**: Generación de contenido PDF
- **Pillow**: Procesamiento de imágenes

## 📝 Próximos Pasos

1. **Implementar agregado de watermark** con coordenadas precisas
2. **Implementar agregado de footer** con coordenadas precisas

## 🐛 Solución de Problemas

### Error de importación
```bash
pip install -r requirements.txt
```

### Error de archivo no encontrado
- Verificar que los archivos estén en las carpetas correctas
- Verificar nombres de archivos (case-sensitive)

### Error de permisos
```bash
chmod +x pdf_processor.py
```

## 📊 Estado de Implementación

| Funcionalidad | Estado | Archivo |
|---------------|--------|---------|
| Header Image | ✅ Implementado | `pdf_processor.py` |
| Footer Image | ❌ Pendiente | - |
| Watermark | ❌ Pendiente | - |
| Coordenadas automáticas | ❌ Pendiente | - |

---

**Última actualización:** Julio 2024
**Versión:** 1.0.0 (Solo header implementado)
