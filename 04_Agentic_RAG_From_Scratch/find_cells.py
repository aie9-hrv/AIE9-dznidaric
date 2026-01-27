import json

with open('Agentic_RAG_From_Scratch_Assignment.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
print(f'Total cells: {len(cells)}')

for i, cell in enumerate(cells):
    source = ''.join(cell.get('source', []))
    if 'Activity #2' in source or 'YOUR CODE HERE' in source or 'Test your memory-enabled' in source:
        print(f'Index {i}: id={cell.get("id", "no-id")}, type={cell["cell_type"]}')
