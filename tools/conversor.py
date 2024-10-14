import json
import os

def parsemd(md_content):
    problems = []
    problem = {}
    lines = md_content.split('\n')
    
    for line in lines:
        if line.startswith('# '):
            if problem:
                problems.append(problem)
                problem = {}
            problem['title'] = line[2:].strip()
        elif line.startswith('## Descripción'):
            problem['description'] = ''
        elif line.startswith('## Solución'):
            problem['solution'] = ''
        elif 'description' in problem and 'solution' not in problem:
            problem['description'] += line + '\n'
        elif 'solution' in problem:
            problem['solution'] += line + '\n'
    
    if problem:
        problems.append(problem)
    
    return problems

def converttojson(md_file_path, json_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    problems = parsemd(md_content)
    
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(problems, json_file, ensure_ascii=False, indent=4)
    
    print(f"Conversión completada. Archivo JSON guardado en {json_file_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_file_path = os.path.join(base_dir, 'template.md')
    json_file_path = os.path.join(base_dir, 'output.json')
    converttojson(md_file_path, json_file_path)