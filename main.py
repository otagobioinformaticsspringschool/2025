import os

def define_env(env):
    """Define macros and filters."""
    
    @env.macro
    def include_all(directory):
        """Includes all markdown files from a given directory."""
        dir_path = os.path.join(env.conf['docs_dir'], directory)
        if not os.path.isdir(dir_path):
            return f"<!-- Directory '{directory}' not found -->"

        output = []
        for filename in sorted(os.listdir(dir_path)):  # Sort to maintain order
            if filename.endswith(".md"):
                with open(os.path.join(dir_path, filename), "r", encoding="utf-8") as f:
                    output.append(f.read())
        
        return "\n\n".join(output)  # Join content with spacing
    
    @env.macro
    def include_md(md_file):
        """Includes all markdown files from a given directory."""
        filename = os.path.join(env.conf['docs_dir'], md_file)
        if not os.path.isfile(filename):
            return f"<!-- File '{md_file}' not found -->"

        output = []
        if filename.endswith(".md"):
            with open(filename, "r", encoding="utf-8") as f:
                output.append(f.read())
        
        return "\n\n".join(output)  # Join content with spacing