# Deteccion-Wincha-OpenCV
Sistema de detección de una wincha mediante visión artificial utilizando Python y OpenCV.

# 1. Descripción del proyecto
El presente proyecto tiene como finalidad desarrollar un sistema de detección de una wincha mediante técnicas de visión artificial, utilizando Python y la biblioteca OpenCV. Para la captura de imágenes se empleó DroidCam, mientras que el entrenamiento del clasificador se realizó mediante Cascade Trainer GUI. El sistema permite identificar visualmente la presencia de una wincha a partir de imágenes capturadas por una cámara y delimitar su ubicación dentro del fotograma.

# 2. Objetivos
- Desarrollar un sistema de detección de una wincha mediante visión artificial.
- Construir un dataset compuesto por imágenes positivas y negativas.
- Entrenar un clasificador en cascada mediante Cascade Trainer GUI.
- Implementar el modelo entrenado utilizando OpenCV y Python.
- Evaluar el funcionamiento del detector y reconocer sus limitaciones.

# 3. Herramientas utilizadas

- Python.
- OpenCV.
- DroidCam.
- Cascade Trainer GUI.
- Visual Studio Code.

# 4. Estructura del proyecto

El repositorio se organiza en carpetas que contienen el código fuente, el conjunto de datos, el modelo entrenado y las evidencias de funcionamiento.

# 5. Instalación y requisitos

Instalar Python y las bibliotecas necesarias:
```bash
pip install opencv-python imutils
```

También se requiere configurar DroidCam y disponer del archivo del clasificador entrenado `cascade.xml`.

# 6. Ejecución del proyecto

1. Conectar el teléfono móvil mediante DroidCam.
2. Verificar la dirección de transmisión de video.
3. Comprobar que el archivo `cascade.xml` se encuentre en la ubicación correspondiente.
4. Ejecutar el programa de detección:

```bash
python codigo/deteccion_wincha.py
```

5. Colocar la wincha frente a la cámara y observar el resultado en pantalla.

# 7. Resultados

El proyecto contempla la captura de imágenes positivas y negativas, el entrenamiento del clasificador y la implementación de la detección mediante OpenCV.
Las evidencias visuales del entrenamiento y de las pruebas realizadas se encuentran en la carpeta `resultados`.

# 8. Limitaciones
El rendimiento del clasificador depende de la cantidad y variedad de imágenes utilizadas durante el entrenamiento, las condiciones de iluminación, la orientación del objeto y los parámetros de detección establecidos.

# 9. Posibles mejoras

- Incrementar la cantidad de imágenes del dataset.
- Incorporar diferentes condiciones de iluminación y orientación.
- Optimizar los parámetros del clasificador.
- Realizar pruebas independientes para evaluar los falsos positivos y falsos negativos.
- Explorar otros algoritmos de detección de objetos.

# 10. Autores

Tracy Guadalupe, Quispe Moran

Asignatura: Herramientas de desarrollo profesional – Civil.

Año: 2026.
