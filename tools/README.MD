# Herramientas

La carpeta `tools` contiene scripts y plantillas útiles para la gestión y conversión de problemas matemáticos en el proyecto. A continuación se describen los componentes principales:

## `conversor.py`

Este script convierte archivos Markdown que contienen problemas matemáticos con soporte para MathJax a un formato JSON compatible con `problems.json`.

### Uso

Para ejecutar el script, abre una terminal en el directorio `math` y ejecuta:

```bash
python3 conversor.py
```

### Estructura del archivo Markdown

El archivo Markdown debe seguir la siguiente estructura:

```markdown
# Título del Problema
## Descripción
Aquí va la descripción del problema. Puedes utilizar MathJax para incluir fórmulas matemáticas. Por ejemplo, una fórmula en línea: \( E = mc^2 \) y una fórmula en bloque:
\[
E = mc^2
\]

## Solución
Aquí va la solución del problema. También puedes utilizar MathJax para incluir fórmulas matemáticas.
\[
R_s = \frac{2G \cdot 10M_{\odot}}{c^2}
\]
```

## `conversorA-MD.py`

Este script convierte archivos JSON que contienen problemas matemáticos a un formato Markdown compatible con `template.md`.

### Uso

Para ejecutar el script, abre una terminal en el directorio `math` y ejecuta:

```bash
python3 json_to_md.py
```

### Estructura del archivo JSON

El archivo JSON debe seguir la siguiente estructura:

```json
[
    {
        "title": "Título del Problema",
        "description": "Aquí va la descripción del problema. Puedes utilizar MathJax para incluir fórmulas matemáticas. Por ejemplo, una fórmula en línea: \\( E = mc^2 \\) y una fórmula en bloque:\n\\[\nE = mc^2\n\\]",
        "solution": "Aquí va la solución del problema. También puedes utilizar MathJax para incluir fórmulas matemáticas.\n\\[\nR_s = \\frac{2G \\cdot 10M_{\\odot}}{c^2}\n\\]"
    }
]
```

## `verify.py`

Este script verifica que el archivo `problems.json` esté bien formado y que las fórmulas de MathJax estén correctamente delimitadas.

### Uso

Para ejecutar el script, abre una terminal en el directorio `math` y ejecuta:

```bash
python verify.py
```

## `template.md`

Este archivo es una plantilla para crear nuevos problemas en formato Markdown. Incluye secciones para el título, la descripción y la solución del problema, con ejemplos de cómo utilizar MathJax para incluir fórmulas matemáticas.

### Estructura del archivo

```markdown
# Título del Problema
## Descripción
Aquí va la descripción del problema. Puedes utilizar MathJax para incluir fórmulas matemáticas. Por ejemplo, una fórmula en línea: \( E = mc^2 \) y una fórmula en bloque:
\[
E = mc^2
\]

## Solución
Aquí va la solución del problema. También puedes utilizar MathJax para incluir fórmulas matemáticas.
\[
R_s = \frac{2G \cdot 10M_{\odot}}{c^2}
\]
```

### Recursos Adicionales

- **Página Principal de MathJax**: [MathJax](https://www.mathjax.org/)
- **Guía de Inicio Rápido**: [MathJax Quick Start Guide](https://docs.mathjax.org/en/latest/)
- **Referencia de Símbolos y Comandos**: [MathJax TeX and LaTeX Support](https://docs.mathjax.org/en/latest/input/tex/index.html)
- **MathJax en GitHub**: [MathJax GitHub Repository](https://github.com/mathjax/MathJax)