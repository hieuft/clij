import typer
from .commands import auto_detect_info, start

# 1. Initialize the app
app = typer.Typer()

app.command()(auto_detect_info.auto_detect_info)
app.command()(start.start)

# 2. Define the command using the @app.command() decorator
@app.command()
def list_users():
    """
    List all users in the system.
    """
    print("Listing users...")

# 3. Keep the callback simple (or remove it entirely if not needed)
@app.callback()
def main():
    """
    Manage users in the local judge system.
    """
    pass

# 4. Standard entry point
if __name__ == "__main__":
    app()
