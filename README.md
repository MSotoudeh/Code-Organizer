# Code-Organizer

Welcome to **Code Organizer**, a powerful and efficient tool designed to help developers structure and manage their code repositories with ease. This project parses a single input file containing multiple code snippets, each associated with specific file paths, and organizes them into a well-structured directory tree. Impress your team and streamline your workflow by automating code organization!

![Code Organizer](assets/code-organizer-banner.png)

## Features

- **Automated Directory Creation**: Automatically creates directories and files based on specified paths.
- **Code Segregation**: Segregates code snippets into the appropriate files, removing path lines for clean code integration.
- **Ease of Use**: Simple setup and execution process.
- **Highly Customizable**: Easily adaptable to various project structures and requirements.

## Getting Started

Follow these steps to get your Code Organizer up and running:

### Prerequisites

- Python 3.x
- Git

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/MSotoudeh/code-organizer.git
    cd code-organizer
    ```

2. **Install Dependencies**

    No external dependencies required.

### Usage

1. **Prepare Your Input File**

    Edit the `data/input_code.txt` file to include your code snippets and their respective paths. Example:

    ```plaintext
    /project/src/app/main.py
    import os

    def main():
        print("Main function in main.py")

    if __name__ == "__main__":
        main()
    /project/src/app/utils/helpers.py
    def greet(name):
        return f"Hello, {name}!"

    def farewell(name):
        return f"Goodbye, {name}."
    ```

2. **Run the Organizer**

    Execute the `main.py` script to organize your code:

    ```bash
    python main.py
    ```

    This will create the necessary directories and files, organizing your code as specified in `data/input_code.txt`.

### Example Output

After running the script, your repository structure will look like this:

```plaintext
output_repo/
├── project/
│ ├── src/
│ │ └── app/
│ │ ├── main.py
│ │ └── utils/
│ │ └── helpers.py
│ ├── tests/
│ │ └── test_helpers.py
│ └── README.md
```

### Contributing

We welcome contributions! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any inquiries, please reach out to:

- **M. Sotoudeh**: [m.sotoude@e.email](mailto:m.sotoude@e.email)
- **GitHub**: [MSotoudeh](https://github.com/MSotoudeh)

---

Thank you for using **Code Organizer**! Happy coding!

![Code Organizer](assets/code-organizer-footer.png)
