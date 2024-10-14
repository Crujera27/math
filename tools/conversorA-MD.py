import json
import os

def convertto_md(json_file_path, md_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        problems = json.load(json_file)
    
    md_content = ""
    for problem in problems:
        md_content += f"# {problem['title']}\n"
        md_content += "## Descripción\n"
        md_content += f"{problem['description']}\n"
        md_content += "## Solución\n"
        md_content += f"{problem['solution']}\n"
    
    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)
    
    print(f"Conversión completada. Archivo Markdown guardado en {md_file_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, 'output.json')
    md_file_path = os.path.join(base_dir, 'output.md')
    convertto_md(json_file_path, md_file_path)