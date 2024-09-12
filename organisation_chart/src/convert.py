import csv

# Configura il percorso dei file
csv_file_path = 'data.csv'
js_file_path = 'data.js'

# Funzione per convertire i dati CSV in una lista di dizionari
def csv_to_dict_list(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

# Funzione per generare il contenuto JS dal dizionario
def generate_js_content(data):
    js_content = 'const employees = [\n'
    for row in data:
        js_content += '  {\n'
        for key, value in row.items():
            # Gestione delle stringhe vuote
            if value == " ":
                js_content += f'    {key}: "",\n'
            else:
                js_content += f'    {key}: "{value}",\n'
        js_content += '  },\n'
    js_content += '];\n\n'
    js_content += 'export default employees;\n'
    return js_content

# Leggi il CSV e genera il contenuto JS
data = csv_to_dict_list(csv_file_path)
js_content = generate_js_content(data)

# Scrivi il contenuto JS nel file
with open(js_file_path, 'w', encoding='utf-8') as jsfile:
    jsfile.write(js_content)

print(f'File {js_file_path} è stato generato con successo!')
