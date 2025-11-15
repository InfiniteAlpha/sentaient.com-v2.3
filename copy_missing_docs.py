from pathlib import Path
import shutil

base_dir = Path('/app/sentient_website_redesign_0308')
docs_dir = base_dir / 'docs'
docs_dir.mkdir(exist_ok=True)

# Check if documentation was created in a temp location or needs to be recreated
print("Checking for documentation files...")

# The create_documentation.py script should have created these
# Let's verify and copy them to production package if needed

deployment_guide_content = open(base_dir / 'create_documentation.py', 'r').read()

# Since the files weren't created in iteration 9, let's create them now
print("Creating missing documentation files...")

# Import and run the functions directly
import sys
sys.path.insert(0, str(base_dir))

try:
    from create_documentation import create_deployment_guide, create_user_manual
    
    deployment_path = create_deployment_guide()
    print(f"✅ Created: {deployment_path}")
    
    user_manual_path = create_user_manual()
    print(f"✅ Created: {user_manual_path}")
    
    # Copy to production package
    prod_dir = base_dir / 'production_package' / 'docs'
    prod_dir.mkdir(parents=True, exist_ok=True)
    
    if deployment_path.exists():
        shutil.copy2(deployment_path, prod_dir / 'DEPLOYMENT_GUIDE.md')
        print(f"✅ Copied to production: DEPLOYMENT_GUIDE.md")
    
    if user_manual_path.exists():
        shutil.copy2(user_manual_path, prod_dir / 'USER_MANUAL.md')
        print(f"✅ Copied to production: USER_MANUAL.md")
    
    print("\n✅ All documentation files created and copied successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    print("Creating files directly...")
    
    # If import fails, create the files directly by executing the script
    import subprocess
    result = subprocess.run(['python', str(base_dir / 'create_documentation.py')], 
                          capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)