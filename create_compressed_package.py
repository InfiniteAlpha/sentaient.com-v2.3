import shutil
from pathlib import Path
import subprocess

base_dir = Path('/app/sentient_website_redesign_0308')
prod_dir = base_dir / 'production_package'

print("="*80)
print("CREATING COMPRESSED PRODUCTION PACKAGE")
print("="*80)
print()

# Verify production package exists
if not prod_dir.exists():
    print("❌ Production package directory not found!")
    exit(1)

print(f"✅ Production package found: {prod_dir}")

# Create tar.gz archive
archive_name = 'sentient_website_production_v1.0'
archive_path = base_dir / f'{archive_name}.tar.gz'

print(f"\n📦 Creating compressed archive: {archive_name}.tar.gz")

try:
    # Use tar command for compression
    result = subprocess.run(
        ['tar', '-czf', str(archive_path), '-C', str(base_dir), 'production_package'],
        capture_output=True,
        text=True,
        check=True
    )
    
    if archive_path.exists():
        size = archive_path.stat().st_size
        print(f"✅ Archive created successfully!")
        print(f"   Location: {archive_path.relative_to(base_dir.parent)}")
        print(f"   Size: {size:,} bytes ({size/1024:.1f} KB)")
        
        # Also create a zip archive for Windows users
        zip_path = base_dir / f'{archive_name}.zip'
        print(f"\n📦 Creating ZIP archive for Windows compatibility...")
        
        shutil.make_archive(
            str(base_dir / archive_name),
            'zip',
            base_dir,
            'production_package'
        )
        
        if zip_path.exists():
            zip_size = zip_path.stat().st_size
            print(f"✅ ZIP archive created successfully!")
            print(f"   Location: {zip_path.relative_to(base_dir.parent)}")
            print(f"   Size: {zip_size:,} bytes ({zip_size/1024:.1f} KB)")
        
        print("\n" + "="*80)
        print("PACKAGE ARCHIVES READY FOR DISTRIBUTION")
        print("="*80)
        print(f"\n✅ TAR.GZ (Linux/Mac): {archive_name}.tar.gz")
        print(f"✅ ZIP (Windows): {archive_name}.zip")
        print("\nBoth archives contain the complete production-ready website.")
        
    else:
        print("❌ Archive creation failed!")
        
except subprocess.CalledProcessError as e:
    print(f"❌ Error creating archive: {e}")
    print(f"STDERR: {e.stderr}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n" + "="*80)