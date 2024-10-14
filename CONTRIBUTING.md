# Cómo Contribuir Añadiendo un Nuevo Problema

¡Gracias por tu interés en contribuir a nuestro proyecto! Aquí tienes una guía paso a paso para añadir un nuevo problema.

## Paso 1: Crear un Fork del Repositorio

1. Ve a la página principal del repositorio en GitHub.
2. Haz clic en el botón "Fork" en la esquina superior derecha de la página.
3. Esto creará una copia del repositorio en tu cuenta de GitHub.

## Paso 2: Clonar el Repositorio Forkeado

Clona el repositorio forkeado a tu máquina local:

```sh
git clone https://github.com/Crujera27/math.git
cd math
```

## Paso 3: Crear una Nueva Rama

Crea una nueva rama para tu contribución:

```sh
git checkout -b agregar-nuevo-problema
```

## Paso 4: Añadir el Nuevo Problema

1. Abre el archivo `web/problems.json`.
2. Añade una nueva entrada para tu problema siguiendo el formato existente. Aquí tienes un ejemplo:

```json
{
    "title": "Nuevo Problema de Física Cuántica",
    "description": "Describe el problema aquí.",
    "solution": "Proporciona la solución aquí."
}
```

3. Si es necesario, añade un nuevo script en el directorio `verify/` para verificar los cálculos del problema. Por ejemplo, crea un archivo llamado `NuevoProblemaDeFisicaCuantica.py` y añade el código necesario.

## Paso 5: Probar los Cambios

Asegúrate de que tu nuevo problema se carga correctamente y que el script de verificación funciona como se espera. Si tu problema incluye fórmulas matemáticas, puedes utilizar el formato MathJax para una mejor presentación.

### Ejemplo de Formato MathJax

Para incluir fórmulas matemáticas en tu problema, utiliza el siguiente formato:

- Fórmulas en línea: `\( E = mc^2 \)`
- Fórmulas en bloque:
  ```markdown
  \[
  E = mc^2
  \]
  ```

## Paso 6: Verificar el Formato del Archivo `problems.json`

Antes de hacer commit de tus cambios, utiliza el script de verificación para asegurarte de que el archivo `problems.json` está bien formado:

```sh
python 

verify.py


```

Este script verificará que el archivo `problems.json` tenga el formato correcto y que las fórmulas de MathJax estén bien formadas.

## Paso 7: Hacer Commit y Push de los Cambios

Guarda tus cambios y súbelos a tu repositorio forkeado:

```sh
git add 

problems.json

 verify/NuevoProblemaDeFisicaCuantica.py
git commit -m "Añadir nuevo problema de física cuántica"
git push origin agregar-nuevo-problema
```

## Paso 8: Crear un Pull Request

1. Ve a la página de tu repositorio forkeado en GitHub.
2. Haz clic en el botón "Compare & pull request".
3. Proporciona una descripción detallada de los cambios que has realizado.
4. Haz clic en "Create pull request".

## Paso 9: Revisión

Uno de los administradores del proyecto revisará tu pull request. Si se necesitan cambios adicionales, se te notificará en los comentarios del pull request.

## Paso 10: Aprobación y Merge

Una vez que tu pull request sea aprobado, se hará merge en la rama principal del proyecto.

¡Gracias por tu contribución!
