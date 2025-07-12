import os
import sys

try:
    from PyPDF2 import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    from PIL import Image
    import io
    
    print("✅ Todas las librerías importadas correctamente.")
except ImportError as e:
    print(f"❌ Error: {e}")
    print("💡 Necesitas instalar las dependencias:")
    print(">>> pip3 install -r requirements.txt")
    sys.exit(1)
    
def process_watermark_image(watermark_path):
    """
    Procesa la imagen del watermark para manejar transparencia.
    """
    try:
        # Crear carpeta temporal si no existe
        temp_dir = "temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Abrir la imagen con PIL
        img = Image.open(watermark_path)
        
        # Convertir a RGBA si no lo está
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Crear una nueva imagen con fondo transparente
        background = Image.new('RGBA', img.size, (255, 255, 255, 0))
        
        # Combinar la imagen con el fondo transparente
        result = Image.alpha_composite(background, img)
        
        # Guardar temporalmente en la carpeta temp_files
        temp_path = os.path.join(temp_dir, "temp_watermark.png")
        result.save(temp_path, 'PNG')
        
        return temp_path
    except Exception as e:
        print(f"⚠️  Error procesando watermark: {e}")
        return watermark_path

def add_images_to_pdf(input_pdf, output_pdf, header_image, watermark_image, footer_image):
    """
    Agrega las imágenes al PDF.
    
    Args:
        input_pdf: Ruta del PDF de entrada.
        output_pdf: Ruta del PDF de salida.
        header_image: Ruta de la imagen del header.
        watermark_image: Ruta de la imagen del watermark.
        footer_image: Ruta de la imagen del footer.
    """
    
    try:
        # Verificar que los archivos existen.
        if not os.path.exists(input_pdf):
            raise FileNotFoundError(f"No se encontró el PDF: {input_pdf}")
        if not os.path.exists(header_image):
            raise FileNotFoundError(f"No se encontró la imagen del header: {header_image}")
        if not os.path.exists(watermark_image):
            raise FileNotFoundError(f"No se encontró la imagen del watermark: {watermark_image}")
        if not os.path.exists(footer_image):
            raise FileNotFoundError(f"No se encontró la imagen del footer: {footer_image}")
        
        print(f"📄 Procesando: {input_pdf}")
        print(f"🖼️  Imagen del header: {header_image}")
        print(f"🖼️  Imagen del watermark: {watermark_image}")
        print(f"🖼️  Imagen del footer: {footer_image}")
        
        # Procesar el watermark para manejar transparencia
        processed_watermark = process_watermark_image(watermark_image)
        print(f"🔧 Watermark procesado: {processed_watermark}")
        
        # Leer el PDF original.
        reader = PdfReader(input_pdf)
        writer = PdfWriter()
        
        # Obtener dimensiones de la primera página.
        page = reader.pages[0]
        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.height)
        
        print(f"📏 Dimensiones del PDF: {page_width:.1f} x {page_height:.1f} puntos")
        
        # ===== <HEADER (arriba)> ===== #
        # Definir posición del header (header.jpg).
        header_width = 3.46 * inch # * pulgadas de ancho.
        header_height = 0.781 * inch # * pulgadas de alto.
        header_x = page_width - header_width - 0.082 * inch # * pulgadas del borde derecho.
        header_y = page_height - header_height - 0.20 * inch # * pulgadas del borde superior.
        
        print(f"\n🎯 Posición del header: X={header_x:.1f}, Y={header_y:.1f}")
        # ===== </HEADER (arriba)> ===== #
        
        # ===== <WATERMARK (centro)> ===== #
        # Definir posición del watermark (watermark.png) - 60% del tamaño de la página.
        watermark_width = page_width * 0.7 # 70% del ancho de la página.
        watermark_height = page_height * 0.5 # 50% del alto de la página.
        watermark_x = (page_width - watermark_width) / 2  # Centrado horizontalmente.
        watermark_y = (page_height - watermark_height) / 2  # Centrado verticalmente.
        
        print(f"🎯 Posición del watermark: X={watermark_x:.1f}, Y={watermark_y:.1f}")
        # ===== </WATERMARK (centro)> ===== #
        
        # ===== <FOOTER (abajo)> ===== #
        # Definir posición del footer (footer.jpg) - abajo, con espacios uniformes.
        margin = 0.1 * inch  # Espacio uniforme desde todos los bordes.
        footer_width = page_width - (2 * margin)  # Ancho menos los márgenes laterales.
        footer_height = 1 * inch  # Altura fija en pulgadas.
        footer_x = margin  # Mismo espacio desde el borde izquierdo.
        footer_y = margin  # Mismo espacio desde el borde inferior.
        
        print(f"🎯 Posición del footer: X={footer_x:.1f}, Y={footer_y:.1f}\n")
        # ===== </FOOTER (abajo)> ===== #
        
        # Procesar cada página.
        for page_num, page in enumerate(reader.pages):
            print(f"   Procesando página {page_num + 1}...")
            
            # Crear un overlay con la imagen del header (header.jpg).
            overlay_packet = io.BytesIO()
            overlay_canvas = canvas.Canvas(overlay_packet, pagesize=(page_width, page_height))
            
            # Dibujar la imagen del header (header.jpg).
            overlay_canvas.drawImage(
                header_image,
                header_x,
                header_y,
                width=header_width,
                height=header_height
            )
            
            # Dibujar la imagen del watermark (watermark.png) con opacidad reducida.
            overlay_canvas.saveState()
            overlay_canvas.setFillAlpha(0.15) # Opacidad al 15%.
            
            # Usar mask='auto' para manejar transparencia PNG
            overlay_canvas.drawImage(
                processed_watermark,
                x=watermark_x,
                y=watermark_y,
                width=watermark_width,
                height=watermark_height,
                mask='auto'
            )
            overlay_canvas.restoreState()
            
            # Dibujar la imagen del footer (footer.jpg).
            overlay_canvas.drawImage(
                footer_image,
                x=footer_x,
                y=footer_y,
                width=footer_width,
                height=footer_height
            )
            
            overlay_canvas.save()
            overlay_packet.seek(0)
            
            # Crear PDF del overlay.
            overlay_pdf = PdfReader(overlay_packet)
            overlay_page = overlay_pdf.pages[0]
            
            # Combinar la página original con el overlay.
            page.merge_page(overlay_page)
            
            # Agregar la página modificada al writer.
            writer.add_page(page)
        
        # Guardar el PDF resultante.
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)
        
        # Limpiar archivo temporal si se creó
        if processed_watermark != watermark_image and os.path.exists(processed_watermark):
            os.remove(processed_watermark)
            print(f"🧹 Archivo temporal eliminado: {processed_watermark}")
            
        # Limpiar carpeta temporal si está vacía
        temp_dir = "temp_files"
        if os.path.exists(temp_dir) and not os.listdir(temp_dir):
            os.rmdir(temp_dir)
            print(f"🧹 Carpeta temporal eliminada: {temp_dir}")
        
        print(f"\n✅ PDF guardado: {output_pdf} \n")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

def main():
    """Función principal."""
    print("🖼️  Agregar Header, Watermark y Footer a los PDFs en el directorio input_pdfs.")
    print("=" * 30)
    
    # Crear carpeta de salida si no existe.
    os.makedirs("output_pdfs", exist_ok=True)
    
    header_image = "images/header.jpg"
    watermark_image = "images/watermark.png"
    footer_image = "images/footer.jpg"
    
    # Repetir el proceso para cada PDF en el directorio input_pdfs.
    for file in os.listdir("input_pdfs"):
        if file.endswith(".pdf"):
            input_pdf = os.path.join("input_pdfs", file)
            output_pdf = os.path.join("output_pdfs", file)
            add_images_to_pdf(input_pdf, output_pdf, header_image, watermark_image, footer_image)
    
    print("\n🎉 ¡Proceso completado exitosamente!")

if __name__ == "__main__":
    main() 