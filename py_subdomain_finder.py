import subprocess
import argparse
import os

def enumerate_subdomains(domain, output_file, verbose):
    try:
        if verbose:
            print(f"Enumerating subdomains for: {domain}")
        
        # Call Sublist3r to enumerate subdomains
        result = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            output = result.stdout
            if verbose:
                print(f"Subdomains for {domain}:")
                print(output)
            
            # Save the output to a text file
            with open(output_file, "w") as file:
                file.write(output)
                
            if verbose:
                print(f"Subdomains have been saved to {output_file}")
        else:
            print(f"Error occurred while running sublist3r: {result.stderr}")
    
    except FileNotFoundError:
        print("Sublist3r is not installed or not found in the system PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Script")
    parser.add_argument("domain", nargs='?', help="The domain to enumerate subdomains for")
    parser.add_argument("-o", "--output", help="The output file to save the subdomains", default="subdomains.txt")
    parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
    
    args = parser.parse_args()

    # If domain is not provided, prompt the user for input
    if not args.domain:
        args.domain = input("Enter the domain to enumerate subdomains: ")

    # If output file is not provided, use the default or prompt the user
    if args.output == "subdomains.txt":
        user_output = input(f"Enter the output file name (default: {args.output}): ")
        if user_output.strip():
            args.output = user_output

    # Ensure output file has the correct extension
    if not args.output.endswith(".txt"):
        args.output += ".txt"
    
    enumerate_subdomains(args.domain, args.output, args.verbose)

if __name__ == "__main__":
    main()

