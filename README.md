# PDF Image Processor

Un script de Python para automatizar la adición de imágenes (header, watermark y footer) a múltiples archivos PDF de manera profesional.

## 🚀 Funcionalidades

### ✅ Implementadas
- **Header Image**: Agrega una imagen en la parte superior derecha del PDF
- **Watermark**: Agrega una imagen como marca de agua centrada con opacidad configurable
- **Footer Image**: Agrega una imagen en la parte inferior del PDF con márgenes uniformes
- **Procesamiento por lotes**: Procesa automáticamente todos los PDFs en la carpeta `input_pdfs`
- **Manejo de transparencia**: Procesa correctamente imágenes PNG con transparencia
- **Archivos temporales**: Sistema organizado de archivos temporales con limpieza automática

### 📋 Características Técnicas

#### Header (Imagen superior)
- **Posición**: Esquina superior derecha
- **Tamaño**: 3.46 x 0.781 pulgadas
- **Margen**: 0.082 pulgadas desde el borde derecho, 0.20 pulgadas desde el borde superior

#### Watermark (Marca de agua)
- **Posición**: Centrado vertical y horizontalmente
- **Tamaño**: 70% del ancho x 50% del alto de la página
- **Opacidad**: 15% (configurable)
- **Transparencia**: Manejo automático de PNGs transparentes

#### Footer (Imagen inferior)
- **Posición**: Parte inferior de la página
- **Tamaño**: Ancho completo menos márgenes uniformes
- **Margen**: 0.1 pulgadas desde todos los bordes
- **Altura**: 1 pulgada

## 📁 Estructura del Proyecto

```
add_images_to_pdf/
├── pdf_processor.py          # Script principal
├── requirements.txt          # Dependencias
├── .gitignore               # Archivos ignorados por Git
├── images/                  # Carpeta de imágenes
│   ├── header.jpg          # Imagen del header
│   ├── watermark.png       # Imagen del watermark (con transparencia)
│   └── footer.jpg          # Imagen del footer
├── input_pdfs/             # PDFs de entrada
├── output_pdfs/            # PDFs procesados
└── temp_files/             # Archivos temporales (se crea automáticamente)
```

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd add_images_to_pdf
   ```

2. **Crear entorno virtual**:
   ```bash
   python3 -m venv myvenv
   source myvenv/bin/activate  # En Windows: myvenv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencias

- **PyPDF2**: Para manipulación de PDFs
- **reportlab**: Para dibujar imágenes en PDFs
- **Pillow (PIL)**: Para procesamiento de imágenes

## 🎯 Uso

### Preparación
1. Coloca tus imágenes en la carpeta `images/`:
   - `header.jpg` - Imagen para el header
   - `watermark.png` - Imagen para el watermark (recomendado PNG con transparencia)
   - `footer.jpg` - Imagen para el footer

2. Coloca los PDFs a procesar en la carpeta `input_pdfs/`

### Ejecución
```bash
python pdf_processor.py
```

### Resultado
- Los PDFs procesados se guardarán en la carpeta `output_pdfs/`
- Los archivos temporales se crean en `temp_files/` y se eliminan automáticamente

## ⚙️ Configuración

### Modificar posiciones y tamaños
Edita las variables en `pdf_processor.py`:

```python
# Header
header_width = 3.46 * inch
header_height = 0.781 * inch
header_x = page_width - header_width - 0.082 * inch
header_y = page_height - header_height - 0.20 * inch

# Watermark
watermark_width = page_width * 0.7  # 70% del ancho
watermark_height = page_height * 0.5  # 50% del alto
watermark_x = (page_width - watermark_width) / 2
watermark_y = (page_height - watermark_height) / 2

# Footer
margin = 0.1 * inch  # Margen uniforme
footer_width = page_width - (2 * margin)
footer_height = 1 * inch
footer_x = margin
footer_y = margin
```

### Modificar opacidad del watermark
```python
overlay_canvas.setFillAlpha(0.15)  # Cambia 0.15 por el valor deseado (0.0 a 1.0)
```

## 🔧 Características Avanzadas

### Manejo de Transparencia
- El script procesa automáticamente imágenes PNG con transparencia
- Crea archivos temporales optimizados para evitar fondos negros
- Limpieza automática de archivos temporales

### Procesamiento por Lotes
- Procesa automáticamente todos los archivos `.pdf` en `input_pdfs/`
- Crea la carpeta `output_pdfs/` si no existe
- Manejo de errores individual por archivo

### Logging Detallado
- Muestra las dimensiones de cada PDF
- Indica las posiciones calculadas para cada imagen
- Confirma la eliminación de archivos temporales

## 🐛 Solución de Problemas

### Error: "No se encontró el PDF"
- Verifica que los PDFs estén en la carpeta `input_pdfs/`
- Asegúrate de que tengan extensión `.pdf`

### Error: "No se encontró la imagen"
- Verifica que las imágenes estén en la carpeta `images/`
- Confirma los nombres exactos: `header.jpg`, `watermark.png`, `footer.jpg`

### Watermark con fondo negro
- El script maneja automáticamente la transparencia
- Si persiste, verifica que el PNG tenga transparencia real

### Error de dependencias
```bash
pip install --upgrade -r requirements.txt
```

## 📝 Notas Técnicas

- **Unidades**: Todas las medidas están en pulgadas (inch)
- **Coordenadas**: Sistema de coordenadas de PDF (0,0 en la esquina inferior izquierda)
- **Formatos soportados**: JPG, PNG (con transparencia)
- **Compatibilidad**: Funciona con PDFs de cualquier tamaño

## 🤝 Contribuciones

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio.
