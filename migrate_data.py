
import json

def transform_backup(input_file, output_file, old_app, new_app, model_mapping=None):
    # Determine encoding - PowerShell redirection often creates UTF-16 LE BOM
    encoding = 'utf-16'
    try:
        with open(input_file, 'r', encoding=encoding) as f:
            data = json.load(f)
    except Exception:
        # Fallback to utf-8 if utf-16 fails
        encoding = 'utf-8'
        with open(input_file, 'r', encoding=encoding) as f:
            data = json.load(f)

    
    new_data = []
    for item in data:
        model = item['model']
        app_label, model_name = model.split('.')
        
        if app_label == old_app:
            new_model = f"{new_app}.{model_name}"
            # Handle specific mapping if needed (e.g. if model names changed, but here they are same)
            # In our case: 
            # blog_ia.recursoeducativo -> blog.recursoeducativo
            # blog_general.post -> blog.post
            
            item['model'] = new_model
            new_data.append(item)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)
    print(f"Bros, transformed {len(new_data)} items from {input_file} to {output_file}")

# Transform blog_ia
transform_backup('blog_ia_backup.json', 'blog_ia_restored.json', 'blog_ia', 'blog')

# Transform blog_general
transform_backup('blog_general_backup.json', 'blog_general_restored.json', 'blog_general', 'blog')
