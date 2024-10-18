import os
import yaml

# Path to the mkdocs.yml file
MKDOCS_FILE = 'mkdocs.yml'

# Root directory for documentation
DOCS_DIR = 'docs'

def scan_docs(directory):
    """Scan the docs directory and generate a structure based on folders and files."""
    structure = []
    overview_page = {'Introduction': 'index.md'}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                # Create relative paths for navigation
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                
                # Replace dashes and underscores with spaces and capitalize the name
                name = os.path.splitext(file)[0].replace('-', ' ').replace('_', ' ').title()

                # Skip adding 'index.md' as it should always be the introduction page
                if name.lower() == 'index':
                    continue

                # For nested files, create nested lists
                if root != directory:
                    sub_dir = os.path.basename(root).replace('-', ' ').replace('_', ' ').title()
                    existing = next((item for item in structure if sub_dir in item), None)
                    if existing:
                        existing[sub_dir].append({name: relative_path})
                    else:
                        structure.append({sub_dir: [{name: relative_path}]})
                else:
                    structure.append({name: relative_path})

    # Insert the Introduction page as the first item in the structure
    structure.insert(0, overview_page)

    return structure

def update_mkdocs_config():
    """Read mkdocs.yml, update the navigation, and write it back."""
    # Load the existing mkdocs.yml file
    with open(MKDOCS_FILE, 'r') as f:
        config = yaml.safe_load(f)

    # Scan the docs directory to build the new navigation
    new_nav = scan_docs(DOCS_DIR)

    # Update the config's navigation
    config['nav'] = new_nav

    # Write the updated config back to mkdocs.yml
    with open(MKDOCS_FILE, 'w') as f:
        yaml.dump(config, f, sort_keys=False)

if __name__ == '__main__':
    update_mkdocs_config()
