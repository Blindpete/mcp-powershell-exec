from mcp.server.fastmcp import FastMCP
import subprocess
import shutil

# Initialize the MCP server
mcp = FastMCP("powershell-integration")

# Determine which PowerShell version to use
powershell_cmd = "pwsh" if shutil.which("pwsh") else "powershell"

# Define the command to run PowerShell code
@mcp.tool()
def run_powershell(code: str) -> str:
    """Runs PowerShell code and returns the output."""
    # Run the PowerShell command using the determined executable
    process = subprocess.Popen(
        [powershell_cmd, "-NonInteractive","-NoLogo", "-Command", code],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Get the output and error messages
    output, error = process.communicate()

    if process.returncode != 0:
        return f"Error: {error}"

    return output

if __name__ == "__main__":
    
    # Run the MCP server
    mcp.run()
