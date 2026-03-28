# A static site generator

A lightweight static site generator build from scratch in Python. It converts Markdown content into a fully styled HTML website using a single template with support for Github Pages deployment.

**[Live Demo](https://ben-dev-su.github.io/static-site-generator/)**

## How it works 

The generator takes Markdown files from the `content/` directory, converts them to HTML using a custom Markdown parser, injects the result into the `template.html` file, and copies assets from `static/` together with the output to `docs/` directory. 

```
content/            ->  Markdown source files
static/             ->  Images, CSS, and other assets
template.html       ->  Template file
  -> generator.py   ->  Parses Markdown to HTML, inject into template
docs/               ->  Final static site to serve/deploy
```

## Project Structure

```
.
├── content/                 ->  Markdown source files
├── docs/                    ->  Final generated content to be served/deploy
├── src/                     ->  Source Code
│   ├── copystatic.py
│   ├── generator.py
│   ├── htmlnode.py
│   ├── inline_markdown.py
│   ├── main.py
│   ├── markdown_blocks.py
│   └── textnode.py
├── static/                  ->   Static assets to be copied to the output
├── build.sh                 ->   Production build for Github Pages "basepath"
├── main.sh                  ->   Local Development: build + server localhost:8888
├── template.html            ->   HTML template to be inected with static site {{ title }} and {{ content }} 
└── test.sh                  ->   Unit test
```

## Getting started

### Prerequisites

- Python3

### Local Development

Build site and start server on port 8888 with:

```bash
./main.sh
```

Be sure you can execute the file `chmod 744 ./main.sh`.

Then open [http://localhost:8888](http://localhost:8888) in your browser.

### Production build

It's intendet to be deployed on GitHub Pages!
You need to change the `basepath` in the `build.sh` file to deploy to GitHub Pages.

```bash
./build.sh
```

Be sure you can execute the file `chmod 744 ./build.sh`.

This runs the generator with "/static-site-generator/" as the `basepath`


## Adding Content
 
1. Create a new Markdown file under `content/`. Each page should live in its own folder as `index.md`:
 
   ```
   content/blog/my-new-post/index.md
   ```
 
2. Start the file with an `h1` heading — this becomes the page title:
 
   ```markdown
   # My New Blog Post
 
   New content here
   ```
 
3. Run the build:
 
   ```bash
   ./main.sh
   ```
 
The generator recursively converts every `.md` file in `content/` to an `.html` file and copies directory structure together with every file in the output directory.
 
## Supported Markdown Features
 
The custom parser handles the following syntax:
 
- **Headings** (`# h1` through `###### h6`)
- **Paragraphs**
- **Bold** (`**boldtext**`)
- **Italic** (`_italictext_`) 
- **Links** (`[text](url)`)
- **Images** (`![alt](src)`)
- **Inline code** (`code`)
- **Code blocks** (fenced with triple backticks)
- **Blockquotes** (`> quote`)
- **Ordered lists** (`1. item`)
- **Unordered lists** (`- item` or `* item`)
 
## Running Tests
 
```bash
./test.sh
```
 
