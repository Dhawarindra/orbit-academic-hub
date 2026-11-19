"""Run the local development server with python -m orbit."""

from . import create_app


def main() -> None:
    try:
        app = create_app()
    except (ValueError, OSError) as error:
        raise SystemExit(f"Orbit startup failed: {error}") from error

    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=False,
        use_reloader=False,
        load_dotenv=False,
    )


if __name__ == "__main__":
    main()
