with open('aml_system.py', 'r') as f:
    lines = f.readlines()

# Replace execute_query with execute_update on specific lines
fixed = 0
for i, line in enumerate(lines):
    if 'self.db.execute_query(' in line and i < len(lines) - 5:
        # Check if the next lines contain INSERT
        next_content = ''.join(lines[i:i+5])
        if 'INSERT INTO cybersecurity_threats' in next_content or 'INSERT INTO threat_indicators' in next_content:
            lines[i] = line.replace('execute_query(', 'execute_update(')
            fixed += 1

with open('aml_system.py', 'w') as f:
    f.writelines(lines)

print(f'Fixed: {fixed} execute_query -> execute_update for INSERT statements')
