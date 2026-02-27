#!/usr/bin/env python3
"""
Gumroad Automation - Creates/updates products via browser automation

This script generates browser action workflows for Claude Code to execute
via Playwright MCP or superpowers-chrome.

Usage:
    python gumroad_automation.py generate-workflow <product-config.json>
    python gumroad_automation.py list-actions

Integration:
    1. Run this script to generate workflow
    2. Execute workflow via Claude Code with Playwright MCP
    3. Script generates step-by-step browser actions

Example product config:
{
    "name": "Content Empire Pro",
    "description": "50+ premium Claude Code skills for content creators",
    "price": 97,
    "cover_image": "/path/to/cover.png",
    "files": ["/path/to/content-empire-pro.zip"]
}
"""
import json
import sys
from pathlib import Path
from datetime import datetime

class GumroadAutomation:
    """Automate Gumroad product management via browser."""

    def __init__(self):
        self.base_url = "https://app.gumroad.com"

    def navigate(self, url: str) -> dict:
        """Navigate to URL."""
        return {
            "action": "navigate",
            "payload": url,
            "description": f"Navigate to {url}"
        }

    def wait_for(self, selector: str, timeout: int = 10000) -> dict:
        """Wait for element."""
        return {
            "action": "await_element",
            "selector": selector,
            "timeout": timeout,
            "description": f"Wait for element: {selector}"
        }

    def type_text(self, selector: str, text: str) -> dict:
        """Type into field."""
        return {
            "action": "type",
            "selector": selector,
            "payload": text,
            "description": f"Type into {selector}"
        }

    def click(self, selector: str) -> dict:
        """Click element."""
        return {
            "action": "click",
            "selector": selector,
            "description": f"Click: {selector}"
        }

    def upload_file(self, selector: str, file_path: str) -> dict:
        """Upload file."""
        return {
            "action": "upload",
            "selector": selector,
            "file_path": file_path,
            "description": f"Upload file: {file_path}"
        }

    def create_product_actions(self, config: dict) -> list:
        """Generate actions to create a Gumroad product."""
        name = config.get("name", "New Product")
        description = config.get("description", "")
        price = config.get("price", 0)

        actions = [
            self.navigate(f"{self.base_url}/products/new"),
            self.wait_for("input[name='name']"),
            self.type_text("input[name='name']", name),
            self.type_text("textarea[name='description']", description),
            self.type_text("input[name='price']", str(price)),
        ]

        # Add cover image if provided
        if "cover_image" in config:
            actions.append(
                self.upload_file("input[type='file']", config["cover_image"])
            )

        # Submit and wait for confirmation
        actions.extend([
            self.click("button[type='submit']"),
            self.wait_for(".product-created, .success-message", timeout=15000)
        ])

        return actions

    def update_product_actions(self, product_id: str, config: dict) -> list:
        """Generate actions to update existing product."""
        actions = [
            self.navigate(f"{self.base_url}/products/{product_id}/edit"),
            self.wait_for("input[name='name']"),
        ]

        if "name" in config:
            actions.append(self.type_text("input[name='name']", config["name"]))
        if "description" in config:
            actions.append(self.type_text("textarea[name='description']", config["description"]))
        if "price" in config:
            actions.append(self.type_text("input[name='price']", str(config["price"])))

        actions.extend([
            self.click("button[type='submit']"),
            self.wait_for(".success-message", timeout=10000)
        ])

        return actions

    def generate_workflow(self, config: dict, action_type: str = "create") -> str:
        """Generate Claude Code workflow for product management."""
        if action_type == "create":
            actions = self.create_product_actions(config)
        elif action_type == "update":
            actions = self.update_product_actions(config.get("product_id", ""), config)
        else:
            raise ValueError(f"Unknown action type: {action_type}")

        workflow = f"# Gumroad Product {action_type.title()} Workflow\n\n"
        workflow += f"Generated: {datetime.now().isoformat()}\n\n"
        workflow += "Execute these browser actions in sequence using Playwright MCP:\n\n"

        for i, action in enumerate(actions, 1):
            workflow += f"## Step {i}: {action['description']}\n"
            workflow += f"```json\n{json.dumps(action, indent=2)}\n```\n\n"

        return workflow

    def generate_claude_prompt(self, config: dict) -> str:
        """Generate a prompt for Claude Code to execute."""
        return f"""Execute this Gumroad product creation workflow:

1. Navigate to {self.base_url}/products/new
2. Fill in product name: "{config.get('name', 'Product')}"
3. Fill in description: "{config.get('description', '')[:100]}..."
4. Set price: ${config.get('price', 0)}
5. Upload cover image if available
6. Click submit
7. Confirm product was created successfully

Use the Playwright MCP tools (playwright_navigate, playwright_fill, playwright_click).
Report back the product URL when complete."""


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python gumroad_automation.py generate-workflow <config.json>")
        print("  python gumroad_automation.py generate-prompt <config.json>")
        print("  python gumroad_automation.py example-config")
        sys.exit(1)

    command = sys.argv[1]
    auto = GumroadAutomation()

    if command == "generate-workflow":
        if len(sys.argv) < 3:
            print("Error: Please provide config.json path")
            sys.exit(1)
        config = json.loads(Path(sys.argv[2]).read_text())
        print(auto.generate_workflow(config))

    elif command == "generate-prompt":
        if len(sys.argv) < 3:
            print("Error: Please provide config.json path")
            sys.exit(1)
        config = json.loads(Path(sys.argv[2]).read_text())
        print(auto.generate_claude_prompt(config))

    elif command == "example-config":
        example = {
            "name": "Content Empire Pro",
            "description": "50+ premium Claude Code skills for content creators, marketers, and developers. Includes YouTube scripts, blog writers, product descriptions, and more.",
            "price": 97,
            "cover_image": "/home/r3d3y3s77/projects/joseph-skills/assets/cover.png",
            "files": ["/home/r3d3y3s77/projects/joseph-skills/dist/content-empire-pro.zip"]
        }
        print(json.dumps(example, indent=2))

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
