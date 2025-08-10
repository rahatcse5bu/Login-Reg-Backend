#!/usr/bin/env python3
"""
MySQL Database Setup Script for Django Login & Registration Backend
This script helps you set up the MySQL database for your Django project.
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    print("🐬 MySQL Database Setup for Django Backend")
    print("=" * 50)

def check_mysql_installed():
    """Check if MySQL is installed and accessible"""
    try:
        result = subprocess.run(['mysql', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✅ MySQL is installed: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ MySQL is not installed or not in PATH")
        print("   Please install MySQL from: https://dev.mysql.com/downloads/mysql/")
        return False

def check_python_packages():
    """Check if required Python packages are installed"""
    try:
        import MySQLdb
        print("✅ mysqlclient is installed")
        return True
    except ImportError:
        print("❌ mysqlclient not found")
        print("   Installing mysqlclient...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'mysqlclient'], check=True)
            print("✅ mysqlclient installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install mysqlclient")
            return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists():
        if env_example.exists():
            print("📝 Creating .env file from .env.example...")
            with open(env_example, 'r') as src, open(env_file, 'w') as dst:
                dst.write(src.read())
            print("✅ .env file created")
        else:
            print("📝 Creating .env file...")
            env_content = """# Database Configuration
DB_NAME=login_reg_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306

# Django Configuration
SECRET_KEY=django-insecure-2tsvt2y42zyf8jz%#njuo-kv170#d#q2as_@5z1!s3l*r24ls2
DEBUG=True
"""
            with open(env_file, 'w') as f:
                f.write(env_content)
            print("✅ .env file created")
    else:
        print("✅ .env file already exists")

def get_mysql_credentials():
    """Get MySQL credentials from user"""
    print("\n🔐 MySQL Database Setup")
    print("Please provide your MySQL credentials:")
    
    db_name = input("Database name [login_reg_db]: ").strip() or "login_reg_db"
    db_user = input("MySQL username [root]: ").strip() or "root"
    db_password = input("MySQL password: ").strip()
    db_host = input("MySQL host [localhost]: ").strip() or "localhost"
    db_port = input("MySQL port [3306]: ").strip() or "3306"
    
    return {
        'DB_NAME': db_name,
        'DB_USER': db_user,
        'DB_PASSWORD': db_password,
        'DB_HOST': db_host,
        'DB_PORT': db_port
    }

def update_env_file(credentials):
    """Update .env file with MySQL credentials"""
    env_file = Path('.env')
    
    if env_file.exists():
        # Read existing content
        with open(env_file, 'r') as f:
            content = f.read()
        
        # Update database credentials
        for key, value in credentials.items():
            if f"{key}=" in content:
                # Replace existing line
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if line.startswith(f"{key}="):
                        lines[i] = f"{key}={value}"
                        break
                content = '\n'.join(lines)
            else:
                # Add new line
                content += f"\n{key}={value}"
        
        # Write back to file
        with open(env_file, 'w') as f:
            f.write(content)
        
        print("✅ .env file updated with MySQL credentials")

def create_mysql_database(credentials):
    """Create MySQL database"""
    print(f"\n📊 Creating MySQL database: {credentials['DB_NAME']}")
    
    sql_commands = f"""
CREATE DATABASE IF NOT EXISTS {credentials['DB_NAME']} 
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Optional: Create dedicated user (uncomment if needed)
-- CREATE USER IF NOT EXISTS 'django_user'@'localhost' IDENTIFIED BY 'secure_password';
-- GRANT ALL PRIVILEGES ON {credentials['DB_NAME']}.* TO 'django_user'@'localhost';
-- FLUSH PRIVILEGES;

USE {credentials['DB_NAME']};
SHOW TABLES;
"""
    
    print("SQL commands to execute:")
    print("-" * 30)
    print(sql_commands)
    print("-" * 30)
    
    print(f"\nTo create the database, run:")
    print(f"mysql -u {credentials['DB_USER']} -p")
    print("Then execute the SQL commands above.")
    
    return True

def run_django_migrations():
    """Run Django migrations"""
    print("\n🔄 Running Django migrations...")
    
    try:
        # Remove old migrations
        migrations_dir = Path('authentication/migrations')
        if migrations_dir.exists():
            for file in migrations_dir.glob('*.py'):
                if file.name != '__init__.py':
                    file.unlink()
            print("✅ Cleaned old migrations")
        
        # Create new migrations
        subprocess.run([sys.executable, 'manage.py', 'makemigrations'], check=True)
        print("✅ Created new migrations")
        
        # Apply migrations
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        print("✅ Applied migrations")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Migration failed: {e}")
        return False

def main():
    print_header()
    
    # Check prerequisites
    if not check_mysql_installed():
        return False
    
    if not check_python_packages():
        return False
    
    # Setup environment
    create_env_file()
    
    # Get user input
    print("\n" + "=" * 50)
    proceed = input("Do you want to configure MySQL database? (y/n): ").strip().lower()
    
    if proceed == 'y':
        credentials = get_mysql_credentials()
        update_env_file(credentials)
        
        if create_mysql_database(credentials):
            print("\n🎯 Next Steps:")
            print("1. Create the MySQL database using the SQL commands above")
            print("2. Run: python setup_mysql.py --migrate")
            print("3. Run: python manage.py createsuperuser")
            print("4. Run: python manage.py runserver")
            print("5. Test: python test_api.py")
    
    elif len(sys.argv) > 1 and sys.argv[1] == '--migrate':
        print("\n🔄 Running migrations only...")
        if run_django_migrations():
            print("\n🎉 Database setup complete!")
            print("Next: python manage.py createsuperuser")
        else:
            print("\n❌ Migration failed. Check your database connection.")
    
    else:
        print("Setup cancelled.")

if __name__ == '__main__':
    main()
