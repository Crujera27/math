import json
import re
import os

def verifyproblemsdata(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Error: El archivo JSON no está bien formado.")
        return False
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encontró.")
        return False

    if not isinstance(data, list):
        print("Error: El archivo JSON debe contener una lista de problemas.")
        return False

    for problem in data:
        if not all(key in problem for key in ['title', 'description', 'solution']):
            print(f"Error: El problema {problem.get('title', 'sin título')} no tiene todos los campos requeridos.")
            return False

        if not verifymathjax(problem['description']):
            print(f"Error: Fórmulas de MathJax mal formadas en la descripción del problema: {problem['title']}")
            return False

        if not verifymathjax(problem['solution']):
            print(f"Error: Fórmulas de MathJax mal formadas en la solución del problema: {problem['title']}")
            return False

    print("El archivo problems.json está bien formado.")
    return True

def verifymathjax(texto):
    inline_pattern = re.compile(r'\\\((.*?)\\\)')
    block_pattern = re.compile(r'\\\[(.*?)\\\]')
    inline_matches = inline_pattern.findall(texto)
    block_matches = block_pattern.findall(texto)
    return all(inline_matches) and all(block_matches)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'output.json')
    verifyproblemsdata(file_path)