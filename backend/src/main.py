import sys
from LimitCalculator import LimitCalculator
from WebApp import LimitWebApp


def main():
    try:
        calc_instance = LimitCalculator()
        web_app = LimitWebApp(calculator=calc_instance)

        web_app.run(host='0.0.0.0', port=5000, debug=True)

    except ImportError as e:
        print(f"Error: Failed to import modules. {e}", file=sys.stderr)
        print("Please ensure LimitCalculator.py and WebApp.py are in the 'src' directory.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
